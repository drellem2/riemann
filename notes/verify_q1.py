#!/usr/bin/env python3
"""Checks for Q1 of `h1-mean-value.md` §9, resolved in `band-edge-connection.md`.

Work item mg-6851.  Needs `mpmath`; no numpy.  Imports the prolate apparatus of
`verify_prolate_rate.py` and the entire-extension apparatus of `verify_h1.py`.

Q1 is

    (Q1)   x |Phi_{n,c}(x)| <= K(c) |Phi_{n,c}(1)|   for x >= 1,   chi_n < c^2,

with K subexponential in c.  `band-edge-connection.md` proves it with

    K(c) = 2^{3/4} exp(E(c)),   E(c) = 5 sqrt2/(c-sqrt2) + (sqrt2 c/3 + 2)/(c-sqrt2)^2,

for every c > sqrt2, uniformly in n subject to chi_n < c^2 -- so K is BOUNDED,
not merely subexponential, and K -> 2^{3/4} = 1.6818 as c -> infinity.

Nothing here proves anything: the theorem is quantified over all x >= 1 and all
c, and no grid reaches that.  What these checks do is (i) validate the entire
extension off [-1,1] against a second, independent method, (ii) test every
algebraic inequality the proof uses on a grid, where a slip in the algebra would
show, and (iii) report how far the proved K sits above the truth.

CHECK 0 -- the entire extension, cross-validated.  Phi off [-1,1] is computed
           from the spherical-Bessel series (verify_h1.py CHECK 0 pins it at
           x = 1 against the Legendre series).  Here it is checked a second way:
           the ODE  ((1-x^2)Phi')' + (chi - c^2 x^2) Phi = 0  is integrated
           outward from x = 1.2 with initial data taken from the Bessel series,
           and the two are compared at a spread of x.  The series and the
           integration share no code below `prolate_even`.

CHECK 1 -- the four algebraic bounds of the proof, on a grid in x >= sqrt2:
               k(x)^2 = c^2 + (c^2-chi)/(x^2-1) > c^2       [phase speed]
               f := D'/(4D) <= 2/x
               |f'| <= 8/x^2
               |k'| <= 4c/x^3
               theta' = k + f sin 2theta >= c - sqrt2 > 0
           These are proved in the note; a grid can only falsify them.  The
           phase-speed bound is where the hypothesis chi < c^2 enters, and it is
           the whole reason the argument closes.

CHECK 2 -- the oscillatory integral.  A := rho D^{1/4} satisfies
           A'/A = -f cos 2theta exactly.  Two things are measured:
             (a) the identity itself: log(A(X)/A(sqrt2)) vs -int f cos2theta,
                 computed from the Bessel series and by quadrature respectively;
             (b) E_obs := sup_X |int_{sqrt2}^X f cos2theta| against the proved
                 bound E(c).  E_obs must be below E(c) or the proof is wrong.

CHECK 3 -- the conclusion.  sup_{x>1} x|Phi(x)|/|Phi(1)| on a fine grid,
           including x within 1e-6 of the band edge (verify_h1.py CHECK 3 stayed
           0.008 away from it and therefore under-reported: the sup is at the
           edge and equals 1).  Compared against the proved K(c).

CHECK 4 -- the sharp constant, OBSERVED not proved.  A(x)/|Phi(1)| is claimed in
           the note (§6, observed) to converge to sqrt(2/pi) = 0.797885, the
           Bessel-J_0 connection constant at the band edge.  That constant is
           what the proof does NOT capture: it would give K ~ sqrt(2/(pi c)),
           i.e. decay in c, where the proof gives K = O(1).

CHECK 5 -- chi_n/c^2 at the indices the corpus actually uses, n = 0..8.  The
           hypothesis chi_n < c^2 is not automatic at index 8 for small c, and
           `h1-mean-value.md` §5 tabulates only n = 0, 2, 4.

Working precision 60 digits (CHECK 0 uses 80).  Runtime ~6 minutes; --quick ~1.
"""

import sys
import mpmath as mp
import verify_prolate_rate as VP
from verify_h1 import sph_j_all, bessel_coeffs, legendre_trunc, prolate_data

QUICK = "--quick" in sys.argv

SQRT2 = None            # set after precision is fixed


def _s2():
    return mp.sqrt(mp.mpf(2))


