#!/usr/bin/env python3
"""Settle audit item U6: does the corpus's h_{4,lambda} mean prolate index 4,
or Connes-Consani's m=4 (= prolate index 8)?

Work item mg-9433.  Companion to `index-convention.md`.

The discriminating artifact proposed by the ticket is `start.tex:180-181`,

        h_lambda(0) = alpha h_{0,lambda}(0) (chi_4 - chi_0)/chi_4 ,

asserted for the CCM combination h_lambda = alpha h_{0,lambda} + beta h_{4,lambda}
under the constraint hat h_lambda(0) = 0 (`start.tex:171`).  This script evaluates
it under both readings, in arbitrary precision, and reports which reproduces it.

ARITHMETIC.  mpmath throughout; the working precision is a parameter and every
table states it.  Nothing here is done in double precision except section 6,
which measures double precision on purpose.  There is no numpy dependency
(unlike `verify_prolate_claims.py`).

    pip install mpmath && python3 notes/verify_index_convention.py

METHOD.  The prolate spheroidal functions are built from the prolate
differential operator

        L_c psi = d/dx[(1-x^2) psi'] - c^2 x^2 psi = -chi^SL psi ,

which is symmetric tridiagonal in the orthonormal Legendre basis Pbar_k
(k = 0,2,4,... for the even prolates) with well-separated eigenvalues ~ -k^2.
This is the route `s3-reduction-audit.md:340-345` recommends; it is stable at
any c, unlike the sinc concentration kernel, whose top eigenvalues cluster at 1
and whose eigenvectors then degenerate.  Eigenvalues come from Sturm-sequence
bisection (exact sign counts, no iteration to a wrong root), eigenvectors from
inverse iteration, and every eigenpair carries a reported residual.

The finite-Fourier eigenvalue is obtained WITHOUT quadrature: Slepian-Pollak
gives  \\int_{-1}^{1} psi_n(t) e^{i c x t} dt = mu_n psi_n(x), and at x = 0 the
left side is just \\int psi_n = sqrt(2) d_0 (the basis is orthonormal and only
Pbar_0 has nonzero integral).  So mu_n = sqrt(2) d_0 / psi_n(0) exactly.  The
concentration eigenvalue is Lambda_n = c mu_n^2/(2 pi) and the corpus's
chi_n = sqrt(Lambda_n) (`s3-reduction-audit.md:55-57`).

Section 0 cross-checks mu_n against a genuinely independent evaluation --
the same integral at x != 0 via  \\int P_k(t) e^{izt} dt = 2 i^k j_k(z)  --
so the eigenvector, not merely the eigenvalue, is verified.
"""

from mpmath import mp, mpf, sqrt, besselj, pi, fabs, nstr, log10, power
import time

from verdict import Verdict

# The exit-code contract (mg-5995).  Section 0's three evaluation points "must
# not depend on x" and their signs must reproduce i^n; section 1 states the
# result BOTH ways -- the identity holds to working precision for every
# m = 0 mod 4 and fails for every m = 2 mod 4 -- and both directions are wired,
# so an identity that started holding for m = 2 mod 4 would fail this script as
# loudly as one that stopped holding for m = 0 mod 4.  Sections 2--6 are
# stability tables and convergences with no threshold stated.
VD = Verdict()

# ---------------------------------------------------------------- prolate core


def build(c, N):
    """L_c in the even orthonormal-Legendre basis.  Row i <-> degree k = 2i."""
    c2 = mpf(c) ** 2
    d, e = [], []
    for i in range(N):
        k = mpf(2 * i)
        b_k = (2 * k * k + 2 * k - 1) / ((2 * k - 1) * (2 * k + 3))   # <P_k|x^2|P_k>
        d.append(-k * (k + 1) - c2 * b_k)
    for i in range(N - 1):
        k = mpf(2 * i)
        a_k = (k + 1) * (k + 2) / ((2 * k + 1) * (2 * k + 3))         # P_{k+2} coeff
        e.append(-c2 * a_k * sqrt((2 * k + 1) / (2 * k + 5)))
    return d, e


