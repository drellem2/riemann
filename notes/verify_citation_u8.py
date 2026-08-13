#!/usr/bin/env python3
"""One check for `citation-audit.md` sec 7 item U8 (work item mg-882b).  Needs `mpmath`.

Imports `Lambda_even` from [`verify_prolate_rate.py`](verify_prolate_rate.py), so the
prolate eigenvalues on the left are produced by machinery that has never seen the
dictionary being tested.

--- WHAT U8 ASKS ---------------------------------------------------------------

`citation-audit.md` sec 5 argues, from the two definitions and not from any printed
statement, that

    c_ours  =  gamma  =  2 pi lambda^2  =  2 pi c_Groskin ,

and the U8 row records "Neither paper states it.  One numerical check would settle
it."  The claim factors into two independent halves, and they close differently:

  (a)  c_Groskin = lambda^2 = mu.       BIBLIOGRAPHIC -- and Groskin *does* state it.
       arXiv:2605.20224, `main.tex:284-287` ("For a cutoff parameter c (controlling
       the primes p <= c ...), set L = log c.  The quadratic form acts on
       L^2([0,L])"), `:433` ("adopt the convention lambda^2 = c from CCM
       throughout"), and `:1095` ("With lambda^2 = c, this is L = log c, so
       e^L = c").  Nothing here is left for a numerical check; sec 5's parenthetical
       "neither paper states it" is simply wrong about this half.

  (b)  c_ours = 2 pi mu.                THE FACTOR 2 pi.  This is what is checked
       below.  It is a statement about *our* scripts' convention -- the c in
       ((1-x^2) psi')' + (chi - c^2 x^2) psi = 0 -- measured against a quantity
       Connes states as a function of lambda alone.

--- THE CHECK ------------------------------------------------------------------

Connes (arXiv:2602.04022, `rhready.tex:1149`) states, for the *angular function*
1 - chi_2(lambda) and in terms of L = 2 log lambda = log mu,

    1 - chi_2  ~  (2^14/3) sqrt2 pi^5 e^{-4 pi e^L + 9L/2}
               =  (2^14/3) sqrt2 pi^5 mu^{9/2} e^{-4 pi mu}   =:  A(mu),

a function of mu with NO free scale in it.  His chi_2 is prolate index 4
([`index-convention.md`](index-convention.md)), so on our side the same quantity is
1 - sqrt(Lambda_4(c)) -- and the only thing linking the two is the convention
c = kappa * mu whose kappa is under test.  So compute, for a grid of mu and a list
of candidate kappa,

    M(kappa, mu)  :=  1 - sqrt( Lambda_4(kappa * mu) )          [measured]

and report log10( M / A ).  If kappa = 2 pi is right the ratio is O(1) at every mu
and flat; any other kappa is off by a factor e^{2(2 pi - kappa) mu}, i.e. tens of
orders of magnitude that grow with mu.  This check therefore does not merely fail
to contradict 2 pi -- it excludes every neighbour.

Independently, and after the fact: Connes' own footnote on the same line says
"chi_k(lambda)^2 = lambda_{2k}(a) with a = sqrt(2 pi) lambda in the notations of
this theorem", i.e. the Fuchs-convention bandwidth is a^2 = 2 pi lambda^2.  The
factor is therefore *also* stated, in a footnote, by the survey sec 6 of this note
already told us to read.  The measurement below and that footnote are independent
and agree, which is why U8 closes rather than narrowing.

--- WHAT THIS CHECK CANNOT DO --------------------------------------------------

It tests our c against CONNES' lambda.  The bridge to GROSKIN's c is (a) above and
is documentary, not measured: no computation here touches the CvS Galerkin matrix.
A reader who doubts Groskin's `:433` should doubt the composite claim, not this
check.

Working precision is stated per row and the Legendre truncation K is reported; both
are varied in the last block so that the reported digits are the ones that are
stable, not the ones mpmath happened to print.
"""

import os
import sys

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verdict import Verdict  # noqa: E402
from verify_prolate_rate import Lambda_even  # noqa: E402

# The exit-code contract (mg-5995).  The check is a CONTRAST, and the script
# says what it has to look like: |log10 ratio| is O(1) at kappa = 2 pi (measured
# 0.15 down to 0.057) and "tens of orders of magnitude" away at every other
# kappa (measured 9.2 to 53).  Both halves are wired, at 1 and at 5 -- an order
# of magnitude of slack on each side of a gap that is eight wide.  The last
# block's claim that the digits do not move is wired as printed: same 12 digits.
VD = Verdict()


def connes_A(mu):
    """(2^14/3) sqrt2 pi^5 mu^{9/2} e^{-4 pi mu}  --  arXiv:2602.04022 rhready.tex:1149."""
    mu = mp.mpf(mu)
    return (mp.mpf(2) ** 14 / 3) * mp.sqrt(2) * mp.pi ** 5 * mu ** mp.mpf(4.5) * mp.exp(-4 * mp.pi * mu)


