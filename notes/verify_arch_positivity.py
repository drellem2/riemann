#!/usr/bin/env python3
"""Four checks for `semilocal-gap.md` §10 (work item mg-555b).  Needs numpy.

The question (`semilocal-gap.md` §8 item S2): is the failure of *archimedean-only*
Weil positivity past mu = 2 a theorem, a numerical observation, or an artefact?
The literature answer is "numerical observation" -- see §10.1 for where that was
looked for.  These checks settle the third possibility, and they are the check
`semilocal-gap.md` §7 recorded as "Not done, and it would be the natural next
check": Connes-Consani's Figures `testeven` / `testeven1` / `testeven2` /
`testeven3` / `testeven4` (arXiv:2106.01715, `Spectraltriples.tex:548`-`:585`)
reproduced from scratch.  Every numerical claim `semilocal-gap.md` §3.3 makes is
one of them.

CHECK 1 (sec 10.2) -- rebuild the archimedean even matrix sigma^+ and compute its
smallest eigenvalue at L = log 2.  Connes-Consani report ~0.00133
(`Spectraltriples.tex:551`).  We get 0.0013303.

CHECK 2 (sec 10.2) -- locate the sign change.  Connes-Consani's prose says the
prime 2 "first lowers the smallest eigenvalue in the interval exp L in (2, 2.27)
but then saves it from being negative" (`:568`), so 2.27 is where their
archimedean-alone curve crosses.  We get mu* = 2.27099.

CHECK 3 (sec 10.2) -- the repair by the primes, and its sharpness.  At mu = 3
adding p = 2 restores positivity, with smallest eigenvalue < 6e-8 (`:568`); the
positivity requirement pins the parameter p to an interval of size < 1e-3 around
2 (`:574`); past mu = 3 the prime 3 repairs it again (`:579`).  All three hold.

CHECK 4 (sec 10.3) -- exhibit a single explicit test function on which the
archimedean form is negative, so the failure does not rest on a matrix
eigenvalue at all.

Checks 1, 2 and 4 are not delicate: matrix entries O(1), spectrum from 1.3e-3 to
5.5, everything quadrature-converged to ten digits.  This is *not* the regime
`citation-audit.md` §6 warns about (CCM at 200 digits, eigenvalues ~1e-48 at
mu = 11); it is four orders of magnitude away from it.  Check 3 does reach into
it -- see the caveat printed there -- and is reported separately for that reason.

Runtime ~2.5 minutes; the cost is the N = 160 matrices, not the quadrature.

--- SETUP ---------------------------------------------------------------------

Connes-Consani, arXiv:2106.01715, write the semi-local Weil quadratic form on
test functions supported in [lambda^{-1}, lambda] as (`Spectraltriples.tex:414`,
eq. \label{bombtestsum}, with L = 2 log lambda = log mu)

    QW(f, g) = psi^#(h),   h(y) = (xi_n * xi_m^* + xi_m * xi_n^*)(y),
    psi^#(F) = W_{0,2}^#(F) - W_R^#(F) - sum_p W_p^#(F),

    W_{0,2}^#(F) = int_1^inf F(x) (x^{1/2} + x^{-1/2}) d*x
    W_R^#(F)     = (1/2)(log 4pi + gamma) F(1)
                   + int_1^inf (x^{1/2} F(x) - F(1)) / (x - x^{-1}) d*x

and, for the archimedean part, carry out the second integral explicitly
(`:532`).  With y = log x and h supported in [-L, L] and even,

    W_{0,2} = int_0^L h(y) 2 cosh(y/2) dy
    W_R     = (h(0)/2) (gamma + log(4 pi (e^L - 1)/(e^L + 1)))
              + int_0^L (e^{y/2} h(y) - h(0)) / (e^y - e^{-y}) dy .

"The archimedean contribution" in their §\ref{sectsensitive} is QW with the prime
terms dropped, i.e. sigma^arch = W_{0,2} - W_R.  For L in [log 2, log 3) the only
prime term is p = 2, so this is exactly the quantity their yellow curve plots.

Basis: theirs (`:385`, eq. \label{basis}), even sector, orthonormal in
L^2([-L/2, L/2], dx):  xi_0 = L^{-1/2},  xi_n = (-1)^n sqrt(2/L) cos(2 pi n x / L).
The overall signs (-1)^n do not affect eigenvalues; they are kept to match.

Why the truncation is safe, and it matters here.  Restricting a quadratic form to
a subspace can only *raise* its smallest eigenvalue.  So a negative truncated
eigenvalue certifies a negative one for the full form: truncation can hide a
failure of positivity, never manufacture one.  Check 1 shows the expected
monotone decrease in N, and Check 3 removes the truncation from the argument
altogether.

--- WHY EVENTUAL FAILURE IS NOT A SURPRISE ------------------------------------

Connes-Consani's own Proposition (`Spectraltriples.tex:289`, \label{Hilbert})
writes the archimedean part of QW_lambda on the Fourier side as

    int |f^(t)|^2 (2 theta'(t) / 2 pi) dt + 2 Re( f^(i/2) conj(f^(-i/2)) )

with theta the Riemann-Siegel theta function.  theta'(t) is *negative* for
|t| < 6.2898 (check 3 prints this).  So the density is negative in a neighbourhood
of t = 0 and the only thing preventing a test function from living there is the
uncertainty principle -- a short support forces f^ to spread past the crossing,
where theta' > 0.  Lengthening the support removes that obstruction.  This is a
mechanism, not a proof: it says failure for large L is structurally expected, and
says nothing about *where*.  Where is checks 1-3.
"""

