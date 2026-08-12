#!/usr/bin/env python3
"""Four checks for `h1-mean-value.md` (work item mg-8462).  Needs `mpmath`; no numpy.

H1 (`prolate-rate.md` §6(c), `paper/positivity-obstruction.tex` Hypothesis H1) is
the mean-value bound

    sum_{1/2 + is in Z} |F_mu r(s)|^2  <=  Theta(lambda) ||r||^2,   Theta subexponential,

for the spill r = E(phi)|_(0,1/lambda).  The note reduces it, unconditionally on
the zeta side, to a statement with no zeros in it: a weighted-L^2 tail bound for

    G(t) = sum_{n>=1} Phi(n t),      t > 1,

where Phi is the ENTIRE extension of the prolate function, normalised by
int_{-1}^{1} Phi^2 = 1.  The note's hypothesis is

    (P)    sup_{t>1} t |G(t)| <= K(c) |Phi(1)|,   K subexponential,

and what this script measures is the SINGLE-TERM statement behind it,

    (P_1)  |Phi_n(x)| <= K_1(c) |Phi_n(1)| / x    for x >= 1.

(P_1) does not imply (P) by the triangle inequality -- that sum diverges
logarithmically, and the cancellation is the sawtooth of note §4.  The passage
from (P_1) to (P) is note §9 item Q2 and is NOT tested here.

This script tests the two halves of (P_1) and the identity that calibrates it.
Nothing here is evidence for H1 itself: H1 quantifies over all mu and no
computation can reach it.  What is tested is (i) an identity, (ii) a lemma
proved in the note, and (iii) the size of the constant the lemma does not give.

CHECK 0 -- the entire extension, validated before it is used.  Phi(x) for x
           outside [-1,1] is computed from the finite-Fourier-transform relation
           int_{-1}^1 Phi(y) e^{icxy} dy = mu Phi(x) as an exact spherical-Bessel
           series, and checked against the Legendre series at x = 0 and x = 1,
           where the two must agree.  The Bessel values themselves come from a
           downward (Miller) recurrence started ABOVE c*x -- started below it the
           recurrence silently returns wrong values, which is how the first draft
           of this script produced a sup that was off by two orders of magnitude.

CHECK 1 -- the endpoint identity, OBSERVED, not proved:

               Phi_n(1)^2 = c (1 - Lambda_n) (1 - (2n+1)/(4c) + O(c^-2)).

           This is what converts the exact L^2 identity
           int_{|x|>1} |Phi_n|^2 = (1 - Lambda_n)/Lambda_n  (proved in the note,
           §4) into the endpoint normalisation that (P) and (P_1) are stated
           against.  It is what distinguishes K = O(1) from K = O(e^{c}), and
           only the first buys anything: that is the whole question.

CHECK 2 -- the amplitude lemma (note §5.1), PROVED there, verified here:
           if chi_n < c^2 then |Phi_n(x)| <= |Phi_n(1)| for all x >= 1.
           chi_n < c^2 is checked too: it is what fails in the regime the
           published off-band results (Osipov-Rokhlin, arXiv:1208.4816) cover.

CHECK 3 -- the constant the lemma does NOT give: sup_{x>1} x |Phi(x)| / |Phi(1)|,
           i.e. the K_1 of (P_1), tabulated against c.  If K_1 grew like e^{c}
           the reduction would be worthless; the note's claim is only that it is
           observed to be below 1 over the range computed, which is not a proof
           and is labelled as such.

Working precision is 60 decimal digits by default (CHECK 1 uses 200).  Phi(1) is
of order 1e-16 at c = 2 pi * 8 and is obtained as a sum of terms of order 1, so
roughly 16 digits are lost to cancellation before anything is printed; CHECK 0
reports the residual so the loss is visible rather than assumed.

Runtime ~12 minutes at the defaults; `--quick` cuts it to about two.
"""

import sys
import mpmath as mp
import verify_prolate_rate as VP

QUICK = "--quick" in sys.argv


# --- the entire extension of a prolate function -------------------------------


def sph_j_all(z, kmax, extra=200):
    """[j_0(z), ..., j_kmax(z)] by Miller downward recurrence.

    Two traps, both of which produced wrong answers in earlier drafts of this
    script and neither of which announces itself:

    * the recurrence j_{k-1} = (2k+1)/z j_k - j_{k+1} is stable downwards but
      must be STARTED ABOVE z, not merely above kmax;
    * it must NOT be normalised on j_0(z) = sin(z)/z.  Here z = c x with
      c = 2 pi mu, so z is near a multiple of pi exactly when x is near an
      integer, and there j_0 is near zero: dividing by it is ill-conditioned and
      corrupts every j_k by an absolute error that then survives the 13-digit
      cancellation in the Phi sum.  At c = 2 pi * 5, x = 1 that route returns
      Phi(1) too large by 36%.

    The normalisation used instead is the sum rule sum_k (2k+1) j_k(z)^2 = 1,
    which is never singular; the sign is then fixed against sin(z)/z.
    """
    top = int(mp.floor(z)) + kmax + extra
    jp1, jk = mp.mpf(0), mp.mpf(1)
    out = [None] * (top + 1)
    out[top] = jk
    big = mp.mpf(2) ** 200
    sc = mp.mpf(2) ** -200
    for k in range(top, 0, -1):
        jm1 = (2 * k + 1) / z * jk - jp1
        out[k - 1] = jm1
        jp1, jk = jk, jm1
        if abs(jk) > big:
            for i in range(k - 1, top + 1):
                out[i] *= sc
            jp1 *= sc
            jk *= sc
    scale = 1 / mp.sqrt(sum((2 * k + 1) * out[k] ** 2 for k in range(top + 1)))
    if (out[0] * scale) * (mp.sin(z) / z) < 0:
        scale = -scale
    return [out[i] * scale for i in range(kmax + 1)]


