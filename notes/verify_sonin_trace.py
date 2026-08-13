#!/usr/bin/env python3
"""How big is the Sonin trace?  Five checks for `sonin-trace.md` (mg-5210).  Needs numpy.

The corpus has never evaluated the one object in Connes-Consani's archimedean
theorem that carries a sign.  That theorem (arXiv:2006.13771, Theorem 1) is

    W_inf(g * g^*)  >=  Tr( theta(g) S theta(g)^* ),      supp g in [2^-1/2, 2^1/2],
                                                          ghat(i/2) = ghat(0) = 0

with S the orthogonal projection onto the Sonin space -- the even L^2(R)
functions vanishing, together with their Fourier transform, on [-1, 1].  The
right-hand side is positive because it is ||S theta(g)^*||_HS^2.  Everything
the corpus has ever bounded is the DIFFERENCE between the two sides.

The trace is not an inaccessible object.  Connes-Consani compute it, in the
same paper, in closed form (`weil-compo.tex:1132`, Theorem \\label{devil}):

    tr(theta(f) S) = W_inf(f) + int f(rho) eps(rho) d*rho,   all f in Cc^inf(R+*)

    eps(rho) = sum_n  lam(n)^2 / (1 - lam(n)^2)  *  rho^1/2 int_{1/rho}^1
                      xi_n^an(x) xi_n^an(rho x) dx,          rho >= 1,        (*)

    eps(rho^-1) = eps(rho),

where xi_n is the L^2-normalized restriction to [-1,1] of the even prolate
spheroidal function PS_{2n,0}(2 pi, .), lam(n) its finite-Fourier eigenvalue,
and xi_n^an = F xi_n / lam(n) its analytic continuation past 1
(`weil-compo.tex:1348`-`:1373`).  So

    Sonin trace  =  W_inf   +   E,        gap := W_inf - Sonin trace  =  -E,

and Theorem 1 is exactly the statement that the quadratic form -E is positive
on the codimension-two subspace, for mu <= 2.  Both halves are computable in
prolate objects: the corpus already computes W_inf (`verify_arch_positivity.py`,
whose `_h` and W_R this script imports rather than re-deriving), and (*) is
computed here.

--- WHICH PROLATE SYSTEM, AND WHY IT IS NOT THE CORPUS'S ----------------------

(*) is a prolate expansion at bandwidth **c = 2 pi, fixed**: the Sonin cutoff of
arXiv:2006.13771 is Lambda = 1 and does not move with the test function's
support.  The corpus's prolate apparatus runs at **c = 2 pi mu**
(`verify_prolate_rate.py:8`, `prolate-rate.md:51`), mu = e^L the support
parameter.  The two systems agree only at mu = 1, which is outside every range
the corpus computes in; CHECK 5 measures the disagreement.  So "our lambda is
their Sonin cutoff Lambda" -- `signed-geometry-proposals.md:373`, and the mg-5210
work item after it -- is true of arXiv:2106.01715, where cutoff and support are
locked, and NOT of the 2021 archimedean theorem, where the cutoff is frozen at 1.
The trace is reachable from the corpus's machinery; it is not reachable from the
corpus's NUMBERS, because those are all at the wrong bandwidth.

--- CONVENTIONS, AND THE FACTOR OF TWO THAT LIVES IN THEM ---------------------

Basis and normalization are `verify_arch_positivity.py`'s, unchanged, so the
columns here read against that script's: xi_0 = L^-1/2,
xi_n = (-1)^n sqrt(2/L) cos(2 pi n y / L) on [-L/2, L/2], L = log mu, and its
`_h` returns the SYMMETRIZED h_{nm} = xi_n * xi_m^* + xi_m * xi_n^*.  Every
matrix M below represents its functional as a^T M a on g = sum a_n xi_n, with
||g||^2 = a^T a; a column "per unit ||g||^2" is an eigenvalue of M.

The symmetrization is where a factor of two hides, and it is worth stating
because it is the one thing in this script that had to be found rather than
read.  Connes-Consani's 2023 paper writes the Weil form as psi(h) =
psi^#(h + h^sigma) (`Spectraltriples.tex:410`, eq. \label{weilQexp}), so its
W_R^# is applied to the symmetrized function; carried out, W_R^#(h + h^sigma)
is exactly the W_R of the 2021 paper applied to h, with NO factor of two.  The
same is NOT true of eps: eq. (*) is stated against the un-symmetrized f, so its
matrix is int_0^L h eps dy and not twice that.  Get this wrong -- read the
corpus's matrices as (1/2) a^T M a, which the Gram h(0) = 2 I invites -- and the
Sonin form comes out INDEFINITE from mu = 1.8 on.  CHECK 2 is what caught it,
and that is the whole reason it is in the script.

`sigma_arch` of `verify_arch_positivity.py` is W_{0,2}^# - W_R^#; the Weil
functional alone is W_inf = -W_R, and the two agree exactly on vectors with
ghat(+-i/2) = 0, which kill W_{0,2}.

--- CHECKS -------------------------------------------------------------------

CHECK 1 -- the cheap instrument, run before anything is built on it: the c = 2 pi
prolate apparatus against Connes-Consani's own five printed anchors -- lam(0..5)
(`:969`), sum lam(n)^2 = 2(Si(4 pi)/(4 pi) + 1) (`:1101`), t(0..4) and
eps'(1+) = 22.9965 (`:1367`, `:1380`), plus eps'(1+) recovered from (*) by finite
difference.  All reproduce.

CHECK 2 -- the one check that can fail from a wrong eps, and it is not delicate:
tr(theta(g) S theta(g)^*) >= 0 holds for EVERY test function, with no support and
no vanishing condition, because it is a Hilbert-Schmidt norm.  So -W_R + Ehat
must be positive semi-definite at every mu.  It is, by a margin of four orders of
magnitude, at every mu on the grid.  This is an independent instrument in the
sense of `statement-defects.md` sec 2.1: the two matrices come from different
apparatus (a principal-value integral of the Weil distribution; a prolate series
at c = 2 pi) and nothing but Theorem \\label{devil} relates them.

CHECK 3 -- the answer.  The size of the trace, per unit ||g||^2, on the corpus's
own test vectors, over the mu range where the corpus has numbers.

CHECK 4 -- the comparison.  gap = -E, so Theorem 1 IS "-Ehat >= 0 on the
codimension-two subspace".  Verified for mu <= 2, and the mu at which it first
fails is located.

    CORRECTED BY mg-d03b, and read the check's own closing note before its
    table.  Its "min gap (cond.)" column is NOT a margin -- it is
    eps'(1+) L^2 / (2 pi^2 N^2), a closed form in the truncation order, and it
    goes to zero as N grows.  Its `conditions()` second row was also evaluated
    at the wrong endpoint until mg-d03b, which no output here could see.  Both
    are measured in `verify_sonin_margin.py` CHECK 1.  The signs -- "positive
    at every mu on the grid", "indefinite unconditioned" -- are unaffected and
    stand.

CHECK 5 -- the two bandwidths, c = 2 pi against c = 2 pi mu.

Runtime ~3 minutes (measured, 2m54s).  The cost is the eps quadrature and
the N = 80 matrices in equal measure.
"""

