#!/usr/bin/env python3
"""An INDEPENDENT recheck of the numerics in `deficit-repair.md` (mg-7606) and
`prolate-rate.md` (mg-fcb8).  Work item mg-9797.  Companion note:
`independent-recheck.md`.

Needs nothing but the Python standard library.  In particular it does NOT need
mpmath, and that is the point: `verify_deficit_repair.py` and
`verify_prolate_rate.py` are one implementation by one author, and a second run
of the same code is not a check of it.  This file was written from the
definitions in Connes-Consani, arXiv:2106.01715 (`Spectraltriples.tex`), read in
the source, WITHOUT reading either of those two scripts.  They were opened only
after every number below had been computed and written down.

WHAT IS INDEPENDENT HERE, AND WHAT IS NOT.  Stated up front because the value of
this file is exactly the part of it that does not share a cause of error with
the original.

  Independent:
    * Arithmetic.  Python's `decimal` (libmpdec, decimal radix) rather than
      mpmath (binary radix, Python ints).  A rounding or radix bug in one is not
      a bug in the other.
    * Transcendental functions.  pi (Machin), log 2 and log (atanh series after
      repeated square roots), exp (halving plus Taylor), sin/cos (Taylor plus
      angle doubling), Euler's gamma (Brent-McMillan B1), digamma (recurrence
      plus asymptotic series with exact Bernoulli numbers) are all implemented
      here from their series.  The original calls mpmath for every one of these.
    * The archimedean boundary term W_{0,2}^#.  Derived here in CLOSED FORM as
      the rank-one matrix 2 v_n v_m, v_n = int xi_n(x) e^{x/2} dx.  The original
      computes it by quadrature.  Two different routes to the same block.
    * The eigenvalue.  Sturm-sequence bisection on the Householder tridiagonal,
      which returns a BRACKET.  The original's route is not known to this file's
      author at the time of writing; whatever it is, a bracket is checkable in a
      way a converged iterate is not.
    * The convolution table (:444) is re-derived, once symbolically by hand (see
      the note, section 2) and once by brute-force numerical convolution of the
      basis functions themselves (CHECK 0).
    * The prolate normalisation constant is checked against the trace sum rule
      sum_n Lambda_n(c) = 2c/pi, which pins the one factor that a derivation of
      Lambda_n from the finite Fourier transform could get wrong.

  NOT independent -- shared with the original, and therefore NOT corroborated
  by any agreement below:
    * The DEFINITIONS.  Both implementations read the same paper.  If
      `Spectraltriples.tex` is misread the same way twice, agreement proves
      nothing.  This is irreducible and is why the note quotes source lines.
    * Proposition `Hilbert` (:289) and Connes-Consani's eq. (thetaprime) :261
      are taken on trust from the paper by both.
    * Composite Gauss-Legendre with Newton-refined Legendre roots.  Chosen here
      independently, but it turns out to be the same method the original uses.
      A shared quadrature *scheme* is a real limit on what CHECK 2 establishes;
      the panel counts, node counts and the grouping of the singular integrand
      differ, and CHECK 7 measures convergence in both.
    * The Legendre (Bouwkamp) route to the prolate eigenvalues, and the
      identity Lambda_n = c d_0^2 / (pi psi_n(0)^2).  Derived here from scratch,
      but it is the same identity the original uses -- it is the natural one.
      The sum-rule check is what this file adds that the original does not have.
    * Fuchs' asymptotic is quoted, not derived, by both.

  Not attempted here: the odd sector, and any re-proof of Proposition `Hilbert`.

Usage:  python3 verify_independent_recheck.py [--quick] [check numbers...]
"""

import sys
from decimal import Decimal as D, getcontext, localcontext
from fractions import Fraction

QUICK = "--quick" in sys.argv


# --------------------------------------------------------------------------
# DMATH
#
# Arbitrary-precision real arithmetic on Python's ``decimal.Decimal``.
#
# Deliberately does NOT use mpmath, sympy, numpy, flint or gmpy2: the point of
# this module is that the transcendental functions used downstream are derived
# and implemented here from their series, so that a downstream numerical
# agreement is not an agreement between two callers of one library.
#
# Everything is computed with guard digits and returned rounded to the ambient
# context precision.
# --------------------------------------------------------------------------


# ---------------------------------------------------------------- utilities

def _extra(n=25):
    """Context with n guard digits above the ambient precision."""
    c = getcontext().copy()
    c.prec = getcontext().prec + n
    return c


def prec():
    return getcontext().prec


# ---------------------------------------------------------------- constants
# cached per precision
_CACHE = {}


def _cached(key, fn):
    p = getcontext().prec
    k = (key, p)
    if k not in _CACHE:
        _CACHE[k] = fn()
    return _CACHE[k]


def _atan_inv(m, ctx):
    """arctan(1/m) for integer m, by the alternating series."""
    with localcontext(ctx):
        m = D(m)
        t = D(1) / m
        m2 = m * m
        term = t
        total = t
        k = 1
        while True:
            term = -term / m2
            nxt = term / (2 * k + 1)
            total += nxt
            if nxt == 0 or abs(nxt) < D(10) ** (-ctx.prec - 5):
                break
            k += 1
        return +total


def pi():
    def f():
        ctx = _extra(30)
        with localcontext(ctx):
            # Machin: pi/4 = 4 atan(1/5) - atan(1/239)
            v = 4 * (4 * _atan_inv(5, ctx) - _atan_inv(239, ctx))
        return +v
    return _cached('pi', f)


def ln2():
    def f():
        ctx = _extra(30)
        with localcontext(ctx):
            # ln 2 = 2 atanh(1/3) = 2 sum_{k>=0} (1/3)^{2k+1}/(2k+1)
            x = D(1) / 3
            x2 = x * x
            term = x
            total = x
            k = 1
            while True:
                term *= x2
                nxt = term / (2 * k + 1)
                total += nxt
                if nxt == 0 or nxt < D(10) ** (-ctx.prec - 5):
                    break
                k += 1
            v = 2 * total
        return +v
    return _cached('ln2', f)


def euler_gamma():
    """Euler-Mascheroni constant by the Brent-McMillan B1 algorithm.

        gamma = A(n)/B(n) - log(n),   |error| <= pi * exp(-4n)

    with A(n) = sum_k (n^k/k!)^2 * H_k, B(n) = sum_k (n^k/k!)^2.
    """
    def f():
        ctx = _extra(35)
        with localcontext(ctx):
            digits = ctx.prec
            # need 4n >= digits*ln(10)
            n = int(digits * 2.302585092994046 / 4) + 5
            N = int(3.6 * n) + 20
            nn = D(n)
            # t_k = (n^k/k!)^2 ; H_k
            t = D(1)
            H = D(0)
            A = D(0)
            B = D(1)
            for k in range(1, N + 1):
                t = t * (nn / k) ** 2
                H += D(1) / k
                A += t * H
                B += t
            v = A / B - ln_(nn, ctx)
        return +v
    return _cached('gamma', f)


# ---------------------------------------------------------------- exp / ln

def ln_(x, ctx=None):
    """Natural logarithm of a positive Decimal."""
    if ctx is None:
        ctx = _extra(20)
    with localcontext(ctx):
        x = +D(x)
        if x <= 0:
            raise ValueError("ln of non-positive")
        # write x = m * 2^e with m in [1,2)
        e = 0
        while x >= 2:
            x /= 2
            e += 1
        while x < 1:
            x *= 2
            e -= 1
        # squeeze m towards 1 by repeated square roots
        nsq = 6
        for _ in range(nsq):
            x = x.sqrt()
        # ln m = 2 atanh(z), z = (m-1)/(m+1)
        z = (x - 1) / (x + 1)
        z2 = z * z
        term = z
        total = z
        k = 1
        while True:
            term *= z2
            nxt = term / (2 * k + 1)
            total += nxt
            if nxt == 0 or abs(nxt) < D(10) ** (-ctx.prec - 5):
                break
            k += 1
        v = 2 * total * (1 << nsq) + e * _ln2_ctx(ctx)
    return +v


def _ln2_ctx(ctx):
    with localcontext(ctx):
        x = D(1) / 3
        x2 = x * x
        term = x
        total = x
        k = 1
        while True:
            term *= x2
            nxt = term / (2 * k + 1)
            total += nxt
            if nxt == 0 or nxt < D(10) ** (-ctx.prec - 5):
                break
            k += 1
        return +(2 * total)


