#!/usr/bin/env python3
"""H0/Q4: is ||g||^2 bounded below?  (work item mg-6818)

Companion to `h0-lower-bound.md`.  Needs mpmath; no numpy.  Imports the prolate
apparatus of `verify_prolate_rate.py`, the Legendre machinery of `verify_h1.py`,
the mode builder of `verify_q2.py` (whose `sph_j_all` is the FIXED one --
mg-9d43; nothing here uses an off-band value in any case), and the three-mode
near-radical vector `Comb` of `verify_q3.py`.

WHAT IS BEING TESTED.  `h1-mean-value.md` §9 row Q4 and the paper's Hypothesis
H0 (`paper/positivity-obstruction.tex:1544`) describe H0 as "a mean value of
|zeta(1/2+it)|^2 against an explicit weight".  The claim under test here is that
this is the wrong description: the mean-value identity is one ROUTE to ||g||^2
and not the requirement, and along that route the only thing that matters is
that the WEIGHT does not degenerate.  Every check below is on-band prolate
arithmetic plus one fixed Hermite function; zeta appears in exactly one check,
CHECK 5, and only to reproduce a number CHECK 3 already has without it.

The identity everything runs on (§2 of the note, exact, no asymptotics):

    E phi(u) = u^{1/2} sum_{n <= lambda/u} phi(n u),  phi(x) = lambda^{-1/2} Phi(x/lambda)

so with u = lambda / t, so that t = 1 is the top of the window u = lambda and
t = mu is the bottom u = 1/lambda,

    ||g||^2 = int_1^mu S(t)^2 dt / t^2,      S(t) = sum_{1 <= n <= t} Phi(n/t),
    ||r||^2 = int_mu^infty S(t)^2 dt / t^2,

with EVERY argument n/t of Phi in [0,1] -- on band.  S(t) = 0 for t < 1, which
is supp E phi subset (0, lambda].

CHECK 0 -- apparatus.  The three-mode vector is admissible (Phi(0) = 0,
           int Phi = 0) and normalised; S(t) reproduces `verify_q3.Comb.R`
           where the two parametrisations overlap.  Stability at two precisions.

CHECK 1 -- the limit vector.  phi_inf = sqrt(8/11) (h_4 - sqrt(3/8) h_0) in the
           pi-convention Hermite basis: unit norm, phi_inf(0) = 0, self-dual,
           and hence E phi_inf(u) = E phi_inf(1/u) -- measured.

CHECK 2 -- ||E phi_inf||^2 and its localisations.  The limit constant, by
           u-space quadrature.  Two localisations are reported because §3 of
           the note only ever needs one: the integral over a FIXED compact
           [A,B] is already a lower bound for ||g||^2 once lambda >= B.

CHECK 3 -- ||g||^2 at finite mu, direct.  The quantity H0 is about, computed
           from the actual prolate vector at each mu.  Compared with CHECK 2's
           limit constant.  ||r||^2 is reported alongside; it is the quantity
           the "||g||^2 = ||E phi||^2 - ||r||^2" route has to subtract, and the
           point is that no route below subtracts it.

CHECK 4 -- the convergence that is the whole content: 1 - <phi_lambda, phi_inf>
           against 1/c and 1/c^2.  This is the input the note isolates, and the
           rate is what decides whether H0 is O(1) or merely non-degenerate.

CHECK 5 -- the mean-value route, for comparison only: ||E phi_inf||^2 recomputed
           as (1/2pi) int |zeta(1/2 - is)|^2 |M(s)|^2 ds with M the Mellin
           transform of phi_inf in closed form.  Two independent computations of
           one number.  This is the only place zeta is evaluated.

CHECK 6 -- the tightness lemma: c^2 int y^2 Phi^2 <= chi, straight from the
           prolate equation, which is what rules out mass escaping to infinity
           in the limit.  Measured per mode against chi_n and against (2n+1)c.

CHECK 7 -- the imported theorem itself: the rescaled prolate mode against the
           Hermite function, per mode, on a grid.  This is Dunster 2017 eq.
           (124) at m = 0 and fixed n, in the one form the note uses it; the
           DLMF identity U(-n-1/2, z) = e^{-z^2/4} He_n(z) that turns his
           parabolic cylinder function into a Hermite function is checked first.

CHECK 8 -- the one upstream link that mg-731c left sketched: an upper bound for
           Phi(1)^2 in terms of (1 - Lambda_n), proved in §A of the note from
           dilate-sum.md Prop. 4.1(ii).  Without it the -4 pi rate rests on an
           OBSERVED conversion.  Measured against the truth.

Arbitrary precision throughout (mpmath).  The quadratures run at 40 digits --
the quantities here are O(1), not 10^-55 -- but the three-mode vector must be
BUILT at more than 2c/log 10 digits, because its index-8 weight is a ratio of
concentration defects and those are 10^-88 at mu = 20; see `build`.  Stability
is reported at 30 vs 40 working digits from vectors built 40 digits apart.
Run with QUICK=1 for one bandwidth per check.
"""

