#!/usr/bin/env python3
"""What lives in the 8.7e-5?  Four checks for `sonin-margin.md` (mg-d03b).  Needs numpy.

Two readings drawn from CHECK 4 below are REFUTED by mg-0b7a (`sonin-ceiling.md`) --
this script computes the EVEN BLOCK ALONE.  See (3) and CHECK 4's own output; the
checks and their values are unchanged and still pass.

    cd notes && python verify_sonin_margin.py            # 4m59s measured
    cd notes && python verify_sonin_margin.py --quick    # 34s, same checks

[`sonin-trace.md`](sonin-trace.md) (mg-5210) established, and this script
re-verifies rather than inherits, that Connes-Consani's archimedean theorem
(arXiv:2006.13771, Theorem 1) is equivalent -- via their own Theorem
`\\label{devil}`, tr(theta(f) S) = W_inf(f) + E(f) -- to the single statement

    the quadratic form  -E  is positive on  {ghat(0) = ghat(i/2) = 0},

    E(f) = int f(rho) eps(rho) d*rho,   f = g * g^*,   supp g in [mu^-1/2, mu^1/2].

It then reported that the smallest eigenvalue of -E on that codimension-two
subspace is 8.7e-5 at mu = 2, "a margin of one part in 10^4", and that the form
stays positive to mu = 3, past where the theorem claims it.

--- WHAT THIS SCRIPT FOUND, AND IT IS TWO DEFECTS AND A STRUCTURE -------------

(1) 8.7e-5 IS NOT A MARGIN.  -E is a compact operator (continuous kernel on a
bounded interval), so its eigenvalues accumulate at 0, and the smallest
eigenvalue of an N-term truncation is not an approximation to anything -- it is
a statement about N.  Concretely, the symbol of -E is -eps_hat(t), and the kink
of eps at rho = 1 (eps(1) = 0, eps'(1+) = 22.9965, `weil-compo.tex:1367`) forces

    eps_hat(t) ~ -2 eps'(1+) / t^2      (t -> infinity),

so the smallest eigenvalue resolved by N cosine modes on [-L/2, L/2] is
-eps_hat at the truncation frequency t = 2 pi N / L, i.e.

    min eigenvalue (codim 2, N modes)  =  eps'(1+) L^2 / (2 pi^2 N^2).

CHECK 1 evaluates that closed form against all eight rows of `sonin-trace.md`
sec 2.2 at N = 40, 80, 160: twenty-four cells, every one within 0.15% -- including
the headline, eps'(1+) (log 2)^2 / (2 pi^2 80^2) = 8.7459e-5 against the printed
8.747916e-5.  The column contains no information about the theorem.  It is the
truncation order, read back out.  And the minimising direction is the last basis
vector: at N = 40, 80, 160 the eigenvector is the top cosine mode with weight
1.000, so "the near-null direction" is an artefact that moves when N moves.

(2) THE SECOND CONDITION ROW WAS EVALUATED AT THE WRONG ENDPOINT, and mg-d03b
fixed it.  `verify_sonin_trace.conditions()` computed ghat(i/2) by evaluating the
antiderivative of cos(a y) e^{y/2} at y = +-L instead of y = +-L/2 (`exp(q)`
where `exp(q/2)` is meant, q = L/2), so the condition it imposed was not
ghat(i/2) = 0.  CHECK 1 reproduces the old row inline -- so the defect stays
measurable after the repair -- and puts both it and the fixed one against direct
integration: the old row is wrong by 1.5 in absolute terms at mu = 5, N = 6, the
new one right to 2e-11.  It did not show up in mg-5210's tables because both rows
produce the same N^{-2} artefact of (1); the two runs of that script, before and
after the fix, are byte-identical.  That is the exact shape
[`statement-defects.md`](statement-defects.md) describes, a discrepancy the
downstream use does not exercise.

(3) THE TRUNCATION-STABLE STATEMENT IS THE INERTIA, AND IT ANSWERS THE
HYPOTHESIS.  What does not move with N is the *number of negative eigenvalues*
and their values: the counts are identical and the values agree to 1e-3 between
N = 60 and N = 120, because they live at low frequency where the basis is
complete long before the truncation bites.  With the conditions computed
correctly, CHECKS 3 and 4 find (N = 120; each is an upper bound falling in N)

    codim k        mu_c(k), THIS SCRIPT      mu_c(k), full space (mg-0b7a)
    ---------------------------------------------------------------------
      0 (none)     indefinite at every mu    indefinite
      1            2.763                     1.771   <-- BELOW 2
      2 (Thm 1)    6.174                     2.754
      3           13.01                      4.140
      4           26.46                      6.024

*** CORRECTED BY mg-0b7a (`sonin-ceiling.md`, `verify_sonin_ceiling.py` CHECK 5).
The basis below -- xi_n = cos(2 pi n y / L) -- spans the EVEN BLOCK ALONE, E is a
convolution form so E(g) = E(g_ev) + E(g_odd), and Theorem 1 imposes no parity
condition, so the admissible odd g are missing from this script's left column.
Two readings drawn from it below do not survive:

  - "mu <= 2 is an artefact by a FACTOR OF THREE" -- it is a factor 1.38
    (2.754 / 2), not 3.09.  That mu <= 2 is an artefact at all survives; the
    size does not, and the hypothesis is much closer to sharp than stated here.
  - "ONE of the two conditions is enough at mu = 2" -- FALSE, not merely
    imprecise.  mu_c(1) = 1.771 < 2 on the full space: an odd g satisfies
    ghat(0) = 0 for free, so one condition is no condition at all on half the
    space, and the second does real work inside Theorem 1's own range.

The left column and every check below are unchanged and still pass: they are
correct statements about the even block, and `verify_sonin_ceiling.py` uses them
as its baseline.  Only the readings are corrected, in place.  Both corrected
numbers are mg-0b7a's, quoted, not re-derived here. ***

The theorem's conclusion does genuinely fail past mu_c(2), on either column.
It has to: eps > 0, so eps_hat(0) = 5.37 > 0, so the symbol
of -E is negative at low frequency and only a support short enough to keep ghat
out of that band can save it.  log mu_c is close to linear in k, slope 0.752
measured against the 2 pi / t_0 = 0.999 the symbol suggests -- CHECK 4.

--- CONVENTIONS --------------------------------------------------------------

Basis, normalisation and the a^T M a convention are `verify_arch_positivity.py`'s
and `verify_sonin_trace.py`'s, unchanged, so the columns read against theirs.
xi_0 = L^-1/2, xi_n = (-1)^n sqrt(2/L) cos(2 pi n y / L) on [-L/2, L/2],
L = log mu, and `_h` returns the symmetrised h_{nm}.

eps is rebuilt here rather than imported, for one reason: `verify_sonin_trace`'s
`epsilon` evaluates F xi_n by a fixed 320-node Gauss rule and the x-integral by a
fixed 120-node one, both of which stop resolving cos(2 pi rho x) around rho = 60.
CHECK 2 shows the two agreeing to 1e-11 for rho <= 50 and the old one returning
2.91 where the true value is 0.0997 at rho = 100.  Nothing in mg-5210 used
rho > 3, so no number of its moves; this script needs rho up to 60.  The
replacement evaluates F xi_n in closed form, int_{-1}^1 P_k(x) e^{izx} dx =
2 i^k j_k(z), with the spherical Bessel functions by Miller downward recurrence.

--- HOUSE RULE ---------------------------------------------------------------

Stated per check at the end.  The two headline statements -- "Theorem 1's
conclusion holds to mu = 6.17, not 2" (even block; 2.754 on the full space,
mg-0b7a) and "it fails past that" -- are statements
about W_inf(g*g^*) >= Tr(theta(g) S theta(g)^*) and are **FALSE for
W_lambda -> -W_lambda**: the trace does not move under that substitution and
W_inf does.  Everything about eps alone, including the whole of (1) and (2), is
sign-blind and is marked so.
"""