def sturm_count(d, e, x):
    """Number of eigenvalues of the tridiagonal (d,e) strictly below x."""
    tiny = mpf(2) ** (-mp.prec + 20)
    q = d[0] - x
    cnt = 1 if q < 0 else 0
    for i in range(1, len(d)):
        if q == 0:
            q = tiny
        q = d[i] - x - e[i - 1] ** 2 / q
        if q < 0:
            cnt += 1
    return cnt


def eig_j(d, e, j, lo, hi):
    """j-th smallest eigenvalue (0-based), by Sturm bisection."""
    for _ in range(mp.prec + 20):
        mid = (lo + hi) / 2
        if sturm_count(d, e, mid) > j:
            hi = mid
        else:
            lo = mid
        if hi - lo < fabs(mid) * mpf(2) ** (-mp.prec + 8):
            break
    return (lo + hi) / 2


def solve_tri(d, e, lam, b):
    """Thomas algorithm for (T - lam I) v = b."""
    n = len(d)
    tiny = mpf(2) ** (-mp.prec + 20)
    cp = [mpf(0)] * n
    dp = [mpf(0)] * n
    piv = d[0] - lam or tiny
    cp[0] = (e[0] / piv) if n > 1 else mpf(0)
    dp[0] = b[0] / piv
    for i in range(1, n):
        piv = d[i] - lam - e[i - 1] * cp[i - 1] or tiny
        if i < n - 1:
            cp[i] = e[i] / piv
        dp[i] = (b[i] - e[i - 1] * dp[i - 1]) / piv
    v = [mpf(0)] * n
    v[n - 1] = dp[n - 1]
    for i in range(n - 2, -1, -1):
        v[i] = dp[i] - cp[i] * v[i + 1]
    return v


def eigvec(d, e, lam, iters=3):
    n = len(d)
    shift = lam * (1 + mpf(2) ** (-mp.prec + 10)) + mpf(2) ** (-mp.prec + 10)
    v = [mpf(1) / sqrt(n)] * n
    for _ in range(iters):
        v = solve_tri(d, e, shift, v)
        nrm = sqrt(sum(x * x for x in v))
        v = [x / nrm for x in v]
    return v


def residual(d, e, lam, v):
    n, r = len(d), mpf(0)
    for i in range(n):
        s = (d[i] - lam) * v[i]
        if i > 0:
            s += e[i - 1] * v[i - 1]
        if i < n - 1:
            s += e[i] * v[i + 1]
        r += s * s
    return sqrt(r)


