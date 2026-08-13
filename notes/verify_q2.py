#!/usr/bin/env python3
"""Checks for `dilate-sum.md` (work item mg-9d43).  Needs `mpmath`; no numpy.

Q2 (`h1-mean-value.md` §9) asks for the passage from the single-term bound

    (Q1)  x |Phi(x)| <= K_1(c) |Phi(1)|     for x >= 1,   proved in
                                            `band-edge-connection.md` Thm 5.2

to the statement the reduction of H1 actually consumes,

    (P)   sup_{t>1} t |G(t)| <= K(c) |Phi(1)|,   G(t) = sum_{n>=1} Phi(n t),

with K subexponential in c.  `dilate-sum.md` proves (P) with K = O(log c).  This
script tests every step of that proof and measures how far the proved constant
sits above the truth.

The engineering unlock, and it is what mg-8462 could not find:  Poisson
summation applied to Phi restricted to [-1,1] turns the infinite sum of
EXPENSIVE OFF-BAND values into a FINITE sum of CHEAP ON-BAND ones.  With
c = 2 pi mu and h = 1/(mu t),

    t G(t) = (1/(2 mu mu_Phi)) sum'_{|k| <= floor(mu t)} Phi(k/(mu t))
             - t Phi(0)/2                                            (I)

-- floor(mu t) + 1 evaluations of Phi INSIDE the band, i.e. about mu t of them,
where the direct sum needs infinitely many outside it and each costs O(c n t)
Bessel values.  At mu = 5, t = 3 that is 15 cheap evaluations.  The two terms of
(I) are of size t Phi(0) and cancel down to |Phi(1)|, so the identity is a
catastrophic-cancellation computation: at c = 2 pi * 5, index 4, about 9 digits
go, and at c = 2 pi * 8 about 15.  That is what arbitrary precision is for and
the residual is reported rather than assumed.

CHECK 0 -- identity (I) itself, against a direct evaluation of sum_n Phi(n t)
           from the off-band Bessel series with the first three terms of the
           asymptotic expansion summed in closed form (Bernoulli polynomials) so
           that the truncation error is O(N^-3) rather than O(N^0).  The two
           routes share no code below `prolate_even`: (I) uses only on-band
           Legendre values, the direct route only off-band spherical Bessel
           values.  This is the check that would catch a wrong constant, a wrong
           sign, or a misplaced factor of 2 pi in (I).

CHECK 1 -- the two constants of the asymptotic form.  `dilate-sum.md` Lemma 3.1
           gives, exactly,
                x Phi(x) = a_1 sin(c x) + O(1/x),  a_1 = 2 Phi(1)/(c mu_Phi),
           i.e. alpha_infty = a_1 and **beta_infty = 0** -- no cosine.  The
           absence of the cosine is what the whole proof turns on, since
           sum_n cos(c n t)/n DIVERGES logarithmically at the resonances while
           sum_n sin(c n t)/n is the bounded sawtooth.  Measured by extracting
           (alpha, beta) from (u, u') with u = sqrt(x^2-1) Phi.

CHECK 2 -- the two bounds on the remainder W = Phi - a_1 sin(cx)/x that the
           proof uses (Lemma 4.2):  |W| <= B_1 |Phi(1)|/x for x >= 1, and
           |W| <= B_2 |Phi(1)|/x^2 for x >= sqrt 2.  The second is the whole
           content of Q2 and the first is free from Q1.

CHECK 3 -- the conclusion: sup_{t>1} t |G(t)| / |Phi(1)| against the proved
           K_P(c).  G has a JUMP of size pi a_1/t at every t with mu t integer
           (the sawtooth's jump; in (I) it is the endpoint term entering the
           Riemann sum), so the grid is stated in the variable mu t and the
           supremum is approached from each side of an integer.

CHECK 4 -- the three-mode combination.  (P) is stated against |Phi(1)| for the
           combination b_0 Phi_0 + b_2 Phi_4 + b_4 Phi_8, and the theorem is per
           mode, so passing to the combination needs
           sum_m |b_m| |Phi_{n_m}(1)| <= C |Phi_comb(1)| -- no cancellation at
           the endpoint.  Measured, not assumed.

Nothing here proves (P): the theorem quantifies over all x >= 1, all t > 1 and
all c, and a grid reaches none of them.  What a grid can do is falsify, and
calibrate.  Every inequality of `dilate-sum.md` §§3-5 is checked on a grid where
an algebra slip would show.

Two traps, both of which produced wrong output in earlier drafts of this script
and neither of which announces itself:

* `verify_h1.sph_j_all` returns the WRONG GLOBAL SIGN when sin(c x) is at
  rounding noise, i.e. at every integer x when mu is an integer.  See the
  docstring of `sph_j_all` below.  It is invisible in a modulus, which is why it
  survived two notes, and fatal here.
* G is DISCONTINUOUS at every t with mu t integral, and both routines must take
  the mid-value there.  `tG_direct` read gamma = c t mod 2 pi as 1e-148 rather
  than 0 and so returned the one-sided limit, disagreeing with identity (I) by
  half a jump on exactly the rows with mu t = 13.  See `tG_direct`.
  Relatedly, CHECK 3's grid must refine AT the jumps: a uniform grid in mu t
  under-reports the supremum by a factor of two, which is the same class of
  error `band-edge-connection.md` §7 had to correct in `h1-mean-value.md` §7.

Working precision 150 decimal digits in CHECK 0, 120 in CHECK 1 and 4, 80 in
CHECK 2 and 60 in CHECK 3 -- the last is set by the cancellation in identity (I),
which is reported in CHECK 0's own column and reaches 1e13.  Runtime ~12 minutes
at the defaults; `--quick` cuts it to about twenty seconds.
"""