import functools

import numpy as np

from verdict import Verdict
from verify_arch_positivity import _h, GAMMA, theta_prime  # noqa: F401

VD = Verdict()


@functools.lru_cache(maxsize=None)
def _gauss(n):
    """Cached Gauss-Legendre nodes.  numpy's leggauss is 10 s at n = 320 and
    16 s at n = 400 on this machine (0.3 s at n = 200): the companion-matrix
    solve behind it is superlinear.  Every quadrature below reuses four node
    sets, so caching turns a twenty-minute script into a ninety-second one."""
    return np.polynomial.legendre.leggauss(n)

CSON = 2 * np.pi          # the Sonin bandwidth: Lambda = 1 in both time and frequency
NMODE = 10                # terms kept in (*); lam(9) ~ 1e-19, CC use 11 for 1e-11
KLEG = 80                 # even Legendre coefficients per prolate mode


# --- the prolate apparatus at bandwidth c ------------------------------------

def _legendre_even(K):
    """Indices 0, 2, ..., 2K of the Legendre basis."""
    return np.arange(0, 2 * K + 1, 2)


def prolate_even(c=CSON, K=KLEG):
    """Even PSWFs at bandwidth c as coefficients on normalized Legendre.

    The prolate operator -d/dx((1-x^2) d/dx) + c^2 x^2 is diagonal-plus-x^2 in
    the normalized Legendre basis, x^2 being the square of the tridiagonal
    multiplication-by-x matrix.  Returns (chi, B) with B[:, n] the coefficients
    of the n-th even mode on bar P_0, bar P_2, ..., sum_k B[k,n]^2 = 1.
    """
    M = 2 * K + 3
    k = np.arange(M)
    off = (k[:-1] + 1) / np.sqrt((2 * k[:-1] + 1) * (2 * k[:-1] + 3))
    X = np.diag(off, 1) + np.diag(off, -1)
    A = np.diag(k * (k + 1.0)) + c ** 2 * (X @ X)
    ev = np.arange(0, M, 2)
    Ae = A[np.ix_(ev, ev)]
    chi, B = np.linalg.eigh(0.5 * (Ae + Ae.T))
    return chi, B