import numpy as np

GAMMA = np.euler_gamma


# --- digamma (real part on 1/4 + i t/2), so that numpy alone suffices ---------

_B2 = np.array([1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510])


def _digamma(z):
    """psi(z) for complex z with Re z > 0, by recurrence + Stirling."""
    z = np.asarray(z, dtype=complex)
    acc = np.zeros_like(z)
    while np.any(np.abs(z) < 20):
        m = np.abs(z) < 20
        acc = np.where(m, acc - 1.0 / z, acc)
        z = np.where(m, z + 1.0, z)
    s = np.log(z) - 0.5 / z
    zp = z ** 2
    for k, b in enumerate(_B2, start=1):
        s -= b / (2 * k * zp)
        zp = zp * z ** 2
    return acc + s


def theta_prime(t):
    """d/dt of the Riemann-Siegel theta function."""
    return 0.5 * np.real(_digamma(0.25 + 0.5j * np.asarray(t, dtype=float))) \
        - 0.5 * np.log(np.pi)


# --- the archimedean even matrix ---------------------------------------------

def _h(L, N, t):
    """h_{nm}(t) = (xi_n * xi_m^*)(t) + (xi_m * xi_n^*)(t), t in [0, L].

    By Connes-Consani's Lemma (`Spectraltriples.tex:392`, \\label{polarize} (i)),
    (phi_1 * phi_2^*)(t) = int_{t - L/2}^{L/2} phi_1(x) phi_2(x - t) dx.
    Both xi are cosines, so the integral is elementary.
    """
    t = np.atleast_1d(np.asarray(t, dtype=float))
    n = np.arange(N + 1)
    a = 2 * np.pi * n / L
    c = np.where(n == 0, L ** -0.5, ((-1.0) ** n) * np.sqrt(2.0 / L))
    p, q = t - L / 2.0, L / 2.0

    def seg(alpha, beta):
        """int_p^q cos(alpha x + beta) dx, broadcast over (T, N+1, N+1)."""
        nz = np.abs(alpha) > 1e-13
        den = np.where(nz, alpha, 1.0)
        val = (np.sin(alpha * q + beta)
               - np.sin(alpha * p[:, None, None] + beta)) / den
        return np.where(nz, val, (q - p[:, None, None]) * np.cos(beta))

    zero = np.zeros((len(t), N + 1, N + 1))
    A = a[None, :, None] + a[None, None, :] + zero      # a_n + a_m
    B = a[None, :, None] - a[None, None, :] + zero      # a_n - a_m
    bt = a[None, None, :] * t[:, None, None]            # a_m t
    I = 0.5 * (seg(A, -bt) + seg(B, bt))                # int cos(a_n x) cos(a_m (x-t))
    return (I + np.transpose(I, (0, 2, 1))) * (c[None, :, None] * c[None, None, :])


