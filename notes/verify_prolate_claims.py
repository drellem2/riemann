"""
Numerical audit of the prolate facts underlying s3.tex items (i)-(iii) and
start.tex:171, :178-186.  Companion to notes/s3-reduction-audit.md (mg-aedf).

Requires numpy.  Run:  python3 verify_prolate_claims.py

SETUP (classical Slepian).  Band-limit c, time interval [-1,1].  Concentration
operator  (Q f)(x) = int_{-1}^{1} sin(c(x-y)) / (pi (x-y)) f(y) dy,  eigenvalues
lam_0 > lam_1 > ... in (0,1), eigenfunctions psi_n orthonormal on [-1,1].

The documents' chi_n is sqrt(lam_n).  That is forced two ways: s3.tex:64-66
writes the leakage as 1-chi_n^2 where the true leakage is 1-lam_n, and
start.tex:180-181 only reproduces under chi_n = sqrt(lam_n) (test C below,
which matches to 8 digits).

WHAT IS CHECKED
  A  double orthogonality => the Pythagoras identity s3.tex:62-67   [exact, analytic]
  B  finite-Fourier eigenrelation  int_{-1}^{1} psi_n = mu_n psi_n(0),
     mu_n = i^n sqrt(2 pi lam_n / c)                                [Slepian-Pollak]
  C  start.tex:180-181  h_lam(0) = alpha psi_0(0) (chi_4-chi_0)/chi_4,
     derived from  hat h_lam(0) = 0  alone
  D  (1-lam_0)/(1-lam_4) ~ (4!/8^4) c^-4                            [Fuchs/Slepian]
  E  psi_4(0)/psi_0(0) -> sqrt(3/8)                                 [fixed-n Hermite limit]
  F  |beta|^2 -> 8/11 and  ||(1-P)h_lam||^2 / (1-lam_4) -> 8/11
  G  the pair {0,4} vs {0,2}: why index 4 is forced
  H  psi_0(0) ~ (2c/pi)^{1/4}: the constant in h_lam(0)=O(1-chi_4) is NOT uniform
  I  double-precision working window for any numerical sign computation
"""
import numpy as np

from verdict import Verdict

# The exit-code contract (mg-5995).  Test B prints its own expectation on the
# same line (`expect +1 both`), and the Legendre-route table states the sign law
# r_0, r_4 > 0 and r_2 < 0 "at every c"; those are wired.  Tests C--H are
# convergences towards printed limits with no threshold stated, and test I is
# the record of where the sinc route STOPS working -- the c = 20 row of table G
# is a documented breakdown, not a failure -- so none of those are wired.
VD = Verdict()

N = 900  # Gauss-Legendre nodes


def _kernel(x, y, c):
    d = x[:, None] - y[None, :]
    return np.where(np.abs(d) < 1e-13, c / np.pi,
                    np.sin(c * d) / (np.pi * np.where(d == 0, 1, d)))


def prolate(c, nmax=6):
    """Return (lam, psi_at_0, integrals) for the first nmax prolates."""
    x, w = np.polynomial.legendre.leggauss(N)
    A = np.sqrt(w)[:, None] * _kernel(x, x, c) * np.sqrt(w)[None, :]
    lam, V = np.linalg.eigh(A)
    idx = np.argsort(lam)[::-1][:nmax]
    lam, V = lam[idx], V[:, idx]
    psi = V / np.sqrt(w)[:, None]
    for n in range(nmax):                      # convention: psi_n(1) > 0
        if psi[-1, n] < 0:
            psi[:, n] *= -1
    k0 = _kernel(np.array([0.0]), x, c)[0]
    psi_0 = (k0 * w) @ psi / lam               # psi_n(0), via the kernel (no interpolation)
    return lam, psi_0, w @ psi                 # lam, psi_n(0), int psi_n


def pair(lam, psi_0, integ, m):
    """Coefficients forced by hat h(0)=0 for h = alpha psi_0 + beta psi_m, ||h||=1."""
    ba = -integ[0] / integ[m]
    a = 1.0 / np.sqrt(1 + ba ** 2)
    b = ba * a
    h0 = a * psi_0[0] + b * psi_0[m]
    leak = a ** 2 * (1 - lam[0]) + b ** 2 * (1 - lam[m])
    return a, b, h0, leak


print(__doc__.split("WHAT IS CHECKED")[0])
print("=" * 118)
print("B, C, D, E, F  --  the pair {0,4}")
print(f"{'c':>4} {'1-lam_0':>11} {'1-lam_4':>11} {'ratio':>10} {'D: 24/4096c^4':>14}"
      f" {'E: psi4/psi0':>13} {'F: |beta|^2':>12} {'F: leak/(1-l4)':>15} {'C: ratio':>11}")
