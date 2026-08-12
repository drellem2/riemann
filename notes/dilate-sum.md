# Q2 is proved: the dilate sum is a sawtooth plus an absolutely convergent tail

Work item mg-9d43. Companion script: [`verify_q2.py`](verify_q2.py) (needs `mpmath`;
no `numpy`; imports the prolate apparatus of [`verify_prolate_rate.py`](verify_prolate_rate.py)
and the entire-extension apparatus of [`verify_h1.py`](verify_h1.py)).
Answers item **Q2** of [`h1-mean-value.md`](h1-mean-value.md) §9 —
the item [`band-edge-connection.md`](band-edge-connection.md) §9 calls "now the whole
remaining content of (P)".

Nothing in `start.tex`, `s3.tex` or the paper was edited. `h1-mean-value.md` and
`band-edge-connection.md` are annotated in place, line-count-preserving, plus one
appended section each.

**Calibration, before anything else.** (P) is a bound on $\sup_{t>1}t|G(t)|$, a
**magnitude**. Proving it turns `prolate-rate.md`'s and the paper's *conditional*
upper bound $\limsup\mu^{-1}\log s(\mu)\le-4\pi$ into an unconditional one **once
Q3 is written** — an improvement to a result the project already has, and **not
progress toward RH**. The matching lower bound is not open — it *is* RH
(`rhready.tex:1145`, paper Thm `thm:boundary`, gap **G10**). §8 applies the house
rule and every line below is sign-blind, which is correct here rather than a defect.

---

## Bottom line

**1. Q2 is proved, with $K_P(c)=O(\log c)$.** For every even index $n$, every
$c>\sqrt2$ and every $\chi_n$ with $0\le\chi_n<c^2$,
$$\sup_{t>1}\;t\,\Big|\sum_{m\ge1}\Phi_n(mt)\Big|\;\le\;K_P(c)\,|\Phi_n(1)|,\qquad
K_P(c)=\frac{\pi}{c|\mu_\Phi|}+B_1\big(1+\log X_*\big)+\frac{2B_2}{X_*},$$
with $B_1=K_1(c)+\frac{2}{c|\mu_\Phi|}$, $B_2=K_1(c)\big(6c+2^{-1/2}\big)$,
$X_*=\max(\sqrt2,B_2/B_1)$ and $K_1(c)=2^{3/4}e^{E(c)}$ the **proved** Q1 constant of
`band-edge-connection.md` Thm 5.2. $K_P$ grows like $\log c$, i.e. slower than any
power — comfortably subexponential, which is all `h1-mean-value.md` Prop. 4.1 asks.
Numerically $K_P=26.5$ at $c=4\pi$, falling to a minimum $17.9$ near $c\approx80$ and
back to $22.9$ at $c=2000\pi$; it never exceeds $27$ in this project's range. The
truth is $0.94$–$1.05$, measured across four bandwidths and three indices and flat
in $c$ (§7), so the proof is loose by a factor $17$–$28$ and **the shape of (P) is
right**: no constant below $0.94$ is admissible. §5.

**2. The note's own diagnosis of Q2 was wrong, and it is what made Q2 look hard.**
`h1-mean-value.md` §9 says "what must be controlled is the sum of the *remainders*
in Osipov–Rokhlin's exact expansion", and its §6 rejects that expansion because the
remainder is "an object of the same exponential size as the term being bounded".
**The exponential size was never the problem.** $\sum_m\frac{|\Phi(1)|}{mt}$
diverges because of the $1/m$, not because $|\Phi(1)|$ is large; a remainder of
exactly the size $|\Phi(1)|$ is harmless the moment it carries $x^{-2}$ instead of
$x^{-1}$. **What (P) needs is decay in $x$, not smallness in $c$**, and the note
inverted which variable was resisting. §1.

That is the **second** inherited misdiagnosis on this chain: mg-6851 refuted §5's
"connection at the regular singular point", and this refutes §9's "control the
Osipov–Rokhlin remainders". Both notes were right that a mechanism was needed and
wrong about which quantity was resisting.

**3. The proof is one application of variation of parameters, and Q1 is exactly the
input that makes it work.** In the Liouville form $u:=\sqrt{x^2-1}\,\Phi$ satisfies
$u''+(c^2+\epsilon)u=0$ with $\epsilon=\frac{c^2-\chi+1}{x^2-1}$ integrable at
infinity. Q1 says $x|\Phi|\le K_1|\Phi(1)|$, which says **exactly that $u$ is
bounded** — and bounded $u$ plus integrable $\epsilon$ gives
$\int^\infty|\alpha'|+|\beta'|<\infty$ for the Lagrange coefficients, hence
convergence of the amplitudes at rate $O(c/x)$, hence the $x^{-2}$ remainder. §§3–4.

**4. The whole thing turns on $\beta_\infty=0$ — the leading off-band term is a
*pure sine*, with no cosine — and that is a quantisation statement, not an ODE
statement.** $\sum_m\frac{\sin(cmt)}{m}$ is the bounded sawtooth, but
$\sum_m\frac{\cos(cmt)}{m}=-\log|2\sin(ct/2)|$ is **unbounded** at every resonance.
So a solution of the same ODE with $\beta_\infty\neq0$ has
$\sup_{t>1}t|G(t)|=+\infty$: **(P) is false for a general solution and true for the
eigenfunctions.** $\beta_\infty=0$ is proved here from the finite-Fourier
eigenrelation plus Riemann–Lebesgue, and it is the one place in this note where
anything beyond the differential equation is used. §3.

