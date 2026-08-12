# Is $s(\mu)$ governed by the prolate concentration defect?

Work item mg-fcb8. Companion script:
[`verify_prolate_rate.py`](verify_prolate_rate.py) (needs `mpmath`; no `numpy`).
Continues [`deficit-repair.md`](deficit-repair.md) §5 and its open item T2
(mg-7606), which fitted $\log_{10}s(\mu)=-A\mu+B\log_{10}\mu+D$ over
$\mu=5,\dots,12$, obtained $A=5.4635\pm0.052$ against $4\pi/\log10=5.4575$, and
asked whether the agreement means what it looks like it means. The ticket's
question: **is $s(\mu)$ genuinely governed by $1-\Lambda_0(c)$, or does a nearby
rate arise a different way?**

Everything numerical below is in arbitrary precision; $1-\Lambda_4(2\pi\cdot12)$
is $9.9\times10^{-55}$ obtained as $1$ minus a number, and $s(12)$ is
$5.5\times10^{-54}$ read off a matrix with entries of order $1$.

Nothing in `start.tex` or `s3.tex` was edited.

---

## Bottom line

**1. The premise is right in kind and wrong in index, and the index is the whole
of the discrimination.** $s(\mu)$ is not of the order of $1-\Lambda_0(2\pi\mu)$:
it exceeds it by nine to ten orders of magnitude, and the discrepancy *grows*,
by a factor $56$ across $\mu=5,\dots,12$. The quantity it is of the order of is
$1-\chi_2=1-\sqrt{\Lambda_4(2\pi\mu)}$ — the defect at prolate index **4** —
where the ratio is $7.6$ to $13.0$ at truncation $N=100$, and $7.1$ to $9.9$
where the truncation bias can be extrapolated away — with no monotone trend
left in it.

**2. The rate $4\pi$ cannot tell those apart, and that is why $0.12\sigma$ was
weaker evidence than it looked.** Fuchs' asymptotic is
$1-\Lambda_n(c)\sim4\sqrt\pi\,8^n c^{n+1/2}e^{-2c}/n!$; the exponential factor
$e^{-2c}$ **does not depend on $n$**. At $c=2\pi\mu$ every prolate index predicts
the same rate $2c/\mu=4\pi$. A test that every candidate passes is not a test —
the same lesson as vision amendment 2 §1, in a different place. What
discriminates is the *power* $n+\tfrac12$ and the *constant*.

**3. Both of those are already published — and this project had already written
them down.** Connes, arXiv:2602.04022 (Feb 2026), `rhready.tex:1149`:
$$1-\chi_2\sim\frac{2^{14}}{3}\sqrt2\,\pi^5e^{-4\pi e^L+\frac92L}
\;=\;\frac{2^{14}\sqrt2\,\pi^5}{3}\,\mu^{9/2}e^{-4\pi\mu},$$
citing Fuchs Theorem 1 with the convention $\chi_k(\lambda)^2=\lambda_{2k}(a)$,
$a=\sqrt{2\pi}\lambda$. That constant is *identically* $\tfrac12$ Fuchs at index
$n=4$ and $c=2\pi\mu$ — verified to $100$ digits in §3 — and the $9/2$ is
$n+\tfrac12$ at $n=4$.

**None of that is new to the corpus.** `semilocal-gap.md` §5.2 (mg-03f0, merged
`b819a1d`) quotes the same line, reproduces the same asymptotic, and states
outright that "**Connes' $\chi_2$ is prolate index 4, i.e. the corpus's
$\chi_4$**"; §5.3 closes `citation-audit.md`'s item U4 on the general-$n$ Fuchs
constant against it; and `citation-audit.md` row 14 says the same. `deficit-repair.md`
was written **two commits later, cites `semilocal-gap.md` in its first
paragraph**, and its §5 nevertheless reached for the index-0 form from
`s3-reduction-audit.md` and reported "no rate is given there or anywhere else in
the paper". That sentence is true of arXiv:2106.01715 and false of the survey,
and the survey was already in our bibliography with the right index attached.
**This is not new information arriving; it is information the project had and did
not apply.** §9.

**4. What that buys is a three-parameter test with no free parameters, and it
passes.** Against mg-7606's fit:

| | fitted (mg-7606 §5) | predicted, index 4 | |
|---|---|---|---|
| $A$ | $5.4635\pm0.052$ | $4\pi/\log10=5.45751$ | $0.12\sigma$ |
| $B$ | $5.322\pm0.96$ | $9/2$ | $0.86\sigma$ |
| $D$ | $6.589\pm0.44$ | $\log_{10}(2^{14}\sqrt2\pi^5/3)=6.37347$ | $0.49\sigma$ |

The index-0 reading predicts $B=\tfrac12$, which is $5.0\sigma$ away. **This
retires open item T3**, which was not a puzzle about subleading structure but
the index-0 hypothesis failing the one test that discriminates. §4.

**5. The derivation exists, and it is one-sided.** Connes–Consani's own chain
gives an *identity*, not an estimate: with $\phi$ the prolate combination and
$g=\mathcal E(\phi)|_{[\lambda^{-1},\lambda]}$,
$$QW_\lambda(g,g)\;=\;\sum_{\frac12+is\in Z}\big|\mathcal F_\mu r(s)\big|^2,
\qquad r:=\mathcal E(\phi)\big|_{(0,\lambda^{-1})},$$
because $\mathcal F_\mu(\mathcal E\phi)$ carries a factor $\zeta(\tfrac12-is)$
and so vanishes at every zero. **$QW_\lambda$ at the prolate vector is the Weil
form of the spill**, and the spill's mass is the concentration defect. One
inequality is missing — a mean-value bound for $\sum_Z|\mathcal F_\mu r|^2$
against $\|r\|^2$ — and under it the *upper* bound, hence
$\limsup\mu^{-1}\log s(\mu)\le-4\pi$, follows. §6.

**6. The other half is RH, and this is the ticket's answer.** A rate is a
two-sided statement, and the lower half is a bound $s(\mu)\ge\kappa(\mu)>0$
holding for every $\mu$. Connes states the equivalence himself
(`rhready.tex:1145`): positivity of $QW_\lambda$ for all $\lambda>1$ **is
equivalent to RH**. So a lower bound of any shape implies RH, and a lower bound
with a *rate* is strictly stronger than RH. **The $4\pi$ rate cannot be turned
into an unconditional theorem, and no computation can change that.** The one
version that escapes the implication is the sign-blind one — a rate for $|s|$
with no claim that $s>0$ — and by the house rule that is not the statement
anyone wants. §7.

**7. A by-product: `start.tex:39` names the right object.** Under
`index-convention.md`'s finding that the corpus indexes prolate modes in full,
the corpus's $QW_\lambda(\mathcal Eh_\lambda)\asymp1-\chi_4$ is *this* estimate —
$\chi_4$ there is the characteristic value at prolate index 4, which is CC's
$\chi_2$. §6(b) shows it is the leading term of the spill's mass, so the corpus's
central estimate is correct as stated and is now attached to a number: the
constant it hides is the $8/11$ of mg-aedf times an $O(1)$ mean value over the
zeros.

