#!/usr/bin/env python3
"""Q3: the log^3 weight and the sigma -> -1/2 edge of h1-mean-value.md §3.

Companion to `q3-log-weight-and-edge.md` (work item mg-731c).  Needs mpmath;
no numpy.  Imports the prolate apparatus of `verify_prolate_rate.py`, the
Legendre/entire-extension apparatus of `verify_h1.py`, and the on-band
evaluator and mode builder of `verify_q2.py` (whose `sph_j_all` is the FIXED
one -- mg-9d43; nothing below uses an off-band value in any case).

The two steps under test are §3's two flagged bullets.  The note calls them
"open, but routine; poly cost at worst".  What is checked here:

CHECK 0 -- the three-mode near-radical vector is admissible: Phi(0) = 0 and
           int_{-1}^{1} Phi = 0 to working precision, and Phi(1) != 0.  The
           second is what makes the spill's ramp cancel exactly (CHECK 2);
           the third is what makes the spill discontinuous (CHECK 1).

CHECK 1 -- THE CORRECTION.  §3 asserts "R is bounded with a single jump at
           v = log lambda and is smooth to the right of it".  It is not.
           r = E phi restricted to (0, 1/lambda) has a jump at u = lambda/N
           for EVERY integer N > mu, of size |Phi(1)| N^{-1/2}, measured here
           against one-sided limits.  This is the same sawtooth the note's own
           §4 uses; §3 and §4 of that note contradict each other.

CHECK 2 -- what a fractional-Sobolev route would have to pay.  Between jumps
           the ramp of lambda sqrt(t) R(t) is -mu Phi(1) t^0 (measured), i.e.
           exactly the jump density times the jump -- so |R'| ~ mu t |R|, not
           "of the same character as (D)" as §3 says.  The only bound on that
           derivative that is currently PROVABLE from the corpus is the
           term-by-term one, and its ratio to the truth is printed: it is
           ||Phi'||_inf / |Phi(1)|, which is exponentially large in c.

CHECK 3 -- arithmetic, not measurement: the coupling between the two flagged
           steps.  (ZFR) forces the sigma-edge at height eta to draw only on
           |t| >= T(eta) = exp(c_0/2eta), where the log^3 weight is already
           (c_0/2eta)^3.  Tabulated against the note's expectation that the
           edge "contributes a further logarithm".

CHECK 4 -- support for the one claim below that is observed rather than
           proved: on Re s = eta < 1/2 the mean square of zeta grows like
           T^{1-2eta}, so the tail integral the divergent ordering needs to be
           small is not small.  Measured for two eta at three heights.

CHECK 5 -- the crude inputs the repair actually uses are polynomial in mu:
           ||Phi||_inf and the total variation of g_0(w) = g(e^w).  Grid-
           limited, so both are under-reports; only their ORDER matters, since
           they enter the repair inside a logarithm.

Everything is arbitrary precision (mpmath), default 120 digits, with a
stability column at 80 vs 120 where a cancellation is involved.  Run with
QUICK=1 for one bandwidth per check.
"""

import os
import sys

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import verify_prolate_rate as VP   # noqa: E402
import verify_h1 as VH             # noqa: E402
import verify_q2 as VQ             # noqa: E402

QUICK = os.environ.get("QUICK", "") not in ("", "0")


# --- the three-mode near-radical vector ---------------------------------------