import os
import sys

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import verify_q2 as VQ             # noqa: E402
import verify_q3 as VT             # noqa: E402

QUICK = os.environ.get("QUICK", "") not in ("", "0")

MUS = [5] if QUICK else [3, 5, 8, 12, 20]

WORK = 40          # working precision for the quadratures; the answers are O(1)


def build(muv, extra=0):
    """The three-mode vector at mu, built at whatever precision its defects need.

    `Comb` divides by chi_0 - chi_8, and 1 - Lambda_8 ~ 4 sqrt(pi) 8^8 c^{17/2}
    e^{-2c}/8!, which is 10^-47 at mu = 12 and 10^-88 at mu = 20.  Building at
    the working precision silently returns chi_0 - chi_8 = 0 (at mu = 8, dps 25,
    it raises ZeroDivisionError, which is the good case).  So the build precision
    is set from 2c/log 10 with margin, and the precision is dropped back to WORK
    afterwards -- the quantities the quadratures then handle are all O(1).
    """
    if (muv, extra) in _BUILT:
        return _BUILT[(muv, extra)]
    c = 2 * mp.pi * mp.mpf(muv)
    need = int(2 * float(c) / float(mp.log(10))) + 60 + extra
    mp.mp.dps = max(WORK, need)
    cb = VT.Comb(c)
    cb.phi_in(mp.mpf(1) / 3)           # force the cached Legendre head
    mp.mp.dps = WORK
    _BUILT[(muv, extra)] = cb
    return cb


_BUILT = {}


# --- the window integrand, from on-band values only ---------------------------


def S_of(cb, t):
    """S(t) = sum_{1 <= n <= t} Phi(n/t).  Every argument is on band."""
    s = mp.mpf(0)
    n = 1
    while n <= t:
        s += cb.phi_in(mp.mpf(n) / t)
        n += 1
    return s


def window_norm2(cb, lo, hi):
    """int_lo^hi S(t)^2 dt/t^2, split at the integers where S jumps."""
    cuts = [mp.mpf(lo)]
    n = int(mp.floor(lo)) + 1
    while n < hi:
        cuts.append(mp.mpf(n))
        n += 1
    cuts.append(mp.mpf(hi))
    tot = mp.mpf(0)
    for a, b in zip(cuts[:-1], cuts[1:]):
        if b <= a:
            continue
        mid = (a + b) / 2
        k = int(mp.floor(mid))          # term count is constant on (a,b)

        def f(t, k=k):
            s = sum(cb.phi_in(mp.mpf(j) / t) for j in range(1, k + 1))
            return s * s / (t * t)

        tot += mp.quad(f, [a, b])
    return tot


# --- the limit vector ----------------------------------------------------------


def herm(n, x):
    """pi-convention Hermite function: h_n(x) = (2^n n!)^-1/2 2^1/4 H_n(sqrt(2pi) x) e^{-pi x^2}.

    Normalised to int_R h_n^2 = 1 and Fourier self-dual for n = 0 mod 4 with the
    convention hat f(xi) = int f(x) e^{2 pi i x xi} dx.
    """
    y = mp.sqrt(2 * mp.pi) * x
    return (mp.hermite(n, y) * mp.exp(-mp.pi * x * x)
            * mp.mpf(2) ** mp.mpf("0.25") / mp.sqrt(mp.mpf(2) ** n * mp.factorial(n)))


def phi_inf(x):
    """The Hermite-limit near-radical vector, normalised: sqrt(8/11) (h_4 - sqrt(3/8) h_0).

    This is `start.tex:39`'s h_4 - sqrt(3/8) h_0 with unit norm; the coefficient
    ratio is forced by h_4(0) = sqrt(3/8) h_0(0), i.e. by phi(0) = 0, and
    hat phi(0) = phi(0) holds automatically since both modes are self-dual.
    """
    return mp.sqrt(mp.mpf(8) / 11) * (herm(4, x)
                                      - mp.sqrt(mp.mpf(3) / 8) * herm(0, x))


