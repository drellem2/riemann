#!/usr/bin/env python3
"""Six checks for `prolate-rate.md` (work item mg-fcb8).  Needs `mpmath`; no numpy.

The question (mg-7606 §9, item T2): is the smallest eigenvalue s(mu) of the even
semi-local Weil matrix genuinely governed by a prolate concentration defect, and
if so which one?  `deficit-repair.md` §5 predicted the decay *rate* 4 pi from the
index-0 Slepian/Fuchs asymptotic 1 - Lambda_0(c) ~ 4 sqrt(pi c) e^{-2c} at
c = 2 pi mu, and matched it to a fit, A = 5.4635 +- 0.052 against
4 pi / log 10 = 5.4575.  This script tests the *identification*, not the rate.

The answer is that the index is wrong and the conclusion is right.  The vector
that realises the smallest eigenvalue of the EVEN matrix is Connes-Consani's
phi_2 = psi_2 psi_0(0) - psi_0 psi_2(0)  (`Spectraltriples.tex:751`), and their
psi_m is PS_{2m,0}, so phi_2 is built from prolate index **4**, not index 0.
The governing defect is therefore 1 - chi_2 = 1 - sqrt(Lambda_4(2 pi mu)).

    against 1 - Lambda_0 :  s/(1-Lambda_0)  =  5.0e8 ... 2.8e10, growing 56x
    against 1 - chi_2    :  s/(1-chi_2)     =  7.7   ... 11.2 , growing 1.5x
                            and after extrapolating the truncation bias away,
                            7.1 ... 9.2, a residual growth no faster than log mu.

None of the index-4 identification is new to this repository.  `semilocal-gap.md`
§5.2 (mg-03f0) already quotes Connes' asymptotic and states that his chi_2 is
prolate index 4, the corpus's chi_4; §5.3 closes `citation-audit.md` item U4 on
the general-n Fuchs constant against it.  `deficit-repair.md` was written two
commits later, cites `semilocal-gap.md` in its first paragraph, and its §5 still
used the index-0 form from `s3-reduction-audit.md`.  What is new here is the
quantitative confrontation -- Connes reports the resemblance as a figure with no
constant -- and the observation that the RATE alone could never have settled it.

CHECK 0 -- the prolate apparatus, validated before it is used for anything.
CHECK 1 -- Fuchs' asymptotic at general index, verified; and Connes' printed
           constant 2^14 sqrt2 pi^5 / 3 identified as (1/2) Fuchs_4 at c=2 pi mu.
CHECK 2 -- the confrontation: s(mu) against 1 - Lambda_0 and against 1 - chi_2.
CHECK 3 -- the truncation bias, measured rather than asserted.
CHECK 4 -- the three-parameter, zero-free-parameter residual test.
CHECK 5 -- stability of the prolate defects in working precision and in the
           Legendre truncation, and against a second, independent eigensolver.

Runtime ~40 minutes at the defaults; `--quick` cuts it to about five.

--- WHY THE RATE CANNOT DISCRIMINATE ------------------------------------------

Fuchs' asymptotic at index n (Fuchs 1964, Thm 1; the form Connes cites at
`rhready.tex:1149`) is

    1 - Lambda_n(c)  ~  4 sqrt(pi) 8^n c^{n + 1/2} e^{-2c} / n!

The exponential factor e^{-2c} does NOT depend on n.  At c = 2 pi mu every index
gives the same rate 2c/mu = 4 pi.  So the 0.12-sigma agreement of
`deficit-repair.md` §5 is passed by every prolate index equally, and is much
weaker evidence for the identification than it looks.  What discriminates is the
POWER n + 1/2 and the CONSTANT, and those are what this script tests.

--- PROLATE COMPUTATION -------------------------------------------------------

Legendre-coefficient method.  With psi(x) = sum_k beta_k Pbar_k(x) the prolate
differential equation ((1-x^2) psi')' + (chi - c^2 x^2) psi = 0 is symmetric
tridiagonal in the even Legendre indices.  Its eigenvalues chi_n are WELL
SEPARATED -- that is the whole point of the Bell Labs commuting operator -- so
the eigenvectors are obtained stably even though the concentration eigenvalues
Lambda_n differ from 1 by as little as 1e-55.  Then

    Lambda_n = (c/2pi) mu_n^2,   mu_n = (int_{-1}^1 psi_n) / psi_n(0)  (n even)

from int_{-1}^1 psi_n(y) e^{i c x y} dy = mu_n psi_n(x) at x = 0.  Diagonalising
the concentration operator P_lambda Phat_lambda P_lambda directly would be
hopeless here: its top eigenvalues agree to 55 decimal places.
"""

