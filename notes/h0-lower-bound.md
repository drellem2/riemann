# H0 is not a mean value of $|\zeta(\tfrac12+it)|^2$: it is the non-degeneracy of the prolate vector, and that is published

Work item mg-6818. Companion script: [`verify_h0.py`](verify_h0.py) (needs `mpmath`;
no `numpy`; imports the prolate apparatus of [`verify_prolate_rate.py`](verify_prolate_rate.py),
the Legendre machinery of [`verify_h1.py`](verify_h1.py), the mode builder of
[`verify_q2.py`](verify_q2.py) — the one with the **fixed** `sph_j_all`, mg-9d43 — and the
three-mode near-radical vector `Comb` of [`verify_q3.py`](verify_q3.py)). Attacks **Q4**,
i.e. hypothesis **(H0)**, of [`h1-mean-value.md`](h1-mean-value.md) §9 — the last open item
between this project and an unconditional $-4\pi$ upper bound. (H0) is Hypothesis `H0` at
`../paper/positivity-obstruction.tex:1234`, and the second half of the paper's gap **G6**. <!-- mg-6467: the paper is revised; (H0) is now at `:1417` and G6 is recorded closed at `:2423`. --> <!-- mg-fc1c: both of those anchors had drifted and are re-measured against the content they name: `\begin{hypothesis}\label{H0}` is at `:1544` and G6's closed row at `:2712`. Same pass corrects the paper's statement of Dunster's hypothesis at its §§1.4, 1.6, 7.7 and G13 -- see §5's own annotations below and `dunster-check.md`. -->

Nothing in `start.tex`, `s3.tex` or the paper was edited. `h1-mean-value.md` and
`prolate-rate.md` are annotated in place (HTML comments, no line-count change) and appended to.

**Calibration, before anything else.** (H0) is a lower bound on $\|g\|^2$, the norm of the
*test vector*. It is **not** a lower bound on $s(\mu)$, which is RH (`rhready.tex:1145`,
paper Thm `thm:boundary`, gap **G10**), and nothing below approaches it: a larger $\|g\|^2$
makes the **upper** bound $s\le QW_\lambda(g,g)/\|g\|^2$ *smaller*, which is the safe
direction. §8 applies the house rule and the verdict is *sign-blind* at every line, as it must
be for a statement about a norm.

---

## Bottom line

**1. The description in §9 and in the paper is wrong in force, and the wrong word is
"mean value".** Both say (H0) "is a mean value of $|\zeta(\tfrac12+it)|^2$ against an explicit
weight". There is such an identity and it is correct —
$\|\mathcal E\phi\|^2=\frac1{2\pi}\int|\Gamma_{\mathbb R}(\tfrac12-is)\zeta(\tfrac12-is)P_\phi(s)|^2ds$
— but it is one **route** to $\|g\|^2$ and it is the harder one, because it computes the whole
norm when only a lower bound is wanted. $\|g\|^2$ is bounded below by
$\int_A^B|\mathcal E\phi|^2\,d^*u$ over **any fixed compact** $[A,B]\subset(0,\infty)$, for
every $\lambda\ge B$, and on a compact window $\mathcal E\phi$ is a **finite sum of on-band
values of one prolate function**. $\zeta$ never enters. §§2–3.

**2. What (H0) actually requires is that the prolate vector does not degenerate**, i.e. that
$\phi_\lambda$ converges — in $L^2(\mathbb R)$, with no mass escaping — to a fixed non-zero
function. That is the whole content, and it is visible from the mean-value route too: the
weight there is $|P_{\phi_\lambda}|^2$, it depends on $\lambda$, and it is the weight's
convergence and not any property of $\zeta$ that decides the question. The paper's own
sentence — "routine in shape, but $P_\phi$ depends on $\lambda$ and the bound must be
uniform" (`:1234`) — names the difficulty correctly and then attaches it to the wrong object. <!-- mg-6467: corrected in the paper, §7.7 at `:1950`. -->
§4.

**3. The limit is the corpus's own vector, and the constant is explicit.**
$\phi_\lambda\to\phi_\infty=\sqrt{8/11}\,(h_4-\sqrt{3/8}\,h_0)$, which is `start.tex:39`'s
$h_4-\sqrt{3/8}\,h_0$ normalised, with $8/11$ the weight of `prolate-rate.md` §2.2 and mg-aedf.
Hence, **measured to twelve digits by two independent computations**,
$$\|g\|^2\;\longrightarrow\;\|\mathcal E\phi_\infty\|^2\;=\;0.219247199549\ldots$$
§§4, 7.

**4. The convergence is published, with error bounds, in exactly our regime — and the
regime is the one that has repeatedly *not* been covered.** T. M. Dunster, *Asymptotics of
prolate spheroidal wave functions*, J. Classical Analysis **11** (2017), no. 1, 1–21,
doi:10.7153/jca-11-01, arXiv:1601.00699,
eq. **(124)** with eq. **(107)**: for fixed $m,n$ and $\gamma\to\infty$, uniformly on
$0\le x\le1-\delta_0$, $\mathrm{Ps}_n^m$ is a parabolic cylinder function of argument
$\hat\rho\sqrt{2\gamma}$ with relative error $O(\gamma^{-1}\log\gamma)$, and
$a=\lambda\gamma^{-1}+\gamma=2(n-m+\tfrac12)+O(\gamma^{-1})$. His $\lambda$ is our
$\chi_n-c^2$, so **his standing hypothesis $\lambda<0$ is exactly our $\chi_n<c^2$** — the <!-- mg-ff96: understated. His standing hypothesis is (29) at `:466`, sigma = sqrt(chi_n)/c <= sigma_0 < 1, which is strictly stronger; §5 below has it right, this summary does not. dunster-check.md §3. -->
hypothesis Osipov–Rokhlin's theorems negate (`h1-mean-value.md` §6) and the one Lemma 5.1 and
Q1 are built on. Dunster says so himself: his earlier paper assumed $\lambda>0$, "which does
not have many of the applications described above". §5.

**5. So (H0) is proved, and $\|g\|^2$ is not merely bounded below — it converges to an
explicit positive constant.** Theorem 6.1. The imported input is Dunster's (124)+(107); the
reduction to it, the tightness lemma, the continuity of $\mathcal E$ on a compact window and
the non-vanishing of $\mathcal E\phi_\infty$ are proved here. **The $-4\pi$ upper bound is
now unconditional**, and quantitative:
$$s(\mu)\;\le\;\big(4.5610\ldots+o(1)\big)\,\Xi(\mu)\,(1-\chi_2(\lambda)),\qquad
\Xi(\mu)=O(\mu^{6}\log^3\mu),$$
hence $s(\mu)=O(\mu^{21/2}\log^3\mu\;e^{-4\pi\mu})$ and
$\limsup\mu^{-1}\log s(\mu)\le-4\pi$, with no hypothesis left. §§6, 9.

**5a. One caveat on "unconditional", and it is inherited rather than mine.** Closing (H0) was
not quite enough: mg-731c's Thm 4.4 bounds the zero sum by $\Phi(1)^2$ and converts
$\Phi(1)^2\to(1-\chi_2)$ citing `h1-mean-value.md` §7, which is **observed**, its reverse half
recorded there as "sketched but not written out". §A writes it out — $\Phi(1)^2\le
2\pi cX_0\kappa^{-1}(1-\Lambda_n)=O(c^{5/2}(1-\Lambda_n))$, from `dilate-sum.md` Prop. 4.1(ii)
and the exact identity (4.1) — at a cost of $\mu^{3/2}$ over the observed truth, which is why
$\Xi$ above is $\mu^6$ and not mg-731c's $\mu^{9/2}$. **Without §A the word "unconditional"
would not have been earned by (H0) alone.** §A, §9.

**6. And the corollary never needed "bounded below" in the first place.** What
`cor:upper` consumes is $\mu^{-1}\log\|g\|^2\to0$; **any** lower bound $\|g\|^2\ge e^{-o(\mu)}$
— subexponential, not bounded — gives the same $-4\pi$. That matters because it is what makes
the crude localisation of §3 sufficient on its own, and because it is the sense in which (H0)
was over-stated from the start. §1.

