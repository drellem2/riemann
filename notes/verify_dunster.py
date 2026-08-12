#!/usr/bin/env python3
"""Numerical audit of the ONE imported input in the H0 chain (work item mg-ff96).

Needs `mpmath`; no `numpy`.  Imports the prolate apparatus of
[`verify_prolate_rate.py`](verify_prolate_rate.py) -- and nothing else from the
corpus, so that the eigenfunctions on the left of Dunster's equation are built
by machinery that has never seen Dunster.

WHAT IS BEING CHECKED.  `h0-lower-bound.md` (mg-6818) proves (H0) modulo one
imported statement, its (E), which it derives from

    T. M. Dunster, "Asymptotics of prolate spheroidal wave functions",
    J. Classical Analysis 11 (2017) 1-21, arXiv:1601.00699,
    eqs. (124) and (107).

Everything else in the -4 pi chain -- Q1, Q2, Q3, H0 -- was proved inside this
repository.  Dunster is the only load-bearing external input, and until this
script nobody here had evaluated it.  A numerical check is NOT a proof; what it
can catch, and what it is for, is the realistic failure mode: that we are
MISREADING the equation or applying it OUTSIDE its hypotheses.

The source was re-read from the arXiv LaTeX (`arxiv.org/e-print/1601.00699`,
file `PSWF_JCA.tex`, md5 667bb99e219c21468128dcbc222228fb, 1858 lines); the
equations are quoted verbatim in `dunster-check.md` Sec. 1 with line anchors.
Nothing below is copied from `h0-lower-bound.md`'s restatement.

    CHECK 0 -- apparatus, validated before use: our prolate solver against the
               gamma -> 0 Legendre limit and against a direct ODE residual;
               mpmath's parabolic cylinder functions against DLMF 12.7.2, the
               Wronskian 12.2.11 and the closed forms 12.2.6 / 12.2.8.
    CHECK 1 -- the symbol dictionary, re-derived: our Phi_n is shown to satisfy
               DUNSTER'S equation (1) as printed, with mu = m = 0, gamma = c and
               lambda = chi_n - c^2, by direct residual.  Then the hypothesis
               audit: sigma = sqrt(1 + gamma^-2 lambda) against his standing
               assumption (29), 0 <= sigma <= sigma_0 < 1.
    CHECK 2 -- eq. (107), a = lambda gamma^-1 + gamma = 2(n - m + 1/2) + O(1/gamma).
    CHECK 3 -- eq. (124) itself, both sides evaluated independently, on the whole
               interval 0 <= x <= 1 - delta_0 that he claims.
    CHECK 4 -- the step the corpus actually takes: (124) => (E), i.e. the Hermite
               limit on |X| <= R with x = X/lambda.  The total error is split
               into Dunster's part and the corpus's part, so that a failure can
               be attributed.
    CHECK 5 -- stability in working precision and in the Legendre truncation.

Runtime ~6 minutes at the defaults; `--quick` cuts it to about one.

--- CONVENTIONS, AND THE TWO COLLISIONS ---------------------------------------

Ours (`h0-lower-bound.md` Sec. 0):  ((1-y^2) Phi')' + (chi - c^2 y^2) Phi = 0 on
[-1,1], c = 2 pi mu, int_{-1}^1 Phi_n^2 = 1, prolate index n even.

Dunster's (1):  (1-z^2) y'' - 2 z y' + (lambda - m^2/(1-z^2) + gamma^2 (1-z^2)) y = 0.

  gamma = c,   lambda_Dunster = chi - c^2,   mu_Dunster = m = 0.

COLLISION 1: his lambda is not our lambda (ours is the dilation parameter,
mu = lambda^2, c = 2 pi mu).  Below, `lamD` is always his.
COLLISION 2: his mu is not our mu either.  Below, `m` is always his mu.
COLLISION 3 (not flagged in `h0-lower-bound.md`): the corpus writes chi_2 for
Connes' sqrt(Lambda_4), a CONCENTRATION eigenvalue, and chi_n for the prolate
SEPARATION constant.  Only the separation constant appears in this file.

His normalisation (19) is int_{-1}^1 {Ps_n^m}^2 = 2(n+m)!/((2n+1)(n-m)!), i.e.
Legendre's, not ours.  It drops out: (124) is normalised at x = 0, so it is a
statement about SHAPE and carries no normalisation at all.  That is a fact about
the equation, and it is checked rather than assumed (CHECK 3 uses only ratios).
"""

import sys
import time
import mpmath as mp
import verify_prolate_rate as P

QUICK = "--quick" in sys.argv

# c = 2 pi mu.  The ticket's range is c = 4 pi .. 24 pi; mu = 3 is added because
# every table in `h0-lower-bound.md` Sec. 7 starts there.
MUS = [2, 3, 4, 6, 8, 10, 12] if not QUICK else [2, 4, 8, 12]
NS = [0, 2, 4, 6, 8]
DELTA0 = mp.mpf("0.05")          # Dunster's delta_0; his claim is 0 <= x <= 1 - delta_0


