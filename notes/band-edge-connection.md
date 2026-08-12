# Q1 is proved, and the band-edge connection is not what stood in the way

Work item mg-6851. Companion script: [`verify_q1.py`](verify_q1.py) (needs `mpmath`;
no `numpy`; imports the prolate apparatus of [`verify_prolate_rate.py`](verify_prolate_rate.py)
and the entire-extension apparatus of [`verify_h1.py`](verify_h1.py)).
Answers item **Q1** of [`h1-mean-value.md`](h1-mean-value.md) §9, the item that note
calls "the whole remaining content".

Nothing in `start.tex`, `s3.tex` or the paper was edited. `h1-mean-value.md` is
annotated in place, line-count-preserving, plus one appended section.

**Calibration, before anything else.** Q1 is a bound on $|\Phi_n|$, a magnitude. It
is one input to (P), which is one input to H1, which if proved turns
`prolate-rate.md`'s and the paper's **conditional** upper bound
$\limsup\mu^{-1}\log s(\mu)\le-4\pi$ into an **unconditional** one. That is an
improvement to a result the project already has, and it is **not progress toward
RH**. The matching lower bound is not open — it *is* RH (`rhready.tex:1145`, paper
Thm `thm:boundary`, gap **G10**). §8 applies the house rule: every statement below
is sign-blind, which is correct here rather than a defect.

---

## Bottom line

**1. Q1 is proved, with $K$ bounded — not merely subexponential.** For every real
solution $\Phi$ of the prolate equation that is analytic at $x=1$, every $c>\sqrt2$
and every $\chi$ with $0\le\chi<c^2$ (and $\chi_n\ge n(n+1)\ge0$ always, so the
lower bound costs nothing),
$$x\,|\Phi(x)|\;\le\;K(c)\,|\Phi(1)|\qquad(x\ge1),\qquad
K(c)=2^{3/4}\exp E(c),$$
$$E(c)=\frac{5\sqrt2}{c-\sqrt2}+\frac{\sqrt2\,c/3+2}{(c-\sqrt2)^2}.$$
$K$ depends on $c$ alone — **not on $n$**, beyond the hypothesis $0\le\chi_n<c^2$ — and
$K(c)$ decreases to $2^{3/4}=1.6818\dots$ as $c\to\infty$. At the bandwidths this
project computes, $K=3.379$ at $c=4\pi$ and $K=1.965$ at $c=16\pi$. §5.

*One cell of the hypothesis fails and is reported rather than rounded away:*
**$\chi_8/c^2=1.040$ at $c=4\pi$**, so the theorem does not cover prolate index 8
at $\mu=2$. It covers index 8 from $\mu=3$ on and indices $0,2,4,6$ throughout.
Whether that matters is `index-convention.md`'s question — mg-9433 put the corpus's
mode at index 4 — and I did not re-open it. §5, §7.

**2. The obstruction the ticket and the previous note both name is not real.**
`h1-mean-value.md` §5 and vision amendment 11 §4 both say the missing step is a
**connection through the regular singular point $x=1$**. It is not. The factor $x$
is only *needed* where $x$ is large; on $1\le x\le\sqrt2$ the inequality
$x|\Phi(x)|\le\sqrt2|\Phi(1)|$ is Lemma 5.1 and nothing else. So the WKB argument
may be *started* at $x=\sqrt2$, where Lemma 5.1 supplies the initial amplitude, and
the singular point is never crossed. **The connection problem was an artefact of
insisting on a single argument valid on all of $[1,\infty)$.** §6.

**3. What makes the argument close is exactly the regime hypothesis, in a form
that had not been used.** In the amplitude–phase variables the phase speed is
$$k(x)^2=\frac{c^2x^2-\chi}{x^2-1}=c^2+\frac{c^2-\chi}{x^2-1}\;>\;c^2 ,$$
so $\chi<c^2$ says precisely: **$q=c^2x^2-\chi$ has no zero on $[1,\infty)$ — there
is no turning point outside the band — and the phase advances at rate at least $c$
everywhere.** That uniform lower bound is what makes the one oscillatory integral in
the proof $O(1/c)$ instead of divergent. In the published regime $\chi>c^2$ there
*is* a turning point, at $x=\sqrt\chi/c>1$; that is the structural reason
Osipov–Rokhlin's analysis is different from ours and cannot be borrowed
(`h1-mean-value.md` §6), and it is the same fact from the other side. §3.

