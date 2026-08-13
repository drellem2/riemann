# How big is the Sonin trace

Work item mg-5210. Companion script:
[`verify_sonin_trace.py`](verify_sonin_trace.py) (needs `numpy`; ~3 minutes).
Continues [`citation-audit.md`](citation-audit.md) (mg-3a9c) and
[`semilocal-gap.md`](semilocal-gap.md) (mg-03f0), which between them established
that the corpus's objects are Connes–Consani's and that
$\operatorname{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)$ is the single place a
Weil sign is actually proved. Neither evaluated it. This note does.

Source read as arXiv LaTeX from `arxiv.org/e-print/`: arXiv:2006.13771
(`weil-compo.tex`, the archimedean theorem) and arXiv:2106.01715
(`Spectraltriples.tex`, the corpus's own objects). Line numbers below are lines
of those files. Provenance is §8, to the standard of `citation-audit.md` §9.

Nothing in `start.tex` or `s3.tex` was edited, and **no existing number in the
corpus moves** — §7.

> **CORRECTED BY mg-d03b — read [`sonin-margin.md`](sonin-margin.md) with this note.**
> Two claims below are wrong and are marked where they occur.
>
> 1. **There is no margin of $8.7\times10^{-5}$.** $-E$ is a compact operator, so its
>    eigenvalues accumulate at $0$ and the smallest eigenvalue of an $N$-term truncation
>    is a statement about $N$. Every entry of §2.2's conditioned column is
>    $\epsilon'(1^+)L^2/2\pi^2N^2$ to four figures, at $N=40$, $80$ and $160$; the
>    minimising direction is the top cosine mode. Bottom line 5 and §§2.2–2.3 are
>    affected. **Every *sign* in this note stands.**
> 2. **`verify_sonin_trace.conditions()` row 1 was not $\hat g(i/2)$** — an endpoint,
>    now fixed. No output of this note's script moved: the two runs are byte-identical.
>
> What replaces the margin is the inertia, which is truncation-stable: Theorem 1's
> conclusion holds to $\mu=6.17$ against its stated $\mu\le2$, is false past that, and
> needs only *one* of its two conditions at $\mu\le2$.

---

## Bottom line

**1. The trace is computable, and Connes–Consani compute it.** It is not an
inaccessible object and it does not need re-deriving. `weil-compo.tex:1132`,
Theorem `devil`, gives, for every $f\in C_c^\infty(\mathbb R_+^*)$,
$$\operatorname{tr}(\vartheta(f)\mathbf S)=W_\infty(f)+\int f(\rho)\,\epsilon(\rho)\,d^*\rho,$$
$\epsilon(\rho^{-1})=\epsilon(\rho)$, with $\epsilon$ an explicit prolate series
(§1). So
$$\boxed{\ \text{Sonin trace}=W_\infty+E,\qquad
\text{gap}:=W_\infty-\text{Sonin trace}=-E\ }$$
and the whole of Theorem 1 — seventy pages — is the single statement that the
quadratic form $-E$ is positive on the codimension-two subspace
$\widehat g(0)=\widehat g(i/2)=0$ for $\mu\le2$. §2.

**2. The answer, in numbers.** Per unit $\lVert g\rVert^2$, over the $\mu$ range
where the corpus has numbers. The floor — the least the trace can be made over
all test functions of that support — and its value on the corpus's own vectors:

| $\mu$ | floor $\min S$ | $S$ on `witness` | $S$ on the two-mode prolate | $W_\infty$ on `witness` |
|---|---|---|---|---|
| 1.2 | 3.72e−1 | 1.913 | 2.259 | 1.947 |
| 1.5 | 3.77e−2 | 0.957 | 1.244 | 1.147 |
| 2.0 | 2.55e−3 | 0.232 | 0.678 | 0.610 |
| 2.271 | 9.41e−4 | 0.0956 | 0.578 | 0.441 |
| 3.0 | 1.49e−4 | 0.0183 | 0.458 | 0.146 |

**The trace is the same order as the Weil functional, not a correction to it.**
On the corpus's two-mode prolate combination it is $73\%$ of $W_\infty$ at
$\mu\ge2.2$ and the ratio is flat in $\mu$. §3.

**3. It is not the corpus's small, and the comparison the work item asks for has
a number: a factor of four in the exponent.** The floor decays at
$-3.06$ per unit $\mu$ (least squares over $\mu\ge1.8$); the corpus's headline is
$\limsup\mu^{-1}\log s(\mu)\le-4\pi=-12.57$. At $\mu=2$ the corpus's deficit
$1-\chi_4$ is $\sim10^{-11}$ and the trace's floor is $2.5\times10^{-3}$ —
**eight orders apart, and separating exponentially.** Nothing the corpus has
bounded is a bound on this. §4.

**4. The premise the work item was filed on is wrong, and it is worth correcting
precisely.** "Our $\lambda$ is their Sonin cutoff $\Lambda$"
(`signed-geometry-proposals.md:373`) is true of arXiv:2106.01715, where cutoff
and support move together, and **false of the 2021 archimedean theorem**, where
the Sonin cutoff is frozen at $\Lambda=1$ and only the support moves. The
consequence is quantitative: $\epsilon$ is a prolate expansion at **fixed**
bandwidth $c=2\pi$, the corpus's apparatus runs at $c=2\pi\mu$
(`verify_prolate_rate.py:8`), and at $\mu=2$ the two concentration defects are
$5.7\times10^{-5}$ and $\sim10^{-11}$. The trace is reachable from the corpus's
*machinery*; it is not reachable from the corpus's *numbers*, because those are
all at the wrong bandwidth. §5.

**5. "Positivity is trace $\ge$ gap" is not what the theorem says.** It says
$W_\infty=\text{trace}+\text{gap}$ with **both** terms non-negative under the
conditions — the trace by construction, the gap by the seventy pages. Positivity
is a sum of two non-negative things, not a race between them. ~~What *is* true, and
is measured here, is that the race is close: on the direction where the gap is
smallest it is $8.7\times10^{-5}$ at $\mu=2$ against a $W_\infty$ of order one, so
**there the Sonin trace is essentially all of the Weil functional.**~~
**WRONG (mg-d03b).** That number is $\epsilon'(1^+)L^2/2\pi^2N^2$, the $N=80$
truncation order; the infimum over the conditioned subspace is $0$ and is not
attained, so there is no such direction. [`sonin-margin.md`](sonin-margin.md) §2.

**6. One sign-sensitive statement, which is the point of the ticket.** *Before
the two vanishing conditions are imposed, the gap $W_\infty-\operatorname{Tr}$ is
negative on some direction at every $\mu\ge1.2$, including $\mu=2$, inside the
theorem's own support range.* That is **FALSE for $W_\lambda\to-W_\lambda$**: the
trace does not move under that substitution and $W_\infty$ does. It is the first
statement in this corpus that is not sign-blind. It is also, read the other way,
a measurement of what the two conditions are doing: they are not decoration, they
are the theorem. §6.

---

## 0. Vocabulary

As in [`semilocal-gap.md`](semilocal-gap.md) §0: **proved** = a theorem with a
proof, cited by label and line; **numerical** = computed here or by the authors,
presented as evidence; **ours** = derived here, marked at every occurrence.

---

## 1. The trace, in closed form

### 1.1 The objects

$\mathbf S$ is the orthogonal projection of $L^2(\mathbb R)_{\rm ev}$ onto Sonin's
space $S(1,1)$ — the even $L^2$ functions vanishing, together with their Fourier
transform, on $[-1,1]$ (`weil-compo.tex:1050`, Definition `defnsonine`).
$\vartheta$ is the scaling action, $(\vartheta(\lambda)\xi)(v)=\lambda^{-1/2}\xi(\lambda^{-1}v)$
(`:917`). $W_\infty:=-W_{\mathbb R}$ is the archimedean Weil functional.

$\xi_n$ is the $L^2$-normalized restriction to $[-1,1]$ of the even prolate
spheroidal function $\mathit{PS}_{2n,0}(2\pi,\cdot)$, $\lambda(n)$ its
finite-Fourier eigenvalue,
$$\int_{-1}^1\mathit{PS}_{2n,0}(2\pi,x)e^{2\pi ix\omega}dx=\lambda(n)\,\mathit{PS}_{2n,0}(2\pi,\omega)$$
(`:966`), and $\xi_n^{\rm an}=\mathcal F\xi_n/\lambda(n)$ the analytic
continuation of $\xi_n$ past $1$ (`:1348`). **Proved.**

### 1.2 The formula

> **Theorem `devil` (`weil-compo.tex:1132`).** The functional
> $\operatorname{tr}(\vartheta(f)\mathbf S)$ is positive and
> $$\operatorname{tr}(\vartheta(f)\mathbf S)=W_\infty(f)+\int f(\rho)\epsilon(\rho)d^*\rho,
> \qquad\forall f\in C_c^\infty(\mathbb R_+^*),$$
> with $\epsilon(\rho^{-1})=\epsilon(\rho)$ and, for $\rho\ge1$ (`:1373`),
> $$\epsilon(\rho)=\sum_n\frac{\lambda(n)^2}{1-\lambda(n)^2}\;
> \rho^{1/2}\!\!\int_{\rho^{-1}}^{1}\!\!\xi_n^{\rm an}(x)\,\xi_n^{\rm an}(\rho x)\,dx .$$

Two remarks the corpus should carry.

**The trace is quadratic in $g$ only through $f$.** $\mathbb R_+^*$ is abelian, so
$\operatorname{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)=\operatorname{tr}(\vartheta(g\star g^*)\mathbf S)$
with no ordering question, and the object of Theorem 1 and the object of Theorem
`devil` are the same object.

**Prolate theory is the coordinate system, not the mechanism** —
`semilocal-gap.md` §1.2 already says this, and $\epsilon$ is where it becomes
concrete. The sign comes from $\mathbf S=\mathbf S^*=\mathbf S^2$; the prolate
functions only make the *difference* computable.

### 1.3 It is computed, and it is anchored five ways

`verify_sonin_trace.py` CHECK 1 rebuilds the $c=2\pi$ apparatus from the Legendre
eigenproblem for $-\partial((1-x^2)\partial)+c^2x^2$ and reproduces every printed
anchor Connes–Consani give for it:

| anchor | source | ours |
|---|---|---|
| $\lambda(0..5)=0.999971,\,-0.979485,\,0.524086,\,-0.0589766,\,0.00273233,\,-7.62914\text{e-}5$ | `:969` | all six, max relative deviation $5.3\times10^{-7}$ |
| $\sum\lambda(n)^2=2(\mathrm{Si}(4\pi)/4\pi+1)$ | `:1101` | $2.2374848349$ both sides |
| $t(n)=\tfrac{\lambda(n)^2}{1-\lambda(n)^2}\xi_n(1)^2=11.9719,\,8.77574,\,2.20528,\,0.0433983,\,1.25459\text{e-}4$ | `:1380` | all five to the printed digits |
| $\epsilon'(1^+)=22.9965$ | `:1367` | $22.996476$ |
| $\epsilon'(1^+)$ recovered from the series itself by difference | — | $22.9964$ at $h=10^{-5}$ |

Two further checks, made while debugging and worth recording because they are
independent of the above: $\delta(\rho)=\sum_n\lambda(n)^2\langle\xi_n\mid\vartheta(\rho^{-1})\xi_n\rangle+\sum_n\lambda(n)^2 I_n(\rho)$
(`:1001`, `:1028`) agrees with the elementary closed form
$\delta(\rho)=2\rho^{1/2}\bigl(\tfrac{\mathrm{Si}(2\pi(1+\rho))}{2\pi(1+\rho)}+\tfrac{\mathrm{Si}(2\pi(\rho-1))}{2\pi(\rho-1)}\bigr)$
(`:576`, eq. `sch18`) to ten digits at every $\rho\in[1,3]$ — a prolate series
against a sine-integral, sharing nothing; and $\epsilon$ computed by two
different splittings of its integral agrees to eight digits under every
quadrature setting tried.

---

## 2. The gap is $-E$, and Theorem 1 is one line about it

### 2.1 The restatement

Subtracting Theorem `devil` from Theorem 1 leaves
$$W_\infty(g\star g^*)\ \ge\ \operatorname{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)
\iff E(g\star g^*)\le0,\qquad E(f):=\int f(\rho)\epsilon(\rho)d^*\rho .$$
So Connes–Consani's main theorem, as a statement about test functions, is:
**the quadratic form $-E$ is positive semi-definite on
$\{\widehat g(0)=\widehat g(i/2)=0\}$ for $\operatorname{supp}g\subset[2^{-1/2},2^{1/2}]$**,
and $-E$ is a prolate series at $c=2\pi$ that fits on one line. The seventy pages
are the proof; the statement is small, and the corpus can now hold it.

### 2.2 It holds where it is claimed, and past it

CHECK 4, smallest eigenvalue of $-E$ restricted to the codimension-two subspace,
per unit $\lVert g\rVert^2$:

| $\mu$ | 1.2 | 1.5 | 1.8 | 2.0 | 2.2 | 2.271 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|
| min gap | 6.05e−6 | 2.99e−5 | 6.29e−5 | 8.75e−5 | 1.13e−4 | 1.22e−4 | 1.53e−4 | 2.20e−4 |

Positive at every $\mu$ on the grid. **Ours, numerical.** *The signs in this row
stand; the values do not — every one of them is
$\epsilon'(1^+)L^2/2\pi^2N^2$ at $N=80$, and they tend to $0$ as $N$ grows
([`sonin-margin.md`](sonin-margin.md) §2). The apparent growth in $\mu$ is the factor
$L^2$; the true infimum is monotone non-increasing in $\mu$.* For $\mu\le2$ this
reproduces the theorem; for $\mu>2$ it is an observation with no theorem behind
it — Connes–Consani's proof is specific to $I=[\frac12,2]$ (`semilocal-gap.md`
§1.3: three numbers, all specific to that interval) and nothing here extends it.