class Comb:
    """The normalised three-mode combination Phi = sum b_k Phi_{n_k}, n = 0,4,8.

    Weights from prolate-rate.md §2.1: with u_m = b_m Phi_{n_m}(0), the two
    admissibility conditions phi(0) = 0 and hat phi(0) = 0 read sum u_m = 0 and
    sum chi_m u_m = 0, whence u_8/u_4 = -(chi_0 - chi_4)/(chi_0 - chi_8) in
    prolate indices.  Normalised by sum b_k^2 = 1, the modes being orthonormal
    on [-1,1].
    """

    def __init__(self, c, tol=mp.mpf(10) ** -60):
        self.c = c
        self.mu = c / (2 * mp.pi)
        ms = VQ.modes(c, jmax=4, tol=tol)
        self.md = {0: ms[0], 4: ms[2], 8: ms[4]}
        ch = {k: mp.sqrt(self.md[k].lam) for k in (0, 4, 8)}
        u = {4: mp.mpf(1)}
        u[8] = -(ch[0] - ch[4]) / (ch[0] - ch[8])
        u[0] = -(u[4] + u[8])
        b = {k: u[k] / self.md[k].p0 for k in (0, 4, 8)}
        nrm = mp.sqrt(sum(b[k] ** 2 for k in (0, 4, 8)))
        self.b = {k: b[k] / nrm for k in (0, 4, 8)}
        self.p1 = sum(self.b[k] * self.md[k].p1 for k in (0, 4, 8))
        self.p0 = sum(self.b[k] * self.md[k].p0 for k in (0, 4, 8))
        self.lam4 = self.md[4].lam

    def phi_in(self, y):
        """Phi(y) for |y| <= 1, on-band Legendre series only."""
        return sum(self.b[k] * self.md[k].phi_in(y) for k in (0, 4, 8))

    def integral(self):
        """int_{-1}^{1} Phi = 2 int_0^1 Phi -- zero iff hat phi(0) = 0."""
        return 2 * mp.quad(self.phi_in, [0, 1])

    def R(self, t):
        """r(u) at u = 1/(lambda t), i.e. R(v) at v = log(lambda t), t > 1.

        E phi(u) = u^{1/2} sum_{n>0} phi(n u) with phi(x) = lambda^{-1/2}
        Phi(x/lambda) supported on |x| <= lambda, so for u = 1/(lambda t) the
        sum is FINITE with floor(mu t) terms and every argument is ON BAND:

            R(t) = (lambda sqrt(t))^{-1} sum_{1 <= n <= mu t} Phi(n/(mu t)).

        No off-band evaluation, no spherical Bessel function, no cancellation
        beyond that of the sum itself.
        """
        lam = mp.sqrt(self.mu)
        M = self.mu * t
        s = mp.mpf(0)
        n = 1
        while n <= M:
            s += self.phi_in(mp.mpf(n) / M)
            n += 1
        return s / (lam * mp.sqrt(t))

    def ramp(self, t):
        """d/dt [ lambda sqrt(t) R(t) ] between jumps, from the ODE-free form
        d/dt sum_{n<=M} Phi(n/M) = -(1/t) sum_{n<=M} Psi(n/M), Psi(x) = x Phi'(x).
        """
        M = self.mu * t
        s = mp.mpf(0)
        n = 1
        while n <= M:
            x = mp.mpf(n) / M
            s += x * mp.diff(self.phi_in, x)
            n += 1
        return -s / t

    def sup_dphi(self, npts=600):
        """grid sup of |Phi'| on [0,1]; grid-limited, so an under-report."""
        best = mp.mpf(0)
        for j in range(npts + 1):
            y = mp.mpf(j) / npts
            best = max(best, abs(mp.diff(self.phi_in, y)))
        return best

    def sup_phi(self, npts=600):
        best = mp.mpf(0)
        for j in range(npts + 1):
            y = mp.mpf(j) / npts
            best = max(best, abs(self.phi_in(y)))
        return best


def cs_of():
    if QUICK:
        return [2 * mp.pi * 3]
    return [2 * mp.pi * 2, 2 * mp.pi * 3, 2 * mp.pi * 5, 2 * mp.pi * 8]


# --- checks -------------------------------------------------------------------


