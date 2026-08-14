# Is sign-sensitivity a generator? — the substitution run on the whole corpus

Work item mg-baa9. **No new numerics.** This is a classification pass over statements
already merged; every number quoted below belongs to the ticket that produced it and is
attributed at the point of use. No script was written and none was run. Nothing in
`start.tex`, `s3.tex` or `paper/` was edited.

The slice replaces R2 (NO-GO, `docs/roadmap.md@3a402d7` under "THE CALL"). It was
dispatched on mg-5210's observation that the corpus had produced its first non-sign-blind
statement, and on the reading that the *mechanism* behind it — the Sonin trace does not
move under $W_\lambda\to-W_\lambda$ while $W_\infty$ does — is a rule for producing such
statements rather than a one-off.

---

## Bottom line

**1. The generator's two halves both hold, and neither is the load-bearing one.**
$\operatorname{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)$ is invariant under
$W_\lambda\to-W_\lambda$ — proved twice in §1, once syntactically (it is built from
$\mathbf S$ and $\vartheta$, and mg-8599 §2.1's lemma applies verbatim) and once
structurally (it is $\lVert\mathbf S\vartheta(g)^*\rVert_{HS}^2$, so no substitution
acting on $W$ alone can reach it). $W_\infty$ is not invariant: it is not identically
zero, and mg-555b's explicit witness (`semilocal-gap.md` §10.3) shows it taking both
signs. **What actually does the work in every classification below is neither of those.
It is that $\operatorname{Tr}$ is *strictly* positive somewhere — and that is measured,
not proved, in this corpus** (`sonin-trace.md` §3(b) floors, mg-5210). §1.4.

**2. The generator as stated in the roadmap is FALSE, and its counterexample is
mg-5210 §6 — the statement the slice was dispatched on.** The roadmap
(`docs/roadmap.md:87-88`) reads: *"every statement that compares the moving quantity to
the fixed square is sign-sensitive, automatically."* It is not automatic, and the
quantifier decides it. Write $T$ for any sign-blind $T\ge0$:

| statement | under $W\to-W$ | verdict |
|---|---|---|
| $\forall g\in X:\ W(g)\ge T(g)$ | forces $W(g_0)<0$ where $W(g_0)\ge T(g_0)>0$ | **false** — sign-sensitive |
| $\exists g\in X:\ W(g)<T(g)$ | witnessed by any $g_1\in X$ with $W(g_1)\ge0$ | **true** — sign-blind |

The two rows are the same comparison, asserted and denied. **Assert the inequality and
you get a sign-sensitive statement; assert that it fails and you get a sign-blind one.**
mg-5210 §6 — *"before the vanishing conditions are imposed, the gap
$W_\infty-\operatorname{Tr}$ is negative on some direction at every $\mu\ge1.2$"* — is
the second row, and the counterexample to its own classification is printed two screens
above it, in mg-5210's own Bottom-line table. §2.

**3. Twenty statements in the five notes are marked sign-sensitive. Twelve survive the
substitution, seven do not, one is conditional — out of 41 examined.** The seven
downgrades are `sonin-trace.md:350`, `sonin-margin.md:390`, `:392`,
`sonin-ceiling.md:536`, `:537`, `semilocal-gap.md:614-616`, `:617-619`. Five are the
failure row of item 2; two are statements that mention no $W$ at all and were classified
by the *role* they play in an argument rather than by the substitution — which is the
trap `sonin-margin.md` §6 names in its own closing line ("the house rule sorts
statements, not errors"), arriving one level up. §3, with the table.

**4. The rule is not invariant under rewriting through a true identity, and this is what
the census has been measuring.** $-E\ge0$ on $X$ and $W_\infty\ge\operatorname{Tr}$ on
$X$ are *the same claim* — Theorem `devil` is the identity between them — and the house
rule calls the first sign-blind and the second sign-sensitive. So a count of
sign-sensitive statements is a count of **presentations**, not of content, and
"three where the corpus had none" (mg-5210 §6), "four where mg-5210 produced three"
(mg-d03b §6) are not measurements of progress. §4.

**5. The generator has a fixed polarity, and it points the wrong way for this corpus.**
Reading it as the transfer it really is — sign-blind facts about $E$, plus
$\operatorname{Tr}\ge0$, plus the identity, give sign facts about $W_\infty$ — the
transfer only runs one way:

- a **lower** bound $-E\ge0$ on $X$ $\Longrightarrow$ $W_\infty\ge\operatorname{Tr}>0$ on
  $X$: sign-sensitive, points toward positivity;
- an **indefiniteness** statement about $-E$ $\Longrightarrow$ "the inequality fails
  somewhere": sign-blind, points nowhere.

Every theorem this corpus has proved for itself about $E$ is of the second kind —
Theorem A (mg-0b7a §3.1), the inertia counts, $\log\mu_c(k)\le\Lambda(k)$, the even/odd
split. **The half of the generator that could point toward positivity needs exactly the
input the corpus has never had** (mg-0b7a Bottom-line item 8: every $\mu_c$ is an upper
bound on a threshold whose lower half is unproved). §5.

**6. The direct answer to the question that decides the programme: no.** Of the twelve
confirmed sign-sensitive members, two point toward positivity — Theorem 1 itself, and
"positivity is restored by adding the prime 2" — and **both are Connes–Consani's**. The
corpus's own contributions to the family are one numerical extension of Theorem 1's
range in the direction Theorem A proves is capped ($\mu_c(2)=2.754$, mg-0b7a), two
claims that were refuted (mg-5210 §2.3, mg-d03b §4.3), and two signed evaluations that
point away (mg-555b §10.3). **No sign-sensitive member that is ours points toward
positivity.** §6.

**7. One thing found while looking, and it is not from this generator.** The corpus's
strongest *ours, proved, sign-sensitive* statement is not a comparison against the fixed
square at all — it is Theorem `thm:deficit` in `paper/positivity-obstruction.tex:1147`, a
lower bound on $\lambda_{\min}$ of the archimedean form obtained from the Riemann–Siegel
theta. That paper's own house-rule section reads its table the same way: *"Every
sign-bearing row is an inequality about $\lambda_{\min}$ of the actual form, or the one
proved square at the archimedean place"* (`:2708-2709`). **If a generator is worth
investing in, that is the one that is already working** — and the trace comparison is a
special case of it, read through the identity. The paper is outside this ticket's stated
corpus and its eighteen-row table was spot-checked, not audited. §7.

---

## 0. What the test is, and the convention used

The house rule as the paper states it (`paper/positivity-obstruction.tex:703-705`):

> *Is the statement false for $-QW_\lambda$?* If not, it is sign-blind, and it cannot be
> evidence about the direction of an inequality however sharp it is.

Applied here as a **syntactic** operation: replace every occurrence of the symbol
$W$ (i.e. $W_\lambda$, $W_\infty$, $QW_\lambda$, $\sigma^{\rm arch}$ — whichever the
statement uses) by its negative, leave everything else alone, and ask whether the
resulting statement is still true. That is how `s3-sign-blindness.md` §3 applies it (item
(iv) is invariant "because $\asymp$ compares magnitudes"), how `signed-geometry-proposals.md`
§9 applies it, and how every closing section in the corpus applies it.

Two readings were checked against each other on every row where they could differ, and
they never did: (i) the syntactic one above, and (ii) the counterfactual one — *if the
Weil functional were $-W_\infty$ and everything else were unchanged, would this
measurement come out the same?* The downgrades of §3 hold under both, and §2 says why.

Vocabulary as in `semilocal-gap.md` §0: **proved** / **announced** / **numerical** /
**ours**.

---

## 1. The generator's two halves

### 1.1 Half A — the trace does not move. Established.

**Statement.** $\operatorname{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)$ is unchanged by
$W_\lambda\to-W_\lambda$.

**Proof 1 (syntactic).** $\mathbf S$ is the orthogonal projection of
$L^2(\mathbb R)_{\rm ev}$ onto the Sonin space $S(1,1)$ — the even $L^2$ functions
vanishing together with their Fourier transform on $[-1,1]$ (`weil-compo.tex:1050`, Def.
`defnsonine`, via `sonin-trace.md` §1.1). $\vartheta$ is the scaling action,
$(\vartheta(\lambda)\xi)(v)=\lambda^{-1/2}\xi(\lambda^{-1}v)$ (`:917`). Neither is a
function of $W$: the first is a closed subspace and its projection, the second is a
unitary representation of $\mathbb R_+^*$, and the trace is the composite of those two
with a Hilbert–Schmidt norm. That is exactly the hypothesis of mg-8599's lemma
(`signed-geometry-proposals.md` §2.1) — *a quantity built from closed subspaces,
orthogonal projections, norms and scalar functionals is invariant under
$W_\lambda\mapsto-W_\lambda$, because none of those objects is a function of
$W_\lambda$* — so the substitution does not reach it. $\square$

**Proof 2 (structural, and it says more).** $\mathbf S=\mathbf S^*=\mathbf S^2$, so
$$\operatorname{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)
=\lVert\mathbf S\vartheta(g)^*\rVert_{HS}^2\ \ge\ 0 ,$$
`semilocal-gap.md` §1.2, which is Connes–Consani's own one-sentence account of where the
archimedean sign comes from (`weil-compo.tex:86`). This is stronger than invariance under
one substitution: the quantity is non-negative for *every* $g$, under every substitution
that acts on $W$ alone, with no support condition and no vanishing condition. mg-5210's
CHECK 2 is the instrument pointed at exactly this and it is what caught that note's
factor-of-two trap (`sonin-trace.md` §7). $\square$

**Neither proof is the intuition the roadmap gives** ("manifestly a square"). The square
is Proof 2 and it establishes positivity, not invariance; the invariance is Proof 1 and it
needs no square. The two facts are separate and they do different jobs — §1.4.

### 1.2 Half B — $W_\infty$ does move. Established.

The substitution acts non-trivially on $W_\infty$ iff $W_\infty\not\equiv0$. It is not:
mg-555b's explicit witness (`semilocal-gap.md` §10.3) is
$f(x)=\cos(\pi x/L)+\kappa\cos(3\pi x/L)$ on $[-L/2,L/2]$ with $\kappa$ fixed by
$\widehat f(\pm i/2)=0$, evaluated by three one-dimensional quadratures with no matrix
and no eigenvalue; it crosses zero at $\mu=3.5581$ and is $-0.646$ at $\mu=4.0552$
against $\lVert f\rVert^2=6.48$. So $W_\infty$ takes a strictly negative value on an
explicit function, and (below the crossing) a strictly positive one. **Both figures are
mg-555b's, quoted, not re-derived here.**

### 1.3 So the ticket's stop condition is not met

Half A holds, so the slice proceeds. **But the roadmap's conclusion does not follow from
the two halves**, and §2 shows it is false. The inference "the trace is fixed, $W_\infty$
flips, so the sign of the difference flips" (`sonin-trace.md:350`) is self-contradicting:
precisely because $\operatorname{Tr}$ does *not* move, the difference does not negate.
$W_\infty-\operatorname{Tr}$ becomes $-W_\infty-\operatorname{Tr}$, which is not
$-(W_\infty-\operatorname{Tr})$.

### 1.4 The load-bearing fact is a third one, and it is measured

Every classification in §3 turns on one of two auxiliary facts, and the strict ones are
not proved in this corpus:

- **(P)** $\operatorname{Tr}(g_0)>0$ for some admissible $g_0$. Needed for every
  *sign-sensitive* verdict on a comparison. Available as: the floor $\min S$ per unit
  $\lVert g\rVert^2$ is $3.72\text{e-}1,\ 3.77\text{e-}2,\ 2.55\text{e-}3,\
  9.41\text{e-}4,\ 1.49\text{e-}4$ at $\mu=1.2,1.5,2,2.271,3$ (`sonin-trace.md` §3(b),
  mg-5210, **numerical, ours, and mg-5210 §8 records the combination as not
  independently anchored**). Proof 2 above gives only $\ge0$.
- **(W)** $W_\infty(g_1)\ge0$ for some $g_1$ in the set quantified over. Needed for every
  *sign-blind* verdict on a failure statement. This one **is** proved: Theorem 1 gives
  $W_\infty(g\star g^*)\ge\operatorname{Tr}\ge0$ on the codimension-two subspace at
  $\mu\le2$, and a test function admissible at $\mu_1$ is admissible at every $\mu_2>\mu_1$
  by extension by zero (mg-0b7a §3.2's monotonicity lemma). Unconditioned, mg-5210's
  Bottom-line table supplies it directly: $W_\infty$ on `witness` is
  $1.947,\ 1.147,\ 0.610,\ 0.441,\ 0.146$ at $\mu=1.2,1.5,2,2.271,3$ — positive at every
  tabulated $\mu$, and the $\mu=1.2$ vector serves at every larger $\mu$ by the same
  extension.

**So the corpus's sign-sensitive verdicts rest on a measured strict positivity, and its
sign-blind verdicts rest on a theorem.** That asymmetry is worth carrying: if (P) failed
— if $\operatorname{Tr}$ vanished identically on the conditioned subspace — every
comparison in the family would collapse to a statement about $W_\infty\ge0$ with no trace
in it, and the generator would have no content whatever.

---

## 2. The quantifier, and why mg-5210 §6 is sign-blind

### 2.1 The instrument, stated as a lemma

Let $T$ be any quantity the substitution does not move ($\operatorname{Tr}$, $E$,
$\epsilon$, a norm, $1-\chi_4$), with $T\ge0$.

> **(a) Assertion.** $\Sigma=\ \forall g\in X:\ W(g)\ge T(g)$. If $\Sigma$ is true and
> some $g_0\in X$ has $T(g_0)>0$, then $\Sigma(-W)$ is **false**: it would give
> $-W(g_0)\ge T(g_0)>0$, i.e. $W(g_0)<0$, while $\Sigma$ gives $W(g_0)\ge T(g_0)>0$.
> **Sign-sensitive.**
>
> **(b) Denial.** $\Sigma=\ \exists g\in X:\ W(g)<T(g)$. If some $g_1\in X$ has
> $W(g_1)\ge0$ and $T(g_1)>0$, then $\Sigma(-W)$ is **true**, witnessed at $g_1$:
> $-W(g_1)\le0<T(g_1)$. **Sign-blind** — both $\Sigma$ and $\Sigma(-W)$ hold.
>
> **(c) Identity.** $\Sigma=\ T_1=W+T_2$. Then $\Sigma\wedge\Sigma(-W)\Rightarrow
> W\equiv0$. **Sign-sensitive** unless $W\equiv0$.
>
> **(d) Magnitude.** $W$ occurring only through $|W|$, $\lVert W\rVert$ or $\asymp$:
> **sign-blind**, by inspection.

(a) and (b) are the same comparison, asserted and denied, and they have opposite
verdicts. That is the whole of the finding.

### 2.2 Applied to the statement the slice was dispatched on

mg-5210 §6, `sonin-trace.md:124-131` and its house-rule row at `:350`:

> *Before the two vanishing conditions are imposed, the gap
> $W_\infty-\operatorname{Tr}$ is negative on some direction at every $\mu\ge1.2$,
> including $\mu=2$, inside the theorem's own support range.*

That is $\exists g:\ W_\infty(g)<\operatorname{Tr}(g)$ — case (b). Substituted:
$\exists g:\ -W_\infty(g)<\operatorname{Tr}(g)$. **True**, and the witness is in mg-5210's
own Bottom-line table: at $\mu=1.2$, `witness` has $W_\infty=1.947$ and
$\operatorname{Tr}=1.913$, so $-W_\infty-\operatorname{Tr}=-3.86<0$; the same vector
serves at every $\mu\ge1.2$ by extension by zero. **The statement is sign-blind.**

The counterfactual reading agrees. If the Weil functional were $-W_\infty$ with
everything else fixed, would the measurement "the gap is negative on some direction" still
be made? Yes: the gap would be $-W_\infty-\operatorname{Tr}$, and it is negative wherever
$W_\infty>-\operatorname{Tr}$, which includes every direction on which the corpus has
recorded a positive $W_\infty$.

**What is sign-sensitive nearby, and this is the constructive half.** The *measurement*
behind the statement is sign-sensitive even though the statement is not: at $\mu=2$, on
the minimising direction of $W_\infty$, the corpus records $W_\infty=-1.29$ against
$\operatorname{Tr}=0.232$ (`sonin-trace.md` §3(a), mg-5210). "There is an explicit
direction on which $W_\infty=-1.29$" is a signed **evaluation** — case (c)-like, false for
$-W$ — and it is mechanism 1 of `s3-sign-blindness.md:192` ("a signed evaluation"). The
corpus reported the existential consequence and lost the sign-sensitivity in the
weakening. **Restating the corpus's failure claims as evaluations rather than as
existentials would move several of them back across the line at zero cost, and would not
add a single new number.** That is the only cheap enlargement of the family this pass
found.

### 2.3 Why the same trap catches the whole "it is false past $\mu_c$" row

$\mu_c(k)$ is defined by the sign of $-E$ and is a threshold (mg-0b7a §3.2). Every
"$\mu_c$" result therefore has two halves:

| half | shape | verdict |
|---|---|---|
| the conclusion **holds** for $\mu\le\mu_c$ | (a) | sign-sensitive |
| the conclusion **is false** for $\mu>\mu_c$ | (b) | **sign-blind** |

and the corpus marks both **YES** (`sonin-margin.md:389-390`, `sonin-ceiling.md:535-536`).
The second is (b) with $g_1$ supplied by Theorem 1 and extension by zero. **The sting is
that these are the wrong way round for the corpus's own provenance:** mg-0b7a Bottom-line
item 8 says the *holds* half is unproved everywhere (truncation raises eigenvalues, so
only the failure certifies), while the *fails* half is the one with a variational
certificate. So in every $\mu_c$ pair, the sign-sensitive half is the numerical one and
the proved half is sign-blind.

---

## 3. The classification — 41 statements, applied one by one

Scope is the five notes the ticket names. Each note's closing house-rule section is a
list of its own load-bearing statements; those lists are what is enumerated here, and
they are the corpus's own choice of what counts as a statement. **Denominator: 41
statements examined** (7 + 9 + 9 + 10 + 6). One of the 41 (`signed-geometry` §2.1's
lemma) is a statement *about* the invariance and is marked n/a by its own note; 40 carry
a verdict.

Notation: **S** = sign-sensitive, **B** = sign-blind. "corpus" is the verdict printed in
that note; "here" is the verdict of the substitution applied afresh.

### 3.1 `sonin-trace.md` §6 — 7 statements

| # | statement | corpus | here | reason |
|---|---|---|---|---|
| T1 | §1: $\operatorname{tr}(\vartheta(f)\mathbf S)=W_\infty(f)+E(f)$ | S | **S** | case (c). Connes–Consani's, Thm `devil` |
| T2 | §2.2: $-E\ge0$ on the codim-2 subspace, $\mu\le3$ | B | **B** | $E$ does not mention $W$. See §4 — it is equivalent, through Theorem `devil`, to the sign-sensitive S1 |
| T3 | §3: the trace's size, every column headed $S$ | B | **B** | magnitudes of an invariant |
| T4 | §6: unconditioned, $W_\infty-\operatorname{Tr}<0$ on some direction, every $\mu\ge1.2$ | S | **B** | case (b). §2.2 — **downgrade** |
| T5 | §2.3 (retired): on the minimising direction $\operatorname{Tr}$ is essentially all of $W_\infty$ | S | **S** | asserts $W_\infty\approx\operatorname{Tr}>0$; case (a). Refuted anyway by mg-d03b |
| T6 | §4: the floor decays at $-3.06$, against $-4\pi$ | B | **B** | |
| T7 | §5: the two bandwidths | B | **B** | |

### 3.2 `sonin-margin.md` §6 — 9 statements

| # | statement | corpus | here | reason |
|---|---|---|---|---|
| M1 | §2: the conditioned column is $\epsilon'(1^+)L^2/2\pi^2N^2$; no margin | B | **B** | |
| M2 | §2.3: the minimiser is the top cosine mode | B | **B** | |
| M3 | §3: `conditions()` row 1 was not $\hat g(i/2)$ | B | **B** | |
| M4 | §1.2/§5: $\hat\epsilon(0)=5.37>0$, $t_0=6.2918$, the tail law | B | **B** | about $\epsilon$ |
| M5 | §4.1: the inertia table and its $N$-stability | B | **B** | about $-E$ |
| M6 | §4.2: Theorem 1's conclusion holds to $\mu=6.17$ *(even block; $2.754$, mg-0b7a)* | S | **S** | case (a) |
| M7 | §4.2: it is false from $\mu=6.17$ on | S | **B** | case (b) — **downgrade** |
| M8 | §4.3: at $\mu\le2$ one condition already gives the inequality | S | **S** | case (a). Refuted by mg-0b7a |
| M9 | §4.3: unconditioned the inequality fails at every $\mu$ | S | **B** | = T4 — **downgrade** |

### 3.3 `sonin-ceiling.md` §6 — 9 statements

| # | statement | corpus | here | reason |
|---|---|---|---|---|
| C1 | §1: $\epsilon(\rho)\sqrt\rho\to1$ | B | **B** | |
| C2 | §2: $\hat\epsilon(0)=5.3722>0$ in closed form | B | **B** | |
| C3 | §3: **Theorem A** | B | **B** | about $E$ only, as that note says |
| C4 | §3.2: $-E$ indefinite at codim 0; $\mu_c(k)$ is a threshold | B | **B** | |
| C5 | §4: $\log\mu_c(k)\le\Lambda(k)$, $\Lambda(k)\sim\pi k/t_0$ | B | **B** | $\mu_c$ is defined by the sign of $-E$ |
| C6 | §5.1: $E$ splits even + odd; the corpus's basis is the even block | B | **B** | |
| C7 | §5.3: the conclusion holds to $\mu=2.754$, a factor $1.38$ | S | **S** | case (a) |
| C8 | §5.3: it is false from $\mu=2.754$ on | S | **B** | case (b) — **downgrade** |
| C9 | §5.3: at $\mu\le2$ one condition is NOT enough | S | **B** | this is the *denial* of M8; case (b) — **downgrade** |

C9 is the sharpest instance of the asymmetry. M8 ("one condition suffices") and C9 ("one
condition does not suffice") are a claim and its refutation, and they do not have the same
verdict: the claim is sign-sensitive, the refutation is not. A refutation of a
sign-sensitive statement is generally sign-blind, which is the general form of item 2.

### 3.4 `semilocal-gap.md` §6 and §10.3 — 10 statements

| # | statement | corpus | here | reason |
|---|---|---|---|---|
| S1 | §1.2: the sign comes from $\operatorname{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)\ge0$, i.e. Theorem 1 | S | **S** | case (a); the note's own reasoning is correct and is the same argument as (a) |
| S2 | §1.1 I7/I9: $\epsilon'(1^+)=+22.9965$, so $\mathcal N_I$ is negative up to finitely many directions | S | **B** | no $W$ occurs. The note classifies the *role* ("flip the sign and the argument gives the opposite conclusion") — **downgrade** |
| S3 | §1.3: $\lambda_{\max}=1.05158>1$ forces a condition; $b(a+c)\le a(b+c)\lvert\langle\zeta\mid\xi_0\rangle\rvert^2$ is not symmetric in the sign of $b$ | S | **B** | statements about $\mathcal K_I$'s spectrum and an overlap; no $W$ — **downgrade** |
| S4 | §3.3: the archimedean contribution ceases to be positive past $\mu=2.271$, and positivity is restored by the prime 2 | S | **S** (compound) | "positive below $2.271$" and "restored" are case (a); "ceases past" is case (b) and is blind. The row is sign-sensitive **as a conjunction** — see §3.6 |
| S5 | §3.2: $V(n)\sim-V(n)$, the prime term is exactly indefinite | B | **B** | |
| S6 | §2: I2/I3/I4 are place-independent | B | **B** | |
| S7 | corpus: `start.tex:39`, $QW_\lambda(Eh_\lambda)\asymp1-\chi_4$ | B | **B** | case (d) |
| S8 | corpus: `start.tex:361-368`, $QW_\lambda(Eh_\lambda)=C_\lambda(1-\chi_4)+o(\cdot)$ with $0<c\le C_\lambda\le C$ | S | **S** | asserts $C_\lambda>0$; case (a) |
| S9 | §10.3: $\theta'<0$ on $\lvert t\rvert<6.2898$ — the density of $W_\infty$ is negative near $t=0$ | S | **S** | a signed statement about $W_\infty$'s own density |
| S10 | §10.3: the witness's value is $-0.646$, not $+0.646$ | S | **S** | a signed evaluation |

### 3.5 `signed-geometry-proposals.md` §9 — 6 statements

| # | statement | corpus | here | reason |
|---|---|---|---|---|
| G1 | C1: $W(f\star f^*)\ge0$ on the Schwartz space of $C_{\mathbb Q}$ | S | **S** | case (a). It is Weil positivity — the open problem |
| G2 | C2: $W_S(f\star f^*)\ge0$ on the Sonin space | S | **S** | case (a); at the archimedean place it is Theorem 1 (= S1) |
| G3 | C3: the leafwise pairing is polarised, $\operatorname{Tr}(\phi\phi^\dagger)>0$ | S | **conditional** | the statement mentions no $W$; it is sign-sensitive only under an identification with $W$ that requires a space "not known to exist" (that note's §5). Sensitive-if-instantiated, and not instantiated |
| G4 | C4: $\lambda(x,x)\in\mathbb Q/\mathbb Z$ | B | **B** | |
| G5 | C5: $\eta(M,\alpha)$ is a Dedekind sum | B | **B** | |
| G6 | §2.1 lemma | n/a | **n/a** | a statement about the invariance |

### 3.6 Counts, with the denominator

| | count |
|---|---|
| statements examined | **41** |
| carrying a verdict (excludes G6) | 40 |
| marked sign-sensitive by the corpus | 20 |
| **confirmed sign-sensitive here** | **12** (T1, T5, M6, M8, C7, S1, S4, S8, S9, S10, G1, G2) |
| **downgraded to sign-blind** | **7** (T4, M7, M9, C8, C9, S2, S3) |
| conditional / not instantiated | 1 (G3) |
| sign-blind, agreeing with the corpus | 20 |

**The 7 downgrades fall into two kinds.** Five (T4, M7, M9, C8, C9) are case (b): a
comparison denied rather than asserted. Two (S2, S3) mention no $W$ at all and were
classified by the argument they feed. `sonin-margin.md` §6 closes with exactly this
warning — *"the house rule sorts statements, not errors"* — and S2/S3 are that warning
one level up: the rule sorts statements, not roles either.

**And one note on compounds (S4).** A conjunction is false whenever any conjunct is, so
bundling a sign-blind claim with a sign-sensitive one produces a row that is correctly
marked sign-sensitive while the interesting half is blind. S4 is that shape, and so is
the paper's `sec:noplacewise` row (`paper/positivity-obstruction.tex:2596-2600`), which
bundles "positivity fails past $\mu=2.2710$" (blind) with the witness value $-0.646$
(sensitive). **The verdict then licenses the blind half.** Applying the rule to atomic
statements is the repair, and it costs nothing.

---

## 4. What the rule measures — presentations, not content

$-E\ge0$ on $X$ (T2, sign-blind) and $W_\infty\ge\operatorname{Tr}$ on $X$ (S1,
sign-sensitive) are the same claim: Theorem `devil` is the identity
$\operatorname{Tr}=W_\infty+E$ that carries one to the other, and it is a theorem
(`weil-compo.tex:1132`). So the house rule assigns opposite verdicts to two presentations
of one statement.

That is not a defect in the rule — it is what the rule is for. $W\mapsto-W$ is not an
automorphism of the ambient mathematics (it does not preserve the identity), so it cannot
be a test on content; it is a test on whether *this sentence, as written*, pins the sign
of $W$. That is exactly the question "can this be evidence about the direction of an
inequality", and the answer is properly a property of the sentence.

**What follows is about the census, not the rule.** A count of sign-sensitive statements
measures how many sentences in a note are written with $W$ on the outside. *"Three
statements that are not sign-blind, where the corpus had none"* (`sonin-trace.md:355`)
and *"Four statements that are not sign-blind, where mg-5210 produced three"*
(`sonin-margin.md:394`) are counts of presentations, and the corpus has been reading them
as a progress metric. §3 corrects them to **two** and **two** (and `sonin-ceiling.md`'s
three to **one**); they were never the metric they looked like. **A rewrite through a true identity cannot add content, and this rule cannot tell a
rewrite from a result.**

The residue that is *not* a rewrite: the transfer of §5.

---

## 5. The generator, restated honestly, and its polarity

Strip the presentation question away and what the generator really is:

> **Transfer.** $\operatorname{Tr}=W_\infty+E$ (identity, proved) together with
> $\operatorname{Tr}\ge0$ (the square) converts a statement about the sign-blind form
> $-E$ into a statement about the sign of $W_\infty$.

This is genuine — it is how Connes–Consani's theorem works, and §1.4(P) is where it
touches the ground. It has a polarity, and the polarity is the finding:

| input, about $E$ alone | output, about $W_\infty$ | verdict |
|---|---|---|
| $-E\ge0$ on $X$ (a **lower** bound) | $W_\infty\ge\operatorname{Tr}>0$ on $X$ | sign-sensitive; points toward positivity |
| $-E$ indefinite on $X$ | $\exists g\in X: W_\infty(g)<\operatorname{Tr}(g)$ | sign-blind; points nowhere |

**Everything this corpus has proved for itself is of the second kind.** Theorem A
(mg-0b7a §3.1: for every $k$ there is a finite $L$ past which $E$ has a positive
direction in $\{\hat g(ij/2)=0\}$); the inertia counts (mg-d03b §4.1, mg-0b7a §5.3);
$\log\mu_c(k)\le\Lambda(k)$ with $\Lambda(k)/k\to\pi/t_0$ (mg-0b7a §4.1); the codim-0
indefiniteness and the threshold lemma (§3.2); the even/odd splitting (§5.1). Each is a
theorem, each is sign-blind, and each transfers to a sign-blind conclusion.

And the first kind is unavailable by that corpus's own accounting. mg-0b7a Bottom-line
item 8: *"Every $\mu_c$ in this corpus, mg-d03b's and this note's, is an upper bound on a
threshold whose lower half is unproved"* — truncation raises eigenvalues, so a negative
truncated eigenvalue certifies a negative one for the full form and never the converse.
**The input the positivity-pointing half of the transfer needs is precisely the one the
corpus has never had, and knows it has never had.**

That is a better explanation of five months of obstructions than "this corpus has been
good at proving things do not work". The instrument has a direction, and it is pointed at
the half that certifies failure.

---

## 6. Does any sign-sensitive member point toward positivity?

### 6.1 What "points toward" is taken to mean

A member points toward positivity if all three hold:

- **P1** it *asserts* $W\ge0$, or $W\ge$ a strictly positive invariant, on a set of test
  functions relevant to Weil's criterion — not that such an assertion fails, and not a
  magnitude;
- **P2** it is not a restatement of the open problem (G1 and S8 fail here: "$W(f\star
  f^*)\ge0$ for all $f$" and "$C_\lambda\ge c>0$" are what is to be proved);
- **P3** it is either ours, or it extends something in a direction Weil's criterion needs
  — more places, or the full test space — as opposed to a direction already known to be
  capped.

### 6.2 The twelve, sorted

| member | asserts positivity? | whose | direction |
|---|---|---|---|
| T1 identity | no — an equation, no direction | Connes–Consani | — |
| T5 | yes, and **refuted** (mg-d03b: no such direction exists) | ours | — |
| M6 / C7: conclusion holds to $\mu=2.754$ | **yes** | ours (numerical) | $\mu$, which Theorem A proves is capped at every codimension |
| M8: one condition suffices at $\mu\le2$ | yes, and **refuted** (mg-0b7a: $\mu_c(1)=1.771<2$) | ours | — |
| S1 / G2: Theorem 1 | **yes** | Connes–Consani | the base that Theorem A caps |
| S4: positivity restored by the prime 2 | **yes** | Connes–Consani, reproduced by mg-555b | **places** — the direction the criterion needs |
| S8: $C_\lambda\ge c>0$ | yes, but is the open problem (fails P2) | Daniel, `start.tex`, unproved | — |
| S9: $\theta'<0$ near $t=0$ | no — the density is hostile | standard | away |
| S10: the witness is $-0.646$ | no — a negative evaluation | ours | away |
| G1: $W(f\star f^*)\ge0$ | yes, but is the open problem (fails P2) | Weil / Connes | — |

### 6.3 The answer

**No sign-sensitive member that is ours points toward positivity.**

Two members point toward positivity and pass P1–P3, and **both are Connes–Consani's**:
Theorem 1 (S1/G2), and "positivity is restored by adding the prime 2" (S4) — the only
member pointing in the direction the criterion actually needs, and the one whose required
theorem `semilocal-gap.md` item 4 identifies as being about *cancellation between places*,
which nobody has.

The corpus's own four contributions to the family are:

1. $\mu_c(2)=2.754$ — Theorem 1's conclusion survives $38\%$ past its stated hypothesis
   (mg-0b7a §5.3). This is the one ours-and-positivity-pointing member, and it fails P3
   twice: the direction it extends is $\mu$, which Theorem A proves is capped at every
   codimension, and the half of it that points toward positivity is the numerical,
   upper-bound half (§5).
2. mg-5210 §2.3's margin — **refuted** by mg-d03b.
3. mg-d03b §4.3's "one condition suffices" — **refuted** by mg-0b7a.
4. mg-555b §10.3's signed evaluations — they point **away**.

So the ticket's stated expectation is met, and it is met with a mechanism rather than a
tally: **the family is real, it is smaller than the corpus recorded (12 of a claimed 20,
out of 41 examined), and its positivity-pointing members are all instances of a theorem
this corpus did not prove, evaluated further out.** Reported as the result of the method,
which is what it is: the substitution test found this in a reading pass, with no grid, no
script, and no number that was not already merged.

---

## 7. One thing found while looking — and it is a different generator

Outside the five notes, `paper/positivity-obstruction.tex` §`sec:houserule` carries its
own eighteen-row table. It was **spot-checked, not audited**, and two things in it bear
directly on the question this ticket asks.

**(i) It contains the corpus's only *ours, proved, sign-sensitive* statement.**
Theorem `thm:deficit` (`:1147`): for every $\mu$ and every unit $f$ in the even sector,
$\sigma^{\rm arch}(f,f)\ge2\vartheta'(0)\lVert f\rVert^2$, hence
$D(\mu)<-2\vartheta'(0)=5.3721834192\ldots$. Marked *ours*, *proved given* Connes–Consani
Prop. `Hilbert`, and its proof is three one-line facts about the Riemann–Siegel theta. It
is sign-sensitive by case (a) and it does **not** come from the trace comparison — no
$\operatorname{Tr}$, no Sonin space, no $E$. Its own paper reports that the margin it
establishes does not decide the question: on the direction that actually decides
positivity, the archimedean contribution is positive and the primes are the threat
(`:1301-1308`), so "the deficit-versus-repair columns are not the two sides of the
balance". **The figures in this paragraph are the paper's, quoted, not re-derived.**

**(ii) The paper has already named the productive generator, in one sentence.**
`:2708-2709`: *"Every sign-bearing row is an inequality about $\lambda_{\min}$ of the
actual form, or the one proved square at the archimedean place."* That is the general
rule of which the trace comparison is a special case — Theorem 1 read through the identity
is $\lambda_{\min}(-E)\ge0$. If the programme wants a generator to invest in, that is the
one already operating, it has one proved ours-member, and it does not route through the
identity.

The paper also anticipates §2's quantifier trap, for one statement, in its closing
warnings (`:2720-2725`): *"$s(\mu)$ is governed by $1-\chi_2$" is by itself invariant
under $W\mapsto-W$; it is sign-bearing only as "$0<s(\mu)\le\cdots$", and the left half of
that is RH.* What §2 adds is that the same trap applies to the *failure* direction, which
the paper's table does not separate (its `sec:noplacewise` row bundles them), and that
five rows of the notes fell into it.

**Not claimed:** that the paper's table is otherwise correct. It was not audited, and a
census of it is a separate ticket.

---

## 8. Sites, for whoever owns the repair

This ticket's acceptance is one note and nothing else touched, so nothing below is
annotated in place. The seven downgrades are each one line, and the corpus's convention
is to annotate rather than rewrite:

| site | row | repair |
|---|---|---|
| `sonin-trace.md:124-131` and `:350` | T4 | the reason given ("the sign of the difference flips") is self-contradicting; the verdict is B. The Bottom line's *"first statement in this corpus that is not sign-blind"* goes with it |
| `sonin-margin.md:390` | M7 | B |
| `sonin-margin.md:392` | M9 | B (it is T4, re-verified) |
| `sonin-ceiling.md:536` | C8 | B |
| `sonin-ceiling.md:537` | C9 | B — and it is the refutation of M8, which is S |
| `semilocal-gap.md:614-616` | S2 | B — no $W$ occurs |
| `semilocal-gap.md:617-619` | S3 | B — no $W$ occurs |
| `docs/roadmap.md:87-88` | the generator | *"every statement that compares the moving quantity to the fixed square is sign-sensitive, automatically"* — false as stated; §2.1(a)/(b) is the corrected form |
| `docs/roadmap.md:149ff` | "The first statements in this corpus that are not sign-blind" | the count in that section inherits T4 |

Also on the list, and cheap: **restate the failure claims as signed evaluations** (§2.2).
"There is an explicit direction on which $W_\infty=-1.29$ at $\mu=2$" is sign-sensitive
where "the gap is negative on some direction" is not, and the number is already merged.

---

## 9. The house rule, applied to this note

Almost everything above is a statement *about* the substitution, so the rule returns n/a
on it, exactly as it does for `signed-geometry-proposals.md` §2.1's lemma row. Three
first-order statements are used and each is quoted, not derived here:

| statement | false for $-W_\lambda$? |
|---|---|
| §1.1: $\operatorname{Tr}$ is invariant, and $=\lVert\mathbf S\vartheta(g)^*\rVert_{HS}^2\ge0$ | **no.** Sign-blind — and that is the point of it |
| §1.4(P): $\operatorname{Tr}>0$ on some admissible direction (mg-5210's floors) | no. Sign-blind |
| §1.4(W): $W_\infty\ge0$ somewhere — Theorem 1, and mg-5210's `witness` column | **yes**, case (a). It is Theorem 1, quoted |
| §1.2: $W_\infty(f)=-0.646$ on mg-555b's explicit $f$ | **yes**. A signed evaluation, quoted from `semilocal-gap.md` §10.3 |
| §3, §6: every classification verdict | n/a — statements about the substitution |

**So this note's own content is sign-blind, and it is a note about sign-blindness.** It
adds no statement that is false for $-W_\lambda$, and it is not offered as progress
towards positivity.

---

## 10. Provenance, and what is unverified

**Method.** The substitution was applied by hand to each of the 41 statements listed in
§3, taken from the closing house-rule section of each of the five notes the ticket names.
Two readings of the substitution (syntactic and counterfactual, §0) were checked against
each other on all seven downgrades and agree on all seven.

**No computation was performed.** Every number quoted carries its originating ticket:
mg-5210 (`sonin-trace.md`: the witness column, the floors, the $-1.29$ at $\mu=2$),
mg-d03b (`sonin-margin.md`: $\mu_c$ even block, the truncation order), mg-0b7a
(`sonin-ceiling.md`: $\mu_c(1..4)=1.771,\,2.754,\,4.140,\,6.024$, Theorem A,
$\hat\epsilon(0)=5.3722$, $t_0=6.29177$), mg-555b (`semilocal-gap.md` §10: the witness,
$-0.646$, $\mu=3.5581$, $\theta'$'s first zero at $6.2898336$), mg-03f0
(`semilocal-gap.md` §1.3's three constants), mg-8599 (`signed-geometry-proposals.md`
§2.1's lemma), and the paper's `thm:deficit` and §`sec:thirddirection` figures, which are
the paper's.

**Established here.**

- §1.1, both proofs of Half A. The first is an application of mg-8599's lemma; the second
  is `semilocal-gap.md` §1.2's identity, restated. Neither is new mathematics and neither
  is claimed to be.
- §2.1's four cases, which are the instrument. They are elementary and each proof is one
  line, given in place.
- §3's 41 verdicts, and the seven disagreements.
- §4's observation that the rule is not invariant under rewriting through a true identity.
- §5's polarity statement.

**Rests on something measured rather than proved.** Every sign-sensitive verdict on a
comparison needs §1.4(P) — $\operatorname{Tr}>0$ on some admissible direction — and the
corpus has that numerically (mg-5210 §3(b)) and not as a theorem. mg-5210 §8 already
records that the combination behind those floors has one non-trivial external check and
that a uniform multiplicative error would not be caught. **A proof that
$\operatorname{Tr}$ is strictly positive on the conditioned subspace would put §3's
sign-sensitive column on a theorem; nothing here supplies one.** By contrast the
sign-blind verdicts need only §1.4(W), which Theorem 1 supplies.

**Not attempted.** Any repair in place — the acceptance is one note (§8 lists the sites).
Any edit to `start.tex`, `s3.tex` or `paper/`. Any audit of the paper's own house-rule
table beyond the two rows of §7. Any new statement in the family: §2.2 says how the
family could be enlarged for free, and does not do it, because doing it is a rewrite of
other people's notes.

**Open, and it is the one question this pass could not answer from the merged corpus.**
Is there *any* route in this corpus to a lower bound on $-E$ — the input §5's transfer
needs? mg-0b7a item 8 says nothing here touches it, and Theorem A says the answer must be
$\mu$-bounded. Absent that input, the generator can produce sign-sensitive statements
only by rewriting Connes–Consani's theorem, and this pass found no member that does
anything else.