**Which outcome of the ticket is this?** Outcome **(2)** — it follows under an
extra hypothesis — with the hypothesis named as sharply as it can be: RH itself
for the lower bound, plus one mean-value estimate for the upper. And with a
correction to the premise that makes the evidence much stronger than the ticket
supposed: not one marginal parameter, but three, none of them free.

---

## 0. What is being asked, and of what object

$\lambda>1$, $\mu=\lambda^2$, $L=2\log\lambda=\log\mu$. Connes–Consani's
semi-local Weil quadratic form (`Spectraltriples.tex:169`, eq. `weilQ`) is
$$QW(f,g)=\sum_{\frac12+is\in Z}\overline{\widehat f(\bar s)}\,\widehat g(s),
\qquad \widehat f(s)=\mathcal F_\mu(f)(s)=\int_{\mathbb R_+^*}f(u)u^{-is}\,d^*u,$$
$Z$ the non-trivial zeros; $QW_\lambda$ is its restriction to test functions
supported in $[\lambda^{-1},\lambda]$, and it involves only the primes
$p\le\lambda^2$ because $f\star f^*$ is then supported in
$[\lambda^{-2},\lambda^2]$.

$s(\mu):=\lambda_{\min}(\sigma^+)$, the smallest eigenvalue of the **even**
matrix — mg-7606's $s(\mu)$, and Connes–Consani's $s(L)$ at `:645`. Connes'
$\epsilon(\lambda)$ is the smallest eigenvalue of $A_\lambda$, the self-adjoint
operator with $QW_\lambda(f,f)=\langle A_\lambda f\mid f\rangle$
(`rhready.tex:1145`–`:1147`), on the *whole* of
$L^2([\lambda^{-1},\lambda],d^*u)$ — so $\epsilon(\lambda)=\min(s^+,s^-)$. That
these coincide is a reading, not a definition: §2's argument puts the odd
sector's smallest eigenvalue at prolate index 6 (open item P4), hence far above
the even one, and Connes comparing $\epsilon(\lambda)$ with $1-\chi_2$ — the
index-4 quantity — says he reads it the same way.

Three quantities are in play and they must not be conflated:

| symbol | what it is | who owns it |
|---|---|---|
| $1-\Lambda_n(c)$ | Slepian concentration defect, prolate index $n$, time–bandwidth $c$ | classical |
| $1-\chi_m$ | $1-\sqrt{\Lambda_{2m}(2\pi\mu)}$; CC's characteristic value for $\psi_m=\mathit{PS}_{2m,0}$ | CC, `:191` |
| $s(\mu)=\epsilon(\lambda)$ | smallest eigenvalue of the even semi-local Weil matrix | CC, `:178` |

The ticket asks whether the third is governed by the first at $n=0$. It is not.
It is governed by the second at $m=2$, which is the first at $n=4$.

---

## 1. The chain, as Connes–Consani state it — *theirs, read in the source*

All of this is in arXiv:2106.01715, read from
`arxiv.org/e-print/2106.01715`, file `Spectraltriples.tex`. It is set out here
because the whole question is which link in it is quantitative and which is not.

1. **The radical contains the range of $\mathcal E$** (`:181` in the introduction, `:699` in §`riemweilexpl`). With
   $\mathcal E(f)(x)=x^{1/2}\sum_{n>0}f(nx)$ on the codimension-two space
   $\mathcal S_0^{ev}=\{f\ \text{even Schwartz}: f(0)=\widehat f(0)=0\}$, the
   Mellin transform picks up $\sum_n n^{-s}$:
   $$\mathcal F_\mu(\mathcal E f)(s)=\pi^{-\frac14+\frac{is}2}
   \Gamma\big(\tfrac14-\tfrac{is}2\big)\,\zeta\big(\tfrac12-is\big)\,P_f(s)$$
   (their appendix, `:1605`, for the Hermite family). It vanishes at every zero.
2. **Support, one side** (`:704`): $\operatorname{supp}f\subseteq[-\lambda,\lambda]
   \Rightarrow\operatorname{supp}\mathcal E f\subseteq(0,\lambda]$.
3. **Support, the other side, by Poisson** (`:708`):
   $\mathcal E(\widehat f)(x)=\mathcal E(f)(x^{-1})$, so
   $\operatorname{supp}\widehat f\subseteq[-\lambda,\lambda]
   \Rightarrow\operatorname{supp}\mathcal Ef\subseteq[\lambda^{-1},\infty)$.
4. **The obstruction is Slepian's** (`:711`): $\mathcal P_\lambda\cap
   \widehat{\mathcal P_\lambda}=\{0\}$, but the angle operator has
   $1+\nu(\mu)\sim2\mu$ minuscule eigenvalues with prolate eigenfunctions
   $\psi_{m,\lambda}(x)=\mathit{PS}_{2m,0}(2\pi\lambda^2,x/\lambda)$, and
   $\mathcal F_{e_{\mathbb R}}\psi_{m,\lambda}=\chi_m\psi_{m,\lambda}$ on
   $[-\lambda,\lambda]$ with $\chi_m$ very close to $(-1)^m$.
5. **The prolate vectors** (`:744`): the combinations that vanish at $0$ are
   $$\phi_{2n}=\psi_{2n}\psi_0(0)-\psi_0\psi_{2n}(0),\qquad
   \phi_{2n+1}=\psi_{2n+1}\psi_1(0)-\psi_1\psi_{2n+1}(0),$$
   and after Gram–Schmidt the $\epsilon_n$ are compared with the eigenvectors:
   "the coincidence of $\epsilon_{2m}$ with the eigenfunction of the even matrix
   for its $m$-th eigenvalue" (`:760`).

So $\epsilon_2\leftrightarrow$ the **smallest** even eigenvalue, and $\epsilon_2$
comes from $\phi_2=\psi_2\psi_0(0)-\psi_0\psi_2(0)$, built from
$\psi_2=\mathit{PS}_{4,0}$ and $\psi_0=\mathit{PS}_{0,0}$.

**The governing index is 4. It is in their own construction, and it has been
since 2021.** Connes names it directly in 2026: "we need the eigenvalues
$\chi_0,\chi_2$ corresponding to the eigenfunctions $h_{0,\lambda},h_{4,\lambda}$"
(`rhready.tex:1134`).

**What is *not* in the chain, at any point, is a quantitative link between step 5
and $s(\mu)$.** CC verify it by *plotting* eigenvectors against $\epsilon_n$
(sixteen values of $\mu$, twelve figures); Connes 2026 reports "a striking
similarity (Figure `fpro1`) between the behavior of $\epsilon(\lambda)$ and of
the angular function $1-\chi_2(\lambda)$" — again a figure. **No constant is
stated anywhere.** That gap is what §4 fills, and it is the only thing in this
note that is new numerically.

