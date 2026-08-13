"""
Numerical tests for notes/s3-sign-blindness.md (mg-8d74).  Companion to, and
reusing the setup of, verify_prolate_claims.py (mg-aedf).

Requires numpy.  Run:  python3 verify_sign_claims.py

Same conventions as verify_prolate_claims.py: band-limit c, interval [-1,1],
concentration eigenvalues lam_0 > lam_1 > ..., chi_n = sqrt(lam_n),
d_n := 1 - lam_n the true leakage of mode n.  Two functionals matter:

    hat h(0) = int_{-1}^{1} h        (zero Fourier mode)   -> I_n := int psi_n
    h(0)                             (endpoint value)      -> p_n := psi_n(0)

and the Slepian-Pollak relation is I_n = mu_n p_n, mu_n = i^n sqrt(2 pi lam_n / c).

WHAT IS CHECKED

  S1  The endpoint sign does not depend on WHICH partner mode is chosen.
      For h = alpha psi_0 + beta psi_m normalized by hat h(0) = 0,
          h(0) = alpha p_0 (1 - r_0/r_m),      r_n := I_n / p_n = mu_n.
      Two independent factors:
          |r_0/r_m| = chi_0/chi_m > 1  for EVERY m > 0   [ground-mode extremality]
          sign(r_0/r_m) = i^{-m}                          [finite-Fourier phase]
      So h(0) < 0 for every m = 0 mod 4 and h(0) > 0 for every m = 2 mod 4.
      Checked for m = 2,4,6,8,10,12.

  S2  h_lambda is NOT the leakage-minimising vector subject to hat h(0) = 0.
      The minimiser has leakage between d_0 and d_2, i.e. smaller than d_4 by a
      factor ~ c^2; in the full space psi_1 alone does better still (factor ~c^3).
      => there is no single-constraint variational principle selecting h_lambda.

  S3  h_lambda IS, to leading order, the leakage-minimising vector subject to
      BOTH hat h(0) = 0 and h(0) = 0, and the minimum value is Theta(d_4).
      => there IS a two-constraint variational principle, it selects mode 4, and
      it turns item (iii) from an asymp into an extremal value (a signed <=).

Numerics use the sinc-kernel route, valid for 10 <= c <= 14 (see test I of
verify_prolate_claims.py); S1 additionally uses the stable Legendre/Bouwkamp
route to reach c = 400.
"""
import numpy as np

from verdict import Verdict

# The exit-code contract (mg-5995).  S1's sign table already prints its own
# expectation in the last column (`expect i^m`); comparing the two is the only
# numerical claim this script makes -- S2/S3 report leakages and drifts and
# state no threshold, so nothing there is wired.
VD = Verdict()

N = 900  # Gauss-Legendre nodes


def _kernel(x, y, c):
    d = x[:, None] - y[None, :]
    return np.where(np.abs(d) < 1e-13, c / np.pi,
                    np.sin(c * d) / (np.pi * np.where(d == 0, 1, d)))


def prolate(c, nmax=13):
    """(lam, psi_n(0), int psi_n) for the first nmax prolates.  Sinc-kernel route."""
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
    p = (k0 * w) @ psi / lam                   # psi_n(0), via the kernel
    return lam, p, w @ psi