def hdr(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)


# --- our prolate functions, evaluated ------------------------------------------


def _legendre_even(x, K):
    """[Pbar_0(x), Pbar_2(x), ..., Pbar_{2K-2}(x)], Pbar_k = sqrt((2k+1)/2) P_k."""
    kmax = 2 * K - 2
    p = [mp.mpf(1), mp.mpf(x)]
    for k in range(1, kmax + 1):
        p.append(((2 * k + 1) * x * p[k] - k * p[k - 1]) / mp.mpf(k + 1))
    return [p[2 * i] * mp.sqrt(mp.mpf(4 * i + 1) / 2) for i in range(K)]


class Prolate:
    """Phi_n(.) at bandwidth c, int_{-1}^1 Phi_n^2 = 1, Phi_n(0) > 0.

    n is the PROLATE index (= Dunster's n at m = 0); it is even, and it is the
    2j-th eigenvalue of the even Legendre tridiagonal, which CHECK 0 verifies
    against the gamma -> 0 limit chi_n -> n(n+1) rather than assuming.
    """

    def __init__(self, c, nmax=8, K=None):
        self.c = mp.mpf(c)
        self.jmax = nmax // 2
        self.K = K
        chis, betas, _ = P.prolate_even(self.c, self.jmax, K)
        self.chi = {2 * j: chis[j] for j in range(self.jmax + 1)}
        self.beta = {2 * j: betas[j] for j in range(self.jmax + 1)}
        self.Kn = len(betas[0])

    def val(self, n, x):
        pb = _legendre_even(x, self.Kn)
        b = self.beta[n]
        return sum(b[i] * pb[i] for i in range(self.Kn))

    def lamD(self, n):
        """Dunster's separation constant lambda_n^0(gamma^2)."""
        return self.chi[n] - self.c ** 2

    def sigma(self, n):
        """Dunster (29): sigma = sqrt(1 + gamma^-2 lambda).  Complex if chi > c^2."""
        return mp.sqrt(mp.mpc(1) + self.lamD(n) / self.c ** 2)

    def a(self, n):
        """Dunster (107) left side: a = lambda gamma^-1 + gamma  (= chi_n / c)."""
        return self.lamD(n) / self.c + self.c


# --- Dunster's right-hand side, transcribed from PSWF_JCA.tex ------------------
#
#   (108)  (1/2) rho^2 = 1 - sqrt(1 - x^2)                        :1305-:1309
#   (117)  Phi(rho)     = a ln(1 - rho^2/4) / (4 rho)             :1362-:1366
#   (116)  rhohat       = rho + gamma^-1 Phi(rho)                 :1357-:1360
#   (124)  Ps_n^m(x) = [Ps_n^m(0)/U(-a/2,0)] (rho/x)^{1/2} (1-x^2)^{-1/4}
#                      [ U(-a/2, rhohat sqrt(2 gamma))
#                        + O(gamma^-1 ln gamma) env U(-a/2, rhohat sqrt(2 gamma)) ]
#                                                                 :1426-:1439


def rho_of(x):
    """(rho, (rho/x)^{1/2}) from (108), in the form that is stable at x -> 0."""
    x = mp.mpf(x)
    s = mp.sqrt(1 - x * x)
    q = 2 / (1 + s)                      # (rho/x)^2
    return x * mp.sqrt(q), mp.power(q, mp.mpf(1) / 4)


def rhohat_of(x, a, gamma, perturb=True):
    """(116)+(117).  `perturb=False` drops the (116) correction, i.e. rhohat = rho.

    Note (111) prints phi(rho) = -a rho / (4 - zeta^2) and (110) prints the term
    gamma zeta phi(rho); both zetas must be read as rho -- zeta is the Liouville
    variable of Sec. 4 and does not occur in Sec. 5.  The reading is forced: with
    phi(v) = -a v/(4-v^2), (1/2 rho) int_0^rho phi = a ln(1 - rho^2/4)/(4 rho),
    which is (117) as printed.  It is also testable, and `perturb=False` tests
    it: if (117) were not the right correction, dropping it would not degrade
    the fit.
    """
    rho, pref = rho_of(x)
    if rho == 0 or not perturb:
        return rho, pref
    Phi = a * mp.log(1 - rho * rho / 4) / (4 * rho)
    return rho + Phi / gamma, pref


def U(a, z):
    return mp.pcfu(a, z)


def Ubar(a, z):
    """DLMF 12.2.21:  Ubar(a,x) = Gamma(1/2 - a) V(a,x)."""
    return mp.gamma(mp.mpf(1) / 2 - a) * mp.pcfv(a, z)


_XC = {}