---

## 2. Why the index is forced to be 4 — *ours as an argument, CC's as a construction*

`deficit-repair.md` §5 took the near-radical vectors to be the prolate functions
and read off $1-\Lambda_0$, the defect of the *best-concentrated* mode. That is
the natural reading of "the smallness of $s$ is the smallness of the angle
operator's eigenvalues", and it is wrong, because the best-concentrated mode is
not admissible.

$\mathcal E$ is defined on $\mathcal S_0^{ev}$, i.e. $f(0)=\widehat f(0)=0$ —
two linear conditions, and they are not optional: they are what makes
$\mathcal E f$ a test function at all. For $f=\sum_mb_m\psi_{m,\lambda}$,
$$f(0)=\sum_mb_m\psi_m(0),\qquad
\widehat f(0)=\int f=\sum_mb_m\chi_m\psi_m(0),$$
the second because $\mathcal F_{e_{\mathbb R}}\psi_m=\chi_m\psi_m$ on
$[-\lambda,\lambda]$ evaluated at $0$. Two modes can satisfy both **only if
$\chi_{m_1}=\chi_{m_2}$** — otherwise the $2\times2$ system is non-singular and
forces $b=0$. Since $\chi_m\simeq(-1)^m$, that requires $m_1\equiv m_2\bmod2$,
i.e. **prolate indices congruent mod 4**.

- $m=0$ alone: $\psi_0(0)\neq0$, inadmissible.
- $\{m_1,m_2\}=\{0,1\}$, prolate indices $\{0,2\}$: $\chi_0\simeq+1$,
  $\chi_1\simeq-1$. Excluded — **by the phase, not by size**.
- $\{0,2\}$, prolate indices $\{0,4\}$: $\chi_0\simeq\chi_2\simeq+1$. Admissible,
  and minimal. This is CC's $\phi_2$.

That is mg-aedf's finding — "mode-4 selection is forced by the finite-Fourier
phase $i^n$, not by geometry" — recovered in the prolate rather than the Hermite
limit, and it is what fixes the index in the asymptotic. `index-convention.md`
records the indexing hazard: CC's $m$ is half the prolate index, so their
$\chi_2$ is prolate index 4, and their $\psi_2$ is $\mathit{PS}_{4,0}$.

Two further consequences, and the first is not cosmetic.

### 2.1 CC's $\phi_2$ satisfies only *one* of the two conditions exactly, and the repair is free

$\chi_0=\chi_2$ only approximately, so $\phi_2$ has $\phi_2(0)=0$ exactly but
$$\widehat{\phi_2}(0)=(\chi_0-\chi_2)\,\psi_0(0)\psi_2(0)\;\neq\;0,
\qquad |\chi_0-\chi_2|\simeq1-\chi_2 .$$
That is not a rounding remark. By Poisson,
$\mathcal E f(x)=x^{-1/2}\big[\sum_{m>0}\widehat f(m/x)+\tfrac12\widehat f(0)\big]$,
so a non-zero $\widehat f(0)$ puts an $x^{-1/2}$ tail on $\mathcal Ef$ as $x\to0$
— which is not in $L^2(d^*u)$ near $0$ — and equivalently a pole in
$\mathcal F_\mu(\mathcal Ef)$ at $s=\pm\tfrac i2$. **That is exactly what the two
conditions are for**, and it is why CC's appendix insists their $P^{ev}_\ell$ is
"divisible by $\tfrac14+s^2$" (`:1600`). §6's identity needs $\mathcal E\phi$ to
be an honest $L^2$ function, so the residual must be removed, not tolerated.

**It can be removed exactly, and at negligible cost, with a third mode.** Take
$\phi=b_0\psi_0+b_2\psi_2+b_4\psi_4$ (prolate indices $0,4,8$; all three have
$\chi\simeq+1$, so nothing leaves the even sector) and impose both conditions.
Writing $u_m=b_m\psi_m(0)$, the system $\sum u_m=0$, $\sum\chi_mu_m=0$ gives
$$\frac{u_4}{u_2}=-\frac{\chi_0-\chi_2}{\chi_0-\chi_4}
\;\simeq\;-\frac{1-\chi_2}{1-\chi_4},\qquad u_0\simeq-u_2 .$$
So the exact solution is CC's $\phi_2$ plus an admixture of prolate index 8 of
relative weight $(1-\chi_2)/(1-\chi_4)$, which Fuchs puts at $1.3\times10^{-8}$
at $\mu=12$. Its contribution to the out-of-band energy is
$|b_4|^2(1-\Lambda_8)\sim|b_2|^2(1-\Lambda_4)\cdot\frac{1-\chi_2}{1-\chi_4}$ —
smaller than the index-4 term by that same factor.

**The two conditions are therefore satisfiable exactly, the vector is still
essentially $\phi_2$, and the governing defect is still $1-\Lambda_4$.** (This
$1.3\times10^{-8}$ uses the general-$n$ Fuchs ratio, whose *form* §3 verifies at
$n=0,2,4$ but which is not computed at $n=8$ here; it is a correction to a
correction and nothing below turns on it.)

### 2.2 The weight

Normalising, the weight on the index-4 mode is
$\psi_0(0)^2/(\psi_0(0)^2+\psi_2(0)^2)$, which tends to $8/11$ in the Hermite
limit — mg-aedf's constant, and `start.tex`'s $h_4-\sqrt{3/8}\,h_0$. So the
out-of-band energy of the normalised prolate vector is
$\tfrac8{11}(1-\Lambda_4)(1+o(1))$, and $8/11$ is the one place a corpus
constant enters the size of $s(\mu)$.

---

## 3. Fuchs at general index, and Connes' constant — *verification*

The ticket flags the Slepian/Fuchs asymptotic as reaching mg-7606 second-hand,
through `s3-reduction-audit.md`, at index 0. `semilocal-gap.md` §5.3 (mg-03f0)
already closed `citation-audit.md`'s U4 on this constant, by checking the
general-$n$ form against Connes' printed one — **two formulas, agreeing to twelve
decimals**. What was not done, and is done here, is checking either of them
against the thing they approximate. It matters: over the range where $s(\mu)$ is
computed the asymptotic is $11$–$31\%$ off at $n=4$.

**The asymptotic.** Fuchs 1964, Theorem 1, in the form Connes cites:
$$1-\Lambda_n(c)\;\sim\;\frac{4\sqrt\pi\,8^n\,c^{\,n+\frac12}}{n!}\,e^{-2c}.$$
At $n=0$ this is $4\sqrt{\pi c}\,e^{-2c}$, mg-7606's quoted form.

