#!/usr/bin/env python3
"""The ceiling is a theorem.  Five checks for `sonin-ceiling.md` (mg-0b7a).  Needs numpy.

    cd notes && python verify_sonin_ceiling.py            # 10m18s measured
    cd notes && python verify_sonin_ceiling.py --quick    # 1m02s

`--quick` coarsens every grid and keeps 23 of the 24 wired checks.  The one it
drops is CHECK 5's N = 60 against N = 120 inertia comparison, which needs both
truncations by construction; `verify_sonin_margin.py`'s `--quick` drops its
counterpart for the same reason.  CI runs `--quick`, so that comparison is NOT
covered by a green tick -- it is covered by the full grid, which is the run
`sonin-ceiling.md` records.

[`sonin-margin.md`](sonin-margin.md) (mg-d03b) closed with a one-line argument
it called "the one thing that could have been said without computing anything":

    eps > 0, so eps_hat(0) = +5.3722 > 0, so the symbol of -E is NEGATIVE at low
    frequency, so only a support too short to let ghat into that band can save
    Theorem 1's inequality.

This script turns that into a theorem, and in the course of doing so it finds
that two of mg-d03b's own numbers are wrong.

--- WHAT THIS SCRIPT FOUND ---------------------------------------------------

(1) THE ASYMPTOTIC IS DERIVABLE AND THE CONSTANT IS 1.  mg-d03b measured
eps(rho) sqrt(rho) -> 1 to 0.5% at rho = 60, marked it "ours, unanchored", and
recorded that an attempt to derive it returned 37.5 and was abandoned.  It is

    eps(rho) sqrt(rho)  ->  (1/2) sum_n lam(n) xi_n(0)^2  =  1,

because sum_m lam_m psi_m(x) psi_m(y) = e^{2 pi i x y} is the spectral expansion
of the finite Fourier operator's kernel on [-1,1] -- at x = y = 0 it reads
sum_m lam_m psi_m(0)^2 = 1 -- and Connes-Consani's xi_n are normalised to
int_{-1}^1 xi_n^2 = 2, not 1.  The factor of two IS the constant.  CHECK 1
measures sum_n lam(n) xi_n(0)^2 = 2 to 1e-14 and the convergence rate O(1/rho).

(2) eps_hat(0) HAS A CLOSED FORM, AND IT DOES NOT GO THROUGH eps > 0.  Mellin
inversion at the self-dual point s = 1/2 -- int_0^inf u^{-1/2} F f(u) du =
int_0^inf x^{-1/2} f(x) dx, the gamma factor being exactly 1 there -- collapses
the double integral to

    eps_hat(0)  =  2 sum_n  lam(n) / (1 + lam(n))  A_n^2,
    A_n = int_0^1 xi_n(x) x^{-1/2} dx,

a series whose partial sums are stable by n = 6.  CHECK 2 gets 5.37218344
against 5.37217300 from the quadrature of `verify_sonin_margin.Symbol`, and
5.37218520 when that quadrature is tightened -- two routes sharing only the
prolate apparatus, and the deviation falls as the quadrature does.  This matters because the argument
as mg-d03b stated it rests on eps > 0 POINTWISE, which this corpus has never
proved, and on convergence of int_0^inf eps(e^y) dy, which rested on (1).  The
closed form needs neither.

(3) THE CEILING IS A THEOREM, AND ITS TEST FUNCTION IS EXPLICIT.  If ghat is
required to vanish at k points z_1..z_k of the complex plane -- which is what
Theorem 1's ghat(0) = ghat(i/2) = 0 is -- then put ghat = P(t) phihat(t) with
P(t) = prod (t - z_j) and phi(u) = psi(u/L) for any fixed bump psi.  This is
admissible by construction, is supported in [-L/2, L/2] because P is a
polynomial, and

    E(g_L) / L  ->  (1/2 pi) eps_hat(0) int |P(0)|^2 |psihat|^2 ds  >  0

by dominated convergence, the domination being |eps_hat| <= ||eps||_1.  So for
every k there is a finite L past which -E is indefinite on the codimension-k
subspace: THE CEILING EXISTS FOR EVERY CODIMENSION, and needs nothing about eps
beyond eps_hat(0) > 0 and integrability.  CHECK 3 exhibits the limit for
k = 1..4 and the (very crude) support at which the explicit g_L turns positive.

(4) THE CONSTANT IS NOT 25% OUT.  IT IS AN UPPER BOUND, AND THE MEASUREMENT IS
BELOW IT, WHICH IS WHAT UPPER BOUNDS LOOK LIKE.  mg-d03b compared its measured
slope 0.7523 of log mu_c in k against 2 pi / t_0 = 0.9986 and called the
constant 25% out.  But restricting a form to a codimension-k subspace kills at
most k negative eigenvalues, so

    n_-(L) > k   ==>   -E is indefinite on EVERY codimension-k subspace,

i.e. log mu_c(k) <= Lambda(k) := inf{L : n_-(L) > k}, and Lambda(k)/k -> pi/t_0
by the Szego density of the truncated convolution form (2 pi / t_0 on the even
block, which is the one mg-d03b's cosine basis computes).  CHECK 4 measures
Lambda(k) directly.  The 25% is the slack in an inequality, not an error.

(5) THE COSINE BASIS IS THE EVEN BLOCK, AND THE ODD BLOCK BREAKS FIRST.  E is a
convolution form, so it block-diagonalises over even + odd g; the basis every
script in this corpus uses -- xi_n = cos(2 pi n y / L) -- spans the even block
alone.  Theorem 1 is stated for g in Cc^inf(R+*) with no parity restriction, so
the odd block is admissible and is missing from mg-d03b's table.  Adding it:

    codim k     mu_c(k), mg-d03b (even only)     mu_c(k), even + odd
    ----------------------------------------------------------------
      1                   2.763                        1.775
      2 (Thm 1)           6.174                        2.759
      3                  13.01                         4.164
      4                  26.46                         6.042

Two of mg-d03b's headline statements do not survive this.  "Theorem 1's
conclusion holds to mu = 6.17, three times its stated hypothesis" becomes
mu = 2.76, a factor 1.38 -- the hypothesis mu <= 2 is much closer to sharp than
that note claims.  And "ghat(0) = 0 ALONE covers Theorem 1's whole range
mu <= 2" is FALSE: mu_c(1) = 1.775 < 2, because an odd g satisfies ghat(0) = 0
for free.  The second condition is doing real work inside Theorem 1's own range,
which is what mg-5210 said and mg-d03b half-retired.  CHECK 5.

--- CONVENTIONS --------------------------------------------------------------

`verify_sonin_margin.py`'s, unchanged and imported rather than re-derived, so
the columns read against its.  L = log mu; xi_n the cosine basis on
[-L/2, L/2]; `_h` the symmetrised correlation.  The odd basis added here is
eta_n = sqrt(2/L) sin(2 pi n y / L), n = 1..N, and `_h_odd` is `_h` with the
product-to-sum identity for sines in place of cosines -- CHECK 5 puts it against
direct quadrature of the correlation integral, and puts E on an explicit mixed g
against brute-force two-dimensional quadrature of the kernel.

--- HOUSE RULE ---------------------------------------------------------------

Stated per check at the end.  The theorem itself -- "E has a positive direction
in every fixed-codimension subspace once the support is long enough" -- is a
statement about eps alone and is SIGN-BLIND.  Its reading, "Theorem 1's
conclusion fails past mu_c", is NOT: the trace does not move under
W_lambda -> -W_lambda and W_inf does.  So the ceiling is sign-blind mathematics
with a non-sign-blind consequence, and CHECK 5's two corrections to mg-d03b are
corrections to non-sign-blind statements.
"""