import sys

import numpy as np

from verdict import Verdict
from verify_arch_positivity import _h
from verify_sonin_trace import Prolate, epsilon as eps_mg5210

VD = Verdict()

QUICK = "--quick" in sys.argv

EPS_PRIME_1 = 22.996476        # eps'(1+), `weil-compo.tex:1367` prints 22.9965
MU_MAX = 60.0                  # the largest support this script computes at
THETA_ZERO = 6.289835989       # where theta' changes sign, `verify_arch_positivity`


# --- spherical Bessel, and an eps that survives large rho ---------------------

def sph_j(rows, z):
    """j_k(z) for k in `rows`, by Miller downward recurrence, z > 0.

    Normalised on whichever of j_0 = sin z / z and j_1 = sin z / z^2 - cos z / z
    is the larger in magnitude.  Normalising on j_0 alone -- the textbook
    recipe -- loses everything at z near a multiple of pi, where j_0 vanishes;
    that was found here by the identity int_{-1}^1 P_2 cos(pi x) dx = -2 j_2(pi)
    coming out 30% wrong.

    Only the rows asked for are stored: the caller wants the even Legendre
    degrees, half of them, and the array is (len(rows), len(z)).
    """
    z = np.asarray(z, dtype=float).ravel()
    rows = np.asarray(rows, dtype=int)
    want = {int(k): i for i, k in enumerate(rows)}
    K0 = int(rows.max() + 60 + 1.5 * float(np.max(z)))
    jkp1 = np.zeros_like(z)
    jk = np.full_like(z, 1e-290)
    out = np.zeros((rows.size, z.size))
    j1hat = np.zeros_like(z)
    for k in range(K0, -1, -1):
        if k in want:
            out[want[k]] = jk
        if k == 1:
            j1hat = jk
        jkm1 = (2 * k + 1) / z * jk - jkp1
        jkp1, jk = jk, jkm1
        if np.any(np.abs(jk) > 1e250):
            sc = np.where(np.abs(jk) > 1e250, 1e-250, 1.0)
            jk, jkp1, j1hat, out = jk * sc, jkp1 * sc, j1hat * sc, out * sc[None, :]
    j0, j1 = np.sin(z) / z, np.sin(z) / z ** 2 - np.cos(z) / z
    scale = np.where(np.abs(j1) > np.abs(j0), j1 / j1hat, j0 / jkp1)
    return out * scale[None, :]