**The identification of Connes' constant.** $\chi_2=\sqrt{\Lambda_4}$, so
$1-\chi_2=\tfrac12(1-\Lambda_4)+O((1-\Lambda_4)^2)$, and at $c=2\pi\mu$
$$\tfrac12\cdot\frac{4\sqrt\pi\,8^4}{4!}(2\pi)^{9/2}
=\frac{4096\sqrt\pi}{12}\,2^{9/2}\pi^{9/2}
=\frac{2^{14}\sqrt2\,\pi^5}{3}.$$
Check 1 of the script evaluates both sides at $100$ digits and the difference is
$1.4\times10^{-101}$. **Connes' statement is Fuchs at index 4, halved.** That is
not a coincidence to be noted; it is the confirmation that the index in the
published asymptotic is 4 and that the convention chain
$\chi_k^2=\lambda_{2k}(a)$, $a=\sqrt{2\pi}\lambda$, $c=a^2=2\pi\mu$ closes.

**The asymptotic against the exact defect.** This is the comparison mg-03f0 did
not make — it checked Connes' printed constant against the general-$n$ form,
which is two formulas. Check 1, at $260$ digits, checks the formula against the
thing it approximates. Ratio (asymptotic / exact):

| $c$ | $n=0$ | $n=2$ | $n=4$ |
|---|---|---|---|
| $2\pi\cdot5=31.416$ | $1.01432$ | $1.09378$ | $1.31219$ |
| $2\pi\cdot8=50.265$ | $1.00885$ | $1.05655$ | $1.17936$ |
| $2\pi\cdot12=75.398$ | $1.00587$ | $1.03699$ | $1.11442$ |
| $120$ | $1.00367$ | $1.02292$ | $1.06965$ |
| $200$ | $1.00220$ | $1.01362$ | $1.04092$ |
| $280$ | $1.00157$ | $1.00969$ | $1.02897$ |

Fuchs *over*-estimates, by $1+O(1/c)$ — the $n=4$ column times $c$ gives
$9.80,9.01,8.63,8.36,8.18,8.11$, converging on a constant, which is the shape the
correction should have. **But over the whole range where $s(\mu)$ is computed the
error is $11$–$31\%$.** So the asymptotic is not accurate enough to serve as the
comparison object, and §4 compares against the exact $1-\chi_2$ instead. (It also
means the fitted constant $D$ in the table above is being compared with an
asymptotic constant, so the $0.49\sigma$ there is the weakest of the three
lines. Correct that bias and the fit sits *above* the asymptotic, which is where
the exact defect is too.)

**How the defects are computed.** The concentration operator
$\mathcal P_\lambda\widehat{\mathcal P_\lambda}\mathcal P_\lambda$ cannot be
diagonalised directly here: its top eigenvalues agree to fifty-five decimal
places. The Bell Labs commuting differential operator is what makes the
computation possible at all — in the normalised Legendre basis it is symmetric
tridiagonal with **well separated** eigenvalues, and $\Lambda_n$ is recovered
from
$$\Lambda_n=\frac{c}{2\pi}\mu_n^2,\qquad
\mu_n=\frac{\int_{-1}^1\psi_n}{\psi_n(0)}\quad(n\ \text{even}),$$
which is the finite Fourier transform identity at $x=0$. Check 0 validates the
apparatus three ways: $\Lambda_0(1)=0.572581780638\ldots$ against Slepian's
tabulated $0.57258$; agreement to every printed digit with a second, independent
eigensolver (mpmath's dense Householder+QL on the same matrix, instead of
bisection plus inverse iteration); and Check 5 shows no movement across working
precisions $80$–$200$ digits and Legendre truncations $K=165,220$.

---

## 4. The confrontation — *ours*