### 2.3 The margin is thin, and that is the interesting part — WRONG (mg-d03b)

**This subsection is retired.** It read the column of §2.2 as a margin. It is not
one: $-E$ is a compact operator, its eigenvalues accumulate at $0$, and the smallest
eigenvalue at $N$ cosine modes is $\epsilon'(1^+)L^2/2\pi^2N^2$ — $8.7459\times10^{-5}$
at $\mu=2$, $N=80$, against the $8.747916\times10^{-5}$ printed above, and a quarter of
that at $N=160$. The minimising vector is the top basis mode.
[`sonin-margin.md`](sonin-margin.md) §2 does the arithmetic against all eight rows at
three truncation orders. The paragraph as written is kept below, struck, because a
retraction that deletes the claim leaves nobody able to check the retraction.

> ~~Compare the two columns. The gap's *minimum* is $8.7\times10^{-5}$ at $\mu=2$; the
> Weil functional on the same test space is of order one. So on that direction the
> inequality of Theorem 1 is very nearly an equality: **the Sonin trace is
> essentially the whole of $W_\infty$, and the seventy pages buy a margin of one
> part in $10^4$.**~~

The rest of this subsection is unaffected, and it is worth saying because the work
item's framing — "positivity is trace
$\ge$ gap … we have spent the programme bounding the gap from above" — reads the
theorem as a competition between two terms. It is not. $W_\infty$ is their
*sum*, both are non-negative under the conditions, and positivity needs neither
to dominate. What the numbers add is that one of them is almost all of it.