# --- Phi and Phi' off the interval, from the spherical-Bessel series ----------


def phi_and_deriv(a, c, x, kmax):
    """(Phi(x), Phi'(x)) from Phi(x) = sum_k a_k j_k(c x), k even.

    j_k'(z) = j_{k-1}(z) - (k+1)/z j_k(z), and j_{-1}(z) = cos(z)/z, so the odd
    indices of the same Miller array are used; nothing new is computed.
    """
    z = c * x
    js = sph_j_all(z, kmax)
    jm1 = mp.cos(z) / z
    val = mp.mpf(0)
    der = mp.mpf(0)
    for k, ak in a.items():
        prev = jm1 if k == 0 else js[k - 1]
        val += ak * js[k]
        der += ak * (prev - mp.mpf(k + 1) / z * js[k])
    return val, c * der


def prufer_at(chi, c, x, Phi, dPhi):
    """(rho, cos2theta, A, k, f, D) at x > 1 from (Phi, Phi')."""
    x2 = x * x
    q = c * c * x2 - chi
    D = (x2 - 1) * q
    p = (x2 - 1) * dPhi
    rho2 = p * p / D + Phi * Phi
    cos2 = (p * p / D - Phi * Phi) / rho2
    A = mp.sqrt(rho2) * D ** mp.mpf('0.25')
    k = mp.sqrt(q / (x2 - 1))
    f = (x / 2) * (1 / (x2 - 1) + c * c / q)
    return mp.sqrt(rho2), cos2, A, k, f, D


def _theta(chi, c, x, a, kmax):
    """theta(x) in [0, 2pi) from Phi = rho sin theta, p/sqrt(D) = rho cos theta."""
    Phi, dPhi = phi_and_deriv(a, c, x, kmax)
    x2 = x * x
    D = (x2 - 1) * (c * c * x2 - chi)
    return mp.atan2(Phi, (x2 - 1) * dPhi / mp.sqrt(D))


def E_proved(c):
    """The note's E(c) = 5 sqrt2/(c-sqrt2) + (sqrt2 c/3 + 2)/(c-sqrt2)^2.

    5 sqrt2 = 4 sqrt2 (the int|g'| x^-2 terms) + sqrt2 (the two boundary terms
    g(sqrt2) + g(X); g(X) is NOT dropped -- the sup is over finite X too).
    """
    s2 = _s2()
    cm = c - s2
    return 5 * s2 / cm + (s2 * c / 3 + 2) / cm ** 2


def K_proved(c):
    return mp.mpf(2) ** mp.mpf('0.75') * mp.e ** E_proved(c)


# --- CHECK 0 ------------------------------------------------------------------


def check0():
    print("\nCHECK 0 -- the entire extension, cross-validated against the ODE")
    print("The Bessel series is one computation of Phi off [-1,1]; integrating")
    print("((1-x^2)Phi')' + (chi - c^2 x^2)Phi = 0 outward from x = 1.2 with data")
    print("taken from that series at x = 1.2 is another.  They agree or one is wrong.\n")
    mp.mp.dps = 80
    print("  c          n    x       Phi (series)        rel. diff (ODE vs series)")
    cs = [2 * mp.pi * 3] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3, 2 * mp.pi * 5]
    for cv in cs:
        c = mp.mpf(cv)
        for (n, lam, chi, mu, p1, b) in prolate_data(c):
            km = legendre_trunc(b, mp.mpf(10) ** -60)
            a = bessel_coeffs(b, mu, km)
            x0 = mp.mpf('1.2')
            v0, d0 = phi_and_deriv(a, c, x0, km)

            def rhs(x, y):
                # y = (Phi, p) with p = (x^2-1)Phi';  p' = -(c^2x^2-chi)Phi
                return [y[1] / (x * x - 1), -(c * c * x * x - chi) * y[0]]

            sol = mp.odefun(rhs, x0, [v0, (x0 * x0 - 1) * d0], tol=mp.mpf(10) ** -40)
            for xt in [mp.mpf('1.5'), mp.mpf('2.5'), mp.mpf('4.0'), mp.mpf('7.0')]:
                vs, _ = phi_and_deriv(a, c, xt, km)
                vo = sol(xt)[0]
                print("  %-10s %-4d %-7s %-19s %s"
                      % (mp.nstr(c, 7), n, mp.nstr(xt, 3), mp.nstr(vs, 10),
                         mp.nstr(abs(vo / vs - 1), 3)))
    mp.mp.dps = 60