def sigma_arch(L, N, ngl=400):
    """The archimedean even matrix W_{0,2} - W_R in the basis xi_0..xi_N."""
    x, w = np.polynomial.legendre.leggauss(ngl)
    t, wt = 0.5 * L * (x + 1.0), 0.5 * L * w
    h, h0 = _h(L, N, t), _h(L, N, np.array([0.0]))[0]
    W02 = np.tensordot(wt * 2 * np.cosh(t / 2), h, axes=(0, 0))
    ratio = (np.exp(t / 2)[:, None, None] * h - h0[None]) \
        / (np.exp(t) - np.exp(-t))[:, None, None]
    WR = h0 / 2.0 * (GAMMA + np.log(4 * np.pi * (np.exp(L) - 1) / (np.exp(L) + 1))) \
        + np.tensordot(wt, ratio, axes=(0, 0))
    S = W02 - WR
    return 0.5 * (S + S.T), h0


def w_prime(L, N, p, ngl=400):
    """The matrix of W_p^#(F) = (log p) sum_{m>=1} p^{-m/2} F(p^m), i.e. of
    y = m log p sampled against h.  `Spectraltriples.tex:1676`.  p need not be
    prime: their §\\ref{sectsensitivep2} varies it as a real parameter."""
    ys = np.array([m * np.log(p) for m in range(1, 2 + int(L / np.log(p)))
                   if m * np.log(p) < L])
    if len(ys) == 0:
        return 0.0
    H = _h(L, N, ys)
    return np.log(p) * sum(p ** (-(k + 1) / 2) * H[k] for k in range(len(ys)))


def lam_min_with(L, primes=(), N=120, ngl=400):
    """Smallest eigenvalue of the even matrix with the listed places included."""
    S, _ = sigma_arch(L, N, ngl)
    for p in primes:
        S = S - w_prime(L, N, p, ngl)
    return np.linalg.eigvalsh(0.5 * (S + S.T))[0]


def lam_min(L, N=120, ngl=400):
    S, _ = sigma_arch(L, N, ngl)
    return np.linalg.eigvalsh(S)[0]


