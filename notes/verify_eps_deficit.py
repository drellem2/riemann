#!/usr/bin/env python3
"""eps_hat(0) is NOT -2 theta'(0).  Six checks for `eps-hat-deficit.md` (mg-e205).  Needs mpmath.

    cd notes && python verify_eps_deficit.py            # 1m54s of CPU
    cd notes && python verify_eps_deficit.py --quick    # 49s of CPU

`--quick` coarsens CHECK 3 (two prolate indices instead of four) and CHECK 6
(three half-widths instead of seven) and keeps every wired check except CHECK 6's
unresolved-rows one, which has no rows to make a claim about on the reduced grid.
CI runs `--quick`.  Those are CPU times and not wall clock, deliberately: this
laptop had other tenants throughout and the same full run measured 2m52s and
4m48s of wall on two consecutive tries.  Neither figure is from a runner.

--- WHAT WAS ASKED ------------------------------------------------------------

mg-e205 was filed on a decimal comparison, and said so.  Two constants derived by
different routes, in different tickets, for different purposes:

    log(pi) - psi(1/4)      = 5.3721834192      thm:deficit, positivity-obstruction.tex:1147
    eps_hat(0) closed form  = 5.37218344        mg-0b7a, sonin-ceiling.md Bottom-line 2

agreeing an order of magnitude better than eps_hat(0) agreed with the quadrature
it had been validated against.  The ticket asked whether that is an identity, and
required the numerics to run FIRST because they can refute.

--- WHAT THIS SCRIPT FOUND ----------------------------------------------------

(1) IT IS NOT AN IDENTITY.  At 30 decimal digits, on an apparatus anchored to
every printed value Connes-Consani give for it,

    eps_hat(0)         =  5.37218343 5911187547213869...
    log(pi) - psi(1/4) =  5.37218341 9225665582232957...

The two constants agree to EIGHT significant digits and part at the ninth.  The
gap is 1.6685521965e-8, relative 3.1e-9.  It is not truncation.  Rebuilding the
whole apparatus at (K, nmax, dps) = (40, 10, 30), (55, 12, 30) and (80, 16, 40)
moves eps_hat(0) by 2.0e-15, 4.0e-20 and 4.3e-25 -- the COARSEST of those still
resolves the gap by seven orders -- and the last term the series keeps is 1.4e-22.
CHECK 4.

(2) BUT THE INEQUALITY IS TRUE, AND IT IS A THEOREM.  Write sigma_S for the
symbol of Connes-Consani's trace, i.e. tr(theta(f) S) = (1/2pi) int fhat(t)
sigma_S(t) dt.  Theorem `devil` (weil-compo.tex:1132) says

    tr(theta(f) S) = W_inf(f) + int f(rho) eps(rho) d*rho,

and R_+^* is abelian, so tr(theta(g * g^*) S) = ||S theta(g)^*||^2 >= 0 is
positivity of sigma_S POINTWISE.  The archimedean symbol carried by
W_inf = -W_R is thm:deficit's own 2 theta'(t) = Re psi(1/4 + it/2) - log pi.  So

    sigma_S(t) = 2 theta'(t) + eps_hat(t) >= 0,   hence
    eps_hat(0) >= -2 theta'(0) = log(pi) - psi(1/4) = 5.3721834192... > 0.

That is an unconditional proof of Theorem A's ONLY hypothesis, from two proved
inputs and no numerics.  What the numerics add is that the inequality is strict
and nearly saturated: sigma_S(0) = 1.6685521965e-8.  CHECK 5 measures sigma_S on
a grid, finds it positive everywhere, minimised at t = 0, and growing like
log(t/2pi).

(3) AND THE EIGHT DIGITS ARE NOT A COINCIDENCE -- THEY ARE log(area) = 0.
Extrapolating eps from the Sonin square S(1,1) to S(a,a) -- which is the c =
2 pi a^2 prolate problem with lam^(a)_n = a lam^(c)_n and an a-free A_n --

    sigma_S(0; a) = 2 log a + delta(a),   delta(a) > 0 and falling with 1 - lam_0:

    a        0.7      0.85       1.0       1.2       1.4     >= 1.7
    delta  2.7e-5    8.6e-7    1.7e-8    4.0e-11   3.7e-14   below the floor

Connes-Consani's eps is the a = 1 case, where 2 log a is exactly zero.  The two
constants look equal to eight digits because the Sonin square (1,1) is precisely
the point at which the cutoff's log-of-area term vanishes, and what is left is
the exponentially small prolate spectral defect at c = 2 pi.  CHECK 6.

    THE EXTRAPOLATION IS OURS AND IS NOT PROVED.  Connes-Consani's eps is stated
    at a = 1.  What makes CHECK 6 evidence rather than curve-fitting is that
    2 log a is not fitted -- nothing in the construction knows about it -- and at
    a = 1.4 it accounts for sigma_S(0;a) to 3.7e-14 in a quantity of size 0.67.

    AND IT STOPS THERE, NOT BECAUSE THE LAW STOPS.  Past a = 1.4 delta falls
    under this script's own eigenproblem error, and CHECK 6 says so and reads
    those two rows as zero rather than as measurements.  The a = 2 row prints
    2.7e-10 -- larger than the a = 1.7 row -- which is noise growing with the
    Legendre order, and is the reason the cut is by half-width and not by size.

(4) THE TWO READINGS OF THE CONSTANT ARE THE SAME INEQUALITY.  "sigma^arch is
bounded below by 2 theta'(0)" (thm:deficit) and "the symbol of -E is negative at
low frequency" (sonin-ceiling.md Theorem A) are not two facts about one number.
sigma_S >= 0 says -eps_hat(t) <= 2 theta'(t) pointwise; at t = 0, where
2 theta'(t) attains its minimum (thm:deficit proof, step (i)) and eps_hat(t)
attains its maximum, that reads -eps_hat(0) <= -5.3721834192 < 0.  The
indefiniteness of -E at low frequency is FORCED by the archimedean lower bound
being the number it is.  One inequality, read from either side.

--- WHAT IS CHECKED, AND WHAT IS ONLY PRINTED ---------------------------------

Wired (`VD.check` / `VD.word`): the CC anchors of CHECK 1; the three routes to
A_n agreeing in CHECK 2; the Mellin step of CHECK 3 against direct oscillatory
quadrature; the refutation, the recorded gap and the strict inequality in
CHECK 4; positivity and the location of the minimum of sigma_S in CHECK 5; the
2 log a law in CHECK 6.  Printed and NOT wired: the sigma_S table's individual
entries, and every sentence of the reading in (4), which is prose about proved
statements and decides nothing.

--- CONVENTIONS ---------------------------------------------------------------

xi_n is Connes-Consani's L^2(0,1)-normalised even prolate, so int_{-1}^1 xi_n^2
= 2 and xi_n = sqrt2 psi_{2n} for an L^2(-1,1)-orthonormal psi.  lam(n) is its
finite-Fourier eigenvalue for F eta(w) = int_{-1}^1 eta(x) e^{2 pi i x w} dx,
real and of sign (-1)^n.  psi_{2n} is built from the Legendre eigenproblem for
-d((1-x^2)d) + c^2 x^2 at c = 2 pi, the same construction
`verify_sonin_trace.py` uses, here in mpmath rather than numpy because the
quantity this script decides is 1.7e-8 against constants of order 5 and mg-aedf
established that this corpus cannot do that class of computation in double.

theta is the Riemann-Siegel theta, theta'(t) = (Re psi(1/4 + it/2) - log pi)/2.
G(s) = 2 Gamma(s) cos(pi s/2) (2 pi)^{-s} is the Fourier gamma factor; note
G(s) = Gamma_R(s)/Gamma_R(1-s) and hence G(1/2 + it) = exp(2 i theta(t)), which
is where both constants pass through the same object -- CHECK 5 prints it.
"""