def _legvals(deg_even, xs):
    """P_k(x) for k = 0, 2, ..., 2*len(deg_even)-2, by the three-term recurrence."""
    xs = np.asarray(xs, dtype=float)
    kmax = int(deg_even[-1])
    out = np.empty((kmax + 1, xs.size))
    out[0] = 1.0
    if kmax >= 1:
        out[1] = xs
    for k in range(1, kmax):
        out[k + 1] = ((2 * k + 1) * xs * out[k] - k * out[k - 1]) / (k + 1)
    return out[deg_even]


class Prolate(object):
    """The vectors xi_n of `weil-compo.tex:997` at bandwidth c, and F xi_n.

    xi_n = P_1 phi_n / ||P_1 phi_n|| in Connes-Consani's inner product
    <eta|xi> = int_0^infty, so int_0^1 xi_n^2 = 1, i.e. int_{-1}^1 xi_n^2 = 2.
    The sign is fixed by xi_n(0) > 0; every quantity used below is quadratic in
    xi_n, so no convention rides on it.
    """

    def __init__(self, c=CSON, K=KLEG, nmode=NMODE, nq=320):
        self.c = c
        self.ev = _legendre_even(K)
        chi, B = prolate_even(c, K)
        B = B[:len(self.ev), :nmode]
        self.scale = np.sqrt(2 * self.ev + 1.0)
        # xi_n = sum_k B[k,n] sqrt(2k+1) P_k  (the sqrt(2) of the normalization
        # times bar P_k = sqrt((2k+1)/2) P_k)
        s = np.sign(B.T @ (self.scale * _legvals(self.ev, [0.0])[:, 0]))
        self.B = B * s[None, :]
        self.chi = chi[:nmode]
        self.nmode = nmode
        x, w = _gauss(nq)
        self.xq, self.wq = 0.5 * (x + 1.0), 0.5 * w
        self.XIq = self.at(self.xq)                       # (nmode, nq)
        self.lam = (self.wq[None, :] * self.XIq * self.F(self.xq)).sum(axis=1)
        self.xi1 = self.B.T @ self.scale                  # xi_n(1)

    def at(self, xs):
        """xi_n(x) for |x| <= 1."""
        return self.B.T @ (self.scale[:, None] * _legvals(self.ev, xs))

    def F(self, om):
        """(F xi_n)(omega) = 2 int_0^1 xi_n(x) cos(2 pi x omega) dx, any omega."""
        om = np.asarray(om, dtype=float).ravel()
        K = np.cos(2 * np.pi * np.outer(om, self.xq)) * self.wq[None, :]
        return 2.0 * (self.XIq @ K.T)                     # (nmode, len(om))


# --- epsilon ------------------------------------------------------------------

def epsilon(pr, rho, nq=120):
    """eps(rho) of `weil-compo.tex:1373` for rho >= 1; eps(rho) = eps(1/rho).

    xi_n^an = F xi_n / lam(n), so the coefficient lam^2/(1-lam^2) times 1/lam
    collapses to lam/(1-lam^2) -- which is what is used, since lam(n) is 1e-19
    by n = 9 and dividing by it would be the only unstable step in the script.
    """
    rho = np.atleast_1d(np.asarray(rho, dtype=float))
    coef = pr.lam / (1.0 - pr.lam ** 2)
    x0, w0 = _gauss(nq)
    a = 1.0 / np.maximum(rho, 1.0)
    xs = 0.5 * (1.0 - a)[:, None] * x0[None, :] + 0.5 * (1.0 + a)[:, None]
    ws = 0.5 * (1.0 - a)[:, None] * w0[None, :]
    XIs = pr.at(xs.ravel()).reshape(pr.nmode, *xs.shape)
    Fs = pr.F((rho[:, None] * xs).ravel()).reshape(pr.nmode, *xs.shape)
    out = np.sqrt(rho) * (coef[:, None, None] * XIs * Fs * ws[None]).sum(axis=(0, 2))
    return np.where(rho <= 1.0, 0.0, out)


