#!/usr/bin/env python3
"""Two checks for `semilocal-gap.md` (work item mg-03f0).  Needs numpy.

CHECK 1 (sec 3.2) -- is the prime term of the semi-local Weil quadratic form of
one sign?  No: it is exactly indefinite, so it cannot be produced by compressing
a projection, which is how the archimedean sign is produced.

CHECK 2 (sec 5.3) -- does mg-aedf's Fuchs constant agree with the asymptotic
Connes states for the same quantity in arXiv:2602.04022 sec 5.4?  It does,
exactly, which closes `citation-audit.md` sec 7 item U4 and corroborates the
index convention settled in `index-convention.md` from a third source.

--- CHECK 1 -------------------------------------------------------------------

The operator V(n) of Connes-Consani, arXiv:2106.01715 Proposition 2.1
(`Spectraltriples.tex:289`, eq. \label{quadratsemi1}),

    <f | V(n) g> = n^{-1/2} ( (f* * g)(n) + (f* * g)(n^{-1}) ),

acting in L^2([lambda^{-1}, lambda], d*u), is *indefinite* -- it has eigenvalues
of both signs -- so the prime contribution -Lambda(n) <f|V(n)f> to QW_lambda
cannot be produced by compressing a projection, which is how the archimedean
sign is produced in arXiv:2006.13771.

Method.  Put x = log u, so L^2([lambda^{-1},lambda], d*u) = L^2([-L/2, L/2], dx)
with L = 2 log lambda = log mu.  Then V(n) = n^{-1/2} (T_a + T_a^*) compressed to
[-L/2, L/2], where a = log n and (T_a g)(x) = g(x + a) with g extended by zero.
In the orthonormal Fourier basis e_k(x) = L^{-1/2} exp(2 pi i k x / L), for
0 < a < L,

    <e_j | T_a e_k> = (1/L) int_{-L/2}^{L/2 - a} exp(2 pi i (k-j) x / L)
                                                 exp(2 pi i k a / L) dx.

Why the truncation is safe.  Restricting to |k| <= N is an orthogonal
compression, and a compression's spectrum lies in the closed convex hull of the
full operator's.  So eigenvalues of both signs in the truncated matrix *prove*
both signs in V(n).  No claim is made in the other direction, and no small
number is being resolved: the entries are O(1) and the eigenvalues reported are
O(1).  Double precision is not load-bearing here (contrast mg-aedf, where it
was).

--- CHECK 2 -------------------------------------------------------------------

mg-aedf takes from Fuchs 1964 (Theorem 1) the asymptotic

    1 - Lambda_n(c) ~ 4 sqrt(pi) 8^n c^{n+1/2} exp(-2c) / n!

(`s3-reduction-audit.md:179`), and `citation-audit.md` sec 7 item U4 records that
the *constant* was never checked against Fuchs' paper -- only the c^{-4} ratio
was checked numerically.  Connes' 2026 survey (arXiv:2602.04022, `rhready.tex`
lines 1149-1150) quotes the same Fuchs theorem for the quantity he calls
1 - chi_2, with chi_k(lambda)^2 = Lambda_{2k}(c), c = 2 pi lambda^2 = 2 pi e^L:

    1 - chi_2 ~ (2^14/3) sqrt(2) pi^5 exp(-4 pi e^L + 9L/2).

His chi_2 is the corpus's chi_4 (prolate index 4 -- `index-convention.md`), and
chi = sqrt(Lambda) gives 1 - chi_2 = (1 - Lambda_4)/2 to leading order.  So the
two expressions are a prediction of each other, and the ratio is a *pure number*
that must come out 1 at every L if both are right.  Nothing about this check is
delicate; it is exact algebra evaluated numerically.
"""

import math

import numpy as np

from verdict import Verdict

# The exit-code contract (mg-5995).  This script already `assert`s the Boas-Kac
# agreement of CHECK 1 and the ratio of CHECK 2, but its own `indef?` column --
# printed `yes`/`NO` -- decided nothing: it could print `NO`, contradicting the
# note's conclusion that every row is indefinite, and still exit 0.  `NO` is
# also excluded from CI's grep, deliberately (README.md), which left that cell
# with no gate at all.
VD = Verdict()


def V_matrix(n, mu, N):
    """Matrix of V(n) in the Fourier basis {e_k : |k| <= N} of L^2([-L/2, L/2])."""
    L = np.log(mu)
    a = np.log(n)
    if a >= L:
        raise ValueError("n must satisfy log n < log mu, i.e. n < mu")
    ks = np.arange(-N, N + 1)
    j = ks[:, None]
    k = ks[None, :]
    d = k - j
    # int_{-L/2}^{L/2-a} exp(2 pi i d x / L) dx
    lo, hi = -L / 2.0, L / 2.0 - a
    w = 2j * np.pi * d / L
    with np.errstate(divide="ignore", invalid="ignore"):
        integ = np.where(
            d == 0,
            (hi - lo) + 0j,
            (np.exp(w * hi) - np.exp(w * lo)) / np.where(d == 0, 1, w),
        )
    T = np.exp(2j * np.pi * k * a / L) * integ / L
    return n ** -0.5 * (T + T.conj().T)


def even_isometry(N):
    """Columns: the even (under u -> u^{-1}, i.e. x -> -x) subspace, in the e_k basis."""
    cols = []
    for k in range(0, N + 1):
        v = np.zeros(2 * N + 1, dtype=complex)
        if k == 0:
            v[N] = 1.0
        else:
            v[N + k] = v[N - k] = 2 ** -0.5
        cols.append(v)
    return np.stack(cols, axis=1)