# --- CHECK 1 ------------------------------------------------------------------


def check1():
    print("\nCHECK 1 -- the algebraic bounds of the proof, on x >= sqrt2")
    print("All five are proved in the note.  Reported: the worst RATIO of the")
    print("actual quantity to its claimed bound over the grid.  Anything > 1 is a")
    print("refutation of that line of the proof.  theta' is reported as the worst")
    print("value of (k + f sin2theta)/(c - sqrt2), which must stay >= 1.\n")
    mp.mp.dps = 60
    s2 = _s2()
    print("  c          n    k/c min   f/(2/x)  |f'|/(8/x^2)  |k'|/(4c/x^3)  theta'/(c-sqrt2)  theta-eqn rel.err")
    cs = [2 * mp.pi * 3] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3,
                                        2 * mp.pi * 5, 2 * mp.pi * 8]
    step = mp.mpf('0.05') if QUICK else mp.mpf('0.02')
    xmax = mp.mpf(20)
    for cv in cs:
        c = mp.mpf(cv)
        for (n, lam, chi, mu, p1, b) in prolate_data(c):
            km = legendre_trunc(b, mp.mpf(10) ** -50)
            a = bessel_coeffs(b, mu, km)
            wk, wf, wfp, wkp, wth = mp.inf, mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.inf
            wthe = mp.mpf(0)
            x = s2
            while x <= xmax:
                x2 = x * x
                u = 1 / (x2 - 1)
                v = c * c / (c * c * x2 - chi)
                f = (x / 2) * (u + v)
                fp = (u + v) / 2 - x2 * (u * u + v * v)
                k = mp.sqrt(c * c + (c * c - chi) * u)
                kp = -x * (c * c - chi) * u * u / k
                wk = min(wk, k / c)
                wf = max(wf, f / (2 / x))
                wfp = max(wfp, abs(fp) / (8 / x2))
                wkp = max(wkp, abs(kp) / (4 * c / x ** 3))
                _, cos2, _, _, _, _ = prufer_at(chi, c, x, *phi_and_deriv(a, c, x, km))
                sin2 = mp.sqrt(max(mp.mpf(0), 1 - cos2 * cos2))
                wth = min(wth, (k - f * sin2) / (c - s2))   # worst case over sign
                # the theta equation itself, by finite difference on atan2
                h = mp.pi / (c * 2000)
                th = [_theta(chi, c, xx, a, km) for xx in (x, x + h)]
                d = th[1] - th[0]
                while d < 0:
                    d += 2 * mp.pi
                sin2t = mp.sin(2 * th[0])
                wthe = max(wthe, abs(d / h - (k + f * sin2t)) / (k + f * sin2t))
                x += step
            print("  %-10s %-4d %-9s %-8s %-13s %-14s %-17s %s"
                  % (mp.nstr(c, 7), n, mp.nstr(wk, 6), mp.nstr(wf, 4),
                     mp.nstr(wfp, 4), mp.nstr(wkp, 4), mp.nstr(wth, 6),
                     mp.nstr(wthe, 3)))


# --- CHECK 2 ------------------------------------------------------------------


