# An independent recheck of the deficit/repair and rate numerics

Work item mg-9797. Companion script:
[`verify_independent_recheck.py`](verify_independent_recheck.py) — needs
**nothing but the Python standard library**. Rechecks
[`deficit-repair.md`](deficit-repair.md) (mg-7606) and
[`prolate-rate.md`](prolate-rate.md) (mg-fcb8), whose numbers
`paper/positivity-obstruction.tex` (mg-8b7b) now rests on and which were
produced by a single implementation — `verify_deficit_repair.py` and
`verify_prolate_rate.py` — written in one sitting by one author.

**Neither of those two scripts was opened until every number below had been
computed and written down.** The order is the whole point:
[[replication-is-not-corroboration]] — N readings of one derivation are one
reading, and a reimplementation written *after* reading the original inherits
its slips silently and then agrees with it, which is worse than no check at all.
The pre-comparison record is the run log quoted in §7.

Nothing in `start.tex` or `s3.tex` was edited, and no number in
`deficit-repair.md` or `prolate-rate.md` was changed: per the ticket, a
verification reports, and amending is a separate act. §8 is the list of what
would have to be amended.

---

## Bottom line

**1. All five numbers reproduce.** Every one, to every digit printed in the
notes, from an implementation that shares no arithmetic library, no
transcendental function, no eigensolver and — for the archimedean boundary term
— no method with the original. The tables are in §3.

| # | claim | outcome |
|---|---|---|
| 1 | $\lvert2\vartheta'(0)\rvert=5.3721834\ldots$, and the deficit saturates it | **verified**, two independent routes to the constant, all 10 rows of §2.2 |
| 2 | $R/D$ falls $1.678\to1.015$ over $\mu=3..20$ | **verified**, all 9 rows of §3 |
| 3 | near-radical: archimedean **+**, primes **−**, both $\approx0.025\log\mu$ | **verified**, all 8 rows of §4.1, signs and magnitudes |
| 4 | $A=5.4635\pm0.052$ against $4\pi/\log10=5.4575$ | **verified**: $A=5.463526\pm0.051591$, $0.117\sigma$ |
| 5 | $s/(1-\chi_2)\in[7,13]$, index 4 not 0, gap to index 0 growing $\sim56\times$ | **verified**: $[7.6074,12.9609]$, growth factor $56.16$ |

**2. Three discrepancies, and the largest of them is in the published paper, not
here.** In decreasing order of consequence:

- **Connes–Consani's own eq. (h02ev), `Spectraltriples.tex:474`, is a factor 2
  too small.** Their closed form for the even-sector boundary term
  $\widehat F(i/2)+\widehat F(-i/2)$ disagrees with their own convolution table
  at `:444` — from which it is derived four lines later — by exactly
  $2.000000000000000$. Their odd-sector (h02) at `:478` is exact. **This does
  not propagate into this project**: neither `verify_deficit_repair.py` nor this
  file uses (h02ev); both build $W_{0,2}$ from the table. It is an erratum in
  arXiv:2106.01715 and is reported here because someone reading their §`w02` and
  trusting the printed formula would halve the term. §6.
- **`deficit-repair.md` §4.1, the "digits" column at $\mu=8$: $31.02$ should be
  $31.06$.** The column is $\log_{10}(\lvert\sigma^{\mathrm{arch}}(v_\mu)\rvert/s)$
  and the row's own two entries give
  $\log_{10}(0.05273312)+32.33898=31.0611$. Every other row of that column is
  right. It changes nothing — the note's derived statement, "an average of
  $5.21$ digits per unit of $\mu$", uses only the endpoints $\mu=5$ and
  $\mu=12$ — but it is a wrong cell in a published table. §8.
- **`deficit-repair.md` §3, $R(3)$: $0.12404900$ should be $0.12404899$.** The
  converged value is $0.124048994835$, stable in precision, in the number of
  inverse iterations, and at $N=60$ and $N=100$. A last-digit rounding slip; the
  same row's $R-D=0.05011122$ is right. §8.

**3. One number in the notes is a definition apart, not a digit apart.**
`deficit-repair.md` §5's "residual rms $0.042$" is the $(n-p)$-normalised
residual, $0.04150$; the $/n$ one is $0.03281$. Both are defensible and the
note's max residual $0.056$ matches exactly. Recorded so the next person can
reproduce the number rather than rediscover the ambiguity. §8.

**4. The one link both implementations took on trust is now tested, and holds.**
`deficit-repair.md` §8 names its own greatest exposure: the normalisation of
Connes–Consani's Proposition `Hilbert`, "a factor of $2$ there doubles the
constant". Both implementations take eq. (thetaprime) `:261` from the paper.
Here it is confirmed to **18 digits** —
$$-W_{\mathbb R}^\#(f,f)\Big/\int\lvert\widehat f(t)\rvert^2\frac{2\vartheta'(t)}{2\pi}dt
= 1.000000000000000007$$
— by a route the original could not use: a test function vanishing to second
order at $\pm L/2$, whose transform decays like $t^{-5}$ instead of $t^{-1}$ and
so needs no asymptotic tail supplied. §5.