def E_inf(u, nmax=None):
    """E phi_inf(u) = u^{1/2} sum_{n>=1} phi_inf(n u), summed to negligibility."""
    if nmax is None:
        nmax = max(4, int(mp.ceil(mp.mpf(12) / u)))
    return mp.sqrt(u) * mp.fsum(phi_inf(mp.mpf(n) * u) for n in range(1, nmax + 1))


def E_inf_norm2(lo, hi):
    """int_lo^hi |E phi_inf|^2 d*u, smooth integrand -- no splitting needed."""
    return mp.quad(lambda u: E_inf(u) ** 2 / u, [lo, hi])


# --- Mellin transform of the limit vector, closed form ------------------------


def mellin_phi_inf(s):
    """M(s) = int_0^infty phi_inf(u) u^{1/2 - is} d*u, in closed form.

    int_0^infty x^{z-1} H_n(sqrt(2pi) x) e^{-pi x^2} dx
        = sum_k H_n[k] (2 pi)^{k/2} (1/2) pi^{-(z+k)/2} Gamma((z+k)/2),
    with H_n[k] the Taylor coefficients of the Hermite polynomial.
    """
    z = mp.mpf(1) / 2 - 1j * s
    out = mp.mpc(0)
    for n, a in ((4, mp.sqrt(mp.mpf(8) / 11)),
                 (0, -mp.sqrt(mp.mpf(8) / 11) * mp.sqrt(mp.mpf(3) / 8))):
        cf = mp.taylor(lambda y: mp.hermite(n, y), 0, n)
        nrm = mp.mpf(2) ** mp.mpf("0.25") / mp.sqrt(mp.mpf(2) ** n * mp.factorial(n))
        tot = mp.mpc(0)
        for k, ck in enumerate(cf):
            if ck == 0:
                continue
            tot += (ck * (2 * mp.pi) ** (mp.mpf(k) / 2) / 2
                    * mp.pi ** (-(z + k) / 2) * mp.gamma((z + k) / 2))
        out += a * nrm * tot
    return out


# --- checks -------------------------------------------------------------------


def check0():
    print("\nCHECK 0 -- apparatus: the vector is admissible, and S(t) is the spill's own sum")
    print("Phi(0) = 0 and int_{-1}^1 Phi = 0 are the two conditions that make E phi")
    print("an L^2 test function at all; both are imposed, so this is a check on the")
    print("solve, not on the theory.  The last column compares S(t)/(lambda sqrt(t'))")
    print("with verify_q3.Comb.R at the same point of (0,1/lambda), i.e. the two")
    print("parametrisations of the same function where they overlap.\n")
    print("  mu    Phi(0)        int Phi       sum b^2 - 1   S vs q3.R (rel)")
    for muv in MUS:
        cb = build(muv)
        nrm = sum(cb.b[k] ** 2 for k in (0, 4, 8)) - 1
        # overlap: q3's R(t') is at u = 1/(lambda t'), i.e. our t = mu t'
        tp = mp.mpf(2)
        lam = mp.sqrt(mp.mpf(muv))
        mine = S_of(cb, muv * tp) / (lam * mp.sqrt(tp))
        theirs = cb.R(tp)
        rel = abs(mine - theirs) / abs(theirs)
        print("  %-5s %-13s %-13s %-13s %s"
              % (muv, mp.nstr(cb.p0, 3), mp.nstr(cb.integral(), 3),
                 mp.nstr(nrm, 3), mp.nstr(rel, 3)))


def check1():
    print("\nCHECK 1 -- the limit vector phi_inf = sqrt(8/11)(h_4 - sqrt(3/8) h_0)")
    print("Unit norm, phi_inf(0) = 0, and -- the consequence that matters --")
    print("E phi_inf(u) = E phi_inf(1/u), which holds iff hat phi = phi and both")
    print("phi(0) and hat phi(0) vanish.  That symmetry is not imposed anywhere in")
    print("`E_inf`; it is a test of the whole construction.\n")
    n2 = 2 * mp.quad(lambda x: phi_inf(x) ** 2, [0, 1, 4])
    print("  ||phi_inf||^2 - 1        = %s" % mp.nstr(n2 - 1, 5))
    print("  phi_inf(0)               = %s" % mp.nstr(phi_inf(mp.mpf(0)), 5))
    print("  int_R phi_inf            = %s   (quadrature-limited, not exact zero)"
          % mp.nstr(2 * mp.quad(phi_inf, [0, mp.mpf(1) / 2, 1, 2, 6]), 5))
    print("\n  u        E phi_inf(u)     E phi_inf(1/u)   rel. difference")
    for uv in ("0.7", "1", "1.3", "2.5"):
        u = mp.mpf(uv)
        a, b = E_inf(u), E_inf(1 / u)
        rel = abs(a - b) / max(abs(a), mp.mpf(10) ** -40)
        print("  %-8s %-16s %-16s %s"
              % (uv, mp.nstr(a, 8), mp.nstr(b, 8), mp.nstr(rel, 3)))