---

## 3. How big — the measurement

CHECK 3, per unit $\lVert g\rVert^2$, at $N=80$ cosine modes. $S$ is the Sonin
trace, $W$ is $W_\infty$, gap $=W-S=-E$.

**(a) On the minimizing direction of $W_\infty$.** $S$ falls from 3.77e−1 at
$\mu=1.2$ to 2.25e−2 at $\mu=3$, while $W_\infty$ there is negative and growing
($-1.29$ at $\mu=2$): unconditioned, the Weil functional alone has directions on
which it is very negative, and the trace on those directions is small, positive,
and larger than it.

**(b) The floor.** $\min S$ over all $g$: 3.72e−1, 3.77e−2, 6.32e−3, 2.55e−3,
1.20e−3, 9.41e−4, 4.73e−4, 1.49e−4 at $\mu=1.2,1.5,1.8,2,2.2,2.271,2.5,3$.

**(c) On `verify_arch_positivity.witness`'s explicit test function.** That
function has $\widehat g(\pm i/2)=0$, so the corpus's `sigma_arch` equals
$W_\infty$ on it exactly and the columns are directly comparable to that script's.
$S/W_\infty$ falls from $0.98$ at $\mu=1.2$ to $0.13$ at $\mu=3$.

**(d) On the two-mode prolate combination** $h_\lambda=\alpha h_{0,\lambda}+\beta h_{4,\lambda}$
at the corpus's own bandwidth $c=2\pi\mu$, with the CCM coefficients
(`citation-audit.md` §4.2), used directly as a test function: $S/W_\infty$
settles at $0.73$ and stays there, $\mu=2.2$ to $3$.