# --- the three matrices, all in the (1/2) a^T M a convention ------------------

def matrices(pr, L, N, ngl=400, nge=200):
    """(W_inf, W_{0,2}, E) on the basis xi_0..xi_N of `verify_arch_positivity`.

    All three in the a^T M a convention; see the header on the symmetrization.
    W_inf = -W_R, and E is int_0^L h(y) eps(e^y) dy -- the factor two of
    E(f) = int_R f(e^y) eps(e^|y|) dy against the half-range is cancelled by
    f = (1/2) a^T h a, h being symmetrized.
    """
    x, w = _gauss(ngl)
    t, wt = 0.5 * L * (x + 1.0), 0.5 * L * w
    h = _h(L, N, t)
    h0 = _h(L, N, np.array([0.0]))[0]
    W02 = np.tensordot(wt * 2 * np.cosh(t / 2), h, axes=(0, 0))
    ratio = (np.exp(t / 2)[:, None, None] * h - h0[None]) \
        / (np.exp(t) - np.exp(-t))[:, None, None]
    WR = h0 / 2.0 * (GAMMA + np.log(4 * np.pi * (np.exp(L) - 1) / (np.exp(L) + 1))) \
        + np.tensordot(wt, ratio, axes=(0, 0))
    xe, we = _gauss(nge)
    te, wte = 0.5 * L * (xe + 1.0), 0.5 * L * we
    # E(f) = int_R f(e^y) eps(e^|y|) dy = 2 int_0^L (1/2) a^T h(y) a eps(e^y) dy
    Eh = np.tensordot(wte * epsilon(pr, np.exp(te)), _h(L, N, te), axes=(0, 0))
    sym = lambda M: 0.5 * (M + M.T)
    return sym(-WR), sym(W02), sym(Eh)


def conditions(L, N):
    """The two rows ghat(0) = 0 and ghat(i/2) = 0 in the cosine basis."""
    n = np.arange(N + 1)
    c = np.where(n == 0, L ** -0.5, ((-1.0) ** n) * np.sqrt(2.0 / L))
    v0 = np.where(n == 0, c * L, 0.0)                       # int cos(2 pi n y/L) dy
    a = 2 * np.pi * n / L
    # int_{-L/2}^{L/2} cos(a y) e^{y/2} dy, done exactly:
    #   = [e^{y/2}(cos(a y)/2 + a sin(a y))/(1/4 + a^2)] from -L/2 to L/2
    #
    # The antiderivative is evaluated at y = +-q with q = L/2, so the factor is
    # e^{+-q/2}, not e^{+-q}.  It was written `np.exp(q)` until mg-d03b, which
    # made row 1 the integral over [-L, L] rather than over the support, wrong
    # by 1.5 in absolute terms at mu = 5 -- its n = 0 entry came out c 4 sinh(L/2)
    # where ghat(i/2) is c 4 sinh(L/4).  Nothing in this script's output moved
    # when it was fixed, which is exactly why nothing caught it: CHECK 4's
    # conditioned column is eps'(1+) L^2 / (2 pi^2 N^2) whichever two conditions
    # are imposed.  See `sonin-margin.md` sec 2 and `verify_sonin_margin.py`
    # CHECK 1, which measures both halves of that sentence.
    q = L / 2.0
    num = np.exp(q / 2) * (np.cos(a * q) / 2 + a * np.sin(a * q)) \
        - np.exp(-q / 2) * (np.cos(a * q) / 2 - a * np.sin(a * q))
    v1 = c * num / (0.25 + a ** 2)
    return v0, v1


def restrict(M, rows):
    """M restricted to the orthogonal complement of the given rows."""
    Q, _ = np.linalg.qr(np.asarray(rows).T)
    B = np.eye(M.shape[0]) - Q @ Q.T
    U, s, _ = np.linalg.svd(B)
    U = U[:, s > 1e-10]
    return U.T @ M @ U


# --- test vectors -------------------------------------------------------------