def check2():
    print("\nCHECK 2 -- the limit constant ||E phi_inf||^2, and two localisations")
    print("The full norm is the mu -> infinity value of ||g||^2 (CHECK 3).  The")
    print("localisations are what §3 of the note actually uses: for any fixed")
    print("[A,B] and any lambda >= B, ||g||^2 >= int_A^B |E phi_lambda|^2 d*u, so a")
    print("lower bound on the limit over ONE fixed compact suffices.\n")
    full = 2 * E_inf_norm2(1, 60)          # symmetric under u -> 1/u
    loc1 = E_inf_norm2(1, 2)
    loc2 = E_inf_norm2(mp.mpf(1) / 2, 2)
    print("  ||E phi_inf||^2               = %s" % mp.nstr(full, 12))
    print("  int_1^2   |E phi_inf|^2 d*u   = %s" % mp.nstr(loc1, 12))
    print("  int_1/2^2 |E phi_inf|^2 d*u   = %s" % mp.nstr(loc2, 12))
    tail = 2 * E_inf_norm2(60, 200)
    print("  tail |u| > 60 (both sides)    = %s   (truncation of the first line)"
          % mp.nstr(tail, 3))
    return full


def check3(limit):
    print("\nCHECK 3 -- ||g||^2 at finite mu, computed from the actual prolate vector")
    print("||g||^2 = int_1^mu S(t)^2 dt/t^2 and ||r||^2 = int_mu^T S(t)^2 dt/t^2.")
    print("No zeta, no mean value, no Mellin transform: on-band Legendre values of")
    print("Phi at rational points n/t, and one quadrature.  The `stab` column is the")
    print("same number at working precision 30 instead of 40, from a vector built")
    print("with 40 digits more margin.\n")
    print("The `loc` column is the SAME integrand over the fixed window u in [1/2,2],")
    print("i.e. t in [lambda/2, 2 lambda], which is inside [1/lambda, lambda] only")
    print("once lambda >= 2 (mu >= 4); that is the quantity §3 of the note bounds")
    print("below, and it is a lower bound for ||g||^2 by inspection.\n")
    print("  mu    ||g||^2         ||g||^2/limit   loc [1/2,2]    ||r||^2        stab (rel)")
    out = []
    for muv in MUS:
        cb = build(muv)
        lam = mp.sqrt(mp.mpf(muv))
        g2 = window_norm2(cb, 1, muv)
        r2 = window_norm2(cb, muv, 4 * muv)
        loc = window_norm2(cb, lam / 2, 2 * lam) if lam >= 2 else None
        cb2 = build(muv, extra=40)
        mp.mp.dps = 30
        g2b = window_norm2(cb2, 1, muv)
        mp.mp.dps = WORK
        rel = abs(g2 - g2b) / g2
        out.append((muv, g2, r2, loc))
        print("  %-5s %-15s %-15s %-14s %-14s %s"
              % (muv, mp.nstr(g2, 10), mp.nstr(g2 / limit, 8),
                 "n/a (lam<2)" if loc is None else mp.nstr(loc, 8),
                 mp.nstr(r2, 4), mp.nstr(rel, 3)))
    return out


def check4():
    print("\nCHECK 4 -- the one input the reduction needs: phi_lambda -> phi_inf")
    print("d(lambda) = 1 - <phi_lambda, phi_inf> with both of unit norm, so")
    print("||phi_lambda - phi_inf||^2 = 2 d.  Reported against 1/c and 1/c^2 to see")
    print("which it is; the note's §5 claims only that d -> 0 is enough, but the")
    print("RATE is what decides whether ||g||^2 -> limit at a usable speed.\n")
    print("  mu    c          d = 1 - <.,.>   d * c        d * c^2")
    for muv in MUS:
        c = 2 * mp.pi * mp.mpf(muv)
        cb = build(muv)
        lam = mp.sqrt(mp.mpf(muv))

        def f(x):
            return cb.phi_in(x / lam) / mp.sqrt(lam) * phi_inf(x)

        ip = 2 * mp.quad(f, [0, 1, 2, lam])
        d = 1 - abs(ip)
        print("  %-5s %-10s %-15s %-12s %s"
              % (muv, mp.nstr(c, 6), mp.nstr(d, 6),
                 mp.nstr(d * c, 6), mp.nstr(d * c * c, 6)))