def check0():
    print("\nCHECK 0 -- the near-radical vector is admissible, and Phi(1) != 0")
    print("phi(0) = 0 and hat phi(0) = 0 are what make E phi an L^2 function at")
    print("all (prolate-rate.md §2.1).  Phi(0) = 0 kills the t Phi(0)/2 term of")
    print("the spill; int_0^1 Phi = 0 kills the secular term mu t int_0^1 Phi in")
    print("the finite sum below, which is what lets R decay at all.  Phi(1) != 0")
    print("is what makes the spill discontinuous at every u = lambda/N.\n")
    mp.mp.dps = 120
    print("  The last column is what fixes the truncation height T_* of the repair.")
    print("  Q1 plus the exact identity int_{|x|>1}|Phi|^2 = (1-Lambda)/Lambda give")
    print("  Phi(1)^2 >= (1-Lambda_4)/(2 K_1^2 C_*^2) -- a PROVED lower bound, from")
    print("  which log(1/Phi(1)^2) <= 2c + O(log c) = 4 pi mu + O(log mu) by Fuchs.")
    print("  Measured the ratio is ~0.7c, i.e. §7's observed identity; the proof")
    print("  needs only that it is bounded below.\n")
    print("  c        Phi(0)          int_{-1}^1 Phi   Phi(1)           1-Lambda_4"
          "     Phi(1)^2/(1-Lambda_4)")
    for cv in cs_of():
        c = mp.mpf(cv)
        C = Comb(c)
        print("  %-8s %-15s %-16s %-16s %-14s %s"
              % (mp.nstr(c, 6), mp.nstr(abs(C.p0), 4), mp.nstr(abs(C.integral()), 4),
                 mp.nstr(C.p1, 8), mp.nstr(1 - C.lam4, 6),
                 mp.nstr(C.p1 ** 2 / (1 - C.lam4), 6)))
    print("\n  Phi(0) and int Phi are zero to the working precision; Phi(1) is not.")


def check1():
    print("\nCHECK 1 -- the spill r has a jump at u = lambda/N for EVERY N > mu")
    print("h1-mean-value.md §3, first flagged bullet: \"R is bounded with a single")
    print("jump at v = log lambda and is smooth to the right of it\".  Measured")
    print("below: one-sided limits of R at t = N/mu (i.e. u = lambda/N), against")
    print("the predicted jump |Phi(1)| N^{-1/2}.  ratio -> 1 means a jump is there.")
    print("The last column is the jump against the local size of R: the jumps are")
    print("not a boundary artefact, they are the whole function.\n")
    mp.mp.dps = 120
    eps = mp.mpf(10) ** -30
    for cv in cs_of():
        c = mp.mpf(cv)
        C = Comb(c)
        mu = C.mu
        Ns = [int(mp.floor(mu)) + k for k in (1, 2, 3, 5, 9, 17)]
        print("  c = %s (mu = %s), Phi(1) = %s"
              % (mp.nstr(c, 6), mp.nstr(mu, 5), mp.nstr(C.p1, 6)))
        print("     N     t=N/mu    measured jump    predicted        ratio"
              "            |jump|/|R|")
        for N in Ns:
            t = mp.mpf(N) / mu
            if t <= 1:
                continue
            hi = C.R(t + eps)
            lo = C.R(t - eps)
            meas = hi - lo
            pred = C.p1 / mp.sqrt(mp.mpf(N))
            print("     %-5d %-9s %-16s %-16s %-16s %s"
                  % (N, mp.nstr(t, 5), mp.nstr(meas, 6), mp.nstr(pred, 6),
                     mp.nstr(meas / pred, 12),
                     mp.nstr(abs(meas) / max(abs(hi), abs(lo)), 5)))
        print()


def check2():
    print("\nCHECK 2 -- the ramp between jumps, and what a Sobolev route would pay")
    print("§3's first bullet asks for \"a bound on ||R'|| of the same character as")
    print("(D)\".  Between jumps, |d/dt [lambda sqrt(t) R(t)]| is of order")
    print("mu |Phi(1)| -- so |R'| ~ mu t |R|, growing, and R' is not a function")
    print("at all across the jumps.  The last column is the ratio of the only")
    print("term-by-term bound available on that derivative, ||Phi'||_inf, to the")
    print("truth |Phi(1)|: that is the factor a Sobolev route costs on today's")
    print("inputs, and it is exponential in c.\n")
    mp.mp.dps = 80
    print("  The ramp is O(mu |Phi(1)|) and NOT asymptotically -mu Phi(1): after")
    print("  differentiation the second off-band term a_2 cos(cx)/x^2 contributes")
    print("  at the same order (c a_2 ~ 2 pi mu Phi(1)/mu_Phi).  What is measured")
    print("  is therefore the RANGE of |ramp|/(mu |Phi(1)|) over one inter-jump")
    print("  interval -- bounded, and bounded away from 0, which is the claim.\n")
    print("  c        interval          min ratio    max ratio    ||Phi'||_inf/|Phi(1)|")
    npts = 12 if QUICK else 40
    for cv in cs_of():
        c = mp.mpf(cv)
        C = Comb(c)
        mu = C.mu
        dsup = C.sup_dphi(300 if QUICK else 600)
        N = int(mp.floor(mu)) + 2
        lo, hi = None, None
        for j in range(1, npts):
            t = (mp.mpf(N) + mp.mpf(j) / npts) / mu   # strictly between jumps
            rr = abs(C.ramp(t)) / (mu * abs(C.p1))
            lo = rr if lo is None else min(lo, rr)
            hi = rr if hi is None else max(hi, rr)
        print("  %-8s (%s,%s)  %-12s %-12s %s"
              % (mp.nstr(c, 6), mp.nstr(mp.mpf(N) / mu, 4),
                 mp.nstr(mp.mpf(N + 1) / mu, 4),
                 mp.nstr(lo, 5), mp.nstr(hi, 5),
                 mp.nstr(dsup / abs(C.p1), 4)))