**4. The mean of the amplitude equation cancels exactly; only an oscillation is
left.** With $D=(x^2-1)(c^2x^2-\chi)$ and $\rho^2=V$ the Sturm amplitude of Lemma
5.1, the WKB invariant $A:=\rho D^{1/4}$ satisfies the *exact* identity
$$\frac{A'}{A}\;=\;-\,\frac{D'}{4D}\,\cos2\theta .$$
`h1-mean-value.md` §5 reaches this point and calls the right-hand side
"sign-indefinite, vanishing only on average over an oscillation". It does vanish on
average, and one integration by parts against $\theta'\ge c-\sqrt2$ converts that
average into a bound: $|\int_{\sqrt2}^X \frac{D'}{4D}\cos2\theta|\le E(c)$ for every
$X$. §4.

**5. The constant is honest but not sharp, and what the connection at $x=1$ is
actually for is the sharp constant.** The truth is $\sup_{x\ge1}x|\Phi(x)|/|\Phi(1)|
=1$, attained at $x=1$; the proof gives $1.86$ to $3.38$ over $\mu=2$ to $12$. More
interestingly, for $x$ bounded away from the edge the truth is
$\sqrt{2/(\pi c)}$ — it *decays* in $c$ — while the proof gives $O(1)$, because it
buys its starting amplitude from Lemma 5.1 and thereby throws away a factor
$\sqrt c$. Recovering that factor **does** require the band-edge connection, which
is Bessel of order zero: in the Liouville variable the equation near $x=1$ is
$y''+4(c^2-\chi)e^{2\xi}y=0$ and $\Phi$ is the $J_0$ branch. Measured,
$A/|\Phi(1)|\to\sqrt{2/\pi}=0.797885$, $c$-free and $n$-free, and that is exactly the
constant in Osipov–Rokhlin's off-band leading term — an independent confirmation of
both. **Observed, not proved**, and recorded as item Q1′ of §9. §6, §7.

**6. Which outcome of the ticket is this?** Outcome **(1)**, proved, with the
ticket's own premise about the obstruction refuted along the way. The hypotheses are
$\chi<c^2$, $c>\sqrt2$, $\Phi$ real and analytic at $x=1$ — no zeta zeros, no sign,
no numerics. **It is not a proof of H1**, which still needs Q2 (single term to the
sum), Q3 and Q4; what it does is remove the item that the previous note called the
whole remaining content, leaving the sum, which is an engineering problem, and H0,
which is untouched. §9.

---

## 0. Conventions, and what is being assumed

$\Phi_n=\Phi_{n,c}$ is the prolate function $\mathit{PS}_{n,0}$ at bandwidth
$c=2\pi\mu$, normalised by $\int_{-1}^1\Phi_n^2=1$ and extended to the entire
function it is; $\chi_n$ is the eigenvalue of the prolate differential operator and
$\Lambda_n$ the Slepian concentration eigenvalue. These are `h1-mean-value.md` §0's
conventions unchanged, including its warnings about the collisions with
Connes–Consani's and Osipov–Rokhlin's labels.

Everything below is about the **differential equation**
$$\big((1-x^2)\Phi'\big)'+(\chi-c^2x^2)\Phi=0 \tag{0.1}$$
on $x>1$, and about it alone. The only facts used about $\Phi_n$ are that it solves
(0.1), that it is real on the real axis, and that it is analytic at $x=1$. The
theorem is therefore about a two-parameter family of ODEs and holds for *any*
solution with those properties — the eigenvalue condition that singles out $\Phi_n$
from the solution space is never used. This is worth saying because it is also the
limit of the result: **nothing here knows that $\Phi_n$ is a prolate function**, and
in particular nothing here can see $\Lambda_n$, so the proof cannot produce the
$c^{-1/2}$ that §6 shows is the truth.

---

## 1. What Q1 asks, and the shape of the gap it sits in

`h1-mean-value.md` reduces H1 (and the paper's gap **G5**) to
> **(P)** $\displaystyle\sup_{t>1}\,t\,|G(t)|\le K(c)\,|\Phi(1)|$ with $K$
> subexponential in $c$, where $G(t)=\sum_{n\ge1}\Phi(nt)$,

and then splits (P) into two open items: **Q1**, the single-term bound
$x|\Phi_{n,c}(x)|\le K|\Phi_{n,c}(1)|$, and **Q2**, the passage from one term to the
sum. This note does Q1 and does not touch Q2.

Its §5 proves the **amplitude** half of Q1 by a Sturm argument:

> **Lemma 5.1** (`h1-mean-value.md` §5, *proved there*, quoted here). *If
> $\chi<c^2$ then $|\Phi(x)|\le|\Phi(1)|$ for all $x\ge1$.*

The proof puts $p:=(x^2-1)\Phi'$, $q:=c^2x^2-\chi$, $D:=(x^2-1)q$ and shows
$V:=p^2/D+\Phi^2$ has $V'=-p^2D'/D^2\le0$ with $V(1^+)=\Phi(1)^2$. I have checked
that derivation line by line and it is correct; §2 below re-uses its variables
verbatim, and I re-record the one inequality it needs, since it is used again:
$$D'=2x\big(2c^2x^2-\chi-c^2\big)>0\ \text{ on }[1,\infty),
\qquad\text{because } 2c^2x^2-\chi-c^2\ge c^2-\chi>0 . \tag{1.1}$$

What is missing is the factor $x$. That is the whole of Q1.

---

## 2. The amplitude–phase system, exactly — *ours (classical technique)*

Throughout §§2–5 fix $c>\sqrt2$ and $0\le\chi<c^2$, and let $\Phi\not\equiv0$ be a real
solution of (0.1) on $(1,\infty)$, analytic at $x=1$. On $x>1$ equation (0.1) is the
first-order system
$$\Phi'=\frac{p}{x^2-1},\qquad p'=-q\,\Phi , \tag{2.1}$$
with $q=c^2x^2-\chi>0$ and $D=(x^2-1)q>0$ (positivity of $q$ on $[1,\infty)$ is
$\chi<c^2$; it is the same fact as (1.1)).

**$V$ is strictly positive.** If $V(x_0)=0$ at some $x_0>1$ then
$\Phi(x_0)=p(x_0)=0$, hence $\Phi'(x_0)=0$, hence $\Phi\equiv0$ by uniqueness at the
regular point $x_0$. So $V>0$ on $(1,\infty)$, and since $V\le V(1^+)=\Phi(1)^2$ by
Lemma 5.1, **$\Phi(1)\ne0$** — the statement of Q1 is not vacuous, and this needs no
input about prolate functions.

**The transformation.** Put $\rho:=\sqrt V>0$ (which is $C^1$, as $V$ is $C^1$ and
positive) and choose a continuous branch $\theta$ with
$$\Phi=\rho\sin\theta,\qquad \frac{p}{\sqrt D}=\rho\cos\theta , \tag{2.2}$$
which is possible because $\Phi^2+p^2/D=\rho^2$. Write
$$k:=\sqrt{\frac{q}{x^2-1}}\;\;\Big(=\frac{\sqrt D}{x^2-1}=\frac{q}{\sqrt D}\Big),
\qquad f:=\frac{D'}{4D}\;(>0\text{ by }(1.1)). \tag{2.3}$$

**Lemma 2.1 (ours; the modified Prüfer system).** *On $(1,\infty)$,*
$$\frac{\rho'}{\rho}=-f\,(1+\cos2\theta),\qquad
\theta'=k+f\,\sin2\theta . \tag{2.4}$$

*Proof.* Differentiate the two equations (2.2) and use (2.1). From the first,
$\rho'\sin\theta+\rho\theta'\cos\theta=\Phi'=\frac{\sqrt D}{x^2-1}\rho\cos\theta
=k\rho\cos\theta$. From the second, after dividing by $\sqrt D$,
$\rho'\cos\theta-\rho\theta'\sin\theta
=\frac{p'}{\sqrt D}-\frac{(\sqrt D)'}{\sqrt D}\rho\cos\theta
=-\frac{q}{\sqrt D}\rho\sin\theta-2f\rho\cos\theta
=-k\rho\sin\theta-2f\rho\cos\theta$, using $(\sqrt D)'/\sqrt D=D'/(2D)=2f$.
Multiply the first by $\sin\theta$ and the second by $\cos\theta$ and add:
$\rho'=-2f\rho\cos^2\theta=-f\rho(1+\cos2\theta)$. Multiply the first by
$\cos\theta$ and the second by $-\sin\theta$ and add:
$\rho\theta'=k\rho+2f\rho\sin\theta\cos\theta=\rho(k+f\sin2\theta)$. ∎

*(The first half of (2.4) is Lemma 5.1 again: $\rho'\le0$ because $1+\cos2\theta\ge0$
and $f>0$. Nothing new yet.)*

**Corollary 2.2 (ours; the WKB invariant).** *Let $A:=\rho\,D^{1/4}$. Then*
$$\frac{A'}{A}=\frac{\rho'}{\rho}+\frac{D'}{4D}=-f\,(1+\cos2\theta)+f
=-f\cos2\theta . \tag{2.5}$$

This is the exact content of `h1-mean-value.md` §5's remark that "the invariant that
is *actually* constant is $\sqrt D\,V$" — indeed $\sqrt D\,V=A^2$ and (2.5) is that
note's displayed identity divided by $2A^2$. **The mean of $f$ has cancelled
identically.** What is left is a pure oscillation, and $\int f$ alone would diverge
logarithmically, so the cancellation is not a convenience: it is the whole
mechanism.

---

## 3. Where $\chi<c^2$ enters: no turning point, and a phase speed of at least $c$

**Lemma 3.1 (ours; trivial but load-bearing).** *For all $x>1$,*
$$k(x)^2=\frac{c^2x^2-\chi}{x^2-1}=c^2+\frac{c^2-\chi}{x^2-1}\;>\;c^2 ,$$
*so $k>c$ on $(1,\infty)$, with $k\downarrow c$ as $x\to\infty$.*

*Proof.* $\dfrac{c^2x^2-\chi}{x^2-1}-c^2=\dfrac{c^2x^2-\chi-c^2x^2+c^2}{x^2-1}
=\dfrac{c^2-\chi}{x^2-1}>0$. ∎

Two readings, and the second is the one that matters.

- $\chi<c^2$ $\iff$ $q(x)=c^2x^2-\chi>0$ for all $x\ge1$ $\iff$ **(0.1) has no
  turning point on $[1,\infty)$**. The solution oscillates from the band edge
  outward with no exponential region anywhere. When $\chi>c^2$ instead, $q$ vanishes
  at $x=\sqrt\chi/c>1$ and there is a turning point *outside* the band; that is why
  the published off-band analysis is a different analysis, and `h1-mean-value.md`
  §6's finding that Osipov–Rokhlin's hypotheses are the negation of ours is this
  fact seen from their side.
- $\theta$ advances at rate at least $c$ minus a correction that §4 shows is at most
  $\sqrt2$. **A uniform lower bound on the phase speed is exactly what an
  integration by parts needs**, and it is available here for free, over the whole
  half-line, with no smallness assumption on $x-1$ and no matching. This is the
  step at which the argument stops being a WKB heuristic.

---

## 4. The oscillatory integral — *ours*

Set $c_-:=c-\sqrt2>0$ and restrict to $x\ge\sqrt2$ for the rest of this section.

**Lemma 4.1 (ours; the four elementary bounds).** *Write $u:=(x^2-1)^{-1}$ and
$v:=c^2/q$, so that $f=\frac x2(u+v)$. Then for $x\ge\sqrt2$*
$$f\le\frac2x,\qquad |f'|\le\frac8{x^2},\qquad |k'|\le\frac{4c}{x^3},
\qquad \theta'\ge k-f\ge c-\frac2x\ge c_->0 .$$

*Proof.* $x\ge\sqrt2$ gives $x^2-1\ge x^2/2$, so $u\le2x^{-2}$; and
$q>c^2(x^2-1)\ge c^2x^2/2$ (Lemma 3.1's computation), so $v\le2x^{-2}$. Hence
$f=\frac x2(u+v)\le\frac x2\cdot\frac4{x^2}=\frac2x$.

$u'=-2xu^2$ and $v'=-2xv^2$ (differentiate; $v=c^2/q$ and $q'=2c^2x$ give
$v'=-2c^2x\cdot c^2/q^2=-2xv^2$), so
$f'=\tfrac12(u+v)-x^2(u^2+v^2)$, a difference of two non-negative terms bounded by
$\tfrac12\cdot4x^{-2}=2x^{-2}$ and $x^2\cdot8x^{-4}=8x^{-2}$ respectively; so
$|f'|\le8x^{-2}$.

$k=\sqrt{c^2+(c^2-\chi)u}$, so $2kk'=(c^2-\chi)u'=-2x(c^2-\chi)u^2$ and
$|k'|=x(c^2-\chi)u^2/k\le xc^2u^2/c=cxu^2\le4c\,x^{-3}$, using $k>c$ and
$0<c^2-\chi\le c^2$. **This last step is the only place $\chi\ge0$ is used, and
it is the only place it is needed**; without it the factor $c^2-\chi$ is
unbounded. For prolate functions $\chi_n\ge n(n+1)\ge0$, so nothing is lost —
but the hypothesis is real and I had first stated the theorem without it.

Finally $\theta'=k+f\sin2\theta\ge k-f>c-2/x\ge c-\sqrt2$. ∎

**Proposition 4.2 (ours).** *For every $X\ge\sqrt2$,*
$$\left|\int_{\sqrt2}^{X} f\,\cos2\theta\;dx\right|\;\le\;E(c)
:=\frac{5\sqrt2}{c_-}+\frac{\sqrt2\,c/3+2}{c_-^{2}} . \tag{4.1}$$

*Proof.* By Lemma 4.1, $\theta'\ge c_->0$ on $[\sqrt2,\infty)$, so
$g:=f/(2\theta')$ is well defined, positive, and $C^1$ there ($f$ is smooth;
$\theta$ is $C^1$, hence $\theta'=k+f\sin2\theta$ is $C^1$). Also
$$0<g\le\frac{2/x}{2c_-}=\frac1{x\,c_-} . \tag{4.2}$$
Since $\cos2\theta=(\sin2\theta)'/(2\theta')$, integration by parts gives
$$\int_{\sqrt2}^{X}f\cos2\theta\,dx=\Big[g\,\sin2\theta\Big]_{\sqrt2}^{X}
-\int_{\sqrt2}^{X}g'\,\sin2\theta\,dx ,$$
so, by (4.2) and $X\ge\sqrt2$,
$$\left|\int_{\sqrt2}^{X}f\cos2\theta\right|\le g(\sqrt2)+g(X)+\int_{\sqrt2}^{\infty}|g'|
\;\le\;\frac{2}{\sqrt2\,c_-}+\int_{\sqrt2}^{\infty}|g'| . \tag{4.3}$$
For $g'$: differentiating $g=f/(2\theta')$ and using
$\theta''=k'+f'\sin2\theta+2f\theta'\cos2\theta$ (differentiate (2.4)),
$$|g'|\le\frac{|f'|}{2\theta'}+\frac{f\,|\theta''|}{2\theta'^2}
\le\frac{|f'|}{2\theta'}+\frac{f\big(|k'|+|f'|\big)}{2\theta'^2}+\frac{f^2}{\theta'} .$$
Insert Lemma 4.1 and $\theta'\ge c_-$:
$$|g'|\;\le\;\frac{4}{c_-x^{2}}+\frac{4c}{c_-^{2}x^{4}}+\frac{8}{c_-^{2}x^{3}}
+\frac{4}{c_-x^{2}}\;=\;\frac{8}{c_-x^{2}}+\frac{8}{c_-^{2}x^{3}}
+\frac{4c}{c_-^{2}x^{4}} .$$
With $\int_{\sqrt2}^\infty x^{-2}=2^{-1/2}$, $\int_{\sqrt2}^\infty x^{-3}=\tfrac14$
and $\int_{\sqrt2}^\infty x^{-4}=\sqrt2/12$,
$$\int_{\sqrt2}^{\infty}|g'|\;\le\;\frac{4\sqrt2}{c_-}+\frac{2}{c_-^{2}}
+\frac{\sqrt2\,c}{3\,c_-^{2}} .$$
Adding the boundary term $2/(\sqrt2c_-)=\sqrt2/c_-$ from (4.3) gives (4.1). ∎

The three sources of the bound are worth separating, because they say what would
have to change to improve it: $4\sqrt2/c_-$ is the variation of the WKB amplitude
ratio, $\sqrt2\,c/(3c_-^2)$ — the only term with a $c$ upstairs, and the one that
does **not** decay faster than $1/c$ — is the variation of the phase speed $k$, and
$\sqrt2/c_-$ is the two endpoints. All three are $O(1/c)$, and none of them is close
to the truth (§7 measures the actual integral at about $E/12$).

---

## 5. The theorem — *ours*

**Theorem 5.2 (Q1).** *Let $c>\sqrt2$ and $0\le\chi<c^2$, and let $\Phi\not\equiv0$
be a real solution of $\big((1-x^2)\Phi'\big)'+(\chi-c^2x^2)\Phi=0$ that is analytic
at $x=1$. Then $\Phi(1)\ne0$ and*
$$x\,|\Phi(x)|\;\le\;K(c)\,|\Phi(1)|\qquad\text{for all }x\ge1,$$
*where $K(c)=2^{3/4}\exp E(c)$ with $E(c)$ as in (4.1). $K$ depends only on $c$;
in particular it is independent of $\chi$ (hence of the index $n$) throughout the
region $0\le\chi<c^2$, and $K(c)\downarrow2^{3/4}=1.68179\dots$ as $c\to\infty$.*

*Proof.* **On $1\le x\le\sqrt2$** there is nothing to do: Lemma 5.1 gives
$|\Phi(x)|\le|\Phi(1)|$, so $x|\Phi(x)|\le\sqrt2|\Phi(1)|\le2^{3/4}e^{E}|\Phi(1)|$,
since $2^{3/4}>\sqrt2$ and $E\ge0$.

**On $X\ge\sqrt2$.** By Corollary 2.2 and Proposition 4.2,
$$A(X)=A(\sqrt2)\exp\left(-\int_{\sqrt2}^{X}f\cos2\theta\right)\le A(\sqrt2)\,e^{E(c)} .$$
Lemma 5.1 bounds the starting amplitude: $\rho(\sqrt2)^2=V(\sqrt2)\le\Phi(1)^2$, and
$D(\sqrt2)=(2-1)(2c^2-\chi)\le2c^2$ (here $\chi\ge0$ is used a second time, though
only for tidiness — any fixed lower bound on $\chi$ would do), so
$$A(\sqrt2)=\rho(\sqrt2)\,D(\sqrt2)^{1/4}\;\le\;2^{1/4}c^{1/2}\,|\Phi(1)| .$$
At the far end, $q>c^2(X^2-1)$ gives $D(X)>c^2(X^2-1)^2$, i.e.
$D(X)^{1/4}>c^{1/2}(X^2-1)^{1/2}$. Since $|\Phi|\le\rho=A\,D^{-1/4}$,
$$X\,|\Phi(X)|\;\le\;\frac{X\,A(X)}{D(X)^{1/4}}
\;\le\;e^{E}\,2^{1/4}c^{1/2}|\Phi(1)|\cdot\frac{X}{c^{1/2}\sqrt{X^2-1}}
\;=\;2^{1/4}e^{E}\,\frac{X}{\sqrt{X^2-1}}\;|\Phi(1)| .$$
$X/\sqrt{X^2-1}$ is decreasing and equals $\sqrt2$ at $X=\sqrt2$, so the right-hand
side is at most $2^{1/4}\cdot\sqrt2\cdot e^{E}|\Phi(1)|=2^{3/4}e^{E}|\Phi(1)|$. ∎

**The constant, evaluated.** $E$ and $K$ at the bandwidths this project uses
($c=2\pi\mu$), computed from the closed forms above:

| $\mu$ | $c$ | $E(c)$ | $K(c)=2^{3/4}e^{E}$ |
|---|---|---|---|
| 2 | $12.5664$ | $0.69777$ | $3.3792$ |
| 3 | $18.8496$ | $0.44137$ | $2.6149$ |
| 5 | $31.4159$ | $0.25436$ | $2.1689$ |
| 8 | $50.2655$ | $0.15551$ | $1.9648$ |
| 12 | $75.3982$ | $0.10243$ | $1.8632$ |
| — | $\to\infty$ | $\to0$ | $\to1.68179$ |

**What the hypotheses do and do not contain.** $\chi<c^2$ (used in Lemma 3.1, (1.1)
and Lemma 4.1), $\chi\ge0$ (used once, for $|k'|$ in Lemma 4.1; free here, since
$\chi_n\ge n(n+1)$ — measured $\chi_n$ from $11.80$ to $816$ over our range, all
positive), $c>\sqrt2$ (used for $c_->0$; our range starts at $c=4\pi$),
$\Phi$ real (the transformation (2.2) is a real one), $\Phi$ analytic at $x=1$ (used
only for $V(1^+)=\Phi(1)^2$ in Lemma 5.1 — boundedness near $x=1$ would do, since by
Frobenius the exponents at $x=1$ are $0,0$ and the second solution carries a
logarithm, for which $p^2/D\to\infty$). **No zeta zeros appear, no sign appears, and
no numerical input appears.** The theorem is quantified over all $x\ge1$, all
$c>\sqrt2$ and all $\chi\in[0,c^2)$, which is what Q1 asks and what no computation
could supply.

**Uniformity in $n$ is real but conditional, and at one corner it fails.** $K$ does
not depend on $\chi$, so the same $K(c)$ serves every index simultaneously — but only
where $\chi_n<c^2$. Since $\chi_n\sim(2n+1)c$ for $n\ll c$, the hypothesis fails for
$n\gtrsim c/2$, and it is **not** automatic at every index this corpus might use.
`h1-mean-value.md` §5 tabulates $n=0,2,4$, all comfortably inside, but its *text*
names the combination $b_0\Phi_0+b_2\Phi_4+b_4\Phi_8$. Measured (§7, CHECK 5):

> **$\chi_8/c^2=1.040$ at $c=4\pi$** — the hypothesis **fails** at index 8 at the
> bottom of this project's range, $\mu=2$. It holds at index 8 for $\mu\ge3$
> ($0.780$ at $c=6\pi$, falling to $0.084$ at $c=200$), and at indices $0,2,4,6$
> throughout.

Whether that matters depends on which indices the combination actually uses, which
is `index-convention.md`'s question and not this note's; mg-9433 settled that the
corpus's $h_{4,\lambda}$ is prolate index **4**, on documentary grounds, which would
put index 8 out of the picture. **I have not re-opened that**, and I record the one
failing cell rather than round it away.

---

## 6. Why the band-edge connection was not needed — and what it *is* needed for

**The ticket's premise, and why it is wrong.** `h1-mean-value.md` §5 ends: "Turning
that average into a bound is a Levinson-type argument that must be connected through
$x=1$, and $x=1$ is a **regular singular point** of the equation. That connection is
the whole of what is missing". Vision amendment 11 §4 repeats it. The Levinson-type
argument is right — §4 is one — but the connection is not needed, for a reason that
is about the *shape of the inequality* rather than about the ODE:

> The factor $x$ that Q1 adds to Lemma 5.1 is worth nothing on a bounded interval.
> On $1\le x\le\sqrt2$, Lemma 5.1 already gives $x|\Phi(x)|\le\sqrt2|\Phi(1)|$. So
> the asymptotic argument only has to run on $[\sqrt2,\infty)$, and its initial data
> at $x=\sqrt2$ is supplied by Lemma 5.1 — which is a statement *at* the band edge
> that has already been propagated outward. **Lemma 5.1 is the connection.**

The cost of routing around the singular point is that Lemma 5.1 gives only
$\rho(\sqrt2)\le|\Phi(1)|$, hence $A(\sqrt2)<2^{1/4}\sqrt c\,|\Phi(1)|$, whereas the
true $A(\sqrt2)$ is about $\sqrt{2/\pi}\,|\Phi(1)|$ (§7, measured) — **a factor
$\asymp\sqrt c$ is thrown away, and it is thrown away at the band edge**. Hence:

**What the connection buys: the $c^{-1/2}$.** In the Liouville variable
$\xi=\int^x\frac{ds}{s^2-1}=\tfrac12\log\frac{x-1}{x+1}\in(-\infty,0)$, equation
(0.1) becomes $d^2\Phi/d\xi^2+D\,\Phi=0$ (this is the transformation that makes
$D=(x^2-1)q$ the momentum and $A=\rho D^{1/4}$ the invariant). As $x\to1^+$,
$x-1\approx2e^{2\xi}$ and $D\to4(c^2-\chi)e^{2\xi}$, so the limiting equation at the
band edge is
$$\frac{d^2y}{d\xi^2}+4(c^2-\chi)e^{2\xi}\,y=0 ,$$
**Bessel's equation of order zero** in exponential form, with solutions
$J_0(z),Y_0(z)$ at $z=2\sqrt{c^2-\chi}\,e^{\xi}=\sqrt{2(x-1)(c^2-\chi)}+O((x-1)^{3/2})$.
$\Phi$ is bounded at $\xi=-\infty$, so it is the $J_0$ branch:
$\Phi\approx\Phi(1)J_0(z)$. In the matching window $c^{-2}\ll x-1\ll1$ one has
$D\approx z^2$ and $J_0(z)\approx\sqrt{2/(\pi z)}\cos(z-\tfrac\pi4)$, whence
$$A=\rho\,D^{1/4}\;\approx\;|\Phi(1)|\sqrt{\tfrac2{\pi z}}\cdot\sqrt z
\;=\;\sqrt{\tfrac2\pi}\;|\Phi(1)| , \tag{6.1}$$
a constant free of $c$, of $n$ and of $z$. Feeding (6.1) into the proof of Theorem
5.2 in place of $A(\sqrt2)<2^{1/4}\sqrt c|\Phi(1)|$ would give
$$x|\Phi(x)|\;\lesssim\;\sqrt{\frac{2}{\pi c}}\;\frac{x}{\sqrt{x^2-1}}\;|\Phi(1)| ,$$
which is $O(c^{-1/2})$, decaying in $c$, and matches Osipov–Rokhlin's leading
off-band term $\Phi_n(x)\approx\frac{2\Phi_n(1)\sin(cx)}{cx\,\mu_\Phi}$ exactly:
with $\mu_\Phi^2=2\pi\Lambda_n/c$ that term has modulus at most
$\frac{2|\Phi_n(1)|}{cx|\mu_\Phi|}=\sqrt{\frac{2}{\pi\Lambda_nc}}\frac{|\Phi_n(1)|}{x}$,
and $\Lambda_n\to1$. Two independent routes to the same constant.

**This is observed, not proved, and it is a separate item.** (6.1) is a matched
asymptotic: it needs a uniform error bound for the $J_0$ approximation on
$c^{-2}\ll x-1\ll1$ and a bound on the drift of $A$ from the matching window out to
$x=\sqrt2$. Neither is written here. §7 measures (6.1) to about $1\%$ at four
bandwidths and three indices; that is evidence and not a proof, and it is filed as
**Q1′** in §9. **Q1 as stated does not need it** — $K=O(1)$ is bounded, hence
subexponential, hence enough for `h1-mean-value.md` Prop. 4.1.

**Classical context, named for orientation and not relied on.** The technique in
§§2–4 is the amplitude–phase (Prüfer/Milne) transformation plus one integration by
parts, and it is the elementary form of the Liouville–Green approximation *with
error bounds* — F. W. J. Olver, "Error bounds for the Liouville–Green (or WKB)
approximation", *Math. Proc. Cambridge Philos. Soc.* (1961), and Ch. 6 of his
*Asymptotics and Special Functions* (1974), where the error is controlled by the
total variation of an error-control function built from $D^{-1/4}$. **I did not open
either**; they are named because a reader should know the proof above is a textbook
technique and not an invention, and the proof is self-contained precisely so that no
statement here depends on a source I have not read. I found no statement of Q1 in
the prolate literature and did not expect to: the natural way to reach it there is
through $\Lambda_n$, which gives the sharp $c^{-1/2}$ and is harder.

**One lead recorded for Q5, not for Q1.** A. Bonami and A. Karoui, "Uniform
approximation and explicit estimates for the prolate spheroidal wave functions",
*Constr. Approx.* (2015), arXiv:1405.3676, states in its abstract "an explicit
approximation of their values at $1$ in terms of the Legendre complete elliptic
integral of the first kind". That is the object of `h1-mean-value.md`'s **Q5** (the
endpoint identity $\Phi_n(1)^2=c(1-\Lambda_n)(1-\frac{2n+1}{4c}+O(c^{-2}))$).
**Abstract only — I did not open the paper**, and the caution of `h1-mean-value.md`
§6 applies in advance: that literature normalises $\psi_n(1)^2\in(\tfrac12,n+\tfrac12)$
in the regime $\chi_n>c^2$, which is not our regime, so the hypotheses must be
checked before anything is borrowed. Recorded as a lead, claimed as nothing.

---

## 7. Numerics — *what was measured, and what it can and cannot do*

`verify_q1.py`. **These checks cannot prove Theorem 5.2 and are not offered as
doing so**: the theorem quantifies over all $x\ge1$ and all $c$, and a grid reaches
neither. What they can do is *falsify* — every inequality in §§2–5 is checked on a
grid, where an algebra slip would show — and *calibrate*, by reporting how far the
proved constant sits above the truth. Arbitrary precision throughout (60 digits;
CHECK 0 at 80), no floating point.

**CHECK 0 — the entire extension, cross-validated.** `verify_h1.py` computes $\Phi$
off $[-1,1]$ from a spherical-Bessel series and pins it at $x=1$ against the
Legendre series. That is one method. Here the ODE (2.1) is integrated outward from
$x=1.2$ by `mpmath.odefun` with initial data from the series, and the two are
compared at $x=1.5,2.5,4,7$. They share no code below `prolate_even`. Agreement:
**relative $10^{-42}$ to $10^{-43}$** at $c=2\pi\cdot2,\,2\pi\cdot3,\,2\pi\cdot5$ and
$n=0,2,4$. This matters because the whole of §7 rests on those off-band values, and
`h1-mean-value.md` §7 records two earlier drafts of that evaluation being silently
wrong by $1.5\%$–$59\%$.

**CHECK 1 — the five inequalities of Lemmas 3.1 and 4.1, plus the $\theta$ equation.**
Reported as the worst ratio of the actual quantity to its claimed bound over
$\sqrt2\le x\le20$; anything exceeding $1$ refutes that line. Also the relative error
in $\theta'=k+f\sin2\theta$ by finite difference on $\operatorname{atan2}(\Phi,p/\sqrt D)$,
an independent test of Lemma 2.1, which comes out at $\approx10^{-4}$ — first order
in the difference step, as it should be.

**CHECK 2 — the oscillatory integral.** Two things: that
$\log(A(X)/A(\sqrt2))=-\int f\cos2\theta$ holds (LHS from the Bessel series, RHS by
Simpson quadrature — an independent test of Corollary 2.2), and
$E_{\mathrm{obs}}:=\sup_X|\int_{\sqrt2}^Xf\cos2\theta|$ against the proved $E(c)$.
$E_{\mathrm{obs}}>E(c)$ would refute Proposition 4.2. **The sup is taken over
$X\le15$, not over all $X$** — the cost of a Bessel array at each of $\sim24c$
points per unit $x$ is what bounds the range, not any belief about the tail; the
tail integrand is $O(x^{-2})$ so it cannot be where a violation hides, but that is
an argument, not a measurement, and the range is stated so it is not mistaken for
one.

**CHECK 3 — the conclusion.** $\sup_{x\ge1}x|\Phi(x)|/|\Phi(1)|$ on a grid refined
geometrically to within $10^{-6}$ of the band edge, against $K(c)$. This corrects a
reporting artefact: `h1-mean-value.md` §7 measured $K_1\le0.79$ on a grid that starts
$0.008$ *above* $x=1$, and the supremum is at $x=1$ itself, where the ratio is $1$ by
definition. The note flags the exclusion ("strictly interior, so the endpoint is not
the answer by construction") and is not wrong, but **$K_1\le0.79$ should not be
quoted as the size of the constant in Q1; the right number is $1$.** The proof gives
$1.86$–$3.38$ over our range, i.e. it is loose by a factor of two to three.

**CHECK 4 — the sharp constant of §6, observed.** $A(x)/|\Phi(1)|$ over
$3\le x\le15$, against $\sqrt{2/\pi}=0.797885$. $A$ is not exactly constant — it
oscillates by $e^{\pm E_{\mathrm{obs}}}$ — so a narrow spread straddling
$\sqrt{2/\pi}$ is what (6.1) predicts, and a single value would be evidence of a bug.

**CHECK 5 — the hypotheses themselves, $0\le\chi_n<c^2$, at $n=0,\dots,8$.** Both
halves. This is the check that found something, so it is reported first below.

### Output

**CHECK 5 first, because it found something.** $\chi_n/c^2$, and $\min_n\chi_n$ for
the $\chi\ge0$ hypothesis:

| $c$ | $\chi_0/c^2$ | $\chi_2/c^2$ | $\chi_4/c^2$ | $\chi_6/c^2$ | $\chi_8/c^2$ | $\min_n\chi_n$ |
|---|---|---|---|---|---|---|
| $12.566$ | $0.0747$ | $0.3724$ | $0.6387$ | $0.8627$ | **$1.040$ — FAILS** | $11.80$ |
| $18.850$ | $0.0509$ | $0.2542$ | $0.4448$ | $0.6210$ | $0.7800$ | $18.09$ |
| $31.416$ | $0.0311$ | $0.1553$ | $0.2751$ | $0.3904$ | $0.5007$ | $30.66$ |
| $50.265$ | $0.0196$ | $0.0980$ | $0.1747$ | $0.2497$ | $0.3229$ | $49.51$ |
| $75.398$ | $0.0131$ | $0.0657$ | $0.1174$ | $0.1685$ | $0.2188$ | $74.65$ |
| $200$ | $0.0050$ | $0.0249$ | $0.0447$ | $0.0645$ | $0.0841$ | $199.2$ |

> **$\chi_8>c^2$ at $c=4\pi$, i.e. at $\mu=2$.** Theorem 5.2 does **not** cover
> prolate index 8 at the bottom of this project's range. It covers it from
> $\mu=3$ on, and covers indices $0,2,4,6$ throughout. This matters only if the
> corpus's combination really involves $\Phi_8$: `h1-mean-value.md` §5's *text*
> names $b_0\Phi_0+b_2\Phi_4+b_4\Phi_8$ while its *table* is at $n=0,2,4$, and
> `index-convention.md` (mg-9433) settled that the corpus's $h_{4,\lambda}$ is
> prolate index **4**, not 8. **I have not resolved which indices the combination
> uses** — that is `index-convention.md`'s question, not this note's — and I record
> the failure rather than assume it away. $\chi_n>0$ at every index and every
> bandwidth, so the second hypothesis is free, as claimed.

**CHECK 0** — Bessel series vs. ODE integration, at $x=1.5,2.5,4,7$ and $n=0,2,4$:
relative difference $2.5\times10^{-43}$ to $2.6\times10^{-41}$ at
$c=2\pi\cdot2,\,2\pi\cdot3,\,2\pi\cdot5$. The off-band values are sound.

**CHECK 1** — worst ratio over $\sqrt2\le x\le20$, step $0.02$ (12 rows, $c=2\pi\mu$
for $\mu=2,3,5,8$ and $n=0,2,4$; ranges over all 12):

| quantity | claimed | worst observed ratio | verdict |
|---|---|---|---|
| $k/c$ | $>1$ | $1.00045$ to $1.00123$ (min) | holds |
| $f\big/(2/x)$ | $\le1$ | $0.8673$ | holds |
| $|f'|\big/(8/x^2)$ | $\le1$ | $0.5530$ | holds |
| $|k'|\big/(4c/x^3)$ | $\le1$ | $0.6967$ | holds |
| $\theta'\big/(c-\sqrt2)$ | $\ge1$ | $1.0290$ (min) | holds |
| $\theta'=k+f\sin2\theta$ | identity | rel. err $3.9\times10^{-5}$–$1.6\times10^{-4}$ | holds (first order in the difference step) |

**CHECK 2** — the oscillatory integral, $\sqrt2\le X\le15$:

| $c$ | $E_{\mathrm{obs}}$ ($n=0,2,4$) | $E(c)$ proved | ratio | identity residual |
|---|---|---|---|---|
| $12.566$ | $0.0478,\,0.0525,\,0.0423$ | $0.6978$ | $\approx14$ | $\le4.3\times10^{-6}$ |
| $18.850$ | $0.0320,\,0.0350,\,0.0323$ | $0.4414$ | $\approx13$ | $\le3.0\times10^{-6}$ |
| $31.416$ | $0.0196,\,0.0205,\,0.0205$ | $0.2544$ | $\approx13$ | $\le1.9\times10^{-6}$ |
| $50.265$ | $0.0124,\,0.0125,\,0.0127$ | $0.1555$ | $\approx12$ | $\le1.2\times10^{-6}$ |

Proposition 4.2 holds everywhere, with about an order of magnitude to spare, and
the ratio is flat in $c$ — so the bound has the right *shape* in $c$ and a loose
constant, not the reverse. The identity residual is Simpson error at step
$\pi/(24c)$ and confirms Corollary 2.2.

**CHECK 3** — the conclusion. The grid is $x-1=10^{-6}$ upward, geometric ratio
$1.15$, then step $\pi/(20c)$ out to $x=15$. **$n$ runs to $8$ at $c=31.4$ and
$50.3$**, where $\chi_8<c^2$, so uniformity in the index is what is being tested:

| $c$ | $\sup_{x>1}x|\Phi|/|\Phi(1)|$ (range over $n$) | attained at | $\sup_{x\ge\sqrt2}$ | proved $K(c)$ |
|---|---|---|---|---|
| $12.566$ ($n\le4$) | $0.99993$–$0.99997$ | $x\to1$ | $0.264$–$0.282$ | $3.3792$ |
| $18.850$ ($n\le4$) | $0.99983$–$0.99990$ | $x\to1$ | $0.216$–$0.227$ | $2.6149$ |
| $31.416$ ($n\le8$) | $0.99952$–$0.99975$ | $x\to1$ | $0.168$–$0.179$ | $2.1689$ |
| $50.265$ ($n\le8$) | $0.99876$–$0.99915$ | $x\to1$ | $0.133$–$0.138$ | $1.9648$ |

Every row is below $K(c)$, by a factor $2.0$ to $3.4$. The supremum is at the band
edge in every one of the 16 rows and the value there is $1$ up to the grid's
$10^{-6}$ offset — the ratio falls just short of $1$ by more at larger $c$ because
$J_0(z)$ has already turned over by $x-1=10^{-6}$ when $c$ is large, which is the
§6 picture and not an artefact. Note how far the two columns are apart: over
$x\ge\sqrt2$, where the WKB half of the proof operates, the true value is $0.13$–$0.28$
and falls like $c^{-1/2}$ (§6), while the proof gives $O(1)$.

**CHECK 4** — the sharp constant, **observed**. $A(x)/|\Phi(1)|$ over $3\le x\le15$:

| $c$ | min over $x,n$ | max over $x,n$ | $\sqrt{2/\pi}$ | the proof's bound $2^{1/4}\sqrt c$ |
|---|---|---|---|---|
| $12.566$ | $0.78735$ | $0.80960$ | $0.797885$ | $4.216$ |
| $18.850$ | $0.79070$ | $0.80519$ | $0.797885$ | $5.163$ |
| $31.416$ | $0.79365$ | $0.80227$ | $0.797885$ | $6.666$ |
| $50.265$ | $0.79522$ | $0.80057$ | $0.797885$ | $8.431$ |

The band straddles $\sqrt{2/\pi}$ at all four bandwidths and all three indices, and
narrows from $\pm1.3\%$ to $\pm0.3\%$ as $c$ grows — which is the predicted
$e^{\pm E_{\mathrm{obs}}}$ oscillation shrinking with $E$. **The last two columns
are the whole of §6:** $A$ is a $c$-free constant near $0.798$, and the proof bounds
it by something growing like $\sqrt c$. That gap is Q1′, and it is $\sqrt c$ wide.

---

## 8. The house rule, applied to this note

> **Is any statement in this note false for $-W_\lambda$?**

| item | under $-W_\lambda$ | verdict |
|---|---|---|
| Lemma 2.1, the Prüfer system | a change of variables in an ODE | **sign-blind** |
| Lemma 3.1, $k>c$ | an inequality between $\chi$ and $c^2$ | **sign-blind** |
| Prop. 4.2, the oscillatory bound | about $|\int f\cos2\theta|$ | **sign-blind** |
| Thm 5.2, Q1 | a bound on $|\Phi|$, a magnitude | **sign-blind** |
| §6, the Bessel connection and $\sqrt{2/\pi}$ | about the ODE at $x=1$ | **sign-blind** |
| Q1 $\Rightarrow$ (P) $\Rightarrow$ H1 $\Rightarrow$ $\limsup\le-4\pi$ | the *upper* bound on $|s|$ becomes an upper bound on $|-s|$ | **sign-blind as a magnitude claim** |

**Every item is sign-blind, and that is the correct answer, not a defect.** This
note contains no zeta function. It is a statement about a two-parameter family of
second-order ODEs, and the reason it bears on the corpus at all is that
`h1-mean-value.md` §3 discharged the zeta side unconditionally, leaving only that
family. `prolate-rate.md` §7 and `h1-mean-value.md` §8 locate the sign elsewhere,
and the elsewhere is RH. **Nothing here moves toward it, including by omission:** if
any argument in this direction ever appears to yield a *lower* bound on $s(\mu)$, it
is wrong.

---

## 9. Open — what Q1 does not close

| # | item | status |
|---|---|---|
| **Q1** | $x|\Phi_{n,c}(x)|\le K|\Phi_{n,c}(1)|$, $x\ge1$, $\chi_n<c^2$, $K$ subexponential | **PROVED**, §5, with $K$ *bounded*: $K(c)=2^{3/4}e^{E(c)}\downarrow2^{3/4}$ |
| **Q1′** | the sharp constant: $A\to\sqrt{2/\pi}|\Phi(1)|$, giving $K=O(c^{-1/2})$ instead of $O(1)$. Needs a uniform error bound for the $J_0$ approximation on $c^{-2}\ll x-1\ll1$ and control of the drift of $A$ out to $x=\sqrt2$ | **observed only** (§6, §7). *New item; not needed for anything currently downstream* |
| **Q2** | single term to the sum $G=\sum_{n\ge1}\Phi(n\,\cdot)$; the sawtooth cancellation, and ~~the remainders in Osipov–Rokhlin's expansion~~ (mg-9d43: not that — one more power of $x$) | **PROVED (mg-9d43), [`dilate-sum.md`](dilate-sum.md) Thm 5.1, $K_P(c)=O(\log c)$. Thm 5.2 above is its only non-elementary input, and §12 records why. Q3 now carries the weight** |
| **Q3** | the two flagged steps of `h1-mean-value.md` §3 (fractional Sobolev for the $\log^3$ weight; the $\sigma\to\pm\frac12$ edge) | **open, routine, poly cost** — unchanged |
| **Q4** | (H0), $\|g\|^2$ bounded below | **open** — unchanged, and untouched by anything in this note |
| **Q5** | the endpoint identity $\Phi_n(1)^2=c(1-\Lambda_n)(1-\frac{2n+1}{4c}+\dots)$ | **observed only** — unchanged; §6 records one unopened lead |

**What this note did not do.** It did not prove H1, or (P), or Q2. It proved one
named lemma that H1 needs. The honest one-line summary is: *the item
`h1-mean-value.md` called "the whole remaining content" is closed, and the item that
inherits that description is Q2, which that note says is blocked on the evaluation <!-- mg-9d43: Q2 is now PROVED, and the "engineering problem" was a Poisson summation away. §12. -->
cost of $\Phi(nt)$ for large $n$ — an engineering problem, not an idea problem.*
Anyone quoting this note should quote Theorem 5.2 and §6's correction of the
obstruction, not a resolution of H1.

---

## 10. Provenance

**Derived here, marked *ours* at the point of use:** the modified Prüfer system
(Lemma 2.1) and the WKB invariant identity (Corollary 2.2) — the latter is
`h1-mean-value.md` §5's own displayed identity in amplitude–phase form, and I say so
there; the phase-speed lower bound and its reading as "no turning point outside the
band" (Lemma 3.1); the four elementary bounds (Lemma 4.1); the integration by parts
and the explicit $E(c)$ (Proposition 4.2); Theorem 5.2 and its constant; the
observation that the connection at $x=1$ is not needed for Q1 and what it *is*
needed for (§6); the Liouville reduction of the band edge to Bessel order zero and
the constant $\sqrt{2/\pi}$ (§6, **observed**); the correction to the reported $K_1$
(§7, CHECK 3).

**Taken from `h1-mean-value.md`, checked line by line, not re-derived:** Lemma 5.1
and its proof, including $D'>0$; the reduction of H1 and G5 to (P) (§4 there); the
statement of Q1–Q5; the reading of Osipov–Rokhlin's hypotheses (§6 there) — I did
not re-open arXiv:1208.4816, and §3 and §6 above quote that note's finding rather
than the source. Its leading off-band form
$\Phi_n(x)\approx2\Phi_n(1)\sin(cx)/(cx\mu_\Phi)$ and
$\mu_\Phi^2=2\pi\Lambda_n/c$ are used in §6 only as a cross-check of a constant I
derived independently, and the agreement is offered as corroboration of both, not as
a citation.

**Classical, named but NOT relied on and NOT opened:** Olver's error bounds for the
Liouville–Green approximation (1961; *Asymptotics and Special Functions* Ch. 6);
Bonami–Karoui arXiv:1405.3676 (abstract only, recorded as a lead for Q5). Nothing in
§§2–5 depends on either; the proof is self-contained by design, because the ticket's
standing instruction is that a reduction to a result whose hypotheses have not been
checked reads as closed and is worse than no reduction.

**Classical, used and standard:** the Prüfer transformation; uniqueness for
second-order linear ODEs at a regular point; Frobenius exponents at a regular
singular point (used only in a parenthesis in §5); $J_0$ asymptotics (§6, in the
observed part only).

**The claim here that would do the most damage if wrong** is Proposition 4.2 — the
bound on the oscillatory integral — because everything else in §5 is arithmetic
around it. Its exposure is Lemma 4.1's four inequalities and the bound on
$|\theta''|$; all five are checked on a grid in CHECK 1, and the conclusion of the
proposition is checked against a directly quadratured integral in CHECK 2, which
also independently confirms Corollary 2.2. The second-most damaging would be the
claim in §6 that the band-edge connection is **not** needed, since it contradicts
two existing documents; that one is not a computation but an observation about which
interval needs which argument, and it is set out explicitly in §6 so it can be
disagreed with directly.

---

## 11. Effect on `h1-mean-value.md`, `prolate-rate.md` and the paper

`h1-mean-value.md` is annotated in place at §5 and at §9's Q1 row (line-count
preserving), plus one appended section pointing here. Its §9 table is otherwise
unchanged and its conditional statements remain correct as written.
`prolate-rate.md` is **not** edited: its §6(c) and §11 already carry mg-8462's
annotations, and Q1 changes nothing there that Q2 does not still gate.

The paper is **not** edited — vision amendment 11 §5 batches paper edits. What this
note adds to that batch:

6. **Q1 is proved.** The gap list's H1 entry, once it is rewritten as Q1–Q5 per
   amendment 11 item 5, should carry Q1 as closed with an explicit bounded constant,
   and Q2 as the item that now carries the weight.
7. **The characterisation "a Bessel-type connection problem at the band edge"
   should go.** It is in amendment 11 §4 and in `h1-mean-value.md` §5 and §9, and it
   is wrong as a description of Q1 — though it is right as a description of Q1′,
   the sharp constant, which is a new and *optional* item.
8. **Lemma 5.1 does more than it was credited with.** It is not only "half of the
   prolate bound": it is also the initial condition that lets the asymptotic
   argument start away from the singular point. If it goes into the paper's body per
   amendment 11 item 4, it should go in with Theorem 5.2 next to it.

None of these touches G10, Theorem `thm:boundary`, or anything about the sign.

---

## 12. Appended by mg-9d43 — Q2 is proved, and Theorem 5.2 is exactly what proved it

*Append-only. Nothing above is rewritten; the in-place annotations are HTML comments
and change no line count. Companion note: [`dilate-sum.md`](dilate-sum.md), script
[`verify_q2.py`](verify_q2.py).*

**Q2 is proved**, `dilate-sum.md` Theorem 5.1: for every even index $n$, every
$c>\sqrt2$ and $0\le\chi_n<c^2$,
$$\sup_{t>1}t\Big|\sum_{m\ge1}\Phi_n(mt)\Big|\le K_P(c)\,|\Phi_n(1)|,\qquad
K_P(c)=O(\log c).$$

**Theorem 5.2 above is the only non-elementary input, and it enters in the one form
this note did not emphasise: it says $u=\sqrt{x^2-1}\,\Phi$ is BOUNDED.** In the
Liouville form $u''+(c^2+\epsilon)u=0$ with $\epsilon=\frac{c^2-\chi+1}{x^2-1}$
integrable at infinity, boundedness of $u$ is exactly what makes the Lagrange
coefficients' derivatives integrable, hence what gives the off-band remainder its
second power of $x$. **Lemma 5.1 alone would not do it** — it gives
$|u|\le\sqrt{x^2-1}\,|\Phi(1)|$, which grows. So the factor $x$ that §6 above called
"worth nothing on a bounded interval" is worth everything on the unbounded one, and
Q1 was not a stepping stone to Q2 but its hypothesis in disguise.

**Q1′ is now quantified downstream, and still not needed.** `dilate-sum.md` §7
measures $\sup_{t>1}t|G|/|\Phi(1)|=0.94$–$1.05$, attained as $t\to1^+$, against the
proved $K_P\approx18$–$27$: a factor $17$–$28$, of which $\sqrt c$ is Q1′ (this note's
§7 CHECK 4) and the rest is the split in `dilate-sum.md` §5. **The truth in Q2 is
$1$** — at $t\to1^+$ the first term of $G$ is $\Phi(t)\to\Phi(1)$, so no constant
below $0.94$ is admissible — which is the exact analogue of this note's §7 CHECK 3 finding that the truth in Q1
is $1$, attained at $x=1$. Recorded so the proved constant is not later mistaken for
a tight one. **Nothing downstream needs it**, which is unchanged.

**And the same grid artefact was committed again, one note later.** §7 CHECK 3 above
corrects `h1-mean-value.md` §7 for measuring on a grid that starts $0.008$ *above*
$x=1$ and so excludes the point where the supremum lives. `dilate-sum.md` §7's first
pass sampled $t$ *uniformly* in $s=\mu t$ and so excluded the jump points where
**its** supremum lives, under-reporting by a factor of two. It is caught and
reported there. Two notes, two grids, the same exclusion — worth naming as a pattern
rather than as two incidents.

**§7's numerics stand, and here is why, because a defect was found in the shared
apparatus.** `verify_h1.sph_j_all` — which this note's CHECK 0, 2, 3 and 4 all use —
normalises on the sum rule but then fixes the remaining **global sign** by
`(out[0]*scale)*(sin(z)/z) < 0`, the very quantity its own docstring explains must
not be used, since $z=cx$ is a multiple of $\pi$ exactly when $x$ is an integer. At
$c=6\pi$, $x=200$ that test compares against $\sin z=10^{-118}$ and returns the wrong
sign. **Every quantity this note reports is a modulus** — $\sup_{x\ge1}x|\Phi|/|\Phi(1)|$,
$A=\rho D^{1/4}$, worst ratios, relative agreements — and a global sign flip is
invisible in a modulus, so CHECK 0–5 above are unaffected. The fixed copy is in
`verify_q2.py`, agreeing with the original to 0 ulp at every index for generic $z$.

**Unchanged:** Theorem 5.2 and its proof; the failing hypothesis cell
$\chi_8/c^2=1.040$ at $c=4\pi$, which `dilate-sum.md` Theorem 5.1 inherits verbatim;
Q1′, Q3, Q4, Q5; every sign-blindness verdict in §8. **H1 is still not proved**:
Q1 and Q2 are the two substantive items and both are now closed, leaving **Q3**,
which `h1-mean-value.md` §9 calls routine and unwritten, and **Q4 (H0)**, which is
separate and untouched.
