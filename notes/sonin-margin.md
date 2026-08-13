# There is no margin of $8.7\times10^{-5}$, and Theorem 1's $\mu\le2$ is an artefact

Work item mg-d03b. Companion script:
[`verify_sonin_margin.py`](verify_sonin_margin.py) (needs `numpy>=2.0`; 5 minutes,
`--quick` 35 s, which is what CI runs). Continues [`sonin-trace.md`](sonin-trace.md) (mg-5210), whose
reduction of Connes–Consani's archimedean theorem this note **re-verifies and keeps**,
and whose central number this note **retires**.

The work item asked three questions about the $8.7\times10^{-5}$ that mg-5210 measured:
what is the near-null direction, what happens to the margin past $\mu=2$, and what do
the two vanishing conditions buy. The first question has no answer because it has no
object; the second and third do, and they are better than the question expected.

---

## Bottom line

**1. $8.7\times10^{-5}$ is not a margin. It is the truncation order, read back out.**
$-E$ is a compact operator — a continuous kernel on a bounded interval — so its
eigenvalues accumulate at $0$ and the smallest eigenvalue of an $N$-term truncation
converges to $0$, not to a margin. Concretely, the kink of $\epsilon$ at $\rho=1$
($\epsilon(1)=0$, $\epsilon'(1^+)=22.9965$, `weil-compo.tex:1367`) forces
$\hat\epsilon(t)\sim-2\epsilon'(1^+)/t^2$, and the smallest eigenvalue resolved by $N$
cosine modes on $[-L/2,L/2]$ is $-\hat\epsilon$ at the truncation frequency
$t=2\pi N/L$:
$$\boxed{\ \min\operatorname{spec}\big({-E}\big|_{\rm codim\ 2}\big)\ \text{at}\ N\ \text{modes}
\ =\ \frac{\epsilon'(1^+)\,L^2}{2\pi^2N^2}\ }$$
All eight rows of `sonin-trace.md` §2.2 are this expression, at $N=40$, $80$ and $160$:
twenty-four cells, worst deviation $0.14\%$. The headline is
$22.996476\,(\log2)^2/(2\pi^2\cdot80^2)=8.7459\times10^{-5}$ against the printed
$8.747916\times10^{-5}$. §2.

**2. And there is no near-null direction.** At $\mu=2$ the minimising vector is the top
resolved cosine mode, with weight $1.000$ on $n=N$ at $N=40$, $80$ and $160$. It moves
when the basis moves. The work item's first question — *is it recognisable, is it
related to the near-null direction of the other form* — is answered by there being
nothing there to recognise. §2.3.

**3. `verify_sonin_trace.conditions()` was computing the wrong second condition**, and
this note fixes it. It evaluated the antiderivative of $\cos(ay)e^{y/2}$ at $y=\pm L$
instead of $y=\pm L/2$, so its $n=0$ entry was $c\cdot4\sinh(L/2)$ where $\hat g(i/2)$
is $c\cdot4\sinh(L/4)$ — wrong by $1.5$ in absolute terms at $\mu=5$. **No output of
that script moved when it was fixed**, because by item 1 the column it feeds is
$\epsilon'(1^+)L^2/2\pi^2N^2$ whichever two conditions are imposed. That is the exact
shape [`statement-defects.md`](statement-defects.md) describes: a discrepancy the
downstream use does not exercise. §3.

**4. What is truncation-stable is the inertia, and it answers the hypothesis.** The
*number* of negative eigenvalues of $-E$ is identical and the eigenvalues agree to
$10^{-3}$ between $N=60$ and $N=120$: they live at low frequency, where the basis is
complete long before the truncation bites. Reading that:

| codimension $k$ | $\mu_c(k)$, $N=60$ | $\mu_c(k)$, $N=120$ |
|---|---|---|
| $0$ | indefinite at every $\mu$ computed | — |
| $1$ — $\hat g(0)=0$ | $2.7680$ | $2.7634$ |
| $2$ — **Theorem 1's** | $6.1928$ | $\mathbf{6.1739}$ |
| $3$ | $13.069$ | $13.011$ |
| $4$ | $26.622$ | $26.461$ |

Each column is an upper bound falling in $N$ — truncation raises a form's eigenvalues —
and they differ by at most $0.6\%$, so three figures is what this supports.
**Theorem 1's conclusion holds to $\mu=6.17$, three times its stated hypothesis
$\mu\le2$. So $\mu\le2$ is an artefact of the proof.** It is not vacuous either: the
conclusion is *false* from $\mu=6.17$ on, and by $\mu=8$ the codimension-two form has a
negative eigenvalue of $-0.0921$, unchanged from $N=60$ to $N=120$. §4.

**5. One of the two conditions is doing all the work at $\mu\le2$.** $\hat g(0)=0$
alone gives $-E\ge0$ up to $\mu=2.763$ — past the whole of Theorem 1's support range.
At $\mu\le2$ the second condition $\hat g(i/2)=0$ buys **nothing** for the sign of $-E$.
This refines mg-5210's "they are not decoration, they are the theorem": one of them is.
§4.

**6. The margin scales understandably with the codimension: each condition buys a
fixed factor in the support.** $\log\mu_c$ is linear in $k$ with measured slope
$0.7523$; $\mu_c(k+1)/\mu_c(k)$ is $2.234$, $2.107$, $2.034$. The mechanism is the symbol:
$\hat\epsilon>0$ only on $|t|<t_0=6.29177$, so $-E$ is negative only on directions whose
$\hat g$ lives in that band, $k$ conditions hold $\hat g$ down near $t=0$ to order $k$,
and a support of length $L$ resolves $t$ only to $2\pi/L$. Equating gives
$\log\mu_c\approx2\pi k/t_0=0.9986\,k$. **The shape is right and the constant is $25\%$
out**, and that is all that is claimed — the geometric growth is measured, the
$2\pi/t_0$ is a count of resolution cells and not a derivation. §5.

**7. Why the conclusion has to fail eventually, which is the one thing that could have
been said without computing anything.** $\epsilon>0$, so
$\hat\epsilon(0)=2\int_0^\infty\epsilon(e^y)\,dy=+5.3722>0$, so the symbol of $-E$ is
*negative* at low frequency. Only a support too short to let $\hat g$ into that band can
save the inequality. Every question in the work item about "what happens past $\mu=2$"
was decided by that one sign. §5.

**8. One tempting coincidence, checked, and it is a coincidence.** $\theta'(t)$ — the
density of $W_\infty$ on the Fourier side — changes sign at $t=6.2898336$, and
$\hat\epsilon$ changes sign at $t_0=6.2917746$. They agree to three digits and no
further: the difference is $1.9\times10^{-3}$ against a $t_0$ stable to $10^{-4}$ under
every setting varied. **They are not the same number.** §5.

---

## 0. Vocabulary and what is inherited

As in [`sonin-trace.md`](sonin-trace.md) §0. What is inherited from mg-5210, and
re-verified here rather than assumed:

- Theorem `devil` (`weil-compo.tex:1132`), $\operatorname{tr}(\vartheta(f)\mathbf
  S)=W_\infty(f)+E(f)$, and therefore that Theorem 1 is exactly "$-E\ge0$ on
  $\{\hat g(0)=\hat g(i/2)=0\}$". **Kept.** Nothing here touches it.
- The $c=2\pi$ prolate apparatus and its five printed anchors. **Kept**; this script
  imports mg-5210's `Prolate` unchanged and CHECK 2 puts its own $\epsilon$ against
  mg-5210's, agreeing to $10^{-11}$ for $\rho\le50$.
- "The gap $-E$ is positive on the codimension-two subspace at every $\mu$ on
  mg-5210's grid." **Kept** — every sign in that table is right.
- "The margin is $8.7\times10^{-5}$, one part in $10^4$." **Retired**, §2.
- "The two conditions move the form from solidly indefinite to barely positive."
  Half kept: indefinite is right (§4), *barely* is not, and *two* is not (§4).

---

## 1. Two things the script had to build, and why

### 1.1 $\epsilon$ at large $\rho$

mg-5210's `epsilon` evaluates $\mathcal F\xi_n$ on a fixed 320-node Gauss rule and the
$x$-integral on a fixed 120-node one. Both stop resolving $\cos(2\pi\rho x)$ somewhere
around $\rho=60$: at $\rho=100$ it returns $2.912$ where the value is $0.09968$.
**Nothing in mg-5210 used $\rho>3$, so no number of its moves** — this is a limit of
that routine, not a defect in it. This note needs $\rho$ up to $60$.

The replacement evaluates $\mathcal F\xi_n$ in closed form. $\xi_n$ is a polynomial on
$[-1,1]$ in the even Legendre basis and $\int_{-1}^1P_k(x)e^{izx}dx=2i^kj_k(z)$, so
$$\mathcal F\xi_n(\omega)=2\sum_kB_{kn}\sqrt{2k+1}\,(-1)^{k/2}j_k(2\pi\omega),$$
with the spherical Bessel functions by Miller downward recurrence. One trap, recorded
because it cost an hour: **normalising Miller's recurrence on $j_0=\sin z/z$ alone
fails** wherever $\sin z$ is near zero, which is every multiple of $\pi$. It was caught
by the identity $\int_{-1}^1P_2(x)\cos(\pi x)dx=-2j_2(\pi)=-6/\pi^2$ coming out $30\%$
wrong — a cheap instrument pointed at the routine, not at its consequences. The script
normalises on whichever of $j_0$, $j_1$ is larger.

### 1.2 The symbol $\hat\epsilon$

$$E(g)=\iint g(u)g(v)\,\epsilon\big(e^{|u-v|}\big)\,du\,dv
=\frac1{2\pi}\int|\hat g(t)|^2\,\hat\epsilon(t)\,dt,\qquad
\hat\epsilon(t)=\int_{\mathbb R}\epsilon(e^{|y|})e^{-ity}dy,$$
so $-\hat\epsilon(t)$ is the Rayleigh quotient of $-E$ on a wave of frequency $t$ in the
long-support limit. **Every structural statement below is read off it.**

Measured: $\epsilon(\rho)\sqrt\rho\to1$ (to $0.5\%$ by $\rho=60$; **ours, unanchored**),
so $\epsilon(e^{|y|})-e^{-|y|/2}$ is integrable and the transform converges.
$\hat\epsilon$ is computed as the transform of that difference plus
$\int_{\mathbb R}e^{-|y|/2}e^{-ity}dy=1/(\tfrac14+t^2)$ exactly. Splicing the asymptotic
on at $y=Y$ instead — the obvious way — leaves a jump of $10^{-2}$ whose transform
decays like $1/t$, and against the $t^2/2$ of §2's tail law that spurious term is $\pm21$
at $t=200$ against a true value of $-23$. The subtraction was not tidiness.

---

## 2. The $8.7\times10^{-5}$

### 2.1 What it is

$\epsilon$ vanishes at $\rho=1$ with $\epsilon'(1^+)=22.996476$, so
$\epsilon(e^{|y|})\approx\epsilon'(1^+)|y|$ near $y=0$, and the Fourier transform of
$|y|$ is $-2/t^2$. Hence
$$\hat\epsilon(t)\ \longrightarrow\ -\frac{2\epsilon'(1^+)}{t^2}\qquad(t\to\infty).$$
Measured: $\hat\epsilon(t)t^2/2$ oscillates about its limit with amplitude $\approx6$
(because $\epsilon$ has structure away from $\rho=1$ too), and its mean over
$t\in[100,300]$ is $-23.0314$ against $-\epsilon'(1^+)=-22.9965$, $0.15\%$.

$\hat\epsilon<0$ for $t>t_0$, so $-E$ is *positive* at high frequency and its spectrum
accumulates at $0$ **from above**. A truncation to $N$ cosine modes on $[-L/2,L/2]$
resolves frequencies up to $t=2\pi N/L$, and the smallest eigenvalue it can see is
therefore
$$-\hat\epsilon\!\left(\frac{2\pi N}{L}\right)=\frac{2\epsilon'(1^+)L^2}{4\pi^2N^2}
=\frac{\epsilon'(1^+)L^2}{2\pi^2N^2}.$$

### 2.2 It reproduces the whole column

`verify_sonin_margin.py` CHECK 1(b), against `sonin-trace.md` §2.2 as printed:

| $\mu$ | printed ($N=80$) | closed form, $N=80$ | ratio, $N=40$ | ratio, $N=80$ | ratio, $N=160$ |
|---|---|---|---|---|---|
| 1.2 | 6.05e−6 | 6.0510e−6 | 1.0004 | 1.0001 | 1.0000 |
| 1.5 | 2.99e−5 | 2.9927e−5 | 1.0006 | 1.0002 | 1.0000 |
| 1.8 | 6.29e−5 | 6.2891e−5 | 1.0008 | 1.0002 | 1.0000 |
| 2.0 | 8.75e−5 | **8.7459e−5** | 1.0009 | 1.0002 | 1.0001 |
| 2.2 | 1.13e−4 | 1.1316e−4 | 1.0010 | 1.0002 | 1.0000 |
| 2.271 | 1.22e−4 | 1.2247e−4 | 1.0010 | 1.0003 | 0.9999 |
| 2.5 | 1.53e−4 | 1.5283e−4 | 1.0012 | 1.0003 | 1.0001 |
| 3.0 | 2.20e−4 | 2.1971e−4 | 1.0014 | 1.0004 | 1.0001 |

Twenty-four cells; the worst is $0.14\%$ and it is at the coarsest truncation, as it
should be. **The column carries no information about Theorem 1.** In particular the
apparent growth in $\mu$ — which mg-5210 read as the margin improving with support —
is the factor $L^2$, and the true infimum is monotone *non-increasing* in $\mu$, since
a test function admissible at $\mu_1$ is admissible at every $\mu_2>\mu_1$ by extension
by zero and $-E$, $\lVert g\rVert^2$ and both conditions are all independent of $L$.
That monotonicity is a one-line theorem and it contradicts the printed table's trend;
it is the cheapest instrument that would have caught this, and it needs no code.

### 2.3 The minimising direction

CHECK 1(c), at $\mu=2$, on the codimension-two subspace:

| $N$ | smallest eigenvalue | three largest $\lvert$coefficients$\rvert$ |
|---|---|---|
| 40 | 3.5013e−4 | $n{=}40$: 1.000, $n{=}39$: 0.010, $n{=}38$: 0.005 |
| 80 | 8.7480e−5 | $n{=}80$: 1.000, $n{=}79$: 0.005, $n{=}78$: 0.002 |
| 160 | 2.1866e−5 | $n{=}160$: 1.000, $n{=}159$: 0.002, $n{=}158$: 0.001 |

It is the last basis vector. The work item asked whether it is a prolate mode, or
something the corpus has a name for, or related to the near-null direction of the other
form. It is none of those: **it is the truncation**. A direction that moves when the
basis moves is not a direction of the form, and there is no other candidate — the
infimum over the codimension-two subspace is $0$ and is not attained.

---

## 3. The condition row

`verify_sonin_trace.conditions()` returns two rows, $\hat g(0)$ and $\hat g(i/2)$ in the
cosine basis. The second is
$$\int_{-L/2}^{L/2}\cos(ay)e^{y/2}dy
=\Big[\tfrac{e^{y/2}(\tfrac12\cos ay+a\sin ay)}{\tfrac14+a^2}\Big]_{-L/2}^{L/2},$$
and the code evaluated the exponential at $y=\pm L$ rather than $y=\pm L/2$ —
`np.exp(q)` for `np.exp(q/2)`, $q=L/2$. So it imposed the integral over $[-L,L]$, twice
the support. CHECK 1(a) measures it: the closed form used here agrees with direct
integration on a fine grid to $2\times10^{-11}$ at $j=0,1,2,3$, and the as-coded row
deviates by $1.517$ at $\mu=5$, $N=6$.

**Machine-checked, not argued: what moves. Nothing does.** `verify_sonin_trace.py` was
run before and after the fix and the two outputs are **byte-identical** — every digit of
CHECK 4's conditioned column included, $8.747916\times10^{-5}$ at $\mu=2$ both times —
for the reason §2 gives: that column is $\epsilon'(1^+)L^2/2\pi^2N^2$ under *any* two
conditions, because the eigenvector realising it is the top cosine mode and two linear
constraints do not reach it. Every verdict the script decides still passes. **So the
defect was invisible to the only instrument pointed at it**, which is
`statement-defects.md`'s class exactly: what survives is the discrepancy the downstream
use does not exercise. Everything in §4 below *does* exercise it, and is computed with
the corrected row.

---

## 4. The inertia, and the hypothesis

### 4.1 Why inertia and not eigenvalue

Restricting a quadratic form to a subspace raises its smallest eigenvalue. So a
*negative* eigenvalue seen in a truncation certifies one for the full form, and the
count of negative eigenvalues can only be an undercount. It is also, unlike §2's
column, actually converged: the negative eigenvalues live at low frequency, where $N=60$
cosine modes are already a complete basis for all practical purposes.

Measured — counts identical and values agreeing to $10^{-3}$ at $N=60$ and $N=120$:

| $\mu$ | codim 0 | codim 1 | codim 2 | codim 3 | codim 4 |
|---|---|---|---|---|---|
| 2 | 1, −1.3411 | 0 | 0 | 0 | 0 |
| 2.5 | 1, −1.6541 | 0 | 0 | 0 | 0 |
| 3 | 2, −1.8667 | 1, −0.0319 | 0 | 0 | 0 |
| 4 | 2, −2.1520 | 1, −0.2076 | 0 | 0 | 0 |
| 6 | 2, −2.4818 | 1, −0.4404 | 0 | 0 | 0 |
| 8 | 3, −2.6798 | 2, −0.5829 | **1, −0.0921** | 0 | 0 |
| 10 | 3, −2.8179 | 2, −0.6828 | 1, −0.1815 | 0 | 0 |
| 14 | 3, −3.0051 | 2, −0.8192 | 1, −0.3084 | 1, −0.0160 | 0 |
| 20 | 3, −3.1807 | 2, −0.9492 | 2, −0.4303 | 1, −0.1233 | 0 |
| 30 | 4, −3.3571 | 3, −1.0832 | 2, −0.5549 | 1, −0.2428 | 1, −0.0258 |
| 50 | 4, −3.5505 | 3, −1.2366 | 2, −0.6950 | 2, −0.3797 | 1, −0.1534 |

*(count of negative eigenvalues, then the most negative)*

### 4.2 $\mu\le2$ is an artefact of the proof

Bisecting the codimension-$k$ smallest eigenvalue in $\mu$:

$$\mu_c(1)=2.7634,\qquad \mu_c(2)=6.1739,\qquad \mu_c(3)=13.011,\qquad \mu_c(4)=26.461$$

at $N=120$, each an upper bound on the true value and each $\le0.6\%$ below its $N=60$
counterpart. Theorem 1 is stated for $\operatorname{supp}g\subset[2^{-1/2},2^{1/2}]$,
i.e. $\mu\le2$, and its conclusion holds to $\mu=6.17$ — a factor $3.09$ in $\mu$,
$2.63$ in $\log\mu$.
**mg-5210 already observed that the form stays positive to $\mu=3$; the answer to "push
that" is that it stays positive to $6.17$ and then stops.** Connes–Consani's proof is
specific to $I=[\frac12,2]$ ([`semilocal-gap.md`](semilocal-gap.md) §1.3 records three
constants specific to that interval); nothing here extends the *proof*, and the
statement above is numerical.

The hypothesis is not vacuous. At $\mu=8$ the codimension-two form has an eigenvalue of
$-0.0921$, against $O(1)$ matrix entries, unchanged from $N=60$ to $N=120$. There is a
genuine threshold and the theorem is on the right side of it by a factor of three.

### 4.3 What one condition buys, and what a third buys

$\mu_c(1)=2.763>2$: **$\hat g(0)=0$ alone covers the whole of Theorem 1's support
range.** At $\mu\le2$ the unconditioned form has exactly one negative eigenvalue
($-1.3411$), and $\hat g(0)=0$ removes it. So for the sign of $-E$ at $\mu\le2$ the
condition $\hat g(i/2)=0$ is inert.

This is the precise refinement of mg-5210's Bottom-line item 6. That item's measurement
— *unconditioned, the gap is negative on some direction at every $\mu\ge1.2$* — is
reproduced here and stands. Its reading, *the two conditions are the theorem*, is half
right: one of them is, and the other is buying support range that Theorem 1 does not
claim. A third condition buys a further factor $2.11$, a fourth a further $2.03$.

---

## 5. Why, in one picture

$\hat\epsilon(0)=+5.3722$ and $\hat\epsilon(t)<0$ for $t>t_0=6.29177$. So the symbol of
$-E$ is negative on $|t|<t_0$ and positive outside it, and everything above follows:

- **§2** is the outside: $-\hat\epsilon(t)\sim2\epsilon'(1^+)/t^2\downarrow0$, so the
  spectrum accumulates at $0^+$ and the smallest truncated eigenvalue is a statement
  about the truncation frequency.
- **§4** is the inside: $-E$ can only be negative on directions whose $\hat g$ lives in
  $|t|<t_0$. A support of length $L$ resolves $t$ to $2\pi/L$, so that band holds about
  $Lt_0/2\pi$ independent directions, and $k$ vanishing conditions remove $k$ of them.
  Positivity therefore survives until $L\approx2\pi k/t_0$, i.e.
  $$\log\mu_c(k)\ \approx\ \frac{2\pi}{t_0}\,k\ =\ 0.9986\,k.$$
  Measured slope: $0.7523$. **The shape is right and the constant is $25\%$ out** — the
  conditions $\hat g(ij/2)=0$ sit at $k$ distinct points of the imaginary axis and only
  approximate a $k$-fold zero of $\hat g$ at $t=0$, which is where the $25\%$ lives.
  This is a count of resolution cells, not a derivation, and is offered as one.
- **§7 of the Bottom line** is the sign at $t=0$: $\epsilon>0$ forces
  $\hat\epsilon(0)>0$, so the failure at large $\mu$ was never avoidable.

**A coincidence, checked.** $t_0=6.2917746$ and $\theta'$ — the density of $W_\infty$ on
the Fourier side, `verify_arch_positivity.py` CHECK 4 — changes sign at $6.2898336$.
Three digits. The difference $1.94\times10^{-3}$ is stable across $Y=3.5\ldots6$,
$110$–$220$ quadrature panels, $8$–$12$ prolate modes and twice the $\epsilon$
quadrature, all of which move $t_0$ by less than $10^{-4}$. **They are different
numbers.** It is recorded here because it is exactly the kind of near-identity a reader
adopts without checking, and because a genuine identity there would have been a real
structural fact about the Sonin projection and $W_\infty$ — worth the ten minutes it
took to rule out.

---

## 6. House rule

| statement | false for $W_\lambda\to-W_\lambda$? |
|---|---|
| §2: the conditioned column is $\epsilon'(1^+)L^2/2\pi^2N^2$; there is no margin | no — about $E$ alone. **Sign-blind** |
| §2.3: the minimiser is the top cosine mode | no. Sign-blind |
| §3: `conditions()` row 1 was not $\hat g(i/2)$ | no. Sign-blind |
| §1.2, §5: $\hat\epsilon(0)=5.37>0$, $t_0=6.2918$, $\hat\epsilon t^2/2\to-\epsilon'(1^+)$ | no. Sign-blind |
| §4.1: the inertia table and its stability in $N$ | no. Sign-blind |
| §4.2: **Theorem 1's conclusion $W_\infty(g\star g^*)\ge\operatorname{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)$ holds to $\mu=6.17$, three times its stated hypothesis** | **YES.** The trace does not move under the substitution and $W_\infty$ does, so the direction of the inequality does |
| §4.2: **it is false from $\mu=6.17$ on** | **YES**, same reason |
| §4.3: **at $\mu\le2$ one condition already gives the inequality** | **YES**, same reason |
| §4.3: unconditioned the inequality fails at every $\mu$ (mg-5210 §6, reproduced) | **YES**, and this is mg-5210's statement, re-verified |

**Four statements that are not sign-blind, where mg-5210 produced three.** They are not
progress towards positivity and are not offered as such — two of them say a positivity
statement is *false* somewhere. What is worth carrying is the pattern mg-5210 identified
and this note confirms: introduce $W_\infty$ as a *term in an identity* rather than as a
thing to be bounded, and statements that know about the sign appear immediately.

**And the warning that goes with it.** Every one of this note's non-sign-blind
statements rests on sign-blind machinery — $\epsilon$, its symbol, a condition row, a
truncation order. Both defects §2 and §3 retire are sign-blind, and both fed straight
into a signed conclusion. *A sign-blind measurement error propagates into a signed
statement perfectly well*; the house rule sorts statements, not errors.

---

## 7. Provenance, and what is unverified

**Re-verified, not inherited.** mg-5210's five printed anchors for the $c=2\pi$ prolate
apparatus are re-run by importing its `Prolate` unchanged; its $\epsilon$ and this
note's agree to $10^{-11}$ for $\rho\le50$ (CHECK 2); its CHECK 4 columns are reproduced
to the last figure before being reinterpreted (CHECK 1).

**Computed here, and anchored:** the tail law $\hat\epsilon(t)t^2/2\to-\epsilon'(1^+)$,
against Connes–Consani's printed $22.9965$, $0.15\%$ — and independently against the
twenty-four truncated eigenvalues of §2.2, which is the same constant reached by a
different route (a Fourier transform of $\epsilon$ against an eigenvalue of a
Galerkin matrix).

**Computed here, and NOT independently anchored:**

- $\epsilon(\rho)\sqrt\rho\to1$. Measured to $0.5\%$ at $\rho=60$ and used only to make
  $\hat\epsilon$ converge. An attempt to derive the constant from the large-$\omega$
  expansion of $\mathcal F\xi_n$ gave $37.5$, not $1$, so the leading term evidently
  cancels; that derivation is **abandoned, not repaired**, and the $1$ is a measurement.
- Every number in §4. They rest on the $-E$ matrix, which rests on $\epsilon$ (anchored)
  and on `verify_arch_positivity._h` (anchored by mg-555b), and on the corrected
  condition rows (anchored against direct integration). The *combination* has one
  external check, and it is mg-5210's CHECK 2 — unconditional positivity of the Sonin
  trace form, a sign rather than a value. **A uniform multiplicative error in $\epsilon$
  would not move any $\mu_c$ at all**, since $\mu_c$ is where an eigenvalue crosses
  zero; it would move the eigenvalue columns.
- $\mu_c(4)=26.46$ is close to the $\mu=60$ ceiling this script's $\epsilon$ table is
  built to, and $\mu_c(5)$ is not computed. Nothing above uses it.
- The cosine basis is not $C_c^\infty$ — mg-5210 §8's caveat, unchanged and inherited.

**Not attempted.** The semilocal case — out of scope by the work item. Anything Lean.
Any paper edit. A proof of anything: §4.2's "the conclusion is false at $\mu=8$" is a
converged numerical eigenvalue with a variational certificate (truncation raises the
smallest eigenvalue, so a negative truncated eigenvalue certifies a negative one for the
full form), which is as close to a proof as this note gets, and it is not one.

**Open, and the obvious next measurement.** The same reduction for the *semilocal* form,
where the corpus's actual target lives — the prime terms add a positive-definite piece
whose symbol is a sum of $\cos(mt\log p)$, and the question is whether they raise
$\hat\epsilon$'s negative band or move $t_0$. And mg-5210's own open item, the Sonin
trace on $k_\lambda=E(h_\lambda)$, which this note does not touch.