import sys
import mpmath as mp
import verify_prolate_rate as VP
import verify_h1 as VH
from verdict import Verdict

QUICK = "--quick" in sys.argv

# The exit-code contract (mg-5995).  Three of the five checks state a criterion
# in their own prose and are wired to it: CHECK 0 ("a disagreement here refutes
# (I)", and the two jump identities it says are checked), CHECK 2 ("ratios above
# 1 refute the lemma") and CHECK 3 (the measured sup against the proved K_P).
# CHECK 1 reports a convergence with no rate claimed, and CHECK 4's chi_8/c^2 is
# a hypothesis that is documented to fail at small c -- neither is wired.
VD = Verdict()


# --- on-band evaluation, from the Legendre series -----------------------------


def legendre_all(y, kmax):
    """[P_0(y), ..., P_kmax(y)] by the three-term recurrence."""
    out = [mp.mpf(1)]
    if kmax >= 1:
        out.append(mp.mpf(y))
    for k in range(1, kmax):
        out.append(((2 * k + 1) * y * out[k] - k * out[k - 1]) / (k + 1))
    return out


def phi_onband(betas, y, coef=None):
    """Phi(y) for |y| <= 1 from Phi = sum_i beta_i Pbar_{2i}.

    `betas` should already be truncated to its significant head (see Mode): the
    full Bouwkamp vector has K = int(c) + 90 entries and evaluating Legendre to
    index 2K when only the first ~60 coefficients are above 1e-50 costs a factor
    of five for nothing.  `coef[i]` caches beta_i sqrt((4i+1)/2).
    """
    if coef is None:
        coef = [betas[i] * mp.sqrt(mp.mpf(4 * i + 1) / 2)
                for i in range(len(betas))]
    kmax = 2 * (len(betas) - 1)
    P = legendre_all(y, kmax)
    return sum(coef[i] * P[2 * i] for i in range(len(betas)))


# --- off-band evaluation, from the spherical-Bessel series --------------------