import sys

import numpy as np

from verdict import Verdict
from verify_arch_positivity import _h
from verify_sonin_margin import (MU_MAX, EpsTable, ProlateExact, Symbol,
                                 bisect, comp_gauss, cond_row, E_matrix,
                                 eps_exact, restrict)

VD = Verdict()

QUICK = "--quick" in sys.argv

# mg-d03b's mu_c(k) at N = 120, `sonin-margin.md` sec 4.2, quoted so CHECK 5
# compares against what was printed rather than against a rerun of that code.
MG_D03B_MUC = {1: 2.7634, 2: 6.1739, 3: 13.011, 4: 26.461}


# --- the odd block ------------------------------------------------------------

def _h_odd(L, N, t):
    """h_{nm}(t) for eta_n = sqrt(2/L) sin(2 pi n y / L), n = 1..N.

    `verify_arch_positivity._h` with sin in place of cos:
    sin(a x) sin(b (x-t)) = 1/2 [cos((a-b) x + b t) - cos((a+b) x - b t)],
    against the cosines' 1/2 [cos((a+b) x - b t) + cos((a-b) x + b t)].
    """
    t = np.atleast_1d(np.asarray(t, dtype=float))
    n = np.arange(1, N + 1)
    a = 2 * np.pi * n / L
    c = np.full(N, np.sqrt(2.0 / L))
    p, q = t - L / 2.0, L / 2.0

    def seg(alpha, beta):
        """int_p^q cos(alpha x + beta) dx, broadcast over (T, N, N)."""
        nz = np.abs(alpha) > 1e-13
        den = np.where(nz, alpha, 1.0)
        val = (np.sin(alpha * q + beta)
               - np.sin(alpha * p[:, None, None] + beta)) / den
        return np.where(nz, val, (q - p[:, None, None]) * np.cos(beta))

    zero = np.zeros((len(t), N, N))
    A = a[None, :, None] + a[None, None, :] + zero
    B = a[None, :, None] - a[None, None, :] + zero
    bt = a[None, None, :] * t[:, None, None]
    I = 0.5 * (seg(B, bt) - seg(A, -bt))
    return (I + np.transpose(I, (0, 2, 1))) * (c[None, :, None] * c[None, None, :])


def E_matrix_odd(eps, L, N, order=16, chunk=64):
    """`verify_sonin_margin.E_matrix` on the sine basis."""
    t, wt = comp_gauss(0.0, L, max(80, int(30 * L) + 60), order)
    ev = eps(t)
    out = np.zeros((N, N))
    for a in range(0, t.size, chunk):
        b = min(a + chunk, t.size)
        out += np.tensordot(wt[a:b] * ev[a:b], _h_odd(L, N, t[a:b]), axes=(0, 0))
    return 0.5 * (out + out.T)