class ProlateExact(Prolate):
    """`verify_sonin_trace.Prolate` with F xi_n in closed form at any omega."""

    def F(self, om):
        om = np.asarray(om, dtype=float).ravel()
        J = sph_j(self.ev, 2 * np.pi * np.maximum(om, 1e-13))
        sgn = (-1.0) ** (self.ev // 2)
        return 2.0 * (self.B * (self.scale * sgn)[:, None]).T @ J


def comp_gauss(a, b, npan, order=16):
    """Composite Gauss-Legendre: `npan` panels of `order` nodes on [a, b]."""
    x, w = np.polynomial.legendre.leggauss(order)
    e = np.linspace(a, b, npan + 1)
    lo, hi = e[:-1, None], e[1:, None]
    xs = (0.5 * (hi - lo) * x[None, :] + 0.5 * (hi + lo)).ravel()
    ws = (0.5 * (hi - lo) * w[None, :] * np.ones_like(x)[None, :]).ravel()
    return xs, ws


def eps_exact(pr, rho, per_wave=6, order=16):
    """eps(rho) of `weil-compo.tex:1373`, x-quadrature resolved to cos(2 pi rho x).

    One Bessel recurrence for all rho: its length is set by the largest argument,
    so evaluating rho one at a time costs O(n rho_max) recurrences instead of one.
    """
    rho = np.atleast_1d(np.asarray(rho, dtype=float))
    coef = pr.lam / (1.0 - pr.lam ** 2)
    out = np.zeros_like(rho)
    idx, XS, WS, RS = [], [], [], []
    for i, r in enumerate(rho):
        if r <= 1.0:
            continue
        npan = max(4, int(np.ceil(2 * per_wave * r / order)))
        xs, ws = comp_gauss(1.0 / r, 1.0, npan, order)
        idx.append(np.full(xs.size, i))
        XS.append(xs)
        WS.append(ws)
        RS.append(np.full(xs.size, r))
    if not idx:
        return out
    idx, XS = np.concatenate(idx), np.concatenate(XS)
    WS, RS = np.concatenate(WS), np.concatenate(RS)
    # Sorted by the Bessel argument, so that each chunk's recurrence is only as
    # long as its own largest argument needs.  Most nodes carry a small rho x
    # even when rho_max is 60, and an unsorted pass pays rho_max for all of them.
    order_z = np.argsort(RS * XS)
    idx, XS, WS, RS = idx[order_z], XS[order_z], WS[order_z], RS[order_z]
    contrib = np.empty(XS.size)
    # 50k, not 400k: `sph_j` holds a (rows, chunk) array and rescales it in
    # place, so a chunk of 400k is a hundred megabytes that gets copied.
    for a in range(0, XS.size, 50000):
        b = min(a + 50000, XS.size)
        contrib[a:b] = (coef[:, None] * pr.at(XS[a:b])
                        * pr.F(RS[a:b] * XS[a:b])).sum(axis=0) * WS[a:b]
    np.add.at(out, idx, contrib)
    return out * np.sqrt(np.maximum(rho, 1.0)) * (rho > 1.0)


class EpsTable(object):
    """eps(e^y) on a grid fine enough to interpolate, built once.

    The matrices below want eps at a few thousand quadrature nodes per mu; the
    quadrature cost of eps grows linearly in rho, so tabulate and interpolate.
    The grid step is 1/6000 of a unit in y, against an oscillation of period
    1/rho <= 1/60, so the interpolation error is four orders below the 1e-3
    oscillation amplitude -- CHECK 2 measures it against `eps_exact` directly.
    """

    def __init__(self, pr, ymax, n):
        self.y = np.linspace(0.0, ymax, n)
        self.e = eps_exact(pr, np.exp(self.y))

    def __call__(self, y):
        return np.interp(y, self.y, self.e)


# --- the form -----------------------------------------------------------------

def E_matrix(eps, L, N, order=16, chunk=64):
    """int_0^L h(y) eps(e^y) dy, in `verify_sonin_trace.matrices`' convention.

    Chunked over the y-quadrature so that N can be large: `_h` returns a
    (T, N+1, N+1) array and T x N^2 is what runs out of memory first.
    """
    t, wt = comp_gauss(0.0, L, max(80, int(30 * L) + 60), order)
    ev = eps(t)
    out = np.zeros((N + 1, N + 1))
    for a in range(0, t.size, chunk):
        b = min(a + chunk, t.size)
        out += np.tensordot(wt[a:b] * ev[a:b], _h(L, N, t[a:b]), axes=(0, 0))
    return 0.5 * (out + out.T)


def cond_row(L, N, j):
    """ghat(i j / 2) on even g:  int_{-L/2}^{L/2} xi_n(y) e^{j y / 2} dy.

    j = 0 and j = 1 are Theorem 1's two conditions.  Closed form:
    int_{-q}^{q} cos(a y) e^{b y} dy = 2 (b cos(aq) sinh(bq) + a sin(aq) cosh(bq))
                                       / (a^2 + b^2),  b = j/2, q = L/2.
    CHECK 1 puts this against direct integration, and against the row
    `verify_sonin_trace.conditions()` returns.
    """
    n = np.arange(N + 1)
    a = 2 * np.pi * n / L
    c = np.where(n == 0, L ** -0.5, ((-1.0) ** n) * np.sqrt(2.0 / L))
    if j == 0:
        return c * np.where(n == 0, L, 0.0)
    b, q = j / 2.0, L / 2.0
    return c * 2 * (b * np.cos(a * q) * np.sinh(b * q)
                    + a * np.sin(a * q) * np.cosh(b * q)) / (a ** 2 + b ** 2)


def restrict(M, rows):
    """M restricted to the orthogonal complement of the given rows."""
    Q, _ = np.linalg.qr(np.asarray(rows).T)
    U, s, _ = np.linalg.svd(np.eye(M.shape[0]) - Q @ Q.T)
    U = U[:, s > 1e-10]
    return U.T @ M @ U


def spectrum(eps, mu, N, k):
    """Eigenvalues of -E at support mu, N modes, on the codimension-k subspace."""
    L = np.log(mu)
    A = -E_matrix(eps, L, N)
    if k == 0:
        return np.linalg.eigvalsh(A)
    return np.linalg.eigvalsh(restrict(A, [cond_row(L, N, j) for j in range(k)]))


# --- eps_hat, the symbol ------------------------------------------------------

class Symbol(object):
    """eps_hat(t) = int_R eps(e^|y|) e^{-i t y} dy, the symbol of E.

    -eps_hat(t) is the Rayleigh quotient of -E on a wave of frequency t in the
    long-support limit, and every structural statement in this script is read
    off it.

    Computed as the transform of eps(e^|y|) - e^{-|y|/2} plus the transform of
    e^{-|y|/2}, which is 1/(1/4 + t^2) exactly.  Subtracting the asymptotic
    rather than splicing it on at y = Y is not tidiness: a splice leaves a jump
    of size |eps e^{y/2} - 1| ~ 1e-2 at the join, whose transform decays like
    1/t, and multiplied by the t^2/2 of the tail law that spurious term is +-21
    at t = 200 against a true value of -23.  The subtracted version leaves only
    the true remainder, which is O(e^{-3Y/2}).
    """

    def __init__(self, pr, Y=4.5, npan=110, order=16):
        self.Y = Y
        self.y, self.w = comp_gauss(0.0, Y, npan, order)
        self.d = eps_exact(pr, np.exp(self.y)) - np.exp(-self.y / 2)
        self.dropped = abs(self.d[-1])

    def __call__(self, t):
        t = np.atleast_1d(np.asarray(t, dtype=float))
        head = 2.0 * (self.w[None, :] * self.d[None, :]
                      * np.cos(np.outer(t, self.y))).sum(axis=1)
        return head + 1.0 / (0.25 + t ** 2)


def bisect(f, lo, hi, n=60):
    flo = f(lo)
    for _ in range(n):
        m = 0.5 * (lo + hi)
        if (f(m) < 0) == (flo < 0):
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


# --- the grid mg-5210 printed -------------------------------------------------

MUS = (1.2, 1.5, 1.8, 2.0, 2.2, 2.271, 2.5, 3.0)

# `sonin-trace.md` sec 2.2, the column this script is about.  Quoted so the
# comparison is against what was printed, not against a rerun of the code.
MG5210_COND = {1.2: 6.05e-6, 1.5: 2.99e-5, 1.8: 6.29e-5, 2.0: 8.75e-5,
               2.2: 1.13e-4, 2.271: 1.22e-4, 2.5: 1.53e-4, 3.0: 2.20e-4}


# --- checks -------------------------------------------------------------------

def check1(pr, eps):
    print("CHECK 1 -- the 8.7e-5 is eps'(1+) L^2 / (2 pi^2 N^2), and the second")
    print("condition row was evaluated at the wrong endpoint (fixed by mg-d03b;")
    print("the old row is reproduced inline below so the defect stays measurable).")
    print()
    print("  (a) the condition rows against direct integration on a fine grid.")
    L, N = np.log(5.0), 6
    y = np.linspace(-L / 2, L / 2, 400001)
    n = np.arange(N + 1)
    c = np.where(n == 0, L ** -0.5, ((-1.0) ** n) * np.sqrt(2.0 / L))
    B = c[:, None] * np.cos(2 * np.pi * n[:, None] * y[None, :] / L)
    dy = y[1] - y[0]
    worst = 0.0
    for j in (0, 1, 2, 3):
        direct = np.trapezoid(B * np.exp(j * y / 2)[None, :], dx=dy, axis=1)
        d = np.abs(cond_row(L, N, j) - direct).max()
        worst = max(worst, d)
        print("      j = %d   ghat(i j/2):  max |closed form - direct| = %.2e" % (j, d))
    VD.check(worst < 1e-6,
             "CHECK 1: this script's condition rows agree with direct integration")
    from verify_sonin_trace import conditions as cond_mg5210
    direct1 = np.trapezoid(B * np.exp(y / 2)[None, :], dx=dy, axis=1)
    a, q = 2 * np.pi * n / L, L / 2.0
    as_was = c * (np.exp(q) * (np.cos(a * q) / 2 + a * np.sin(a * q))
                  - np.exp(-q) * (np.cos(a * q) / 2 - a * np.sin(a * q))) \
        / (0.25 + a ** 2)
    bad = np.abs(as_was - direct1).max()
    now = np.abs(cond_mg5210(L, N)[1] - direct1).max()
    print("      row 1 as it stood before mg-d03b:  max deviation = %.3e" % bad)
    print("        (its n = 0 entry is c 4 sinh(L/2); ghat(i/2) is c 4 sinh(L/4))")
    print("      row 1 as `verify_sonin_trace.conditions()` now stands: %.2e" % now)
    VD.check(bad > 1.0,
             "CHECK 1: the pre-mg-d03b condition row 1 was NOT ghat(i/2) -- it is "
             "reproduced inline here so the defect stays measurable after the fix")
    VD.check(now < 1e-6,
             "CHECK 1: `verify_sonin_trace.conditions()` row 1 is now ghat(i/2) "
             "(regression test on the mg-d03b fix)")
    print()

    print("  (b) `sonin-trace.md` sec 2.2's conditioned column against the closed")
    print("      form.  The kink eps(1) = 0, eps'(1+) = 22.9965 gives eps_hat(t) ~")
    print("      -2 eps'(1+)/t^2; the truncation resolves up to t = 2 pi N / L.")
    print()
    print("  %7s %5s %16s %16s %16s %8s"
          % ("mu", "N", "as printed", "recomputed", "eps'L^2/2pi^2N^2", "ratio"))
    worst, cells = 0.0, 0
    for mu in MUS:
        L = np.log(mu)
        for N in ((40, 80, 160) if not QUICK else (80,)):
            cells += 1
            got = spectrum(eps, mu, N, 2)[0]
            pred = EPS_PRIME_1 * L ** 2 / (2 * np.pi ** 2 * N ** 2)
            worst = max(worst, abs(got / pred - 1.0))
            print("  %7.3f %5d %16s %16.6e %16.6e %8.4f"
                  % (mu, N, ("%.2e" % MG5210_COND[mu]) if N == 80 else "",
                     got, pred, got / pred))
    print()
    VD.check(worst < 0.01,
             "CHECK 1: every conditioned smallest eigenvalue is the closed form "
             "eps'(1+) L^2 / (2 pi^2 N^2) to within 1%")
    print("  %d cells, worst deviation %.2f%%.  At mu = 2, N = 80 the closed"
          % (cells, 100 * worst))
    print("  form is %.6e against the %.2e `sonin-trace.md` prints."
          % (EPS_PRIME_1 * np.log(2.0) ** 2 / (2 * np.pi ** 2 * 6400), MG5210_COND[2.0]))
    print("  The column is the truncation order read back out.  -E is compact --")
    print("  a continuous kernel on a bounded interval -- so its eigenvalues")
    print("  accumulate at 0 and the smallest one at finite N converges to 0, not")
    print("  to a margin.  There is nothing to be thin.")
    print()

    print("  (c) and the minimising direction is the last basis vector.")
    print("  %7s %5s %16s %28s" % ("mu", "N", "min eigenvalue", "top 3 |coefficients|"))
    for mu in (2.0,):
        L = np.log(mu)
        for N in ((40, 80, 160) if not QUICK else (40, 80)):
            A = -E_matrix(eps, L, N)
            rows = [cond_row(L, N, j) for j in range(2)]
            Q, _ = np.linalg.qr(np.asarray(rows).T)
            U, s, _ = np.linalg.svd(np.eye(N + 1) - Q @ Q.T)
            U = U[:, s > 1e-10]
            w, V = np.linalg.eigh(U.T @ A @ U)
            a = U @ V[:, 0]
            top = np.argsort(-np.abs(a))[:3]
            VD.check(top[0] == N,
                     "CHECK 1: the minimising direction at mu = 2 is the top cosine "
                     "mode n = N (N = %d)" % N)
            print("  %7.3f %5d %16.6e   %s"
                  % (mu, N, w[0], "  ".join("n=%d: %.3f" % (i, abs(a[i])) for i in top)))
    print()
    print("  It is the top resolved mode at every N, with weight 1.000.  A direction")
    print("  that moves when the basis moves is not a direction of the form.")
    print()


def check2(pr, eps, sym):
    print("CHECK 2 -- eps at large rho, and the symbol of -E.  The cheap instrument")
    print("first: this script's eps against mg-5210's, where mg-5210's is good.")
    print()
    rs = np.array([1.2, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0, 100.0])
    a, b = eps_exact(pr, rs), eps_mg5210(pr, rs)
    print("  %8s %16s %16s %10s" % ("rho", "this script", "mg-5210", "rel dev"))
    for r, x, y in zip(rs, a, b):
        print("  %8.1f %16.7e %16.7e %10.1e" % (r, x, y, abs(x - y) / abs(x)))
    ok = np.max(np.abs(a[:7] - b[:7]) / np.abs(a[:7])) < 1e-8
    VD.check(ok, "CHECK 2: the two eps agree to 1e-8 for rho <= 50")
    VD.check(abs(a[-1] - b[-1]) / abs(a[-1]) > 1.0,
             "CHECK 2: mg-5210's eps has failed by rho = 100 (its fixed 320-node "
             "rule stops resolving cos(2 pi rho x)); nothing in mg-5210 used rho > 3")
    print()
    print("  and the interpolation table against eps_exact at the same points:")
    dev = np.max(np.abs(eps(np.log(rs[:7])) - a[:7]) / np.abs(a[:7]))
    print("      max relative deviation %.2e" % dev)
    VD.check(dev < 2e-4, "CHECK 2: the tabulated eps agrees with eps_exact to 2e-4")
    print()

    print("  eps(rho) sqrt(rho) -> 1: the decay that makes eps_hat converge.")
    rr = np.exp(np.linspace(2.0, np.log(MU_MAX), 7))
    for r, v in zip(rr, eps_exact(pr, rr)):
        print("      rho %9.2f    eps sqrt(rho) = %.6f" % (r, v * np.sqrt(r)))
    v = eps_exact(pr, np.array([MU_MAX]))[0] * np.sqrt(MU_MAX)
    VD.check(abs(v - 1.0) < 0.02, "CHECK 2: eps(rho) sqrt(rho) -> 1 (ours, unanchored)")
    print()

    print("  the symbol eps_hat(t).  Two things are read off it, and they are the")
    print("  whole structure: eps_hat(0) > 0, so -E is NEGATIVE at low frequency and")
    print("  a long support must break the theorem; and eps_hat(t) -> -2 eps'(1+)/t^2")
    print("  < 0, so -E is positive at high frequency and its spectrum accumulates")
    print("  at 0 from above -- which is CHECK 1 seen from the other side.")
    print()
    e0 = sym(0.0)[0]
    print("      dropped tail |eps(e^Y) - e^{-Y/2}| = %.1e" % sym.dropped)
    print("      eps_hat(0) = 2 int_0^inf eps(e^y) dy = %+.6f" % e0)
    VD.check(e0 > 0, "CHECK 2: eps_hat(0) > 0 (eps > 0), so -E is negative at "
                     "low frequency and Theorem 1's conclusion must fail for "
                     "large enough support")
    t0 = bisect(lambda t: sym(t)[0], 0.5, 12.0)
    print("      first zero of eps_hat:  t_0 = %.7f" % t0)
    print()
    print("  %8s %16s %16s" % ("t", "eps_hat(t)", "eps_hat t^2 / 2"))
    for t in (1.0, 3.0, t0, 8.0, 20.0, 50.0, 100.0, 200.0):
        print("  %8.3f %16.6e %16.6f" % (t, sym(t)[0], sym(t)[0] * t * t / 2))
    # 4001 points, in both modes: the oscillation below has to be averaged over
    # whole periods and a coarse grid beats against it -- 121 points gives
    # -22.0, 4% out, purely from where the samples land.
    ts = np.linspace(100.0, 300.0, 4001)
    mean = float(np.mean(sym(ts) * ts * ts / 2))
    print()
    print("  eps_hat t^2 / 2 does not converge pointwise -- it oscillates about its")
    print("  limit with an amplitude of about 6, because eps has structure away from")
    print("  rho = 1 as well.  Its mean over t in [100, 300] is what to read:")
    print("      mean = %.4f   against -eps'(1+) = %.4f   (%.2f%%)"
          % (mean, -EPS_PRIME_1, 100 * abs(mean + EPS_PRIME_1) / EPS_PRIME_1))
    VD.check(abs(mean + EPS_PRIME_1) / EPS_PRIME_1 < 0.02,
             "CHECK 2: mean of eps_hat(t) t^2 / 2 over t in [100,300] is "
             "-eps'(1+) = -22.9965, the constant `weil-compo.tex:1367` prints")
    print()
    print("  A coincidence, checked because it is tempting.  theta'(t), the density")
    print("  of W_inf on the Fourier side (`verify_arch_positivity.py` CHECK 4),")
    print("  changes sign at t = 6.2898336, and eps_hat changes sign at %.7f." % t0)
    print("  They are NOT the same number: they differ by %.2e, and t_0 is stable"
          % (t0 - THETA_ZERO))
    print("  to 1e-4 across Y = 3.5..6, npan = 110..220, nmode = 8..12 and twice the")
    print("  eps quadrature.  Three digits of agreement is not an identity, and the")
    print("  identity is what a reader will assume unless told otherwise.")
    VD.check(abs(t0 - THETA_ZERO) > 1e-3,
             "CHECK 2: t_0 is NOT the zero of theta' -- the two agree to three "
             "digits and no further")
    print()
    return t0


def check3(pr, eps):
    print("CHECK 3 -- the inertia, which is what does not move with N.  Count of")
    print("NEGATIVE eigenvalues of -E and the most negative one, by codimension.")
    print("A negative eigenvalue of a truncation certifies one for the full form")
    print("(restriction raises the smallest eigenvalue), so the count can only be")
    print("an undercount -- and it does not move between N = 60 and N = 120.")
    print()
    mus = (2.0, 3.0, 6.0, 8.0, 20.0) if QUICK else (2.0, 2.5, 3.0, 4.0, 6.0, 8.0,
                                                    10.0, 14.0, 20.0, 30.0, 50.0)
    Ns = (60, 120) if not QUICK else (60,)
    print("  %7s %5s" % ("mu", "N") + "".join("%18s" % ("codim %d" % k)
                                              for k in range(5)))
    stable = True
    for mu in mus:
        prev = None
        for N in Ns:
            cells = []
            for k in range(5):
                w = spectrum(eps, mu, N, k)
                cells.append(((w < 0).sum(), w[0] if w[0] < 0 else 0.0))
            if prev is not None:
                stable &= all(c[0] == p[0] and abs(c[1] - p[1]) < 1e-3
                              for c, p in zip(cells, prev))
            prev = cells
            print("  %7.2f %5d" % (mu, N)
                  + "".join("%10d %7.4f" % c for c in cells))
        if mu == 2.0:
            n2 = [c[0] for c in prev]
            VD.check(n2[2] == 0,
                     "CHECK 3: at mu = 2 the codimension-two form has no negative "
                     "eigenvalue -- Theorem 1 reproduced")
            VD.check(n2[1] == 0,
                     "CHECK 3: at mu = 2 ONE condition (ghat(0) = 0) already leaves "
                     "no negative eigenvalue")
            VD.check(n2[0] > 0,
                     "CHECK 3: at mu = 2 the unconditioned form is indefinite "
                     "(mg-5210's sec 6, reproduced)")
        if mu == 8.0:
            VD.check([c[0] for c in prev][2] > 0,
                     "CHECK 3: at mu = 8 the codimension-two form HAS a negative "
                     "eigenvalue -- Theorem 1's conclusion is false there")
    print("   (each cell: how many negative eigenvalues, then the most negative)")
    print()
    if not QUICK:
        VD.check(stable, "CHECK 3: the inertia and the most negative eigenvalue "
                         "agree to 1e-3 between N = 60 and N = 120")
        print("  The counts agree exactly and the values to 1e-3 across N = 60 and 120:")
        print("  unlike CHECK 1's column, this is a statement about -E.")
        print()


def check4(pr, eps, t0):
    print("CHECK 4 -- mu_c(k), the largest support at which -E >= 0 survives k")
    print("conditions ghat(i j/2) = 0, j = 0..k-1.  k = 2 is Theorem 1's, whose")
    print("stated hypothesis is supp g in [2^-1/2, 2^1/2], i.e. mu <= 2.")
    print()
    Ns = (60,) if QUICK else (60, 120)
    ks = (1, 2, 3) if QUICK else (1, 2, 3, 4)
    print("  %3s %5s %12s %12s %12s %14s"
          % ("k", "N", "mu_c", "log mu_c", "mu_c/prev", "2 pi k / t_0"))
    prev, mcs, drift = None, {}, 0.0
    for k in ks:
        first = None
        for N in Ns:
            mc = bisect(lambda mu: spectrum(eps, mu, N, k)[0], 1.02, MU_MAX, 26)
            if first is None:
                first = mc
            else:
                drift = max(drift, abs(mc - first) / first)
            mcs[k] = mc          # the largest N is the best estimate, and the
            print("  %3d %5d %12.5f %12.5f %12s %14.5f"   # tightest upper bound
                  % (k, N, mc, np.log(mc),
                     "%.4f" % (mc / prev) if prev and N == Ns[-1] else "",
                     2 * np.pi * k / t0))
        prev = mcs[k]
    print()
    if len(Ns) > 1:
        print("  mu_c moves by at most %.2e relative between N = 60 and N = 120, and" % drift)
        print("  DOWNWARD in every row: truncation raises a form's eigenvalues, so each")
        print("  mu_c here is an upper bound falling towards the true one.  The drift is")
        print("  larger than the 1e-6 the inertia table shows because near mu_c the")
        print("  crossing eigenvalue is flat in mu -- a 1e-3 shift in it is a 3e-3 shift")
        print("  in mu_c.  Three figures of mu_c is what this supports, not six.")
        VD.check(drift < 1e-2,
                 "CHECK 4: mu_c(k) is stable to 1% between N = 60 and N = 120")
        print()
    VD.check(mcs[2] > 2.0,
             "CHECK 4: mu_c(2) > 2 ON THE EVEN BLOCK -- Theorem 1's conclusion "
             "survives past its stated hypothesis, so mu <= 2 is an artefact of "
             "the proof.  The full-space figure is mg-0b7a's 2.754, not 6.174; "
             "this half of the claim survives the correction, the factor does not")
    VD.check(mcs[1] > 2.0,
             "CHECK 4: mu_c(1) > 2 ON THE EVEN BLOCK -- the reading of this drawn "
             "here, that ghat(0) = 0 alone covers Theorem 1's range and the second "
             "condition buys nothing at mu <= 2, is REFUTED by mg-0b7a: on the full "
             "space mu_c(1) = 1.771 < 2 (odd g has ghat(0) = 0 for free).  The "
             "even-block inequality below is what this check asserts")
    VD.check(mcs[2] < MU_MAX,
             "CHECK 4: mu_c(2) is finite -- the conclusion does fail, it is not "
             "true for all mu")
    print("  Theorem 1 is stated for mu <= 2 and its conclusion holds, ON THE EVEN")
    print("  BLOCK, to mu = %.2f -- a factor %.2f in mu, %.2f in log mu."
          % (mcs[2], mcs[2] / 2.0, np.log(mcs[2]) / np.log(2.0)))
    print("  CORRECTED by mg-0b7a (`sonin-ceiling.md`, `verify_sonin_ceiling.py`")
    print("  CHECK 5): the cosine basis here spans the EVEN BLOCK ALONE and Theorem 1")
    print("  imposes no parity, so the admissible odd g are missing.  With them,")
    print("  mu_c(2) = 2.754 -- a factor 1.38, NOT %.2f.  The hypothesis is still not"
          % (mcs[2] / 2.0))
    print("  sharp and still not vacuous: the conclusion is FALSE at mu = %.2f and"
          % mcs[2])
    print("  above ON THIS BLOCK.  Both halves are FALSE for W_lambda -> -W_lambda.")
    print()
    print("  log mu_c against k: each condition buys a fixed FACTOR in the support,")
    print("  and that is the structural handle the work item asked for.  The reason")
    print("  is the symbol: eps_hat > 0 only on |t| < t_0 = %.4f, so -E is negative" % t0)
    print("  only on directions whose ghat lives in that band; k conditions of the")
    print("  form ghat(i j/2) = 0 hold ghat down near t = 0 to order k; and a support")
    print("  of length L resolves t to 2 pi / L, so the band admits about k L t_0/2 pi")
    print("  directions.  Equating gives log mu_c ~ 2 pi k / t_0 = %.4f k."
          % (2 * np.pi / t0))
    if len(ks) >= 3:
        sl = np.polyfit(list(ks), [np.log(mcs[k]) for k in ks], 1)[0]
        print("      least squares slope of log mu_c in k = %.5f" % sl)
        print("      heuristic 2 pi / t_0                  = %.5f" % (2 * np.pi / t0))
        print("      ratio                                 = %.4f" % (sl / (2 * np.pi / t0)))
        VD.check(0.5 < sl / (2 * np.pi / t0) < 1.5,
                 "CHECK 4: log mu_c(k) grows linearly in k at the rate 2 pi / t_0 "
                 "the symbol predicts, within a factor 1.5")
        print()
        print("  The SHAPE is right and the CONSTANT is 25% out, and that is what is")
        print("  claimed: the geometric growth is a measurement, the 2 pi / t_0 is a")
        print("  count of resolution cells and is not a derivation.  The conditions")
        print("  ghat(i j/2) = 0 sit at k distinct points of the imaginary axis and")
        print("  only approximate a k-fold zero at t = 0, which is where the 25% is.")
    print()
    return mcs


def house_rule(mcs):
    print("HOUSE RULE, statement by statement.")
    print()
    print("  FALSE for W_lambda -> -W_lambda (the trace is fixed, W_inf flips):")
    print("    * Theorem 1's conclusion W_inf(g*g^*) >= Tr(theta(g) S theta(g)^*)")
    print("      holds on the codimension-two subspace to mu = %.2f -- ON THE EVEN"
          % mcs[2])
    print("      BLOCK.  REFUTED as a full-space statement by mg-0b7a: it is")
    print("      mu = 2.754, a factor 1.38 on the stated mu <= 2, not 3.09.")
    print("                                                        CHECK 4")
    print("    * It is FALSE past that, at mu = 8 and above.       CHECKS 3, 4")
    print("    * At mu <= 2 one condition, ghat(0) = 0, already gives it; the second")
    print("      buys nothing there.  REFUTED by mg-0b7a: on the full space")
    print("      mu_c(1) = 1.771 < 2, since an odd g has ghat(0) = 0 for free, so")
    print("      one condition is no condition at all on half the space.")
    print("                                                        CHECKS 3, 4")
    print("    * Unconditioned, the inequality fails at every mu on the grid")
    print("      (mg-5210 sec 6, reproduced).                       CHECK 3")
    print()
    print("  SIGN-BLIND -- statements about eps and -E alone, which never mention")
    print("  W_lambda, so nothing in them changes under the substitution:")
    print("    * 8.7e-5 = eps'(1+) L^2 / (2 pi^2 N^2), and the whole of")
    print("      `sonin-trace.md` sec 2.2's conditioned column.     CHECK 1")
    print("    * `verify_sonin_trace.conditions()` row 1 is not ghat(i/2).  CHECK 1")
    print("    * the minimiser is the top resolved cosine mode.     CHECK 1")
    print("    * eps(rho) sqrt(rho) -> 1; eps_hat(0) = 5.37; eps_hat t^2/2 ->")
    print("      -eps'(1+); t_0.                                    CHECK 2")
    print("    * the inertia table, and its stability in N.         CHECK 3")
    print()
    print("  The two defects of CHECK 1 are sign-blind, and they are the reason the")
    print("  non-sign-blind statements above could be got wrong: a sign-blind")
    print("  measurement error propagates into a signed conclusion perfectly well.")
    print()


if __name__ == "__main__":
    np.set_printoptions(linewidth=120)
    print(__doc__.split("--- CONVENTIONS")[0])
    pr = ProlateExact()
    eps = EpsTable(pr, np.log(MU_MAX) + 0.05, 6000 if QUICK else 24000)
    sym = Symbol(pr, npan=60 if QUICK else 110)
    check1(pr, eps)
    t0 = check2(pr, eps, sym)
    check3(pr, eps)
    mcs = check4(pr, eps, t0)
    house_rule(mcs)
    VD.finish()