**What (d) is not.** It is not $k_\lambda=E(h_\lambda)$: building the summation
operator $E$ is out of this script's scope. The distinction matters and is not
papered over — $k_\lambda$ is where the corpus's $\asymp1-\chi_4$ lives
(`start.tex:39`), and evaluating the Sonin trace on it is the obvious next
measurement. What (d) does establish is that a vector built from the corpus's own
prolate modes, at the corpus's own bandwidth, carries a Sonin trace of the same
order as its Weil functional — flat in $\mu$, no decay.

---

## 4. Against the corpus's own rate

Least squares on $\log(\min S)$ over $\mu\ge1.8$ gives $-3.06$ per unit $\mu$.
The corpus's headline is $\limsup\mu^{-1}\log s(\mu)\le-4\pi=-12.566$. The
smallest the trace can be made therefore decays **four times slower in the
exponent** than the quantity the first six notes assemble a bound for.

At $\mu=2$: $1-\chi_4\sim10^{-11}$ (`prolate-rate.md`, $e^{-4\pi\mu}$ at
$c=2\pi\mu$) against a trace floor of $2.5\times10^{-3}$. Eight orders, widening
by $e^{9.5\mu}$.

**So the answer to "is the trace above or below the gap, and how does the margin
move" is that the two live on different scales entirely, and the corpus's $-4\pi$
is not a statement about either of them.** $-4\pi$ bounds the prolate
concentration defect at $c=2\pi\mu$; the gap in Theorem 1 is $-E$, an $O(1)$
quantity at $c=2\pi$. The work item's identification of the two — "our deficit,
our rate, our $-4\pi$ bound and all 91 Lean results are statements about the gap"
— does not survive contact with the objects. They are statements about a
different gap.