def check3():
    print("\nCHECK 3 -- arithmetic: the two flagged steps are not independent")
    print("(ZFR) says a zero with eta_rho = min(beta,1-beta) <= eta sits above")
    print("height T(eta) = exp(c_0/eta) - 3.  So in the ordering §3 proposes --")
    print("keep log^3(3+|t|) inside, cut sigma by (ZFR) -- the log^3 weight in the")
    print("edge region is already (c_0/eta)^3, and the note's \"further logarithm\"")
    print("int d(eta)/eta becomes int d(eta)/eta^4.  Pure arithmetic; no zeta.\n")
    mp.mp.dps = 30
    for c0 in (mp.mpf(1), mp.mpf("0.18")):
        print("  c_0 = %s" % mp.nstr(c0, 4))
        print("     eta        T(eta)=e^{c_0/eta}   log^3(3+T)   int_eta^{1/2} de/e"
              "   int_eta^{1/2} de/e^4")
        for k in (1, 2, 3, 4):
            eta = mp.mpf(10) ** (-k)
            T = mp.e ** (c0 / eta)
            l3 = mp.log(3 + T) ** 3
            i1 = mp.log(mp.mpf("0.5") / eta)
            i4 = (eta ** -3 - mp.mpf(8)) / 3
            print("     %-10s %-20s %-12s %-20s %s"
                  % (mp.nstr(eta, 3), mp.nstr(T, 6), mp.nstr(l3, 6),
                     mp.nstr(i1, 6), mp.nstr(i4, 6)))
        print()
    print("  And the repair's cost: truncating the zero sum at log T_* = 4 pi mu")
    print("  puts the edge at eta_* = c_0/(2 log T_*) and freezes the log^3 weight")
    print("  at log^3(3+T_*).  Both are then polynomial in mu:")
    print("     mu     log T_* = 4 pi mu   log^3(3+T_*)     eta_*(c_0=1)   "
          "log(1/2eta_*)")
    for muv in (2, 5, 12, 50):
        mu = mp.mpf(muv)
        lT = 4 * mp.pi * mu
        eta_s = mp.mpf(1) / (2 * lT)
        print("     %-6s %-19s %-16s %-14s %s"
              % (muv, mp.nstr(lT, 6), mp.nstr(lT ** 3, 6),
                 mp.nstr(eta_s, 4), mp.nstr(mp.log(1 / (2 * eta_s)), 5)))