def cond_row_odd(L, N, j):
    """ghat(i j / 2) on odd g:  int_{-L/2}^{L/2} eta_n(y) e^{j y / 2} dy.

    j = 0 returns zeros, and that is the whole point of CHECK 5: an odd g
    satisfies Theorem 1's first condition ghat(0) = 0 for free, so the second
    condition is the only one it costs anything to impose.
    """
    n = np.arange(1, N + 1)
    a = 2 * np.pi * n / L
    c = np.full(N, np.sqrt(2.0 / L))
    if j == 0:
        return np.zeros(N)
    b, q = j / 2.0, L / 2.0
    return c * 2 * (b * np.sin(a * q) * np.cosh(b * q)
                    - a * np.cos(a * q) * np.sinh(b * q)) / (a ** 2 + b ** 2)


_FULL_CACHE = {}


def full_matrix(eps, L, N):
    """-E on the full basis xi_0..xi_N, eta_1..eta_N: block diagonal.

    Memoised on (L, N).  CHECK 5 asks for five codimensions at each (mu, N) and
    a bisection asks for one L many times over; rebuilding the two blocks each
    time is the whole cost of this script.  The cache is keyed on the float L
    exactly, which is what both callers hand it.
    """
    key = (L, N)
    if key not in _FULL_CACHE:
        if len(_FULL_CACHE) > 8:              # bisections walk L, so bound it
            _FULL_CACHE.clear()
        A = np.zeros((2 * N + 1, 2 * N + 1))
        A[:N + 1, :N + 1] = -E_matrix(eps, L, N)
        A[N + 1:, N + 1:] = -E_matrix_odd(eps, L, N)
        _FULL_CACHE[key] = A
    return _FULL_CACHE[key]


def full_spec(eps, mu, N, k):
    """Eigenvalues of -E on {ghat(i j/2) = 0, j < k}, even AND odd g."""
    L = np.log(mu)
    A = full_matrix(eps, L, N)
    if k == 0:
        return np.linalg.eigvalsh(A)
    rows = [np.concatenate([cond_row(L, N, j), cond_row_odd(L, N, j)])
            for j in range(k)]
    return np.linalg.eigvalsh(restrict(A, rows))


# --- checks -------------------------------------------------------------------

def check1(pr):
    print("CHECK 1 -- eps(rho) sqrt(rho) -> 1, DERIVED.  mg-d03b measured this and")
    print("marked it unanchored; an attempt to derive the constant gave 37.5 and was")
    print("abandoned (`sonin-margin.md` sec 7).  The constant is a reproducing kernel.")
    print()
    print("  Substituting u = rho x in eps(rho) = sqrt(rho) sum_n lam/(1-lam^2)")
    print("  int_{1/rho}^1 xi_n(x) F xi_n(rho x) dx gives")
    print()
    print("      eps(rho) sqrt(rho) = sum_n lam(n)/(1-lam(n)^2) int_1^rho")
    print("                             xi_n(u/rho) F xi_n(u) du,")
    print()
    print("  and int_1^inf F xi_n = (1/2)(1 - lam(n)^2) xi_n(0), because")
    print("  int_R F xi_n = xi_n(0) by inversion and int_{-1}^1 F xi_n = lam(n)^2 xi_n(0)")
    print("  by the eigenrelation.  So the limit is (1/2) sum_n lam(n) xi_n(0)^2.")
    print()
    x, w = comp_gauss(-1.0, 1.0, 200, 16)
    XI = pr.at(x)
    nrm = (w[None, :] * XI * XI).sum(axis=1)
    print("      int_{-1}^1 xi_n^2, n = 0..5: %s" % np.array2string(nrm[:6], precision=9))
    VD.check(np.abs(nrm - 2.0).max() < 1e-8,
             "CHECK 1: Connes-Consani's xi_n are normalised to int_{-1}^1 xi_n^2 = 2 "
             "(int_0^1 = 1), NOT to 1 -- this factor of two is the constant")
    xi0 = pr.at(np.array([0.0]))[:, 0]
    S = float((pr.lam * xi0 ** 2).sum())
    print("      sum_n lam(n) xi_n(0)^2 = %.14f" % S)
    print("        (= 2 sum_m lam_m psi_m(0)^2 over the L^2-orthonormal prolates,")
    print("         and sum_m lam_m psi_m(x) psi_m(y) = e^{2 pi i x y} at x = y = 0)")
    VD.check(abs(S - 2.0) < 1e-9,
             "CHECK 1: sum_n lam(n) xi_n(0)^2 = 2 -- the spectral expansion of the "
             "finite Fourier kernel at the origin")
    print("      so the limit is %.14f" % (S / 2.0))
    print()
    print("  and against the measurement, with the rate:")
    print("  %10s %18s %16s" % ("rho", "eps sqrt(rho)", "(1 - that) rho"))
    rr = np.array([10.0, 20.0, 40.0, 60.0] if QUICK
                  else [10.0, 20.0, 40.0, 60.0, 100.0, 200.0])
    ev = eps_exact(pr, rr)
    for r, v in zip(rr, ev):
        print("  %10.1f %18.6f %16.4f" % (r, v * np.sqrt(r), (1 - v * np.sqrt(r)) * r))
    dev = abs(ev[-1] * np.sqrt(rr[-1]) - S / 2.0)
    VD.check(dev < 0.02,
             "CHECK 1: the measured eps(rho) sqrt(rho) agrees with the derived limit "
             "(1/2) sum lam(n) xi_n(0)^2 at the largest rho computed")
    print()
    print("  The third column is bounded, so the approach is O(1/rho): eps(e^|y|) -")
    print("  e^{-|y|/2} is integrable and eps_hat(0) converges.  That is the whole")
    print("  use mg-d03b made of the asymptotic, and it is now derived rather than")
    print("  measured.  SIGN-BLIND.")
    print()
    return S