---

## 5. Two bandwidths, and why the corpus cannot reach the trace with its numbers

| | Sonin trace | corpus |
|---|---|---|
| prolate bandwidth | $c=2\pi$, **fixed** (the Sonin cutoff $\Lambda=1$) | $c=2\pi\mu$, moving |
| what moves with $\mu$ | the test function's support | both cutoff and support |
| $1-\Lambda_0$ at $\mu=2$ | $5.72\times10^{-5}$ | $2.1\times10^{-1}$ (index 0), $\sim10^{-11}$ (index 4) |
| source | arXiv:2006.13771 `:965` | `verify_prolate_rate.py:8` |

CHECK 5 tabulates the ratio: 325 at $\mu=1.2$ rising to 7129 at $\mu=3$ for index
0, and far larger for the index-4 quantity the corpus actually uses.

This is the precise form of the finding the work item asked for under "if it
turns out not to be expressible in them, that is the finding". The answer is in
between: **the trace is expressible in the corpus's machinery — the same Legendre
eigenproblem, the same functions, the same script style — and not in the corpus's
numbers, every one of which is at a bandwidth that grows with $\mu$ while the
Sonin space's does not.** A transport by name alone is wrong by the table above.

---

## 6. House rule

Applied statement by statement.

| statement | false for $W_\lambda\to-W_\lambda$? |
|---|---|
| §1: $\operatorname{tr}(\vartheta(f)\mathbf S)=W_\infty(f)+E(f)$ | **yes** — an identity between something that flips and something that does not; it is false for $-W_\lambda$ unless $W_\infty\equiv0$ |
| §2.2: the gap $-E$ is positive on the codimension-two subspace, $\mu\le3$ | no — $E$ is built from $\mathbf S$ and $\vartheta$ and never mentions $W_\lambda$. Sign-blind |
| §3: the trace's size, every column headed $S$ | no. Sign-blind |
| §6 headline: *unconditioned, $W_\infty-\operatorname{Tr}<0$ on some direction at every $\mu\ge1.2$* | **YES.** The trace is fixed, $W_\infty$ flips, so the sign of the difference flips |
| ~~§2.3: on the minimizing direction the trace is essentially all of $W_\infty$~~ | **retired by mg-d03b** — there is no such direction. The house rule sorted it correctly as not sign-blind; it was still false |
| §4: the trace's floor decays at $-3.06$, against $-4\pi$ | no. Sign-blind |
| §5: the two bandwidths | no. Sign-blind |