**5. What this check does NOT establish, stated as sharply as the agreements.**
Both implementations read the same paper. **If `Spectraltriples.tex` has been
misread the same way twice, every agreement above is worthless** — and that is
irreducible, not a defect of effort. Three further shared dependencies are named
in §2, of which the substantive one is that the prolate route is the same route.
Proposition `Hilbert` is still not re-proved by anyone here. And the truncation
caveat is unchanged and cuts the same way: every $s(\mu)$ in both notes and in
this one is an **upper bound**. §4.4.

---

## 1. What was checked against what

The five numbers are `deficit-repair.md` §2.1–§2.2, §3, §4.1, §5, and
`prolate-rate.md` §3. The comparison target is the **notes**, i.e. the published
numbers the paper rests on, not the scripts. The scripts were read afterwards,
once, to answer one question each: what method did they use (§2), and did the
(h02ev) erratum reach them (§6).

Definitions were taken from arXiv:2106.01715, `Spectraltriples.tex`, read in the
source. The ones that matter, with their lines, because §5's caveat means the
*reading* is the shared risk and it should be legible enough to disagree with:

| object | line | as used here |
|---|---|---|
| basis | `:385` | $\xi_0=L^{-1/2}$, $\xi_n=(-1)^n\sqrt{2/L}\cos(2\pi nx/L)$, $n>0$ |
| the form | `:414` | $\psi^\#=W_{0,2}^\#-W_{\mathbb R}^\#-\sum_pW_p^\#$ |
| $W_{0,2}^\#$ | `:419` | $\int_1^\infty F(x)(x^{1/2}+x^{-1/2})d^*x$ |
| $W_{\mathbb R}^\#$ | `:422` | $\tfrac12(\log4\pi+\gamma)F(1)+\int_1^\infty\frac{x^{1/2}F(x)-F(1)}{x-x^{-1}}d^*x$ |
| $W_p^\#$ | `:425` | $(\log p)\sum_{m\ge1}p^{-m/2}F(p^m)$ |
| matrix | `:432` | $\sigma(n,m)=\psi^\#(h)$, $h(u)=(\xi_n\star\xi_m^*+\xi_m\star\xi_n^*)(\log u)$ |
| convolution | `:444` | the table, whose general term is $\tfrac12(\xi_n\star\xi_m^*+\xi_m\star\xi_n^*)$ |
| $\vartheta'$ | `:261`, `:266` | $W_\infty(F)=\int\widehat F(t)\frac{2\vartheta'(t)}{2\pi}dt$; $\vartheta(t)=-\tfrac t2\log\pi+\Im\log\Gamma(\tfrac14+\tfrac{it}2)$ |

$L=\log\mu$, even sector, indices $0..N$.

---

## 2. Independence, itemised — the part of this that is worth anything

Independence is a property one has to argue. Here is the argument, and here is
where it stops.

### 2.1 Independent

- **Arithmetic.** Python's `decimal` — libmpdec, decimal radix — against
  mpmath's binary radix over Python ints. A rounding or radix bug in one is not
  a bug in the other.
- **Every transcendental function.** $\pi$ (Machin), $\log2$ and $\log$ (atanh
  series after repeated square roots), $\exp$ (halving then Taylor), $\sin/\cos$
  (Taylor then angle doubling), $\gamma$ (Brent–McMillan B1), $\psi$ (recurrence
  plus asymptotic series with exact Bernoulli numbers), $\Re\psi$ of a complex
  argument (the same, in complex arithmetic on Decimal pairs) are implemented
  from their series in the companion script. The original calls mpmath for all
  of these. Check 0(a) puts them against known digits at $10^{-59}$.
- **The archimedean boundary term, by a different method.** Derived here in
  closed form: on the even sector
  $$W_{0,2}^\#(n,m)=2v_nv_m,\qquad v_n=\int_{-L/2}^{L/2}\xi_n(x)e^{x/2}dx
  =\sqrt{2/L}\,\frac{4L\sinh(L/4)}{L^2+16\pi^2n^2}\ (n\ge1),$$
  a rank-one positive matrix. The original computes this block by quadrature.
  Two routes, agreeing to every digit (check 0(d)) — and the closed form is what
  makes `deficit-repair.md` §2.1's "the boundary term is a square" visible
  rather than asserted.
- **The convolution table, re-derived twice.** Once symbolically by hand
  (product-to-sum on $\int_{t-L/2}^{L/2}\cos(a_nx)\cos(a_m(x-t))dx$, both
  boundary terms killed by $a_kL=2\pi k$), and once by brute-force numerical
  convolution of the basis functions themselves — check 0(c), sixteen entries in
  both sectors, agreeing to $10^{-37}$.