def bessel_coeffs(betas, mu, kmax):
    """Coefficients a_k with Phi(x) = sum_k a_k j_k(c x), k even.

    From int_{-1}^1 P_k(y) e^{izy} dy = 2 i^k j_k(z) and Pbar_k = sqrt((2k+1)/2)
    P_k, applied to int_{-1}^1 Phi(y) e^{icxy} dy = mu Phi(x).
    """
    out = {}
    for i, b in enumerate(betas):
        k = 2 * i
        if k > kmax:
            break
        out[k] = b * mp.sqrt(mp.mpf(2 * k + 1) / 2) * 2 * mp.mpf(-1) ** (k // 2) / mu
    return out


def legendre_trunc(betas, tol):
    """Largest even Legendre index whose coefficient still matters."""
    kmax = 0
    for i, v in enumerate(betas):
        if abs(v) > tol:
            kmax = 2 * i
    return kmax


def prolate_data(c, jmax=2):
    """[(n, Lambda_n, chi_n, mu_n, Phi_n(1), betas)] for n = 0, 2, ..., 2 jmax."""
    chis, betas, P0 = VP.prolate_even(c, jmax=jmax)
    out = []
    for j in range(jmax + 1):
        b = betas[j]
        integ = b[0] * mp.sqrt(mp.mpf(2))
        val0 = sum(b[i] * P0[i] for i in range(len(b)))
        mu = integ / val0
        lam = c / (2 * mp.pi) * mu * mu
        p1 = sum(b[i] * mp.sqrt(mp.mpf(4 * i + 1) / 2) for i in range(len(b)))
        out.append((2 * j, lam, chis[j], mu, p1, b))
    return out


# --- CHECK 0 -------------------------------------------------------------------


def check0():
    print("\nCHECK 0 -- the entire extension, validated where a second method exists")
    print("The Bessel series and the Legendre series are independent computations")
    print("of the same function; off [-1,1] only the first is available, so it is")
    print("pinned at x = 1, where both are.  Two further columns: the same value")
    print("with the recurrence started 200 indices higher (stability), and with the")
    print("ill-conditioned j_0 normalisation instead of the sum rule -- the latter")
    print("is what an earlier draft of this script used, and it is wrong by O(1).\n")
    mp.mp.dps = 60
    print("  c          n   |Phi(1)|        rel.err at x=1   rel.err, extra=400   "
          "rel.err, j_0 normalisation")
    for cv in ([2 * mp.pi * 5] if QUICK else [2 * mp.pi * 3, 2 * mp.pi * 5, 2 * mp.pi * 8]):
        c = mp.mpf(cv)
        for (n, lam, chi, mu, p1, b) in prolate_data(c):
            kmax = legendre_trunc(b, mp.mpf(10) ** -50)
            a = bessel_coeffs(b, mu, kmax)
            v1 = sum(ak * sph_j_all(c, kmax)[k] for k, ak in a.items())
            v2 = sum(ak * sph_j_all(c, kmax, extra=400)[k] for k, ak in a.items())
            # the same evaluation normalised on j_0, which is near zero here
            top = int(mp.floor(c)) + kmax + 200
            jp1, jk = mp.mpf(0), mp.mpf(1)
            bad = [None] * (top + 1)
            bad[top] = jk
            big, sc = mp.mpf(2) ** 200, mp.mpf(2) ** -200
            for k in range(top, 0, -1):
                jm1 = (2 * k + 1) / c * jk - jp1
                bad[k - 1] = jm1
                jp1, jk = jk, jm1
                if abs(jk) > big:
                    for i in range(k - 1, top + 1):
                        bad[i] *= sc
                    jp1 *= sc
                    jk *= sc
            s0 = (mp.sin(c) / c) / bad[0]
            vbad = sum(ak * bad[k] * s0 for k, ak in a.items())
            print("  %-10s %-3d %-15s %-16s %-20s %s"
                  % (mp.nstr(c, 7), n, mp.nstr(abs(p1), 6),
                     mp.nstr(abs(v1 / p1 - 1), 3), mp.nstr(abs(v2 / p1 - 1), 3),
                     mp.nstr(abs(vbad / p1 - 1), 3)))


# --- CHECK 1 -------------------------------------------------------------------


def check1():
    print("\nCHECK 1 -- the endpoint identity  Phi_n(1)^2 = c (1-Lambda_n) (1 - (2n+1)/(4c) + ...)")
    print("OBSERVED.  Columns: the raw ratio, then the residual (1 - ratio) * c,")
    print("which the identity predicts converges to (2n+1)/4 = 0.25, 1.25, 2.25.\n")
    print("  c            n   1-Lambda_n         Phi_n(1)^2         "
          "ratio                (1-ratio)*c   (2n+1)/4")
    cs = [mp.mpf(10), 2 * mp.pi * 5, 2 * mp.pi * 12] if QUICK else \
         [mp.mpf(5), mp.mpf(10), 2 * mp.pi * 3, 2 * mp.pi * 5, 2 * mp.pi * 8,
          2 * mp.pi * 12, mp.mpf(120), mp.mpf(200), mp.mpf(320)]
    for cv in cs:
        mp.mp.dps = 200 if cv < 130 else 320
        c = mp.mpf(cv)
        for (n, lam, chi, mu, p1, b) in prolate_data(c):
            d = 1 - lam
            ratio = p1 ** 2 / (c * d)
            print("  %-12s %-3d %-18s %-18s %-20s %-13s %s"
                  % (mp.nstr(c, 7), n, mp.nstr(d, 8), mp.nstr(p1 ** 2, 8),
                     mp.nstr(ratio, 12), mp.nstr((1 - ratio) * c, 6),
                     mp.nstr(mp.mpf(2 * n + 1) / 4, 4)))
    mp.mp.dps = 60


# --- CHECKS 2 and 3 ------------------------------------------------------------


def scan(c, xmax, step, jmax=2):
    """sup |Phi_n(x)| and sup x|Phi_n(x)| over 1 < x <= xmax, all n at once."""
    data = prolate_data(c, jmax)
    coeffs, kmaxes = [], []
    for (n, lam, chi, mu, p1, b) in data:
        km = legendre_trunc(b, mp.mpf(10) ** -50)
        kmaxes.append(km)
        coeffs.append(bessel_coeffs(b, mu, km))
    kmax = max(kmaxes)
    sup_a = [mp.mpf(0)] * len(data)
    sup_x = [mp.mpf(0)] * len(data)
    at_x = [None] * len(data)
    x = mp.mpf(1) + step                         # strictly inside (1, xmax]
    while x <= xmax:
        js = sph_j_all(c * x, kmax)              # one Bessel array serves every n
        for i, a in enumerate(coeffs):
            v = abs(sum(ak * js[k] for k, ak in a.items()))
            if v > sup_a[i]:
                sup_a[i] = v
            if x * v > sup_x[i]:
                sup_x[i], at_x[i] = x * v, x
        x += step
    return data, sup_a, sup_x, at_x


def checks23():
    mp.mp.dps = 60
    xmax = mp.mpf(8) if QUICK else mp.mpf(14)
    step = mp.mpf('0.02') if QUICK else mp.mpf('0.008')
    print("\nCHECK 2 -- the amplitude lemma:  chi_n < c^2  implies  |Phi_n(x)| <= |Phi_n(1)|, x >= 1")
    print("CHECK 3 -- the constant the lemma does not give:  K = sup_{x>1} x|Phi_n(x)|/|Phi_n(1)|")
    print("Scanned STRICTLY inside 1 < x <= %s in steps of %s, so neither column"
          % (mp.nstr(xmax, 4), mp.nstr(step, 3)))
    print("is the endpoint value by construction.  A grid can only UNDER-report a")
    print("sup, so CHECK 2 passing on a grid is weaker than the lemma it illustrates;")
    print("the lemma is what is relied on.  K is reported, not bounded: the note")
    print("does NOT claim K = 1 is proved, only that it is what is observed here.\n")
    print("  c          n   chi_n/c^2   chi<c^2   sup|Phi|/|Phi(1)|   K = sup x|Phi|/|Phi(1)|   at x")
    for cv in ([2 * mp.pi * 5] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3,
                                              2 * mp.pi * 5, 2 * mp.pi * 8]):
        c = mp.mpf(cv)
        data, sup_a, sup_x, at_x = scan(c, xmax, step)
        for i, (n, lam, chi, mu, p1, b) in enumerate(data):
            print("  %-10s %-3d %-11s %-9s %-19s %-24s %s"
                  % (mp.nstr(c, 7), n, mp.nstr(chi / c ** 2, 4),
                     "yes" if chi < c ** 2 else "NO",
                     mp.nstr(sup_a[i] / abs(p1), 8),
                     mp.nstr(sup_x[i] / abs(p1), 8), mp.nstr(at_x[i], 5)))


if __name__ == "__main__":
    print(__doc__.split("CHECK 0")[0].rstrip())
    check0()
    check1()
    checks23()
    print("\ndone.")