def X_c(cD):
    """DLMF 14.15.23's X_c: the largest positive root of U(-c,x) = Ubar(-c,x)."""
    key = (mp.mp.prec, mp.nstr(cD, 25))
    if key in _XC:
        return _XC[key]
    f = lambda t: U(-cD, t) - Ubar(-cD, t)
    hi = 2 * mp.sqrt(cD) + 20
    step = mp.mpf(1) / 16
    x = hi
    while x > 0 and f(x) < 0:
        x -= step
    if x <= 0:
        _XC[key] = mp.mpf(0)
        return _XC[key]
    lo, hi = x, x + step
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    _XC[key] = (lo + hi) / 2
    return _XC[key]


def envU(cD, z):
    """DLMF 14.15.23, quoted at PSWF_JCA.tex:924-:926 as the meaning of `env`."""
    if z <= X_c(cD):
        return mp.sqrt(U(-cD, z) ** 2 + Ubar(-cD, z) ** 2)
    return 2 * U(-cD, z)


def dunster124(x, a, gamma, perturb=True):
    """The main term of (124), normalised at x = 0: RHS(x) / Ps(0).

    Returns (value, z, envelope) with z = rhohat sqrt(2 gamma).
    """
    a = mp.mpf(a)
    gamma = mp.mpf(gamma)
    rhohat, pref = rhohat_of(x, a, gamma, perturb)
    z = rhohat * mp.sqrt(2 * gamma)
    cD = a / 2
    val = pref * mp.power(1 - mp.mpf(x) ** 2, -mp.mpf(1) / 4) * U(-cD, z) / U(-cD, 0)
    return val, z, envU(cD, z) / abs(U(-cD, 0))


# --- the pi-convention Hermite functions of `h0-lower-bound.md` Sec. 0 ---------


def h(n, x):
    """h_n(x) = (2^n n!)^{-1/2} 2^{1/4} H_n(sqrt(2 pi) x) e^{-pi x^2}."""
    x = mp.mpf(x)
    return (mp.power(2, mp.mpf(1) / 4) / mp.sqrt(mp.mpf(2) ** n * mp.factorial(n))
            * mp.hermite(n, mp.sqrt(2 * mp.pi) * x) * mp.exp(-mp.pi * x * x))


# --- CHECK 0 -------------------------------------------------------------------