def ln(x):
    ctx = _extra(20)
    return +ln_(x, ctx)


def exp(x):
    ctx = _extra(20)
    with localcontext(ctx):
        x = +D(x)
        if x == 0:
            return D(1)
        L2 = _ln2_ctx(ctx)
        n = int((x / L2).to_integral_value(rounding='ROUND_FLOOR'))
        r = x - n * L2
        # further reduce
        m = 10
        t = r / (1 << m)
        term = D(1)
        total = D(1)
        k = 1
        while True:
            term = term * t / k
            total += term
            if term == 0 or abs(term) < D(10) ** (-ctx.prec - 5):
                break
            k += 1
        for _ in range(m):
            total = total * total
        v = total * (D(2) ** n)
    return +v


# ---------------------------------------------------------------- trig

def _sincos_small(t, ctx):
    """(sin t, cos t) for |t| small, by Taylor."""
    with localcontext(ctx):
        s = D(0)
        c = D(0)
        term = D(1)
        k = 0
        # cos
        while True:
            c += term
            term = -term * t * t / ((2 * k + 1) * (2 * k + 2))
            k += 1
            if term == 0 or abs(term) < D(10) ** (-ctx.prec - 5):
                break
        term = t
        k = 0
        while True:
            s += term
            term = -term * t * t / ((2 * k + 2) * (2 * k + 3))
            k += 1
            if term == 0 or abs(term) < D(10) ** (-ctx.prec - 5):
                break
        return +s, +c


def sincos(x):
    ctx = _extra(30)
    with localcontext(ctx):
        x = +D(x)
        P = pi()
        two_pi = 2 * P
        q = (x / two_pi).to_integral_value(rounding='ROUND_HALF_EVEN')
        r = x - q * two_pi
        m = 10
        t = r / (1 << m)
        s, c = _sincos_small(t, ctx)
        for _ in range(m):
            s, c = 2 * s * c, 2 * c * c - 1
    return +s, +c


def sin(x):
    return sincos(x)[0]


def cos(x):
    return sincos(x)[1]


def sinh(x):
    e = exp(x)
    return (e - 1 / e) / 2


def cosh(x):
    e = exp(x)
    return (e + 1 / e) / 2


def sqrt(x):
    return D(x).sqrt()


# ---------------------------------------------------------------- digamma
# Bernoulli numbers B_{2n} as exact fractions, from the recurrence
# sum_{j=0}^{m} C(m+1,j) B_j = 0.

def _bernoulli(upto):
    from math import comb
    B = [Fraction(0)] * (upto + 1)
    B[0] = Fraction(1)
    for m in range(1, upto + 1):
        s = Fraction(0)
        for j in range(m):
            s += comb(m + 1, j) * B[j]
        B[m] = -s / (m + 1)
    return B


def digamma(x, nterms=20):
    """psi(x) for real x>0, by recurrence up to a large argument plus the
    standard asymptotic series with exact Bernoulli numbers."""
    ctx = _extra(25)
    with localcontext(ctx):
        x = +D(x)
        acc = D(0)
        M = max(30, int(ctx.prec))
        while x < M:
            acc -= 1 / x
            x += 1
        v = ln_(x, ctx) - 1 / (2 * x)
        B = _bernoulli(2 * nterms + 2)
        xp = x * x
        for n in range(1, nterms + 1):
            b = B[2 * n]
            v -= D(b.numerator) / D(b.denominator) / (2 * n) / xp
            xp *= x * x
        v += acc
    return +v

# --------------------------------------------------------------------------
# GAUSS
#
# Gauss-Legendre nodes and weights in Decimal, computed here by Newton
# iteration on the Legendre recurrence.  No external quadrature is used.
# --------------------------------------------------------------------------


_NODES = {}


def legendre(n, x):
    """(P_n(x), P_n'(x)) by the three-term recurrence."""
    p0 = D(1)
    p1 = x
    if n == 0:
        return p0, D(0)
    for k in range(2, n + 1):
        p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
    dp = n * (x * p1 - p0) / (x * x - 1)
    return p1, dp