- **The eigenvalue.** Householder tridiagonalisation then Sturm-sequence
  bisection, which returns a **bracket**: an interval whose endpoints are
  separately checkable by an inertia count. For a quantity of size $10^{-54}$
  read off entries of order $1$ that is worth more than a converged iterate.
- **The prolate normalisation constant.** Checked against the trace sum rule
  $\sum_n\Lambda_n(c)=2c/\pi$, to 58 digits at $c=5$ (check 6). This pins the one
  factor that a derivation of $\Lambda_n$ from the finite Fourier transform could
  get wrong, and the original does not have this check.
- **(thetaprime), tested rather than assumed.** §5.

### 2.2 NOT independent — and therefore not corroborated by anything above

- **The definitions.** Both implementations read the same paper. A shared
  misreading is invisible to this exercise. It is why §1 tabulates the lines.
- **Proposition `Hilbert` (`:289`) itself**, and the identity (thetaprime)
  `:261` as a *theorem*. §5 tests the latter's normalisation numerically; nobody
  here has re-proved either.
- **Composite Gauss–Legendre with Newton-refined Legendre roots.** Chosen here
  independently, and it turns out to be the same scheme the original uses. This
  is a real limit on what the matrix agreement establishes. What differs is the
  panel count, the node count, and the grouping of the singular integrand — the
  original regularises $e^{y/2}/(2\sinh y)$ by factoring $y/(2\sinh y)$ and
  carries a separate scalar $\kappa=\int(e^{y/2}-1)/(2\sinh y)$; this file
  subtracts $L$ inside the numerator and never forms $\kappa$. Check 7(b) varies
  panels and nodes and the answer does not move.
- **The Legendre (Bouwkamp) route to the prolate eigenvalues**, and the identity
  $\Lambda_n=c\,d_0^2/(\pi\psi_n(0)^2)$. Derived here from the ODE and the finite
  Fourier transform rather than looked up — but it is the same identity the
  original uses, because it is the natural one. **Of everything in §2, this is
  the weakest independence claim.** The sum rule is what mitigates it.
- **Fuchs' asymptotic** is quoted by both, derived by neither.

### 2.3 Not attempted

The odd sector $\sigma^-$ (open item T4 in `deficit-repair.md`, untouched); any
re-proof of Proposition `Hilbert`; and the mantissa of Connes–Consani's
$2.389\times10^{-48}$, which is not converged in $N$ and which nobody has
verified — see §4.4.

---

## 3. The five numbers

### 3.1 Number one — the bound, and the saturation

The constant, two ways at three working precisions (check 1). From
$\vartheta'(t)=\tfrac12[\Re\psi(\tfrac14+\tfrac{it}2)-\log\pi]$,
$$\lvert2\vartheta'(0)\rvert=\log\pi-\psi(\tfrac14)
=\gamma+3\log2+\tfrac\pi2+\log\pi=5.37218341922566558223295749744974228901\ldots$$
The left form is computed from a recurrence-plus-asymptotic $\psi$; the right is
Gauss' closed form for $\psi(\tfrac14)$. They agree to 75 digits at 120 dps —
and that agreement is itself a check, since the two routes share nothing but
$\pi$. **The note's $5.3721834192\ldots$ is confirmed.**

The deficit, $N=160$, 60 dps, against `deficit-repair.md` §2.2:

| $\mu$ | $D(\mu)$, this file | §2.2 | |
|---|---|---|---|
| $3$ | $0.07397888857108$ | $0.07397889$ | ✓ |
| $5$ | $0.37270354635970$ | $0.37270355$ | ✓ |
| $11$ | $0.77466582875372$ | $0.77466583$ | ✓ |
| $20$ | $1.02682548048722$ | $1.02682548$ | ✓ |
| $10^2$ | $1.62332471718417$ | $1.62332472$ | ✓ |
| $10^3$ | $2.44603690912012$ | $2.44603691$ | ✓ |
| $10^6$ | $4.23599851146085$ | $4.23599851$ | ✓ |
| $10^9$ | $4.87322925026319$ | $4.87322925$ | ✓ |
| $10^{12}$ | $5.10422655279278$ | $5.10422655$ | ✓ |
| $10^{20}$ | $5.28349631418786$ | $5.28349631$ | ✓ |

Ten rows, every printed digit. $D$ increases, never reaches the bound, and the
gap at $10^{20}$ is $0.0887$.

**External anchor.** At $\mu=2$ this file gives
$\lambda_{\min}(\sigma^{\mathrm{arch}})=0.0013310$ at $N=60$, against
Connes–Consani's own $\sim0.00133$ (`:551`). That is an agreement with a
published number computed by neither implementation.

### 3.2 Number two — the over-repair, and the closing margin