import sys
import mpmath as mp
import verify_deficit_repair as V
from verdict import Verdict

QUICK = "--quick" in sys.argv

# The exit-code contract (mg-5995).  Wired: CHECK 0's tabulated value and its
# second eigensolver, CHECK 1's identification of Connes' constant with Fuchs',
# CHECK 4's "all within one standard error", and CHECK 5's "no movement".
# CHECK 2 reports ratios and CHECK 3 reports a fit that is allowed to refuse
# (`(not geometric)` at mu = 6 and 9 is documented, not a failure) -- so the
# extrapolation column is deliberately left ungated.
VD = Verdict()

# s(mu) is recomputed by this script; nothing below is copied from a note.

# --- prolate spheroidal apparatus ---------------------------------------------


def _tri(c, K):
    """(a, b): the prolate operator on even Legendre indices k = 0,2,...,2K-2."""
    c2 = c * c
    a, b = [], []
    for i in range(K):
        k = 2 * i
        a.append(mp.mpf(k * (k + 1))
                 + c2 * mp.mpf(2 * k * (k + 1) - 1) / mp.mpf((2 * k + 3) * (2 * k - 1)))
        if i + 1 < K:
            b.append(c2 * mp.mpf((k + 2) * (k + 1))
                     / (mp.mpf(2 * k + 3) * mp.sqrt(mp.mpf((2 * k + 1) * (2 * k + 5)))))
    return a, b


def _sturm(a, b, x):
    """Number of eigenvalues of the tridiagonal matrix strictly below x."""
    tiny = mp.mpf(2) ** (-mp.mp.prec + 20)
    cnt = 0
    d = a[0] - x
    if d < 0:
        cnt += 1
    for i in range(1, len(a)):
        if d == 0:
            d = tiny
        d = a[i] - x - b[i - 1] * b[i - 1] / d
        if d < 0:
            cnt += 1
    return cnt


def _eig_bisect(a, b, j):
    """j-th smallest eigenvalue (0-based) by bisection on the Sturm count."""
    lo = min(a) - 2 * max(abs(x) for x in b) - 1
    hi = max(a) + 2 * max(abs(x) for x in b) + 1
    tol = (hi - lo) * mp.mpf(2) ** (-mp.mp.prec + 8)
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if _sturm(a, b, mid) > j:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def _tri_solve(a, b, shift, rhs):
    """(T - shift I) x = rhs for symmetric tridiagonal T."""
    n = len(a)
    tiny = mp.mpf(2) ** (-mp.mp.prec + 20)
    d = [mp.mpf(0)] * n
    y = [mp.mpf(0)] * n
    d[0] = a[0] - shift or tiny
    y[0] = rhs[0]
    for i in range(1, n):
        m = b[i - 1] / d[i - 1]
        d[i] = a[i] - shift - m * b[i - 1]
        if d[i] == 0:
            d[i] = tiny
        y[i] = rhs[i] - m * y[i - 1]
    x = [mp.mpf(0)] * n
    x[n - 1] = y[n - 1] / d[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - b[i] * x[i + 1]) / d[i]
    return x


def _P_at_zero(K):
    """Pbar_k(0) = sqrt((2k+1)/2) P_k(0), even k = 0,2,...,2K-2."""
    out, p = [], mp.mpf(1)
    for i in range(K):
        k = 2 * i
        out.append(p * mp.sqrt(mp.mpf(2 * k + 1) / 2))
        p = -p * mp.mpf(k + 1) / mp.mpf(k + 2)
    return out


_CACHE = {}