def vec_witness(L, N):
    """`verify_arch_positivity.witness`'s explicit f, in the cosine basis.

    cos(pi y/L) + kappa cos(3 pi y/L) on [-L/2, L/2].  It is not in the span of
    the cosine basis (half-integer frequencies), so it is projected; the
    projection error is reported by the caller as the residual norm.
    """
    y = np.linspace(-L / 2, L / 2, 40001)
    wy = np.gradient(y) * 0 + (y[1] - y[0])
    wy[0] = wy[-1] = 0.5 * (y[1] - y[0])          # trapezoid on a fine grid
    m1, m3 = np.cos(np.pi * y / L), np.cos(3 * np.pi * y / L)
    kap = -np.sum(wy * m1 * np.cosh(y / 2)) / np.sum(wy * m3 * np.cosh(y / 2))
    f = m1 + kap * m3
    n = np.arange(N + 1)
    c = np.where(n == 0, L ** -0.5, ((-1.0) ** n) * np.sqrt(2.0 / L))
    basis = c[:, None] * np.cos(2 * np.pi * n[:, None] * y[None, :] / L)
    a = (basis * (wy * f)[None, :]).sum(axis=1)
    resid = np.sum(wy * f ** 2) - a @ a
    return a, max(resid, 0.0)


def vec_prolate2(L, N, mu):
    """The two-mode prolate combination at the corpus's own bandwidth c = 2 pi mu.

    g(y) = psi_4(0) psi_0(2y/L) - psi_0(0) psi_4(2y/L), the CCM coefficient
    choice recorded at `citation-audit.md` sec 4.2 (phi_2n = psi_2n psi_0(0) -
    psi_0 psi_2n(0)), with psi_0, psi_4 the even prolate modes of index 0 and 4
    -- even-only indices 0 and 2 -- at c = 2 pi mu.  This is the corpus's
    h_lambda = alpha h_{0,lambda} + beta h_{4,lambda} (`start.tex:138`) used
    directly as a test function.  It is NOT k_lambda = E(h_lambda): building the
    summation operator E is out of this script's scope, and the difference is
    stated in `sonin-trace.md` sec 5 rather than papered over.
    """
    pr = Prolate(c=2 * np.pi * mu, K=KLEG, nmode=3, nq=320)
    y = np.linspace(-L / 2, L / 2, 40001)
    wy = np.full_like(y, y[1] - y[0])
    wy[0] = wy[-1] = 0.5 * (y[1] - y[0])          # trapezoid on a fine grid
    u = 2 * y / L
    vals = pr.at(np.abs(u))
    p0 = pr.at(np.array([0.0]))[:, 0]
    f = p0[2] * vals[0] - p0[0] * vals[2]
    n = np.arange(N + 1)
    c = np.where(n == 0, L ** -0.5, ((-1.0) ** n) * np.sqrt(2.0 / L))
    basis = c[:, None] * np.cos(2 * np.pi * n[:, None] * y[None, :] / L)
    a = (basis * (wy * f)[None, :]).sum(axis=1)
    resid = np.sum(wy * f ** 2) - a @ a
    return a, max(resid, 0.0)


def _q(M, a):
    """The functional's value on g = sum a_n xi_n, per unit ||g||^2."""
    return (a @ M @ a) / (a @ a)


MUS = (1.2, 1.5, 1.8, 2.0, 2.2, 2.271, 2.5, 3.0)


# --- checks -------------------------------------------------------------------