def check0():
    hdr("CHECK 0 -- apparatus, validated before it is used  [VERIFICATION]")

    print("\n(a) the prolate solver's index convention, from the gamma -> 0 limit.")
    print("    Ps_n^0(x, 0) = P_n(x) and chi_n -> n(n+1).  c = 1e-3.")
    print("    The ratio is signed: `prolate_even` fixes Phi_n(0) > 0, so Phi_n")
    print("    = -Pbar_n exactly when Pbar_n(0) < 0, i.e. n = 2, 6 (mod 4).  Ratio")
    print("    -1 is therefore the index matching, not a failure; (124) is a ratio")
    print("    statement and cannot see the overall sign either way.")
    pr = Prolate(mp.mpf("1e-3"), 8, K=40)
    print(f"    {'n':>3} {'chi_n':>22} {'n(n+1)':>8} {'Phi_n/Pbar_n at x=0.37':>26}")
    for n in NS:
        v = pr.val(n, mp.mpf("0.37"))
        pb = mp.sqrt(mp.mpf(2 * n + 1) / 2) * mp.legendre(n, mp.mpf("0.37"))
        print(f"    {n:>3} {mp.nstr(pr.chi[n], 16):>22} {n*(n+1):>8} "
              f"{mp.nstr(v / pb, 16):>26}")

    print("\n(b) the prolate solver against the ODE, at c = 8 pi.")
    print("    residual of ((1-y^2) Phi')' + (chi - c^2 y^2) Phi, relative to")
    print("    c^2 max|Phi|; derivatives by mp.diff.")
    c = 8 * mp.pi
    pr = Prolate(c, 8)
    for n in NS:
        f = lambda t: pr.val(n, t)
        y = mp.mpf("0.41")
        res = (mp.diff(lambda t: (1 - t * t) * mp.diff(f, t), y)
               + (pr.chi[n] - c * c * y * y) * f(y))
        scale = c * c * max(abs(f(mp.mpf("0.0"))), abs(f(y)))
        print(f"    n = {n}:  |residual| / (c^2 |Phi|) = {mp.nstr(abs(res) / scale, 4)}")

    print("\n(c) int_{-1}^1 Phi_n^2 = 1 (by construction: sum beta^2 = 1) and the")
    print("    Legendre coefficient tail, which controls the truncation.")
    for n in NS:
        b = pr.beta[n]
        print(f"    n = {n}:  sum beta^2 - 1 = {mp.nstr(sum(t*t for t in b) - 1, 4)}"
              f"   |beta_last| = {mp.nstr(abs(b[-1]), 4)}")

    print("\n(d) mpmath's parabolic cylinder functions.")
    print("    DLMF 12.7.2:  U(-n-1/2, z) = e^{-z^2/4} He_n(z),  z = 1.7")
    z = mp.mpf("1.7")
    for n in NS:
        lhs = U(-n - mp.mpf(1) / 2, z)
        rhs = mp.exp(-z * z / 4) * mp.power(2, -mp.mpf(n) / 2) * mp.hermite(n, z / mp.sqrt(2))
        print(f"    n = {n}:  ratio - 1 = {mp.nstr(abs(lhs / rhs - 1), 4)}")
    print("    DLMF 12.2.11 (Wronskian):  U V' - U' V = sqrt(2/pi),  a = -4.4321")
    a = -mp.mpf("4.4321")
    for zz in ["0.3", "2.9", "7.5"]:
        zz = mp.mpf(zz)
        w = (U(a, zz) * mp.diff(lambda t: mp.pcfv(a, t), zz)
             - mp.diff(lambda t: U(a, t), zz) * mp.pcfv(a, zz))
        print(f"    z = {zz}:  W / sqrt(2/pi) - 1 = "
              f"{mp.nstr(abs(w / mp.sqrt(2 / mp.pi) - 1), 4)}")
    print("    DLMF 12.2.6:  U(a,0) = sqrt(pi) / (2^{a/2+1/4} Gamma(3/4 + a/2))")
    u0 = mp.sqrt(mp.pi) / (mp.power(2, a / 2 + mp.mpf(1) / 4)
                           * mp.gamma(mp.mpf(3) / 4 + a / 2))
    print(f"    a = -4.4321:  ratio - 1 = {mp.nstr(abs(U(a, 0) / u0 - 1), 4)}")

    print("""
(e) Ubar, and with it DUNSTER'S OWN conventions, against his (75) and (76):
        U(-a/2, x)    ~ x^{(a-1)/2} e^{-x^2/4}                        :1930-:1934
        Ubar(-a/2, x) ~ (2/pi)^{1/2} Gamma(a/2+1/2) x^{-(a+1)/2} e^{x^2/4}
    This is what pins DLMF 12.2.21's Ubar to the Ubar in his `env'.  The error
    is O(x^-2), so the two columns must approach 1 by a factor 4 from x=30 to 60.""")
    print(f"    {'a':>10} {'x':>5} {'U / (75)':>22} {'Ubar / (76)':>22}")
    for aD in ["1", "9", "4.4321"]:
        aD = mp.mpf(aD)
        for xx in [mp.mpf(30), mp.mpf(60)]:
            ru = U(-aD / 2, xx) / (xx ** ((aD - 1) / 2) * mp.exp(-xx * xx / 4))
            rb = Ubar(-aD / 2, xx) / (mp.sqrt(2 / mp.pi) * mp.gamma(aD / 2 + mp.mpf(1) / 2)
                                      * xx ** (-(aD + 1) / 2) * mp.exp(xx * xx / 4))
            print(f"    {mp.nstr(aD, 6):>10} {int(xx):>5} {mp.nstr(ru, 14):>22} "
                  f"{mp.nstr(rb, 14):>22}")

    print("""
(f) X_c, the largest root of U(-c,x) = Ubar(-c,x) (DLMF 14.15.23).  env is
    discontinuous there BY CONSTRUCTION -- sqrt(U^2+Ubar^2) = sqrt(2) U on the
    left, 2U on the right -- so the jump must be exactly sqrt(2) - 1 = 0.414214.
    That it is, is the check that the root was found.""")
    for cD in ["0.5", "4.5", "8.5"]:
        cD = mp.mpf(cD)
        xc = X_c(cD)
        eps = mp.mpf("1e-12")
        print(f"    c = {cD}:  X_c = {mp.nstr(xc, 12)}   jump - (sqrt2 - 1) = "
              f"{mp.nstr(abs(envU(cD, xc + eps) / envU(cD, xc - eps) - 1) - (mp.sqrt(2) - 1), 4)}")


# --- CHECK 1 -------------------------------------------------------------------