def prolate_even(c, jmax=2, K=None):
    """(chis, betas, Pbar(0)) for PS_{0,0}, PS_{2,0}, ..., PS_{2 jmax, 0}.

    betas[j] is normalised to sum(beta^2) = 1, i.e. int_{-1}^1 psi^2 = 1, and
    the sign is fixed by psi_j(0) > 0.
    """
    if K is None:
        K = int(c) + 90
    key = (mp.mp.prec, mp.nstr(c, 30), K, jmax)
    if key in _CACHE:
        return _CACHE[key]
    a, b = _tri(c, K)
    P0 = _P_at_zero(K)
    chis, betas = [], []
    for j in range(jmax + 1):
        chi = _eig_bisect(a, b, j)
        v = [mp.mpf(1) / (i + 1) for i in range(K)]
        for _ in range(3):                      # inverse iteration on the shift
            v = _tri_solve(a, b, chi, v)
            nrm = mp.sqrt(sum(x * x for x in v))
            v = [x / nrm for x in v]
        if sum(v[i] * P0[i] for i in range(K)) < 0:
            v = [-x for x in v]
        chis.append(chi)
        betas.append(v)
    _CACHE[key] = (chis, betas, P0)
    return _CACHE[key]


def Lambda_even(c, jmax=2, K=None):
    """[(n, Lambda_n(c))] for n = 0, 2, ..., 2 jmax."""
    chis, betas, P0 = prolate_even(c, jmax, K)
    out = []
    for j, b in enumerate(betas):
        integ = b[0] * mp.sqrt(mp.mpf(2))       # int_{-1}^1 psi = beta_0 sqrt 2
        val0 = sum(b[i] * P0[i] for i in range(len(b)))
        m = integ / val0
        out.append((2 * j, c / (2 * mp.pi) * m * m))
    return out


def fuchs(n, c):
    """Fuchs 1964 Thm 1:  1 - Lambda_n(c) ~ 4 sqrt(pi) 8^n c^{n+1/2} e^{-2c}/n!"""
    return (4 * mp.sqrt(mp.pi) * mp.mpf(8) ** n * c ** (mp.mpf(n) + mp.mpf(1) / 2)
            / mp.factorial(n) * mp.exp(-2 * c))


def defects(mu, K=None):
    """(1 - Lambda_0, 1 - Lambda_4, 1 - chi_2) at c = 2 pi mu."""
    c = 2 * mp.pi * mp.mpf(mu)
    L = dict(Lambda_even(c, 2, K))
    return 1 - L[0], 1 - L[4], 1 - mp.sqrt(L[4])


# --- the Weil side (recomputed here, not quoted) -------------------------------


def s_of(mu, N):
    """Smallest eigenvalue of the even semi-local Weil matrix, truncation N."""
    L = mp.log(mp.mpf(mu))
    return V.lam_min(V.sub(V.sigma_arch(L, N), V.w_primes(L, N)))


def geom_extrap(logs):
    """Geometric extrapolation of a monotone decreasing sequence's limit.

    logs = [f(N_1), ..., f(N_k)] equally spaced in N.  Returns the limit under
    the model f(N) - f(inf) = C r^N, using the last three entries.
    """
    d1 = logs[-2] - logs[-3]
    d2 = logs[-1] - logs[-2]
    if d1 == 0 or not (0 < d2 / d1 < 1):
        return logs[-1]
    r = d2 / d1
    return logs[-1] + d2 * r / (1 - r)


# --- checks -------------------------------------------------------------------