def check2(pr, sym):
    print("CHECK 2 -- eps_hat(0) in closed form, by a route that does not use eps > 0.")
    print()
    print("  mg-d03b's argument is 'eps > 0, so eps_hat(0) > 0'.  Pointwise positivity")
    print("  of eps is not proved anywhere in this corpus -- Theorem `devil` proves the")
    print("  FUNCTIONAL tr(theta(f) S) is positive, which is W_inf + E >= 0, not")
    print("  eps >= 0 -- and the convergence of int_0^inf eps(e^y) dy rested on CHECK 1.")
    print("  Both are avoidable.  Substituting u = rho x and using Fubini,")
    print()
    print("      eps_hat(0) = 2 int_1^inf eps(rho) d*rho = 2 sum_n lam/(1-lam^2) A_n B_n,")
    print("      A_n = int_0^1 xi_n(x) x^{-1/2} dx,  B_n = int_1^inf F xi_n(u) u^{-1/2} du,")
    print()
    print("  and Mellin inversion at the SELF-DUAL point s = 1/2, where the gamma")
    print("  factor 2 Gamma(s) cos(pi s/2) (2 pi)^{-s} is exactly 1, gives")
    print("  int_0^inf u^{-1/2} F xi_n = int_0^1 x^{-1/2} xi_n = A_n, so")
    print("  B_n = (1 - lam(n)) A_n and the coefficient collapses:")
    print()
    print("      eps_hat(0) = 2 sum_n lam(n) / (1 + lam(n)) A_n^2.")
    print()
    v, wv = comp_gauss(0.0, 1.0, 60, 16)
    A = 2.0 * (wv[None, :] * pr.at(v * v)).sum(axis=1)      # x = v^2
    terms = 2.0 * pr.lam / (1.0 + pr.lam) * A ** 2
    print("  %4s %14s %14s %16s %16s" % ("n", "lam(n)", "A_n", "term", "partial sum"))
    ps = np.cumsum(terms)
    for n in range(min(8, len(terms))):
        print("  %4d %14.6e %14.6e %16.6e %16.8f"
              % (n, pr.lam[n], A[n], terms[n], ps[n]))
    closed = float(terms.sum())
    print()
    print("      closed form  eps_hat(0) = %.8f" % closed)
    quad = float(sym(0.0)[0])
    print("      quadrature   eps_hat(0) = %.8f   (`verify_sonin_margin.Symbol`)" % quad)
    print("      relative deviation       = %.2e" % (abs(closed - quad) / abs(quad)))
    VD.check(abs(closed - quad) / abs(quad) < 1e-4,
             "CHECK 2: the closed form 2 sum lam/(1+lam) A_n^2 reproduces the "
             "quadrature value of eps_hat(0) to 1e-4")
    VD.check(closed > 0,
             "CHECK 2: eps_hat(0) > 0 from a convergent explicit series, with no "
             "appeal to eps > 0 pointwise and none to the rho^{-1/2} asymptotic")
    tail = float(np.abs(terms[6:]).sum())
    print("      |tail| from n = 6 on      = %.2e, against a value of %.4f"
          % (tail, closed))
    VD.check(tail < 1e-4 * closed,
             "CHECK 2: the series is stable by n = 6 -- the sign of eps_hat(0) is "
             "decided by finitely many terms")
    print()
    print("  Note A_1 = %.4e.  lam(1)/(1+lam(1)) = %.1f, so without that near-zero"
          % (A[1], pr.lam[1] / (1 + pr.lam[1])))
    print("  the n = 1 term alone would swamp the sum.  The series is not termwise")
    print("  positive and its positivity is a computation, not a sign argument.")
    print("  SIGN-BLIND.")
    print()
    return closed