def check5(limit):
    print("\nCHECK 5 -- the mean-value route, for comparison only")
    print("||E phi_inf||^2 = (1/2pi) int |zeta(1/2 - is)|^2 |M(s)|^2 ds, M the Mellin")
    print("transform of phi_inf.  This is the ONLY evaluation of zeta in this script,")
    print("and it recomputes a number CHECK 2 already has without it.  Agreement is")
    print("a check on both; the point of the note is that the left-hand route is")
    print("available and the right-hand one is not needed.\n")
    f = lambda s: abs(mp.zeta(mp.mpf(1) / 2 - 1j * s)) ** 2 * abs(mellin_phi_inf(s)) ** 2
    val = mp.quad(f, [-40, -8, 0, 8, 40]) / (2 * mp.pi)
    print("  Mellin route     = %s" % mp.nstr(val, 10))
    print("  u-space (CHECK 2)= %s" % mp.nstr(limit, 10))
    print("  relative diff    = %s" % mp.nstr(abs(val - limit) / limit, 4))
    print("\n  |s|   |M(s)|          |zeta(1/2-is)|   -- the weight is the decaying factor")
    for sv in (0, 5, 10, 20, 40):
        s = mp.mpf(sv)
        print("  %-5s %-15s %s"
              % (sv, mp.nstr(abs(mellin_phi_inf(s)), 6),
                 mp.nstr(abs(mp.zeta(mp.mpf(1) / 2 - 1j * s)), 6)))


def check6():
    print("\nCHECK 6 -- the tightness lemma the reduction uses, and it is elementary")
    print("Multiplying the prolate equation by Phi and integrating over [-1,1] kills")
    print("the boundary term, so with int Phi^2 = 1")
    print("    c^2 int y^2 Phi^2 = chi - int (1-y^2) Phi'^2  <=  chi,")
    print("hence int x^2 |phi_lambda|^2 <= lambda^2 chi / c^2 = chi/(4 pi^2 lambda^2),")
    print("which is O(1) because chi_n = (2n+1) c + O(1) (Dunster 2017 eq. (107)).")
    print("That is what stops mass escaping to |x| = infinity in the limit; nothing")
    print("asymptotic is used for the inequality itself.\n")
    print("  mu    n   c^2 int y^2 Phi^2   chi_n         ratio      chi_n/((2n+1)c)")
    for muv in MUS:
        c = 2 * mp.pi * mp.mpf(muv)
        cb = build(muv)
        for n in (0, 4, 8):
            md = cb.md[n]
            m2 = 2 * mp.quad(lambda y: y * y * md.phi_in(y) ** 2, [0, 1])
            lhs = c * c * m2
            print("  %-5s %-3s %-19s %-13s %-10s %s"
                  % (muv, n, mp.nstr(lhs, 8), mp.nstr(md.chi, 8),
                     mp.nstr(lhs / md.chi, 6),
                     mp.nstr(md.chi / ((2 * n + 1) * c), 6)))
    m2inf = 2 * mp.quad(lambda x: x * x * phi_inf(x) ** 2, [0, 1, 2, 6])
    print("\n  int x^2 phi_inf^2 = %s   (the limit of int x^2 |phi_lambda|^2)"
          % mp.nstr(m2inf, 8))
    print("  mu    lambda^2 int y^2 Phi_comb^2   ratio to the limit")
    for muv in MUS:
        cb = build(muv)
        m2 = 2 * mp.quad(lambda y: y * y * cb.phi_in(y) ** 2, [0, 1])
        v = mp.mpf(muv) * m2
        print("  %-5s %-29s %s" % (muv, mp.nstr(v, 8), mp.nstr(v / m2inf, 6)))