Check 2. $s(\mu)$ is **recomputed here** (the machinery is
`verify_deficit_repair.py`'s, imported; nothing is copied from a note), at
$N=100$ and $120$ digits, which reproduces `deficit-repair.md` §4.1.

| $\mu$ | $s(\mu)$, $N=100$ | $1-\Lambda_0$ | $s/(1-\Lambda_0)$ | $1-\chi_2$ | $s/(1-\chi_2)$ |
|---|---|---|---|---|---|
| $5$ | $1.00502\times10^{-17}$ | $2.02073\times10^{-26}$ | $4.974\times10^{8}$ | $1.29839\times10^{-18}$ | $7.741$ |
| $6$ | $8.21103\times10^{-23}$ | $7.73821\times10^{-32}$ | $1.061\times10^{9}$ | $1.07935\times10^{-23}$ | $7.607$ |
| $7$ | $7.73054\times10^{-28}$ | $2.91979\times10^{-37}$ | $2.648\times10^{9}$ | $7.78995\times10^{-29}$ | $9.924$ |
| $8$ | $4.58127\times10^{-33}$ | $1.08993\times10^{-42}$ | $4.203\times10^{9}$ | $5.07899\times10^{-34}$ | $9.020$ |
| $9$ | $3.13549\times10^{-38}$ | $4.03552\times10^{-48}$ | $7.770\times10^{9}$ | $3.06721\times10^{-39}$ | $10.223$ |
| $10$ | $1.78439\times10^{-43}$ | $1.48462\times10^{-53}$ | $1.202\times10^{10}$ | $1.74467\times10^{-44}$ | $10.228$ |
| $11$ | $1.22587\times10^{-48}$ | $5.43359\times10^{-59}$ | $2.256\times10^{10}$ | $9.45817\times10^{-50}$ | $12.961$ |
| $12$ | $5.53055\times10^{-54}$ | $1.98020\times10^{-64}$ | $2.793\times10^{10}$ | $4.92908\times10^{-55}$ | $11.220$ |

Read the two ratio columns against each other:

- against $1-\Lambda_0$, the ratio is $\sim10^9$ and it **grows by a factor
  $56$** across the range. Almost all of that ($38.7$ of it) is the growth of the
  defect ratio $(1-\chi_2)/(1-\Lambda_0)$ itself, which is $\mu^{4.3}$ over this
  range: Fuchs' index ratio $8^4c^4/4!$ contributes $\mu^4$ and the rest is the
  $1+O(1/c)$ correction, which is larger at $n=4$ than at $n=0$. The index-0
  hypothesis is not off by a constant; it is off by the whole of the index-4
  prefactor.
- against $1-\chi_2$, the ratio is between $7.6$ and $13.0$, and the residual
  growth from $\mu=5$ to $\mu=12$ is a factor $1.45$.

**A factor of ten, nearly flat, against nine orders of magnitude with a $\mu^4$
drift.** That is the discrimination the rate could not make.

One structure worth recording rather than smoothing: the ratio is *largest* at
$\mu=7,9,11$ — each of them the last integer before a prime power enters the
form ($7$, $9$, $11$). $s$ is at its largest just before a new prime power
arrives to repair it. This is `deficit-repair.md` §3's oscillation of $R-D$
("maxima just after a new prime power enters") seen from the near-radical
direction, and it is a reminder that $s(\mu)$ at integer $\mu$ is sampling a
function with arithmetic structure at exactly the scale of the sample spacing.

---

## 5. The truncation bias, measured rather than asserted — *ours*

The ticket's standing constraint: truncation is variational and cuts one way, so
any argument that treats the computed $s$ as the true $s$ must say why. This
note does not treat it as the true $s$; it measures the gap.

Restricting the form to $|n|,|m|\le N$ can only raise $\lambda_{\min}$, so every
$s$ in §4 is an **upper** bound, looser at larger $\mu$ — which is the direction
that inflates the ratio $s/(1-\chi_2)$ at large $\mu$. Check 3 computes $s(\mu)$
at $N=60,80,100,120$ and extrapolates geometrically in $N$:

| $\mu$ | $N=60$ | $N=80$ | $N=100$ | $N=120$ | $N\to\infty$ | $s/(1-\chi_2)$, $N=120$ | extrapolated |
|---|---|---|---|---|---|---|---|
| $5$ | $-16.94910$ | $-16.97792$ | $-16.99782$ | $-17.01077$ | $-17.03490$ | $7.513$ | $7.107$ |
| $6$ | $-22.06885$ | $-22.07379$ | $-22.08560$ | $-22.09862$ | — | $7.383$ | — |
| $7$ | $-27.05853$ | $-27.10720$ | $-27.11179$ | $-27.11514$ | $-27.12414$ | $9.848$ | $9.645$ |
| $8$ | $-32.28306$ | $-32.30323$ | $-32.33901$ | $-32.34980$ | $-32.35446$ | $8.799$ | $8.705$ |
| $9$ | $-37.42317$ | $-37.49099$ | $-37.50370$ | $-37.52958$ | — | $9.631$ | — |
| $10$ | $-42.65705$ | $-42.71119$ | $-42.74851$ | $-42.75834$ | $-42.76185$ | $9.999$ | $9.918$ |
| $11$ | $-47.78865$ | $-47.86311$ | $-47.91156$ | $-47.95051$ | $-48.11014$ | $11.849$ | $8.205$ |
| $12$ | $-53.03665$ | $-53.20270$ | $-53.25723$ | $-53.29056$ | $-53.34293$ | $10.391$ | $9.211$ |

(columns 2–6 are $\log_{10}s$; the last two are the ratio at the finest
truncation and after extrapolation. At $\mu=6$ and $\mu=9$ the last two
increments are not decreasing, so the geometric fit refuses and no
extrapolation is reported — that is the fit declining, not the sequence
diverging.)

The extrapolation is a three-point geometric fit and is a model, not a theorem —
but it can only move the ratio **down**, and it moves it down more at large $\mu$.
What survives is a ratio of order ten — $7.11,\ 9.65,\ 8.71,\ 9.92,\ 8.21,\ 9.21$
at $\mu=5,7,8,10,11,12$ — spanning a factor of $1.40$ **with no monotone trend
left in it.** At $N=100$ the ratio rose by $1.45$ across the range; after
extrapolation the rise is gone.

That is all the rate claim needs. **A sub-polynomial residual cannot change an
exponential rate.** On this evidence $\kappa=s/(1-\chi_2)$ is simply a constant of about $9$, and the
apparent growth at fixed $N$ was bias. That is a stronger reading than the note
needs and the extrapolation is a three-point model, so the claim made here is
only the weak one: **$\kappa$ grows no faster than $\log\mu$**, which is also
what §6's missing inequality would produce, since the mean density of zeros near
height $T$ is $\frac1{2\pi}\log\frac T{2\pi}$. Either way it is sub-polynomial
and cannot touch an exponential rate.

---

## 6. The derivation, and the one inequality it is missing — *ours*

Everything in §1 is exact except the last step, and the last step is where a
proof would live. Here is what the chain actually gives.

Let $\phi$ be the normalised three-mode vector of §2.1 — CC's $\phi_2$ with the
index-8 correction that makes $\phi(0)=\widehat\phi(0)=0$ hold **exactly**, so
that $\mathcal E\phi\in L^2(d^*u)$ and $\mathcal F_\mu(\mathcal E\phi)$ has no
pole at $s=\pm\tfrac i2$. Then $\operatorname{supp}\phi\subseteq[-\lambda,\lambda]$
and $\phi\in\mathcal S_0^{ev}$ in every respect except smoothness at
$\pm\lambda$, which the compact support makes harmless for $\mathcal E$ (the sum
$\sum_{n>0}\phi(nx)$ is finite for each $x>0$). Put
$$g:=\mathcal E(\phi)\big|_{[\lambda^{-1},\lambda]},\qquad
r:=\mathcal E(\phi)\big|_{(0,\lambda^{-1})},\qquad
\mathcal E(\phi)=g+r$$
— the decomposition is exhaustive because $\operatorname{supp}\mathcal E\phi
\subseteq(0,\lambda]$ by §1 step 2, so nothing spills *above* $\lambda$.

**(a) The identity.** $\mathcal F_\mu(\mathcal E\phi)$ vanishes on $Z$ (§1 step
1), so $\mathcal F_\mu g=-\mathcal F_\mu r$ on $Z$ and
$$QW_\lambda(g,g)\;=\;\sum_{\frac12+is\in Z}\big|\mathcal F_\mu r(s)\big|^2 .$$
This is an identity, and it is the conceptual content: **$QW_\lambda$ evaluated
at the prolate vector is the Weil form of the part of $\mathcal E\phi$ that falls
outside the window.** The near-radical is not "nearly in the kernel" by accident;
it is exactly as far from the kernel as the construction fails to fit inside
$[\lambda^{-1},\lambda]$.

**(b) The size of the spill.** By Poisson (§1 step 3), for $x<\lambda^{-1}$,
$\mathcal E\phi(x)=\mathcal E\widehat\phi(x^{-1})$, so with $y=x^{-1}>\lambda$,
$$\|r\|^2_{L^2(d^*u)}=\int_\lambda^\infty\Big|\sum_{n>0}\widehat\phi(ny)\Big|^2dy .$$
The $n=1$ diagonal term is $\int_\lambda^\infty|\widehat\phi|^2
=\tfrac12\big\|(1-\widehat{\mathcal P_\lambda})\phi\big\|^2$, half the
out-of-band energy of $\phi$. That energy splits **exactly** across the prolate
modes: the in-band parts are mutually orthogonal, since
$\langle\widehat{\mathcal P_\lambda}\psi_n,\widehat{\mathcal P_\lambda}\psi_m\rangle
=\langle\psi_n,\mathcal P_\lambda\widehat{\mathcal P_\lambda}\mathcal P_\lambda
\psi_m\rangle=\Lambda_m\delta_{nm}$, so the out-of-band parts are too, and
$$\big\|(1-\widehat{\mathcal P_\lambda})\phi\big\|^2=\sum_m|b_m|^2(1-\Lambda_{2m})
=w\,(1-\Lambda_4)\,(1+o(1)),\qquad w\to\tfrac8{11},$$
because $1-\Lambda_0$ is smaller than $1-\Lambda_4$ by a factor $4!/(8^4c^4)$ and
the index-8 admixture of §2.1 is smaller by $(1-\chi_2)/(1-\chi_4)$. **So $\|r\|^2\asymp(1-\chi_2)$, linearly**, which is `start.tex:39`'s
$QW_\lambda(\mathcal Eh_\lambda)\asymp1-\chi_4$ with the index convention of
`index-convention.md` — the corpus's central estimate is the $n=1$ term of this
line.

The $n\ge2$ terms and the cross terms are not free: $\widehat\phi$ decays only
like $y^{-1}$ off-band, and $\sum_{n\ge1}$ of the Cauchy–Schwarz bounds is
logarithmically divergent before the oscillation of $\widehat\phi$ is used. So
(b) as stated needs its own small argument; the honest form is
$\|r\|^2=C_1(\lambda)(1-\chi_2)$ with $C_1$ conjecturally $O(\log\mu)$.

**(c) The missing inequality.** To convert (a)+(b) into a bound on $s$ one needs

> **(H1)** There is $\Theta(\lambda)$, subexponential in $\mu$, with
> $\displaystyle\sum_{\frac12+is\in Z}|\mathcal F_\mu r(s)|^2\le\Theta(\lambda)\|r\|^2$
> for the spill $r$.

This is a mean-value estimate for the zeta zeros as a sampling set, of
Plancherel–Pólya type. It is not automatic: $QW_\lambda$ takes values in
$(-\infty,+\infty]$ (`:289`) and is **unbounded above**, so no uniform $\Theta$
exists on $L^2$; (H1) must use the specific $r$, which is smooth on
$(0,\lambda^{-1})$ but has a jump at the endpoint, so $\mathcal F_\mu r$ decays
only like $|s|^{-1}$ and the sum converges only because the zero density is
logarithmic. The expected size of $\Theta$ is $O(\log\mu)$, which is what §5
measures.

**(d) What follows.** Under (H1), and with $\|g\|^2$ bounded below (call it
(H0); $\|g\|^2=\|\mathcal E\phi\|^2-\|r\|^2$ and
$\|\mathcal E\phi\|^2=\frac1{2\pi}\int|\Gamma_{\mathbb R}(\tfrac12-is)
\zeta(\tfrac12-is)P_\phi(s)|^2ds$, so this is a statement about a mean value of
$|\zeta(\tfrac12+it)|^2$ against an explicit weight — routine but not free),
$$s(\mu)\;\le\;\frac{QW_\lambda(g,g)}{\|g\|^2}\;\le\;
\frac{\Theta(\lambda)C_1(\lambda)}{\|g\|^2}\,(1-\chi_2(\lambda)),$$
hence
$$\limsup_{\mu\to\infty}\frac{\log s(\mu)}{\mu}\;\le\;-4\pi .$$

**That is a real half of the answer**, and it is the half every number in this
project is consistent with, because every computed $s$ is itself an upper bound.
It also says the direction of the residual bias in §5 and the direction of the
truncation bias in mg-7606 §5 are the *same* direction, which is why the fitted
$A$ under-estimating and the identification being an upper bound are one fact
and not two.

---

## 7. The other half is RH — *ours*

A rate is two-sided. The remaining half is: $s(\mu)$ does not decay *faster*
than $e^{-4\pi\mu}$, i.e. a lower bound
$$s(\mu)\;\ge\;\kappa(\mu)\;>\;0\qquad\text{for all }\mu .$$

Connes states the equivalence in the survey (`rhready.tex:1145`): "By the result
of André Weil discussed in §`sectweilpos`, the positivity of $QW_\lambda$ for all
$\lambda>1$ **is equivalent to RH**." Connes–Consani state the same at
`Spectraltriples.tex:169`. Therefore:

> **Any theorem of the form $\min(s^+(\mu),s^-(\mu))\ge\kappa(\mu)>0$ for all
> $\mu$ implies RH.** A theorem that additionally pins the rate is strictly
> stronger, since RH gives positivity with no rate at all.

Two remarks on the shape of that, because both are places one might hope to
slip through.

- **Restricting to large $\mu$ does not help.** The supports are nested, so
  $QW_\Lambda\ge0$ implies $QW_\lambda\ge0$ for every $\lambda<\Lambda$: a lower
  bound valid for all $\mu\ge\mu_0$ already gives positivity for *all* $\lambda$.
- **Dropping the sign does help — and that is the tell.** The statement
  $|s(\mu)|=e^{-4\pi\mu+o(\mu)}$, with no claim that $s>0$, does *not* formally
  imply RH. But that statement is invariant under
  $W_\lambda\mapsto-W_\lambda$, and by the house rule it is therefore not the
  statement anyone wants: it is compatible with the form being negative on the
  near-radical at every $\mu$. **The only version of "the rate is $4\pi$" that
  says anything about the sign of the Weil form is the version that contains
  RH.** That is not a technicality about how the claim is phrased; it is the
  same fact as the sign-blindness of the whole prolate mechanism, arriving from
  the other side.

Two things follow, and they are the point of this note.

1. **The $4\pi$ rate cannot be made an unconditional theorem.** Not for want of
   technique: the statement contains RH. mg-7606's T2 ("prove the rate $4\pi$")
   is therefore not a tractable open problem of the kind its neighbours T1, T4,
   T5 are; it is RH with a decoration. It should be restated as the upper bound,
   which is provable in principle and is what §6 sets up.
2. **No amount of numerics can settle it either**, which retires the reflex that
   a wider grid or a converged $N$ would upgrade $0.12\sigma$. A wider grid
   sharpens $A$; it cannot supply a lower bound at any $\mu$ it has not
   computed, and the statement quantifies over all $\mu$.

**The house rule predicted this.** §1's mechanism — the radical contains
$\operatorname{ran}\mathcal E$, the near-radical is the failure of a
double-support condition, the size is a concentration defect — is entirely
invariant under $W_\lambda\mapsto-W_\lambda$. A kernel is a kernel either way; a
concentration defect is a magnitude. So the prolate story explains why $|s|$ is
minuscule and says **nothing whatever** about why $s>0$. It is exactly that
sign-blindness that forces the lower bound to carry the whole arithmetic content,
and RH is the arithmetic content. The standing test located the obstruction
before the analysis did.

---

## 8. The house rule, applied to this note

> **Is any statement in this note false for $-W_\lambda$?**

| item | under $-W_\lambda$ | verdict |
|---|---|---|
| 1. the index is 4, not 0 | a statement about $\mathcal E$'s domain and the prolate phase; unchanged | **sign-blind** |
| 2. $s/(1-\chi_2)\in[7,13]$ | $\lambda_{\min}(-\sigma^+)=-\lambda_{\max}(\sigma^+)$, which is large and negative and grows without bound in $N$ (mg-7606 §7) | **FALSE for $-W$** |
| 3. $QW_\lambda(g)=\sum_Z|\mathcal F_\mu r|^2$ | both sides negate; the identity survives | **sign-blind** |
| 4. $0<s(\mu)\le\Theta C_1\|g\|^{-2}(1-\chi_2)$ | the left inequality fails | **FALSE for $-W$** |
| 5. a lower bound for all $\mu$ implies RH | for $-W$ the hypothesis asserts $\sigma^+\prec0$, false already at $\mu=2$ where $\lambda_{\max}=5.4855$ | **FALSE for $-W$** |
| 6. the rate $4\pi$ | magnitude only | **sign-blind** |

Three of the six are sign-blind, and §7 says so in the strongest available form:
**the sign-blindness is not a defect of the exposition, it is the finding.** The
prolate mechanism is a magnitude mechanism; the sign is elsewhere; and the
elsewhere is RH. Items 2, 4, 5 are the sign-bearing ones and each is an
inequality about $\lambda_{\min}$ of the actual form.

Warning to whoever quotes this, in the spirit of `deficit-repair.md` §7's:
"$s(\mu)$ is governed by $1-\chi_2$" is by itself invariant under
$W\mapsto-W$. It is sign-bearing only as "$0<s(\mu)\le\ldots$", and the left
half of that is RH.

---

## 9. What this does to `deficit-repair.md`

Three changes, annotated in place there and stated here in full.

**(i) §5's rate claim must be narrowed, and the correction was already in the
repository — twice.** §5 says: "They plot $\log s$ against $\mu$ and call the
behaviour 'exponential' (`:645`); **no rate is given there or anywhere else in
the paper**." True of arXiv:2106.01715. But:

- `semilocal-gap.md` §5.2 (mg-03f0, merged `b819a1d`, **two commits before**
  `deficit-repair.md`) block-quotes `rhready.tex:1149`, reproduces
  $1-\chi_2\sim\frac{2^{14}}3\sqrt2\pi^5e^{-4\pi e^L+9L/2}$ with the footnote
  $\chi_k^2=\Lambda_{2k}$, and states in bold that **Connes' $\chi_2$ is prolate
  index 4, the corpus's $\chi_4$**. Its §5.3 closes `citation-audit.md` item U4
  — the general-$n$ Fuchs constant — against that same line.
- `citation-audit.md` row 14, as narrowed by mg-03f0 and applied by mg-6d7e,
  says the same in one sentence.

And `deficit-repair.md`'s own first paragraph cites `semilocal-gap.md` as the
note it continues. So the index was not missing, and the survey was not
unopened: **§5 reached past both for `s3-reduction-audit.md`'s index-0 Slepian
formula, because that was the formula in the note it was reading.** The vision's
CURRENT STATE also records the published asymptotic, and item 12 of it —
"THE RESULT: the rate is $4\pi$ … Connes–Consani plot that decay and never name
its rate; we supply it" — inherits the same narrowing: the rate of $1-\chi_2$ is
Connes'; the rate of $s(\mu)$ is still nobody's theorem.

So the correct attribution is:

- the asymptotic for $1-\chi_2$, including $4\pi$, $9/2$ and the constant:
  **Connes 2026**, from Fuchs 1964; recorded here by **mg-03f0**;
- $\chi_2\leftrightarrow$ prolate index 4 $\leftrightarrow$ the corpus's
  $\chi_4$: **mg-03f0** and `index-convention.md` (mg-9433);
- the identification of $\epsilon(\lambda)$ with $1-\chi_2$: **Connes 2026**, as
  a figure and the words "striking similarity" — with no constant, and mg-03f0
  records it as such;
- that the *rate alone cannot discriminate the index*, so the $0.12\sigma$ was
  passed by every candidate: **ours**;
- the *quantitative* confrontation — exact $1-\chi_2$ and $1-\Lambda_0$ in
  arbitrary precision against a recomputed $s(\mu)$, with the truncation bias
  extrapolated: **ours**. This is the ratio Connes has only as a figure;
- the three-parameter test against mg-7606's fit, and the closure of T3:
  **ours**;
- Fuchs at general index checked against *exact* prolate eigenvalues rather than
  against Connes' printed form (mg-03f0 compared two formulas to twelve
  decimals; here the formula is compared to the thing it approximates, and it is
  $11$–$31\%$ off over the range where $s$ is computed): **ours**;