def check3(pr, sym, e0):
    print("CHECK 3 -- the ceiling, as a theorem, with an explicit test function.")
    print()
    print("  THEOREM.  Let K(y) = eps(e^|y|) be in L^1(R) with eps_hat(0) > 0, let")
    print("  z_1..z_k be any k points of C, and let psi be any non-zero bump in")
    print("  Cc^inf(-1/2, 1/2).  Define g_L by ghat_L(t) = P(t) L psihat(L t) with")
    print("  P(t) = prod_j (t - z_j).  Then supp g_L is in [-L/2, L/2] (P is a")
    print("  polynomial, so g_L is a finite combination of derivatives of")
    print("  psi(./L)), ghat_L(z_j) = 0 for every j, and")
    print()
    print("      E(g_L) = (L / 2 pi) int |P(s/L)|^2 |psihat(s)|^2 eps_hat(s/L) ds")
    print()
    print("  converges, after the scaling by the order of vanishing of P at 0, to")
    print("  eps_hat(0) times a positive constant -- by dominated convergence, the")
    print("  dominating function being |eps_hat| <= ||K||_1 times a polynomial")
    print("  multiple of |psihat|^2, which is integrable because psi is smooth.")
    print("  So E(g_L) > 0 for all large L.  QED.")
    print()
    print("  Nothing in that uses anything about eps except eps_hat(0) > 0 (CHECK 2)")
    print("  and integrability (CHECK 1).  Below, the even form of the construction:")
    print("  ghat_L(t) = prod_{j<k} (t^2 + j^2/4) L psihat(L t), which is Theorem 1's")
    print("  conditions ghat(i j/2) = 0 for j = 0..k-1, P vanishing to order 2 at 0.")
    print()
    TG = np.concatenate([np.linspace(0.0, 40.0, 4001),
                         np.linspace(40.0, 4000.0, 4001)[1:]])
    EG = sym(TG)
    symi = lambda t: np.interp(t, TG, EG)

    def psi(v):
        out = np.zeros_like(v)
        m = np.abs(v) < 0.5
        out[m] = np.exp(-1.0 / (0.25 - v[m] ** 2))
        return out

    v, wv = comp_gauss(-0.5, 0.5, 200, 16)
    PV = psi(v)
    S, WS = comp_gauss(0.0, 120.0, 600 if QUICK else 1200, 16)
    PS = (wv[None, :] * PV[None, :] * np.cos(np.outer(S, v))).sum(axis=1)
    norm4 = 2.0 * (WS * S ** 4 * PS ** 2).sum() / (2 * np.pi)

    def E_of_L(L, k):
        P = np.ones_like(S)
        for j in range(k):
            P = P * (S ** 2 / L ** 2 + j ** 2 / 4.0)
        return (L / (2 * np.pi)) * 2.0 * (WS * P ** 2 * PS ** 2 * symi(S / L)).sum()

    print("  ||psi''||^2 = (1/2 pi) int s^4 |psihat|^2 = %.8f" % norm4)
    print()
    print("  %3s %9s %16s %16s %10s" % ("k", "L", "E(g_L)", "L^3 E(g_L)", "/ limit"))
    Ls = (10.0, 40.0, 160.0) if QUICK else (10.0, 20.0, 40.0, 80.0, 160.0)
    worst = 0.0
    for k in (1, 2, 3, 4):
        c = 1.0
        for j in range(1, k):
            c *= j * j / 4.0
        pred = e0 * c ** 2 * norm4
        for L in Ls:
            e = E_of_L(L, k)
            print("  %3d %9.1f %16.6e %16.6e %10.4f"
                  % (k, L, e, L ** 3 * e, L ** 3 * e / pred))
        print("  %3s %9s %16s %16.6e %10s" % ("", "limit", "", pred, "1.0000"))
        worst = max(worst, abs(Ls[-1] ** 3 * E_of_L(Ls[-1], k) / pred - 1.0))
        VD.check(E_of_L(Ls[-1], k) > 0,
                 "CHECK 3: the explicit admissible g_L has E(g_L) > 0 at L = %g, "
                 "codimension k = %d -- the ceiling, exhibited" % (Ls[-1], k))
    print()
    print("  worst deviation from the limit at L = %g: %.1f%%" % (Ls[-1], 100 * worst))
    VD.check(worst < 0.25,
             "CHECK 3: L^3 E(g_L) converges to eps_hat(0) prod (j^2/4)^2 ||psi''||^2, "
             "the limit the theorem's dominated convergence produces")
    print()
    print("  The construction is CRUDE: it certifies finiteness, not the threshold.")
    print("  Its first positive L for k = 1 is around 1.45 (mu = 4.3) against a true")
    print("  mu_c(1) of 1.775, and for k = 4 it is mu ~ 8e5 against 6.04.  A bump is")
    print("  a bad prolate.  What it buys is a proof rather than an eigenvalue.")
    print("  SIGN-BLIND.")
    print()