def check2():
    print("\nCHECK 2 -- the oscillatory integral  int_{sqrt2}^X f cos2theta")
    print("(a) the identity  log(A(X)/A(sqrt2)) = -int f cos2theta: LHS from the")
    print("    Bessel series, RHS by Simpson quadrature of the same integrand.")
    print("(b) E_obs = sup_X |int| against the proved bound E(c).  E_obs > E(c)")
    print("    would refute the estimate; E_obs << E(c) means the bound is loose.\n")
    mp.mp.dps = 60
    s2 = _s2()
    print("  c          n    E_obs      E(c) proved   identity resid   K(c) proved  verdict")
    cs = [2 * mp.pi * 3] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3,
                                        2 * mp.pi * 5, 2 * mp.pi * 8]
    xmax = mp.mpf(12) if QUICK else mp.mpf(25)
    for cv in cs:
        c = mp.mpf(cv)
        # step must resolve the oscillation: phase speed is >= c
        step = mp.pi / (c * 40)
        for (n, lam, chi, mu, p1, b) in prolate_data(c):
            km = legendre_trunc(b, mp.mpf(10) ** -50)
            a = bessel_coeffs(b, mu, km)

            def integrand(x):
                _, cos2, _, _, f, _ = prufer_at(chi, c, x, *phi_and_deriv(a, c, x, km))
                return f * cos2

            _, _, A0, _, _, _ = prufer_at(chi, c, s2, *phi_and_deriv(a, c, s2, km))
            acc = mp.mpf(0)
            worst = mp.mpf(0)
            x = s2
            g0 = integrand(x)
            resid = mp.mpf(0)
            while x + 2 * step <= xmax:
                g1 = integrand(x + step)
                g2 = integrand(x + 2 * step)
                acc += step / 3 * (g0 + 4 * g1 + g2)
                x += 2 * step
                g0 = g2
                worst = max(worst, abs(acc))
                _, _, Ax, _, _, _ = prufer_at(chi, c, x, *phi_and_deriv(a, c, x, km))
                resid = max(resid, abs(mp.log(Ax / A0) + acc))
            ok = "ok" if worst <= E_proved(c) else "REFUTED"
            print("  %-10s %-4d %-10s %-13s %-16s %-12s %s"
                  % (mp.nstr(c, 7), n, mp.nstr(worst, 4),
                     mp.nstr(E_proved(c), 4), mp.nstr(resid, 3),
                     mp.nstr(K_proved(c), 5), ok))


# --- CHECK 3 ------------------------------------------------------------------


def check3():
    print("\nCHECK 3 -- the conclusion  sup_{x>=1} x|Phi(x)|/|Phi(1)|  vs the proved K(c)")
    print("The grid is refined toward the band edge (x - 1 = 1e-6 up), which is")
    print("where the sup actually sits: at x = 1 the ratio is 1 by definition, and")
    print("verify_h1.py CHECK 3 started 0.008 away and so reported 0.4--0.79.")
    print("`sup, x>=sqrt2' is the branch the WKB half of the proof covers; the")
    print("branch 1 <= x <= sqrt2 is covered by Lemma 5.1 alone, giving sqrt2.\n")
    mp.mp.dps = 60
    s2 = _s2()
    print("  c          n    sup all x>1   at x        sup x>=sqrt2   proved K(c)   K/sup    verdict")
    cs = [2 * mp.pi * 3] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3,
                                        2 * mp.pi * 5, 2 * mp.pi * 8]
    xmax = mp.mpf(12) if QUICK else mp.mpf(25)
    for cv in cs:
        c = mp.mpf(cv)
        # K is claimed uniform in n subject to chi_n < c^2; go to n = 8 where
        # that hypothesis still holds, so uniformity is what is being tested.
        jm = 4 if c > 30 else 2
        for (n, lam, chi, mu, p1, b) in prolate_data(c, jmax=jm):
            if chi >= c ** 2:
                print("  %-10s %-4d  SKIPPED: chi_n/c^2 = %s >= 1, hypothesis fails"
                      % (mp.nstr(c, 7), n, mp.nstr(chi / c ** 2, 4)))
                continue
            km = legendre_trunc(b, mp.mpf(10) ** -50)
            a = bessel_coeffs(b, mu, km)
            xs = []
            e = mp.mpf(10) ** -6
            while e < mp.mpf('0.4'):                 # geometric toward the edge
                xs.append(1 + e)
                e *= mp.mpf('1.15')
            x = mp.mpf('1.4')
            step = mp.pi / (c * 30)
            while x <= xmax:
                xs.append(x)
                x += step
            best, bestx, best_far = mp.mpf(0), None, mp.mpf(0)
            for xv in xs:
                v = abs(phi_and_deriv(a, c, xv, km)[0]) * xv / abs(p1)
                if v > best:
                    best, bestx = v, xv
                if xv >= s2 and v > best_far:
                    best_far = v
            ok = "ok" if best <= K_proved(c) else "REFUTED"
            print("  %-10s %-4d %-13s %-11s %-14s %-13s %-7s %s"
                  % (mp.nstr(c, 7), n, mp.nstr(best, 7), mp.nstr(bestx, 6),
                     mp.nstr(best_far, 7), mp.nstr(K_proved(c), 5),
                     mp.nstr(K_proved(c) / best, 4), ok))