def measured(kappa, mu, K=None):
    """1 - sqrt(Lambda_4(kappa * mu)), from the Legendre-coefficient eigensolver."""
    c = mp.mpf(kappa) * mp.mpf(mu)
    L = dict(Lambda_even(c, 2, K))
    return 1 - mp.sqrt(L[4])


MUS = [4, 6, 8, 10]


def kappa_values():
    return [("1", mp.mpf(1)), ("2", mp.mpf(2)), ("pi", mp.pi),
            ("2*pi", 2 * mp.pi), ("4*pi", 4 * mp.pi)]


def main():
    mp.mp.dps = 320
    print("=" * 96)
    print("U8 -- the scale factor in c_ours = kappa * mu")
    print(f"working precision: mp.dps = {mp.mp.dps}")
    print()
    print("log10 [ (1 - sqrt(Lambda_4(kappa*mu))) / A(mu) ],  A = Connes' asymptotic, "
          "rhready.tex:1149")
    print("A ratio of 1 (log10 = 0) means the convention is right.")
    print()
    hdr = f"{'kappa':>8} " + " ".join(f"{'mu=' + str(m):>14}" for m in MUS)
    print(hdr)
    print("-" * len(hdr))
    for name, kap in kappa_values():
        row = f"{name:>8} "
        for mu in MUS:
            c = kap * mp.mpf(mu)
            K = int(c) + 90
            m = measured(kap, mu, K)
            r = m / connes_A(mu)
            lg = abs(mp.log10(r))
            if name == "2*pi":
                VD.check(lg < 1, "U8: |log10 ratio| = O(1) at kappa = 2 pi (mu=%d)" % mu)
            else:
                VD.check(lg > 5, "U8: kappa = %s excluded by orders of magnitude "
                                 "(mu=%d)" % (name, mu))
            row += f"{mp.nstr(mp.log10(r), 8):>15}"
        print(row)
    print()
    print("Read the 2*pi row against every other: the ratio is O(1) and flat only there.")
    print("The others are off by e^{2(2pi - kappa) mu}, growing with mu -- so the check")
    print("does not merely admit 2 pi, it excludes 2, pi and 4 pi by tens of orders of")
    print("magnitude at every mu on the grid.")
    print()

    print("=" * 96)
    print("The 2*pi row, in full, with the asymptotic's own O(1/c) error visible")
    print()
    print(f"{'mu':>5} {'c = 2 pi mu':>14} {'K':>6} {'measured 1-chi_2':>26} {'A(mu)':>26}"
          f" {'ratio':>14} {'(1-ratio)*c':>13}")
    for mu in [4, 6, 8, 10, 12]:
        c = 2 * mp.pi * mp.mpf(mu)
        K = int(c) + 90
        m = measured(2 * mp.pi, mu, K)
        a = connes_A(mu)
        r = m / a
        print(f"{mu:>5} {mp.nstr(c, 8):>14} {K:>6} {mp.nstr(m, 12):>26} {mp.nstr(a, 12):>26}"
              f" {mp.nstr(r, 10):>14} {mp.nstr((1 - r) * c, 6):>13}")
    print()
    print("The ratio rises towards 1 from BELOW, and the last column says at what rate:")
    print("(1 - ratio) * c is bounded and slowly increasing, i.e. the shortfall is O(1/c).")
    print("Fuchs' asymptotic is a leading term, so an O(1/c) deficit is what agreement")
    print("looks like -- and note that a WRONG kappa could not produce it, because the")
    print("error there is exponential in mu, not a fixed inverse power of c.  The point")
    print("of the table above remains the CONTRAST with the other kappa.")
    print()

    print("=" * 96)
    print("Stability: the digits above are the stable ones")
    print()
    print(f"{'mu':>5} {'dps':>6} {'K':>6} {'ratio at kappa = 2 pi':>28}")
    for mu in [8, 10]:
        seen = set()
        for dps in [200, 320, 420]:
            for dK in [40, 90, 160]:
                mp.mp.dps = dps
                c = 2 * mp.pi * mp.mpf(mu)
                K = int(c) + dK
                r = measured(2 * mp.pi, mu, K) / connes_A(mu)
                seen.add(mp.nstr(r, 12))
                print(f"{mu:>5} {dps:>6} {K:>6} {mp.nstr(r, 12):>28}")
        # "Unchanged in the printed digits across dps 200/320/420 and
        # K = c+40/90/160" -- the nine rows are one number or they are not.
        VD.check(len(seen) == 1,
                 "U8: ratio unchanged in the printed digits across dps and K (mu=%d)" % mu)
    mp.mp.dps = 320
    print()
    print("Unchanged in the printed digits across dps 200/320/420 and K = c+40/90/160.")


if __name__ == "__main__":
    main()
    VD.finish()