$N=60$, 40 dps, against §3. $v_{\rm arch}$ from inverse iteration at the
bisected eigenvalue; $R=-\sum_pW_p(v_{\rm arch})$.

| $\mu$ | $D$ | $R$ | $R-D$ | $R/D$ | §3's $R/D$ |
|---|---|---|---|---|---|
| $3$ | $0.07393778$ | $0.12404899$ | $0.05011122$ | $1.6777$ | $1.6777$ |
| $4$ | $0.23972403$ | $0.26633090$ | $0.02660687$ | $1.1110$ | $1.1110$ |
| $5$ | $0.37262595$ | $0.41590755$ | $0.04328161$ | $1.1162$ | $1.1162$ |
| $6$ | $0.47506903$ | $0.48993904$ | $0.01487000$ | $1.0313$ | $1.0313$ |
| $8$ | $0.62435999$ | $0.64978693$ | $0.02542693$ | $1.0407$ | $1.0407$ |
| $10$ | $0.73104987$ | $0.74250899$ | $0.01145912$ | $1.0157$ | $1.0157$ |
| $12$ | $0.81337243$ | $0.83273410$ | $0.01936168$ | $1.0238$ | $1.0238$ |
| $16$ | $0.93617534$ | $0.94601094$ | $0.00983560$ | $1.0105$ | $1.0105$ |
| $20$ | $1.02672849$ | $1.04224568$ | $0.01551719$ | $1.0151$ | $1.0151$ |

Every cell matches except $R(3)$, where §3 prints $0.12404900$ and the converged
value is $0.1240489948$ — §8. **$R>D$ everywhere; $R/D$ falls $1.6777\to1.0151$;
the absolute slack oscillates in $0.010$–$0.050$ with minima at $\mu=6,10,16$.
Confirmed, including the shape.**

### 3.3 Number three — the reversed signs

The ticket says to check this hardest, because it is the surprising claim.
$N=100$, 120 dps, against §4.1. $v_\mu$ is the bottom eigenvector of the *full*
form, not of $\sigma^{\mathrm{arch}}$.

| $\mu$ | $\sigma^{\mathrm{arch}}(v_\mu)$ | $-\sum_pW_p(v_\mu)$ | $s(\mu)$ | $\log_{10}s$ | digits |
|---|---|---|---|---|---|
| $5$ | $+0.03958194$ | $-0.03958194$ | $1.0050\times10^{-17}$ | $-16.998$ | $15.60$ |
| $6$ | $+0.04538231$ | $-0.04538231$ | $8.2110\times10^{-23}$ | $-22.086$ | $20.74$ |
| $7$ | $+0.04959492$ | $-0.04959492$ | $7.7305\times10^{-28}$ | $-27.112$ | $25.81$ |
| $8$ | $+0.05273312$ | $-0.05273312$ | $4.5813\times10^{-33}$ | $-32.339$ | $31.06$ |
| $9$ | $+0.05520046$ | $-0.05520046$ | $3.1355\times10^{-38}$ | $-37.504$ | $36.25$ |
| $10$ | $+0.05719477$ | $-0.05719477$ | $1.7844\times10^{-43}$ | $-42.749$ | $41.51$ |
| $11$ | $+0.05882638$ | $-0.05882638$ | $1.2259\times10^{-48}$ | $-47.912$ | $46.68$ |
| $12$ | $+0.06018733$ | $-0.06018733$ | $5.5305\times10^{-54}$ | $-53.257$ | $52.04$ |

**Identical to §4.1 in every cell but one** — the "digits" entry at $\mu=8$,
where §4.1 has $31.02$ and the arithmetic of its own row gives $31.06$ (§8).

**The signs are as claimed and they are not delicate.** On the direction that
decides positivity the archimedean contribution is positive and the prime
contribution is negative — the deficit/repair picture of §3.2 with its signs
reversed. The two halves agree to 15–52 decimal digits, so the *sign* of each
half is decided at the first digit and is not a near-thing: reversing either
would require an error of order $1$ in a quantity computed to $10^{-53}$. Both
halves divided by $\log\mu$ lie in $[0.02422,0.02549]$ across the range, i.e.
$\approx0.025\log\mu$, and both are two orders below the deficit $D$ of §3.1 —
the near-radical direction is where the archimedean form is nearly flat, not
where it is bad. **Confirmed, and it is the least fragile of the five.**

The prime-drop table of §4.3 also reproduces exactly (check 8): at $\mu=12$,
$N=60$, omitting one prime power at a time gives
$-0.71226224$, $-0.83688017$, $-0.34656987$, $-0.71772943$, $-0.59699566$,
$-0.17682307$, $-0.24427816$, $-0.10260697$ for $2,3,4,5,7,8,9,11$, against
$+9.1907\times10^{-54}$ with all present.

### 3.4 Number four — the fit

Least squares on §3.3's eight points, $\log_{10}s(\mu)=-A\mu+B\log_{10}\mu+D$,
normal equations solved in Decimal (check 5):