def check4(eps, sym, t0):
    print("CHECK 4 -- the constant is an upper bound, and 'the shape is right and the")
    print("constant is 25% out' is the slack in an inequality.")
    print()
    print("  Restricting a quadratic form to a subspace of codimension k destroys at")
    print("  most k negative eigenvalues.  So with n_-(L) the negative inertia of -E")
    print("  on the full space L^2[-L/2, L/2],")
    print()
    print("      n_-(L) > k   ==>   -E is indefinite on EVERY codimension-k subspace,")
    print()
    print("  hence log mu_c(k) <= Lambda(k) := inf{L : n_-(L) > k} for the specific")
    print("  conditions ghat(i j/2) = 0 and for any others.  The Szego density of a")
    print("  truncated convolution form is |{t : eps_hat(t) > 0}| / 2 pi = t_0 / pi,")
    print("  so Lambda(k) ~ pi k / t_0 -- and half that density, i.e. 2 pi k / t_0,")
    print("  on the even block, which is the block mg-d03b's cosine basis computes.")
    print()
    print("  t_0 = %.7f    pi / t_0 = %.5f    2 pi / t_0 = %.5f"
          % (t0, np.pi / t0, 2 * np.pi / t0))
    print()
    # The bisection cannot leave the support range this script's eps table is
    # built to.  A bisection whose answer is AT the bracket end is not an answer,
    # so `inside` rejects those rather than printing the bracket back.
    N = 40 if QUICK else 60
    HI = np.log(MU_MAX) + 0.05          # the ceiling `EpsTable` is built to
    inside = lambda L: L < 0.99 * HI
    ks = (1, 2, 3) if QUICK else (1, 2, 3, 4, 5, 6, 7)
    print("  %3s %12s %12s %8s | %12s %12s %8s"
          % ("k", "Lambda", "pi k/t_0", "ratio", "Lam (even)", "2 pi k/t_0", "ratio"))
    nb = 22 if QUICK else 32
    rf, re = [], []
    for k in ks:
        Lf = bisect(lambda L: np.sort(np.linalg.eigvalsh(full_matrix(eps, L, N)))[k],
                    0.02, HI, nb)
        rf.append(Lf / (np.pi * k / t0))
        cell = ""
        Le = bisect(lambda L: np.linalg.eigvalsh(-E_matrix(eps, L, N))[k],
                    0.02, HI, nb)
        if inside(Le):
            re.append(Le / (2 * np.pi * k / t0))
            cell = "%12.5f %12.5f %8.4f" % (Le, 2 * np.pi * k / t0, re[-1])
        else:
            cell = "%12s   (past the eps table's mu <= %g ceiling)" % ("--", MU_MAX)
        print("  %3d %12.5f %12.5f %8.4f | %s"
              % (k, Lf, np.pi * k / t0, rf[-1], cell))
    print()
    print("  Both ratios approach 1 from above -- the Landau-Widom correction to the")
    print("  eigenvalue count is +O(log), so a finite-k Lambda sits above the density")
    print("  line and comes down onto it.")
    VD.check(abs(rf[-1] - 1.0) < 0.25,
             "CHECK 4: Lambda(k) / (pi k / t_0) is within 25% of 1 at the largest k "
             "computed -- the negative inertia has the Szego density t_0 / pi")
    VD.check(abs(re[-1] - 1.0) < 0.25,
             "CHECK 4: the even block's Lambda(k) / (2 pi k / t_0) is within 25% of "
             "1 -- half the density, which is where mg-d03b's 2 pi / t_0 comes from")
    print()
    print("  and the inequality log mu_c(k) <= Lambda(k), against mg-d03b's mu_c:")
    print("  %3s %14s %14s %14s" % ("k", "log mu_c (even)", "Lambda (even)", "slack"))
    ok = True
    for k in ((1, 2) if QUICK else (1, 2, 3, 4)):
        Le = bisect(lambda L: np.linalg.eigvalsh(-E_matrix(eps, L, N))[k],
                    0.02, HI, nb)
        lm = np.log(MG_D03B_MUC[k])
        ok &= inside(Le) and lm <= Le + 1e-3
        print("  %3d %14.5f %14.5f %14.5f" % (k, lm, Le, Le - lm))
    VD.check(ok,
             "CHECK 4: log mu_c(k) <= Lambda(k) at k = 1..4 -- mg-d03b's measured "
             "slope 0.7523 lies BELOW 2 pi / t_0 = 0.9986 because the latter bounds "
             "it, not because it is 25% wrong")
    print()
    print("  So 0.7523 < 0.9986 is not a discrepancy.  What the gap measures is that")
    print("  the conditions ghat(i j/2) = 0 are INEFFICIENT: they are not aligned with")
    print("  the negative eigenvectors, so the codimension-k subspace already contains")
    print("  a negative direction before n_- has climbed past k.")
    print()
    print("  What is NOT available in this direction: nothing here proves -E >= 0")
    print("  below mu_c.  Truncation raises eigenvalues, so a negative truncated")
    print("  eigenvalue certifies one for the full form and not the converse; and the")
    print("  theorem of CHECK 3 is one-sided by construction.  Every mu_c in this")
    print("  corpus is an UPPER bound on a threshold whose lower half is unproved.")
    print()