**5. The computational blocker was real and it was on the wrong side of a Poisson
summation.** mg-8462 reported Q2 as unverifiable because "the evaluation cost of
$\Phi(nt)$ for large $n$ defeated it". With $h=2\pi/(ct)=1/(\mu t)$,
$$t\,G(t)\;=\;\frac{1}{2\mu\,\mu_\Phi}\sideset{}{'}\sum_{|k|\le\lfloor\mu t\rfloor}
\Phi\!\Big(\frac{k}{\mu t}\Big)\;-\;\frac{t\,\Phi(0)}{2},$$
an **exact identity**: the infinite, conditionally convergent sum of *off-band*
values — each costing $O(cmt)$ Bessel values — becomes a **finite** sum of
$\lfloor\mu t\rfloor+1$ *on-band* values, each a Legendre series. At $\mu=5,t=3$
that is 16 cheap terms. The price is arithmetic, not algorithmic: the two terms are
of size $t\Phi(0)$ and cancel down to $|\Phi(1)|$, so $10^{3}$ to $10^{8}$ of
cancellation, reported rather than assumed. §6.

**6. A latent sign defect in the shared apparatus, found and fixed here.**
`verify_h1.sph_j_all` normalises on the sum rule — its docstring explains at length
why normalising on $j_0(z)=\sin z/z$ is wrong, since $z=cx$ is a multiple of $\pi$
exactly when $x$ is an integer — and then **fixes the remaining sign by that same
ill-conditioned quantity**. At $c=6\pi$, $x=200$ the test compares against
$\sin z=10^{-118}$, i.e. against rounding noise, and returns the wrong global sign:
$\Phi(200)$ comes back $+1.281\times10^{-8}$ between neighbours $-1.374\times10^{-8}$
and $-1.189\times10^{-8}$. **It invalidates nothing in `h1-mean-value.md` or
`band-edge-connection.md`** — every number those notes report is a *modulus*, and a
global sign flip is invisible in a modulus — but it is fatal here, where the
explicit leading term is subtracted. §7, and the fix is in `verify_q2.py`.

**7. Which outcome of the ticket is this?** Outcome **(1)**, proved, with the
ticket's own premise refuted along the way — the ticket asked for that explicitly and
it is §1. The hypotheses are $c>\sqrt2$, $0\le\chi_n<c^2$, $n$ even, and the
finite-Fourier eigenrelation; **no zeta zeros, no sign, no numerical input.** It is
**not a proof of H1**: what H1 still needs is **Q3**, which `h1-mean-value.md` §9
calls routine-but-unwritten, and the corollary needs **Q4 (H0)**, untouched. §9.

---

## 0. Conventions, and what is being assumed

`h1-mean-value.md` §0's conventions unchanged, including its warnings about the
collisions with Connes–Consani's and Osipov–Rokhlin's labels. $\Phi_n=\Phi_{n,c}$ is
$\mathit{PS}_{n,0}$ at bandwidth $c=2\pi\mu$, normalised by $\int_{-1}^1\Phi_n^2=1$
and extended to the entire function it is; $\chi_n$ is the prolate ODE eigenvalue,
$\Lambda_n$ the Slepian concentration eigenvalue, $\mu_\Phi$ the finite-Fourier
eigenvalue with $\Lambda_n=\frac{c}{2\pi}\mu_\Phi^2$, so $c|\mu_\Phi|=\sqrt{2\pi\Lambda_nc}$.

Throughout §§2–5 fix $c>\sqrt2$, an **even** index $n$, and $\chi:=\chi_n$ with
$0\le\chi<c^2$. Three facts about $\Phi:=\Phi_n$ are used and no others:

- **(E)** the **prolate equation** $\big((1-x^2)\Phi'\big)'+(\chi-c^2x^2)\Phi=0$,
  with $\Phi$ real and analytic at $x=1$;
- **(F)** the **finite-Fourier eigenrelation**
  $\int_{-1}^1\Phi(y)e^{icxy}\,dy=\mu_\Phi\,\Phi(x)$, valid for **all** $x$ (not
  merely $|x|\le1$), with $\mu_\Phi\neq0$ real — $n$ even makes $\Phi$ even and
  $\mu_\Phi=i^n|\mu_\Phi|$ real;
- **(Q1)** `band-edge-connection.md` **Thm 5.2**: $x|\Phi(x)|\le K_1(c)|\Phi(1)|$ for
  $x\ge1$, with $K_1(c)=2^{3/4}e^{E(c)}$ bounded and independent of $n$.

(E) and (Q1) are the ODE; (F) is the eigenvalue condition, and §3 shows it is
**not** removable — the theorem is false without it.

$$G(t):=\sum_{m\ge1}\Phi(mt),\qquad t>1,$$
the limit of the symmetric partial sums, which §5 shows exists.

---

## 1. Why the note's own diagnosis of Q2 was not the way in — *ours*

`h1-mean-value.md` §9's **Q2** row reads:

> The mechanism is the sawtooth $\sum_n n^{-1}\sin(cnt)$ (§4); what must be
> controlled is the sum of the *remainders* in Osipov–Rokhlin's exact expansion,
> which is the off-band leakage of $t\Phi(t)$ (§6).

**The first clause is right. The second is wrong, and it is the second that made Q2
look hard.** That note's §6 rejects the Osipov–Rokhlin expansion with

> That remainder is not a nuisance term. […] **the out-of-band leakage of
> $t\Phi(t)$** — an object of the same exponential size as the quantity being
> bounded […] The identity is therefore a *bootstrap relation among the off-band
> values of the whole prolate family*, not an estimate for one of them.

Every clause of that is true and none of it is an obstruction, because **(P) does
not need the remainder to be small.** Look at what actually fails in the naive
argument. Q1 gives $|\Phi(mt)|\le K_1|\Phi(1)|/(mt)$, so
$$t|G(t)|\;\le\;K_1|\Phi(1)|\sum_{m\ge1}\frac1m\;=\;\infty .$$
The divergence is *harmonic*. It is caused by the exponent $1$ in $x^{-1}$ and by
nothing else; the factor $|\Phi(1)|$ sits outside the sum and its size is
irrelevant. A remainder of *exactly* the size $|\Phi(1)|$ — the size §6 rejects as
fatal — costs nothing at all provided it decays like $x^{-2}$, because
$\sum_m m^{-2}<\infty$.

> **What (P) needs is one more power of $x$, not one more power of $e^{-c}$.**

Once that is seen the proof is short, and the reason it is short is that Q1 has
already been proved: §4's remainder bound is Q1 plus a single integration of the
Lagrange system. Prop. 4.1(ii) delivers a remainder of size $\asymp c|\Phi(1)|x^{-2}$
— *larger* in $c$ than the leading term by a factor $c^{3/2}$, and completely
harmless.

**Recorded as the ticket asked.** This is the second time on this chain that a
note's account of its own obstruction pointed away from the proof. mg-6851 refuted
`h1-mean-value.md` §5's "connection through the regular singular point"; this
refutes its §9's "control the Osipov–Rokhlin remainders". The common shape is worth
naming: **both diagnoses identified a true difficulty in the wrong variable** — the
first put the difficulty at a place ($x=1$) where the inequality was free, the
second put it in a size ($e^{-c}$) that the inequality never asked about.

---

## 2. The exact off-band identity, and the band-edge Taylor data — *ours (elementary)*

**Lemma 2.1 (ours; two integrations by parts).** *For $x\neq0$,*
$$\mu_\Phi\,\Phi(x)\;=\;\frac{2\Phi(1)\sin(cx)}{cx}\;+\;\frac{2\Phi'(1)\cos(cx)}{(cx)^2}
\;-\;\frac{J(x)}{(cx)^2},\qquad J(x):=\int_{-1}^{1}\Phi''(y)\cos(cxy)\,dy,
\tag{2.1}$$
*and $J(x)\to0$ as $x\to\infty$.*

*Proof.* $\Phi$ even makes the sine part of (F) vanish, so
$\mu_\Phi\Phi(x)=\int_{-1}^1\Phi(y)\cos(cxy)dy$. Integrating by parts once, and using
$\Phi(-1)=\Phi(1)$,
$$\int_{-1}^1\Phi\cos(cxy)\,dy=\frac{2\Phi(1)\sin(cx)}{cx}-\frac1{cx}\int_{-1}^1\Phi'\sin(cxy)\,dy ;$$
again, using $\Phi'$ odd so that $\Phi'(1)-\Phi'(-1)=2\Phi'(1)$,
$$\int_{-1}^1\Phi'\sin(cxy)\,dy=-\frac{2\Phi'(1)\cos(cx)}{cx}+\frac{J(x)}{cx}.$$
Combine. $\Phi$ is entire, so $\Phi''$ is continuous on $[-1,1]$, hence in $L^1$, and
$J(x)\to0$ by Riemann–Lebesgue. ∎

**The band-edge Taylor data.** Evaluating (E) and its first derivative at $x=1$,
where $1-x^2$ vanishes:
$$\Phi'(1)=\frac{\chi-c^2}{2}\,\Phi(1),\qquad
\Phi''(1)=\frac{(\chi-c^2-2)\Phi'(1)-2c^2\Phi(1)}{4}. \tag{2.2}$$
(The exponents at the regular singular point $x=1$ are $0,0$, so the solution
analytic there is determined up to scale and *every* $\Phi^{(m)}(1)$ is an explicit
multiple of $\Phi(1)$; only these two are used.) Both are checked against finite
differences of the Legendre series to 29 digits in §7.

Write, for later use,
$$a_1:=\frac{2\Phi(1)}{c\,\mu_\Phi},\qquad
a_2:=\frac{2\Phi'(1)}{c^2\mu_\Phi},\qquad
a_3:=-\frac{2\Phi''(1)}{c^3\mu_\Phi}, \tag{2.3}$$
so that (2.1) and one further integration by parts give
$\Phi(x)=\frac{a_1\sin cx}{x}+\frac{a_2\cos cx}{x^2}+\frac{a_3\sin cx}{x^3}+O(x^{-4})$
— used only in §7, to accelerate an independent numerical evaluation, never in the
proof.

*Note $a_1$ is Osipov–Rokhlin's leading off-band coefficient
(`h1-mean-value.md` §6(c)), reached here by two lines of integration by parts rather
than borrowed. That is deliberate: their statement is an identity valid everywhere,
so re-deriving the part of it this note needs costs nothing and removes a citation
whose hypotheses would otherwise have to be re-checked.*

---

## 3. The Liouville form, and the two constants at infinity — *ours (classical technique)*

**Lemma 3.1 (ours).** *Put $u:=\sqrt{x^2-1}\,\Phi$. On $x>1$,*
$$u''+\big(c^2+\epsilon(x)\big)\,u=0,\qquad
\epsilon(x)=\frac{c^2-\chi+1}{x^2-1}\;>\;0. \tag{3.1}$$

*Proof.* (E) is $(p\Phi')'+q\Phi=0$ with $p=x^2-1$, $q=c^2x^2-\chi$. Substituting
$\Phi=p^{-1/2}u$ gives $(p\Phi')'=p^{1/2}u''-\tfrac12(p^{-1/2}p')'u$, so
$$u''+\Big[\frac qp-\frac{(p^{-1/2}p')'}{2p^{-1/2}}\Big]u=0 .$$
With $p'=2x$, $p^{-1/2}p'=2x(x^2-1)^{-1/2}$ and
$(p^{-1/2}p')'=2(x^2-1)^{-1/2}-2x^2(x^2-1)^{-3/2}=-2(x^2-1)^{-3/2}$, so the bracket's
second term is $-\frac1{x^2-1}$ and
$\frac qp+\frac1{x^2-1}=\frac{c^2x^2-\chi+1}{x^2-1}=c^2+\frac{c^2-\chi+1}{x^2-1}$.
Positivity of $\epsilon$ is $\chi<c^2$. ∎

**Lemma 3.2 (ours; the Lagrange system, and Q1 is what closes it).** *Write, on
$(1,\infty)$,*
$$u=\alpha\sin(cx)+\beta\cos(cx),\qquad u'=c\big(\alpha\cos(cx)-\beta\sin(cx)\big),$$
*which determines $\alpha,\beta$ uniquely and gives*
$$\alpha'=-\frac{\epsilon}{c}\,u\cos(cx),\qquad \beta'=\frac{\epsilon}{c}\,u\sin(cx).
\tag{3.2}$$
*Then $|u|\le K_1|\Phi(1)|$ on $(1,\infty)$, the limits
$\alpha_\infty=\lim\alpha$, $\beta_\infty=\lim\beta$ exist, and for every
$X\ge\sqrt2$*
$$|\alpha(X)-\alpha_\infty|+|\beta(X)-\beta_\infty|\;\le\;\frac{6\,c\,K_1\,|\Phi(1)|}{X}.
\tag{3.3}$$

*Proof.* Differentiating $u=\alpha\sin+\beta\cos$ and imposing
$\alpha'\sin+\beta'\cos=0$ gives $u''=c(\alpha'\cos-\beta'\sin)-c^2u$; comparing with
(3.1), $c(\alpha'\cos-\beta'\sin)=-\epsilon u$, and solving the two linear equations
for $(\alpha',\beta')$ gives (3.2).

**The bound on $u$ is Q1 and only Q1**: $|u|=\sqrt{x^2-1}\,|\Phi(x)|
\le\frac{\sqrt{x^2-1}}{x}\,K_1|\Phi(1)|\le K_1|\Phi(1)|$. (Lemma 5.1 of
`h1-mean-value.md`, $|\Phi|\le|\Phi(1)|$, is *not* enough: it gives
$|u|\le\sqrt{x^2-1}\,|\Phi(1)|$, which grows, and then $\int|\alpha'|$ diverges. The
factor $x$ that Q1 adds is exactly the factor that makes $u$ bounded.)

Hence $|\alpha'|,|\beta'|\le\frac{\epsilon}{c}K_1|\Phi(1)|$, and for $X\ge\sqrt2$,
using $\chi\ge0$ and $\operatorname{artanh}s\le\frac{s}{1-s^2}$,
$$\int_X^\infty\epsilon
=(c^2-\chi+1)\,\operatorname{artanh}\frac1X
\;\le\;(c^2+1)\,\frac{X}{X^2-1}\;\le\;\frac{2(c^2+1)}{X},$$
the last step because $X^2-1\ge X^2/2$ for $X\ge\sqrt2$. Since $c>\sqrt2$ gives
$2(c^2+1)\le3c^2$,
$$\int_X^\infty|\alpha'|,\ \int_X^\infty|\beta'|\;\le\;\frac{K_1|\Phi(1)|}{c}\cdot\frac{3c^2}{X}
=\frac{3cK_1|\Phi(1)|}{X}.$$
Both integrals are finite, so the limits exist, and (3.3) is the sum of the two
tails. ∎

**Lemma 3.3 (ours; the constants, and where the eigenvalue condition enters).**
$$\alpha_\infty=a_1=\frac{2\Phi(1)}{c\,\mu_\Phi},\qquad \boxed{\beta_\infty=0.}$$

*Proof.* By Lemma 3.2, $u(x)-\alpha_\infty\sin(cx)-\beta_\infty\cos(cx)\to0$. By
Lemma 2.1 and $J(x)\to0$, $x\Phi(x)-a_1\sin(cx)\to0$. And
$x\Phi(x)-u(x)=\big(\tfrac{x}{\sqrt{x^2-1}}-1\big)u(x)\to0$ since $u$ is bounded.
Subtracting,
$$(\alpha_\infty-a_1)\sin(cx)+\beta_\infty\cos(cx)\;\longrightarrow\;0
\qquad(x\to\infty),$$
and evaluating along $cx=2\pi k$ and $cx=\tfrac\pi2+2\pi k$ gives $\beta_\infty=0$
and $\alpha_\infty=a_1$. ∎

**This is the load-bearing line of the note, and it is not an ODE statement.**
$\beta_\infty=0$ says the phase accumulated from the band edge out to infinity is
*exactly* commensurate with $\sin(cx)$. That is a quantisation condition on $\chi$: a
solution of (E) analytic at $x=1$ with $\chi$ **not** a prolate eigenvalue has
$\beta_\infty\neq0$ in general, and Lemma 3.3 is proved from (F), not from (E). The
consequence is sharp, because
$$\sum_{m\ge1}\frac{\sin m\gamma}{m}=\frac{\pi-\gamma}{2}\ \ (0<\gamma<2\pi)
\quad\text{is bounded, while}\quad
\sum_{m\ge1}\frac{\cos m\gamma}{m}=-\log\big|2\sin\tfrac\gamma2\big|
\quad\text{is not.}$$

> **Corollary 3.4 (ours).** For a solution of (E) analytic at $x=1$ with
> $\beta_\infty\neq0$, $\sup_{t>1}t\,|G(t)|=+\infty$: the sum diverges
> logarithmically as $ct$ approaches $2\pi\mathbb Z$.
>
> **So (P) is *false* for a general solution of the prolate equation and true for
> the eigenfunctions.** No argument using (E) alone can prove Q2, and any argument
> that appears to is wrong. This is the precise sense in which Q2 is not, unlike
> Q1, a two-parameter ODE statement.

---

## 4. The remainder decays like $x^{-2}$ — *ours*

**Definition.** $W(x):=\Phi(x)-\dfrac{a_1\sin(cx)}{x}$ for $x\ge1$.

**Proposition 4.1 (ours).** *For all $x\ge1$,*
$$\text{(i)}\quad |W(x)|\;\le\;\frac{B_1|\Phi(1)|}{x},\qquad
B_1:=K_1(c)+\frac{2}{c|\mu_\Phi|},$$
*and for all $x\ge\sqrt2$,*
$$\text{(ii)}\quad |W(x)|\;\le\;\frac{B_2|\Phi(1)|}{x^{2}},\qquad
B_2:=K_1(c)\Big(6c+\frac1{\sqrt2}\Big).$$

*Proof.* (i) $|W(x)|\le|\Phi(x)|+\frac{|a_1|}{x}\le\frac{K_1|\Phi(1)|}{x}
+\frac{2|\Phi(1)|}{c|\mu_\Phi|\,x}$, by Q1 and $|\sin|\le1$.

(ii) Since $x\Phi(x)=\frac{x}{\sqrt{x^2-1}}u(x)$,
$$x\,W(x)=x\Phi(x)-a_1\sin(cx)
=\Big(\frac{x}{\sqrt{x^2-1}}-1\Big)u(x)
\;+\;\big[(\alpha(x)-\alpha_\infty)\sin(cx)+(\beta(x)-\beta_\infty)\cos(cx)\big],$$
using Lemma 3.3 to replace $a_1$ by $\alpha_\infty$ and $0$ by $\beta_\infty$. For
$x\ge\sqrt2$ put $s=x^{-2}\le\tfrac12$; then $(1-s)^{-1/2}\le1+s$, because
$(1+s)^2(1-s)=1+s-s^2-s^3\ge1$ for $s\le\tfrac12$, so
$\big|\tfrac{x}{\sqrt{x^2-1}}-1\big|\le x^{-2}$. With $|u|\le K_1|\Phi(1)|$ and
(3.3),
$$x\,|W(x)|\;\le\;\frac{K_1|\Phi(1)|}{x^{2}}+\frac{6cK_1|\Phi(1)|}{x},$$
so $x^2|W(x)|\le K_1|\Phi(1)|\big(\tfrac1x+6c\big)\le K_1|\Phi(1)|\big(6c+2^{-1/2}\big)$. ∎

**What (ii) costs and what it buys.** $B_2\asymp6cK_1$ is *larger* than the leading
coefficient $|a_1|/|\Phi(1)|=\frac{2}{\sqrt{2\pi\Lambda_nc}}$ by a factor
$\asymp c^{3/2}$. That is fine and is the whole point of §1: the remainder is allowed
to dominate the main term in size, provided it decays one power faster in $x$. §7
measures the true ratio at $3\times10^{-3}$ of the proved $B_2$, so the bound is
loose by about $300$ — and the looseness is inherited, since $6c$ comes from
$\int_X^\infty\epsilon\asymp c^2/X$ divided by $c$, and $\epsilon$ is genuinely that
big near the band edge.

---

## 5. The theorem — *ours*

**Theorem 5.1 (Q2).** *Let $c>\sqrt2$, let $n$ be even and $0\le\chi_n<c^2$, and let
$\Phi=\Phi_{n,c}$ satisfy (E), (F) and (Q1). Then for every $t>1$ the series
$G(t)=\sum_{m\ge1}\Phi(mt)$ converges, and*
$$\sup_{t>1}\;t\,|G(t)|\;\le\;K_P(c)\,|\Phi(1)|,$$
$$K_P(c)\;=\;\frac{\pi}{c|\mu_\Phi|}\;+\;B_1\big(1+\log X_*\big)\;+\;\frac{2B_2}{X_*},
\qquad X_*:=\max\Big(\sqrt2,\ \frac{B_2}{B_1}\Big).$$
*When $X_*=B_2/B_1$ this is $K_P=\frac{\pi}{c|\mu_\Phi|}+B_1\big(3+\log\frac{B_2}{B_1}\big)
\le\frac{\pi}{c|\mu_\Phi|}+B_1\big(3+\log(6c+1)\big)$, so $K_P(c)=O(\log c)$ —
subexponential, and indeed sub-polynomial.*

*Proof.* Fix $t>1$ and write $\gamma:=ct\bmod2\pi\in[0,2\pi)$. For every $N$,
$$\sum_{m=1}^{N}\Phi(mt)=\frac{a_1}{t}\sum_{m=1}^{N}\frac{\sin(m\gamma)}{m}
+\sum_{m=1}^{N}W(mt).$$
The first sum converges as $N\to\infty$ (Dirichlet's test) to $\frac{\pi-\gamma}{2}$
for $\gamma\in(0,2\pi)$ and to $0$ for $\gamma=0$, of modulus $\le\frac\pi2$ in
either case. The second converges absolutely by Prop. 4.1(ii). So $G(t)$ exists and
$$t\,|G(t)|\;\le\;\frac{\pi}{2}\,|a_1|\;+\;t\sum_{m\ge1}|W(mt)| .$$
The first term is $\frac{\pi|\Phi(1)|}{c|\mu_\Phi|}$. For the second, split at
$X_*\ (\ge\sqrt2$, so Prop. 4.1(ii) applies above it, and $mt>1$, so Prop. 4.1(i)
applies below it$)$:
$$t\!\!\sum_{mt<X_*}\!\!|W(mt)|\;\le\;B_1|\Phi(1)|\!\!\sum_{m<X_*/t}\!\!\frac1m
\;\le\;B_1|\Phi(1)|\big(1+\log(X_*/t)\big)\;\le\;B_1|\Phi(1)|\big(1+\log X_*\big),$$
since $t>1$; and with $N_*:=\lceil X_*/t\rceil\ge X_*/t$ and
$\sum_{m\ge N}m^{-2}\le N^{-2}+\int_N^\infty s^{-2}ds\le\frac2N$,
$$t\!\!\sum_{mt\ge X_*}\!\!|W(mt)|\;\le\;\frac{B_2|\Phi(1)|}{t}\sum_{m\ge N_*}\frac1{m^2}
\;\le\;\frac{B_2|\Phi(1)|}{t}\cdot\frac{2t}{X_*}\;=\;\frac{2B_2|\Phi(1)|}{X_*}. \qquad\blacksquare$$

**The constant, evaluated.** $K_1$, $B_1$, $B_2$, $K_P$ at the bandwidths this
project uses, computed from the closed forms above with $\Lambda_n\to1$:

| $\mu$ | $c$ | $K_1(c)$ | $B_1$ | $B_2$ | $X_*$ | $K_P(c)$ |
|---|---|---|---|---|---|---|
| 2 | $12.566$ | $3.3792$ | $3.6042$ | $257.17$ | $71.35$ | $26.548$ |
| 3 | $18.850$ | $2.6149$ | $2.7987$ | $297.59$ | $106.3$ | $21.745$ |
| 5 | $31.416$ | $2.1689$ | $2.3113$ | $410.36$ | $177.6$ | $19.128$ |
| 8 | $50.265$ | $1.9648$ | $2.0773$ | $593.95$ | $285.9$ | $18.157$ |
| 12 | $75.398$ | $1.8632$ | $1.9551$ | $844.21$ | $431.8$ | $17.873$ |
| 100 | $628.32$ | $1.7022$ | $1.7340$ | $6418.2$ | $3701$ | $19.499$ |
| 1000 | $6283.2$ | $1.6838$ | $1.6939$ | $63479$ | $37476$ | $22.936$ |
| — | $\to\infty$ | $\to1.6818$ | $\to1.6818$ | $\asymp6c$ | — | $\to2^{3/4}\big(3+\log6c\big)$ |

$K_P$ is **not** monotone: it falls to a minimum $\approx17.87$ near $c\approx80$
($\mu\approx13$) and then grows like $2^{3/4}\log c$. It never exceeds $27$ anywhere
in this project's range. Measured truth: $0.94$–$1.05$, attained as $t\to1^+$ (§7).

**Corollary 5.2 (the three-mode combination).** *Let
$\phi=\sum_m b_m\Phi_{n_m}$ with every $n_m$ even and $0\le\chi_{n_m}<c^2$. Then*
$$\sup_{t>1}t\Big|\sum_{k\ge1}\phi(kt)\Big|\;\le\;\Big(\max_m K_P^{(m)}(c)\Big)
\sum_m|b_m|\,\big|\Phi_{n_m}(1)\big| .$$
*(Immediate, by linearity: apply Thm 5.1 to each mode. $K_P^{(m)}$ depends on the
index only through $\Lambda_{n_m}$ in the two $O(c^{-1/2})$ terms.)*

**What Cor. 5.2 does and does not give, stated rather than smoothed.** The
right-hand side is $\sum_m|b_m||\Phi_{n_m}(1)|$, not $|\phi(1)|$. Two remarks:

- **What `h1-mean-value.md` §4 actually consumes** is $N(\alpha)\ll\lambda^{2\alpha}K^2\,c\,(1-\Lambda_4)$,
  reached from (P) through that note's §7 identity $\Phi_n(1)^2\asymp c(1-\Lambda_n)$.
  Since $1-\Lambda_n$ increases rapidly in $n$, the sum
  $\sum_m|b_m||\Phi_{n_m}(1)|$ is dominated by its top *retained* index and is
  $\asymp|b_2|\sqrt{c(1-\Lambda_4)}$ — which is what Prop. 4.1 needs, **without**
  passing through $|\phi(1)|$ at all.
- **(P) in its literal wording** additionally needs
  > **(C)** $\sum_m|b_m||\Phi_{n_m}(1)|\le C\,|\phi(1)|$ — *no cancellation at the
  > band edge.*

  This is **observed, not proved**: $C=1.0089$ at $c=6\pi$ and $1.0018$ at $c=16\pi$
  (§7, CHECK 4), the index-4 term outweighing the others by $10^{3.8}$ and $10^{2.4}$.
  It would follow at once from `h1-mean-value.md` §7's endpoint identity — which is
  that note's **Q5, itself observed only**. So the chain already leans on one
  observed identity at this junction and (C) adds no new kind of exposure; it is
  recorded as a hypothesis rather than absorbed.

**Every hypothesis, and the confirmation that none smuggles in a lower bound.**
$c>\sqrt2$; $n$ even; $0\le\chi_n<c^2$; (E), (F), (Q1). $\chi_n\ge n(n+1)\ge0$ is
free. **No zeta zeros appear, no numerical input appears, and no sign appears.**
Every conclusion is an *upper* bound on a modulus, and each step is an application of
the triangle inequality, Q1, or an identity; nothing anywhere produces a lower bound
on $|G|$, on $|\Phi|$ or on $s(\mu)$, and by §8 nothing could. **The one hypothesis
that fails at a corner** is $\chi_n<c^2$: `band-edge-connection.md` §7 measures
$\chi_8/c^2=1.040$ at $c=4\pi$, so Thm 5.1, like Thm 5.2 before it, does not cover
prolate index 8 at $\mu=2$. It covers index 8 from $\mu=3$ on and indices $0,2,4,6$
throughout. Inherited, not new, and not re-opened here.

---

## 6. The identity that makes $G$ computable — *ours (classical technique)*

**Proposition 6.1 (ours; Poisson on the band).** *Let $t>0$, $h:=\frac{2\pi}{ct}=\frac1{\mu t}$
and $M:=\lfloor\mu t\rfloor$. Then*
$$t\,G(t)\;=\;\frac{1}{2\mu\,\mu_\Phi}\;\sideset{}{'}\sum_{|k|\le M}
\Phi\!\left(\frac{k}{\mu t}\right)\;-\;\frac{t\,\Phi(0)}{2}, \tag{6.1}$$
*where the prime halves the terms $k=\pm M$ in the exceptional case $\mu t\in\mathbb Z$.*

*Proof.* Put $P:=\Phi\cdot\mathbf 1_{[-1,1]}$, of bounded variation and compactly
supported. By **(F)** — which holds at *every* real $\omega$, not merely
$|\omega|\le c$ — its Fourier transform is
$\hat P(\omega)=\int_{-1}^1\Phi(y)e^{-i\omega y}dy=\mu_\Phi\Phi(\omega/c)$. The
$h$-periodisation of $P$ is of bounded variation, so its Fourier series converges
pointwise (Dirichlet–Jordan) to the mid-value at each point, giving Poisson
summation
$$\sideset{}{'}\sum_{k\in\mathbb Z}P(kh)=\frac1h\sum_{m\in\mathbb Z}\hat P\!\Big(\frac{2\pi m}{h}\Big)$$
with the right side summed symmetrically. Now $\frac{2\pi m}{hc}=mt$, so the right
side is $\mu t\,\mu_\Phi\sum_{m\in\mathbb Z}\Phi(mt)=\mu t\,\mu_\Phi\big(\Phi(0)+2G(t)\big)$
by evenness, and the left side is the finite sum over $|k|\le M$. Rearranging gives
(6.1). ∎

**Why this is the engineering unlock, and why mg-8462 was blocked.** That note
records Q2 as *"not verified numerically here either — the evaluation cost of
$\Phi(nt)$ for $n$ large defeated it in this session"*. Both sides of (6.1) compute
the same number and the costs are not comparable:

| | left side (direct) | right side (6.1) |
|---|---|---|
| number of terms | infinite, **conditionally** convergent | $\lfloor\mu t\rfloor+1$, finite |
| where $\Phi$ is evaluated | **outside** $[-1,1]$, at $mt$ up to $\infty$ | **inside** $[-1,1]$ |
| cost of one evaluation | $O(c\,m\,t)$ spherical Bessel values (Miller recurrence) | $O(c)$ Legendre values |
| at $\mu=5$, $t=3$ | unbounded | **16 terms** |

$M=\lfloor\mu t\rfloor$ — *not* $\lfloor ct\rfloor$ — because $c=2\pi\mu$ and the
$2\pi$ cancels. **The cost was never intrinsic; it was on the wrong side of a
Poisson summation.** The price paid instead is arithmetic: both terms of (6.1) are
of size $t|\Phi(0)|$ and cancel down to $O(|\Phi(1)|)$, so $10^{3}$–$10^{8}$ of
cancellation over the range computed, which arbitrary precision absorbs and §7
reports in a column rather than assuming.

**Two structural facts (6.1) makes visible, neither used in the proof.**

- **$G$ is discontinuous, and (6.1) says where.** $G$ jumps by $\pi a_1/t$ exactly
  when $\mu t$ crosses an integer — on the left because the sawtooth
  $\frac{\pi-\gamma}{2}$ jumps by $\pi$ at $\gamma=0$, on the right because the
  endpoint samples $\Phi(\pm1)$ enter the finite sum. Two descriptions of one
  discontinuity, and a cheap consistency test between the two sides.
- **(P) is a quadrature statement.** Since $\int_{-1}^1\Phi=\mu_\Phi\Phi(0)$ is (F)
  at $x=0$, (6.1) says
  $$t\,G(t)=\frac{1}{2\mu\,\mu_\Phi}\Big[\sideset{}{'}\sum_{|k|\le M}\Phi(kh)
  -\frac1h\int_{-1}^{1}\Phi\Big],$$
  i.e. **(P) is exactly the statement that the trapezoid-rule error for
  $\int_{-1}^1\Phi$ at step $h<2\pi/c$ is $O\big(\sqrt c\,K\,|\Phi(1)|\big)$,
  uniformly in $h$.** Recorded as a third face of the same object; the Euler–Maclaurin
  route to it was tried and is *worse*, because its kernel $B_1(\{y/h\})$ has to be
  paired with $\int_{-1}^1|\Phi'|$, which is $O(c^{1/4})$ in absolute terms and
  therefore $e^{+\Theta(c)}$ times too large relative to $|\Phi(1)|$. The off-band
  route of §§3–5 is the one that keeps everything proportional to $|\Phi(1)|$.

---

## 7. Numerics — *what was measured, and what it can and cannot do*

`verify_q2.py`. **These checks cannot prove Theorem 5.1 and are not offered as
doing so**: the theorem quantifies over all $t>1$, all $x\ge1$ and all $c$, and a
grid reaches none of them. What they can do is *falsify* — every inequality of
§§3–5 is checked where an algebra slip would show — and *calibrate*. Arbitrary
precision throughout (150 digits; CHECK 1 and CHECK 4 at 120, CHECK 2 at 100), no
floating point.

**The defect found in the shared apparatus, reported first because it is the one
thing here that touches other notes.** `verify_h1.sph_j_all` computes spherical
Bessel values by Miller downward recurrence and normalises on the sum rule
$\sum_k(2k+1)j_k^2=1$; its docstring explains, correctly and at length, why
normalising on $j_0(z)=\sin z/z$ is wrong, because $z=cx$ sits at a multiple of $\pi$
exactly when $x$ is an integer. **It then fixes the remaining global sign by
`(out[0]*scale)*(sin(z)/z) < 0` — the same ill-conditioned quantity, in the same
place.** Measured at $c=6\pi$, prolate index 4:

| $x$ | $\Phi(x)$, as returned by `verify_h1` | $\sin(cx)$ |
|---|---|---|
| $199.9999$ | $-1.3735\times10^{-8}$ | $-1.885\times10^{-3}$ |
| $200$ | $\mathbf{+1.2812\times10^{-8}}$ | $9.8\times10^{-119}$ |
| $200.0001$ | $-1.1889\times10^{-8}$ | $+1.885\times10^{-3}$ |

The sign at $x=200$ is decided by rounding noise. `verify_q2.py` carries a fixed
copy: the sign is set by the two-term inner product against the closed forms
$j_0=\sin z/z$ and $j_1=\sin z/z^2-\cos z/z$, which is unconditionally well
conditioned since $\max(|\sin z|,|\cos z|)\ge2^{-1/2}$. Cross-checked: the two agree
to **0 ulp at every index** for generic $z$ ($37.3$, $412.77$, $1234.5$), so the
change is a sign fix and nothing else.

> **It invalidates nothing already published in this corpus.** Every number
> `h1-mean-value.md` and `band-edge-connection.md` report from that routine is a
> **modulus** — $\sup|\Phi|$, $\sup x|\Phi|$, $A=\rho D^{1/4}$, relative agreements —
> and a global sign flip is invisible in a modulus. That is also why it survived two
> notes' worth of checking. It is fatal *here* because §4 subtracts the explicit
> leading term $a_1\sin(cx)/x$ from $\Phi$, and a flipped sign converts a remainder
> of size $x^{-2}$ into one of size $x^{-1}$ — which is precisely the difference
> between (P) and its negation. Both notes are annotated.

**CHECK 0 — the Poisson identity (6.1), against direct off-band summation.** Two
computations sharing no code below `prolate_even`: (6.1) uses only Legendre values
inside $[-1,1]$; the direct route uses only spherical-Bessel values outside it, with
the first three asymptotic terms of §2 summed in closed form (Bernoulli polynomials:
$\sum\frac{\sin m\gamma}{m}$, $\sum\frac{\cos m\gamma}{m^2}$,
$\sum\frac{\sin m\gamma}{m^3}$) so that the truncation is $O(N^{-3})$ rather than
$O(1)$. A disagreement refutes (6.1). Observed relative difference at $N=60$:
$10^{-5}$ to $10^{-9}$, falling like $N^{-3}$ ($3.7\times10^{-4}$, $6.1\times10^{-5}$,
$1.8\times10^{-6}$ at $N=10,20,40$), against cancellation of $10^{1}$–$10^{13}$
reported in its own column.

> **This check found something, and it is a feature of $G$ rather than a defect in
> either route.** At $c=10\pi$, $t=2.6$ one has $\mu t=13$ — a **resonance**, where
> $G$ jumps. The first draft of the direct route read
> $\gamma=ct\bmod2\pi$ as $\approx10^{-148}$ rather than $0$ and so returned the
> *one-sided* limit $\sum_m m^{-1}\sin m\gamma=\frac{\pi-\gamma}2\to\frac\pi2$, where
> the truth at $\gamma=0$ is $0$ — every term $\sin(cmt)$ vanishes identically there.
> The two routes then disagreed by exactly half a jump, and the three affected rows
> reported relative differences of $24$, $2.9$ and $2.2$ while every other row agreed
> to $10^{-6}$. Detecting the resonance on $\mu t$ — the same test (6.1) already
> makes for its prime — fixes it, and those rows now agree to $3\times10^{-5}$.

**CHECK 0b — the jump itself, straddling $\mu t=13$ at $c=10\pi$, index 4:**

| $t$ | $t\,G(t)$ |
|---|---|
| $2.5999999$ | $-2.98208\times10^{-9}$ |
| $2.6$ (resonance) | $-1.04105\times10^{-9}$ |
| $2.6000001$ | $+9.00037\times10^{-10}$ |

The half-jump is $1.94106\times10^{-9}$ against $\frac\pi2|a_1|=1.94109\times10^{-9}$,
and the value at the resonance is the mid-value of the two one-sided limits to
$2\times10^{-5}$. **Both predictions of §6 confirmed**: the jump size $\pi a_1/t$,
and the Dirichlet–Jordan mid-value convention that (6.1)'s prime encodes.

**CHECK 1 — $\alpha_\infty=a_1$ and $\beta_\infty=0$ (Lemma 3.3).** $(\alpha,\beta)$
extracted from $(u,u')$ at $x=20,200,2000$, three bandwidths and three indices. What
is being tested is the one line the theorem cannot survive without: the *absence* of
the cosine.

**CHECK 2 — the two remainder bounds (Prop. 4.1).** Worst ratio of the actual
quantity to its proved bound over $1\le x\le40$, step $\pi/(6c)$, which resolves the
oscillation; anything exceeding $1$ refutes the proposition.

**CHECK 3 — the conclusion.** $\sup_{t>1}t|G(t)|/|\Phi(1)|$ against the proved
$K_P(c)$. **$G$ is discontinuous** (§6), jumping by $\pi a_1/t$ whenever $s=\mu t$
crosses an integer, so the supremum is approached *at* the jumps and a uniform grid
in $s$ **systematically misses it**. The grid is $8$ uniform points per unit of $s$
*plus* geometric refinement $10^{-1},\dots,10^{-6}$ inward from each side of every
integer, $s$ running to $40$.

> **A grid artefact of my own, corrected before it was quoted.** A first pass used
> $40$ *uniform* sub-samples per unit and reported $\sup=0.45$, attained near
> $t\approx4$–$7$. That is wrong by a factor of two: with the endpoints refined the
> supremum is $0.94$–$1.05$ and is attained as $t\to1^{+}$. This is the same error
> `band-edge-connection.md` §7 CHECK 3 had to correct in `h1-mean-value.md` §7 — a
> grid that excludes the point where the supremum lives — committed again, one note
> later, in the one variable that note had just shown to matter. Reported rather
> than quietly fixed, and it is why §7 states every grid's endpoints.

**CHECK 4 — the combination, and hypothesis (C).** $|b_m\Phi_{n_m}(1)|$ by mode for
the three-mode vector of `prolate-rate.md` §2.1, and $C=\sum_m|b_m\Phi_{n_m}(1)|/|\phi(1)|$;
$\chi_8/c^2$ is printed alongside because Thm 5.1 needs it $<1$.

### Output

(Table cells below are transcribed from `verify_q2.py`; the script prints more
digits than are reproduced.)

**CHECK 3 — the conclusion, reported first because it is what (P) asserts.** With
the endpoint-refined grid, $s=\mu t$ to $40$:

| $c$ | $n$ | $\sup_{t>1}t|G|/|\Phi(1)|$ | attained at | proved $K_P(c)$ | ratio | $\frac\pi2|a_1|/|\Phi(1)|$ |
|---|---|---|---|---|---|---|
| $12.566$ | 0 | $0.9571$ | $t\to1^+$ | $26.55$ | $27.7$ | $0.3536$ |
| $12.566$ | 2 | $1.0663$ | $t\to1^+$ | $26.55$ | $24.9$ | $0.3536$ |
| $12.566$ | 4 | $1.0343$ | $t\to1^+$ | $26.55$ | $25.7$ | $0.3537$ |
| $18.850$ | 0 | $1.0521$ | $t\to1^+$ | $21.75$ | $20.7$ | $0.2887$ |
| $18.850$ | 2 | $0.9907$ | $t\to1^+$ | $21.75$ | $22.0$ | $0.2887$ |
| $18.850$ | 4 | $0.9505$ | $t\to1^+$ | $21.75$ | $22.9$ | $0.2887$ |
| $31.416$ | 0 | $0.9546$ | $t\to1^+$ | $19.13$ | $20.0$ | $0.2236$ |
| $31.416$ | 2 | $1.0410$ | $t\to1^+$ | $19.13$ | $18.4$ | $0.2236$ |
| $31.416$ | 4 | $1.0052$ | $t\to1^+$ | $19.13$ | $19.0$ | $0.2236$ |
| $50.265$ | 0 | $0.9450$ | $t\to1^+$ | $18.16$ | $19.2$ | $0.1768$ |
| $50.265$ | 2 | $0.9966$ | $t\to1^+$ | $18.16$ | $18.2$ | $0.1768$ |
| $50.265$ | 4 | $1.0497$ | $t\to1^+$ | $18.16$ | $17.3$ | $0.1768$ |

**Every one of the twelve rows is below $K_P(c)$**, by a factor $17.3$ to $27.7$.
Two things about the first column, and the second is the more interesting:

- **It is $1$ to within $\pm7\%$ at every bandwidth and every index, and it does not
  drift with $c$** — where the sawtooth-only prediction in the last column *decays*
  like $c^{-1/2}$. So the supremum is **not** the sawtooth; it is the $t\to1^{+}$
  endpoint, where the very first term of $G$ is $\Phi(t)\to\Phi(1)$ and the rest is
  a small correction. Explicitly, $\sup_{t>1}t|G(t)|\ge\big|\Phi(1)+\sum_{m\ge2}\Phi(m)\big|$,
  and at integer $\mu$ that correction is small because $\sin(cm)=\sin(2\pi\mu m)=0$
  annihilates the leading term of every $m\ge2$. **The true constant in (P) is
  therefore $1$, not $o(1)$**: no $K$ below about $0.94$ can work, so `h1-mean-value.md`
  §4 wrote the statement down in the right shape and the only slack is the factor
  $\approx22$ in the proof. This is the exact analogue of `band-edge-connection.md`
  §7's finding that the truth in Q1 is $1$, attained at $x=1$.
- **The proof's looseness widens with $c$ only through $\log c$**, since the truth is
  flat and $K_P\asymp2^{3/4}\log c$; the bulk of the factor $\approx22$ is the
  $\sqrt c$ thrown away at the band edge (Q1′) plus the split of §5, both of which
  are visible in CHECK 2's second column sitting at $0.003$ of its bound.

Two controls, because "$\approx1$ at integer $\mu$" could be an artefact of the
resonance structure:

- **Off resonance.** At non-integer $\mu=3.37$ and $\mu=5.618$ the supremum is
  $0.565$–$0.801$, attained at $t=1.07$–$4.15$ — still $O(1)$, still far below
  $K_P\approx19$–$21$. The conclusion does not depend on $\mu\in\mathbb Z$; what
  does depend on it is the sharpness, the supremum falling to about $0.8$ off
  resonance.
- **The supremum is real, not a cancellation artefact.** (6.1) at $t=1.0003$ was
  cross-checked against the direct off-band route (CHECK 0's method, $N=80$):
  $4.9098939\times10^{-4}$ vs $4.9098841\times10^{-4}$, agreeing to $2\times10^{-6}$.

**CHECK 1 — the two constants**, at $c=10\pi$, indices $0,2,4$ (the $c=4\pi,6\pi$
rows are the same picture):

| $x$ | $\alpha/a_1-1$ | $\beta/|a_1|$ |
|---|---|---|
| $20$ | $-0.276$ to $-0.158$ | $-0.690$ to $-0.539$ |
| $200$ | $-2.89\times10^{-3}$ to $-1.62\times10^{-3}$ | $-7.60\times10^{-2}$ to $-5.69\times10^{-2}$ |
| $2000$ | $-2.89\times10^{-5}$ to $-1.62\times10^{-5}$ | $-7.61\times10^{-3}$ to $-5.69\times10^{-3}$ |

$\beta\to0$ like $x^{-1}$ and $\alpha\to a_1$ like $x^{-2}$: the first is the rate
(3.3) proves, the second is one power *faster* than proved — the usual gain from the
mean of the oscillation — and is not relied on anywhere. **Lemma 3.3 is confirmed at
three indices and three bandwidths.**

**CHECK 2 — the two remainder bounds**, worst ratio over $1\le x\le40$, step
$\pi/(6c)$:

| $c$ | $\sup x|W|/(B_1|\Phi(1)|)$ | $\sup x^2|W|/(B_2|\Phi(1)|)$ | $B_1$ | $B_2$ |
|---|---|---|---|---|
| $12.566$ | $0.2775$ | $0.00223$–$0.00507$ | $3.604$ | $257.2$ |
| $18.850$ | $0.3573$ | $0.00322$–$0.00548$ | $2.799$ | $297.6$ |
| $31.416$ | $0.4327$ | $0.00390$–$0.00515$ | $2.311$ | $410.4$ |

Both hold everywhere, the first with a factor $2$–$4$ to spare and the second with a
factor $180$–$450$ — the $c^{3/2}$ of §4 made visible. **The grid stops at $x=40$**;
the same argument run from $X=40$ instead of $\sqrt2$ bounds the tail, but that is an
argument and not a measurement, and it is stated so it is not mistaken for one.

**CHECK 4 — the combination:**

| $c$ | $|b_0\Phi_0(1)|$ | $|b_2\Phi_4(1)|$ | $|b_4\Phi_8(1)|$ | $C$ | $\chi_8/c^2$ |
|---|---|---|---|---|---|
| $12.566$ | $4.288\times10^{-5}$ | $9.677\times10^{-2}$ | $2.450\times10^{-3}$ | $1.0529$ | **$1.0402$ — FAILS** |
| $18.850$ | $9.885\times10^{-8}$ | $5.878\times10^{-4}$ | $2.495\times10^{-6}$ | $1.00887$ | $0.780$ |
| $31.416$ | $4.476\times10^{-13}$ | $8.216\times10^{-9}$ | $8.909\times10^{-12}$ | $1.00228$ | $0.5007$ |
| $50.265$ | $3.699\times10^{-21}$ | $1.834\times10^{-16}$ | $6.701\times10^{-20}$ | $1.00077$ | $0.3230$ |

The index-4 term outweighs the other two by $10^{1.6}$ to $10^{5.3}$, **there is no
cancellation at the band edge**, and $C\to1$ as $c$ grows — $1.00077$ at $c=16\pi$.
So hypothesis (C) is comfortable and gets *more* comfortable with $c$, which is what
`h1-mean-value.md` §7's endpoint identity predicts.

> **The $c=4\pi$ row is inside the theorem's blind spot and is reported, not
> rounded away.** $\chi_8/c^2=1.0402>1$ there, so Theorem 5.1 — like
> `band-edge-connection.md` Theorem 5.2, from which it inherits the hypothesis — does
> **not** cover prolate index 8 at $\mu=2$, and the $|b_4\Phi_8(1)|$ entry in that row
> is therefore not covered either. It is covered from $\mu=3$ on. Whether the
> combination uses index 8 at all is `index-convention.md`'s question (mg-9433 put
> the corpus's mode at index 4), and I did not re-open it.

---

## 8. The house rule, applied to this note

> **Is any statement in this note false for $-W_\lambda$?**

| item | under $-W_\lambda$ | verdict |
|---|---|---|
| Lemma 2.1, the two integrations by parts | an identity for $\Phi$ | **sign-blind** |
| Lemma 3.1, the Liouville form | a change of variables in an ODE | **sign-blind** |
| Lemma 3.3, $\beta_\infty=0$ | about the prolate eigenrelation only | **sign-blind** |
| Prop. 4.1, the $x^{-2}$ remainder | a bound on $|W|$, a magnitude | **sign-blind** |
| Thm 5.1, (P) | a bound on $t|G|$, a magnitude | **sign-blind** |
| Prop. 6.1, Poisson on the band | an identity between two sums | **sign-blind** |
| Q1 + Q2 $\Rightarrow$ (P) $\Rightarrow$ H1 $\Rightarrow\limsup\le-4\pi$ | the *upper* bound on $|s|$ becomes an upper bound on $|-s|$ | **sign-blind as a magnitude claim** |

**Every item is sign-blind, and that is the correct answer, not a defect.** This
note contains no zeta function at all. It is a statement about one classical special
function outside its interval, and the reason it bears on the corpus is that
`h1-mean-value.md` §3 discharged the zeta side unconditionally, leaving only that.
`prolate-rate.md` §7, `h1-mean-value.md` §8 and `band-edge-connection.md` §8 locate
the sign elsewhere, and the elsewhere is RH. **Nothing here moves toward it,
including by omission:** if any argument in this direction ever appears to yield a
*lower* bound on $s(\mu)$, it is wrong. §5 states the check explicitly for each
hypothesis of Thm 5.1.

---

## 9. Open — what Q2 does not close

| # | item | status |
|---|---|---|
| **Q1** | $x|\Phi_{n,c}(x)|\le K_1|\Phi_{n,c}(1)|$, $x\ge1$, $\chi_n<c^2$ | **PROVED** (mg-6851), `band-edge-connection.md` Thm 5.2 |
| **Q2** | single term to the sum $G=\sum_{m\ge1}\Phi(m\,\cdot)$ | **PROVED**, §5 Thm 5.1, $K_P(c)=O(\log c)$ |
| **(C)** | $\sum_m|b_m||\Phi_{n_m}(1)|\le C|\phi(1)|$ — needed only for (P)'s *literal* wording, not for what §4 of `h1-mean-value.md` consumes | **observed** ($C=1.0089$ at $c=6\pi$); implied by Q5 |
| **Q2′** | the sharp constant. Proved $K_P\asymp2^{3/4}\log c$; measured $\sup t|G|/|\Phi(1)|=0.94$–$1.05$, flat in $c$, attained as $t\to1^+$ where the first term of $G$ is $\Phi(t)\to\Phi(1)$ — so the truth is $1$ and no $K<0.94$ is admissible. Slack $17$–$28$, of which $\sqrt c$ is Q1′ | **observed only**; *new item, and nothing downstream needs it* |
| **Q3** | the two flagged steps of `h1-mean-value.md` §3: fractional Sobolev for the $\log^3$ weight, and the $\sigma\to\pm\frac12$ edge | **open, routine, poly cost** — unchanged, and **now the only substantive item between here and H1** |
| **Q4** | (H0), $\|g\|^2$ bounded below | **open** — unchanged, untouched, and separate |
| **Q5** | the endpoint identity $\Phi_n(1)^2=c(1-\Lambda_n)(1-\frac{2n+1}{4c}+\dots)$ | **observed only** — unchanged |
| **index 8 at $\mu=2$** | $\chi_8/c^2=1.040$ at $c=4\pi$, so Thm 5.1 (like Thm 5.2) does not cover prolate index 8 at the bottom of the range | **inherited**, not re-opened; `index-convention.md`'s question |

**What this note did not do.** It did not prove H1. **H1 = Q1 + Q2 + Q3**, and this
note closes Q2; Q3 is `h1-mean-value.md`'s own item, described there as
exponent-checked but unwritten, and I have **not** re-verified that note's §3–§4
reduction — I proved the hypothesis (P) it states, in the form it states it. The
honest one-line summary is: *the item that inherited the description "the whole
remaining content" is closed, and what inherits it now is **Q3, which is routine**,
after which the paper's $-4\pi$ upper bound is unconditional modulo H0 alone.*

Anyone quoting this note should quote Theorem 5.1, Corollary 3.4 (why the
eigenrelation is not removable) and Proposition 6.1 (why the sum is cheap) — not a
resolution of H1.

---

## 10. Provenance

**Derived here, marked *ours* at the point of use:** the reading of Q2's difficulty
as an exponent in $x$ rather than a size in $c$, and the consequent refutation of
`h1-mean-value.md` §9's Q2 row (§1); the two-integration-by-parts identity and the
band-edge Taylor data (Lemma 2.1, (2.2)); the Liouville form $u=\sqrt{x^2-1}\,\Phi$
and its potential (Lemma 3.1); the Lagrange system with Q1 as the boundedness input
(Lemma 3.2); $\alpha_\infty=a_1$, $\beta_\infty=0$ and the observation that it is a
quantisation condition rather than an ODE fact, with Corollary 3.4 showing (P) fails
without it (Lemma 3.3); the $x^{-2}$ remainder bound (Prop. 4.1); Theorem 5.1 and its
constant; Corollary 5.2 and hypothesis (C); Proposition 6.1 and the reading of (P) as
a trapezoid-rule error (§6); the sign defect in `verify_h1.sph_j_all` and its fix
(§7).

**Taken from our own notes, used, not re-derived:** Q1, i.e.
`band-edge-connection.md` Theorem 5.2 with $K_1(c)=2^{3/4}e^{E(c)}$ — used in Lemma
3.2 and Prop. 4.1, and it is the only non-elementary input to this note; Lemma 5.1 of
`h1-mean-value.md` §5 (quoted in Lemma 3.2 only to say it is *not* strong enough);
the reduction of H1 and G5 to (P) and Prop. 4.1 of `h1-mean-value.md` §4 — **quoted,
not re-verified**; the statement of Q1–Q5; the three-mode combination and its weights
(`prolate-rate.md` §2.1); $\Lambda_n=\frac c{2\pi}\mu_\Phi^2$ and the prolate
apparatus (`verify_prolate_rate.py`, validated there against Slepian's tabulated
$\Lambda_0(1)=0.57258$); the entire extension (`verify_h1.py`, with the sign fix of
§7).

**Classical, quoted and used, not re-derived:** Poisson summation for functions of
bounded variation, in the Dirichlet–Jordan form (Prop. 6.1); the Riemann–Lebesgue
lemma (Lemma 2.1); Dirichlet's test and the closed forms
$\sum m^{-1}\sin m\gamma=\frac{\pi-\gamma}2$,
$\sum m^{-1}\cos m\gamma=-\log|2\sin\frac\gamma2|$,
$\sum m^{-2}\cos m\gamma$ and $\sum m^{-3}\sin m\gamma$ as Bernoulli polynomials;
the Lagrange/variation-of-parameters system for $y''+k^2y=0$; the Liouville
transformation; Frobenius exponents $0,0$ at $x=1$ (used only in a parenthesis
in §2).

**Named for orientation, NOT opened and NOT relied on:** Osipov–Rokhlin,
arXiv:1208.4816 — its `lem_psi_for_large_x` has the same leading coefficient $a_1$
as (2.1), and §2 derives that coefficient rather than borrowing it, precisely so that
nothing here rests on hypotheses I have not checked. I did **not** re-open the
source; `h1-mean-value.md` §6 read it and this note quotes that note, not the paper.
Olver's error bounds for the Liouville–Green approximation are the classical home of
§3's technique; not opened, not needed, the argument being self-contained.

**The claim here that would do the most damage if wrong** is **Lemma 3.3's
$\beta_\infty=0$**, because Corollary 3.4 shows (P) is *false* without it — it is not
a constant that could be repaired but the difference between a theorem and its
negation. Its exposure is two lines: the Riemann–Lebesgue step in Lemma 2.1, and the
elimination along $cx\in\frac\pi2+2\pi\mathbb Z$ and $cx\in2\pi\mathbb Z$. Both are
elementary, and the conclusion is checked numerically at three indices and three
bandwidths in §7 CHECK 1, where $\beta/|a_1|$ falls like $x^{-1}$ through
$4.5\times10^{-3}$ at $x=2000$. The second-most damaging would be Prop. 6.1, since
every number in §7 CHECK 3 comes through it; it is cross-checked against a wholly
independent off-band evaluation in CHECK 0, agreeing to $10^{-6}$–$10^{-8}$ across
$10^{3}$–$10^{8}$ of cancellation.

---

## 11. Effect on `h1-mean-value.md`, `band-edge-connection.md` and the paper

`h1-mean-value.md` is annotated in place at §4 and at §9's Q2 row (line-count
preserving), plus one appended section pointing here. `band-edge-connection.md` is
annotated at §9's Q2 row plus one appended section. Neither note's conditional
statements are rewritten and both remain correct as written. `prolate-rate.md` is
**not** edited: its §6(b)'s own log-divergence remark — *"$\widehat\phi$ decays only
like $y^{-1}$ off-band, and $\sum_{n\ge1}$ of the Cauchy–Schwarz bounds is
logarithmically divergent before the oscillation of $\widehat\phi$ is used"* — is the
same obstruction as Q2 and is now removed by Theorem 5.1, but its conditional
statement $\|r\|^2=C_1(\lambda)(1-\chi_2)$ stands as written and rewriting it is
`h1-mean-value.md` §4's business, not this note's.

The paper is **not** edited — vision amendments 11 §5 and 12 §5 batch paper edits,
and six items are pending. What this note adds to that batch:

9. **Q2 is proved**, with $K_P(c)=O(\log c)$ and the hypotheses of Thm 5.1. The gap
   list's H1 entry, once rewritten as Q1–Q5, should carry **Q1 and Q2 as closed** and
   **Q3 as the only substantive item left**, with H0 separate.
10. **"the sum of the remainders in Osipov–Rokhlin's expansion" should go** wherever
   it appears as a description of what Q2 needs. It names the wrong variable; the
   correct one-line description is *one more power of $x$ in the off-band remainder,
   which follows from Q1 by variation of parameters*.
11. **Corollary 3.4 belongs in the body if Q2 does.** (P) is false for a general
   solution of the prolate equation and true for the eigenfunctions; a statement of
   Q2 that does not say so invites exactly the ODE-only proof attempt that cannot
   work.
12. **`prolate-rate.md` §6(b)'s $C_1=O(\log\mu)$ conjecture is now a consequence**,
   not a conjecture, to the same extent that H1 is — i.e. modulo Q3.

None of these touches G10, Theorem `thm:boundary`, or anything about the sign.