def report(n, mu, N=200, even_only=False):
    M = V_matrix(n, mu, N)
    assert np.allclose(M, M.conj().T), "V(n) must be self-adjoint"
    if even_only:
        W = even_isometry(N)
        M = W.conj().T @ M @ W
    ev = np.linalg.eigvalsh(M)
    return ev.min(), ev.max()


def fuchs_ours(L, n=4):
    """1 - chi_{n/2}, from mg-aedf's Fuchs constant, via 1 - chi = (1 - Lambda)/2."""
    c = 2 * np.pi * np.exp(L)
    one_minus_Lambda = (4 * np.sqrt(np.pi) * 8 ** n * c ** (n + 0.5)
                        * np.exp(-2 * c) / math.factorial(n))
    return one_minus_Lambda / 2


def fuchs_connes(L):
    """1 - chi_2, as stated in arXiv:2602.04022 sec 5.4."""
    return (2 ** 14 / 3) * np.sqrt(2) * np.pi ** 5 * np.exp(-4 * np.pi * np.exp(L) + 4.5 * L)


def check2():
    print()
    print("CHECK 2 -- mg-aedf's Fuchs constant vs Connes' 1 - chi_2 (arXiv:2602.04022)")
    print()
    print(f"{'L':>5} {'c=2 pi e^L':>12} {'ours':>14} {'Connes':>14} {'ratio':>16}")
    worst = 0.0
    for L in (1.0, 1.5, 2.0, 2.5, 3.0):
        a, b = fuchs_ours(L), fuchs_connes(L)
        worst = max(worst, abs(a / b - 1.0))
        print(f"{L:>5.1f} {2 * np.pi * np.exp(L):>12.4f} {a:>14.6e} {b:>14.6e} {a / b:>16.12f}")
    assert worst < 1e-12, worst
    print()
    print("Ratio 1 to 12 decimals at every L: the two constants are the same constant.")
    print("This closes citation-audit.md sec 7 item U4 (the Fuchs constant, never")
    print("checked against Fuchs) by a third-party route, and corroborates the index")
    print("convention of index-convention.md: Connes' chi_2 is the corpus's chi_4.")


if __name__ == "__main__":
    print("CHECK 1 -- sign of the prime term")
    print()
    print("V(n) on L^2([mu^{-1/2}, mu^{1/2}], d*u), Fourier truncation |k|<=200")
    print("symbol range on the line: [-2 n^{-1/2}, +2 n^{-1/2}]")
    print()
    print(f"{'n':>3} {'mu':>6} {'min eig':>12} {'max eig':>12}"
          f" {'min (even)':>12} {'max (even)':>12}  {'Boas-Kac':>10}  indef?")
    for n, mu in [(2, 3.0), (2, 4.0), (2, 7.0), (2, 11.0),
                  (3, 4.0), (3, 7.0), (3, 11.0),
                  (4, 7.0), (5, 7.0), (5, 11.0), (7, 11.0)]:
        lo, hi = report(n, mu)
        elo, ehi = report(n, mu, even_only=True)
        # Boas-Kac, as used in arXiv:2006.13771 at `weil-compo.tex:842`
        # (Remark \label{improve}, with the ceiling-function correction): with
        # m + 1 = ceil(L / log n) the largest number of points of an orbit
        # x + (log n) Z inside the interval, the extreme eigenvalues are
        # 2 n^{-1/2} cos(pi / (m + 2)).
        m = int(np.ceil(np.log(mu) / np.log(n))) - 1
        bk = 2 * n ** -0.5 * np.cos(np.pi / (m + 2))
        ok = lo < 0 < hi and elo < 0 < ehi
        VD.check(ok, "CHECK 1: V(n) indefinite on both the full space and the "
                 "even sector (n=%d, mu=%.1f)" % (n, mu))
        # "the spectrum is exactly symmetric about 0.  It is, to 1e-15."
        VD.check(abs(lo + hi) < 1e-12,
                 "CHECK 1: full-space spectrum symmetric about 0 "
                 "(n=%d, mu=%.1f)" % (n, mu))
        assert abs(hi - bk) < 1e-6, (n, mu, hi, bk)
        print(f"{n:>3} {mu:>6.1f} {lo:>12.6f} {hi:>12.6f} {elo:>12.6f} {ehi:>12.6f}"
              f"  {bk:>10.6f}  {'yes' if ok else 'NO'}")
    print()
    print("Every row indefinite, on the full space and on the even sector that")
    print("carries Connes-Consani's matrix sigma^+ => the prime term is not of one")
    print("sign, at any of these scales, for any test function class -- before any")
    print("support or vanishing condition is imposed.")
    print()
    print("The full-space columns are also a check of an exact statement (see")
    print("`semilocal-gap.md` §3.2): multiplication by exp(i pi x / log n) is a")
    print("unitary of L^2([-L/2,L/2]) conjugating V(n) into -V(n), so the spectrum")
    print("is exactly symmetric about 0.  It is, to 1e-15.  The 'Boas-Kac' column is")
    print("2 n^{-1/2} cos(pi/(m+2)), m = ceil(L/log n) - 1, the bound the archimedean")
    print("paper itself uses at `weil-compo.tex:842` of arXiv:2006.13771; the asserts")
    print("above check the computed extreme eigenvalues against it.")
    check2()
    VD.finish()