- the identity $QW_\lambda(g)=\sum_Z|\mathcal F_\mu r|^2$, the exactness of the
  orthogonal splitting of the out-of-band energy, and the observation that CC's
  two-mode $\phi_2$ satisfies $\widehat\phi(0)=0$ only to $O(1-\chi_2)$ and
  needs a third mode: **ours**;
- the RH-equivalence of the lower bound, hence the unreachability of T2 as
  posed: **ours as an observation**, from Connes' and Weil's statements.

This is the fourth time in this project that a claim was stated at higher
confidence than its evidence, and the fourth time the fix was one file away
(vision amendment 4 §3). But the mechanism is different enough to name
separately. The earlier three were *a downstream summary quoted instead of a
source*. This one is worse and easier to repeat: **the source had been opened,
by us, two commits earlier, and its conclusion written into two notes and the
vision — and the later note still used the older, nearer formula, because that
formula was in the document it was continuing.** Proximity beat provenance, and
the provenance was our own.

**(ii) T3 is closed.** "The $B=5.32$ in the fit — not the $\tfrac12$ the naive
Slepian prefactor predicts. Either the subleading structure differs or the fit is
absorbing a truncation drift." Neither: the prediction was never $\tfrac12$. At
the forced index the prefactor is $n+\tfrac12=9/2$ and the fit is $0.86\sigma$
from it. T3 was the index-0 hypothesis leaving a visible mark, and it is the one
place in mg-7606 where the wrong index was already showing.