def check1():
    hdr("CHECK 1 -- the symbol dictionary and the hypothesis audit  [VERIFICATION]")

    print("""
(a) The dictionary is re-derived, not accepted.  Our Phi_n is fed into DUNSTER'S
    equation (1) as printed at PSWF_JCA.tex:117-:121,

        (1-z^2) y'' - 2 z y' + (lambda - m^2/(1-z^2) + gamma^2 (1-z^2)) y = 0,

    with m = 0, gamma = c, lambda = chi_n - c^2, and the residual is measured.
    If the dictionary were wrong the residual would not vanish.""")
    c = 8 * mp.pi
    pr = Prolate(c, 8)
    y = mp.mpf("0.41")
    print(f"    c = 8 pi,  y = {y}")
    for n in NS:
        f = lambda t: pr.val(n, t)
        lamD = pr.lamD(n)
        res = ((1 - y * y) * mp.diff(f, y, 2) - 2 * y * mp.diff(f, y)
               + (lamD + c * c * (1 - y * y)) * f(y))
        scale = c * c * abs(f(y))
        print(f"    n = {n}:  lambda_D = {mp.nstr(lamD, 12):>18}"
              f"   |residual|/(c^2|Phi|) = {mp.nstr(abs(res) / scale, 4)}")

    print("""
(b) The standing hypothesis.  `h0-lower-bound.md` Sec. 0 and Sec. 5 report it as
    "lambda < 0, i.e. chi_n < c^2".  That is TRUE but it is not the whole
    hypothesis.  What the paper assumes throughout, at :466-:471, is (29):

        0 <= sigma = sqrt(1 + gamma^-2 lambda_n^m(gamma^2)) <= sigma_0 < 1,

    "where sigma_0 is an arbitrary positive constant" -- i.e. sigma bounded away
    from 1 UNIFORMLY, not merely below it.  sigma = sqrt(chi_n)/c, so this is
    chi_n <= sigma_0^2 c^2 with sigma_0 fixed.  sigma is also the location of the
    turning points x = +- sigma (:483-:487), and Sec. 5's whole construction is
    for a "pair of almost coalescent turning points near x = 0" (:1303-:1304),
    which is sigma -> 0, not merely sigma < 1.""")
    print(f"\n    {'mu':>4} {'c':>10} " + " ".join(f"{'n='+str(n):>10}" for n in NS)
          + "     <- sigma = sqrt(chi_n)/c")
    worst = mp.mpf(0)
    for mu in MUS:
        c = 2 * mp.pi * mp.mpf(mu)
        pr = Prolate(c, 8)
        row = []
        for n in NS:
            s = pr.sigma(n)
            sr = mp.re(s) if abs(mp.im(s)) < mp.mpf("1e-30") else s
            row.append(mp.nstr(sr, 6))
            if abs(mp.im(s)) > mp.mpf("1e-30"):
                row[-1] = "IMAG " + mp.nstr(abs(mp.im(s)), 4)
            else:
                worst = max(worst, mp.re(s))
        print(f"    {mu:>4} {mp.nstr(c, 8):>10} " + " ".join(f"{t:>10}" for t in row))
    print(f"\n    largest sigma over the whole grid: {mp.nstr(worst, 8)}")
    print("""    `h0-lower-bound.md` Sec. 5 states "the corpus's measured chi_n/c^2 runs
    0.020 to 0.64, so sigma <= 0.8 with room", citing `h1-mean-value.md` Sec. 5.
    That range was measured at n <= 4; the corpus's own vector carries index 8.
    Compare the column above.

    The threshold, computed rather than estimated: the smallest c at which
    chi_n(c) = c^2, i.e. sigma = 1, i.e. Dunster's lambda changes sign.  Below it
    the paper does not apply AT ALL -- it is the case he says is [9]'s, not his
    (:184-:189).  `verify_q1.py` CHECK 6 already records the same cell failing for
    Q1's hypothesis ("index 8 is the one that can fail in the range this project
    computes"); what is new is that it fails for Dunster's too, and that
    `h0-lower-bound.md` Sec. 5 does not carry it across.""")
    print(f"\n    {'n':>3} {'c* (sigma = 1)':>18} {'mu* = c*/2pi':>16}")
    for n in NS:
        lo, hi = mp.mpf("0.5"), mp.mpf(60)
        f = lambda cc: Prolate(cc, 8, K=int(cc) + 90).chi[n] - cc * cc
        if f(hi) > 0:
            print(f"    {n:>3} {'> 60':>18}")
            continue
        if f(lo) < 0:
            # no crossing at all: chi_0(c) = c^2/3 + O(c^4) < c^2 for every c > 0.
            print(f"    {n:>3} {'none':>18} {'-- sigma < 1 always':>16}")
            continue
        for _ in range(60):
            mid = (lo + hi) / 2
            if f(mid) > 0:
                lo = mid
            else:
                hi = mid
        cstar = (lo + hi) / 2
        print(f"    {n:>3} {mp.nstr(cstar, 12):>18} {mp.nstr(cstar / (2 * mp.pi), 10):>16}")

    print("""
(c) The other local hypotheses of Sec. 5, checked one at a time.

    (i)  "With the exception of Sec. 5, our results will be uniformly valid for
         m bounded, n small or large, and specifically 0 <= m <= n <= 2 pi^-1
         gamma (1-delta)" (:138-:146).  Sec. 5 IS the exception: it is the
         fixed-m-and-n section (:1284), and (107)'s O(gamma^-1) is stated as
         "valid for fixed m and n and gamma -> infinity" (:1300-:1301).  Our
         n in {0,2,4,6,8} is fixed as c -> infinity.                     -- OK
    (ii) (124) is derived under "Let us assume that Ps_n^m(x, gamma^2) (and
         hence m+n) is even" (:1396-:1397).  m = 0 and n even.           -- OK
         (The odd case is (125), which we never use.)
    (iii) lambda -> -infinity is assumed for the whole paper (:136-:138), citing
         [1, p. 186] = Arscott 1964.  For fixed n, lambda ~ -gamma^2.    -- OK
    (iv) mu = m and nu = n integers, i.e. the eigenvalue case, assumed
         throughout (:131-:135).                                          -- OK
    (v)  delta_0 in (0, 1 - sigma_0) is arbitrary (:783-:787).  This binds
         delta_0 from ABOVE, so the claimed interval 0 <= x <= 1 - delta_0 may
         be taken as large as we please; the implied constant depends on
         delta_0.  This script uses delta_0 = 0.05.                       -- OK
    (vi) The error bounds behind (120) are Dunster's own [10] (the
         double-turning-point theory), which was NOT opened -- here or in
         mg-6818.  So the O(gamma^-1 ln gamma) is itself an import inside the
         import.                                              -- STILL UNOPENED
    (vii) (107)'s O(gamma^-1) rests on (27) at :455-:461, which Dunster takes
         from [1, p. 186] = Arscott 1964 -- a SECOND-LEVEL external dependency
         that mg-6818 does not mention.  CHECK 2 tests it numerically.
                                                               -- STILL UNOPENED""")