def check1():
    print("CHECK 1 -- the c = 2 pi prolate apparatus against Connes-Consani's own")
    print("anchors, before anything is built on it (`statement-defects.md` sec 2.1).")
    print()
    pr = Prolate()
    cc_lam = np.array([0.999971, -0.979485, 0.524086, -0.0589766,
                       0.00273233, -0.0000762914])
    print("  lambda(n), `weil-compo.tex:969`")
    print("   %3s %16s %16s" % ("n", "ours", "CC"))
    for n in range(6):
        print("   %3d %16.7g %16.7g" % (n, pr.lam[n], cc_lam[n]))
    ok = np.max(np.abs(pr.lam[:6] - cc_lam) / np.abs(cc_lam)) < 5e-6
    VD.check(ok, "CHECK 1: lambda(0..5) at c = 2 pi reproduce `weil-compo.tex:969`")
    print("   max relative deviation %.1e" % np.max(np.abs(pr.lam[:6] - cc_lam)
                                                    / np.abs(cc_lam)))
    print()

    # sum lam(n)^2 = 2 (Si(4 pi)/(4 pi) + 1)   -- `weil-compo.tex:1101`
    xs = np.linspace(0.0, 4 * np.pi, 400001)
    sinc = np.ones_like(xs)
    sinc[1:] = np.sin(xs[1:]) / xs[1:]
    target = 2 * (np.trapezoid(sinc, xs) / (4 * np.pi) + 1)
    got = (pr.lam ** 2).sum()
    print("  sum lambda(n)^2  = %.10f" % got)
    print("  2(Si(4pi)/4pi+1) = %.10f      `weil-compo.tex:1101`, CC: ~2.237484835"
          % target)
    VD.check(abs(got - target) < 1e-8,
             "CHECK 1: sum lambda(n)^2 = 2(Si(4 pi)/(4 pi) + 1)")
    print()

    t = pr.lam ** 2 / (1 - pr.lam ** 2) * pr.xi1 ** 2
    cc_t = np.array([11.9719, 8.77574, 2.20528, 0.0433983, 0.000125459])
    print("  t(n) = lam^2/(1-lam^2) xi_n(1)^2, `weil-compo.tex:1380`")
    print("   %3s %16s %16s" % ("n", "ours", "CC"))
    for n in range(5):
        print("   %3d %16.6g %16.6g" % (n, t[n], cc_t[n]))
    VD.check(np.max(np.abs(t[:5] - cc_t) / cc_t) < 1e-4,
             "CHECK 1: t(0..4) reproduce `weil-compo.tex:1380`")
    print("  sum t(n) = eps'(1+) = %.6f      CC: 22.9965" % t.sum())
    VD.check(abs(t.sum() - 22.9965) < 5e-4,
             "CHECK 1: sum t(n) = eps'(1+) = 22.9965 (`weil-compo.tex:1367`)")
    print()

    print("  and eps'(1+) recovered from the series (*) itself, by difference:")
    for hh in (1e-3, 1e-4, 1e-5):
        d = epsilon(pr, np.array([1.0 + hh]))[0] / hh
        print("    (eps(1+h) - eps(1))/h  at h = %.0e :  %.5f" % (hh, d))
    d = epsilon(pr, np.array([1.0 + 1e-5]))[0] / 1e-5
    VD.check(abs(d - t.sum()) < 5e-3,
             "CHECK 1: eps from (*) has the derivative Lemma `epsilon'` predicts")
    print()
    print("  Five anchors, five reproductions.  Everything below rests on this.")
    print()
    return pr


def check2(pr):
    print("CHECK 2 -- tr(theta(g) S theta(g)^*) >= 0 for EVERY g: the independent")
    print("instrument.  -W_R + Ehat must be positive semi-definite at every mu, with")
    print("no support and no vanishing condition, because it is ||S theta(g)^*||_HS^2.")
    print("W_R is a principal value of the Weil distribution; Ehat is a prolate series")
    print("at c = 2 pi.  Nothing but Theorem `devil` relates them.")
    print()
    print("  %8s %5s %16s %16s %14s" % ("mu", "N", "min Sonin", "max Sonin", "min/max"))
    worst = 1.0
    for mu in MUS:
        L = np.log(mu)
        for N in (40, 80):
            MW, _, Eh = matrices(pr, L, N)
            e = np.linalg.eigvalsh(MW + Eh)
            worst = min(worst, e[0] / e[-1])
            if N == 80:
                print("  %8.4f %5d %16.6e %16.6e %14.2e"
                      % (mu, N, e[0], e[-1], e[0] / e[-1]))
        VD.check(e[0] > 0.0,
                 "CHECK 2: Sonin trace form is positive definite at mu = %g" % mu)
    print()
    print("  Positive definite at every mu, and this is a real constraint: read at")
    print("  (1/2) a^T M a instead -- the reading the Gram h(0) = 2 I invites, and the")
    print("  one this script was first written with -- the same matrices give a")
    print("  NEGATIVE smallest eigenvalue from mu = 1.8 on.  A wrong eps, or a wrong")
    print("  normalization, does not survive eight values of mu.  The smallest")
    print("  eigenvalue does fall to %.0e of the largest, which is CHECK 3's answer" % worst)
    print("  seen from the side: the trace is small, and it is not zero.")
    print()