def sph_j_all(z, kmax, extra=200):
    """[j_0(z), ..., j_kmax(z)] by Miller downward recurrence, sign-robust.

    This is `verify_h1.sph_j_all` with ONE change, and the change fixes a latent
    defect in it that this note's computation is the first to be sensitive to.

    That function normalises on the sum rule sum_k (2k+1) j_k^2 = 1 -- correct,
    and its docstring explains at length why normalising on j_0(z) = sin z / z
    is not, since z = c x is a multiple of pi exactly when x is an integer (with
    c = 2 pi mu, mu integral) and there j_0 vanishes.  But it then fixes the
    remaining SIGN by the test  (out[0] * scale) * (sin(z)/z) < 0  -- which is
    the same ill-conditioned quantity, in the same place.  At x = 200, c = 6 pi
    the test compares against sin(z) = 1e-118, i.e. against rounding noise, and
    returns the wrong global sign about half the time.  Measured: Phi(200) comes
    back as +1.281e-8 between neighbours -1.374e-8 and -1.189e-8.

    It does not invalidate anything in `h1-mean-value.md` or
    `band-edge-connection.md`: every quantity those notes report is a MODULUS
    (sup |Phi|, sup x|Phi|, A = rho D^1/4), and a global sign flip is invisible
    in a modulus.  It is fatal here, because this note subtracts the explicit
    leading term a_1 sin(cx)/x from Phi and a flipped sign turns a remainder of
    size 1/x^2 into one of size 1/x.

    The fix: fix the sign by the two-term inner product against the closed forms
    j_0 = sin z / z and j_1 = sin z / z^2 - cos z / z.  Since
    max(|sin z|, |cos z|) >= 1/sqrt 2, the pair is never simultaneously small
    and the test is unconditionally well conditioned.
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
    s, co = mp.sin(z), mp.cos(z)
    j0 = s / z
    j1 = s / (z * z) - co / z
    if (out[0] * j0 + out[1] * j1) * scale < 0:
        scale = -scale
    return [out[i] * scale for i in range(kmax + 1)]


def phi_offband(a, c, x, kmax, want_deriv=False):
    """Phi(x) (and Phi'(x)) for x >= 1 from Phi = sum_k a_k j_k(c x)."""
    z = c * x
    j = sph_j_all(z, kmax + 1)
    val = sum(ak * j[k] for k, ak in a.items())
    if not want_deriv:
        return val
    # j_k'(z) = j_{k-1}(z) - (k+1)/z j_k(z)
    der = c * sum(ak * (j[k - 1] - (k + 1) / z * j[k]) for k, ak in a.items()
                  if k >= 1)
    k0 = 0
    if k0 in a:                                  # j_0'(z) = -j_1(z)
        der += c * a[k0] * (-j[1])
    return val, der


# --- the mode data ------------------------------------------------------------


class Mode:
    """One prolate mode Phi_n at bandwidth c, with everything the proof names."""

    def __init__(self, c, n, lam, chi, mu, p1, betas, tol=mp.mpf(10) ** -60):
        self.c, self.n, self.lam, self.chi, self.mu = c, n, lam, chi, mu
        self.betas = betas
        self.kmax = VH.legendre_trunc(betas, tol)
        self.a = VH.bessel_coeffs(betas, mu, self.kmax)
        # the significant head of the Legendre vector, and its cached weights:
        # everything beyond `kmax` is below `tol` and contributes nothing on band.
        self.bt = betas[: self.kmax // 2 + 1]
        self.coef = [self.bt[i] * mp.sqrt(mp.mpf(4 * i + 1) / 2)
                     for i in range(len(self.bt))]
        self.p1 = p1                                     # Phi(1)
        self.p0 = phi_onband(betas, mp.mpf(0))           # Phi(0)
        # Taylor data at the band edge, from the ODE (dilate-sum.md §2):
        #   Phi'(1)  = (chi - c^2)/2 Phi(1)
        #   Phi''(1) = [(chi - c^2 - 2) Phi'(1) - 2 c^2 Phi(1)] / 4
        self.d1 = (chi - c * c) / 2 * p1
        self.d2 = ((chi - c * c - 2) * self.d1 - 2 * c * c * p1) / 4
        # the asymptotic coefficients of x Phi(x) ~ a1 sin + a2 cos/x + a3 sin/x^2
        self.a1 = 2 * p1 / (c * mu)
        self.a2 = 2 * self.d1 / (c * c * mu)
        self.a3 = -2 * self.d2 / (c ** 3 * mu)

    def phi(self, x, want_deriv=False):
        return phi_offband(self.a, self.c, x, self.kmax, want_deriv)

    def phi_in(self, y):
        return phi_onband(self.bt, y, self.coef)


def modes(c, jmax=2, tol=mp.mpf(10) ** -60):
    out = []
    for (n, lam, chi, mu, p1, b) in VH.prolate_data(c, jmax=jmax):
        out.append(Mode(c, n, lam, chi, mu, p1, b, tol))
    return out


# --- identity (I): t G(t) from on-band values only ----------------------------


def tG_poisson(m, t):
    """t G(t) via Poisson summation -- on-band evaluations only.

    Phi restricted to [-1,1] has Fourier transform mu_Phi Phi(omega/c) at EVERY
    real omega (the finite-Fourier eigenrelation holds off the band too), so
    Poisson summation at step h = 2 pi/(c t) = 1/(mu t) reads

        sum'_{|k h| <= 1} Phi(k h) = (1/h) mu_Phi [Phi(0) + 2 G(t)],

    the left side a finite sum of on-band values and the right side the object
    wanted.  Valid pointwise because Phi 1_{[-1,1]} is of bounded variation
    (Dirichlet-Jordan); at the jump, i.e. when mu t is an integer, the endpoint
    terms carry weight 1/2, which is the prime on the sum.
    """
    mu_bw = m.c / (2 * mp.pi)                    # = mu, the bandwidth parameter
    s = mu_bw * t                                # = 1/h
    M = int(mp.floor(s))
    exact = abs(s - M) < mp.mpf(10) ** -(mp.mp.dps - 20)
    tot = m.phi_in(mp.mpf(0))
    for k in range(1, M + 1):
        v = m.phi_in(mp.mpf(k) / s)
        if k == M and exact:
            v /= 2
        tot += 2 * v                             # k and -k, Phi even
    return tot / (2 * mu_bw * m.mu) - t * m.p0 / 2


def tG_direct(m, t, N):
    """t G(t) by direct off-band summation with the first three asymptotic
    terms summed in closed form.

    Phi(x) = a1 sin(cx)/x + a2 cos(cx)/x^2 + a3 sin(cx)/x^3 + O(x^-4), so with
    alpha = c t mod 2 pi,
        sum_n a1 sin(c n t)/(n t)   = (a1/t) (pi - alpha)/2
        sum_n a2 cos(c n t)/(n t)^2 = (a2/t^2)(pi^2/6 - pi alpha/2 + alpha^2/4)
        sum_n a3 sin(c n t)/(n t)^3 = (a3/t^3)(pi^2 alpha/6 - pi alpha^2/4
                                                + alpha^3/12),
    and the residual sum over n <= N is done term by term, leaving O(N^-3).
    """
    two_pi = 2 * mp.pi
    al = mp.fmod(m.c * t, two_pi)
    if al < 0:
        al += two_pi
    # THE RESONANCE, and the first draft of this routine got it wrong.
    # gamma = c t mod 2 pi is 0 exactly when mu t is an integer, and there the
    # sawtooth is DISCONTINUOUS: sum_m sin(m gamma)/m equals (pi - gamma)/2 on
    # (0, 2 pi) but 0 AT gamma = 0, since every term is then identically zero.
    # Detect the resonance on mu t rather than on gamma: fmod returns ~1e-148
    # rather than 0, so the closed form silently returns the one-sided limit
    # pi/2 and the routine disagrees with identity (I) by half a jump.  That is
    # what the c = 10 pi, t = 2.6 rows (mu t = 13) reported before this fix,
    # and it is a real feature of G, not a defect in either route.  The mid-value
    # is the truth for the symmetric limit, and it is what (I) returns via the
    # prime on its sum -- so the two agree once both take it.
    s_par = m.c / (2 * mp.pi) * t
    if abs(s_par - mp.nint(s_par)) < mp.mpf(10) ** -(mp.mp.dps - 20):
        al = mp.mpf(0)
        S1, S2, S3 = mp.mpf(0), mp.pi ** 2 / 6, mp.mpf(0)
    else:
        S1 = (mp.pi - al) / 2
        S2 = mp.pi ** 2 / 6 - mp.pi * al / 2 + al * al / 4
        S3 = mp.pi ** 2 * al / 6 - mp.pi * al * al / 4 + al ** 3 / 12
    closed = m.a1 / t * S1 + m.a2 / t ** 2 * S2 + m.a3 / t ** 3 * S3
    resid = mp.mpf(0)
    for n in range(1, N + 1):
        x = n * t
        z = m.c * x
        asym = (m.a1 * mp.sin(z) / x + m.a2 * mp.cos(z) / x ** 2
                + m.a3 * mp.sin(z) / x ** 3)
        resid += m.phi(x) - asym
    return t * (closed + resid)


# --- the proved constants -----------------------------------------------------


def E_of_c(c):
    """band-edge-connection.md (4.1)."""
    cm = c - mp.sqrt(2)
    return 5 * mp.sqrt(2) / cm + (mp.sqrt(2) * c / 3 + 2) / cm ** 2


def K1_of_c(c):
    """band-edge-connection.md Thm 5.2 -- the proved Q1 constant."""
    return mp.mpf(2) ** mp.mpf("0.75") * mp.exp(E_of_c(c))


def constants(m):
    """(B1, B2, K_P) of dilate-sum.md Lemma 4.2 and Theorem 5.1."""
    c, K1 = m.c, K1_of_c(m.c)
    cmu = abs(c * m.mu)                          # = sqrt(2 pi Lambda_n c)
    B1 = K1 + 2 / cmu
    B2 = K1 * (6 * c + 1 / mp.sqrt(2))
    KP = mp.pi / cmu + B1 * (3 + mp.log(B2 / B1))
    return B1, B2, KP


# --- CHECK 0 -------------------------------------------------------------------


def check0():
    print("\nCHECK 0 -- the Poisson identity (I), against direct off-band summation")
    print("Two computations that share no code below `prolate_even`: (I) uses only")
    print("Phi INSIDE [-1,1] (Legendre series, floor(mu t)+1 points); the direct")
    print("route uses only Phi OUTSIDE it (spherical-Bessel series, N points, each")
    print("costing O(c n t) Bessel values) with three asymptotic terms summed in")
    print("closed form so the truncation is O(N^-3).  A disagreement here refutes")
    print("(I), which is the engineering claim of the whole note.\n")
    mp.mp.dps = 150
    N = 30 if QUICK else 60
    cs = [2 * mp.pi * 3] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3, 2 * mp.pi * 5]
    print("  c        n  t        t G(t) [Poisson]        rel. diff vs direct   "
          "cancellation")
    for cv in cs:
        c = mp.mpf(cv)
        for m in modes(c):
            for t in [mp.mpf("1.37"), mp.mpf("2.6")]:
                A = tG_poisson(m, t)
                B = tG_direct(m, t, N)
                rel = abs(A - B) / abs(B) if B != 0 else abs(A - B)
                canc = abs(t * m.p0 / 2) / abs(A) if A != 0 else mp.inf
                # The direct route's truncation is O(N^-3) at N = 30 or 60, and
                # the column measures 1e-9 to 3e-5.  1e-3 is a wide margin on
                # that and still catches the wrong-constant/wrong-sign/factor-
                # of-2-pi disagreements this check exists to catch, all O(1).
                VD.check(rel < mp.mpf("1e-3"),
                         "CHECK 0: identity (I) vs direct off-band sum "
                         "(c=%s, n=%d, t=%s)" % (mp.nstr(c, 6), m.n, mp.nstr(t, 4)))
                print("  %-8s %-2d %-8s %-23s %-21s %s"
                      % (mp.nstr(c, 6), m.n, mp.nstr(t, 4), mp.nstr(A, 12),
                         mp.nstr(rel, 4), "%.1e" % float(canc)))
    print("\n  The jump.  G is discontinuous where mu t is an integer.  Straddling")
    print("  mu t = 13 at c = 10 pi (t = 2.6), the jump must be pi a_1/t and the")
    print("  value AT the resonance must be the mid-value of the two one-sided")
    print("  limits -- the first because the sawtooth jumps by pi, the second")
    print("  because Dirichlet-Jordan gives (I) the mid-value and because every")
    print("  term sin(c m t) vanishes identically there.  Both are checked, and")
    print("  they are what a first draft of `tG_direct` got wrong (see its body).\n")
    mp.mp.dps = 150
    c = 2 * mp.pi * 5
    print("  n   t G(2.6-)             t G(2.6) [resonance]  t G(2.6+)             "
          "mid-value err   half-jump/(pi|a1|/2) - 1")
    for m in modes(c):
        lo = tG_poisson(m, mp.mpf("2.5999999"))
        at = tG_poisson(m, mp.mpf("2.6"))
        hi = tG_poisson(m, mp.mpf("2.6000001"))
        mid = (lo + hi) / 2
        half = (hi - lo) / 2
        # "Both are checked": the value at the resonance is the mid-value of the
        # one-sided limits, and the half-jump is pi|a_1|/2.  Both columns
        # measure ~2e-5, set by the 1e-7 straddle, not by either identity.
        VD.check(abs(mid - at) / abs(at) < mp.mpf("1e-3"),
                 "CHECK 0: G(2.6) is the mid-value at the resonance (n=%d)" % m.n)
        VD.check(abs(abs(half) / (mp.pi * abs(m.a1) / 2) - 1) < mp.mpf("1e-3"),
                 "CHECK 0: the jump is pi a_1/t (n=%d)" % m.n)
        print("  %-3d %-21s %-21s %-21s %-15s %s"
              % (m.n, mp.nstr(lo, 10), mp.nstr(at, 10), mp.nstr(hi, 10),
                 mp.nstr(abs(mid - at) / abs(at), 4),
                 mp.nstr(abs(half) / (mp.pi * abs(m.a1) / 2) - 1, 4)))


# --- CHECK 1 -------------------------------------------------------------------


def check1():
    print("\nCHECK 1 -- alpha_infty = 2 Phi(1)/(c mu_Phi) and beta_infty = 0")
    print("u = sqrt(x^2-1) Phi solves u'' + (c^2 + eps) u = 0 with")
    print("eps = (c^2 - chi + 1)/(x^2 - 1); writing u = alpha sin(cx) + beta cos(cx),")
    print("u' = c(alpha cos - beta sin), both alpha and beta converge.  The proof")
    print("needs beta_infty = 0 EXACTLY -- it is what makes the dilate sum a")
    print("sawtooth rather than a divergent log.  Reported relative to |a_1|.\n")
    mp.mp.dps = 120
    cs = [2 * mp.pi * 3] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3, 2 * mp.pi * 5]
    print("  c        n   x       alpha/a_1 - 1        beta/|a_1|")
    for cv in cs:
        c = mp.mpf(cv)
        for m in modes(c):
            for x in [mp.mpf(20), mp.mpf(200), mp.mpf(2000)]:
                v, d = m.phi(x, want_deriv=True)
                rt = mp.sqrt(x * x - 1)
                u = rt * v
                du = x * v / rt + rt * d
                s, co = mp.sin(c * x), mp.cos(c * x)
                al = u * s + du / c * co
                be = u * co - du / c * s
                print("  %-8s %-2d  %-7s %-20s %s"
                      % (mp.nstr(c, 6), m.n, mp.nstr(x, 5),
                         mp.nstr(al / m.a1 - 1, 4), mp.nstr(be / abs(m.a1), 4)))