# --- CHECK 2 -------------------------------------------------------------------


def check2():
    hdr("CHECK 2 -- eq. (107)  [VERIFICATION]")
    print("""
    (107)   a = lambda gamma^-1 + gamma = 2(n - m + 1/2) + O(gamma^-1),
    verbatim at PSWF_JCA.tex:1296-:1299, "the O(gamma^-1) term being valid for
    fixed m and n and gamma -> infinity".

    The first equality is a definition (it is how a enters (106) at :1290-:1294);
    what is testable is the second.  At m = 0 the claim is a = 2n + 1 + O(1/c),
    i.e. gamma * (a - 2n - 1) bounded as gamma -> infinity.  The column to read
    is the last one: if (107) held only with O(1) -- which is all (27) literally
    gives for lambda -- that column would grow like c.""")
    print("""
    The last column is also compared against the classical next term.  If
    chi_n = (2n+1) c - ((2n+1)^2 + 5)/8 + O(1/c) -- Meixner-Schaefke's expansion,
    which is what [1, p. 186] is -- then c(a - 2n - 1) -> -((2n+1)^2+5)/8, and
    the residual column must go to zero.  That turns (107) from "bounded" into a
    verified statement with its constant, WITHOUT opening Arscott.""")
    for n in NS:
        nxt = -(mp.mpf((2 * n + 1) ** 2) + 5) / 8
        print(f"\n    n = {n}    predicted limit -((2n+1)^2+5)/8 = {mp.nstr(nxt, 8)}")
        print(f"    {'mu':>4} {'c':>12} {'a = chi_n/c':>20} {'a - (2n+1)':>16} "
              f"{'c (a - 2n - 1)':>18} {'  + ((2n+1)^2+5)/8':>20}")
        for mu in MUS:
            c = 2 * mp.pi * mp.mpf(mu)
            pr = Prolate(c, 8)
            a = pr.a(n)
            d = a - (2 * n + 1)
            print(f"    {mu:>4} {mp.nstr(c, 10):>12} {mp.nstr(a, 14):>20} "
                  f"{mp.nstr(d, 10):>16} {mp.nstr(c * d, 10):>18} "
                  f"{mp.nstr(c * d - nxt, 8):>20}")


# --- CHECK 3 -------------------------------------------------------------------


def _grid(nx):
    """x-grid on (0, 1 - delta_0], denser near 0 where our application lives."""
    hi = 1 - DELTA0
    return [hi * mp.power(mp.mpf(i) / nx, mp.mpf(2)) for i in range(1, nx + 1)]