**(iii) T2 must be restated.** "Prove the rate $4\pi$ … the route would be to
evaluate $QW_\lambda$ directly on Connes–Consani's prolate near-radical vectors
rather than on the numerical eigenvector." The route is right and §6 carries it
out to an identity; but the *goal* as stated is unreachable, because the rate is
two-sided and its lower half implies RH. T2 splits:

- **T2a (open, and a real problem):** prove (H1) — the mean-value bound over the
  zeros for the spill $r$ — and (H0). That gives
  $\limsup\mu^{-1}\log s\le-4\pi$ unconditionally.
- **T2b (not open — it is RH):** the matching lower bound.

---

## 10. Provenance

To the standard of `citation-audit.md` §9 and `deficit-repair.md` §8.

**Read as primary source**, from arXiv LaTeX downloaded 2026-08-12:

- `arxiv.org/e-print/2106.01715`, `Spectraltriples.tex`: `:160`–`:215` in full
  (the statement of $QW_\lambda$; the Weil-criterion sentence at `:169`; the
  $2.389\times10^{-48}$ at `:178`; the near-radical, the prolate identification
  and $\nu(\mu)\sim2\mu$ at `:184`–`:190`); `§riemweilexpl`, `:696`–`:770` in
  full (the radical of $QW$ contains $\operatorname{ran}\mathcal E$ at `:699`; the
  two support statements at `:704` and `:708`; the Slepian obstruction at `:711`;
  the prolate combinations $\phi_{2n},\phi_{2n+1}$ at `:744`;
  the $\epsilon_{2m}\leftrightarrow m$-th even eigenvalue statement at `:760`);
  `§sectsmall`, `:643`–`:660`; the appendix "Size of
  $\mathcal F_\mu\circ w$(Prolate)", `:1547`–`:1630`, for
  $\mathcal F_\mu(\mathcal E\psi^{ev}_\ell)=\Gamma_{\mathbb R}\zeta P^{ev}_\ell$.