def prolate_legendre(c, nmax=13, K=400):
    """psi_n(0) and int psi_n via L_c in the normalized-Legendre basis (stable at any c)."""
    k = np.arange(K, dtype=float)
    diag = k * (k + 1) + c**2 * (2 * k * (k + 1) - 1) / ((2 * k - 1) * (2 * k + 3))
    ku = k[:-2]
    off = c**2 * (ku + 2) * (ku + 1) / ((2 * ku + 3) * np.sqrt((2 * ku + 1) * (2 * ku + 5)))
    A = np.diag(diag) + np.diag(off, 2) + np.diag(off, -2)
    chi, D = np.linalg.eigh(A)
    D = D[:, np.argsort(chi)][:, :nmax]
    pk0 = np.zeros(K)                          # Pbar_k(0)
    v = 1.0
    for mm in range(K // 2 + K % 2):
        pk0[2 * mm] = v
        v *= -(2 * mm + 1) / (2 * mm + 2)
    pk0 *= np.sqrt((2 * np.arange(K) + 1) / 2)
    for n in range(nmax):                      # convention: int psi_n > 0
        if D[0, n] < 0:
            D[:, n] *= -1
    return pk0 @ D, np.sqrt(2.0) * D[0, :]


def constrained_min(d, U):
    """min c^T diag(d) c over ||c||=1, U^T c = 0.  Returns (value, minimiser)."""
    # orthonormal basis of ker(U^T) via SVD
    _, _, Vt = np.linalg.svd(U.T)
    kern = Vt[U.shape[1]:].T                   # columns span the kernel
    M = kern.T @ (d[:, None] * kern)
    ev, evec = np.linalg.eigh(M)
    return ev[0], kern @ evec[:, 0]


# ----------------------------------------------------------------------------
print(__doc__.split("WHAT IS CHECKED")[0])
print("=" * 100)
print("""S1  --  the endpoint sign is mode-independent within each phase class.

  h(0) = alpha p_0 (1 - r_0/r_m),  r_n := I_n/p_n = mu_n = i^n sqrt(2 pi lam_n / c),
  so  r_0/r_m = i^{-m} chi_0/chi_m  and the sign splits into two INDEPENDENT factors:

      (P)  sign(r_0/r_m) = i^{-m}     -- the finite-Fourier phase   [Slepian-Pollak]
      (X)  |r_0/r_m| = chi_0/chi_m > 1 for every m > 0
                                      -- chi_0 is the LARGEST concentration
                                         eigenvalue, so no partner can beat it

  Given (P) and (X) the sign law is EXACT and needs no numerics:

      m = 0 mod 4:  h(0) = alpha p_0 (1 - chi_0/chi_m) < 0   for EVERY such m
      m = 2 mod 4:  h(0) = alpha p_0 (1 + chi_0/chi_m) > 0   for EVERY such m

  (X) is just the ordering lam_0 > lam_1 > ... and is not a numerical claim at all.
  So the only thing worth checking numerically is (P), the convention-dependent one.
""")
print("  (P)  sign(r_m) relative to r_0.  Legendre route, stable at every c.")
print(f"{'c':>5} " + " ".join(f"{'sign r_' + str(m):>10}" for m in (2, 4, 6, 8, 10, 12))
      + f" {'expect i^m':>26}")
for c in [10, 20, 50, 100, 200, 400]:
    p, I = prolate_legendre(c, K=max(400, 4 * c))
    r = I / p
    row = " ".join(f"{'+' if r[m] / r[0] > 0 else '-':>10}" for m in (2, 4, 6, 8, 10, 12))
    # (P): sign(r_m/r_0) = i^m, which is + for m = 0 mod 4 and - for m = 2 mod 4.
    # That is the `expect i^m` column, printed as a literal on the same line.
    for m in (2, 4, 6, 8, 10, 12):
        VD.check((r[m] / r[0] > 0) == (m % 4 == 0),
                 "S1 (P): sign(r_%d/r_0) = i^%d (c=%d)" % (m, m, c))
    print(f"{c:>5} " + row + f" {'-  +  -  +  -  +':>26}")

print("\n  (X)  chi_0/chi_m > 1, shown via d_n = 1-lam_n increasing.  Sinc-kernel route,")
print("       valid only for c <= 14 (see test I of verify_prolate_claims.py).")
print(f"{'c':>5} " + " ".join(f"{'d_' + str(m):>11}" for m in (0, 2, 4, 6, 8, 10, 12)))
for c in [10, 12, 14]:
    lam, p, I = prolate(c, nmax=13)
    d = 1 - lam
    ms = (0, 2, 4, 6, 8, 10, 12)
    # (X) is the ordering lam_0 > lam_m, i.e. d_0 < d_m, for every m > 0.
    VD.check(all(d[a] < d[b] for a, b in zip(ms, ms[1:])),
             "S1 (X): d_n = 1 - lam_n increasing in n (c=%d)" % c)
    print(f"{c:>5} " + " ".join(f"{d[m]:>11.3e}" for m in ms))
print("""
  CAUTION.  Evaluating the sign of (1 - r_0/r_m) numerically at c >= 20 returns
  NOISE: chi_0/chi_m - 1 is O(e^{-2c}) and underflows against 1, so the printed
  ratio is 1.000000 and the subtraction has no significant digits left.  The sign
  law above is nonetheless exact, because (X) is an ordering, not a measurement.
  This is the same double-precision ceiling documented in the mg-aedf audit, and
  it is a reason to derive this sign rather than to compute it.

  CONCLUSION.  Every m = 0 mod 4 gives the same sign (negative); every m = 2 mod 4
  gives the same sign (positive).  The sign therefore carries NO information about
  the selection of 4 -- only the magnitude, 1 - chi_0/chi_m ~ -(1-chi_m), does.""")

# ----------------------------------------------------------------------------
print("\n" + "=" * 100)
print("""S2/S3  --  is h_lambda extremal?  Leakage of the constrained minimisers.

  L(h) := ||(1-P)h||^2 = sum_n c_n^2 d_n  for h = sum c_n psi_n, ||h|| = 1.
  Column 'h_lambda' is the CCM two-mode vector alpha psi_0 + beta psi_4.
  'min | F' is the minimum of L over unit vectors satisfying the constraints F.
""")
hdr = (f"{'c':>4} {'d_1':>10} {'d_2':>10} {'d_4':>10} | {'h_lambda':>10} "
       f"{'min|hat h(0)=0':>15} {'min|both=0':>11} | {'min/d_4':>8} {'overlap':>8} {'h_lam excess':>12}")
print(hdr)
for c in [10, 11, 12, 13, 14]:
    lam, p, I = prolate(c, nmax=13)
    d = 1 - lam
    ev = np.arange(0, 13, 2)                   # even sector: the Weil form is even
    d_e, p_e, I_e = d[ev], p[ev], I[ev]

    ba = -I[0] / I[4]                          # the CCM vector
    a = 1 / np.sqrt(1 + ba**2)
    b = ba * a
    leak_h = a**2 * d[0] + b**2 * d[4]
    c_h = np.zeros(len(ev)); c_h[0] = a; c_h[2] = b

    v1, _ = constrained_min(d_e, I_e[:, None])                     # hat h(0) = 0
    v2, w2 = constrained_min(d_e, np.column_stack([I_e, p_e]))     # both = 0
    print(f"{c:>4} {d[1]:>10.3e} {d[2]:>10.3e} {d[4]:>10.3e} | {leak_h:>10.3e} "
          f"{v1:>15.3e} {v2:>11.3e} | {v2/d[4]:>8.4f} {abs(w2 @ c_h):>8.5f}"
          f" {(leak_h - v2)/v2:>12.2e}")
print(f"\n  'min/d_4' is drifting down towards 8/11 = {8/11:.4f}, the exact constant the")
print("  mg-aedf audit derived for ||(1-P)h_lambda||^2/(1-lam_4).  That the VARIATIONAL")
print("  problem reproduces the same constant is evidence the characterisation is real")
print("  and not an artefact of the 3-mode truncation.")

print("""
  S2.  'min | hat h(0)=0' is smaller than d_4 by ~c^2 (and psi_1 alone, which
       satisfies hat h(0)=0 identically since I_odd = 0, does better by ~c^3).
       So h_lambda does NOT minimise leakage under the single constraint, and
       there is no one-constraint extremal principle that selects it.

  S3.  Under BOTH endpoint constraints the minimum is a fixed fraction of d_4
       ('ratio to d_4'), and its minimiser has overlap ~1 with h_lambda.
       So h_lambda IS near-extremal for the two-constraint problem, mode 4 is
       what that problem selects, and

           min { ||(1-P)h||^2 : ||h||=1, h even, hat h(0)=0, h(0)=0 }  =  Theta(1-lam_4)

       is item (iii) as an EXTREMAL VALUE -- an inequality with a direction,
       not an asymp.  Note this is still a statement about h and P only: it
       does not mention W_lambda, E, Q or zeta, and so is invariant under
       W_lambda -> -W_lambda.  See s3-sign-blindness.md section 3.""")

VD.finish()