# --- CHECK 2 -------------------------------------------------------------------


def check2():
    print("\nCHECK 2 -- the two remainder bounds, W(x) = Phi(x) - a_1 sin(cx)/x")
    print("Proved (dilate-sum.md Lemma 4.2):  x |W| <= B_1 |Phi(1)| for x >= 1,")
    print("and x^2 |W| <= B_2 |Phi(1)| for x >= sqrt 2, with B_2 = K_1(6c + 2^-1/2).")
    print("Ratios above 1 refute the lemma.  The grid runs to x = 40 in steps of")
    print("pi/(6c), which resolves the oscillation; it cannot see x > 40 and the")
    print("second column's quantity is bounded there by the same argument run from")
    print("X = 40 instead of sqrt 2, so that is an argument and not a measurement.\n")
    mp.mp.dps = 80
    cs = [2 * mp.pi * 3] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3, 2 * mp.pi * 5]
    XMAX = mp.mpf(20 if QUICK else 40)
    print("  c        n   sup x|W|/(B1|Phi(1)|)   sup x^2|W|/(B2|Phi(1)|)   "
          "B_1       B_2")
    for cv in cs:
        c = mp.mpf(cv)
        step = mp.pi / (6 * c)
        for m in modes(c, tol=mp.mpf(10) ** -60):
            B1, B2, _ = constants(m)
            r1 = r2 = mp.mpf(0)
            x = mp.mpf(1)
            while x <= XMAX:
                w = m.phi(x) - m.a1 * mp.sin(c * x) / x
                r1 = max(r1, x * abs(w) / (B1 * abs(m.p1)))
                if x >= mp.sqrt(2):
                    r2 = max(r2, x * x * abs(w) / (B2 * abs(m.p1)))
                x += step
            # "Ratios above 1 refute the lemma."
            VD.check(r1 <= 1, "CHECK 2: x|W| <= B_1 |Phi(1)| (c=%s, n=%d)"
                              % (mp.nstr(c, 6), m.n))
            VD.check(r2 <= 1, "CHECK 2: x^2|W| <= B_2 |Phi(1)| (c=%s, n=%d)"
                              % (mp.nstr(c, 6), m.n))
            print("  %-8s %-2d  %-23s %-25s %-9s %s"
                  % (mp.nstr(c, 6), m.n, mp.nstr(r1, 6), mp.nstr(r2, 6),
                     mp.nstr(B1, 5), mp.nstr(B2, 5)))