**Which outcome of the ticket is this?** **(1)** and **(2)** together, plus **(4)**: (H0) is
proved, the one imported ingredient is a published theorem whose hypotheses were checked in the
source, and the §9 description of what (H0) *is* was wrong — the fourth inherited misdiagnosis
in a row on this chain (mg-6851 on §5, mg-9d43 on §§4/6, mg-731c on §3, this on §9's Q4 row).
**The correct closing sentence is not "H1 is proved"**: `h1-mean-value.md` §1 rules out the
$\|r\|^2$ form of (H1) outright, and what mg-731c established is **(4.3)**. §9.

---

## 0. Conventions, and the one place they can collide

$\lambda>1$, $\mu=\lambda^2$, $c=2\pi\mu$. $\Phi$ is the normalised three-mode prolate
combination on $[-1,1]$ at bandwidth $c$ — prolate indices $0,4,8$, `prolate-rate.md` §2.1,
$\int_{-1}^1\Phi^2=1$ — and
$$\phi(x)=\lambda^{-1/2}\Phi(x/\lambda)\ \ (|x|\le\lambda),\qquad \phi(x)=0\ \ (|x|>\lambda),
\qquad \|\phi\|_{L^2(\mathbb R)}=1 .$$
$\phi$ is admissible: $\phi(0)=0$ and $\widehat\phi(0)=\int\phi=0$, exactly. With
$$\mathcal E f(u)=u^{1/2}\sum_{n>0}f(nu),\qquad
g=\mathcal E\phi\big|_{[\lambda^{-1},\lambda]},\qquad r=\mathcal E\phi\big|_{(0,\lambda^{-1})},$$
norms are in $L^2(\mathbb R_+^*,d^*u)$ and $\|\mathcal E\phi\|^2=\|g\|^2+\|r\|^2$ because the
two supports are disjoint and exhaust $(0,\lambda]$.

$h_n$ is the **$\pi$-convention** Hermite function
$h_n(x)=(2^nn!)^{-1/2}2^{1/4}H_n(\sqrt{2\pi}\,x)e^{-\pi x^2}$, normalised by
$\int_{\mathbb R}h_n^2=1$ and self-dual, $\widehat{h_{4k}}=h_{4k}$, for
$\widehat f(\xi)=\int f(x)e^{2\pi ix\xi}dx$. **The collision to watch** is with Dunster, whose
separation constant $\lambda$ is not our $\lambda$: his equation is
$(1-z^2)y''-2zy'+(\lambda-\mu^2(1-z^2)^{-1}+\gamma^2(1-z^2))y=0$ and ours is
$((1-y^2)\Phi')'+(\chi-c^2y^2)\Phi=0$, so
$$\gamma=c,\qquad \lambda_{\text{Dunster}}=\chi-c^2,\qquad \mu_{\text{Dunster}}=m=0 .$$
Everything in §5 is stated in the converted symbols, and the one hypothesis that matters,
$\lambda_{\text{Dunster}}<0$, is our $\chi<c^2$. <!-- mg-ff96: the dictionary is confirmed by direct residual against Dunster's (1) as printed (dunster-check.md §2), but "the one hypothesis that matters" is (29), not lambda<0. -->

---

## 1. What the corollary needs is weaker than "bounded below" — *ours*

`cor:upper` chains
$$s(\mu)\;\le\;\frac{QW_\lambda(g,g)}{\|g\|^2}\;\le\;\frac{\Xi(\mu)\,(1-\chi_2(\lambda))}{\|g\|^2},$$
the second inequality being mg-731c's Thm 4.4 with $\Xi=O(\mu^{9/2}\log^3\mu)$ — $O(\mu^6\log^3\mu)$
once §A replaces its one observed step by a proved one, which changes nothing here. Taking
$\mu^{-1}\log$ and using $1-\chi_2=e^{-4\pi\mu+O(\log\mu)}$,
$$\limsup_{\mu\to\infty}\frac{\log s(\mu)}\mu\;\le\;-4\pi+\limsup_{\mu\to\infty}
\frac{-\log\|g\|^2}{\mu} .$$

> **Observation 1.1 (*ours*, trivial and worth stating).** The $-4\pi$ conclusion needs only
> $$\mu^{-1}\log\|g(\lambda)\|^2\;\longrightarrow\;0,$$
> i.e. $\|g\|^2\ge e^{-o(\mu)}$. A polynomially small lower bound $\|g\|^2\gg\mu^{-A}$ suffices;
> so does $e^{-\sqrt\mu}$. "Bounded below" is stronger than the corollary consumes.

This is not pedantry. It is what licenses throwing away all of the window except a fixed
compact piece (§3), and it is the reason (H0) was mis-sized: the statement *as printed* asks
for a uniform constant, and a uniform constant is exactly what forces the $\lambda$-dependence
of the weight to be confronted. Both are in fact available (§6), but only one is needed.

---

## 2. The exact identity, with no $\zeta$ in it — *ours*

**Lemma 2.1 (*proved*).** *For $t\ge1$ put $S(t):=\sum_{1\le n\le t}\Phi(n/t)$. Then*
$$\|g\|^2=\int_1^{\mu}\frac{S(t)^2}{t^2}\,dt,\qquad
\|r\|^2=\int_{\mu}^{\infty}\frac{S(t)^2}{t^2}\,dt,\qquad
\|\mathcal E\phi\|^2=\int_1^\infty\frac{S(t)^2}{t^2}\,dt. \tag{2.1}$$
*Every argument $n/t$ lies in $[0,1]$: the sums are on band.*

*Proof.* $\phi$ is supported in $[-\lambda,\lambda]$, so $\mathcal E\phi(u)=u^{1/2}
\sum_{n\le\lambda/u}\phi(nu)$ is a finite sum. Substitute $u=\lambda/t$, so that $t=1$ is the
top of the window $u=\lambda$ and $t=\mu$ is its bottom $u=\lambda^{-1}$, and
$\phi(nu)=\lambda^{-1/2}\Phi(n/t)$:
$$\mathcal E\phi(\lambda/t)=(\lambda/t)^{1/2}\lambda^{-1/2}\!\!\sum_{n\le t}\Phi(n/t)
=t^{-1/2}S(t).$$
$d^*u=dt/t$, so $|\mathcal E\phi|^2d^*u=S(t)^2t^{-2}dt$. $S(t)=0$ for $t<1$, which is
$\operatorname{supp}\mathcal E\phi\subseteq(0,\lambda]$. ∎

Three things follow immediately, and the first is the finding.

- **(H0) contains no number theory.** (2.1) is an integral of a finite sum of values of one
  classical special function on its own interval. The mean-value identity for
  $\|\mathcal E\phi\|^2$ is a *Plancherel rewriting* of the third integral in (2.1); it is
  exact, it is a fine way to compute the number (§7 uses it as a cross-check, agreeing to 22
  digits), and it is not a route to a lower bound, because a lower bound for
  $\int|\zeta|^2w_\lambda$ with $w_\lambda$ moving is harder than the thing it is bounding.
- **$\|r\|^2$ is never subtracted.** The decomposition $\|g\|^2=\|\mathcal E\phi\|^2-\|r\|^2$
  is what makes (H0) look like a statement about the whole line; (2.1) shows $\|g\|^2$ is its
  own integral over its own range and needs nothing from the spill. (Measured, $\|r\|^2$ is
  $7.5\times10^{-9}$ at $\mu=3$ and $10^{-88}$ at $\mu=20$ — §7 — so the subtraction is
  harmless; the point is that it is also unnecessary.)
- **$S$ jumps at every integer $t=N$, by $\Phi(1)$.** That is mg-731c's sawtooth
  (`q3-log-weight-and-edge.md` Cor. 1.2) seen from inside the window rather than outside it,
  and it is why the quadrature in `verify_h0.py` splits at the integers. It costs nothing here:
  $|\Phi(1)|$ is exponentially small in $c$ — bounded above and below by multiples of
  $\sqrt{c(1-\Lambda_4)}$, the lower bound proved in mg-731c from Q1 and (4.1), the upper one
  observed (`h1-mean-value.md` §7, Q5).

---

## 3. The localisation, and why it is enough — *ours*

**Lemma 3.1 (*proved*).** *Let $0<A<B<\infty$ and $\lambda\ge B$. Then*
$$\|g\|^2\;\ge\;\int_A^B|\mathcal E\phi(u)|^2\,d^*u . \tag{3.1}$$

*Proof.* $[A,B]\subseteq[\lambda^{-1},\lambda]$ and the integrand is non-negative. ∎

That is the whole of the reduction, and it is why nothing about $\zeta$ can be needed: the
right-hand side of (3.1) is a fixed-window functional of $\phi$, and $\phi$ lives at scale
$O(1)$ in $x$ (Lemma 3.3). What has to be shown is that this functional does not collapse.

**Lemma 3.2 ($\mathcal E$ is continuous on a fixed window, *proved*).** *Let
$0<A<B<\infty$. For $f\in L^2(\mathbb R)$ even with $\|xf\|_2\le M$,*
$$\Big(\int_A^B|\mathcal Ef|^2d^*u\Big)^{1/2}\;\le\;
C(A,B)\,\big(M\,\|f\|_2\big)^{1/2}+C(A,B)\|f\|_2 . \tag{3.2}$$

*Proof.* $|\mathcal Ef(u)|\le B^{1/2}\sum_{n\ge1}|f(nu)|$ for $u\le B$, and by Minkowski in
$L^2([A,B],du)$, $\|f(n\cdot)\|_{L^2([A,B])}=n^{-1/2}\|f\|_{L^2([nA,nB])}$. Bound
$\|f\|_{L^2([nA,nB])}$ two ways — by $\|f\|_2$, and by $(nA)^{-1}\|xf\|_2$ — and split the sum
at $N$:
$$\sum_{n\le N}n^{-1/2}\|f\|_2+\sum_{n>N}n^{-3/2}A^{-1}M\;\le\;2\sqrt N\|f\|_2+2A^{-1}MN^{-1/2}.$$
Choosing $N\asymp M/(A\|f\|_2)$ gives (3.2), and $d^*u\le A^{-1}du$ on $[A,B]$. ∎

**Lemma 3.3 (tightness, *proved*, and elementary).** *For any solution of the prolate equation
with $\int_{-1}^1\Phi_n^2=1$,*
$$c^2\int_{-1}^1y^2\Phi_n^2\,dy\;=\;\chi_n-\int_{-1}^1(1-y^2)\Phi_n'^2\,dy\;\le\;\chi_n,
\qquad\text{hence}\qquad
\int_{\mathbb R}x^2|\phi_n(x)|^2dx\;\le\;\frac{\chi_n}{4\pi^2\lambda^2}. \tag{3.3}$$
*For the three-mode combination, $\|x\phi\|_2^2\le3\max_{n\in\{0,4,8\}}\chi_n/(4\pi^2\lambda^2)$.*

*Proof.* Multiply the equation by $\Phi_n$ and integrate; the boundary term
$[(1-y^2)\Phi_n'\Phi_n]_{-1}^1$ vanishes because $\Phi_n$ is analytic at $\pm1$. Rescale with
$c=2\pi\lambda^2$. The combination bound is Cauchy–Schwarz on $\sum_m|b_m|\le\sqrt3$. ∎

$\chi_n=(2n+1)c+O(1)$ (§5, Dunster eq. (107)), so the right-hand side of (3.3) is
$(2n+1)/(2\pi)+O(\lambda^{-2})$: **bounded, uniformly in $\lambda$.** Measured in CHECK 6, the
inequality in (3.3) holds with a factor $0.51$–$0.54$ to spare, and
$\lambda^2\int y^2\Phi^2$ sits within $2\%$ of its Hermite limit $0.5426$ already at $\mu=5$.
This is what stops mass escaping to $|x|=\infty$, and it is the only place the *whole* of
$\mathbb R$ is used.

---

## 4. The limit vector, and the constant — *ours, from the corpus's own object*

Let
$$\phi_\infty:=\sqrt{\tfrac8{11}}\Big(h_4-\sqrt{\tfrac38}\,h_0\Big).$$

**Proposition 4.1 (*proved*).** *$\|\phi_\infty\|_2=1$; $\phi_\infty(0)=0$;
$\widehat{\phi_\infty}=\phi_\infty$, hence $\widehat{\phi_\infty}(0)=0$; and consequently*
$$\mathcal E\phi_\infty(u)=\mathcal E\phi_\infty(1/u)\qquad(u>0). \tag{4.1}$$

*Proof.* $h_0(0)=2^{1/4}$ and $h_4(0)=2^{1/4}H_4(0)/\sqrt{2^44!}=2^{1/4}\cdot12/\sqrt{384}
=2^{1/4}\sqrt{3/8}$, so $\phi_\infty(0)=0$; the norm is
$\tfrac8{11}(1+\tfrac38)=1$; $h_0$ and $h_4$ are Fourier self-dual because their Hermite
indices are divisible by $4$. (4.1) is Poisson: for $f$ even with $f(0)=\widehat f(0)=0$,
$\mathcal E\widehat f(x)=\mathcal Ef(1/x)$ (`prolate-rate.md` §1 step 3), and here
$\widehat f=f$. ∎

$\phi_\infty$ is **the corpus's own vector**: `start.tex:39`'s $h_4-\sqrt{3/8}h_0$, normalised,
with the index-4 weight $8/11$ of `prolate-rate.md` §2.2 and mg-aedf. The index-8 mode of
`prolate-rate.md` §2.1 disappears in the limit, because its relative weight is
$(1-\chi_2)/(1-\chi_4)=O(c^{-4})$ by Fuchs. *That is not needed below*: what §6 uses is only
that a limit exists and is a non-zero admissible Hermite combination — see Remark 6.3.

**Proposition 4.2 (*proved*).** *$\mathcal E\phi_\infty$ is real-analytic and $\not\equiv0$ on
$(0,\infty)$; hence $\int_A^B|\mathcal E\phi_\infty|^2d^*u>0$ for every $0<A<B$.*

*Proof.* $\sum_{n\ge1}\phi_\infty(nu)$ converges locally uniformly on a complex neighbourhood
of $(0,\infty)$, $\phi_\infty$ being a polynomial times $e^{-\pi x^2}$; so the sum is analytic
and its zeros are isolated unless it vanishes identically. It does not: $\mathcal E$ is
injective on $\mathcal S_0^{ev}$, since on the Mellin side it is multiplication by
$\zeta(\tfrac12-is)$, which is not the zero function. ∎

*(This is the only appearance of $\zeta$ in the proof, and it is used only for
$\zeta\not\equiv0$. One could equally argue from $\mathcal E\phi_\infty(u)=u^{1/2}\phi_\infty(u)
\ne0$ for large $u$ plus analyticity.)*

**The constant.** $\|\mathcal E\phi_\infty\|^2=0.219247199549\ldots$, computed twice
independently in §7 — once by quadrature in $u$, once as
$\frac1{2\pi}\int|\zeta(\tfrac12-is)|^2|M(s)|^2ds$ with $M$ the closed-form Mellin transform of
$\phi_\infty$ — agreeing to $1.3\times10^{-22}$. Almost all of it is local: $\int_{1/2}^2$
recovers $0.219246959898$, i.e. $99.99989\%$.

---

## 5. The convergence, and where it is published — *primary source, hypotheses checked*

Read as primary source from `arxiv.org/e-print/1601.00699`, file `PSWF_JCA.tex`:

> **T. M. Dunster, "Asymptotics of prolate spheroidal wave functions", J. Classical Analysis
> 11 (2017), arXiv:1601.00699.** Abstract at `:89`–`:102`; the PSWE and the standing hypothesis
> $\lambda\to-\infty$ at `:118`–`:146`; §5 "Fixed $m$ and $n$: the angular case" at `:1284`;
> eq. (107) at `:1300`; the Liouville variable (108) at `:1310`; eq. (124) at `:1432`–`:1443`.

**The regime.** Dunster's standing assumption for this paper is $\lambda<0$, i.e.
$\boxed{\chi_n<c^2}$ — *our* regime, the one Lemma 5.1 of `h1-mean-value.md` and Q1 live in.
He is explicit that the complementary case is elsewhere (`:184`): "in comparison to the current
paper in which $\lambda<0$, in [9] the case $\lambda>0$ was assumed, which does not have many
of the applications described above." His summary §6 states the same as
$\sigma=\sqrt{1+\gamma^{-2}\lambda}=\sqrt{\chi_n}/c\in[0,\sigma_0]$, $\sigma_0<1$; the corpus's
measured $\chi_n/c^2$ runs $0.020$ to $0.64$ (`h1-mean-value.md` §5), so $\sigma\le0.8$ with <!-- mg-ff96: WRONG at index 8. That range was measured at n<=4. Measured at n=8: sigma = 0.883 at mu=3 (a row of §7 CHECK 6 below) and sigma = 1.0199 at mu=2, where the hypothesis FAILS -- chi_8 > c^2 below c* = 13.3007 (mu* = 2.1169). Thm 6.1 is a lambda->infinity limit at fixed n and is unaffected; the sentence is not. dunster-check.md §3.1. -->
room, and in the fixed-$n$ limit $\sigma\to0$.

**This is the third time the regime has decided the outcome on this chain, and the first time
it has decided it in our favour.** `h1-mean-value.md` §6 rejected Osipov–Rokhlin because their
theorems assume $\chi_n>c^2$; Q1 turned on $\chi<c^2$ being "no turning point outside the
band" (mg-6851); and the paper that covers $\chi<c^2$ is by the author of the paper that covers
$\chi>c^2$, and says so on its second page. **The estimate was not missing from the literature.
It was one hypothesis-sign away, in a paper nobody in this corpus had opened.**

**The statement, converted.** At $m=0$ and fixed even $n$, with $\gamma=c$:

- **(107)** $a=\lambda\gamma^{-1}+\gamma=\chi_n/c=2n+1+O(c^{-1})$, for fixed $n$ as <!-- mg-ff96: verified numerically at n=0,2,4,6,8 and c=4pi..24pi, including its next coefficient: chi_n = (2n+1)c - ((2n+1)^2+5)/8 + O(1/c). Note (107)'s O(1/gamma) is itself imported, from (27) at `:455` citing Arscott [1, p.186] -- a second-level dependency §10 does not record. dunster-check.md §4. -->
  $c\to\infty$. *(This is the eigenvalue input Lemma 3.3 needs, and it is where
  $\chi_n\le(2n+1)c+O(1)$ comes from.)*
- **(124)** uniformly for $0\le x\le1-\delta_0$,
  $$\Phi_n(x)=\frac{\Phi_n(0)}{U(-\tfrac12a,0)}\Big(\frac\rho x\Big)^{1/2}(1-x^2)^{-1/4}
  \Big[U\big(-\tfrac12a,\hat\rho\sqrt{2c}\big)+O(c^{-1}\log c)\operatorname{env}
  U\big(-\tfrac12a,\hat\rho\sqrt{2c}\big)\Big],$$
  with $\tfrac12\rho^2=1-\sqrt{1-x^2}$ and $\hat\rho=\rho+c^{-1}\Phi(\rho)$,
  $\Phi(\rho)=\frac{a}{4\rho}\log(1-\tfrac14\rho^2)$. "Explicit error bounds are furnished in
  [10]" — Dunster's own general theory for a pair of almost-coalescent turning points, **cited
  by him and not opened by me, and marked accordingly**; the $O(c^{-1}\log c)$ at (120) is what
  he deduces from it.

**Why that is the Hermite statement.** $U(-n-\tfrac12,z)=e^{-z^2/4}\mathit{He}_n(z)$ (DLMF
12.7.2; verified to 41 digits in CHECK 7). At $x=X/\lambda$ with $X$ in a fixed compact set:
$\rho=x(1+O(x^2))$ and $\hat\rho=\rho(1+O(c^{-1}))$, so
$\hat\rho\sqrt{2c}=X\sqrt{2c}/\lambda\,(1+O(\lambda^{-2}))=2\sqrt\pi X(1+O(\lambda^{-2}))$,
the prefactor $(\rho/x)^{1/2}(1-x^2)^{-1/4}=1+O(\lambda^{-2})$, and
$e^{-z^2/4}\mathit{He}_n(z)|_{z=2\sqrt\pi X}=e^{-\pi X^2}2^{-n/2}H_n(\sqrt{2\pi}X)$ — which is
$h_n(X)$ up to normalisation. The order perturbation $a=2n+1+O(c^{-1})$ moves $U$ by
$O(c^{-1})$ locally uniformly, by analyticity of $U(\cdot,z)$ in its first argument. So:

> **(E)** For each fixed even $n$ and each fixed $R>0$, <!-- mg-ff96: (E) is measured to hold with O(1/c); the step (124)=>(E) is measured separately and costs O(1/c) too. But (124)'s own error and the corpus's conversion error are each ~3x the total and largely cancel, so CHECK 7 below is NOT evidence that (124) is accurate. dunster-check.md §6. -->
> $$\frac{\Phi_n(X/\lambda)}{\Phi_n(0)}\;=\;\frac{h_n(X)}{h_n(0)}+O\big(c^{-1}\log c\big)
> \qquad\text{uniformly on }|X|\le R .$$

**(E) is what §6 imports, and nothing else.** Note what it is and is not: (124) is a statement
about the *shape* of $\Phi_n$, normalised at $x=0$, because Dunster's prefactor is
$\mathrm{Ps}_n^m(0,\gamma^2)$ — so (E) carries no normalisation, and fixing the normalisation
against $\int_{-1}^1\Phi_n^2=1$ is step (i) of Theorem 6.1's job, not Dunster's. The $O(\cdot)$
is additive against the local envelope of $U$, which is bounded on a compact $X$-range; it is
*not* a relative bound near the zeros of $h_n$, and nothing below needs it to be. Measured in
CHECK 7 — the sup of $|\lambda^{-1/2}\Phi_n(X/\lambda)-h_n(X)|$ over $|X|\le4$, i.e. of the
normalised statement that step (i) produces — the errors are $O(1/c)$ at all three indices.

---

## 6. (H0), proved — *ours, on Dunster's (E)*

**Theorem 6.1 (*proved*, modulo (E) as imported from Dunster (124)+(107)).**
$$\lim_{\lambda\to\infty}\|g(\lambda)\|^2\;=\;\|\mathcal E\phi_\infty\|^2\;=\;0.2192471995\ldots
\;>\;0 .$$
*In particular $\|g\|^2$ is bounded below, uniformly in $\lambda$, for $\lambda$ large; with
the finite-$\lambda$ values of §7, uniformly for all $\lambda>1$ in the corpus's range.*

*Proof.* In four steps.

**(i) $\phi_\lambda\to\phi_\infty$ in $L^2(\mathbb R)$.** Fix $n$ and write
$\phi^{(\lambda)}_n(X)=\lambda^{-1/2}\Phi_n(X/\lambda)$ on $|X|\le\lambda$, zero outside, so
$\|\phi^{(\lambda)}_n\|_2=1$. Put $A_\lambda:=\lambda^{-1/2}\Phi_n(0)/h_n(0)$, positive since
$\Phi_n(0)>0$ by the sign convention and $h_n(0)>0$ at $n=0,4,8$. By (E), on $|X|\le R$,
$$\phi_n^{(\lambda)}(X)=A_\lambda\big[h_n(X)+O(c^{-1}\log c)\big]\quad\text{uniformly},$$
so $\int_{|X|\le R}|\phi_n^{(\lambda)}|^2=A_\lambda^2\big(\int_{|X|\le R}h_n^2+O(Rc^{-1}\log c)\big)$;
in particular $A_\lambda$ is bounded, since the left side is $\le1$. By Lemma 3.3,
$\int_{|X|>R}|\phi^{(\lambda)}_n|^2\le M/R^2$ with $M$ independent of $\lambda$. Hence
$$1-\frac M{R^2}\;\le\;A_\lambda^2\Big(\int_{|X|\le R}h_n^2+o(1)\Big)\;\le\;1 ,$$
so $A_\lambda\to1$ (let $\lambda\to\infty$, then $R\to\infty$), and then
$\|\phi_n^{(\lambda)}-h_n\|_2^2\le o(1)+2M/R^2+2\int_{|X|>R}h_n^2\to0$. The mode
coefficients $b_m(\lambda)$ converge because they are determined by $\Phi_m(0)$ and the ratio
$u_8/u_4=-(\chi_0-\chi_4)/(\chi_0-\chi_8)$, and each converges by the same argument (the
latter to $0$, at rate $O(c^{-4})$ by Fuchs); so $\phi_\lambda\to\phi_\infty$ in
$L^2(\mathbb R)$, with the sign fixed by $b_4>0$.

**(ii) The window functional converges.** Fix $[A,B]=[\tfrac12,2]$ and $\lambda\ge2$. By
Lemma 3.2 applied to $f=\phi_\lambda-\phi_\infty$, whose second moment is bounded by
Lemma 3.3 and Prop. 4.1,
$$\Big|\Big(\int_A^B|\mathcal E\phi_\lambda|^2d^*u\Big)^{1/2}
-\Big(\int_A^B|\mathcal E\phi_\infty|^2d^*u\Big)^{1/2}\Big|
\;\ll\;\big(M\|\phi_\lambda-\phi_\infty\|_2\big)^{1/2}\;\longrightarrow\;0 .$$

**(iii) Lower bound.** By Lemma 3.1 and Prop. 4.2,
$$\liminf_{\lambda\to\infty}\|g(\lambda)\|^2\;\ge\;\int_{1/2}^2|\mathcal E\phi_\infty|^2d^*u
\;=\;0.219246959898\ldots\;>\;0 .$$
This already gives (H0), and it is the only step the $-4\pi$ bound needs.

**(iv) The limit itself.** For the matching upper bound the two tails must be controlled
uniformly in $\lambda$, and they are *not* controlled the same way. Both follow from

> **(T)** *if $f$ is even with $\int_{|x|>Y}|f|^2\le M^2/Y^2$ for every $Y>0$, then
> $\int_B^\infty|\mathcal Ef|^2d^*u\le CM^2/B^2$*,

which is the Minkowski computation of Lemma 3.2 with only the second of the two bounds used:
$\big(\int_B^\infty|\sum_nf(n\cdot)|^2du\big)^{1/2}\le\sum_nn^{-1/2}\|f\|_{L^2([nB,\infty))}
\le\frac M B\sum_nn^{-3/2}$, and $d^*u\le du/B$ is not even needed since the $u^{1/2}$ cancels.

- *Large $u$.* $\phi$ satisfies (T)'s hypothesis with $M^2=3\max_n\chi_n/(4\pi^2\lambda^2)$, by
  Chebyshev and Lemma 3.3. So $\int_B^\lambda|\mathcal E\phi|^2d^*u\le CM^2/B^2$.
- *Small $u$.* Here the symmetry is used: $\phi(0)=\widehat\phi(0)=0$ exactly, so
  $\mathcal E\phi(u)=\mathcal E\widehat\phi(1/u)$ and
  $\int_0^A|\mathcal E\phi|^2d^*u=\int_{1/A}^\infty|\mathcal E\widehat\phi|^2d^*v$. And
  $\widehat\phi$ satisfies (T)'s hypothesis with the *same* $M$ up to a constant:
  $\widehat\phi=\sqrt{\Lambda}\,\lambda^{-1/2}\Phi_{\text{ent}}(\cdot/\lambda)$ exactly
  (`h1-mean-value.md` §4's finite-Fourier relation, valid for all $x$), so for $Y\le\lambda$ the
  in-band bound of Lemma 3.3 applies verbatim, and for $Y>\lambda$ **Q1** gives
  $|\Phi_{\text{ent}}(y)|\le K_1|\Phi(1)|/y$ and hence a bound smaller by $\Phi(1)^2$, which is
  exponentially small. Note $\int x^2|\widehat\phi|^2=\infty$ — $\widehat\phi$ decays only like
  $x^{-1}$ off band — so Lemma 3.2 could **not** have been applied to $\widehat\phi$; (T) can,
  because it asks only for the tail and not for the moment.

So the contribution of $u\notin[A,B]$ to $\|g\|^2$ is $O(M^2A^2)+O(M^2/B^2)$, uniformly in
$\lambda$; letting $A\to0$ and $B\to\infty$ after $\lambda\to\infty$ gives
$\|g\|^2\to\|\mathcal E\phi_\infty\|^2$. ($\|r\|^2\to0$ is then immediate, and also follows from
(2.1) with Q1+Q2.) ∎

**Remark 6.2 (what is imported and what is not).** Only (E) is imported. Lemmas 2.1, 3.1, 3.2,
3.3 and Props. 4.1, 4.2 are proved here from the prolate equation, Poisson summation and
Cauchy–Schwarz. Nothing anywhere in the argument uses a property of $\zeta$ beyond
$\zeta\not\equiv0$, and even that is avoidable (Prop. 4.2).

**Remark 6.3 (the theorem is robust to the identity of the limit).** Step (iii) needs only that
$\phi_\lambda$ converges in $L^2$ to *some* non-zero $\phi_*$ with $\mathcal E\phi_*$
real-analytic — any Hermite combination will do, and Prop. 4.2's argument applies verbatim.
If the mode weights were different from $8/11$, or if the index-8 admixture did not vanish, the
constant would change and (H0) would not. **The only way (H0) can fail is if the prolate vector
degenerates entirely**, which Lemma 3.3 already forbids in one of the two possible ways (escape
to $|x|=\infty$); (E) forbids the other (concentration at $x=0$).

**Remark 6.4 (what is *not* re-derived here).** The chain from $\|g\|^2$ to $s(\mu)$ is the
corpus's, unchanged: `prolate-rate.md` §6(a)'s identity, mg-731c's Thm 4.4, and the reading
(`prolate-rate.md` §0) that $\epsilon(\lambda)=\min(s^+,s^-)$ coincides with $s(\mu)$. In
particular $g$ is not *exactly* even in the multiplicative sense — $\mathcal E\phi(1/u)$ is
$\mathcal E\widehat\phi(u)$ and $\widehat\phi=\sqrt{\Lambda}\,\Phi_{\text{ent}}$ differs from
$\phi$ by $O(\sqrt{1-\Lambda_4})$ — so what $QW_\lambda(g,g)/\|g\|^2$ bounds directly is
$\epsilon(\lambda)=\min(s^+,s^-)$. That reading pre-dates this note and is not disturbed by it;
it is flagged because this note is where the chain is finally closed.

---

## 7. The numbers — *measurement*

`verify_h0.py`, arbitrary precision. Working precision 40 digits for the quadratures; the
three-mode vector is **built** at more than $2c/\log10$ digits, because its index-8 weight is a
ratio of concentration defects and those are $10^{-47}$ at $\mu=12$ and $10^{-88}$ at $\mu=20$.
(At working precision the build returns $\chi_0-\chi_8=0$; at 25 digits and $\mu=8$ it raises
`ZeroDivisionError`, which is the good case, and is how this was found.)

**CHECK 2/5 — the limit constant, twice.**

| computation | value |
|---|---|
| $\int_0^\infty|\mathcal E\phi_\infty|^2d^*u$, quadrature in $u$ | $0.219247199549$ |
| $\frac1{2\pi}\int|\zeta(\tfrac12-is)|^2|M(s)|^2ds$, $M$ in closed form | $0.219247199549$ |
| relative difference | $1.3\times10^{-22}$ |
| $\int_{1/2}^2|\mathcal E\phi_\infty|^2d^*u$ | $0.219246959898$ |

The second line is the mean value of $|\zeta(\tfrac12+it)|^2$ that §9 names — computed here
only to check the first, which does not contain $\zeta$ at all. The weight $|M(s)|^2$ falls
from $0.079$ at $s=0$ to $1.8\times10^{-22}$ at $s=40$: it is the weight, not $\zeta$, that
carries the integral.

**CHECK 3 — $\|g\|^2$ at finite $\mu$, from the actual prolate vector.**

| $\mu$ | $\|g\|^2$ | $\|g\|^2/$limit | $\int_{1/2}^2$ part | $\|r\|^2$ |
|---|---|---|---|---|
| $3$ | $0.226900403$ | $1.0349067$ | — ($\lambda<2$) | $7.5\times10^{-9}$ |
| $5$ | $0.2226854396$ | $1.015682$ | $0.22268544$ | $1.2\times10^{-18}$ |
| $8$ | $0.2210993344$ | $1.0084477$ | $0.22109932$ | $4.0\times10^{-34}$ |
| $12$ | $0.2203874624$ | $1.0052008$ | $0.22038742$ | $4.0\times10^{-55}$ |
| $20$ | $0.2198899179$ | $1.0029315$ | $0.21988982$ | $1.8\times10^{-93}$ |

Monotone down to the limit, and the fixed window $[\tfrac12,2]$ recovers $\|g\|^2$ to eight
digits at every $\mu$ — the localisation of §3 throws away nothing that matters. $\|r\|^2$ is
what the subtraction route would have to control; it is never used above.

**CHECK 4 — the convergence (E), through the combination.**
$d(\lambda)=1-\langle\phi_\lambda,\phi_\infty\rangle$, so
$\|\phi_\lambda-\phi_\infty\|^2=2d$.

| $\mu$ | $c$ | $d$ | $d\cdot c$ | $d\cdot c^2$ |
|---|---|---|---|---|
| $3$ | $18.8496$ | $3.083\times10^{-3}$ | $0.05811$ | $1.0953$ |
| $5$ | $31.4159$ | $9.134\times10^{-4}$ | $0.02870$ | $0.9015$ |
| $8$ | $50.2655$ | $3.250\times10^{-4}$ | $0.01634$ | $0.8212$ |
| $12$ | $75.3982$ | $1.377\times10^{-4}$ | $0.01038$ | $0.7825$ |
| $20$ | $125.664$ | $4.776\times10^{-5}$ | $0.006001$ | $0.7542$ |

$d\cdot c\to0$ and $d\cdot c^2$ is flat to within a factor $1.45$ and still settling, so
$\|\phi_\lambda-\phi_\infty\|_2=O(c^{-1})$ — one power better than Dunster's
$O(c^{-1}\log c)$ would guarantee, and far more than §6 needs, which is only $d\to0$.

**CHECK 7 — (E) per mode, against the Hermite functions.**
$\sup_{|X|\le4}\big|\lambda^{-1/2}\Phi_n(X/\lambda)-h_n(X)\big|$:

| $\mu$ | $c$ | $n=0$ | $n=4$ | $n=8$ |
|---|---|---|---|---|
| $3$ | $18.8496$ | $0.008159$ | $0.0790$ | $0.2796$ |
| $5$ | $31.4159$ | $0.004689$ | $0.04098$ | $0.1192$ |
| $8$ | $50.2655$ | $0.002865$ | $0.02397$ | $0.06555$ |
| $12$ | $75.3982$ | $0.001887$ | $0.01545$ | $0.04115$ |
| $20$ | $125.664$ | $0.001121$ | $0.009035$ | $0.02364$ |

At $n=4$ the product $c\cdot(\text{error})$ runs $1.489,\ 1.287,\ 1.205,\ 1.165,\ 1.135$: $O(1/c)$,
with no $\log c$ visible. The error grows with the index, as (E)'s $O(\cdot)$ being uniform only
for *fixed* $n$ predicts.

**CHECK 6 — the tightness lemma.** $c^2\int y^2\Phi_n^2$ against $\chi_n$, and $\chi_n$
against $(2n+1)c$:

| $\mu$ | $n$ | $c^2\int y^2\Phi_n^2$ | $\chi_n$ | ratio | $\chi_n/((2n+1)c)$ |
|---|---|---|---|---|---|
| $3$ | $0$ | $9.4305$ | $18.089$ | $0.5213$ | $0.9596$ |
| $3$ | $8$ | $166.03$ | $277.14$ | $0.5991$ | $0.8649$ |
| $8$ | $0$ | $25.135$ | $49.512$ | $0.5077$ | $0.9850$ |
| $8$ | $8$ | $428.28$ | $815.97$ | $0.5249$ | $0.9549$ |
| $20$ | $0$ | $62.833$ | $124.91$ | $0.5030$ | $0.9940$ |
| $20$ | $8$ | $1068.5$ | $2098.9$ | $0.5091$ | $0.9825$ |

The inequality of Lemma 3.3 holds with a factor two to spare — the missing half is
$\int(1-y^2)\Phi'^2$ — and $\chi_n/((2n+1)c)\to1$, which is Dunster's (107). The combination's
second moment $\lambda^2\int y^2\Phi^2$ runs $0.5632,\ 0.5532,\ 0.5487,\ 0.5465,\ 0.5449$
against its Hermite limit $\int x^2\phi_\infty^2=0.5425737$: **bounded, and converging**, which
is the whole use made of it.

**CHECK 8 — §A's bound against the truth.** $\Phi_n(1)^2/(c(1-\Lambda_n))$ (the observed
identity of `h1-mean-value.md` §7, reproduced) against Prop. A.1's proved bound in the same
units:

| $\mu$ | truth, $n=0$ | truth, $n=4$ | proved bound | truth/bound |
|---|---|---|---|---|
| $3$ | $0.98607$ | $0.86589$ | $2.352\times10^5$ | $4.19\times10^{-6}$ |
| $8$ | $0.99494$ | $0.95352$ | $7.667\times10^5$ | $1.30\times10^{-6}$ |
| $20$ | $0.99800$ | $0.98184$ | $2.753\times10^6$ | $3.63\times10^{-7}$ |

$\kappa=0.086503328$. The bound is loose by five to six orders of magnitude and by
$c^{3/2}K_1$ in shape — which is what "only its order matters" means, and the order is what
the rate consumes.

**Numerical hygiene.** CHECK 0 checks that the vector is admissible ($\Phi(0)$ and
$\int_{-1}^1\Phi$ at the $10^{-41}$ level, i.e. round-off) and that $S(t)$ reproduces
`verify_q3.Comb.R` where the two parametrisations of $\mathcal E\phi$ overlap. CHECK 1 checks
the limit vector by a property that is nowhere imposed in the code — the functional equation
$\mathcal E\phi_\infty(u)=\mathcal E\phi_\infty(1/u)$, which holds only if $\phi_\infty$ is
self-dual *and* both admissibility conditions hold; it is verified to $10^{-40}$. CHECK 7
verifies DLMF 12.7.2 to 41 digits before using it. Stability is reported at 30 vs 40 working
digits from vectors built 40 digits apart.

---

## 8. The house rule, applied to this note

> **Is any statement in this note false for $-W_\lambda$?**

| item | under $-W_\lambda$ | verdict |
|---|---|---|
| 1. Lemma 2.1, the window identity | $W$ does not appear in it | **sign-blind** |
| 2. Lemma 3.1–3.3, the localisation and tightness | statements about $\phi$ and the prolate ODE | **sign-blind** |
| 3. Prop. 4.1–4.2, the limit vector | statements about Hermite functions and $\mathcal E$ | **sign-blind** |
| 4. (E), Dunster's approximation | a statement about a special function | **sign-blind** |
| 5. Thm 6.1, $\|g\|^2\to0.2192\ldots$ | a norm; unchanged | **sign-blind** |
| 6. §9's $-4\pi$, now unconditional | $QW_\lambda$ negates; an upper bound on $|s|$ stays one | **sign-blind as a magnitude claim** |

**Every item is sign-blind, and that is correct rather than a defect.** (H0) is a lower bound
on the norm of the test vector; it cannot see $W$ at all, let alone its sign.

**And the sign constraint the ticket names is respected.** A lower bound on $\|g\|^2$ enters
`cor:upper` in the **denominator of an upper bound**: it makes the upper bound on $s(\mu)$
*smaller*. Nothing in this note produces a lower bound on $s(\mu)$, and nothing in it could —
$QW_\lambda(g,g)$ is never bounded below here, only $\|g\|^2$. `prolate-rate.md` §7 and
`h1-mean-value.md` §8 are undisturbed: the matching lower bound is still RH.

---

## 9. What this closes, and the sentence to use

**Closed.** (H0) = Q4 = the second half of gap **G6**. With Q1 (mg-6851), Q2 (mg-9d43),
Q3 (mg-731c), this, and §A,
$$\boxed{\;\limsup_{\mu\to\infty}\frac{\log s(\mu)}\mu\;\le\;-4\pi\;}$$
**unconditionally**, and quantitatively $s(\mu)\le(4.5610\ldots+o(1))\,\Xi(\mu)(1-\chi_2)$ with
$1-\chi_2\sim\frac{2^{14}\sqrt2\pi^5}3\mu^{9/2}e^{-4\pi\mu}$ and
$$\Xi(\mu)=O(\mu^{9/2}\log^3\mu)\ \text{ on }\ \Phi(1)^2=O(\mu(1-\chi_2))\ \textit{(observed)},
\qquad O(\mu^{6}\log^3\mu)\ \text{ on §A }\ \textit{(proved)},$$
i.e. $s(\mu)=O(\mu^{21/2}\log^3\mu\,e^{-4\pi\mu})$ with everything proved.
($4.5610617\ldots=1/0.2192472$.)

**But read the word "unconditionally" with §A attached, and this is a status I did not inherit
cleanly.** mg-731c's Thm 4.4 bounds the zero sum by $\Phi(1)^2$, and its §4 cost table converts
$\Phi(1)^2\to(1-\chi_2)$ citing `h1-mean-value.md` §7 — which is **observed, not proved**, and
whose reverse half mg-731c's own §14 records as "sketched but not written out". So on arriving
at this ticket the $-4\pi$ rate rested on (H0) *and* on that observed conversion. §A writes the
conversion out, at a cost of $\mu^{3/2}$ over the observed truth. **Anyone who prints
"unconditional" without §A is quoting a status that was not there.**

**The sentence to use, and the one not to.** **Do not write "H1 is proved."**
`h1-mean-value.md` §1 proves that no bound of the form $\Theta(\lambda)\|r\|^2$ can exist, so
(H1) *as printed at* `:1242` is not what was closed and never could be. What is proved is <!-- mg-6467: now `:1421`; the paper says so itself in §7.1, `:1504`. -->
**(4.3)** — `h1-mean-value.md` §4, established by mg-731c — together with (H0). The correct
sentence is:

> *The upper bound $\limsup\mu^{-1}\log s(\mu)\le-4\pi$ is unconditional. Hypothesis (H1) as
> stated is bypassed rather than proved — it is false in that form — and is replaced by
> estimate (4.3); hypothesis (H0) is proved.*

**What this does not touch.** The lower bound, which is RH (Thm `thm:boundary`, G10). The
sign. The odd sector. Remark 6.4's reading of $\epsilon(\lambda)$ versus $s^\pm$.

---

## 10. Open — what is left, and it is small

| # | item | status |
|---|---|---|
| **H0-1** | Write out (E) from Dunster (124) with the constants tracked, rather than as $O(c^{-1}\log c)$. Needs his [10] (the coalescing-turning-point theory), which was **not opened here** <!-- mg-ff96: TWO sources are unopened, not one: [10] for (124)'s error bounds, and Arscott [1, p.186] for (107)'s via (27). dunster-check.md §9 D-1, D-2. --> | **imported, source read for (124) but not for its error bounds** |
| **H0-2** | The effective range. Thm 6.1 is a limit statement; the finite-$\mu$ table in §7 covers $\mu\le20$ and $\|g\|^2$ is monotone there. A $\lambda_0$ beyond which $\|g\|^2\ge\tfrac15$ provably is not written out | **measured, not proved, for $\mu\le20$** |
| **H0-2b** | §A is loose by $\mu^{3/2}$. Replacing it by the observed truth $\Phi(1)^2\asymp c(1-\Lambda_4)$ — i.e. proving Q5's constant — would take $\Xi$ back to $O(\mu^{9/2}\log^3\mu)$ | **proved but loose; sharpening is Q5** |
| **H0-3** | Q5 of `h1-mean-value.md` — the endpoint identity $\Phi_n(1)^2=c(1-\Lambda_n)(1-\frac{2n+1}{4c}+\ldots)$ — is still **observed only** in its constant. Dunster's §§3–4 (Bessel-function approximations, radial case, valid at the band edge) is the obvious place to look next, and was **not** pursued here | **open, and now with a candidate source** |
| **H0-4** | The paper edits. Ten are batched in vision amendments 11 §5, 12 §5, 13 §6, 14 §5; this note adds: `H0` at `:1234` should say *"the non-degeneracy of the prolate vector in the Hermite limit"*, not *"a mean-value statement about $|\zeta(\tfrac12+it)|^2$"*; and G6 is closed | **DONE by mg-6467** — all eleven folded in; see the paper's §7 and its restructured gap list |

---

## A. Appendix, outside Q4: the upstream link mg-731c left sketched — *ours*

*Supplied because §9's sentence needs it, not because Q4 does. Nothing in §§1–8 uses it.*

`q3-log-weight-and-edge.md` Thm 4.4 bounds the zero sum by a polynomial times **$\Phi(1)^2$**,
and its §4 cost table then converts $\Phi(1)^2\to(1-\chi_2)$ at cost $O(\mu)$, citing
`h1-mean-value.md` §7 — which is **observed**. mg-731c's own append (§14 of `h1-mean-value.md`)
says so: the lower half of that identity "is now proved (Q1 plus (4.1))", and "the reverse
inequality follows from `dilate-sum.md` Prop. 4.1(ii) and is sketched but not written out". The
reverse inequality is the half the $-4\pi$ rate needs. Here it is, written out; only its order
matters, so no attempt is made to be sharp.

**Proposition A.1 (*ours*, from `dilate-sum.md` Prop. 4.1(ii)).** *Let $\Phi_n$ be an even
prolate mode at bandwidth $c\ge1$ with $\int_{-1}^1\Phi_n^2=1$, $\Lambda_n$ its concentration
eigenvalue and $\mu_\Phi$ its finite-Fourier eigenvalue, $\mu_\Phi^2=2\pi\Lambda_n/c$. Then*
$$\Phi_n(1)^2\;\le\;\frac{2\pi c\,X_0}{\kappa}\,(1-\Lambda_n),\qquad
X_0:=B_2\,c\,|\mu_\Phi|,\qquad
\kappa:=\frac1{2\pi}\int_0^{2\pi}\big(|\sin\theta|-\tfrac12\big)_+^2d\theta
=\frac1\pi\Big(\frac\pi2+\frac{\sqrt3}4-\sqrt3\Big),$$
*with $B_2=K_1(c)(6c+2^{-1/2})$ the constant of `dilate-sum.md` Prop. 4.1(ii) and $K_1$ the
proved Q1 constant. Since $K_1$ is bounded and $|\mu_\Phi|\le\sqrt{2\pi/c}$, this is*
$$\Phi_n(1)^2\;=\;O\big(c^{5/2}(1-\Lambda_n)\big).$$

*Proof.* Write, as in `dilate-sum.md` §4, $\Phi(x)=\dfrac{a_1\sin(cx)}{x}+W(x)$ with
$a_1=2\Phi(1)/(c\mu_\Phi)$, and $|W(x)|\le B_2|\Phi(1)|x^{-2}$ for $x\ge\sqrt2$ — that is
Prop. 4.1(ii) there, **proved there and quoted, not re-derived here**. For $x\ge X_0$ one has
$B_2|\Phi(1)|x^{-2}\le|a_1|/(2x)$, since $X_0=B_2c|\mu_\Phi|=2B_2|\Phi(1)|/|a_1|$ — and
$X_0\ge\sqrt2$ comfortably, since $X_0\asymp c^{3/2}$, so Prop. 4.1(ii) applies on the whole
range used; hence
$$|\Phi(x)|\;\ge\;\frac{|a_1|}{x}\Big(|\sin cx|-\tfrac12\Big)_+ \qquad(x\ge X_0).$$
Therefore, using $x^{-2}\ge(2X_0)^{-2}$ on $[X_0,2X_0]$ and averaging the oscillation over the
$\ge cX_0/2\pi\gg1$ periods it contains,
$$\int_{X_0}^{2X_0}\Phi^2\,dx\;\ge\;\frac{a_1^2}{4X_0^2}\int_{X_0}^{2X_0}
\big(|\sin cx|-\tfrac12\big)_+^2dx\;\ge\;\frac{\kappa\,a_1^2}{8X_0} .$$
On the other hand $[X_0,2X_0]\subset(1,\infty)$ and, by the exact identity (4.1) of
`h1-mean-value.md` — $\int_{|x|>1}\Phi_n^2=(1-\Lambda_n)/\Lambda_n$, proved there —
$\int_{X_0}^{2X_0}\Phi^2\le(1-\Lambda_n)/(2\Lambda_n)$. Combining, and substituting
$a_1^2=4\Phi(1)^2/(c^2\mu_\Phi^2)$ and $\mu_\Phi^2=2\pi\Lambda_n/c$, gives the claim. ∎

**Corollary A.2 (*ours*).** *For the three-mode combination,
$\Phi(1)^2=O(\mu^{5/2}(1-\chi_2))$, so `q3-log-weight-and-edge.md` Thm 4.4 holds with
$\Xi(\mu)=O(\mu^{6}\log^3\mu)$ — proved, in place of $O(\mu^{9/2}\log^3\mu)$ observed.*

*Proof.* $\Phi(1)=\sum_kb_k\Phi_{n_k}(1)$ over $n_k\in\{0,4,8\}$ with $\sum b_k^2=1$, so
$\Phi(1)^2\le3\sum_kb_k^2\Phi_{n_k}(1)^2$. For $n_k=0,4$, Prop. A.1 gives
$O(c^{5/2}(1-\Lambda_4))$ since $1-\Lambda_0<1-\Lambda_4$. For $n_k=8$,
$b_8^2=O(c^{-8})$ (`prolate-rate.md` §2.1, at the Fuchs rate) and
$1-\Lambda_8=O(c^4(1-\Lambda_4))$ (Fuchs), so that term is $O(c^{-3/2}(1-\Lambda_4))$ and is
negligible. Finally $1-\Lambda_4=2(1-\chi_2)(1+o(1))$. ∎

**Measured (CHECK 8).** The truth, $\Phi_n(1)^2/(c(1-\Lambda_n))$, runs $0.986\to0.998$ at
$n=0$ and $0.866\to0.982$ at $n=4$ across $\mu=3,\dots,20$ — this is `h1-mean-value.md` §7's
observed identity, reproduced. Prop. A.1's proved bound, in the same units, is
$2.4\times10^5$ to $2.8\times10^6$: **the bound holds with a factor $2.4\times10^5$ to
$2.8\times10^6$ to spare**, and the ratio truth/bound falls like $c^{-3/2}K_1^{-1}$, exactly the
looseness the statement advertises. Being loose by $\mu^{3/2}$ costs a power of $\mu$ in $\Xi$
and nothing in the rate.

**What A.1 does *not* do.** It does not prove Q5. The constant $c$ (rather than $\pi c/2$) and
the $-(2n+1)/(4c)$ correction of `h1-mean-value.md` §7 remain **observed**; A.1 only bounds the
same quantity from above by $c^{5/2}$, which is all the rate needs and is $\mu^{3/2}$ away from
the truth.

---

## 11. Provenance

**Read as primary source**, from arXiv LaTeX downloaded 2026-08-12:

- `arxiv.org/e-print/1601.00699`, `PSWF_JCA.tex` (T. M. Dunster, *Asymptotics of prolate
  spheroidal wave functions*, J. Classical Analysis 11 (2017)): title/author `:66`–`:74`;
  abstract `:89`–`:102`; the PSWE `:119`–`:126`; the standing hypothesis $\lambda\to-\infty$
  and the range of $n$ `:143`–`:150`; the remark that [9] assumes $\lambda>0$ `:183`–`:187`;
  §5 "Fixed $m$ and $n$" `:1284`; eq. (107) `:1300`; the Liouville variable (108) `:1310`;
  the perturbation $\hat\rho$ (116)–(117) `:1364`–`:1372`; the error statement (120) `:1388`;
  **eq. (124)** `:1432`–`:1443`; the summary's $\sigma\le\sigma_0<1$ `:1470`–`:1474`.

**Cited by Dunster, not opened by me, and therefore marked:** his [10] (the general
coalescing-turning-point theory that furnishes the explicit error bounds behind (120)), and
his [9] (the $\lambda>0$ companion, SIAM J. Math. Anal. **17** (1986) 1495–1524, whose
*hypothesis* I did read, from the journal abstract page, and which is what places it in the
complementary regime). Nothing here rests on [9]; it is quoted only to locate the regime.

**Classical, quoted and used, not re-derived:** Poisson summation; DLMF 12.7.2
($U(-n-\tfrac12,z)=e^{-z^2/4}\mathit{He}_n(z)$, verified numerically here); Plancherel on the
critical line; Fuchs 1964 Thm 1, used only for the $O(c^{-4})$ rate at which the index-8
admixture vanishes, which §6 Remark 6.3 does not need.

**Taken from our own notes, not re-derived:** the decomposition $\mathcal E\phi=g+r$ and the
identity $QW_\lambda(g,g)=\sum_Z|\mathcal F_\mu r|^2$ (`prolate-rate.md` §6(a)); the three-mode
vector and its admissibility conditions (`prolate-rate.md` §2.1, implemented in
`verify_q3.Comb`); the weight $8/11$ and `start.tex:39`'s $h_4-\sqrt{3/8}h_0$
(`prolate-rate.md` §2.2, mg-aedf); $\Xi=O(\mu^{9/2}\log^3\mu)$ (`q3-log-weight-and-edge.md`
Thm 4.4); Connes' $1-\chi_2$ asymptotic (`prolate-rate.md` §3); the RH-equivalence of the
lower bound (`rhready.tex:1145`).

**Quoted from our own notes inside §A, proved there and not re-derived here:**
`dilate-sum.md` Prop. 4.1(ii) ($|W(x)|\le B_2|\Phi(1)|x^{-2}$ for $x\ge\sqrt2$), with its
$W$ and $a_1$; `h1-mean-value.md` (4.1) ($\int_{|x|>1}\Phi_n^2=(1-\Lambda_n)/\Lambda_n$);
the Q1 constant $K_1$ (`band-edge-connection.md` Thm 5.2). **Q1, Q2 and Q3 themselves are
quoted at their recorded statuses and were not re-verified here**, which is why §9 says what
the $-4\pi$ sentence rests on rather than asserting it flat.

**Derived here, marked *ours* at the point of use:** Observation 1.1 (the corollary needs only
$e^{-o(\mu)}$); Lemma 2.1 (the window identity, with no $\zeta$); Lemmas 3.1–3.3 (localisation,
$\mathcal E$-continuity on a window, tightness from the prolate equation); Props. 4.1–4.2 (the
limit vector, its functional equation, and non-vanishing); the conversion of Dunster's (124)
into (E) in our normalisation (§5); Theorem 6.1 and Remarks 6.2–6.4; Prop. A.1 and Cor. A.2 (§A);
the reading that the §9 description of (H0) is wrong in force (§2).

**The claim here that would do the most damage if wrong** is the conversion of Dunster's
(124) into (E) — the rescaling $x=X/\lambda$, $c=2\pi\lambda^2$, the identification of
$U(-n-\tfrac12,\cdot)$ with $h_n$, and the order perturbation $a=2n+1+O(c^{-1})$ — because
everything else here is elementary and Theorem 6.1 rests on it alone. Its exposure is guarded
in three independent ways: the DLMF identity is verified to 41 digits, the conversion's
*conclusion* is measured directly per mode in CHECK 7 and through the combination in CHECK 4,
and the *consequence* — $\|g\|^2\to0.2192\ldots$ — is measured at five bandwidths in CHECK 3
against a limit computed two independent ways. The second-most damaging would be the regime
check on Dunster's standing hypothesis; that one is quoted verbatim from the source, in his
own symbols, with the conversion $\lambda_{\text{Dunster}}=\chi-c^2$ written out in §0.

---

## 12. Appended by mg-ff96: the Dunster import, checked numerically — *second reader*

Full note: [`dunster-check.md`](dunster-check.md). Script: [`verify_dunster.py`](verify_dunster.py).
Nothing above was rewritten; the in-place marks are HTML comments and the line count is unchanged.

§11 nominated two claims as the ones that would do the most damage if wrong. Both were
attacked. **The first survived; the second did not, in the one respect §11 did not anticipate.**

**The conversion (124) $\Rightarrow$ (E) survives, and (124) itself is confirmed.** Both sides
of (124) were evaluated independently — left from `prolate_even`, right from mpmath's parabolic
cylinder function — at $n=0,2,4,6,8$ and $c=4\pi,\ldots,24\pi$. The quantity (124) actually
bounds, $\sup|{\rm LHS}-{\rm RHS}|/\operatorname{env}U$, times $c/\log c$, is bounded at every
index and decreasing at $n=0,2$. The ratio at $x=0.95$ at $c=24\pi$ is $1.02249$ ($n=0$),
$1.19397$ ($n=4$), $1.56475$ ($n=8$). (107) is confirmed too, with its next coefficient:
$\chi_n=(2n+1)c-\frac{(2n+1)^2+5}8+O(c^{-1})$.

**The regime check did not survive intact.** §11 says it "is quoted verbatim from the source".
The *quotation* is fine; the *numeric check attached to it* in §5 is not. Three corrections,
all marked in place above:

1. Dunster's standing hypothesis is **(29)** at `PSWF_JCA.tex:466`, $0\le\sigma=\sqrt{\chi_n}/c
   \le\sigma_0<1$ with $\sigma_0$ **fixed**, not $\lambda<0$. §5 states this correctly in its
   "summary §6" sentence and then §0 and Bottom line 4 print the weaker form.
2. §5's "$\sigma\le0.8$ with room" is **false at index 8**: $\sigma=0.883$ at $\mu=3$, which is
   a row of §7 CHECK 6 above. The $0.020$–$0.64$ range it quotes from `h1-mean-value.md` §5 was
   measured at $n\le4$; $\phi_\lambda$ carries index 8.
3. At $\mu=2$, $\sigma=1.0199$ and **the hypothesis fails outright** — $\chi_8>c^2$, Dunster's
   $\lambda>0$, the case he assigns to [9] and not to this paper. The threshold is
   $c^*_8=13.3006991$, $\mu^*=2.1168720$. `verify_q1.py` CHECK 6 already prints this cell as
   failing *Q1's* hypothesis (mg-6851); §5 did not carry it across to Dunster's.

**Theorem 6.1 is undisturbed**, and the reason is structural rather than lucky: (E) enters only
at step (i), a $\lambda\to\infty$ limit at fixed $n$, and $\sigma_n(c)\to0$, so the limit is
taken well inside (29). §7's tables are measurements, not applications of (E).

**Two further corrections that cost nothing but should be on the record.**

- §10 H0-1 records one unopened source. There are **two**: Dunster [10] for (124)'s error
  bounds, and Arscott [1, p. 186] for (107)'s, via his (27) at `:455`. The chain is two deep.
- §7 CHECK 7's clean $O(1/c)$ is **not** evidence that (124) is accurate at those bandwidths.
  Splitting the error, Dunster's part and the conversion's part are each about three times the
  total and largely cancel ($n=4$, $c=24\pi$: $0.1031$ and $0.0923$ against $0.0315$).

**What did not change.** (H0), Theorem 6.1, the constant $0.2192471995\ldots$, the $-4\pi$
bound, or G13's status as an external dependency. A numerical check is not a proof. What it
buys is that G13 is now a *tested* import, with its hypotheses enumerated and one of them
found to bite.