def check3(pr):
    print("CHECK 3 -- THE ANSWER.  Size of the Sonin trace, per unit ||g||^2, on the")
    print("corpus's own test vectors.  Columns: S = tr(theta(g) S theta(g)^*),")
    print("W = W_inf(g*g^*) = -W_R, gap = W - S = -E.  `arch` is")
    print("`verify_arch_positivity.py`'s W_{0,2} - W_R, for cross-reference.")
    print()
    N = 80
    print("  (a) on the minimizing direction of the Weil form W_inf")
    print("  %8s %14s %14s %14s %10s" % ("mu", "S", "W", "gap = W - S", "S/W"))
    for mu in MUS:
        L = np.log(mu)
        MW, W02, Eh = matrices(pr, L, N)
        ev, U = np.linalg.eigh(MW)
        a = U[:, 0]
        S, W = _q(MW + Eh, a), _q(MW, a)
        print("  %8.4f %14.6e %14.6e %14.6e %10.4f" % (mu, S, W, W - S, S / W))
    print()
    print("  (b) on the smallest direction of the Sonin form itself (the smallest")
    print("      the trace can be made, over all g)")
    print("  %8s %14s %14s %14s" % ("mu", "min S", "W there", "gap there"))
    for mu in MUS:
        L = np.log(mu)
        MW, W02, Eh = matrices(pr, L, N)
        ev, U = np.linalg.eigh(MW + Eh)
        a = U[:, 0]
        print("  %8.4f %14.6e %14.6e %14.6e"
              % (mu, _q(MW + Eh, a), _q(MW, a), _q(-Eh, a)))
    print()
    print("  (c) on `verify_arch_positivity.witness`'s explicit test function")
    print("      f = cos(pi y/L) + kappa cos(3 pi y/L), which has ghat(+-i/2) = 0")
    print("      so that arch = W_inf on it exactly")
    print("  %8s %14s %14s %14s %10s %10s"
          % ("mu", "S", "W", "gap", "S/W", "proj err"))
    for mu in MUS:
        L = np.log(mu)
        MW, W02, Eh = matrices(pr, L, N)
        a, r = vec_witness(L, N)
        S, W = _q(MW + Eh, a), _q(MW, a)
        print("  %8.4f %14.6e %14.6e %14.6e %10.4f %10.1e"
              % (mu, S, W, W - S, S / W, r / (a @ a)))
    print()
    print("  (d) on the two-mode prolate combination at the corpus's bandwidth")
    print("      c = 2 pi mu (`start.tex:138`; NOT k_lambda = E(h_lambda))")
    print("  %8s %14s %14s %14s %10s %10s"
          % ("mu", "S", "W", "gap", "S/W", "proj err"))
    for mu in MUS:
        L = np.log(mu)
        MW, W02, Eh = matrices(pr, L, N)
        a, r = vec_prolate2(L, N, mu)
        S, W = _q(MW + Eh, a), _q(MW, a)
        print("  %8.4f %14.6e %14.6e %14.6e %10.4f %10.1e"
              % (mu, S, W, W - S, S / W, r / (a @ a)))
    print()
    print("  (e) how the floor moves with mu, against the corpus's own rate")
    ms = []
    for mu in MUS:
        MW, _, Eh = matrices(pr, np.log(mu), N)
        ms.append(np.linalg.eigvalsh(MW + Eh)[0])
    ms = np.array(ms)
    mus = np.array(MUS)
    sel = mus >= 1.8
    rate = np.polyfit(mus[sel], np.log(ms[sel]), 1)[0]
    print("  %8s %16s" % ("mu", "min S"))
    for mu, v in zip(mus, ms):
        print("  %8.4f %16.6e" % (mu, v))
    print("  least-squares rate of log(min S) over mu >= 1.8:  %+.4f per unit mu"
          % rate)
    print("  the corpus's headline rate, limsup mu^-1 log s(mu) <= -4 pi:  %+.4f"
          % (-4 * np.pi))
    VD.check(rate > -4 * np.pi,
             "CHECK 3: the Sonin trace floor decays strictly slower than -4 pi")
    print()
    print("  ANSWER.  The trace is small and it is not the corpus's small.  Its floor")
    print("  -- the least it can be made, over all g -- is 2.5e-3 at mu = 2 and 1.5e-4")
    print("  at mu = 3, and on the corpus's own test vectors it is 2e-2 to 7e-1: the")
    print("  same order as the Weil functional, not a correction to it.  It decays at")
    print("  %+.2f per unit mu, against the -4 pi = -12.57 of" % rate)
    print("  `limsup mu^-1 log s(mu) <= -4 pi`.  At mu = 2 the corpus's deficit")
    print("  1 - chi_4 is ~1e-11 and the trace's floor is 2.5e-3 -- eight orders")
    print("  apart, and separating exponentially.  Nothing the corpus has bounded is")
    print("  a bound on this.")
    print()