- `arxiv.org/e-print/2602.04022`, `rhready.tex`: `:1123`–`:1155` in full — the
  Slepian fact at `:1123`, $\chi_m^2=\nu_m$ and the naming of $\chi_0,\chi_2$ as
  belonging to $h_{0,\lambda},h_{4,\lambda}$ at `:1134`; the Weil-criterion
  equivalence, $A_\lambda$ and $QW_\lambda(f,f)=\langle A_\lambda f\mid f\rangle$ at
  `:1145`–`:1147`; $\epsilon(\lambda)$, the "striking similarity" and the
  asymptotic with its Fuchs footnote at `:1149`; Figure `fpro1` at `:1153`.

**Second-hand, and marked:** Fuchs 1964, *On the eigenvalues of an integral
equation arising in the theory of band-limited signals*, J. Math. Anal. Appl. 9,
Theorem 1, is **not** read here. Its statement is taken in the form Connes cites
it, and it is then **verified against an independent arbitrary-precision
computation** of $\Lambda_0,\Lambda_2,\Lambda_4$ (§3, check 1) — the ratio
asymptotic-to-exact tends to $1$ like $1+O(1/c)$ at all three indices. That is
not a substitute for reading Fuchs, and if the general-$n$ constant were wrong
this note's $B$ and $D$ predictions would move; the $A$ prediction would not.
Slepian's tabulated $\Lambda_0(1)=0.57258$ is likewise quoted from the standard
literature and used only as a five-digit sanity check.

**Taken from our own earlier notes, not re-derived** — and the point of §9 is
that mg-7606 should have taken them too: that Connes' $\chi_2$ is prolate index 4
and the corpus's $\chi_4$ (`semilocal-gap.md` §5.2, `citation-audit.md` row 14,
`index-convention.md`); that Connes' printed asymptotic and the general-$n$ Fuchs
form are the same expression (`semilocal-gap.md` §5.3, closing U4); the $8/11$ and
$\sqrt{3/8}$ (mg-aedf, `s3-reduction-audit.md`); that mode selection is forced by
the finite-Fourier phase $i^n$ (mg-aedf). §3 re-derives the second of these in a
different normalisation and §2 re-derives the last in the prolate rather than the
Hermite limit, but neither is claimed as new.

**Derived here, not taken from any source** — each marked *ours* at the point of
use: that the *rate* is index-independent and therefore cannot discriminate (§0,
§4); the tie between the forced index and $\mathcal E$'s **domain**, i.e. that the
two conditions collapse to one exactly when the characteristic values agree (§2);
that CC's two-mode $\phi_2$ meets $\widehat\phi(0)=0$ only to $O(1-\chi_2)$, what
that costs, and the three-mode repair (§2.1); Fuchs checked against *exact*
prolate eigenvalues rather than against another formula (§3); the exact prolate
defects and the confrontation with $s(\mu)$ (§4); the measured truncation bias
and the extrapolated ratio (§5); the identity
$QW_\lambda(g)=\sum_Z|\mathcal F_\mu r|^2$, the exact orthogonal splitting of the
out-of-band energy, and the reduction of the upper bound to (H0)+(H1) (§6); the
RH-equivalence of the lower bound and therefore of the two-sided rate, including
that only the sign-blind version of the rate claim escapes it (§7).

**The claim in this note that would do the most damage if wrong** is §4's
ratio, because §§2, 6, 7 are all readings of it. Its exposures are two: the
prolate solver (guarded by check 0's independent eigensolver and check 5's
precision stability), and the possibility that the near-flatness of
$s/(1-\chi_2)$ over $\mu=5..12$ is an accident of a short range — eight integer
points spanning a factor $2.4$ in $\mu$, on a quantity that varies by $37$ orders
of magnitude across them. The second is not guarded and cannot be, at this cost.

---

## 11. Open

| # | item | why it is open |
|---|---|---|
| **P1** | Prove (H1): $\sum_{Z}|\mathcal F_\mu r(s)|^2\le\Theta(\lambda)\|r\|^2$ for the spill, with $\Theta$ subexponential | This is mg-7606's T2 with the unreachable half removed. It is a mean-value estimate over the zeros for one explicit function and it is the whole remaining content of the upper bound |
| **P2** | Prove (H0): $\|g\|^2$ bounded below, i.e. a lower bound for $\int|\zeta(\tfrac12+it)P_\phi|^2$ against the archimedean weight | Routine in shape, but $P_\phi$ depends on $\lambda$ and the bound must be uniform |
| **P3** | Is $\kappa(\mu)=s/(1-\chi_2)$ a constant, and is it about $9$? | §5's extrapolated values are $7.1$–$9.9$ with no trend, which suggests a constant; but the extrapolation is a three-point model over eight points and cannot separate a constant from $\log\mu$. Distinguishing them needs converged $s$ over a wider range, or the constant in (H1) |
| **P4** | The odd sector | CC's $\phi_3=\psi_3\psi_1(0)-\psi_1\psi_3(0)$ is built from $\mathit{PS}_{6,0}$ and $\mathit{PS}_{2,0}$, so the odd smallest eigenvalue should be governed by $1-\chi_3$, i.e. prolate index **6** — a *different* power, $13/2$, at the same rate $4\pi$. Not checked here, and it is a sharp prediction: mg-7606's T4 now has a number to aim at |
| **P5** | Evaluate $QW_\lambda$ on $g$ directly and compare with $s(\mu)$ | §6(a) makes this the cleanest possible test of the whole chain — it would replace CC's twelve figures with a ratio. Not done here: $\mathcal E\phi$ has jump discontinuities at $u=\lambda/n$, so its coefficients in the $\xi_j$ basis decay like $j^{-1}$ and the truncated Rayleigh quotient may be dominated by the tail rather than by the $10^{-54}$ it is trying to measure. Worth one ticket, with panel quadrature at the breakpoints |