def check0():
    print("CHECK 0 -- the prolate apparatus, before it is used for anything")
    print()
    mp.mp.dps = 40
    got = dict(Lambda_even(mp.mpf(1), 2, K=40))[0]
    # "agreement to the five digits he prints"
    VD.check(abs(got - mp.mpf("0.57258")) < mp.mpf("5e-6"),
             "CHECK 0: Lambda_0(c=1) agrees with Slepian's tabulated 0.57258")
    print("  Lambda_0(c=1) = %s" % mp.nstr(got, 15))
    print("  Slepian's classical tabulated value for c = 1 is 0.57258 ; agreement")
    print("  to the five digits he prints.")
    print()
    print("  A SECOND, INDEPENDENT EIGENSOLVER.  The same tridiagonal matrix, but")
    print("  diagonalised by mpmath's dense symmetric routine (Householder + QL)")
    print("  instead of by bisection plus inverse iteration.  Nothing but the")
    print("  matrix is shared:")
    print()
    mp.mp.dps = 80
    c = 2 * mp.pi * mp.mpf(5)
    K = 60 if QUICK else 140
    a, b = _tri(c, K)
    A = mp.matrix(K, K)
    for i in range(K):
        A[i, i] = a[i]
        if i + 1 < K:
            A[i, i + 1] = b[i]
            A[i + 1, i] = b[i]
    ev, W = mp.eigsy(A)
    order = sorted(range(K), key=lambda i: ev[i])
    P0 = _P_at_zero(K)
    print("      %-4s %-28s %-28s" % ("n", "bisection + inv.it.", "dense eigsy"))
    mine = dict(Lambda_even(c, 2, K=K))
    for j, n in ((0, 0), (1, 2), (2, 4)):
        col = [W[i, order[j]] for i in range(K)]
        nrm = mp.sqrt(sum(x * x for x in col))
        col = [x / nrm for x in col]
        m = col[0] * mp.sqrt(mp.mpf(2)) / sum(col[i] * P0[i] for i in range(K))
        alt = c / (2 * mp.pi) * m * m
        # "Agreement to every digit printed": twenty of them, on quantities of
        # size 1e-18 to 1e-26 that are each 1 minus a number.
        VD.check(mp.nstr(1 - mine[n], 20) == mp.nstr(1 - alt, 20),
                 "CHECK 0: the two eigensolvers agree to every printed digit "
                 "(n=%d)" % n)
        print("      %-4d %-28s %-28s" % (n, mp.nstr(1 - mine[n], 20), mp.nstr(1 - alt, 20)))
    print()
    print("  Agreement to every digit printed, on quantities of size 1e-18 to")
    print("  1e-26 obtained as 1 minus a number.  The reason this is possible at")
    print("  all is that the prolate DIFFERENTIAL operator has well separated")
    print("  eigenvalues while the concentration operator it commutes with has")
    print("  its top eigenvalues equal to 55 decimal places.  Diagonalising the")
    print("  latter directly -- the obvious approach -- cannot work.")
    print()