def check4(pr):
    print("CHECK 4 -- gap = -E, so Connes-Consani's Theorem 1 IS the statement that")
    print("-Ehat is positive on the codimension-two subspace {ghat(0) = ghat(i/2) = 0}.")
    print("Their hypothesis is supp g in [2^-1/2, 2^1/2], i.e. mu <= 2.")
    print()
    N = 80
    print("  %8s %18s %18s %10s" % ("mu", "min gap (uncond.)", "min gap (cond.)", "Thm 1"))
    first_fail = None
    for mu in MUS:
        L = np.log(mu)
        _, _, Eh = matrices(pr, L, N)
        gu = np.linalg.eigvalsh(-Eh)[0]
        v0, v1 = conditions(L, N)
        gc = np.linalg.eigvalsh(restrict(-Eh, [v0, v1]))[0]
        holds = gc >= -1e-12
        if not holds and first_fail is None:
            first_fail = mu
        print("  %8.4f %18.6e %18.6e %10s"
              % (mu, gu, gc, "holds" if holds else "FAILS"))
        if mu <= 2.0:
            VD.check(holds,
                     "CHECK 4: Theorem 1 (-E >= 0 on the conditioned subspace) "
                     "holds at mu = %g" % mu)
    print()
    print("  Read the two columns apart.  Unconditioned, -Ehat is negative at every")
    print("  mu, including mu = 2: the trace exceeds the Weil functional on some")
    print("  direction even inside the theorem's support range, so the vanishing")
    print("  conditions are not decoration.  Conditioned, the theorem holds where it")
    print("  is claimed, and past it, to mu = 3.")
    if first_fail is not None:
        print("  It first fails on this grid at mu = %.4f." % first_fail)
    else:
        print("  It does not fail anywhere on this grid.")
    print()
    print("  READ THE CONDITIONED COLUMN AS A MARGIN AND YOU WILL BE WRONG (mg-d03b).")
    print("  -Ehat is a compact operator, so its eigenvalues accumulate at 0 and the")
    print("  smallest one at N = 80 is a statement about N, not about the theorem:")
    print("  it is eps'(1+) L^2 / (2 pi^2 N^2) to four figures at every mu above,")
    print("  8.7459e-5 at mu = 2.  The minimising vector is the top cosine mode.")
    print("  `sonin-margin.md` and `verify_sonin_margin.py` CHECK 1 do that")
    print("  arithmetic; what is truncation-stable is the INERTIA, and by it the")
    print("  theorem's conclusion holds to mu = 6.19 and is false from mu = 8.")
    print()


def check5(pr):
    print("CHECK 5 -- the two bandwidths.  The Sonin trace's prolate system is")
    print("c = 2 pi (fixed); the corpus's is c = 2 pi mu.  They are the same family")
    print("and different numbers, and the corpus has no number at c = 2 pi.")
    print()
    print("  %8s %18s %18s %18s"
          % ("mu", "1-lam(0)^2 c=2pi", "1-Lam_0 c=2pi mu", "ratio"))
    base = 1 - pr.lam[0] ** 2
    for mu in MUS:
        p2 = Prolate(c=2 * np.pi * mu, K=KLEG, nmode=3, nq=320)
        d = 1 - p2.lam[0] ** 2
        print("  %8.4f %18.6e %18.6e %18.6e" % (mu, base, d, d / base))
    print()
    print("  At mu = 2 the corpus's concentration defect is ~1e-11 and the Sonin")
    print("  system's is ~5.7e-5: six orders of magnitude, and the gap widens as")
    print("  e^{-4 pi mu}.  Anything transported between them by name alone is wrong")
    print("  by that factor.")
    print()


if __name__ == "__main__":
    np.set_printoptions(linewidth=120)
    pr = check1()
    check2(pr)
    check3(pr)
    check4(pr)
    check5(pr)
    print("HOUSE RULE.  CHECK 4's statement -- 'the gap W_inf - Tr(theta(g) S")
    print("theta(g)^*) is negative on some direction at every mu on this grid,")
    print("including mu = 2, before the two vanishing conditions are imposed' -- is")
    print("FALSE for W_lambda -> -W_lambda: the trace does not move under that")
    print("substitution and W_inf does, so the sign of the difference does.  So is")
    print("CHECK 3's 'the trace exceeds the Weil functional on the minimizing")
    print("direction'.  CHECKS 1, 2 and 5 are sign-blind: CHECK 2's positivity is a")
    print("Hilbert-Schmidt norm and mentions no Weil form at all.")
    VD.finish()