def check5(pr, eps):
    print("CHECK 5 -- the cosine basis is the even block, and the odd block breaks")
    print("first.  Two of mg-d03b's headline numbers do not survive this.")
    print()
    print("  E(g) = int A_g(y) eps(e^|y|) dy with A_g the autocorrelation, so")
    print("  E(g) = E(g_even) + E(g_odd): the cross term is odd in t against an even")
    print("  eps_hat and integrates to zero.  The form block-diagonalises, and every")
    print("  script in this corpus works in xi_n = cos(2 pi n y / L), which spans the")
    print("  even block alone.  Theorem 1 is stated for g in Cc^inf(R+*) with no")
    print("  parity condition, so the odd block is admissible and is missing.")
    print()
    print("  (a) the odd machinery, against direct quadrature.")
    L, N = np.log(5.0), 5
    ts = np.array([0.0, 0.31, 0.9, 1.5])
    H = _h_odd(L, N, ts)
    n = np.arange(1, N + 1)
    a = 2 * np.pi * n / L
    c = np.sqrt(2.0 / L)
    worst = 0.0
    for it, t in enumerate(ts):
        x = np.linspace(t - L / 2, L / 2, 100001)
        dx = x[1] - x[0]
        Pn = c * np.sin(a[:, None] * x[None, :])
        Pm = c * np.sin(a[:, None] * (x - t)[None, :])
        I = np.trapezoid(Pn[:, None, :] * Pm[None, :, :], dx=dx, axis=2)
        worst = max(worst, np.abs((I + I.T) - H[it]).max())
    print("      _h_odd vs direct correlation quadrature:  max dev %.2e" % worst)
    VD.check(worst < 1e-6, "CHECK 5: `_h_odd` agrees with direct quadrature of the "
                           "correlation integral it claims to evaluate")
    # The same comparison against the EVEN `_h`, as a control on the comparison
    # itself: a grid too coarse to resolve either would agree with neither.
    ce = np.where(np.arange(N + 1) == 0, L ** -0.5,
                  ((-1.0) ** np.arange(N + 1)) * np.sqrt(2.0 / L))
    ae = 2 * np.pi * np.arange(N + 1) / L
    He = _h(L, N, ts)
    ctrl = 0.0
    for it, t in enumerate(ts):
        x = np.linspace(t - L / 2, L / 2, 100001)
        dx = x[1] - x[0]
        Pn = ce[:, None] * np.cos(ae[:, None] * x[None, :])
        Pm = ce[:, None] * np.cos(ae[:, None] * (x - t)[None, :])
        I = np.trapezoid(Pn[:, None, :] * Pm[None, :, :], dx=dx, axis=2)
        ctrl = max(ctrl, np.abs((I + I.T) - He[it]).max())
    print("      _h     vs the same, as a control:          max dev %.2e" % ctrl)
    VD.check(ctrl < 1e-6, "CHECK 5: the control -- the corpus's own `_h` passes the "
                          "same comparison, so it measures `_h_odd` and not the grid")
    y = np.linspace(-L / 2, L / 2, 200001)
    B = c * np.sin(a[:, None] * y[None, :])
    worst = 0.0
    for j in (1, 2):
        direct = np.trapezoid(B * np.exp(j * y / 2)[None, :], dx=y[1] - y[0], axis=1)
        worst = max(worst, np.abs(cond_row_odd(L, N, j) - direct).max())
    print("      cond_row_odd vs direct integration:       max dev %.2e" % worst)
    VD.check(worst < 1e-6, "CHECK 5: the odd condition rows agree with direct "
                           "integration")
    rng = np.random.default_rng(7)
    ac, ao = rng.standard_normal(N + 1), rng.standard_normal(N)
    u = np.linspace(-L / 2, L / 2, 2001)
    du = u[1] - u[0]
    g = ((ac * ce)[:, None] * np.cos(ae[:, None] * u[None, :])).sum(axis=0) \
        + (ao[:, None] * c * np.sin(a[:, None] * u[None, :])).sum(axis=0)
    K = eps(np.abs(u[:, None] - u[None, :]))
    E_brute = np.trapezoid(np.trapezoid(g[:, None] * g[None, :] * K, dx=du, axis=1),
                           dx=du)
    E_blocks = ac @ E_matrix(eps, L, N) @ ac + ao @ E_matrix_odd(eps, L, N) @ ao
    rel = abs(E_brute - E_blocks) / abs(E_blocks)
    print("      E on a mixed g: brute-force 2D %.6f, blocks %.6f, rel dev %.1e"
          % (E_brute, E_blocks, rel))
    VD.check(rel < 2e-4,
             "CHECK 5: E on an explicit even-plus-odd g equals the sum of the two "
             "block forms -- the decomposition, and the odd matrix, both checked "
             "against brute-force two-dimensional quadrature of the kernel")
    print()

    print("  (b) the inertia of -E on the FULL space, count and most negative.")
    mus = (2.0, 3.0, 8.0, 20.0) if QUICK else (1.5, 2.0, 2.5, 3.0, 4.0, 6.0, 8.0,
                                               14.0, 20.0, 30.0, 50.0)
    Ns = (60,) if QUICK else (60, 120)
    print("  %7s %5s" % ("mu", "N") + "".join("%18s" % ("codim %d" % k)
                                              for k in range(5)))
    stable = True
    for mu in mus:
        prev = None
        for N in Ns:
            cells = []
            for k in range(5):
                w = full_spec(eps, mu, N, k)
                cells.append(((w < 0).sum(), w[0] if w[0] < 0 else 0.0))
            if prev is not None:
                # 5e-3, where mg-d03b's even-only table holds to 1e-3.  The
                # sine basis imposes g(+-L/2) = 0, which the form does not, so
                # its coefficients decay like 1/n against the cosines' faster
                # decay and the odd block converges more slowly in N.  The
                # COUNTS are identical at every row, which is what the inertia
                # argument uses; the worst value drift is 2.4e-3, at mu = 50.
                stable &= all(cc[0] == p[0] and abs(cc[1] - p[1]) < 5e-3
                              for cc, p in zip(cells, prev))
            prev = cells
            print("  %7.2f %5d" % (mu, N)
                  + "".join("%10d %7.4f" % cc for cc in cells))
        if mu == 2.0:
            VD.check(prev[1][0] > 0,
                     "CHECK 5: at mu = 2 the codimension-ONE form is already "
                     "indefinite once odd g are admitted -- mg-d03b's 'ghat(0) = 0 "
                     "alone covers Theorem 1's whole range' is FALSE")
            VD.check(prev[2][0] == 0,
                     "CHECK 5: at mu = 2 the codimension-two form is still positive "
                     "-- Theorem 1 itself is reproduced on the full space")
    if len(Ns) > 1:
        VD.check(stable, "CHECK 5: the full-space inertia agrees between N = 60 and "
                         "N = 120 -- counts identical, values to 5e-3 (the odd block "
                         "converges more slowly in N than the even one; see the "
                         "comment above)")
    print()

    print("  (c) mu_c(k) on the full space, against mg-d03b's even-only column.")
    N = 60 if QUICK else 120
    nb = 22 if QUICK else 26
    print("  %3s %16s %16s %10s" % ("k", "mu_c, even only", "mu_c, even+odd", "ratio"))
    mcs = {}
    for k in (1, 2, 3, 4):
        mcs[k] = bisect(lambda mu: full_spec(eps, mu, N, k)[0], 1.02, MU_MAX, nb)
        print("  %3d %16.4f %16.4f %10.4f"
              % (k, MG_D03B_MUC[k], mcs[k], mcs[k] / MG_D03B_MUC[k]))
    print()
    VD.check(mcs[1] < 2.0,
             "CHECK 5: mu_c(1) < 2 -- one condition does NOT cover Theorem 1's "
             "support range, so the second condition is not inert there "
             "(mg-5210 sec 6's reading, which mg-d03b half-retired, stands)")
    VD.check(mcs[2] > 2.0,
             "CHECK 5: mu_c(2) > 2 -- Theorem 1's conclusion still survives past its "
             "stated hypothesis, so mu <= 2 is still an artefact of the proof")
    VD.check(mcs[2] < MG_D03B_MUC[2],
             "CHECK 5: mu_c(2) is BELOW mg-d03b's 6.174 -- that number is the even "
             "block only, and Theorem 1's hypothesis is a factor 1.4 from sharp, "
             "not a factor 3")
    print("  Theorem 1's conclusion holds to mu = %.3f, a factor %.2f on its stated"
          % (mcs[2], mcs[2] / 2.0))
    print("  mu <= 2, not the factor %.2f `sonin-margin.md` sec 4.2 prints.  The"
          % (MG_D03B_MUC[2] / 2.0))
    print("  hypothesis is still not sharp and still not vacuous.  BOTH corrections")
    print("  are to statements that are FALSE for W_lambda -> -W_lambda.")
    print()
    return mcs