for c in [4, 6, 8, 10, 12, 14]:
    lam, psi_0, integ = prolate(c)
    chi = np.sqrt(lam)
    a, b, h0, leak = pair(lam, psi_0, integ, 4)
    c_pred = a * psi_0[0] * (chi[4] - chi[0]) / chi[4]
    mu = [integ[n] / psi_0[n] / np.sqrt(2 * np.pi * lam[n] / c) for n in (0, 4)]
    print(f"{c:>4} {1-lam[0]:>11.3e} {1-lam[4]:>11.3e} {(1-lam[0])/(1-lam[4]):>10.3e}"
          f" {24/4096/c**4:>14.3e} {psi_0[4]/psi_0[0]:>13.6f} {b**2:>12.6f}"
          f" {leak/(1-lam[4]):>15.6f} {h0/c_pred:>11.8f}")
    # B is the Slepian-Pollak eigenrelation and the line prints its own
    # expectation: both entries are +1.00000000 at every c on this grid.
    for n, v in zip((0, 4), mu):
        VD.check(abs(v - 1) < 1e-6, "B: mu_%d / sqrt(2 pi lam_%d / c) = +1 (c=%d)"
                                    % (n, n, c))
    print(f"     B: mu_n / sqrt(2 pi lam_n / c) = {mu[0]:+.8f} (n=0), {mu[1]:+.8f} (n=4)"
          f"   [expect +1 both, since i^0 = i^4 = +1]")

print(f"\n  predicted limits:  E -> sqrt(3/8) = {np.sqrt(3/8):.6f};"
      f"  F -> 8/11 = {8/11:.6f};  C ratio -> 1")

print("\n" + "=" * 118)
print("G  --  why index 4 and not 2.  Same constraint hat h(0)=0 imposed in both columns.")
print(f"{'c':>4} {'2c/pi':>7} | {'{0,2}: |h(0)|':>14} {'leak':>11} | {'{0,4}: |h(0)|':>14}"
      f" {'leak':>11} | {'H: psi_0(0)':>12} {'psi_0(0)/c^.25':>15}")
for c in [8, 10, 12, 14, 16, 20]:
    lam, psi_0, integ = prolate(c)
    _, _, h2, lk2 = pair(lam, psi_0, integ, 2)
    _, _, h4, lk4 = pair(lam, psi_0, integ, 4)
    print(f"{c:>4} {2*c/np.pi:>7.2f} | {abs(h2):>14.4e} {lk2:>11.4e} | {abs(h4):>14.4e}"
          f" {lk4:>11.4e} | {psi_0[0]:>12.4f} {psi_0[0]/c**0.25:>15.4f}")
print(f"  H: psi_0(0) ~ (c/pi)^(1/4), i.e. psi_0(0)/c^(1/4) -> pi^(-1/4) = {np.pi**-0.25:.4f}")
print("     (prolate ODE degenerates to the oscillator u'' + (chi - c^2 x^2)u = 0, scale sqrt(c))")

print("""
The sinc-kernel route above CANNOT be pushed to large c: once 2c/pi modes have
lam_n = 1 - O(1e-17), eigh returns an arbitrary rotation inside that numerically
degenerate cluster, so the eigenVECTORS are junk too, not just the eigenvalues.
(At c=30 it reports psi_4(0)/psi_0(0) = 7.88; at c=120, 39.7.  Both meaningless.)

For E, H and |beta|^2 at large c use the Legendre/Bouwkamp route instead: the
prolate differential operator L_c has WELL-SEPARATED eigenvalues chi_n ~ n^2,
so its eigenvectors are stable at any c.  (This is the same L_c whose commutator
[L_c, P] = 0 is invoked at start.tex:264-273.)  It is also the route that ports
to extended precision without difficulty.
""")