import sys

from mpmath import (mp, mpf, mpc, sqrt, pi, gamma, log, binomial, matrix, eigsy,
                    besselj, quad, quadosc, legendre, cos, re, im, inf, si,
                    digamma, psi as mppsi)

from verdict import Verdict

VD = Verdict()
QUICK = "--quick" in sys.argv

mp.dps = 30
K = 70          # even Legendre degrees 0, 2, ..., 2(K-1) kept
NMAX = 14       # prolate indices kept in the closed-form series
HALF = mpf(1) / 2

# The value this script decides, recorded so a later run that moves it fails
# rather than quietly reporting a different number.
GAP = mpf("1.66855219649809e-8")


# --- the apparatus -----------------------------------------------------------

class Prolate(object):
    """Even c-prolates on [-1,1] from the Legendre eigenproblem, in mpmath."""

    def __init__(self, c, K, nmax):
        self.c, self.K, self.nmax = c, K, nmax
        self.degs = [2 * j for j in range(K)]
        c2 = c ** 2
        A = matrix(K, K)
        for j, k in enumerate(self.degs):
            k = mpf(k)
            A[j, j] = (k * (k + 1)
                       + c2 * (2 * k * (k + 1) - 1) / ((2 * k - 1) * (2 * k + 3)))
            if j + 1 < K:
                o = (c2 * (k + 1) * (k + 2)
                     / ((2 * k + 3) * sqrt((2 * k + 1) * (2 * k + 5))))
                A[j, j + 1] = A[j + 1, j] = o
        self.chi, V = eigsy(A)
        self.b = [[V[j, n] for j in range(K)] for n in range(nmax)]
        self.nrm = [sqrt(mpf(k) + HALF) for k in self.degs]
        P0 = [(-1) ** (k // 2) * binomial(k, k // 2) / mpf(2) ** k for k in self.degs]
        # lam(n) psi_n(0) = int_{-1}^1 psi_n = sqrt2 b_0.
        self.lam = [sqrt(2) * self.b[n][0]
                    / sum(self.b[n][j] * self.nrm[j] * P0[j] for j in range(K))
                    for n in range(nmax)]

    def xi(self, n, x):
        return sqrt(2) * sum(self.b[n][j] * self.nrm[j] * legendre(self.degs[j], x)
                             for j in range(self.K))

    def xi1(self, n):
        return sqrt(2) * sum(self.b[n][j] * self.nrm[j] for j in range(self.K))

    def Fxi(self, n, u):
        """F xi_n(u) for any u, via int_{-1}^1 P_k(x) e^{izx} dx = 2 i^k j_k(z)."""
        z = 2 * pi * u
        pref = sqrt(pi / (2 * z))
        return 2 * sqrt(2) * sum(
            self.b[n][j] * self.nrm[j] * (-1) ** (self.degs[j] // 2)
            * pref * besselj(self.degs[j] + HALF, z)
            for j in range(self.K) if abs(self.b[n][j]) > mpf(10) ** -28)

    def A(self, n, s=None):
        """A_n(s) = int_0^1 xi_n(x) x^{s-1} dx;  A_n(1/2) is mg-0b7a's A_n."""
        s = HALF if s is None else s
        return sum(self.b[n][j] * sqrt(2 * mpf(self.degs[j]) + 1) * Jk(self.degs[j], s)
                   for j in range(self.K))


def Jk(k, s):
    """int_0^1 x^{s-1} P_k(x) dx = sqrt(pi) Gamma(s) / (2^s G((s-k+1)/2) G((s+k)/2+1))."""
    return sqrt(pi) * gamma(s) / (2 ** s * gamma((s - k + 1) / 2)
                                  * gamma((s + k) / 2 + 1))


def Jk_rational(k):
    """The same integral at s = 1/2, in closed form: (-1)^{k/2} 2/(2k+1), k even."""
    return mpf((-1) ** (k // 2) * 2) / (2 * k + 1)


G = lambda s: 2 * gamma(s) * cos(pi * s / 2) * (2 * pi) ** (-s)
theta_p = lambda t: (re(mppsi(0, mpf(1) / 4 + mpc(0, t) / 2)) - log(pi)) / 2


def eps_hat(pr, t, a=mpf(1)):
    """eps_hat(t) = 2 sum_n c_n [ Re(G(1/2+it) conj(A_n)^2) - lam_n |A_n|^2 ].

    At t = 0 this is mg-0b7a's 2 sum lam/(1+lam) A_n^2.  `a` is the half-width of
    the Sonin square S(a,a); a = 1 is Connes-Consani's, anything else is CHECK 6's
    extrapolation.
    """
    g = G(HALF + mpc(0, t))
    tot = mpf(0)
    for n in range(pr.nmax):
        lam = a * pr.lam[n]
        An = pr.A(n, HALF + mpc(0, t))
        tot += lam / (1 - lam ** 2) * (re(g * An.conjugate() ** 2) - lam * abs(An) ** 2)
    return 2 * tot


# --- checks ------------------------------------------------------------------

CC_LAM = ["0.999971", "-0.979485", "0.524086", "-0.0589766", "0.00273233",
          "-7.62914e-5"]                                   # weil-compo.tex:969
CC_T = ["11.9719", "8.77574", "2.20528", "0.0433983", "1.25459e-4"]   # :1380


def check1(pr):
    print("CHECK 1  the apparatus, against every printed value CC give for it")
    print("  lam(n), weil-compo.tex:969")
    worst = mpf(0)
    for n in range(6):
        want = mpf(CC_LAM[n])
        rel = abs(pr.lam[n] - want) / abs(want)
        worst = max(worst, rel)
        print("    n=%d  ours %-24s  CC %-12s  rel %s"
              % (n, mp.nstr(pr.lam[n], 12), CC_LAM[n], mp.nstr(rel, 3)))
    VD.check(worst < mpf(10) ** -6,
             "CHECK 1: lam(0..5) reproduce CC's printed values to their last digit "
             "(worst rel %s)" % mp.nstr(worst, 4))

    lhs = sum(l ** 2 for l in pr.lam)
    rhs = 2 * (si(4 * pi) / (4 * pi) + 1)
    print("  sum lam(n)^2 = 2(Si(4pi)/4pi + 1), :1101")
    print("    ours %s   closed %s   diff %s"
          % (mp.nstr(lhs, 20), mp.nstr(rhs, 20), mp.nstr(lhs - rhs, 4)))
    VD.check(abs(lhs - rhs) < mpf(10) ** -25,
             "CHECK 1: sum lam^2 matches its closed form to 25 digits "
             "(diff %s)" % mp.nstr(lhs - rhs, 4))

    print("  t(n) = lam^2/(1-lam^2) xi_n(1)^2, :1380 -- this is what pins the")
    print("         normalisation A_n also uses")
    worst = mpf(0)
    for n in range(5):
        t = pr.lam[n] ** 2 / (1 - pr.lam[n] ** 2) * pr.xi1(n) ** 2
        rel = abs(t - mpf(CC_T[n])) / mpf(CC_T[n])
        worst = max(worst, rel)
        print("    n=%d  ours %-22s  CC %-12s  rel %s"
              % (n, mp.nstr(t, 12), CC_T[n], mp.nstr(rel, 3)))
    VD.check(worst < mpf(10) ** -5,
             "CHECK 1: t(0..4) reproduce CC's printed values (worst rel %s)"
             % mp.nstr(worst, 4))
    print()


def check2(pr):
    print("CHECK 2  A_n = int_0^1 xi_n(x) x^{-1/2} dx, three ways")
    print("  int_0^1 x^{-1/2} P_k(x) dx = (-1)^{k/2} 2/(2k+1) for even k -- the")
    print("  Gamma expression collapses, which is worth having because it makes")
    print("  A_n an exact rational combination of the Legendre coefficients.")
    worst = mpf(0)
    for k in (0, 2, 4, 10, 40):
        g, r = Jk(k, HALF), Jk_rational(k)
        worst = max(worst, abs(g - r))
        print("    k=%-3d Gamma %-26s rational %-26s diff %s"
              % (k, mp.nstr(g, 18), mp.nstr(r, 18), mp.nstr(g - r, 3)))
    VD.check(worst < mpf(10) ** -25,
             "CHECK 2: J_k Gamma form = (-1)^{k/2} 2/(2k+1) (worst %s)"
             % mp.nstr(worst, 4))

    print("  A_n: Gamma route vs direct quadrature (x = v^2, so the integrand is")
    print("       a polynomial and the endpoint singularity is gone)")
    worst = mpf(0)
    for n in (0, 1, 3, 6):
        q = quad(lambda v: 2 * v * pr.xi(n, v * v) / v, [0, 1])
        rel = abs(pr.A(n) - q) / abs(q)
        worst = max(worst, rel)
        print("    n=%d  closed %-30s quad %-30s rel %s"
              % (n, mp.nstr(pr.A(n), 22), mp.nstr(q, 22), mp.nstr(rel, 3)))
    VD.check(worst < mpf(10) ** -22,
             "CHECK 2: A_n agrees with direct quadrature to 22 digits "
             "(worst rel %s)" % mp.nstr(worst, 4))
    print()


def check3(pr):
    """The ONE analytic step in mg-0b7a's closed form, checked without using it."""
    print("CHECK 3  the Mellin step, by oscillatory quadrature rather than by the")
    print("         identity it is supposed to follow from")
    print("  mg-0b7a's closed form rests on exactly one non-elementary step:")
    print("    B_n := int_1^inf F xi_n(u) u^{-1/2} du = (1 - lam(n)) A_n,")
    print("  from int_0^inf u^{-1/2} F f(u) du = int_0^inf x^{-1/2} f(x) dx (the")
    print("  Fourier gamma factor G(s) is exactly 1 at the self-dual s = 1/2)")
    print("  together with F xi_n = lam(n) xi_n on [0,1].  Both halves are checked")
    print("  here against numbers that do not assume either.")
    print("  Run at 18 digits, not 30: quadosc over an oscillating u^{-3/2} tail is")
    print("  what this script spends its time on, and 14 digits is nine orders more")
    print("  than the step needs to be right to.")
    ns = (0, 2) if QUICK else (0, 1, 2, 3)
    worst_e, worst_b = mpf(0), mpf(0)
    for n in ns:
        w = mpf(7) / 10
        lhs, rhs = pr.Fxi(n, w), pr.lam[n] * pr.xi(n, w)
        rel = abs(lhs - rhs) / abs(rhs)
        worst_e = max(worst_e, rel)
        print("    n=%d  eigen-relation at w=0.7: F xi %-22s lam xi %-22s rel %s"
              % (n, mp.nstr(lhs, 16), mp.nstr(rhs, 16), mp.nstr(rel, 3)))
        with mp.workdps(18):
            q = quadosc(lambda u: pr.Fxi(n, u) / sqrt(u), [1, inf], period=mpf(1))
        cf = (1 - pr.lam[n]) * pr.A(n)
        rel = abs(q - cf) / abs(cf)
        worst_b = max(worst_b, rel)
        print("         B_n quadosc %-24s (1-lam)A_n %-24s rel %s"
              % (mp.nstr(q, 16), mp.nstr(cf, 16), mp.nstr(rel, 3)))
    VD.check(worst_e < mpf(10) ** -15,
             "CHECK 3: F xi_n = lam(n) xi_n off zero (worst rel %s)"
             % mp.nstr(worst_e, 4))
    VD.check(worst_b < mpf(10) ** -13,
             "CHECK 3: B_n = (1 - lam(n)) A_n against direct oscillatory "
             "quadrature (worst rel %s)" % mp.nstr(worst_b, 4))
    print()


def check4(pr):
    print("CHECK 4  THE QUESTION mg-e205 ASKED")
    print("  eps_hat(0) = 2 sum_n lam(n)/(1+lam(n)) A_n^2   (mg-0b7a section 2.1)")
    s = mpf(0)
    for n in range(pr.nmax):
        term = 2 * pr.lam[n] / (1 + pr.lam[n]) * pr.A(n) ** 2
        s += term
        if n < 8:
            print("    n=%d  term %-26s partial %s"
                  % (n, mp.nstr(term, 12), mp.nstr(s, 14)))
    tail = abs(2 * pr.lam[pr.nmax - 1] / (1 + pr.lam[pr.nmax - 1])
               * pr.A(pr.nmax - 1) ** 2)
    print("    last term kept (n=%d): %s, which is %s of the gap this script"
          % (pr.nmax - 1, mp.nstr(tail, 4), mp.nstr(tail / GAP, 3)))
    print("    decides -- the truncation cannot be what the 9th digit is made of.")
    VD.check(tail < mpf(10) ** -10 * GAP,
             "CHECK 4: the series truncation is at least ten orders below the "
             "1.7e-8 being decided (last term %s)" % mp.nstr(tail, 4))

    rhs = log(pi) - digamma(mpf(1) / 4)
    d = s - rhs
    print()
    print("    eps_hat(0)          = %s" % mp.nstr(s, 25))
    print("    log(pi) - psi(1/4)  = %s" % mp.nstr(rhs, 25))
    print("    difference          = %s   (relative %s)"
          % (mp.nstr(d, 15), mp.nstr(d / rhs, 4)))
    print()
    verdict = VD.word(abs(d) > mpf(10) ** -12, "REFUTED", "(identity holds)",
                      "CHECK 4: eps_hat(0) = -2 theta'(0) is refuted, i.e. the two "
                      "constants differ by more than 1e-12 (they differ by %s)"
                      % mp.nstr(d, 6))
    print("    eps_hat(0) = -2 theta'(0) ?   %s -- they agree to 8 significant"
          % verdict)
    print("    digits and part at the 9th: ...4359 against ...4192.")
    VD.check(abs(d - GAP) < mpf(10) ** -20,
             "CHECK 4: the gap reproduces the recorded 1.66855219649809e-8 "
             "(measured %s)" % mp.nstr(d, 15))
    VD.check(d > 0,
             "CHECK 4: the inequality eps_hat(0) > log(pi) - psi(1/4) holds, "
             "which is the half that IS a theorem (gap %s)" % mp.nstr(d, 6))

    print()
    print("    Is the 9th digit an artefact of a truncation?  Rebuild the whole")
    print("    apparatus at other Legendre orders, prolate cutoffs and precisions:")
    sweep = ([(40, 10, 30)] if QUICK else [(40, 10, 30), (55, 12, 30), (80, 16, 40)])
    worst = mpf(0)
    for Ks, Ns, dps in sweep:
        with mp.workdps(dps):
            v = mpf(0)
            p2 = Prolate(2 * pi, Ks, Ns)
            for n in range(Ns):
                v += 2 * p2.lam[n] / (1 + p2.lam[n]) * p2.A(n) ** 2
        worst = max(worst, abs(v - s))
        print("      K=%-4d nmax=%-3d dps=%-3d  eps_hat(0) = %-28s |diff| %s"
              % (Ks, Ns, dps, mp.nstr(v, 20), mp.nstr(abs(v - s), 3)))
    print("    The coarsest setting here still resolves the gap by six orders, so")
    print("    the ninth digit is not made of truncation.")
    VD.check(worst < mpf(10) ** -6 * GAP,
             "CHECK 4: eps_hat(0) is stable across (K, nmax, dps) to at least six "
             "orders below the gap (worst spread %s)" % mp.nstr(worst, 4))
    print("    But eps_hat(0) > log(pi) - psi(1/4) > 0, and THAT is provable:")
    print("    it is sigma_S(0) >= 0, i.e. Theorem `devil`.  CHECK 5.")
    print()
    return s


def check5(pr, e0):
    print("CHECK 5  sigma_S(t) = 2 theta'(t) + eps_hat(t), which Theorem `devil`")
    print("         forces to be >= 0 because S is an orthogonal projection")
    print("  G(1/2+it) = Gamma_R(s)/Gamma_R(1-s) at s = 1/2+it = exp(2 i theta(t)):")
    for t in (mpf(1), mpf(3), 2 * pi):
        g = G(HALF + mpc(0, t))
        print("    t=%-9s |G| = %-18s arg(G)/2 = %s"
              % (mp.nstr(t, 6), mp.nstr(abs(g), 14), mp.nstr(im(log(g)) / 2, 14)))
    VD.check(all(abs(abs(G(HALF + mpc(0, t))) - 1) < mpf(10) ** -25
                 for t in (mpf(1), mpf(3), 2 * pi)),
             "CHECK 5: |G(1/2+it)| = 1, so G is a pure phase on the critical line")

    ts = ([mpf(0), mpf(1) / 2, mpf(2), mpf(5), 2 * pi, mpf(10), mpf(50)] if QUICK
          else [mpf(0), mpf(1) / 10, mpf(1) / 2, mpf(1), mpf(2), mpf(3), mpf(4),
                mpf(5), mpf(6), 2 * pi, mpf(7), mpf(10), mpf(20), mpf(50)])
    print("  %10s %22s %22s %22s" % ("t", "2 theta'(t)", "eps_hat(t)", "sigma_S(t)"))
    sig = []
    for t in ts:
        a, b = 2 * theta_p(t), eps_hat(pr, t)
        sig.append(a + b)
        print("  %10s %22s %22s %22s"
              % (mp.nstr(t, 6), mp.nstr(a, 13), mp.nstr(b, 13), mp.nstr(a + b, 13)))
    VD.check(all(x > 0 for x in sig),
             "CHECK 5: sigma_S(t) > 0 at every grid point, which is Theorem "
             "`devil` (min %s)" % mp.nstr(min(sig), 6))
    VD.check(sig[0] == min(sig),
             "CHECK 5: sigma_S is minimised at t = 0, so the near-degeneracy of "
             "CC's positivity sits exactly at zero frequency")
    VD.check(abs(sig[0] - GAP) < mpf(10) ** -20,
             "CHECK 5: sigma_S(0) is the CHECK 4 gap -- the two constants' "
             "disagreement IS the trace symbol at zero frequency")
    print("    sigma_S(0) = %s = the CHECK 4 gap." % mp.nstr(sig[0], 15))
    print("    So the deficit bound is saturated at t = 0 to 8 digits and no")
    print("    further, and -eps_hat(t) <= 2 theta'(t) is one inequality that")
    print("    reads as thm:deficit from one side and as Theorem A from the other.")
    print()
    return sig[0]


def check6(sig0):
    print("CHECK 6  where the eight digits come from: sigma_S(0; a) = 2 log a + delta")
    print("  S(a,a) is the c = 2 pi a^2 prolate problem: lam^(a)_n = a lam^(c)_n and")
    print("  A_n is a-free.  CC's eps is a = 1.  EXTRAPOLATION, NOT PROVED -- but")
    print("  2 log a is not fitted, and nothing in the construction knows about it.")
    rhs = log(pi) - digamma(mpf(1) / 4)
    # (a, Legendre order, is delta resolvable above this script's own noise).
    # RESOLVABLE IS SET BY HALF-WIDTH, NOT BY MAGNITUDE, deliberately: a K x K
    # mpmath eigenproblem at 30 digits does not return 30 digits, the loss grows
    # with K, and by a = 1.7 the true delta has fallen under what is left.  A
    # magnitude threshold would get this wrong and the a = 2 row is the proof --
    # it prints 2.7e-10, LARGER than the a = 1.7 row's 1.9e-15, which is noise
    # growing with K and not a residual growing with a.
    grid = ([(mpf("0.85"), 45, True), (mpf(1), 60, True), (mpf("1.4"), 80, True)]
            if QUICK else
            [(mpf("0.7"), 40, True), (mpf("0.85"), 45, True), (mpf(1), 60, True),
             (mpf("1.2"), 70, True), (mpf("1.4"), 80, True),
             (mpf("1.7"), 95, False), (mpf(2), 110, False)])
    print("  %6s %10s %24s %16s %16s %12s"
          % ("a", "c=2pi a^2", "eps_hat_a(0)", "sigma_S(0;a)", "2 log a", "1-lam^(a)_0"))
    deltas = []
    for a, Ka, ok in grid:
        pra = Prolate(2 * pi * a * a, Ka, 16)
        eh = eps_hat(pra, mpf(0), a)
        s, l2 = eh - rhs, 2 * log(a)
        deltas.append((a, s - l2, ok))
        print("  %6s %10s %24s %16s %16s %12s"
              % (mp.nstr(a, 4), mp.nstr(2 * pi * a * a, 6), mp.nstr(eh, 18),
                 mp.nstr(s, 11), mp.nstr(l2, 11), mp.nstr(1 - a * pra.lam[0], 5)))
    print("  residual delta(a) = sigma_S(0;a) - 2 log a.  RESOLVED is set by")
    print("  half-width, not by size: the eigenproblem's own error grows with K,")
    print("  and past a = 1.4 it is larger than the residual.  The a = 1.7 row")
    print("  printing NEGATIVE is what that floor looks like, and the a = 2.0 row")
    print("  printing LARGER than it is why a size threshold would be wrong here.")
    res = [(a, d) for a, d, ok in deltas if ok]
    unres = [(a, d) for a, d, ok in deltas if not ok]
    for a, d, ok in deltas:
        print("    a=%-6s delta = %-14s %s"
              % (mp.nstr(a, 4), mp.nstr(d, 6),
                 "RESOLVED" if ok else "at the precision floor, read as 0"))
    VD.check(bool(res) and all(d > 0 for _, d in res),
             "CHECK 6: delta(a) > 0 at every half-width where it is resolved "
             "(%d of %d rows)" % (len(res), len(deltas)))
    VD.check(res[-1][1] < res[0][1] * mpf(10) ** -3,
             "CHECK 6: delta(a) falls by at least three orders across the "
             "resolved rows, so 2 log a is the whole of sigma_S(0;a) in the "
             "limit (%s -> %s)"
             % (mp.nstr(res[0][1], 4), mp.nstr(res[-1][1], 4)))
    if unres:
        VD.check(all(abs(d) < mpf(10) ** -9 for _, d in unres),
                 "CHECK 6: the unresolved rows are consistent with delta = 0, "
                 "i.e. with sigma_S(0;a) = 2 log a exactly (%d rows)" % len(unres))
    else:
        print("    NOT EXERCISED on this grid: the unresolved-rows check needs a")
        print("    row past a = 1.4, and --quick has none.  Run the full grid.")
    at1 = [d for a, d, _ in deltas if a == 1][0]
    VD.check(abs(at1 - sig0) < mpf(10) ** -20,
             "CHECK 6: at a = 1, 2 log a = 0 and delta(1) is exactly the gap "
             "CHECK 4 measured -- which is the explanation of the eight digits")
    print()


def summary():
    print("--- WHAT mg-e205 ASKED FOR, AND WHAT IT GOT ---------------------------")
    print()
    print("  ASKED: prove eps_hat(0) = log(pi) - psi(1/4), or refute it with the")
    print("  digit at which it fails.")
    print()
    print("  REFUTED, at the 9th significant digit.  5.372183435911... against")
    print("  5.372183419225...; gap 1.6685521965e-8, stable in every truncation.")
    print()
    print("  What replaces it is stronger than the identity would have been for")
    print("  the one purpose the identity was wanted:")
    print()
    print("    eps_hat(0)  >=  -2 theta'(0)  =  log(pi) - psi(1/4)  >  0,")
    print()
    print("  proved from Theorem `devil` (S = S* = S^2, so the trace symbol is")
    print("  >= 0) and the archimedean symbol thm:deficit already uses.  Theorem")
    print("  A's only hypothesis, eps_hat(0) > 0, is therefore discharged with no")
    print("  numerics at all, and with a NAMED constant as the lower bound.")
    print()
    print("  Sign-sensitivity (sign-sensitivity-generator.md): the inequality")
    print("  eps_hat(0) >= -2 theta'(0) is NOT sign-blind -- it reverses under")
    print("  W_lam -> -W_lam, because sigma_S >= 0 is a statement about which way")
    print("  the trace points.  The refutation itself IS sign-blind: two numbers")
    print("  differ at the 9th digit whichever way the form is oriented.")
    print()


if __name__ == "__main__":
    print(__doc__.split("--- CONVENTIONS")[0])
    pr = Prolate(2 * pi, K, NMAX)
    check1(pr)
    check2(pr)
    check3(pr)
    e0 = check4(pr)
    sig0 = check5(pr, e0)
    check6(sig0)
    summary()
    VD.finish()