**Three statements that are not sign-blind, where the corpus had none** — two after
mg-d03b retired the third, and that is the lesson worth carrying with the finding: *the
house rule sorts statements, not errors.* It marked §2.3's claim as sign-sensitive,
correctly, and the claim was wrong anyway, for a sign-blind reason (a truncation order).
 They are
not progress towards positivity and are not offered as such — the first is
Connes–Consani's identity, and the other two are measurements of how their
theorem sits. What they demonstrate is that the sign-blindness of the corpus was
never forced by the subject: it followed from working only with subspaces,
projections and norms (`signed-geometry-proposals.md` §2.1's lemma). Introduce
$W_\infty$ *as a term in an identity* rather than as a thing to be bounded, and
statements that know about the sign appear immediately.

---

## 7. The defect this note nearly shipped, and the instrument that caught it

Recorded because [`statement-defects.md`](statement-defects.md) asks for it, and
because it is the same class one level out: **the printed identification of two
objects did not match the objects.**

The first version of `verify_sonin_trace.py` read
`verify_arch_positivity.py`'s matrices as $\tfrac12a^\top Ma$ — the reading the
Gram $h(0)=2I$ invites — and identified its $W_{\mathbb R}^\#$ with the
$W_{\mathbb R}$ of the 2021 paper. It is off by a factor of two, because
Connes–Consani 2023 write the Weil form as $\psi(h)=\psi^\#(h+h^\sigma)$
(`Spectraltriples.tex:410`), so $W_{\mathbb R}^\#$ is applied to the
**symmetrized** function and $W_{\mathbb R}^\#(h+h^\sigma)$ is exactly the 2021
paper's $W_{\mathbb R}(h)$, with no factor. $\epsilon$, stated against the
un-symmetrized $f$, carries the factor and $W_{\mathbb R}^\#$ does not.

Everything downstream still looked right. All five CHECK 1 anchors passed —
they are about $\epsilon$ alone. The tables printed plausible numbers. What
failed was CHECK 2: $\operatorname{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)$ is a
Hilbert–Schmidt norm and is therefore non-negative for **every** test function,
with no support and no vanishing condition — and with the wrong factor the
computed form is *indefinite from $\mu=1.8$ on*, by a margin of $10^{-1}$.

That is the shape `statement-defects.md` §2.1 asks for: an instrument pointed at
the statement rather than at its consequences, which could disagree with it, and
did. Three other things were tried first and all three passed with the wrong
factor — positivity of $L=D+W_\infty$, positivity of
$Z=\sum\lambda(n)^2\langle\zeta_n\mid\vartheta(f)\zeta_n\rangle$, and agreement of
the matrix code with direct integration to seven digits. A check that passes
under both readings is not an instrument.

**Machine-checked, not argued: nothing downstream moves.** No file outside this
note and its script was changed, so no corpus number can have moved; and the
factor was never in the corpus in the first place — `verify_arch_positivity.py`
uses its own matrices as $a^\top Ma$ throughout, which is correct, and it does
not claim its $W_{\mathbb R}^\#$ is the 2021 paper's $W_{\mathbb R}$. **This is
not a defect in the corpus.** It is a trap on the path between the two
Connes–Consani papers, and it is recorded so the next reader crossing it pays
once.

---

## 8. Provenance, and what is unverified

**Sources.** arXiv:2006.13771 and arXiv:2106.01715, downloaded as LaTeX from
`arxiv.org/e-print/` on 2026-08-13 and read directly. Every `weil-compo.tex:NNN`
and `Spectraltriples.tex:NNN` above is a line of those files as downloaded.

**Computed here, and anchored:** the $c=2\pi$ prolate apparatus (five printed
anchors, §1.3), $\epsilon$ (two independent splittings, and $\delta$ against the
sine-integral closed form to ten digits).

**Computed here, and NOT independently anchored:**

- Every number in §§2–4. They rest on `verify_arch_positivity.py`'s
  $W_{\mathbb R}$ matrix, which is itself anchored (mg-555b reproduced
  Connes–Consani's $0.00133$ and $2.27099$), and on $\epsilon$, which is anchored
  — but the *combination* has one non-trivial external check, CHECK 2's
  unconditional positivity, and that check is a sign, not a value. **A uniform
  multiplicative error in the tables of §3 would not be caught by anything in
  this note.** The ratios $S/W_\infty$ would be, since both columns would scale
  together.
- The $N=80$ truncation. Restricting a quadratic form to a subspace raises its
  smallest eigenvalue, so the floors of §3(b) are upper bounds for the true
  floor, and CHECK 2's positivity at finite $N$ does not by itself prove
  positivity of the full form. CHECK 2 was run at $N=40$ and $N=80$ with the same
  sign at every $\mu$.
- The cosine basis is not $C_c^\infty$: its elements have jumps at $\pm L/2$.
  Theorem `devil` is stated for $C_c^\infty$. The functionals involved are
  continuous in a norm for which $C_c^\infty$ is dense, so the extension is
  routine, but it is an extension and is not proved here. §3's rows (c) and (d)
  use functions that vanish at the endpoints, and agree with the eigenvalue
  columns in order of magnitude.

**Not attempted.** The semilocal case — out of scope by the work item.
$k_\lambda=E(h_\lambda)$ — §3(d) says what was used instead and why. Anything
Lean.

**Superseded.** §2.3's margin, and the values (not the signs) of §2.2's conditioned
column — [`sonin-margin.md`](sonin-margin.md), which also fixes `conditions()`.

**Open, and the obvious next measurement.** Evaluate the Sonin trace on
$k_\lambda=E(h_\lambda)$, the vector `start.tex:39`'s $\asymp1-\chi_4$ is about.
That is the one place where the corpus's central unresolved estimate and the
object with the sign in it would be evaluated on the same vector.