def check1():
    print("CHECK 1 -- Fuchs at general index, and Connes' printed constant")
    print()
    mp.mp.dps = 100
    print("  Connes, `rhready.tex:1149` (arXiv:2602.04022, Feb 2026), states")
    print("      1 - chi_2  ~  (2^14/3) sqrt2 pi^5 exp(-4 pi e^L + (9/2) L)")
    print("  and his footnote fixes the convention: chi_k^2 = lambda_{2k}(a) with")
    print("  a = sqrt(2 pi) lambda, i.e. c = a^2 = 2 pi mu.  With e^L = mu that is")
    print("  a mu^{9/2} e^{-4 pi mu} law.  Identify the constant:")
    print()
    K1 = mp.mpf(2) ** 14 * mp.sqrt(2) * mp.pi ** 5 / 3
    K2 = mp.mpf(1) / 2 * 4 * mp.sqrt(mp.pi) * mp.mpf(8) ** 4 / mp.factorial(4) * (2 * mp.pi) ** (mp.mpf(9) / 2)
    print("      2^14 sqrt2 pi^5 / 3          = %s" % mp.nstr(K1, 25))
    print("      (1/2) Fuchs_4 at c = 2 pi mu = %s" % mp.nstr(K2, 25))
    print("      difference                   = %s" % mp.nstr(K1 - K2, 5))
    # "They are the same number."  Both are closed forms at 100 digits.
    VD.check(abs(K1 - K2) < abs(K1) * mp.mpf(10) ** -60,
             "CHECK 1: Connes' constant IS Fuchs' constant at index 4")
    print()
    print("  They are the same number.  So Connes' statement IS Fuchs' theorem at")
    print("  index n = 4, halved because chi_2 = sqrt(Lambda_4) and")
    print("  1 - sqrt(x) = (1 - x)/2 + O((1-x)^2).  Index 4, not index 0: the")
    print("  9/2 is n + 1/2 at n = 4.")
    print()
    print("  Now Fuchs' asymptotic against the exact defect, at three indices --")
    print("  which is the check `semilocal-gap.md` §5.3 did NOT do: it compared")
    print("  Connes' printed constant with the general-n form, two formulas, and")
    print("  found them equal to twelve decimals.  Here the formula is compared")
    print("  with the thing it approximates.  The ratio must tend to 1 in c, and")
    print("  the correction must be O(1/c):")
    print()
    mp.mp.dps = 260
    print("      %-22s %-14s %-14s %-14s" % ("c", "n=0", "n=2", "n=4"))
    cs = ([2 * mp.pi * 5, 2 * mp.pi * 12] if QUICK
          else [2 * mp.pi * 5, 2 * mp.pi * 8, 2 * mp.pi * 12,
                mp.mpf(120), mp.mpf(200), mp.mpf(280)])
    for c in cs:
        L = dict(Lambda_even(c, 2, K=int(c) + 90))
        row = [mp.nstr(fuchs(n, c) / (1 - L[n]), 8) for n in (0, 2, 4)]
        lbl = mp.nstr(c, 7) + ("  (mu = %d)" % round(float(c / (2 * mp.pi)))
                               if c < 100 else "")
        print("      %-22s %-14s %-14s %-14s" % (lbl, row[0], row[1], row[2]))
    print()
    print("  Fuchs OVER-estimates the defect, by 1 + O(1/c).  At n = 4 that is a")
    print("  31% error at c = 2 pi * 5 falling to 11% at c = 2 pi * 12 -- i.e.")
    print("  across the whole range where s(mu) is computed.  So the asymptotic is")
    print("  not accurate enough to serve as the comparison object in CHECK 2; the")
    print("  exact defect is.  (This is also why 260 digits here: 1 - Lambda_0 at")
    print("  c = 280 is 1e-240, and at 120 digits the subtraction returns noise.)")
    print()


def sgrid():
    """log10 s(mu, N) over the whole grid, computed once and shared by 2 and 3."""
    mp.mp.dps = 130 if not QUICK else 100
    mus = (5, 6, 7, 8, 9, 10, 11, 12) if not QUICK else (5, 8, 12)
    Ns = (60, 80, 100, 120) if not QUICK else (40, 60, 80)
    S = {}
    for mu in mus:
        for N in Ns:
            S[(mu, N)] = mp.log10(s_of(mu, N))
    return mus, Ns, S


def check2(mus, Ns, S):
    print("CHECK 2 -- the confrontation")
    print()
    Nref = Ns[-2]
    print("  s(mu) recomputed here at N = %d, %d digits (this reproduces" % (Nref, mp.mp.dps))
    print("  `deficit-repair.md` §4.1; nothing is copied from a note).  Against the")
    print("  index-0 defect that §5 named, and against the index-4 defect that")
    print("  Connes-Consani's own construction forces:")
    print()
    print("   %-3s %-15s %-15s %-12s %-15s %-11s"
          % ("mu", "s(mu)", "1 - Lambda_0", "s/(1-L_0)", "1 - chi_2", "s/(1-chi_2)"))
    rows = []
    for mu in mus:
        s = mp.mpf(10) ** S[(mu, Nref)]
        d0, d4, c2 = defects(mu)
        rows.append((mu, s, d0, c2))
        print("   %-3d %-15s %-15s %-12s %-15s %-11s"
              % (mu, mp.nstr(s, 7), mp.nstr(d0, 7), mp.nstr(s / d0, 5),
                 mp.nstr(c2, 7), mp.nstr(s / c2, 5)))
    print()
    r0 = [r[1] / r[2] for r in rows]
    r2 = [r[1] / r[3] for r in rows]
    print("  index 0:  ratio spans %s to %s, a factor of %s"
          % (mp.nstr(min(r0), 5), mp.nstr(max(r0), 5), mp.nstr(max(r0) / min(r0), 4)))
    print("  index 4:  ratio spans %s to %s, a factor of %s"
          % (mp.nstr(min(r2), 5), mp.nstr(max(r2), 5), mp.nstr(max(r2) / min(r2), 4)))
    print()
    print("  That is the answer to the ticket.  s(mu) is NOT of the order of")
    print("  1 - Lambda_0: it exceeds it by nine to ten orders of magnitude and the")
    print("  discrepancy GROWS, by a factor of about mu^4 -- which is 8^4 c^4 / 4!,")
    print("  exactly the index ratio in Fuchs.  It IS of the order of 1 - chi_2,")
    print("  within a factor of about ten, and CHECK 3 shows most of the residual")
    print("  growth to be the truncation bias.")
    print()
    print("  Note which mu carry the larger ratio: 7, 9, 11 -- each of them the last")
    print("  integer before a prime power enters the form.  s is largest just before")
    print("  a new prime power arrives to repair it.  That is `deficit-repair.md`")
    print("  §3's oscillation seen from the near-radical direction.")
    print()
    return rows