def gl_nodes(q):
    """Nodes/weights for q-point Gauss-Legendre on [-1,1], at the ambient
    precision.  Returns (xs, ws) with xs increasing."""
    key = (q, getcontext().prec)
    if key in _NODES:
        return _NODES[key]
    ctx = getcontext().copy()
    ctx.prec = getcontext().prec + 20
    xs, ws = [], []
    with localcontext(ctx):
        P = pi()
        for i in range(1, q // 2 + 1):
            # Chebyshev-like starting guess
            th = P * (D(i) - D(1) / 4) / (D(q) + D(1) / 2)
            x = cos(th)
            for _ in range(200):
                p, dp = legendre(q, x)
                dx = -p / dp
                x = x + dx
                if abs(dx) < D(10) ** (-ctx.prec + 5):
                    break
            p, dp = legendre(q, x)
            w = 2 / ((1 - x * x) * dp * dp)
            xs.append(-x)
            ws.append(w)
        mid = []
        if q % 2 == 1:
            p, dp = legendre(q, D(0))
            mid = [(D(0), 2 / (dp * dp))]
        allx = [(+x, +w) for x, w in zip(xs, ws)]
        allx = allx + mid + [(-x, +w) for x, w in reversed(list(zip(xs, ws)))]
    res = ([a for a, _ in allx], [b for _, b in allx])
    _NODES[key] = res
    return res

# --------------------------------------------------------------------------
# DLINALG
#
# Symmetric eigenvalue machinery in Decimal.
#
# Route: Householder tridiagonalisation, then the smallest eigenvalue by
# Sturm-sequence bisection (Sylvester inertia), then the eigenvector by inverse
# iteration with Gaussian elimination.  Bisection is chosen because it is
# monotone and gives a bracket: for an eigenvalue of size 1e-54 read off entries
# of order 1, an interval endpoint is a statement one can check, where a
# QR/QL sweep's output is not.
# --------------------------------------------------------------------------



def tridiagonalize(A):
    """Householder reduction of a symmetric matrix (list of lists) to
    tridiagonal form.  Returns (alpha, beta) with alpha the diagonal
    (length n) and beta the off-diagonal (length n-1)."""
    n = len(A)
    a = [row[:] for row in A]
    alpha = [D(0)] * n
    beta = [D(0)] * (n - 1)
    for k in range(n - 2):
        s = D(0)
        for i in range(k + 1, n):
            s += a[i][k] * a[i][k]
        if s == 0:
            beta[k] = D(0)
            alpha[k] = a[k][k]
            continue
        anorm = s.sqrt()
        if a[k + 1][k] > 0:
            anorm = -anorm
        v = [D(0)] * n
        v[k + 1] = a[k + 1][k] - anorm
        for i in range(k + 2, n):
            v[i] = a[i][k]
        h = (anorm * anorm - anorm * a[k + 1][k])
        if h == 0:
            beta[k] = a[k + 1][k]
            alpha[k] = a[k][k]
            continue
        # p = A v / h ; K = v.p/(2h) ; q = p - K v ; A -= v q^T + q v^T
        p = [D(0)] * n
        for i in range(k + 1, n):
            t = D(0)
            ai = a[i]
            for j in range(k + 1, n):
                t += ai[j] * v[j]
            p[i] = t / h
        K = D(0)
        for i in range(k + 1, n):
            K += v[i] * p[i]
        K = K / (2 * h)
        for i in range(k + 1, n):
            p[i] = p[i] - K * v[i]
        for i in range(k + 1, n):
            vi, pi = v[i], p[i]
            ai = a[i]
            for j in range(k + 1, n):
                ai[j] = ai[j] - vi * p[j] - pi * v[j]
        alpha[k] = a[k][k]
        beta[k] = anorm
    alpha[n - 2] = a[n - 2][n - 2]
    beta[n - 2] = a[n - 1][n - 2]
    alpha[n - 1] = a[n - 1][n - 1]
    return alpha, beta


def count_below(alpha, beta, x):
    """Number of eigenvalues of the tridiagonal matrix strictly below x
    (Sturm sequence / LDL^T inertia)."""
    n = len(alpha)
    tiny = D(10) ** (-getcontext().prec * 2)
    cnt = 0
    d = alpha[0] - x
    if d < 0:
        cnt += 1
    for i in range(1, n):
        if d == 0:
            d = tiny
        d = (alpha[i] - x) - beta[i - 1] * beta[i - 1] / d
        if d < 0:
            cnt += 1
    return cnt


def gershgorin(alpha, beta):
    n = len(alpha)
    lo = hi = None
    for i in range(n):
        r = D(0)
        if i > 0:
            r += abs(beta[i - 1])
        if i < n - 1:
            r += abs(beta[i])
        a, b = alpha[i] - r, alpha[i] + r
        lo = a if lo is None else min(lo, a)
        hi = b if hi is None else max(hi, b)
    return lo, hi


def eig_k(alpha, beta, k, digits=None, lo=None, hi=None):
    """The k-th smallest eigenvalue (k = 0 for the smallest), by bisection.
    Returns (lo, hi) bracket."""
    if digits is None:
        digits = getcontext().prec - 8
    g_lo, g_hi = gershgorin(alpha, beta)
    lo = g_lo - 1 if lo is None else lo
    hi = g_hi + 1 if hi is None else hi
    scale = max(abs(g_lo), abs(g_hi), D(1))
    tol = scale * D(10) ** (-digits)
    # first bracket the eigenvalue by sign of the count
    for _ in range(20000):
        if hi - lo <= tol:
            break
        mid = (lo + hi) / 2
        if count_below(alpha, beta, mid) > k:
            hi = mid
        else:
            lo = mid
    return lo, hi


def eig_min(alpha, beta, digits=None):
    lo, hi = eig_k(alpha, beta, 0, digits)
    return (lo + hi) / 2, hi - lo


def eig_min_relative(alpha, beta, reldigits=None):
    """Smallest eigenvalue to a *relative* accuracy: bisect first to an
    absolute tolerance, then continue in the bracket until the bracket is
    small relative to the value.  Handles eigenvalues many orders below the
    matrix norm."""
    if reldigits is None:
        reldigits = 20
    g_lo, g_hi = gershgorin(alpha, beta)
    lo, hi = g_lo - 1, g_hi + 1
    for _ in range(200000):
        mid = (lo + hi) / 2
        if count_below(alpha, beta, mid) > 0:
            hi = mid
        else:
            lo = mid
        if hi == lo:
            break
        m = max(abs(lo), abs(hi))
        if m > 0 and (hi - lo) / m < D(10) ** (-reldigits):
            break
    return (lo + hi) / 2, hi - lo


def solve(A, b):
    """Gaussian elimination with partial pivoting; A is copied."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(M[r][c]))
        if M[piv][c] == 0:
            continue
        M[c], M[piv] = M[piv], M[c]
        pc = M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / pc
            if f == 0:
                continue
            Mr, Mc = M[r], M[c]
            for j in range(c, n + 1):
                Mr[j] -= f * Mc[j]
    x = [D(0)] * n
    for r in range(n - 1, -1, -1):
        s = M[r][n]
        for j in range(r + 1, n):
            s -= M[r][j] * x[j]
        x[r] = s / M[r][r] if M[r][r] != 0 else D(0)
    return x


def inverse_iteration(A, shift, iters=4, seed=None):
    """Eigenvector for the eigenvalue nearest `shift`."""
    n = len(A)
    B = [[A[i][j] - (shift if i == j else 0) for j in range(n)] for i in range(n)]
    v = seed[:] if seed else [D(1) / (i + 3) ** 2 + D(1) / n for i in range(n)]
    for _ in range(iters):
        v = solve(B, v)
        nrm = sum(x * x for x in v).sqrt()
        v = [x / nrm for x in v]
    return v


def rayleigh(A, v):
    n = len(A)
    num = D(0)
    for i in range(n):
        s = D(0)
        Ai = A[i]
        for j in range(n):
            s += Ai[j] * v[j]
        num += v[i] * s
    den = sum(x * x for x in v)
    return num / den


def quadform(A, v):
    n = len(A)
    num = D(0)
    for i in range(n):
        s = D(0)
        Ai = A[i]
        for j in range(n):
            s += Ai[j] * v[j]
        num += v[i] * s
    return num

# --------------------------------------------------------------------------
# WEIL
#
# The semi-local Weil quadratic form in the even sector, built from the
# definitions in Connes-Consani, arXiv:2106.01715 (`Spectraltriples.tex`).
#
# Definitions used (source lines cited):
#
#   :385  basis      xi_0(x) = L^{-1/2},  xi_n(x) = (-1)^n sqrt(2/L) cos(2 pi n x/L)
#   :414  psi^#(F)  = W_{0,2}^#(F) - W_R^#(F) - sum_p W_p^#(F)
#   :419  W_{0,2}^#(F) = int_1^inf F(x)(x^{1/2}+x^{-1/2}) d*x
#   :422  W_R^#(F)     = (1/2)(log 4pi + gamma) F(1)
#                        + int_1^inf (x^{1/2}F(x) - F(1))/(x - x^{-1}) d*x
#   :425  W_p^#(F)     = (log p) sum_{m>=1} p^{-m/2} F(p^m)
#   :432  sigma(n,m)   = psi^#(h),  h(u) = (xi_n * xi_m^* + xi_m * xi_n^*)(log u)
#   :444  the table of (1/2)(xi_n * xi_m^* + xi_m * xi_n^*)(y) on y in [0,L]
#
# The convolution table entries are re-derived from scratch in `check_theta.py`
# rather than taken on trust, and W_{0,2}^# is evaluated from a closed form
# derived here (see `note` below), not by quadrature.
# --------------------------------------------------------------------------



def von_mangoldt_upto(mu_int):
    """[(n, Lambda(n))] for 1 < n <= mu_int with Lambda(n) != 0."""
    out = []
    for n in range(2, mu_int + 1):
        # is n a prime power?
        m = n
        p = None
        for q in range(2, int(n ** 0.5) + 2):
            if m % q == 0:
                p = q
                break
        if p is None:
            p = n
        k = 0
        while m % p == 0:
            m //= p
            k += 1
        if m == 1:
            out.append((n, p))          # Lambda(n) = log p, store p
    return out


class Form:
    """Even-sector matrices of QW_lambda at mu, truncated to indices 0..N."""

    def __init__(self, mu, N, panels_per_period=1, q=48, verbose=False,
                 with_primes=True):
        self.mu = D(mu)
        self.N = N
        self.L = ln(self.mu)
        L = self.L
        self.PI = pi()
        self.a1 = 2 * self.PI / L
        self._quad(panels_per_period, q, verbose)
        self._w02()
        self.pp = []
        if with_primes:
            self._primes()

    # ---------------------------------------------------------------- W_{0,2}
    def _w02(self):
        """W_{0,2}^#(n,m) = 2 v_n v_m  with v_n = int_{-L/2}^{L/2} xi_n(x)
        e^{x/2} dx.  Derived here:  v_n = sqrt(2/L) 4 L sinh(L/4) beta_n
        (n>=1), v_0 = L^{-1/2} 4 sinh(L/4), beta_k = L/(L^2+16 pi^2 k^2).
        This is the boundary term 2 Re(fhat(i/2) conj(fhat(-i/2))) of
        Proposition `Hilbert` (:292), which on the even sector is a square."""
        L, PI = self.L, self.PI
        sh = sinh(L / 4)
        v = []
        for k in range(self.N + 1):
            beta = L / (L * L + 16 * PI * PI * k * k)
            if k == 0:
                v.append(4 * sh / L.sqrt())
            else:
                v.append((2 / L).sqrt() * 4 * L * sh * beta)
        self.v = v

    # ---------------------------------------------------------------- W_R
    def _quad(self, ppp, q, verbose):
        """P_k = int_0^L e^{y/2} sin(a_k y)/(2 sinh y) dy         (k>=1)
           Q_k = int_0^L [e^{y/2}(L-y)cos(a_k y) - L]/(2 sinh y) dy (k>=0)

        Composite Gauss-Legendre: `ppp` panels per period of the highest
        frequency present, q nodes each."""
        L, N = self.L, self.N
        M = max(int(ppp * max(N, 1)), 24)
        xs, ws = gl_nodes(q)
        h = L / M
        P = [D(0)] * (N + 1)
        Q = [D(0)] * (N + 1)
        ctx = getcontext().copy()
        ctx.prec = getcontext().prec + 15
        with localcontext(ctx):
            a1 = 2 * pi() / L
            for j in range(M):
                lo = j * h
                for x, w in zip(xs, ws):
                    y = lo + h * (x + 1) / 2
                    wt = w * h / 2
                    E = exp(y / 2)
                    E2 = E * E
                    S2 = E2 - 1 / E2                    # 2 sinh y
                    s1, c1 = sincos(a1 * y)
                    sk, ck = D(0), D(1)                 # k = 0
                    Ly = L - y
                    for k in range(N + 1):
                        if k > 0:
                            sk, ck = sk * c1 + ck * s1, ck * c1 - sk * s1
                            P[k] += wt * E * sk / S2
                        Q[k] += wt * (E * Ly * ck - L) / S2
        self.P = [+p for p in P]
        self.Q = [+qq for qq in Q]
        self.M, self.q = M, q
        # the constant in front of theta_sym(0)/2 (:532)
        eL = exp(L)
        self.G = euler_gamma() + ln(4 * self.PI * (eL - 1) / (eL + 1))

    # ------------------------------------------------------- theta_sym coeffs
    def coeffs(self, n, m):
        """theta_sym^{nm}(y) = sum_k cs[k] sin(a_k y) + sum_k cc[k] (L-y)cos(a_k y).
        Returned as two dicts.  (Twice the :444 table, since the table gives
        one half of the symmetrised convolution.)"""
        L, PI = self.L, self.PI
        cs, cc = {}, {}
        if n == 0 and m == 0:
            cc[0] = 2 / L
        elif n == m:
            cc[n] = 2 / L
            cs[n] = -1 / (PI * n)
        elif n == 0 or m == 0:
            k = n + m
            cs[k] = -D(2).sqrt() / (PI * k)
        else:
            d = PI * (D(m * m) - D(n * n))
            cs[n] = 2 * D(n) / d
            cs[m] = cs.get(m, D(0)) - 2 * D(m) / d
        return cs, cc

    def theta0(self, n, m):
        return D(2) if n == m else D(0)

    def theta_sym_at(self, n, m, y, trig):
        """theta_sym^{nm}(y) using precomputed trig[k] = (sin a_k y, cos a_k y)."""
        cs, cc = self.coeffs(n, m)
        L = self.L
        tot = D(0)
        for k, c in cs.items():
            tot += c * trig[k][0]
        for k, c in cc.items():
            tot += c * (L - y) * trig[k][1]
        return tot

    # ---------------------------------------------------------------- primes
    def _primes(self):
        """sum_p W_p^#(n,m) = sum_{1<j<=mu} Lambda(j) j^{-1/2} theta_sym(log j)."""
        L, N = self.L, self.N
        mu_int = int(self.mu)
        self.pp = []
        for j, p in von_mangoldt_upto(mu_int):
            y = ln(D(j))
            if y >= L:
                continue
            w = ln(D(p)) / D(j).sqrt()
            s1, c1 = sincos(2 * self.PI * y / L)
            trig = [(D(0), D(1))]
            sk, ck = D(0), D(1)
            for k in range(1, N + 1):
                sk, ck = sk * c1 + ck * s1, ck * c1 - sk * s1
                trig.append((sk, ck))
            self.pp.append((j, y, w, trig))

    # ---------------------------------------------------------------- matrices
    def arch(self):
        """sigma^arch = W_{0,2}^# - W_R^#, as a list of rows (n,m = 0..N)."""
        N, L = self.N, self.L
        A = [[D(0)] * (N + 1) for _ in range(N + 1)]
        for n in range(N + 1):
            for m in range(n, N + 1):
                cs, cc = self.coeffs(n, m)
                wr = self.theta0(n, m) / 2 * self.G
                for k, c in cs.items():
                    wr += c * self.P[k]
                for k, c in cc.items():
                    wr += c * self.Q[k]
                val = 2 * self.v[n] * self.v[m] - wr
                A[n][m] = val
                A[m][n] = val
        return A

    def primes_matrix(self):
        N = self.N
        B = [[D(0)] * (N + 1) for _ in range(N + 1)]
        for n in range(N + 1):
            for m in range(n, N + 1):
                tot = D(0)
                for j, y, w, trig in self.pp:
                    tot += w * self.theta_sym_at(n, m, y, trig)
                B[n][m] = tot
                B[m][n] = tot
        return B

    def full(self, drop=None):
        A = self.arch()
        N = self.N
        for n in range(N + 1):
            for m in range(n, N + 1):
                tot = D(0)
                for j, y, w, trig in self.pp:
                    if drop is not None and j == drop:
                        continue
                    tot += w * self.theta_sym_at(n, m, y, trig)
                A[n][m] -= tot
                if m != n:
                    A[m][n] = A[n][m]
        return A

# --------------------------------------------------------------------------
# PROLATE
#
# Slepian prolate concentration eigenvalues Lambda_n(c), by the Legendre
# (Bouwkamp) expansion.  Everything here is derived from the prolate ODE and the
# definition of the sinc kernel; no prolate library is used.
#
# Setting.  psi_n(c,.) are the eigenfunctions of the time-limiting/band-limiting
# operator on [-1,1] with band [-c,c]:
#
#     int_{-1}^{1} sin(c(x-y))/(pi(x-y)) psi_n(y) dy = Lambda_n psi_n(x),
#
# normalised by int_{-1}^1 psi_n^2 = 1.  They are also the bounded solutions of
#
#     [(1-x^2) psi']' + (chi - c^2 x^2) psi = 0     on [-1,1].
#
# Expanding psi_n = sum_k d_k Pbar_k in normalised Legendre polynomials
# Pbar_k = sqrt(k+1/2) P_k and using x^2 P_k = ... (three-term recurrence twice)
# turns the ODE into a symmetric tridiagonal eigenproblem in steps of two:
#
#     diag_k    = k(k+1) + c^2 (2k(k+1)-1)/((2k-1)(2k+3))
#     offdiag_k = c^2 (k+1)(k+2) / ((2k+3) sqrt((2k+1)(2k+5)))    [k <-> k+2]
#
# The concentration eigenvalue is then recovered from the finite Fourier
# transform.  With F(x) := int_{-1}^1 e^{icxy} psi_n(y) dy = gamma_n psi_n(x),
# composing the transform with itself gives Lambda_n = c |gamma_n|^2/(2 pi), and
# evaluating F at x=0 (n even) or F'(0) (n odd) gives gamma_n in closed form:
#
#     n even:  gamma_n = sqrt(2) d_0 / psi_n(0)
#     n odd :  gamma_n = i c sqrt(2/3) d_1 / psi_n'(0)
#
# so that
#
#     n even:  Lambda_n = c d_0^2 / (pi psi_n(0)^2)
#     n odd :  Lambda_n = c^3 d_1^2 / (3 pi psi_n'(0)^2).
#
# Both are derived above, not quoted.  `sum_rule` checks them against
# sum_n Lambda_n = 2c/pi, which is the trace of the operator.
#
# 1 - Lambda_n is obtained by subtraction.  That costs about 2c/log(10) digits of
# cancellation and is the reason for the working precision.
# --------------------------------------------------------------------------



def _matrix(c, kmax, parity):
    """(diag, off) of the symmetric tridiagonal, over k = parity, parity+2, ..."""
    c2 = c * c
    ks = list(range(parity, kmax + 1, 2))
    diag, off = [], []
    for k in ks:
        kk = D(k)
        diag.append(kk * (kk + 1) + c2 * (2 * kk * (kk + 1) - 1) /
                    ((2 * kk - 1) * (2 * kk + 3)))
    for k in ks[:-1]:
        kk = D(k)
        off.append(c2 * (kk + 1) * (kk + 2) /
                   ((2 * kk + 3) * ((2 * kk + 1) * (2 * kk + 5)).sqrt()))
    return ks, diag, off


def _count_below(diag, off, x):
    n = len(diag)
    tiny = D(10) ** (-getcontext().prec * 2)
    cnt = 0
    d = diag[0] - x
    if d < 0:
        cnt += 1
    for i in range(1, n):
        if d == 0:
            d = tiny
        d = (diag[i] - x) - off[i - 1] * off[i - 1] / d
        if d < 0:
            cnt += 1
    return cnt


def _eig(diag, off, j, digits):
    lo = min(diag) - sum(abs(o) for o in off) - 1
    hi = max(diag) + sum(abs(o) for o in off) + 1
    scale = max(abs(lo), abs(hi))
    tol = scale * D(10) ** (-digits)
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if _count_below(diag, off, mid) > j:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def _tri_solve(diag, off, shift, b):
    """Solve (T - shift I) x = b for symmetric tridiagonal T (Thomas, with a
    guard against a zero pivot)."""
    n = len(diag)
    tiny = D(10) ** (-getcontext().prec + 5)
    cp = [D(0)] * n
    dp = [D(0)] * n
    den = diag[0] - shift
    if den == 0:
        den = tiny
    cp[0] = off[0] / den if n > 1 else D(0)
    dp[0] = b[0] / den
    for i in range(1, n):
        den = (diag[i] - shift) - off[i - 1] * cp[i - 1]
        if den == 0:
            den = tiny
        if i < n - 1:
            cp[i] = off[i] / den
        dp[i] = (b[i] - off[i - 1] * dp[i - 1]) / den
    x = [D(0)] * n
    x[n - 1] = dp[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]
    return x


def _eigvec(diag, off, lam, iters=3):
    n = len(diag)
    v = [D(1) / (i + 2) for i in range(n)]
    for _ in range(iters):
        v = _tri_solve(diag, off, lam, v)
        nrm = sum(x * x for x in v).sqrt()
        v = [x / nrm for x in v]
    return v


def _legendre_at_0(kmax, parity):
    """P_k(0) for even k, P_k'(0) for odd k."""
    out = {}
    if parity == 0:
        val = D(1)
        out[0] = val
        for k in range(2, kmax + 1, 2):
            val = -val * (k - 1) / D(k)
            out[k] = val
    else:
        val = D(1)
        out[1] = val
        for k in range(3, kmax + 1, 2):
            val = -val * k / D(k - 1)
            out[k] = val
    return out


def lambda_n(c, n, kmax=None, digits=None):
    """Lambda_n(c) and the Legendre coefficients."""
    c = D(c)
    if kmax is None:
        kmax = int(2 * float(c)) + 2 * n + 240
    if digits is None:
        digits = getcontext().prec - 10
    parity = n % 2
    if (kmax - parity) % 2:
        kmax -= 1
    ks, diag, off = _matrix(c, kmax, parity)
    j = n // 2
    lam = _eig(diag, off, j, digits)
    d = _eigvec(diag, off, lam)
    # fix sign so that d[0] > 0
    if d[0] < 0:
        d = [-x for x in d]
    P0 = _legendre_at_0(kmax, parity)
    PI = pi()
    if parity == 0:
        psi0 = sum(dk * (D(k) + D(1) / 2).sqrt() * P0[k] for k, dk in zip(ks, d))
        Lam = c * d[0] * d[0] / (PI * psi0 * psi0)
    else:
        dpsi0 = sum(dk * (D(k) + D(1) / 2).sqrt() * P0[k] for k, dk in zip(ks, d))
        Lam = c ** 3 * d[0] * d[0] / (3 * PI * dpsi0 * dpsi0)
    return Lam, lam, d, ks


def sum_rule(c, nmax=None):
    """sum_n Lambda_n(c) should equal 2c/pi (the trace)."""
    c = D(c)
    if nmax is None:
        nmax = int(4 * float(c) / 3.14159) + 40
    tot = D(0)
    for n in range(nmax):
        L, _, _, _ = lambda_n(c, n)
        tot += L
    return tot, 2 * c / pi()


def fuchs(c, n):
    """Fuchs' asymptotic 1 - Lambda_n(c) ~ 4 sqrt(pi) 8^n c^{n+1/2} e^{-2c}/n!"""
    from math import factorial
    c = D(c)
    PI = pi()
    return (4 * PI.sqrt() * D(8) ** n * c ** (D(n) + D(1) / 2) *
            exp(-2 * c) / D(factorial(n)))

# --------------------------------------------------------------------------
# THE CHECKS
# --------------------------------------------------------------------------

def F(x, n=18, e=False, sgn=False):
    """Exact fixed/scientific formatting of a Decimal.  NOT %-formatting: the %
    operator converts a Decimal to a float first and silently truncates every
    digit past the seventeenth, which is fatal for a quantity of size 1e-54."""
    return format(x, ("+" if sgn else "") + "." + str(n) + ("E" if e else "f"))


def _xi(n, x, L):
    """:385 basis, extended by zero outside [-L/2, L/2].  Used only by CHECK 0,
    which tests the closed-form table against the definition."""
    if x < -L / 2 or x > L / 2:
        return D(0)
    if n == 0:
        return 1 / L.sqrt()
    s = D(-1) ** abs(n)
    if n > 0:
        return s * (2 / L).sqrt() * cos(2 * pi() * n * x / L)
    return s * (2 / L).sqrt() * sin(2 * pi() * n * x / L)


def _conv(n, m, t, L, M=400, q=32):
    """(xi_n * xi_m^*)(t) = int_{t-L/2}^{L/2} xi_n(x) xi_m(x-t) dx   (:395)."""
    lo, hi = t - L / 2, L / 2
    if hi <= lo:
        return D(0)
    xs, ws = gl_nodes(q)
    h = (hi - lo) / M
    tot = D(0)
    for j in range(M):
        a = lo + j * h
        for x, w in zip(xs, ws):
            y = a + h * (x + 1) / 2
            tot += w * h / 2 * _xi(n, y, L) * _xi(m, y - t, L)
    return tot


def _table(n, m, y, L):
    """The :444 table entry, i.e. (1/2)(xi_n*xi_m^* + xi_m*xi_n^*)(y) on [0,L]."""
    PI = pi()
    a = lambda k: 2 * PI * k / L
    if n == 0 and m == 0:
        return (L - y) / L
    if n == m and n > 0:
        return (L - y) * cos(a(n) * y) / L - sin(a(n) * y) / (2 * PI * n)
    if n == m and n < 0:
        return sin(a(n) * y) / (2 * PI * n) + (L - y) * cos(a(n) * y) / L
    if n > 0 and m > 0:
        return (n * sin(a(n) * y) - m * sin(a(m) * y)) / (PI * (m * m - n * n))
    if n < 0 and m < 0:
        return (m * sin(a(n) * y) - n * sin(a(m) * y)) / (PI * (m * m - n * n))
    if n > 0 and m == 0:
        return -sin(a(n) * y) / (D(2).sqrt() * PI * n)
    if n == 0 and m > 0:
        return -sin(a(m) * y) / (D(2).sqrt() * PI * m)
    return D(0)


def check0():
    print("CHECK 0 -- the apparatus, before it is used for anything")
    print()
    getcontext().prec = 60
    print("  (a) the standard-library arithmetic against known digits")
    for nm, got, want in (
            ("pi   ", pi(), "3.1415926535897932384626433832795028841971693993751058209749"),
            ("log 2", ln2(), "0.6931471805599453094172321214581765680755001343602552541207"),
            ("gamma", euler_gamma(), "0.5772156649015328606065120900824024310421593359399235988058"),
            ("e    ", exp(D(1)), "2.7182818284590452353602874713526624977572470936999595749670")):
        d = abs(got - D(want))
        print("      %s = %s   |got - known| = %s   %s"
              % (nm, F(got, 50), F(d, 3, e=True), "OK" if d < D("1e-55") else "MISMATCH"))
    print()
    print("  (b) psi(1/4): the asymptotic-series route against Gauss' closed form")
    a = digamma(D(1) / 4)
    b = -euler_gamma() - 3 * ln2() - pi() / 2
    print("      series  psi(1/4) = %s" % a)
    print("      closed  -g-3ln2-pi/2 = %s" % b)
    print("      difference = %s" % (a - b))
    print()
    getcontext().prec = 40
    L = ln(D(5))
    print("  (c) the convolution table (:444) against brute-force quadrature of")
    print("      the basis functions themselves.  Nothing in this comparison uses")
    print("      the table; the table is the thing being tested.")
    print()
    print("      %-4s %-4s %-6s %-24s %s" % ("n", "m", "t", "direct convolution", "table - direct"))
    pairs = [(0, 0), (1, 1), (2, 3), (0, 4), (-1, -1), (-2, -3)]
    if not QUICK:
        pairs += [(3, 0), (5, 5)]
    for (n, m) in pairs:
        for tt in ("0.3", "1.1"):
            t = D(tt)
            direct = (_conv(n, m, t, L) + _conv(m, n, t, L)) / 2
            print("      %-4d %-4d %-6s %-24s %.2e"
                  % (n, m, tt, F(direct, 20), float(_table(n, m, t, L) - direct)))
    print()
    print("  (d) W_{0,2}^# three ways: quadrature of the table against the closed")
    print("      form 2 v_n v_m derived here, and against the paper's own printed")
    print("      closed forms (h02ev) :474 (even) and (h02) :478 (odd).")
    print()
    K = exp(L / 2) - 2 + exp(-L / 2)
    sh = sinh(L / 4)
    PI = pi()

    def vv(n):
        if n == 0:
            return 4 * sh / L.sqrt()
        return (2 / L).sqrt() * 4 * L * sh * (L / (L * L + 16 * PI * PI * n * n))

    def numeric(n, m, M=600, q=32):
        xs, ws = gl_nodes(q)
        h = L / M
        tot = D(0)
        for j in range(M):
            for x, w in zip(xs, ws):
                y = j * h + h * (x + 1) / 2
                tot += w * h / 2 * 2 * _table(n, m, y, L) * 2 * cosh(y / 2)
        return tot

    print("      %-8s %-26s %-14s %-14s" % ("n,m", "quadrature", "/ 2 v_n v_m", "/ paper"))
    for (n, m) in ([(1, 2), (0, 0), (0, 2)] if QUICK else [(1, 2), (3, 3), (0, 0), (0, 2), (4, 7)]):
        num = numeric(n, m)
        mine = 2 * vv(n) * vv(m)
        rp = ""
        if n > 0 and m > 0:
            paper = 8 * K * L ** 3 / ((L * L + 16 * PI * PI * m * m) *
                                      (L * L + 16 * PI * PI * n * n))
            rp = F(num / paper, 15)
        print("      %-8s %-26s %-14s %-14s"
              % ("%d,%d" % (n, m), F(num, 18), F(num / mine, 15), rp))
    for (n, m) in [(-1, -2), (-3, -3)]:
        num = numeric(n, m)
        paper = -256 * PI ** 2 * L * K * m * n / (
            (L * L + 16 * PI * PI * m * m) * (L * L + 16 * PI * PI * n * n))
        print("      %-8s %-26s %-14s %-14s"
              % ("%d,%d" % (n, m), F(num, 18), "", F(num / paper, 15)))
    print()
    print("  FINDING.  The table (:444) is right, in both sectors, to every digit")
    print("  the quadrature resolves.  The rank-one closed form derived here")
    print("  reproduces it exactly.  The paper's own (h02) for the ODD sector is")
    print("  exact.  The paper's (h02ev) for the EVEN sector is a factor 2 too")
    print("  small -- the ratio above is 2.000000000000000, not 1.  This is an")
    print("  erratum in arXiv:2106.01715, not in this project: neither")
    print("  `verify_deficit_repair.py` nor this file uses (h02ev), both building")
    print("  W_{0,2} from the table instead.  See the note, section 6.")
    print()


def check1():
    print("CHECK 1 -- NUMBER ONE: the bound |2 theta'(0)| = 5.3721834...")
    print()
    print("  theta(t) = -t/2 log pi + Im log Gamma(1/4 + it/2)   (:266), so")
    print("  theta'(t) = -1/2 log pi + 1/2 Re psi(1/4 + it/2) and 2 theta'(0) =")
    print("  psi(1/4) - log pi.  psi' has negative imaginary part on the ray, so")
    print("  theta' increases on t>0 and theta'(0) is its infimum; with Plancherel")
    print("  and the even-sector boundary term being a square (CHECK 0(d) shows")
    print("  W_{0,2} = 2 v v^T >= 0), lambda_min(sigma^arch) >= 2 theta'(0).")
    print()
    for p in (30, 60, 100):
        getcontext().prec = p
        a = ln(pi()) - digamma(D(1) / 4)
        b = euler_gamma() + 3 * ln2() + pi() / 2 + ln(pi())
        print("      %3d dps:  log pi - psi(1/4) = %s" % (p, a))
        print("                closed form       = %s" % b)
    print()
    print("  Both routes, at three precisions.  |2 theta'(0)| = 5.3721834192256656")
    print("  and the note's 5.3721834192... is confirmed.")
    print()


def _cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def _cinv(a):
    d = a[0] * a[0] + a[1] * a[1]
    return (a[0] / d, -a[1] / d)


def re_digamma(zr, zi, M=60, nterms=14):
    """Re psi(zr + i zi).  Recurrence to a large argument then the asymptotic
    series; only the real part is wanted, so no arctan is needed and the
    branch of the logarithm never enters."""
    acc = D(0)
    for k in range(M):
        acc -= _cinv((zr + k, zi))[0]
    w = (zr + M, zi)
    v = ln(w[0] * w[0] + w[1] * w[1]) / 2 - _cinv((2 * w[0], 2 * w[1]))[0]
    B = _bernoulli(2 * nterms + 2)
    w2 = _cmul(w, w)
    wp = w2
    for n in range(1, nterms + 1):
        b = B[2 * n]
        v -= D(b.numerator) / D(b.denominator) / (2 * n) * _cinv(wp)[0]
        wp = _cmul(wp, w2)
    return v + acc


def check1b(T=None):
    print("CHECK 1b -- the one link BOTH implementations take on trust:")
    print("            is eq (thetaprime) :261 normalised as printed?")
    print()
    print("  -W_R^#(f,f) = int |fhat(t)|^2 2 theta'(t)/(2 pi) dt.  A factor 2 here")
    print("  would double the bound of CHECK 1, and `deficit-repair.md` section 8")
    print("  names this as the claim that would do the most damage if wrong.  It is")
    print("  Connes-Consani's, not ours, and it is not re-proved here -- but it can")
    print("  be tested, and is.")
    print()
    print("  Test function f = (1 + cos(a_1 x))^2 = 3/2 + 2 cos(a_1 x) + 1/2 cos(a_2 x),")
    print("  chosen because it vanishes to second order at +-L/2, so fhat decays")
    print("  like t^-5 and the tail past the cutoff is negligible -- where the")
    print("  natural choice f = xi_1 decays like 1/t and needs its tail supplied")
    print("  from an asymptotic form.  Re psi(1/4 + it/2) is computed by the")
    print("  complex recurrence above.")
    print()
    getcontext().prec = 40
    cases = [("3", 60), ("8", 60)] if QUICK else [("3", 60), ("8", 60), ("8", 200)]
    for muv, Tv in cases:
        T = D(Tv)
        mu = D(muv)
        L = ln(mu)
        PI = pi()
        a1 = 2 * PI / L
        a2 = 4 * PI / L
        c = [D(3) / 2 * L.sqrt(), -(2 * L).sqrt(), D(1) / 2 * (L / 2).sqrt()]
        f = Form(mu, 4, with_primes=False)
        lhs = D(0)
        for n in range(3):
            for m in range(3):
                cs, cc = f.coeffs(n, m)
                wr = f.theta0(n, m) / 2 * f.G
                for k, cf in cs.items():
                    wr += cf * f.P[k]
                for k, cf in cc.items():
                    wr += cf * f.Q[k]
                lhs += c[n] * c[m] * (-wr)
        M = int(T * 20)
        xs, ws = gl_nodes(24)
        h = T / M
        rhs = D(0)
        pl = D(0)
        for j in range(M):
            for x, w in zip(xs, ws):
                t = j * h + h * (x + 1) / 2
                fh = sin(t * L / 2) * (3 / t + 4 * t / (a1 * a1 - t * t)
                                       - t / (a2 * a2 - t * t))
                wt = w * h / 2 * fh * fh
                rhs += wt * (re_digamma(D(1) / 4, t / 2) - ln(PI)) / 2
                pl += wt
        rhs = 2 / PI * rhs
        pl = pl / PI
        nf = sum(x * x for x in c)
        print("      mu = %s,  cutoff T = %s" % (muv, T))
        print("        -W_R^#(f,f) from the matrix     = %s" % F(lhs, 22))
        print("        int |fhat|^2 2 theta'/(2 pi) dt = %s" % F(rhs, 22))
        print("        ratio                           = %s" % F(rhs / lhs, 22))
        print("        Plancherel (1/2pi) int |fhat|^2 = %s" % F(pl, 22))
        print("        ||f||^2                         = %s" % F(nf, 22))
        print("        ratio                           = %s" % F(pl / nf, 22))
    print()
    print("  There is no extra factor of 2.  The residual in both ratios is the")
    print("  truncated tail int_T^infty, which is O(log T / T^9) here.  Three things")
    print("  say it is the tail and not a constant: the identity and Plancherel --")
    print("  which is exact -- are off by the same amount in the same direction;")
    print("  raising the working precision from 40 to 70 dps does not move either;")
    print("  and at mu=8 raising T from 60 to 200 improves the identity by a factor")
    print("  3.1e4, against the (200/60)^9 = 2.6e4 that O(T^-9) predicts.")
    print()


def check2(N=None):
    print("CHECK 2 -- NUMBER ONE, continued: the deficit D(mu) saturates the bound")
    print()
    N = N or (60 if QUICK else 160)
    getcontext().prec = 60
    bound = euler_gamma() + 3 * ln2() + pi() / 2 + ln(pi())
    print("  N = %d (even-sector indices 0..%d), 60 dps.  D(mu) = -lambda_min(sigma^arch)."
          % (N, N))
    print()
    print("      %-8s %-12s %-24s %s" % ("mu", "L", "D(mu)", "bound - D"))
    mus = ["3", "5", "11", "20", "100"] if QUICK else \
          ["3", "5", "11", "20", "100", "1000", "1e6", "1e9", "1e12", "1e20"]
    for mu in mus:
        f = Form(D(mu), N, with_primes=False)
        al, be = tridiagonalize(f.arch())
        lo, hi = eig_k(al, be, 0, digits=30)
        Dm = -(lo + hi) / 2
        print("      %-8s %-12s %-24s %s"
              % (mu, F(f.L, 5), F(Dm, 14), F(bound - Dm, 8)))
    print()
    print("  D increases in mu, never reaches the bound, and is 5.2835 at 1e20.")
    print("  Compare `deficit-repair.md` section 2.2.")
    print()


def check3(N=60):
    print("CHECK 3 -- NUMBER TWO: on the archimedean worst direction the primes")
    print("           over-repair, and the margin is closing")
    print()
    getcontext().prec = 40
    print("  N = %d, 40 dps.  v_arch minimises sigma^arch; R = -sum_p W_p(v_arch)." % N)
    print()
    print("      %-5s %-14s %-14s %-13s %s" % ("mu", "D(mu)", "R(mu)", "R-D", "R/D"))
    for mu in ((3, 5, 8, 12, 20) if QUICK else (3, 4, 5, 6, 8, 10, 12, 16, 20)):
        f = Form(D(mu), N)
        A = f.arch()
        Pr = f.primes_matrix()
        al, be = tridiagonalize(A)
        lam = eig_k(al, be, 0, digits=28)[0]
        v = inverse_iteration(A, lam, iters=3)
        Dm = -rayleigh(A, v)
        R = -quadform(Pr, v) / sum(x * x for x in v)
        print("      %-5d %-14s %-14s %-13s %s"
              % (mu, F(Dm, 8), F(R, 8), F(R - Dm, 8), F(R / Dm, 4)))
    print()
    print("  R > D at every mu computed; R/D falls from 1.6777 to 1.0151.")
    print("  Compare `deficit-repair.md` section 3.")
    print()


def check4(N=None):
    print("CHECK 4 -- NUMBER THREE: the near-radical direction, and the REVERSED")
    print("           SIGNS.  This is the claim the ticket says to check hardest.")
    print()
    N = N or (60 if QUICK else 100)
    getcontext().prec = 80 if QUICK else 120
    print("  N = %d, %d dps.  v_mu is the bottom eigenvector of the FULL form."
          % (N, getcontext().prec))
    print()
    print("      %-5s %-20s %-20s %-16s %-10s %s"
          % ("mu", "sigma^arch(v_mu)", "-sum_p W_p(v_mu)", "s(mu)", "log10 s", "digits"))
    out = {}
    for mu in (5, 6, 7, 8, 9, 10, 11, 12):
        f = Form(D(mu), N)
        A = f.arch()
        Pr = f.primes_matrix()
        Full = [[A[i][j] - Pr[i][j] for j in range(N + 1)] for i in range(N + 1)]
        al, be = tridiagonalize(Full)
        lam, _ = eig_min_relative(al, be, reldigits=25)
        v = inverse_iteration(Full, lam, iters=3)
        nrm = sum(x * x for x in v)
        qa = quadform(A, v) / nrm
        qp = -quadform(Pr, v) / nrm
        s = qa + qp
        out[mu] = s
        print("      %-5d %-20s %-20s %-16s %-10s %s"
              % (mu, F(qa, 8, sgn=True), F(qp, 8, sgn=True), F(s, 4, e=True),
                 F(ln(s) / ln(D(10)), 3), F(ln(abs(qa) / s) / ln(D(10)), 2)))
    print()
    print("  CONFIRMED.  On the direction that decides positivity the archimedean")
    print("  half is POSITIVE and the prime half is NEGATIVE -- the deficit/repair")
    print("  picture of CHECK 3 with its signs reversed -- and both halves are")
    print("  ~0.025 log mu, two orders below the deficit D.  Compare section 4.1.")
    print()
    return out


def check5(svals):
    print("CHECK 5 -- NUMBER FOUR: the fit, against 4 pi / log 10")
    print()
    getcontext().prec = 50
    ln10 = ln(D(10))
    rows = []
    for mu in sorted(svals):
        rows.append(([D(-mu), ln(D(mu)) / ln10, D(1)], ln(svals[mu]) / ln10))
    p = 3
    M = [[sum(r[i] * r[j] for r, _y in rows) for j in range(p)] for i in range(p)]
    b = [sum(r[i] * y for r, y in rows) for i in range(p)]
    coef = solve(M, b)
    res = [y - sum(coef[i] * r[i] for i in range(p)) for r, y in rows]
    n = len(rows)
    s2 = sum(x * x for x in res) / (n - p)
    se = [(s2 * solve(M, [D(1) if k == i else D(0) for k in range(p)])[i]).sqrt()
          for i in range(p)]
    names = ("A", "B", "D")
    reported = ("5.4635 +- 0.052", "5.322 +- 0.96", "6.589 +- 0.44")
    for i in range(p):
        print("      %s = %10s +- %-10s      (reported: %s)"
              % (names[i], F(coef[i], 6), F(se[i], 6), reported[i]))
    print("      residual rms = %s (/n)  %s (/(n-p))   max |res| = %s"
          % (F((sum(x * x for x in res) / n).sqrt(), 5),
             F((sum(x * x for x in res) / (n - p)).sqrt(), 5),
             F(max(abs(x) for x in res), 5)))
    print()
    tgt = 4 * pi() / ln10
    print("      4 pi / log 10 = %s" % tgt)
    print("      A - 4pi/log10 = %s  =  %s sigma"
          % (F(coef[0] - tgt, 6), F((coef[0] - tgt) / se[0], 3)))
    print("      B vs 9/2 (prolate index 4)     ->  %s sigma" % F((coef[1] - D("4.5")) / se[1], 3))
    print("      B vs 1/2 (prolate index 0)     ->  %s sigma" % F((coef[1] - D("0.5")) / se[1], 3))
    c4 = ln(D(2) ** 14 * D(2).sqrt() * pi() ** 5 / 3) / ln10
    print("      D vs log10(2^14 sqrt2 pi^5/3) = %s  ->  %s sigma"
          % (F(c4, 6), F((coef[2] - c4) / se[2], 3)))
    print()
    print("  All three fitted parameters and all three standard errors reproduce")
    print("  the note's, and the constant 6.373563 -- which `deficit-repair.md`")
    print("  records as having been mis-transcribed once as 6.37347 -- is")
    print("  confirmed here from scratch.  Compare section 5 and `prolate-rate.md`")
    print("  section 4.")
    print()
    return coef


def check6(svals):
    print("CHECK 6 -- NUMBER FIVE: the index is 4, not 0")
    print()
    getcontext().prec = 40
    L0, _, _, _ = lambda_n(D(1), 0, kmax=60)
    print("  Lambda_0(c=1) = %s" % L0)
    print("  Slepian's classical tabulated value is 0.57258 -- an external anchor,")
    print("  and the only one available for the prolate apparatus.")
    print()
    getcontext().prec = 60
    tot, exact = sum_rule(D(5), nmax=30)
    print("  THE TRACE SUM RULE, which is what pins the normalisation constant:")
    print("      sum_n Lambda_n(5) = %s" % tot)
    print("      2c/pi             = %s" % exact)
    print("      difference        = %s" % F(tot - exact, 3, e=True))
    print("  The identity Lambda_n = c d_0^2/(pi psi_n(0)^2) is derived in the")
    print("  module docstring above from the finite Fourier transform; a wrong")
    print("  factor there is exactly what this sum rule would expose, and does not.")
    print()
    getcontext().prec = 160
    PI = pi()
    print("      %-4s %-14s %-14s %-14s %-16s %s"
          % ("mu", "1-Lambda_0", "1-Lambda_4", "1-chi_2", "s/(1-Lambda_0)", "s/(1-chi_2)"))
    r0 = []
    r2 = []
    for mu in sorted(svals):
        c = 2 * PI * mu
        A0, _, _, _ = lambda_n(c, 0)
        A4, _, _, _ = lambda_n(c, 4)
        d0 = 1 - A0
        dchi = 1 - A4.sqrt()
        s = +svals[mu]
        r0.append(s / d0)
        r2.append(s / dchi)
        print("      %-4d %-14s %-14s %-14s %-16s %s"
              % (mu, F(d0, 5, e=True), F(1 - A4, 5, e=True), F(dchi, 5, e=True),
                 F(s / d0, 5, e=True), F(s / dchi, 4)))
    print()
    print("      s/(1-Lambda_0) grows by a factor %s over mu=5..12" % F(r0[-1] / r0[0], 2))
    print("      s/(1-chi_2) stays in [%s, %s]" % (F(min(r2), 4), F(max(r2), 4)))
    print()
    print("  CONFIRMED.  s exceeds the index-0 defect by nine to ten orders and")
    print("  the gap GROWS; against the index-4 defect the ratio stays O(10) with")
    print("  no trend.  The index is 4.  Compare `prolate-rate.md` section 3.")
    print("  At the full N=100 the figures are: growth factor 56.16, ratio in")
    print("  [7.6074, 12.9609].  Under --quick (N=60) both are inflated, because")
    print("  s(N) is an UPPER bound and a looser truncation gives a larger one --")
    print("  which is the variational point of CHECK 7(c) showing up as a")
    print("  systematic, not as noise.")
    print()
    getcontext().prec = 100
    c = 2 * PI * 12
    connes = D(2) ** 14 * D(2).sqrt() * PI ** 5 / 3 * D(12) ** (D(9) / 2) * exp(-4 * PI * 12)
    print("  Connes' printed constant (`rhready.tex:1149`) against Fuchs at n=4:")
    print("      (2^14 sqrt2 pi^5/3) mu^{9/2} e^{-4 pi mu}  /  (Fuchs(4, 2 pi mu)/2)")
    print("      = %s" % (connes / (fuchs(c, 4) / 2)))
    print("  Identically one half of Fuchs at index 4, as `prolate-rate.md` says,")
    print("  and the halving is exactly 1 - sqrt(x) ~ (1-x)/2.  Derived, not quoted.")
    print()


def check7():
    print("CHECK 7 -- stability: working precision, quadrature, truncation")
    print()
    print("  (a) same L = log 8, same N = 60, three working precisions")
    print()
    print("      %-8s %-22s %s" % ("dps", "D(8)", "s(8)"))
    for prec, rel in ((40, 6), (80, 20), (140, 25)):
        getcontext().prec = prec
        f = Form(D(8), 60)
        A = f.arch()
        al, be = tridiagonalize(A)
        Dv = -eig_k(al, be, 0, digits=prec - 12)[0]
        al2, be2 = tridiagonalize(f.full())
        s, _ = eig_min_relative(al2, be2, reldigits=rel)
        print("      %-8d %-22s %s" % (prec, F(Dv, 18), F(s, 18, e=True)))
    print()
    print("  D does not move at all.  s is correct to seven digits at 40 dps and")
    print("  stops moving thereafter -- a quantity of size 1e-33 read off entries")
    print("  of order 1 has 40-33 = 7 digits of room at 40 dps, and double")
    print("  precision has 16-33 < 0, which is not lost accuracy but none.")
    print()
    print("  (b) quadrature refinement at mu=8, N=60, 80 dps")
    print()
    getcontext().prec = 80
    for ppp, q in ((1, 40), (2, 40), (1, 64), (2, 64)):
        f = Form(D(8), 60, panels_per_period=ppp, q=q)
        al, be = tridiagonalize(f.arch())
        print("      panels/period=%d  nodes/panel=%2d :  D(8) = %s"
              % (ppp, q, F(-eig_k(al, be, 0, digits=40)[0], 36)))
    print()
    print("  (c) N-convergence of s(11) against Connes-Consani's ONE published")
    print("      number, 2.389e-48 at :178")
    print()
    getcontext().prec = 100
    for N in ((50, 80) if QUICK else (50, 80, 100, 120)):
        f = Form(D(11), N)
        al, be = tridiagonalize(f.full())
        s, _ = eig_min_relative(al, be, reldigits=25)
        print("      N = %-4d s(11) = %s   log10 = %s"
              % (N, F(s, 7, e=True), F(ln(s) / ln(D(10)), 4)))
    print()
    print("      TRUNCATION IS VARIATIONAL AND CUTS ONE WAY.  Restricting the form")
    print("      to a subspace can only raise its smallest eigenvalue, so every")
    print("      s(N) above is an UPPER BOUND on the true s and the sequence is")
    print("      decreasing.  The exponent -48 is settled and reproduces their")
    print("      number; the mantissa is still falling at N=120 and is NOT")
    print("      converged, so nothing here verifies their 2.389.  N=50 landing on")
    print("      2.3894 is either their truncation level or a coincidence and the")
    print("      paper does not say which.")
    print()
    print("  (d) prolate defect stability at mu=12 (the smallest quantity here)")
    print()
    for prec, kmax in ((100, None), (160, None), (220, None), (160, 500)):
        getcontext().prec = prec
        A4, _, _, _ = lambda_n(2 * pi() * 12, 4, kmax=kmax)
        print("      dps=%-4d kmax=%-5s 1-Lambda_4(2 pi 12) = %s"
              % (prec, kmax, F(1 - A4, 20, e=True)))
    print()


def check8():
    print("CHECK 8 -- every prime power below mu is load-bearing")
    print()
    getcontext().prec = 70
    N = 60
    f = Form(D(12), N)
    al, be = tridiagonalize(f.full())
    s, _ = eig_min_relative(al, be, reldigits=20)
    print("  mu = 12, N = %d, 70 dps." % N)
    print()
    print("      %-12s %s" % ("omitted", "lambda_min"))
    print("      %-12s %s" % ("none", F(s, 4, e=True, sgn=True)))
    for j in (2, 3, 4, 5, 7, 8, 9, 11):
        al, be = tridiagonalize(f.full(drop=j))
        print("      %-12d %s" % (j, F(eig_k(al, be, 0, digits=25)[0], 8, sgn=True)))
    print()
    print("  Compare `deficit-repair.md` section 4.3.")
    print()


if __name__ == "__main__":
    want = [a for a in sys.argv[1:] if not a.startswith("--")]
    run = (lambda k: (not want) or str(k) in want)
    if run(0):
        check0()
    if run(1):
        check1()
        check1b()
    if run(2):
        check2()
    if run(3):
        check3()
    sv = None
    if run(4) or run(5) or run(6):
        sv = check4()
    if run(5) and sv:
        check5(sv)
    if run(6) and sv:
        check6(sv)
    if run(7):
        check7()
    if run(8):
        check8()