def check3():
    hdr("CHECK 3 -- eq. (124), both sides evaluated independently  [VERIFICATION]")
    print("""
    LHS   Phi_n(x) / Phi_n(0), from the Legendre-coefficient eigensolver.
    RHS   [U(-a/2, rhohat sqrt(2 gamma)) / U(-a/2, 0)] (rho/x)^{1/2} (1-x^2)^{-1/4},
          from mpmath's parabolic cylinder function.
    The two sides share no code.  a is taken EXACT, a = chi_n/c, which is the
    left-hand side of (107); the effect of replacing it by 2n+1 is in CHECK 4.

    (124) bounds LHS - RHS by O(gamma^-1 ln gamma) env U / U(-a/2, 0), with env
    as in DLMF 14.15.23 (Dunster says so at :924-:926).  So the quantity that
    must be BOUNDED is

        D := sup_x |LHS - RHS| / (env U / |U(-a/2,0)|)  divided by (ln c)/c,

    D is the ONLY quantity (124) constrains.  A raw ratio LHS/RHS is NOT a fair
    test of it: (124)'s error is additive against the envelope, so near a zero of
    U the ratio is unbounded by design and a large value there means nothing.
    The ratio is nevertheless reported with digits, but only at x = 0.9 and
    x = 0.95 -- both beyond the turning point x = sigma for every (c, n) in the
    grid except (mu <= 3, n = 8), so U is monotone there and has no zeros, and
    the ratio is a fair number.  A ratio at small x would be dominated by
    proximity to a zero of U and would say nothing.""")
    nx = 60 if QUICK else 200
    xs = _grid(nx)
    XPTS = [mp.mpf("0.9"), mp.mpf("0.95")]
    for n in NS:
        print(f"\n    n = {n}    (m = 0, m+n even, so (124) and not (125) applies)")
        print(f"    {'mu':>4} {'c':>10} {'sigma':>9} {'D = sup|L-R|/env':>17} "
              f"{'D c':>10} {'D c / ln c':>11} {'argmax x':>9}   "
              + "  ".join(f"{'L/R @ ' + mp.nstr(x, 3):>21}" for x in XPTS))
        for mu in MUS:
            c = 2 * mp.pi * mp.mpf(mu)
            pr = Prolate(c, 8)
            a = pr.a(n)
            phi0 = pr.val(n, mp.mpf(0))
            worst, argx = mp.mpf(0), mp.mpf(0)
            for x in xs:
                lhs = pr.val(n, x) / phi0
                rhs, z, env = dunster124(x, a, c)
                d = abs(lhs - rhs) / env
                if d > worst:
                    worst, argx = d, x
            rats = []
            for x0 in XPTS:
                l0 = pr.val(n, x0) / phi0
                r0, _, _ = dunster124(x0, a, c)
                rats.append(mp.nstr(l0 / r0, 17))
            sg = pr.sigma(n)
            sgs = (mp.nstr(mp.re(sg), 6) if abs(mp.im(sg)) < mp.mpf("1e-30")
                   else "IMAG")
            print(f"    {mu:>4} {mp.nstr(c, 8):>10} {sgs:>9} "
                  f"{mp.nstr(worst, 6):>17} {mp.nstr(worst * c, 6):>10} "
                  f"{mp.nstr(worst * c / mp.log(c), 6):>11} "
                  f"{mp.nstr(argx, 4):>9}   "
                  + "  ".join(f"{t:>21}" for t in rats))

    print("""
    Where the supremum sits, and what that costs.  `argmax x` is 1 - delta_0
    almost everywhere above: the worst disagreement is AT THE RIGHT ENDPOINT of
    the interval Dunster claims, which is exactly where his own split at
    :783-:787 puts the boundary between (124) and the Bessel approximation (61).
    So the constant in the O(gamma^-1 ln gamma) depends on delta_0, and must
    blow up as delta_0 -> 0.  Measured, at n = 4:""")
    print(f"\n    {'delta_0':>9} " + "  ".join(f"{'D, mu=' + str(m):>14}" for m in MUS[:4]))
    for d0 in ["0.5", "0.3", "0.1", "0.05", "0.02", "0.01"]:
        d0 = mp.mpf(d0)
        row = []
        for mu in MUS[:4]:
            c = 2 * mp.pi * mp.mpf(mu)
            pr = Prolate(c, 8)
            a = pr.a(4)
            phi0 = pr.val(4, mp.mpf(0))
            hi = 1 - d0
            w = mp.mpf(0)
            for i in range(1, 61):
                x = hi * mp.power(mp.mpf(i) / 60, 2)
                rhs, _, env = dunster124(x, a, c)
                w = max(w, abs(pr.val(4, x) / phi0 - rhs) / env)
            row.append(mp.nstr(w, 6))
        print(f"    {mp.nstr(d0, 4):>9} " + "  ".join(f"{t:>14}" for t in row))

    print("""
    Is the variable perturbation (116)+(117) doing any work?  The correction is
    gamma^-1 Phi(rho), the same order as the error (124) claims, so a check that
    passed with rhohat replaced by rho would not have tested our reading of
    (117) -- and (111) as printed has a zeta where a rho belongs, so the reading
    had to be reconstructed.  D with and without it, at delta_0 = 0.1:""")
    print(f"\n    {'n':>3} {'mu':>4} {'D with rhohat':>15} {'D with rho':>13} {'ratio':>9}")
    for n in [0, 4]:
        for mu in MUS[:4] + MUS[-1:]:
            c = 2 * mp.pi * mp.mpf(mu)
            pr = Prolate(c, 8)
            a = pr.a(n)
            phi0 = pr.val(n, mp.mpf(0))
            w1 = w0 = mp.mpf(0)
            for i in range(1, 121):
                x = mp.mpf("0.9") * mp.power(mp.mpf(i) / 120, 2)
                L = pr.val(n, x) / phi0
                r1, _, e1 = dunster124(x, a, c, True)
                r0, _, e0 = dunster124(x, a, c, False)
                w1 = max(w1, abs(L - r1) / e1)
                w0 = max(w0, abs(L - r0) / e0)
            print(f"    {n:>3} {mu:>4} {mp.nstr(w1, 6):>15} {mp.nstr(w0, 6):>13} "
                  f"{mp.nstr(w0 / w1, 6):>9}")


# --- CHECK 4 -------------------------------------------------------------------