def check3(mus, Ns, S):
    print("CHECK 3 -- the truncation bias, measured")
    print()
    print("  Every s above is an UPPER bound -- restricting a quadratic form to a")
    print("  subspace raises its smallest eigenvalue -- and the bound is looser at")
    print("  larger mu, which is the direction that inflates s/(1-chi_2) at large")
    print("  mu.  So measure it rather than asserting it.  log10 s(mu, N):")
    print()
    print("   %-3s %s  %-14s" % ("mu", "  ".join("%-14s" % ("N = %d" % N) for N in Ns), "N -> inf"))
    ext = {}
    for mu in mus:
        logs = [S[(mu, N)] for N in Ns]
        lim = geom_extrap(logs)
        ok = lim != logs[-1]
        if ok:
            ext[mu] = lim
        print("   %-3d %s  %-14s"
              % (mu, "  ".join("%-14s" % mp.nstr(x, 10) for x in logs),
                 mp.nstr(lim, 10) if ok else "(not geometric)"))
    print()
    print("  The N -> infinity column is a three-point geometric fit to the last")
    print("  three truncations, and it is a model, not a theorem.  At mu = 6 and 9")
    print("  the last two increments are not decreasing, so no fit is reported")
    print("  there; that is the fit refusing rather than the sequence diverging.")
    print("  What the fit can only ever do is move s DOWN, and it moves it down")
    print("  more at large mu.  The resulting ratios:")
    print()
    print("   %-3s %-16s %-16s" % ("mu", "s/(1-chi_2), N=%d" % Ns[-1], "s/(1-chi_2), N->inf"))
    for mu in mus:
        d0, d4, c2 = defects(mu)
        last = mp.mpf(10) ** S[(mu, Ns[-1])] / c2
        e = mp.nstr(mp.mpf(10) ** ext[mu] / c2, 6) if mu in ext else "--"
        print("   %-3d %-16s %-16s" % (mu, mp.nstr(last, 6), e))
    print()
    print("  A ratio of order ten whose residual growth across mu = 5..12 is a")
    print("  factor of about 1.3 -- no faster than log mu.  A sub-polynomial")
    print("  residual cannot change an exponential rate, which is the only thing")
    print("  the rate claim needs.  It does mean the O(1) constant in")
    print("  s ~ kappa (1 - chi_2) is not constant; kappa growing like log mu is")
    print("  what the missing inequality of §6 would produce, since the mean")
    print("  density of zeros near height T is log(T/2pi)/2pi.  That is a")
    print("  consistency, not a derivation.")
    print()
    return ext