| | this file | `deficit-repair.md` §5 |
|---|---|---|
| $A$ | $5.463526\pm0.051591$ | $5.4635\pm0.052$ |
| $B$ | $5.322229\pm0.956951$ | $5.322\pm0.96$ |
| $D$ | $6.588946\pm0.441716$ | $6.589\pm0.44$ |
| max residual | $0.05575$ | $0.056$ |

$4\pi/\log10=5.4575054153673653899\ldots$, so $A-4\pi/\log10=+0.006020$, which
is $\mathbf{0.117\sigma}$ — the note's $0.12\sigma$. The two-parameter fit gives
$A=5.1788$ (§5's $5.179$) with max residual $0.1370$, so the $\log\mu$ term is
real, as §5 says.

`prolate-rate.md` §4's three-way test also reproduces: $B$ against $9/2$ is
$0.859\sigma$ (its $0.86\sigma$), $D$ against
$\log_{10}(2^{14}\sqrt2\pi^5/3)=6.373563$ is $0.488\sigma$ (its $0.49\sigma$),
and $B$ against the index-0 prediction $\tfrac12$ is $5.039\sigma$ (its
$5.0\sigma$). **The constant $6.373563$ — which `deficit-repair.md` records as
having been mis-transcribed once as $6.37347$, caught while assembling the paper
— is confirmed from scratch here.** That is the class of slip this ticket exists
to catch, and it had already been caught; this is the second pair of eyes
agreeing with the correction rather than with the slip.

### 3.5 Number five — the index is 4

$\Lambda_n(c)$ from the Legendre expansion; $1-\Lambda_n$ by subtraction, which
costs $2c/\log10$ digits of cancellation and is why the working precision is 160
dps. $\chi_2=\sqrt{\Lambda_4}$, $c=2\pi\mu$ (check 6):

| $\mu$ | $1-\Lambda_0$ | $1-\Lambda_4$ | $1-\chi_2$ | $s/(1-\Lambda_0)$ | $s/(1-\chi_2)$ |
|---|---|---|---|---|---|
| $5$ | $2.02073\times10^{-26}$ | $2.59678\times10^{-18}$ | $1.29839\times10^{-18}$ | $4.9736\times10^{8}$ | $7.7405$ |
| $6$ | $7.73821\times10^{-32}$ | $2.15870\times10^{-23}$ | $1.07935\times10^{-23}$ | $1.0611\times10^{9}$ | $7.6074$ |
| $7$ | $2.91979\times10^{-37}$ | $1.55799\times10^{-28}$ | $7.78995\times10^{-29}$ | $2.6476\times10^{9}$ | $9.9237$ |
| $8$ | $1.08993\times10^{-42}$ | $1.01580\times10^{-33}$ | $5.07899\times10^{-34}$ | $4.2033\times10^{9}$ | $9.0201$ |
| $9$ | $4.03552\times10^{-48}$ | $6.13442\times10^{-39}$ | $3.06721\times10^{-39}$ | $7.7697\times10^{9}$ | $10.2226$ |
| $10$ | $1.48462\times10^{-53}$ | $3.48934\times10^{-44}$ | $1.74467\times10^{-44}$ | $1.2019\times10^{10}$ | $10.2276$ |
| $11$ | $5.43359\times10^{-59}$ | $1.89163\times10^{-49}$ | $9.45817\times10^{-50}$ | $2.2561\times10^{10}$ | $12.9609$ |
| $12$ | $1.98020\times10^{-64}$ | $9.85817\times10^{-55}$ | $4.92908\times10^{-55}$ | $2.7929\times10^{10}$ | $11.2202$ |

$1-\Lambda_4(2\pi\cdot12)=9.858\times10^{-55}$, against `prolate-rate.md`'s
$9.9\times10^{-55}$. $s/(1-\Lambda_0)$ runs $5.0\times10^8$ to
$2.8\times10^{10}$ and **grows by a factor $56.16$** — its "factor $56$".
$s/(1-\chi_2)$ stays in $[7.6074,12.9609]$ — its "$7.6$ to $13.0$", and its
$[7,13]$. **The index is 4 and not 0, confirmed.**

Two further pieces of §3.5 checked here:

- **External anchor.** $\Lambda_0(c=1)=0.5725817806378951\ldots$ against
  Slepian's classical tabulated $0.57258$. The only external anchor the prolate
  apparatus has, and it holds.
- **Connes' constant is exactly half Fuchs at index 4, and that is derivable
  rather than coincidental.** Fuchs at $n=4$, $c=2\pi\mu$ is
  $\tfrac{2^{15}\sqrt2\pi^5}{3}\mu^{9/2}e^{-4\pi\mu}$ by one line of algebra
  ($4\sqrt\pi\cdot8^4/4!=2048\sqrt\pi/3$, and $2048\cdot2^{9/2}=2^{15}\sqrt2$);
  Connes prints $\tfrac{2^{14}\sqrt2\pi^5}{3}$. The ratio is confirmed
  numerically to 160 digits, and the halving is not a discrepancy but
  $1-\sqrt x\sim\tfrac12(1-x)$, i.e. exactly the passage from $\Lambda_4$ to
  $\chi_2=\sqrt{\Lambda_4}$. `prolate-rate.md` §3's claim stands, and the reason
  it is exactly $\tfrac12$ is now written down.

---

## 4. Stability, and the caveats that survive

### 4.1 Working precision

Same $L=\log8$, same $N=60$, three precisions (check 7a):

| dps | $D(8)$ | $s(8)$ |
|---|---|---|
| $40$ | $0.624359994002551113$ | $5.211181182462378\times10^{-33}$ |
| $80$ | $0.624359994002551113$ | $5.211180349298816\times10^{-33}$ |
| $140$ | $0.624359994002551113$ | $5.211180349298816\times10^{-33}$ |

$D(8)$ does not move at all and matches `deficit-repair.md` §1.3's
$0.624359994002551113$ to all eighteen printed digits. $s(8)$ converges to
$5.211180349298816156\times10^{-33}$, which is §1.3's $80$- and $140$-dps value
to all eighteen digits. At 40 dps the value is right to seven, which is §1.3's
own arithmetic ($40-33=7$ digits of room) and its point about double precision
having $16-33<0$.

**A mistake of my own, recorded because the ticket asks for it.** My first
40-dps run reported $6.27\times10^{-33}$ — 20% off — and I nearly wrote it up as
a disagreement with §1.3. It was not: my relative-accuracy bisection had been
handed a tolerance of $10^{0}$ by an off-by-one in the calling code and stopped
one step in. The lesson is the ticket's own: a disagreement is the valuable
outcome *and* is the outcome most likely to be one's own bug, so it has to be
driven to convergence before it is reported. It is reported here as a mistake
rather than omitted.

### 4.2 Quadrature

At $\mu=8$, $N=60$, 80 dps, doubling the panels per period and taking the nodes
per panel from 40 to 64 moves $D(8)$ in none of 36 decimals (check 7b).

### 4.3 Prolate truncation

$1-\Lambda_4(2\pi\cdot12)=9.85816985725366456587\times10^{-55}$, unchanged
across 100/160/220 dps and across Legendre truncations $k_{\max}=320$ and $500$
— 21 digits stable (check 7d).

### 4.4 Truncation is variational, and it cuts one way

Unchanged, and it applies to this file exactly as to the original. Restricting
the form to a subspace can only raise its smallest eigenvalue, so every
$s(\mu)$ above is an **upper bound** on the true $s(\mu)$ and the sequence in
$N$ decreases. Confirmed here (check 7c), $\mu=11$, 100 dps:

| $N$ | $s(11)$ | §5.1 |
|---|---|---|
| $50$ | $2.3894685\times10^{-48}$ | $2.389468$ |
| $80$ | $1.3705488\times10^{-48}$ | $1.370549$ |
| $100$ | $1.2258655\times10^{-48}$ | $1.225866$ |
| $120$ | $1.1207125\times10^{-48}$ | $1.120712$ |

Four rows, seven digits each, exact. **The exponent $-48$ is settled and
reproduces Connes–Consani's $2.389\times10^{-48}$ (`:178`); the mantissa is
still falling at $N=120$ and nothing here verifies their $2.389$.** $N=50$
landing on $2.3894$ is either their truncation level or a coincidence, and the
paper does not say which (`:210` gives only "$\le N$"). §5.1's reading is
correct and this file adds nothing to it except a second computation of the
same four numbers.

The same caveat has a visible consequence in §3.5: run the companion script with
`--quick`, which drops to $N=60$, and $s/(1-\chi_2)$ inflates to $[7.9,18.6]$
and the growth factor to $83$. That is not noise — it is the upper bound getting
looser, systematically, exactly as the variational principle says. The $[7,13]$
and the $56$ are $N=100$ statements and should always be quoted with their $N$.

---

## 5. The link both implementations took on trust — *tested here*

`deficit-repair.md` §8 says it plainly: "the claim in this note that would do the
most damage if wrong is §2.1's bound … Its exposure is the normalisation of
Proposition `Hilbert` — a factor of $2$ there doubles the constant." Both
implementations take
$$W_\infty(F)=-W_{\mathbb R}^\#(F)=\int\widehat F(t)\frac{2\partial_t\vartheta(t)}{2\pi}dt
\qquad(\texttt{:261})$$
from the paper. It is testable, and the test is check 1b.

The original tests it on $f=\xi_1$, for which $\widehat f$ is closed-form but
decays like $1/t$, so $\lvert\widehat f\rvert^2\vartheta'\sim\log t/t^2$ and the
tail has to be supplied from an asymptotic form — which is why its residual is
$2\times10^{-8}$. Here a different test function removes that difficulty
entirely:
$$f=(1+\cos(a_1x))^2=\tfrac32+2\cos(a_1x)+\tfrac12\cos(a_2x),$$
which vanishes to second order at $\pm L/2$. Its transform is
$\widehat f(t)=\sin(tL/2)\big[3/t+4t/(a_1^2-t^2)-t/(a_2^2-t^2)\big]$, whose
$t^{-1}$ and $t^{-3}$ coefficients both cancel identically, leaving
$\widehat f\sim12a_1^4\sin(tL/2)/t^5$. The tail past $T$ is then
$O(\log T/T^9)$ and can simply be cut off. $\Re\psi(\tfrac14+\tfrac{it}2)$ is
computed by complex recurrence plus asymptotic series on Decimal pairs — no
arctan, because only the real part is wanted, so no branch of the logarithm
enters.

At $\mu=8$, cutting off at $T$:

| $T$ | $\Big(\int\lvert\widehat f\rvert^2\tfrac{2\vartheta'}{2\pi}\Big)\Big/\big(-W_{\mathbb R}^\#(f,f)\big)$ | Plancherel $\tfrac1{2\pi}\int\lvert\widehat f\rvert^2\big/\lVert f\rVert^2$ |
|---|---|---|
| $60$ | $1.000000000000233$ | $0.999999999999815$ |
| $200$ | $1.000000000000000007$ | $0.999999999999999996$ |

**There is no extra factor of 2, and the residual is provably the tail rather
than a constant.** Three things say so: the identity and Plancherel — which is
exact — are off by the same amount in the same direction; raising the working
precision from 40 to 70 dps does not move either; and raising $T$ from 60 to 200
improves the identity by $2.3\times10^{-13}\to7.4\times10^{-18}$, a factor
$3.1\times10^4$, against the $(200/60)^9=2.6\times10^4$ that $O(T^{-9})$
predicts. **Proposition `Hilbert`'s normalisation, as used by both
implementations, is confirmed to 18 digits.** Its *proof* remains taken on trust
from the paper by everyone here.

---

## 6. The erratum in `Spectraltriples.tex:474`

Connes–Consani's Lemma `w02` gives closed forms for
$\widehat F(i/2)+\widehat F(-i/2)$ with $F(x)=\theta(\log x)$,
$\theta=\xi_m\star\xi_n^*$. Their proof computes
$\int_0^L(\theta(t)+\theta(-t))(e^{t/2}+e^{-t/2})dt$ and substitutes the `:444`
table, i.e. twice the table's general term. Carrying that out:

| | printed | from the table | ratio |
|---|---|---|---|
| even, `:474` (h02ev) | $\dfrac{8e^{-L/2}(e^{L/2}-1)^2L^3}{(L^2+16\pi^2m^2)(L^2+16\pi^2n^2)}$ | the same with $16$ | $2.000000000000000$ |
| odd, `:478` (h02) | $-\dfrac{256\pi^2Le^{-L/2}(e^{L/2}-1)^2mn}{(L^2+16\pi^2m^2)(L^2+16\pi^2n^2)}$ | the same | $1.000000000000000$ |

Check 0(d) does this numerically at $L=\log5$ for $(n,m)=(1,2),(3,3),(4,7)$ and
for $(-1,-2),(-3,-3)$; the ratios above are what it prints. The even factor is
$16$, not $8$, and three independent arguments agree on that:

1. Direct integration of the `:444` even entry against $2\cosh(y/2)$, term by
   term, using their own `:493` integral.
2. The rank-one form derived in §2.1: $W_{0,2}^\#(n,m)=2v_nv_m$ with
   $v_n=\sqrt{2/L}\,4L\sinh(L/4)\beta_n$, and $16KL=64L\sinh^2(L/4)$ since
   $K=e^{L/2}-2+e^{-L/2}=4\sinh^2(L/4)$. This is the boundary term
   $2\Re(\widehat f(\tfrac i2)\overline{\widehat f(-\tfrac i2)})$ of `:292`
   evaluated in the basis, so the factor is fixed by Proposition `Hilbert`
   itself.
3. The $(0,0)$ entry, where $\int_0^L(L-y)2\cosh(y/2)dy=4K$ exactly by parts,
   giving $W_{0,2}^\#(0,0)=8K/L$ — which is the $16$ convention with the
   $g_0=1/\sqrt2$ scaling, not the $8$ one.

The odd formula being right while the even one is out by 2 is consistent with
their proof: it is written out for the odd case (`:481`, "We give the proof of
(h02)") and the even case is left as "similar".

**It does not reach this project.** `verify_deficit_repair.py` builds $W_{0,2}$
by quadrature from the table, not from (h02ev); this file builds it from the
rank-one closed form, also not from (h02ev); and the two agree. Reported because
the printed formula is wrong in the literature and someone will eventually use
it.

---

## 7. Reproduction, verification, second-hand — per number

To `deficit-repair.md` §1.4's standard and the ticket's. The distinction is
whether the quantity was computed here before any comparison, and the pre-comparison
run log is in the commit that adds this note.

**Verifications** — computed here independently, then compared:

- the constant $\lvert2\vartheta'(0)\rvert$ (two routes, §3.1);
- the deficit table, all ten rows (§3.1);
- $D$, $R$, $R-D$, $R/D$, all nine rows (§3.2);
- the near-radical split, its signs and its magnitudes, all eight rows (§3.3);
- the prime-power drop table, all eight rows (§3.3);
- all three fitted parameters, their standard errors, and the four $\sigma$
  comparisons (§3.4);
- $1-\Lambda_0$, $1-\Lambda_4$, $1-\chi_2$ and both ratio columns (§3.5);
- the exact halving of Fuchs at index 4 (§3.5), which is derived here as algebra
  and not merely observed numerically;
- the normalisation of (thetaprime) (§5);
- the `:444` convolution table (§2.1), and the erratum at `:474` (§6).

**Reproductions, not verifications**:

- $s(\mu)$, all of it. Every $s$ here is an $N$-truncated upper bound, as in the
  original. Agreement between two upper bounds computed at the same $N$ is
  agreement about a bound, not about $s$.
- the match with Connes–Consani's $2.389\times10^{-48}$: the exponent only
  (§4.4).

**External anchors** — agreement with numbers computed by neither implementation:
$\lambda_{\min}(\sigma^{\mathrm{arch}})\approx0.00133$ at $\mu=2$ (`:551`);
$\Lambda_0(c=1)=0.57258$ (Slepian); Connes' printed constant
$2^{14}\sqrt2\pi^5/3$ (`rhready.tex:1149`).

**Second-hand, marked as such**: Fuchs' asymptotic
$1-\Lambda_n(c)\sim4\sqrt\pi\,8^nc^{n+1/2}e^{-2c}/n!$ is quoted from
`prolate-rate.md` and `s3-reduction-audit.md`; Fuchs' paper is still not read by
anyone here. It enters only the *interpretation* in §3.4–§3.5, never the
measurement — except that the exact-halving statement of §3.5 is a statement
about that quoted formula, so it inherits the quotation.

**Primary source**: `Spectraltriples.tex` was re-downloaded and every line cited
in §1 was read in it. `rhready.tex:1149` was read in the source for the constant
in §3.4.

---

## 8. What would have to change in the two notes — *not changed here*

Verification only, per the ticket; amending is a separate act. For whoever does
it:

| where | printed | should be | consequence |
|---|---|---|---|
| `deficit-repair.md` §4.1, "digits" column, $\mu=8$ | $31.02$ | $31.06$ | none — the derived "$5.21$ digits per unit $\mu$" uses only the $\mu=5$ and $\mu=12$ endpoints, which are right |
| `deficit-repair.md` §3, $R(3)$ | $0.12404900$ | $0.12404899$ | none — $R-D$ and $R/D$ in the same row are right |
| `deficit-repair.md` §5, "residual rms $0.042$" | — | say which normalisation | none — it is the $(n-p)$ one, $0.04150$; the $/n$ one is $0.03281$ |

Neither note's argument, and no claim in
`paper/positivity-obstruction.tex`, moves on any of these. The three constraints
on method (§6 of `deficit-repair.md`), the $4\pi$ rate, the $5.3722$ bound and
the reversed signs are all untouched.

The erratum of §6 is Connes–Consani's and is not ours to amend. If the paper
draft ever cites `:474`, it should cite `:444` instead.

---

## 9. Open

| # | item | why it is open |
|---|---|---|
| **I1** | The shared reading of `Spectraltriples.tex` | The irreducible one. Two implementations, one reading. The only fix is a third party who reads the paper without reading either note — which is the mathematician `vision.md` item 17 says is Daniel's to find, and this exercise does not substitute for it |
| **I2** | The prolate route is shared | Both use the Legendre/Bouwkamp expansion and the same identity for $\Lambda_n$. The trace sum rule pins the normalisation; it does not pin the expansion. A genuinely different route — e.g. the out-of-band energy $1-\Lambda_n=\frac1{2\pi}\int_{\lvert t\rvert>c}\lvert\widehat\psi_n\rvert^2dt$, which is manifestly positive and needs no cancellation — was scoped here and not done; it is the obvious next check and it is cheap |
| **I3** | Proposition `Hilbert` is proved by nobody here | Its *normalisation* is now confirmed to 18 digits (§5). Its proof is still taken from the paper by both implementations |
| **I4** | The odd sector | Untouched here, as in `deficit-repair.md` T4 |
| **I5** | The mantissa of $s(11)$ | Still not converged at $N=120$, in either implementation. `deficit-repair.md` T3's descendant |