def check7():
    print("\nCHECK 7 -- the imported theorem, per mode: Dunster 2017 eq. (124)")
    print("At m = 0 and fixed n, (124) reads Phi_n(x)/Phi_n(0) = [U(-a/2, rho-hat")
    print("sqrt(2 gamma)) + O(gamma^-1 log gamma) env U] / U(-a/2, 0) times an")
    print("elementary prefactor, with a = chi_n/c = 2n+1 + O(1/c) by (107).  Since")
    print("U(-n-1/2, z) = e^{-z^2/4} He_n(z) (DLMF 12.7.2) and z = rho sqrt(2c) is")
    print("2 sqrt(pi) X at x = X/lambda, that IS the pi-convention Hermite function.")
    print("Measured: e(mu) = sup_{|X|<=4} |lambda^-1/2 Phi_n(X/lambda) - s h_n(X)|")
    print("with the sign s chosen to match, on a grid of 201 points.\n")
    print("  first, the DLMF identity itself, at n = 4:")
    for zv in ("0.5", "2", "5"):
        z = mp.mpf(zv)
        lhs = mp.pcfu(-mp.mpf(9) / 2, z)
        rhs = mp.exp(-z * z / 4) * mp.hermite(4, z / mp.sqrt(2)) / 2 ** 2
        print("    z = %-5s U(-9/2,z) = %-18s e^{-z^2/4} He_4(z) = %-18s rel %s"
              % (zv, mp.nstr(lhs, 10), mp.nstr(rhs, 10),
                 mp.nstr(abs(lhs - rhs) / abs(rhs), 3)))
    print("\n  mu    c          n=0 sup err   n=4 sup err   n=8 sup err   (n=4) * c")
    for muv in MUS:
        c = 2 * mp.pi * mp.mpf(muv)
        cb = build(muv)
        lam = mp.sqrt(mp.mpf(muv))
        errs = []
        for n in (0, 4, 8):
            md = cb.md[n]
            s = mp.sign(md.p0 * herm(n, mp.mpf(0)))
            best = mp.mpf(0)
            for j in range(201):
                X = mp.mpf(4) * j / 200
                if X / lam > 1:
                    break
                v = md.phi_in(X / lam) / mp.sqrt(lam)
                best = max(best, abs(v - s * herm(n, X)))
            errs.append(best)
        print("  %-5s %-10s %-13s %-13s %-13s %s"
              % (muv, mp.nstr(c, 6), mp.nstr(errs[0], 4), mp.nstr(errs[1], 4),
                 mp.nstr(errs[2], 4), mp.nstr(errs[1] * c, 5)))


def check8():
    print("\nCHECK 8 -- the upstream link mg-731c recorded as sketched: Phi(1)^2 from above")
    print("q3-log-weight-and-edge.md Thm 4.4 bounds the zero sum by Phi(1)^2, and its")
    print("§4 table converts Phi(1)^2 -> (1 - chi_2) citing h1-mean-value.md §7, which")
    print("is OBSERVED.  §A of the note proves the upper half:")
    print("    Phi_n(1)^2 <= (2 pi c X_0 / kappa) (1 - Lambda_n),   X_0 = B_2 c |mu_Phi|,")
    print("with B_2 = K_1 (6c + 2^-1/2) the constant of dilate-sum.md Prop. 4.1(ii) and")
    print("kappa = (1/2pi) int (|sin| - 1/2)_+^2 = pi^-1 (pi/2 + sqrt3/4 - sqrt3).")
    print("Printed: the truth (which h1 §7 puts at ~1), the proved bound, and the ratio.\n")
    kap = (mp.pi / 2 + mp.sqrt(3) / 4 - mp.sqrt(3)) / mp.pi
    print("  kappa = %s\n" % mp.nstr(kap, 8))
    print("  mu    n   Phi(1)^2/(c(1-Lam))  proved bound/(c(1-Lam))   truth/bound")
    for muv in MUS:
        c = 2 * mp.pi * mp.mpf(muv)
        cb = build(muv)
        K1 = VQ.K1_of_c(c)
        for n in (0, 4, 8):
            md = cb.md[n]
            defect = 1 - md.lam
            truth = md.p1 ** 2 / (c * defect)
            X0 = K1 * (6 * c + 1 / mp.sqrt(2)) * c * abs(md.mu)
            bound = 2 * mp.pi * c * X0 / kap / c          # per unit of (1 - Lam), over c
            print("  %-5s %-3s %-20s %-25s %s"
                  % (muv, n, mp.nstr(truth, 8), mp.nstr(bound, 8),
                     mp.nstr(truth / bound, 4)))


def main():
    mp.mp.dps = 40
    print(__doc__.split("\n")[0])
    print("mpmath dps = %d;  QUICK = %s" % (mp.mp.dps, QUICK))
    check0()
    check1()
    limit = check2()
    check3(limit)
    check4()
    check5(limit)
    check6()
    check7()
    check8()
    print("\nDone.")


if __name__ == "__main__":
    main()