def check4(rows):
    print("CHECK 4 -- the three-parameter test, with no free parameters")
    print()
    print("  `deficit-repair.md` §5 fits log10 s = -A mu + B log10 mu + D and")
    print("  reports A = 5.4635 +- 0.052, B = 5.322 +- 0.96, D = 6.589 +- 0.44,")
    print("  comparing A alone with 4 pi / log 10 = 5.4575 (0.12 sigma) and leaving")
    print("  B as open item T3 because the naive index-0 Slepian prefactor is 1/2.")
    print("  Connes' index-4 asymptotic predicts all three:")
    print()
    mp.mp.dps = 60
    A = 4 * mp.pi / mp.log(10)
    B = mp.mpf(9) / 2
    D = mp.log10(mp.mpf(2) ** 14 * mp.sqrt(2) * mp.pi ** 5 / 3)
    fit = [("A", mp.mpf("5.4635"), mp.mpf("0.052"), A),
           ("B", mp.mpf("5.322"), mp.mpf("0.96"), B),
           ("D", mp.mpf("6.589"), mp.mpf("0.44"), D)]
    print("      %-3s %-18s %-14s %-8s" % ("", "fitted (mg-7606)", "predicted", "sigma"))
    for name, val, err, pred in fit:
        # "Three parameters, none of them free, all within one standard error."
        VD.check(abs(val - pred) / err <= 1,
                 "CHECK 4: %s is within one standard error of its prediction" % name)
        print("      %-3s %-18s %-14s %-8s"
              % (name, "%s +- %s" % (mp.nstr(val, 6), mp.nstr(err, 3)),
                 mp.nstr(pred, 8), mp.nstr(abs(val - pred) / err, 3)))
    print()
    print("  Three parameters, none of them free, all within one standard error.")
    print("  The index-0 reading predicts B = 1/2, which is %s sigma away."
          % mp.nstr(abs(mp.mpf("5.322") - mp.mpf("0.5")) / mp.mpf("0.96"), 3))
    print()
    print("  T3 is therefore not an open problem about subleading structure.  It")
    print("  was the index-0 hypothesis failing a test the index-4 hypothesis")
    print("  passes, and it is the one place in `deficit-repair.md` where the wrong")
    print("  index left a visible mark.")
    print()
    print("  Residuals of log10 s - log10(1 - chi_2), i.e. the same test done")
    print("  against the exact defect rather than its asymptotic:")
    print()
    for mu, s, d0, c2 in rows:
        print("      mu = %-3d  log10[s/(1-chi_2)] = %s" % (mu, mp.nstr(mp.log10(s / c2), 6)))
    print()


def check5():
    print("CHECK 5 -- stability of the prolate defects")
    print()
    print("  Same c = 2 pi * 12, three working precisions and two Legendre")
    print("  truncations.  1 - Lambda_4 is 1e-55 read off a matrix whose entries")
    print("  are of order c^2 = 5.7e3, so this is the check that matters:")
    print()
    seen = set()
    for dps, K in ((80, 165), (120, 165), (120, 220), (200, 220)):
        mp.mp.dps = dps
        c = 2 * mp.pi * mp.mpf(12)
        L = dict(Lambda_even(c, 2, K=K))
        seen.add((mp.nstr(1 - L[0], 16), mp.nstr(1 - L[4], 16)))
        print("      dps = %-4d K = %-4d  1-Lambda_0 = %s   1-Lambda_4 = %s"
              % (dps, K, mp.nstr(1 - L[0], 16), mp.nstr(1 - L[4], 16)))
    # "No movement": the four rows are one row, in the digits printed.
    VD.check(len(seen) == 1,
             "CHECK 5: the defects do not move across dps 80/120/200 and K 165/220")
    print()
    print("  No movement.  The Legendre coefficients beta_k decay super-")
    print("  exponentially past k ~ c, so K = c + 90 is already past the point")
    print("  where adding coefficients changes anything, and the 1 - Lambda")
    print("  subtraction loses only the leading 55 digits of a 120-digit number.")
    print()


if __name__ == "__main__":
    print(__doc__)
    print("=" * 79)
    print()
    check0()
    print("=" * 79)
    print()
    check1()
    print("=" * 79)
    print()
    mus, Ns, S = sgrid()
    rows = check2(mus, Ns, S)
    print("=" * 79)
    print()
    check3(mus, Ns, S)
    print("=" * 79)
    print()
    check4(rows)
    print("=" * 79)
    print()
    check5()
    VD.finish()