def house_rule(mcs):
    print("HOUSE RULE, statement by statement.")
    print()
    print("  SIGN-BLIND -- about eps and -E alone, so nothing in them moves under")
    print("  W_lambda -> -W_lambda:")
    print("    * eps(rho) sqrt(rho) -> (1/2) sum lam(n) xi_n(0)^2 = 1.     CHECK 1")
    print("    * eps_hat(0) = 2 sum lam/(1+lam) A_n^2 = 5.3722 > 0.        CHECK 2")
    print("    * THE CEILING: for every k there is a finite L past which E has a")
    print("      positive direction in {ghat(i j/2) = 0, j < k}.           CHECK 3")
    print("    * log mu_c(k) <= Lambda(k), Lambda(k) ~ pi k / t_0.         CHECK 4")
    print("    * E splits over even + odd g.                               CHECK 5")
    print()
    print("  FALSE for W_lambda -> -W_lambda (the trace is fixed, W_inf flips), and")
    print("  these are the two corrections this script makes to `sonin-margin.md`:")
    print("    * Theorem 1's conclusion holds to mu = %.2f, NOT 6.17: a factor %.2f"
          % (mcs[2], mcs[2] / 2.0))
    print("      on its stated mu <= 2, not a factor 3.09.                 CHECK 5")
    print("    * At mu <= 2, ghat(0) = 0 alone is NOT enough: mu_c(1) = %.3f < 2."
          % mcs[1])
    print("      The second condition is doing work inside Theorem 1's own range.")
    print("                                                                CHECK 5")
    print()
    print("  The ceiling itself is sign-blind mathematics with a non-sign-blind")
    print("  consequence: 'E is inherently indefinite at low frequency' says nothing")
    print("  about W, and 'so Theorem 1's inequality must fail eventually' says")
    print("  everything.  The house rule sorts statements; it does not sort which")
    print("  half of a sentence carries the sign.")
    print()


if __name__ == "__main__":
    np.set_printoptions(linewidth=120)
    print(__doc__.split("--- CONVENTIONS")[0])
    pr = ProlateExact()
    eps = EpsTable(pr, np.log(MU_MAX) + 0.05, 6000 if QUICK else 24000)
    sym = Symbol(pr, npan=60 if QUICK else 110)
    t0 = bisect(lambda t: sym(t)[0], 0.5, 12.0)
    check1(pr)
    e0 = check2(pr, sym)
    check3(pr, sym, e0)
    check4(eps, sym, t0)
    mcs = check5(pr, eps)
    house_rule(mcs)
    VD.finish()