# --- CHECK 3 -------------------------------------------------------------------


def check3():
    print("\nCHECK 3 -- the conclusion:  sup_{t>1} t|G(t)| / |Phi(1)|  vs proved K_P(c)")
    print("G is DISCONTINUOUS: it jumps by pi a_1/t whenever s = mu t crosses an")
    print("integer, because the sawtooth (pi - gamma)/2 jumps by pi at gamma = 0 --")
    print("equivalently, because the endpoint sample Phi(+-1) enters the finite sum")
    print("of identity (I).  So the supremum is approached AT the jumps, and a")
    print("uniform grid in s would systematically miss it.  The grid used is: NSUB")
    print("uniform points per unit of s, PLUS geometric refinement 10^-1, ..., 10^-6")
    print("inward from each side of every integer.  The last column is the")
    print("sawtooth-only prediction (pi/2)|a_1|/|Phi(1)| = pi/sqrt(2 pi Lambda_n c),")
    print("which decays like c^-1/2 while the proved K_P grows like log c.\n")
    mp.mp.dps = 60
    cs = [2 * mp.pi * 3] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3,
                                        2 * mp.pi * 5, 2 * mp.pi * 8]
    SMAX = 20 if QUICK else 40
    NSUB = 4 if QUICK else 8
    EDGE = [mp.mpf(10) ** -j for j in range(1, 4 if QUICK else 7)]
    print("  c        n   sup t|G|/|Phi(1)|   at t       proved K_P(c)   ratio    "
          "(pi/2)|a1|/|Phi(1)|")
    for cv in cs:
        c = mp.mpf(cv)
        mu_bw = c / (2 * mp.pi)
        for m in modes(c, tol=mp.mpf(10) ** -45):
            _, _, KP = constants(m)
            best, bt = mp.mpf(0), None
            # t = 1 is s = mu, so start at floor(mu): the interval just above
            # t = 1 is where the O(1/t) part of the bound is largest and must
            # not be skipped.
            s = mp.floor(mu_bw)
            while s <= SMAX:
                offs = [mp.mpf(2 * i + 1) / (2 * NSUB) for i in range(NSUB)]
                offs += EDGE + [1 - e for e in EDGE]
                for o in offs:
                    t = (s + o) / mu_bw
                    if t <= 1:
                        continue
                    v = abs(tG_poisson(m, t))
                    if v > best:
                        best, bt = v, t
                s += 1
            r = best / abs(m.p1)
            # the conclusion of `dilate-sum.md` Thm 5.1: the measured sup must
            # sit below the proved K_P(c).  Measured, it sits ~20x below.
            VD.check(r <= KP, "CHECK 3: sup t|G|/|Phi(1)| <= K_P(c) proved "
                              "(c=%s, n=%d)" % (mp.nstr(c, 6), m.n))
            print("  %-8s %-2d  %-19s %-10s %-15s %-8s %s"
                  % (mp.nstr(c, 6), m.n, mp.nstr(r, 6), mp.nstr(bt, 5),
                     mp.nstr(KP, 6), mp.nstr(KP / r, 4),
                     mp.nstr(mp.pi / 2 * abs(m.a1) / abs(m.p1), 5)))