def Pbar_at_0(k):
    """Pbar_k(0) = sqrt((2k+1)/2) * (-1)^{k/2} (k-1)!!/k!!, k even."""
    val = mpf(1)
    for j in range(2, k + 1, 2):
        val *= mpf(j - 1) / mpf(j)
    if (k // 2) % 2:
        val = -val
    return val * sqrt(mpf(2 * k + 1) / 2)


def Pbar_at(k, x):
    x = mpf(x)
    p0, p1 = mpf(1), x
    if k == 0:
        return sqrt(mpf(1) / 2)
    for j in range(1, k):
        p0, p1 = p1, ((2 * j + 1) * x * p1 - j * p0) / (j + 1)
    return p1 * sqrt(mpf(2 * k + 1) / 2)


class Prolate:
    """Even prolate psi_n (n = 2*idx), band-limit c, L^2[-1,1]-normalised."""

    def __init__(self, c, idx, d, e, lam):
        self.c, self.idx, self.n = mpf(c), idx, 2 * idx
        self.chi_sl = -lam
        self.dcoef = eigvec(d, e, lam)
        self.res = residual(d, e, lam, self.dcoef)
        self.at0 = sum(dk * Pbar_at_0(2 * i) for i, dk in enumerate(self.dcoef))
        self.integral = sqrt(mpf(2)) * self.dcoef[0]        # \int_{-1}^{1} psi_n
        self.mu = self.integral / self.at0                  # finite-Fourier eigenvalue
        self.Lam = self.c * self.mu ** 2 / (2 * pi)         # concentration eigenvalue
        self.chi = sqrt(self.Lam)                           # the corpus's chi_n

    def mu_at(self, x):
        """Independent mu_n from \\int P_k e^{izt} = 2 i^k j_k(z), at x != 0."""
        tot = mpf(0)
        for i, dk in enumerate(self.dcoef):
            k = 2 * i
            sgn = -1 if (k // 2) % 2 else 1                 # i^k, k even
            jk = sqrt(pi / (2 * self.c * mpf(x))) * besselj(k + mpf(1) / 2,
                                                            self.c * mpf(x))
            tot += dk * sqrt(mpf(2 * k + 1) / 2) * 2 * sgn * jk
        psi_x = sum(dk * Pbar_at(2 * i, x) for i, dk in enumerate(self.dcoef))
        return tot / psi_x


def prolates(c, idx_max, N=None, dps=None):
    if dps is not None:
        mp.dps = dps
    c = mpf(c)
    if N is None:
        N = int(2 * float(c) + 60 + 4 * idx_max)
    d, e = build(c, N)
    lo = min(d[i] - (fabs(e[i - 1]) if i else 0)
             - (fabs(e[i]) if i < N - 1 else 0) for i in range(N)) - 1
    hi = max(d[i] + (fabs(e[i - 1]) if i else 0)
             + (fabs(e[i]) if i < N - 1 else 0) for i in range(N)) + 1
    # chi^SL rises with n, so the n-th even prolate is the (N-1-idx)-th
    # smallest eigenvalue of the matrix (whose eigenvalues are -chi^SL).
    return [Prolate(c, idx, d, e, eig_j(d, e, N - 1 - idx, lo, hi))
            for idx in range(idx_max + 1)]


# ------------------------------------------------------------------- the test


def identity_ratio(ps, m):
    """LHS/RHS of start.tex:180-181 with partner mode m (prolate index m).

    h_lambda = alpha psi_0 + beta psi_m, alpha = 1, beta fixed by hat h(0)=0.
    """
    p0, pm = ps[0], ps[m // 2]
    beta = -p0.integral / pm.integral                       # hat h_lambda(0) = 0
    lhs = p0.at0 + beta * pm.at0                            # h_lambda(0)
    rhs = p0.at0 * (pm.chi - p0.chi) / pm.chi               # start.tex:180-181
    return lhs / rhs, beta


def b_squared(ps, m):
    """|b_lambda|^2 for the L^2-normalised combination."""
    beta = -ps[0].integral / ps[m // 2].integral
    return beta ** 2 / (1 + beta ** 2)


def hr(title):
    print("\n" + "=" * 78 + "\n" + title + "\n" + "=" * 78)


def main():
    t_start = time.time()

    hr("0.  Pipeline verification -- mu_n from three independent evaluation points")
    print("mu_n = \\int psi_n e^{icxt} dt / psi_n(x) must not depend on x.")
    print("x=0 uses only d_0; x=0.7 and x=1 use the whole eigenvector and\n"
          "spherical Bessel functions.  Agreement checks the eigenVECTOR.\n")
    mp.dps = 40
    ps = prolates(10, 4, dps=40)
    print("  c = 10, dps = 40")
    print("  %3s %-24s %-24s %-24s %s" % ("n", "mu from x=0", "mu from x=0.7",
                                          "mu from x=1", "eig residual"))
    for p in ps:
        m07, m1 = p.mu_at(mpf(7) / 10), p.mu_at(1)
        # "must not depend on x": the three columns agree in all 20 printed
        # digits, the eigenvector residual being 1e-38 at dps = 40.
        for lbl, v in (("0.7", m07), ("1", m1)):
            VD.check(fabs(v / p.mu - 1) < mpf(10) ** -30,
                     "0: mu_%d from x=%s agrees with x=0" % (p.n, lbl))
        VD.check((p.mu > 0) == (p.n % 4 == 0),
                 "0: sign(mu_%d) = i^%d" % (p.n, p.n))
        print("  %3d %-24s %-24s %-24s %s" % (
            p.n, nstr(p.mu, 20), nstr(m07, 20), nstr(m1, 20), nstr(p.res, 4)))
    print("\n  Signs reproduce the Slepian-Pollak phase mu_n = i^n sqrt(2 pi Lambda_n/c):")
    print("  " + "  ".join("mu_%d %s 0" % (p.n, ">" if p.mu > 0 else "<") for p in ps))

    hr("1.  THE TEST -- start.tex:180-181 under every even partner mode")
    print("Ratio LHS/RHS at c = 30, dps = 80.  Reading A (mg-aedf) is m = 4;")
    print("reading B (Connes-Consani m=4 => PS_{8,0}) is m = 8.\n")
    mp.dps = 80
    ps = prolates(30, 10, dps=80)
    print("  %3s %8s %10s %-14s %-14s" % ("m", "m mod 4", "sign(mu_m)",
                                          "Lambda_m", "|ratio - 1|"))
    for m in range(2, 21, 2):
        r, _ = identity_ratio(ps, m)
        # both halves of the paragraph printed below the table.  For m = 0 mod 4
        # the column measures 1e-65 or smaller at dps = 80; for m = 2 mod 4 the
        # smallest failure on the grid is 12.56 (at m = 18), so the two classes
        # are separated by sixty orders and 1 is a safe place to cut.
        if m % 4 == 0:
            VD.check(fabs(r - 1) < mpf(10) ** -40,
                     "1: the identity holds at m = %d (= 0 mod 4)" % m)
        else:
            VD.check(fabs(r - 1) > 1,
                     "1: the identity fails at m = %d (= 2 mod 4)" % m)
        tag = ""
        if m == 4:
            tag = "   <- reading A"
        if m == 8:
            tag = "   <- reading B"
        print("  %3d %8d %10s %-14s %-14s%s" % (
            m, m % 4, "+" if ps[m // 2].mu > 0 else "-",
            nstr(ps[m // 2].Lam, 6), nstr(fabs(r - 1), 4), tag))
    print("\n  The identity holds to full working precision for EVERY m = 0 mod 4")
    print("  and fails by 4 to 20 orders of magnitude for EVERY m = 2 mod 4.")
    print("  It separates the phase classes and nothing finer.  A and B both pass.")

    hr("2.  Precision stability -- required by the ticket")
    print("|ratio - 1| must shrink as the working precision grows, or the")
    print("agreement in section 1 is roundoff rather than an identity.\n")
    cols = (30, 50, 80, 120, 200)
    print("  %5s %4s | %s" % ("c", "m", " ".join("dps=%-9d" % d for d in cols)))
    for c in (12, 20, 30, 40, 60):
        for m in (4, 8):
            row = []
            for dps in cols:
                psx = prolates(c, m // 2, dps=dps)
                r, _ = identity_ratio(psx, m)
                row.append(nstr(fabs(r - 1), 3).ljust(9))
            print("  %5d %4d | %s" % (c, m, " ".join(row)))
    print("\n  Every entry tracks the working precision.  The residual is roundoff;")
    print("  the identity is exact.  Practical rule: dps >~ 0.9c + (digits wanted).")

    hr("3.  Why both pass -- the identity carries exactly one bit")
    print("With hat h_lambda(0) = 0 and the Slepian-Pollak relation,")
    print("    h_lambda(0) = alpha psi_0(0) (1 - mu_0/mu_m),")
    print("and mu_0/mu_m = chi_0/(chi_m i^m).  So start.tex:180-181 holds")
    print("    <=>  i^m = +1  <=>  m = 0 (mod 4).")
    print("It fixes the finite-Fourier PHASE of h_{4,lambda} and says nothing")
    print("about which phase-matching index it is.  4 and 8 are both = 0 (mod 4).\n")
    print("This is not a small-c coincidence -- the two candidate modes are")
    print("wildly different objects at every c tested:")
    mp.dps = 120
    print("  %6s %-16s %-16s %-14s" % ("c", "Lambda_4", "Lambda_8", "1-Lambda_0"))
    for c in (8, 10, 14, 16, 20, 30):
        psx = prolates(c, 4, dps=120)
        print("  %6d %-16s %-16s %-14s" % (c, nstr(psx[2].Lam, 8),
                                           nstr(psx[4].Lam, 8),
                                           nstr(1 - psx[0].Lam, 4)))

    hr("4.  Constants under each reading")
    print("|b_lambda|^2 -> 8/11 under reading A, 128/163 under reading B.")
    print("(Hermite limit: psi_{2k}(0)^2/psi_0(0)^2 -> C(2k,k)/4^k; 3/8 for")
    print("n=4, 35/128 for n=8.  |b|^2 = 1/(1 + that).)   dps = 60\n")
    mp.dps = 60
    print("  %6s | %-20s %-20s" % ("c", "m=4  (-> 8/11)", "m=8  (-> 128/163)"))
    store = {}
    for c in (20, 40, 100, 200, 400):
        psx = prolates(c, 4, dps=60)
        v4, v8 = b_squared(psx, 4), b_squared(psx, 8)
        store[c] = (v4, v8)
        print("  %6d | %-20s %-20s" % (c, nstr(v4, 14), nstr(v8, 14)))
    print("  %6s | %-20s %-20s" % ("target", nstr(mpf(8) / 11, 14),
                                   nstr(mpf(128) / 163, 14)))
    e4 = 2 * store[400][0] - store[200][0]
    e8 = 2 * store[400][1] - store[200][1]
    print("\n  Richardson from c=200,400 assuming O(1/c) error:")
    print("    m=4: %s   vs 8/11    = %s   (diff %s)" % (
        nstr(e4, 10), nstr(mpf(8) / 11, 10), nstr(e4 - mpf(8) / 11, 3)))
    print("    m=8: %s   vs 128/163 = %s   (diff %s)" % (
        nstr(e8, 10), nstr(mpf(128) / 163, 10), nstr(e8 - mpf(128) / 163, 3)))

    print("\n  Lower-mode leakage ratio (1-Lambda_0)/(1-Lambda_m).  Fuchs predicts")
    print("  m!/8^m c^{-m}: 3/512 c^{-4} for m=4, 315/131072 c^{-8} for m=8.")
    mp.dps = 120
    print("  %5s | %-14s %-14s | %-14s %-14s" % (
        "c", "meas m=4", "pred", "meas m=8", "pred"))
    for c in (14, 20, 30, 40, 60):
        psx = prolates(c, 4, dps=120)
        print("  %5d | %-14s %-14s | %-14s %-14s" % (
            c,
            nstr((1 - psx[0].Lam) / (1 - psx[2].Lam), 6),
            nstr(mpf(3) / 512 / mpf(c) ** 4, 6),
            nstr((1 - psx[0].Lam) / (1 - psx[4].Lam), 6),
            nstr(mpf(315) / 131072 / mpf(c) ** 8, 6)))
    print("  Consistent with both exponents; the constants converge slowly, as")
    print("  Fuchs asymptotics do.  Same status as s3-reduction-audit.md's U4.")

    print("\n  psi_0(0)/c^{1/4} -> pi^{-1/4} = %s  (index-independent):"
          % nstr(power(pi, -mpf(1) / 4), 8))
    mp.dps = 60
    for c in (100, 200, 400):
        print("    c=%4d  %s" % (c, nstr(prolates(c, 0, dps=60)[0].at0
                                         / power(c, mpf(1) / 4), 10)))

    hr("5.  Matrix-truncation stability")
    print("|ratio - 1| at c=30, m=8, dps=80 as the Legendre basis is enlarged:")
    for N in (60, 90, 120, 160, 220):
        psx = prolates(30, 4, N=N, dps=80)
        r, _ = identity_ratio(psx, 8)
        print("    N = %4d   |ratio-1| = %s" % (N, nstr(fabs(r - 1), 3)))
    print("  Flat: the truncation is not the limiting error.")

    hr("6.  Double precision, on the well-conditioned route")
    print("s3-reduction-audit.md:328-331 reports the identity ~10% wrong at")
    print("c=16 and meaningless at c=20 in double precision.  That was measured")
    print("on the sinc concentration kernel.  On the differential-operator route")
    print("the same note recommends (:340-345), double precision does better:\n")
    print("  %5s %4s  %-14s" % ("c", "m", "|ratio-1| at dps=16"))
    for c in (12, 16, 20, 24, 28):
        for m in (4, 8):
            psx = prolates(c, m // 2, dps=16)
            r, _ = identity_ratio(psx, m)
            print("  %5d %4d  %-14s" % (c, m, nstr(fabs(r - 1), 4)))
    print("\n  So the double-precision ceiling mg-aedf measured is a property of")
    print("  the sinc-kernel implementation, not of the identity.  The residual")
    print("  cancellation (chi_m - chi_0 ~ 1-Lambda_0 ~ e^{-2c}) still bites, and")
    print("  arbitrary precision is still required above c ~ 24.")

    print("\n" + "-" * 78)
    print("total runtime %.1f s" % (time.time() - t_start))


if __name__ == "__main__":
    main()
    VD.finish()