def prolate_legendre(c, nmax=6, K=400):
    """psi_n via L_c in the normalized-Legendre basis. Returns psi_n(0), int psi_n, d_0.

    L_c in basis Pbar_k = sqrt((2k+1)/2) P_k is symmetric, banded at offset 2:
        A[k,k]   = k(k+1) + c^2 (2k(k+1)-1)/((2k-1)(2k+3))
        A[k,k+2] = c^2 (k+2)(k+1) / ((2k+3) sqrt((2k+1)(2k+5)))
    """
    k = np.arange(K, dtype=float)
    diag = k * (k + 1) + c**2 * (2 * k * (k + 1) - 1) / ((2 * k - 1) * (2 * k + 3))
    ku = k[:-2]
    off = c**2 * (ku + 2) * (ku + 1) / ((2 * ku + 3) * np.sqrt((2 * ku + 1) * (2 * ku + 5)))
    A = np.diag(diag) + np.diag(off, 2) + np.diag(off, -2)
    chi, D = np.linalg.eigh(A)                      # chi_n increasing == prolate order
    D = D[:, np.argsort(chi)][:, :nmax]
    # Pbar_k(0): 0 for odd k; P_{2m}(0) = (-1)^m C(2m,m)/4^m
    pk0 = np.zeros(K)                               # P_{2m}(0) by recurrence (no overflow)
    v = 1.0
    for mm in range(K // 2 + K % 2):
        pk0[2 * mm] = v
        v *= -(2 * mm + 1) / (2 * mm + 2)
    pk0 *= np.sqrt((2 * np.arange(K) + 1) / 2)
    for n in range(nmax):                           # convention: d_0 > 0, i.e. int psi_n > 0
        if D[0, n] < 0:
            D[:, n] *= -1
    psi_0 = pk0 @ D                                 # psi_n(0)
    integ = np.sqrt(2.0) * D[0, :]                  # int_{-1}^{1} psi_n = sqrt(2) d_0
    return psi_0, integ


print(f"{'c':>5} {'E: psi_4(0)/psi_0(0)':>21} {'H: psi_0(0)/c^(1/4)':>21} {'|beta/alpha|':>13} {'|beta|^2':>10}")
for c in [10, 20, 50, 100, 200, 400]:
    psi_0, integ = prolate_legendre(c, K=max(400, 4 * c))
    ba = abs(integ[0] / integ[4])
    print(f"{c:>5} {psi_0[4]/psi_0[0]:>21.6f} {psi_0[0]/c**0.25:>21.6f}"
          f" {ba:>13.6f} {ba**2/(1+ba**2):>10.6f}")
print(f"   limits: sqrt(3/8) = {np.sqrt(3/8):.6f},  pi^(-1/4) = {np.pi**-0.25:.6f},"
      f"  sqrt(8/3) = {np.sqrt(8/3):.6f},  8/11 = {8/11:.6f}")

print("""
G, convention-free.  r_n := (int psi_n) / psi_n(0) is independent of how each
eigenvector's sign is fixed, and r_n = mu_n = i^n sqrt(2 pi lam_n / c).  So the
SIGN of r_n is exactly the finite-Fourier phase i^n that selects the mode.""")
print(f"{'c':>5} {'r_0':>12} {'r_2':>12} {'r_4':>12} {'sqrt(2pi/c)':>13}")
for c in [10, 20, 50, 100, 200, 400]:
    psi_0, integ = prolate_legendre(c, K=max(400, 4 * c))
    r = integ / psi_0
    # the line printed below the table: the finite-Fourier phase i^n.
    VD.check(r[0] > 0 and r[4] > 0 and r[2] < 0,
             "G: r_0, r_4 > 0 and r_2 < 0 (c=%d)" % c)
    print(f"{c:>5} {r[0]:>12.6f} {r[2]:>12.6f} {r[4]:>12.6f} {np.sqrt(2*np.pi/c):>13.6f}")
print("   r_0, r_4 > 0 and r_2 < 0 at every c: i^0 = i^4 = +1, i^2 = -1.")
print("""
  mu_n = i^n |mu_n|, so mu_0, mu_4 > 0 but mu_2 < 0.  Imposing hat h(0)=0 gives
      m = 4:  h(0) = alpha psi_0(0) (chi_4 - chi_0)/chi_4  ~ -alpha psi_0(0)(1-chi_4)   [cancels]
      m = 2:  h(0) = alpha psi_0(0) (chi_2 + chi_0)/chi_2  ~  2 alpha psi_0(0)          [reinforces]
  Index 4 is the least-leaky even prolate whose finite-Fourier phase matches mode 0.
  This is Slepian-Pollak, not geometry.

I  --  double-precision working window.  Column 'C: ratio' above is 1.0 to 8 digits for
  c <= 12, drifts by ~1e-4 at c=14, is ~10% wrong at c=16 and meaningless at c=20:
  1-lam_0 ~ e^{-2c} underflows relative to lam_0 ~ 1.  Usable window is roughly
  10 <= c <= 14 (mode 4 needs 2c/pi > 5, i.e. c > 7.9, to be inside the plateau at all).
  Any numerical determination of sign(C_lambda) needs extended precision, or 1-lam_n
  computed directly rather than by subtraction.
""")

print("=" * 118)
print("""A  --  Pythagoras premise (analytic, no numerics needed).
  psi_n supported in [-1,1], B = band-limiting projection, DBD psi_n = lam_n psi_n:
     <(1-B)psi_0, (1-B)psi_4> = <psi_0,psi_4> - <B psi_0, psi_4>
                              = 0 - lam_0 <psi_0,psi_4> = 0.
  So s3.tex:62-67 is exactly the double orthogonality of the prolates.  It needs no
  hypothesis about which modes occur and no S^3 input.
  Consequence: the UPPER half of s3.tex:75-77 is free --
     ||(1-P)h_lam||^2 = |a|^2(1-lam_0) + |b|^2(1-lam_4) <= 1-lam_4   since lam_0 > lam_4.
  Only the LOWER bound needs a uniformity claim, namely |b_lam| bounded below.
""")

VD.finish()