def check4():
    hdr("CHECK 4 -- (124) => (E), the step the corpus actually takes  [VERIFICATION]")
    print("""
    `h0-lower-bound.md` Sec. 5 deduces from (124), at x = X/lambda with X in a
    fixed compact set,

        (E)   Phi_n(X/lambda)/Phi_n(0) = h_n(X)/h_n(0) + O(c^-1 ln c),
              uniformly on |X| <= R,

    by three simplifications: rhohat sqrt(2c) -> 2 sqrt(pi) X, the prefactor
    (rho/x)^{1/2}(1-x^2)^{-1/4} -> 1, and a -> 2n+1.  Each is claimed to cost
    O(lambda^-2) or O(c^-1).  Those steps are OURS, not Dunster's, so a failure
    there is a failure of this repository and not of the paper.  The error is
    therefore split:

        eD := sup |Phi_n(X/lam)/Phi_n(0) - RHS(124)|      Dunster's part
        eC := sup |RHS(124) - h_n(X)/h_n(0)|              the corpus's part
        eT := sup |Phi_n(X/lam)/Phi_n(0) - h_n(X)/h_n(0)| what (E) asserts

    all over |X| <= R with R = 4, matching `h0-lower-bound.md` Sec. 7 CHECK 7.

    `Xmax' is the part of |X| <= 4 that is actually inside Dunster's interval,
    namely lambda (1 - delta_0) = sqrt(mu) * 0.95.  Below mu = 17.7 that is less
    than 4, so at every bandwidth in this ticket's range (E) is being tested on
    LESS than the window `h0-lower-bound.md` CHECK 7 quotes.  Outside it the
    corpus's phi vanishes identically and h_n(X) does not, so the difference
    there is just |h_n(X)| -- 1e-22 at X = 4 -- which is why nothing turned on
    it; but it is not a test of (E).""")
    R = 4
    nX = 24 if QUICK else 80
    Xs = [mp.mpf(R) * i / nX for i in range(1, nX + 1)]
    for n in NS:
        print(f"\n    n = {n}")
        print(f"    {'mu':>4} {'c':>10} {'Xmax':>7} {'eD':>12} {'c eD/ln c':>12} "
              f"{'eC':>12} {'c eC':>12} {'eT':>12} {'c eT':>12}")
        for mu in MUS:
            c = 2 * mp.pi * mp.mpf(mu)
            lam = mp.sqrt(mp.mpf(mu))
            pr = Prolate(c, 8)
            a = pr.a(n)
            phi0 = pr.val(n, mp.mpf(0))
            h0 = h(n, mp.mpf(0))
            eD = eC = eT = mp.mpf(0)
            for X in Xs:
                x = X / lam
                if x >= 1 - DELTA0:
                    continue
                L = pr.val(n, x) / phi0
                Rv, _, _ = dunster124(x, a, c)
                H = h(n, X) / h0
                eD = max(eD, abs(L - Rv))
                eC = max(eC, abs(Rv - H))
                eT = max(eT, abs(L - H))
            print(f"    {mu:>4} {mp.nstr(c, 8):>10} "
                  f"{mp.nstr(min(mp.mpf(R), lam * (1 - DELTA0)), 4):>7} "
                  f"{mp.nstr(eD, 6):>12} "
                  f"{mp.nstr(eD * c / mp.log(c), 6):>12} {mp.nstr(eC, 6):>12} "
                  f"{mp.nstr(eC * c, 6):>12} {mp.nstr(eT, 6):>12} "
                  f"{mp.nstr(eT * c, 6):>12}")


# --- CHECK 5 -------------------------------------------------------------------


def check5():
    hdr("CHECK 5 -- stability  [numerical hygiene]")
    print("""
    The same three numbers at three working precisions and two Legendre
    truncations.  A digit that moves is a digit that was never there.""")
    mu, n = 8, 4
    c = 2 * mp.pi * mp.mpf(mu)
    x0 = mp.mpf("0.5")
    base = mp.mp.dps
    print(f"\n    mu = {mu}, n = {n}, x = {x0}")
    print(f"    {'dps':>5} {'K':>6} {'a = chi_n/c':>26} {'LHS':>26} {'RHS':>26}")
    for dps in [25, 40, 60]:
        for dK in [0, 40]:
            mp.mp.dps = dps
            cc = 2 * mp.pi * mp.mpf(mu)
            K = int(cc) + 90 + dK
            pr = Prolate(cc, 8, K=K)
            a = pr.a(n)
            L = pr.val(n, x0) / pr.val(n, mp.mpf(0))
            Rv, _, _ = dunster124(x0, a, cc)
            print(f"    {dps:>5} {K:>6} {mp.nstr(a, 20):>26} "
                  f"{mp.nstr(L, 20):>26} {mp.nstr(Rv, 20):>26}")
    mp.mp.dps = base


def main():
    mp.mp.dps = 40
    t0 = time.time()
    print(__doc__)
    print(f"working precision: {mp.mp.dps} digits" + ("   [--quick]" if QUICK else ""))
    for f in (check0, check1, check2, check3, check4, check5):
        f()
    print(f"\n[{time.time() - t0:.0f} s]")


if __name__ == "__main__":
    main()