# --- CHECK 4 -------------------------------------------------------------------


def check4():
    print("\nCHECK 4 -- the three-mode combination, and hypothesis (C)")
    print("(P) is stated against |Phi(1)| of the combination")
    print("phi = b_0 Phi_0 + b_2 Phi_4 + b_4 Phi_8 (prolate-rate.md §2.1), while the")
    print("theorem is per mode.  Passing to the combination needs")
    print("sum_m |b_m| |Phi_{n_m}(1)| <= C |phi(1)|, i.e. no cancellation at the")
    print("band edge.  C is measured here; the mode weights come from the two")
    print("conditions phi(0) = 0, hat phi(0) = 0 of prolate-rate.md §2.1.")
    print("chi_n/c^2 is printed too: Q1, hence this note, needs it < 1.\n")
    mp.mp.dps = 120
    cs = [2 * mp.pi * 3] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3,
                                        2 * mp.pi * 5, 2 * mp.pi * 8]
    print("  c        |b_m Phi(1)| by mode (n=0,4,8)                  C = sum/|phi(1)|"
          "   chi_8/c^2")
    for cv in cs:
        c = mp.mpf(cv)
        ms = modes(c, jmax=4)
        idx = {0: ms[0], 4: ms[2], 8: ms[4]}
        # u_m = b_m psi_m(0);  sum u_m = 0, sum chi_m u_m = 0 with chi_m the
        # finite-Fourier eigenvalue sqrt(Lambda) up to sign, i.e. our mu_Phi
        # normalised: use CC's chi_m = sqrt(Lambda_{2m}) with alternating sign.
        ch = {}
        for k in (0, 4, 8):
            ch[k] = mp.sqrt(idx[k].lam)          # all three have chi ~ +1
        # u_4/u_2 = -(chi_0 - chi_2)/(chi_0 - chi_4) in CC's labels
        u = {0: None, 4: None, 8: None}
        u[8] = -(ch[0] - ch[4]) / (ch[0] - ch[8])
        u[4] = mp.mpf(1)
        u[0] = -(u[4] + u[8])
        terms, tot = [], mp.mpf(0)
        for k in (0, 4, 8):
            b = u[k] / idx[k].p0
            terms.append(b * idx[k].p1)
            tot += abs(b * idx[k].p1)
        phi1 = sum(terms)
        print("  %-8s %-14s %-14s %-14s  %-18s %s"
              % (mp.nstr(c, 6), mp.nstr(abs(terms[0]), 4), mp.nstr(abs(terms[1]), 4),
                 mp.nstr(abs(terms[2]), 4), mp.nstr(tot / abs(phi1), 6),
                 mp.nstr(idx[8].chi / (c * c), 5)))


def main():
    print(__doc__.split("\n\n")[0])
    print("mpmath %s;  QUICK=%s" % (mp.__version__, QUICK))
    check0()
    check1()
    check2()
    check3()
    check4()
    print("\nDone.")


if __name__ == "__main__":
    main()
    VD.finish()