# --- CHECK 4 ------------------------------------------------------------------


def check4():
    print("\nCHECK 4 -- the sharp constant, OBSERVED.  A(x)/|Phi(1)| -> sqrt(2/pi) = 0.797885")
    print("A = rho D^{1/4} is the WKB invariant; the proof bounds it by 2^{1/4} c^{1/2}")
    print("|Phi(1)| via Lemma 5.1, which loses a factor c^{1/2}.  Its true limit is the")
    print("Bessel-J_0 connection constant at the band edge, and it is c- and n-free.")
    print("Reported: min and max of A(x)/|Phi(1)| over a grid on x in [3, xmax].")
    print("A is not exactly constant -- it oscillates by exp(+-E) -- so a spread")
    print("straddling sqrt(2/pi) is what the claim predicts, not a single value.\n")
    mp.mp.dps = 60
    print("  c          n    min A/|Phi(1)|  max A/|Phi(1)|  sqrt(2/pi)  2^{1/4} c^{1/2} (proof)")
    cs = [2 * mp.pi * 3] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3,
                                        2 * mp.pi * 5, 2 * mp.pi * 8]
    xmax = mp.mpf(12) if QUICK else mp.mpf(25)
    for cv in cs:
        c = mp.mpf(cv)
        step = mp.pi / (c * 30)
        for (n, lam, chi, mu, p1, b) in prolate_data(c):
            km = legendre_trunc(b, mp.mpf(10) ** -50)
            a = bessel_coeffs(b, mu, km)
            lo, hi = mp.inf, mp.mpf(0)
            x = mp.mpf(3)
            while x <= xmax:
                _, _, A, _, _, _ = prufer_at(chi, c, x, *phi_and_deriv(a, c, x, km))
                r = A / abs(p1)
                lo, hi = min(lo, r), max(hi, r)
                x += step
            print("  %-10s %-4d %-15s %-15s %-11s %s"
                  % (mp.nstr(c, 7), n, mp.nstr(lo, 8), mp.nstr(hi, 8),
                     mp.nstr(mp.sqrt(2 / mp.pi), 6),
                     mp.nstr(mp.mpf(2) ** mp.mpf('0.25') * mp.sqrt(c), 6)))


# --- CHECK 5 ------------------------------------------------------------------


def check5():
    print("\nCHECK 5 -- the hypothesis chi_n < c^2 at the indices the corpus uses")
    print("`h1-mean-value.md` §5 tabulates n = 0, 2, 4 only, but its §5 text names")
    print("the combination b_0 Phi_0 + b_2 Phi_4 + b_4 Phi_8.  chi_n ~ (2n+1)c for")
    print("n << c, so chi_n < c^2 needs c > 2n+1 roughly, and index 8 is the one")
    print("that can fail in the range this project computes.\n")
    mp.mp.dps = 40
    print("Also: the proof needs chi_n >= 0 once, for the |k'| bound of Lemma 4.1.")
    print("chi_n >= n(n+1) >= 0 for prolate functions, so it is free -- but it is a")
    print("real hypothesis and chi_n is printed below so it can be seen to hold.\n")
    ns = [0, 2, 4, 6, 8]
    print("  c          " + "  ".join("chi_%d/c^2 " % n for n in ns)
          + "  min chi_n")
    cs = [2 * mp.pi * 3] if QUICK else [2 * mp.pi * 2, 2 * mp.pi * 3, 2 * mp.pi * 5,
                                        2 * mp.pi * 8, 2 * mp.pi * 12, mp.mpf(200)]
    for cv in cs:
        c = mp.mpf(cv)
        chis, _, _ = VP.prolate_even(c, jmax=4)
        row = []
        for j, n in enumerate(ns):
            r = chis[j] / c ** 2
            row.append(("%s%s" % (mp.nstr(r, 4), "" if r < 1 else " (FAILS)")).ljust(11))
        lo = min(chis)
        print("  %-10s " % mp.nstr(c, 7) + " ".join(row)
              + "  %s%s" % (mp.nstr(lo, 6), "" if lo >= 0 else " (NEGATIVE)"))
    mp.mp.dps = 60


if __name__ == "__main__":
    print(__doc__.split("CHECK 0")[0].rstrip())
    check5()
    check0()
    check1()
    check2()
    check3()
    check4()
    print("\ndone.")