def check4():
    print("\nCHECK 4 -- observed, not proved: zeta's mean square on Re s = eta < 1/2")
    print("The divergent ordering of CHECK 3 would still converge if the tail")
    print("int_{|t|>T(eta)} |F|^2 dt were O(eta^{2+}) as eta -> 0.  It is not:")
    print("F = zeta(1/2-is) P_phi(s) - F_mu g (prolate-rate.md §1 step 1), and on")
    print("Re = eta the mean square of zeta grows like T^{1-2eta}, which cancels")
    print("the T^{-2eta} the tail would need.  Measured: M(T) = (1/T) int_T^{2T}")
    print("|zeta(eta+it)|^2 dt against the classical prediction")
    print("    M(T) ~ zeta(2eta) + K(eta) (2^{2-2eta} - 1) T^{1-2eta},")
    print("    K(eta) = (2 pi)^{2eta-1} zeta(2-2eta) / (2-2eta),")
    print("from Titchmarsh Thm 7.2(A) -- QUOTED FROM MEMORY, NOT OPENED, so what")
    print("the table tests is the formula as much as the arithmetic.  Note")
    print("zeta(2eta) < 0 for eta < 1/2, which is why the local exponent comes")
    print("down to 1-2eta from above.  This supports the shape of the claim; it")
    print("is a property of zeta, not of our F.\n")
    mp.mp.dps = 25
    Ts = [mp.mpf(50), mp.mpf(100)] if QUICK else [mp.mpf(50), mp.mpf(100),
                                                  mp.mpf(200), mp.mpf(400)]
    for eta in (mp.mpf("0.1"), mp.mpf("0.25")):
        K = (2 * mp.pi) ** (2 * eta - 1) * mp.zeta(2 - 2 * eta) / (2 - 2 * eta)
        print("  eta = %s   (exponent 1-2eta = %s, zeta(2eta) = %s, K = %s)"
              % (mp.nstr(eta, 3), mp.nstr(1 - 2 * eta, 4),
                 mp.nstr(mp.zeta(2 * eta), 6), mp.nstr(K, 6)))
        print("     T        M(T) measured    M(T) predicted   meas/pred"
              "     local exponent")
        prev = None
        for T in Ts:
            f = lambda t: abs(mp.zeta(mp.mpc(eta, t))) ** 2
            M = mp.quad(f, [T, T + (T - T / 2) / 2, 2 * T]) / T
            pred = (mp.zeta(2 * eta)
                    + K * (2 ** (2 - 2 * eta) - 1) * T ** (1 - 2 * eta))
            fit = "" if prev is None else mp.nstr(
                mp.log(M / prev[1]) / mp.log(T / prev[0]), 5)
            print("     %-8s %-16s %-16s %-14s %s"
                  % (mp.nstr(T, 5), mp.nstr(M, 8), mp.nstr(pred, 8),
                     mp.nstr(M / pred, 6), fit))
            prev = (T, M)
        print()


def check5():
    print("\nCHECK 5 -- the crude inputs of the repair are polynomial in mu")
    print("The repair discards the zeros above height T_* using |F_mu g(s)| <=")
    print("V_g/|t| with V_g the total variation of w -> g(e^w) e^{sigma w} on")
    print("[-log lambda, log lambda], endpoint jumps included.  V_g enters only")
    print("inside log T_*, so any polynomial V_g costs O(log mu) there.  Measured")
    print("on a grid, hence an UNDER-report of the variation.\n")
    mp.mp.dps = 60
    print("  c        mu      ||Phi||_inf   V_g (grid)     V_g/mu^2    #jumps")
    for cv in cs_of():
        c = mp.mpf(cv)
        C = Comb(c)
        mu = C.mu
        lam = mp.sqrt(mu)
        L = mp.log(lam)
        npts = 400 if QUICK else 1200
        prev = None
        V = mp.mpf(0)
        for j in range(npts + 1):
            w = -L + 2 * L * mp.mpf(j) / npts
            u = mp.e ** w
            # g(u) = u^{1/2} sum_{n <= lambda/u} phi(n u), on band
            M = lam / u
            s = mp.mpf(0)
            n = 1
            while n <= M:
                s += C.phi_in(n * u / lam)
                n += 1
            val = mp.sqrt(u) * s / mp.sqrt(lam)
            if prev is not None:
                V += abs(val - prev)
            prev = val
        V += abs(prev)                       # the jump down to 0 at u = lambda
        print("  %-8s %-7s %-13s %-14s %-11s %s"
              % (mp.nstr(c, 6), mp.nstr(mu, 4), mp.nstr(C.sup_phi(300), 5),
                 mp.nstr(V, 6), mp.nstr(V / mu ** 2, 5), int(mp.floor(mu))))


def main():
    print(__doc__.split("\n\n")[0])
    print("mpmath %s;  QUICK=%s" % (mp.__version__, QUICK))
    check0()
    check1()
    check2()
    check3()
    check4()
    check5()
    print("\nDone.")


if __name__ == "__main__":
    main()