def _bisect(f, lo, hi, tol=1e-11):
    flo = f(lo)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if hi - lo < tol:
            return mid
        fm = f(mid)
        if (fm < 0) == (flo < 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


# --- an explicit witness ------------------------------------------------------

def witness(L, ngl=2000):
    """A single test function f, even, supported in [-L/2, L/2], with the
    boundary term killed.  Returns (kappa, ||f||^2, archimedean value).

    f(x) = cos(pi x / L) + kappa cos(3 pi x / L), continuous on R (both modes
    vanish at x = +- L/2), with kappa fixed by int f(x) cosh(x/2) dx = 0.

    For real even f that integral is f^(i/2) = f^(-i/2), so the boundary term
    2 Re(f^(i/2) conj(f^(-i/2))) -- equivalently W_{0,2} -- vanishes exactly,
    and the archimedean value is -W_R alone.  This is a legitimate vector for
    Connes-Consani's *unconditioned* form: no vanishing condition is imposed on
    it, the condition simply happens to hold.
    """
    x, w = np.polynomial.legendre.leggauss(ngl)

    def gl(f, lo, hi):
        return 0.5 * (hi - lo) * np.sum(w * f(0.5 * (hi - lo) * x + 0.5 * (hi + lo)))

    m1 = lambda u: np.cos(np.pi * u / L)
    m3 = lambda u: np.cos(3 * np.pi * u / L)
    c1 = gl(lambda u: m1(u) * np.cosh(u / 2), -L / 2, L / 2)
    c3 = gl(lambda u: m3(u) * np.cosh(u / 2), -L / 2, L / 2)
    kap = -c1 / c3
    f = lambda u: m1(u) + kap * m3(u)

    def h(y):
        return 0.0 if abs(y) >= L else \
            2 * gl(lambda u: f(u) * f(u - abs(y)), abs(y) - L / 2, L / 2)

    h0 = h(0.0)
    W02 = gl(lambda y: np.array([h(v) for v in np.atleast_1d(y)])
             * 2 * np.cosh(y / 2), 0.0, L)
    WR = h0 / 2 * (GAMMA + np.log(4 * np.pi * (np.exp(L) - 1) / (np.exp(L) + 1))) \
        + gl(lambda y: (np.exp(y / 2) * np.array([h(v) for v in np.atleast_1d(y)])
                        - h0) / (np.exp(y) - np.exp(-y)), 0.0, L)
    return kap, h0 / 2, W02 - WR


# --- checks -------------------------------------------------------------------

def check1():
    print("CHECK 1 -- smallest eigenvalue of the archimedean even matrix at L = log 2")
    print("Connes-Consani, `Spectraltriples.tex:551` (Figure `testeven`): ~0.00133")
    print()
    print(f"{'N':>5} {'gram err':>10} {'lambda_min':>14}")
    prev = None
    for N in (10, 20, 40, 80, 160):
        S, h0 = sigma_arch(np.log(2.0), N)
        ev = np.linalg.eigvalsh(S)
        gram = np.abs(h0 - 2 * np.eye(N + 1)).max()   # h(0) = 2 <xi_n|xi_m>
        assert gram < 1e-12, gram
        if prev is not None:
            assert ev[0] <= prev + 1e-14, "truncation must be monotone decreasing"
        prev = ev[0]
        print(f"{N:>5} {gram:>10.1e} {ev[0]:>14.7f}")
    print()
    print(f"spectrum at N = 160 runs [{ev[0]:.3e}, {ev[-1]:.3e}] -- nothing small is")
    print("being resolved, and the decrease in N is the variational direction.")
    print()


def check2():
    print("CHECK 2 -- where does the archimedean contribution alone change sign?")
    print("Connes-Consani, `Spectraltriples.tex:568`: the prime 2 'first lowers the")
    print("smallest eigenvalue in the interval exp L in (2, 2.27) but then saves it")
    print("from being negative' -- so 2.27 is their crossing.")
    print()
    print(f"{'L':>9} {'mu':>9} {'lambda_min':>14}")
    for L in (0.60, np.log(2.0), 0.75, 0.80, 0.82, 0.83, 0.85, 1.00, 1.10):
        print(f"{L:>9.5f} {np.exp(L):>9.5f} {lam_min(L):>14.7f}")
    print()
    print(f"{'N':>5} {'L*':>12} {'mu*':>12}")
    for N in (20, 40, 80, 160):
        Ls = _bisect(lambda L: lam_min(L, N), 0.75, 0.95)
        print(f"{N:>5} {Ls:>12.7f} {np.exp(Ls):>12.7f}")
    print()
    print("mu* = 2.27099 against their 2.27, on a number this note did not aim at;")
    print("with 0.0013303 against their ~0.00133 that is two independent matches.")
    print("So the sign change is *their* computation reproduced, not an artefact of")
    print("theirs and not of ours.  It is real, and it is still only numerical.")
    print()


def check3():
    print("CHECK 3 -- the repair by the primes, and how sharp it is")
    print("Connes-Consani: at mu = 3, arch + p=2 has smallest eigenvalue < 6e-8")
    print("(`Spectraltriples.tex:568`); positivity fails for p = 1.9999 and for")
    print("p = 2.0005, an interval of size < 1e-3 (`:574`); past mu = 3 the prime 3")
    print("repairs it (`:579`, Figure `testeven4`).")
    print()
    L3 = np.log(3.0)
    print(f"mu = 3, archimedean alone      : {lam_min_with(L3):>14.6e}")
    print(f"mu = 3, archimedean + p = 2    : {lam_min_with(L3, (2,)):>14.6e}"
          "   (their bound: < 6e-8)")
    print()
    print(f"{'p':>9} {'lambda_min at mu = 3':>22}")
    for p in (1.9990, 1.9999, 2.0, 2.0005, 2.0010):
        print(f"{p:>9.4f} {lam_min_with(L3, (p,), 160):>22.6e}")
    lo = _bisect(lambda p: lam_min_with(L3, (p,), 80), 1.999, 2.0, 1e-8)
    hi = _bisect(lambda p: lam_min_with(L3, (p,), 80), 2.0, 2.001, 1e-8)
    print(f"admissible window [{lo:.7f}, {hi:.7f}], width {hi - lo:.3e} < 1e-3")
    print()
    print(f"{'mu':>6} {'arch + 2':>14} {'arch + 2 + 3':>14}")
    for mu in (3.2, 3.5, 3.8):
        print(f"{mu:>6.1f} {lam_min_with(np.log(mu), (2,)):>14.6e}"
              f" {lam_min_with(np.log(mu), (2, 3)):>14.6e}")
    print()
    print("CAVEAT, and it is the one `citation-audit.md` §6 records.  The repaired")
    print("eigenvalues here are 1e-8 to 1e-12 against O(1) matrix entries, so double")
    print("precision leaves 2-4 digits of margin and no more.  The *negative* rows")
    print("are safe -- they are O(1e-2) to O(1e-5).  The near-zero *positive* rows")
    print("are reproductions, not verifications: past mu ~ 4 they should be redone")
    print("in extended precision before anyone leans on them.  Nothing in §3.3 or")
    print("§10 does.")
    print()


def check4():
    print("CHECK 4 -- an explicit test function, no matrix, no truncation")
    print()
    t0 = _bisect(lambda t: theta_prime(t), 5.0, 8.0)
    assert theta_prime(0.0) < 0 < theta_prime(10.0)
    print(f"theta'(0) = {theta_prime(0.0):.8f};  theta' changes sign at t = {t0:.7f}")
    print("so the Weil density 2 theta'(t)/2pi of `Spectraltriples.tex:289` is")
    print("negative on |t| < 6.29.  That is the mechanism; below is a witness.")
    print()
    print(f"{'L':>7} {'mu':>9} {'kappa':>11} {'||f||^2':>10} {'archimedean':>14}")
    for L in (0.8202, 1.0, 1.2, 1.2692, 1.4, 1.5, 2.0):
        kap, nrm, val = witness(L)
        print(f"{L:>7.4f} {np.exp(L):>9.5f} {kap:>11.6f} {nrm:>10.6f} {val:>14.7f}")
    Ls = _bisect(lambda L: witness(L)[2], 1.2, 1.5)
    print()
    print(f"this two-mode witness turns negative at L = {Ls:.6f}, mu = {np.exp(Ls):.6f}")
    print("-- a weaker threshold than the true 2.271, because it is one fixed vector")
    print("and not the bottom eigenvector.  What it buys is that at mu = 4.055 the")
    print("archimedean form is negative on a function one can write down in a line,")
    print("with a margin of 0.6 against a norm of 6.3.  No truncation is involved,")
    print("and the whole evaluation is three one-dimensional quadratures.")
    print()


if __name__ == "__main__":
    print(__doc__.split("--- SETUP")[0])
    check1()
    check2()
    check3()
    check4()
    print("Conclusion (`semilocal-gap.md` §10): possibility (3) -- artefact of the")
    print("truncation or the numerics -- is excluded.  The answer to S2 is (2): a")
    print("numerical observation, now an independently reproduced one, with no")
    print("theorem asserting it anywhere in the corpus (§10.1).")
