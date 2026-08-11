# A geometry that can sign the Weil form — ranked proposals

Work item mg-8599. Prior work, not re-derived here:
[`s3-reduction-audit.md`](s3-reduction-audit.md) (mg-aedf) and
[`s3-sign-blindness.md`](s3-sign-blindness.md) (mg-8d74). This note assumes both.

Nothing in `start.tex` or `s3.tex` was edited. References are by line.

*Citations unverified — like the two prior notes, this one was written offline. The
load-bearing external facts are flagged in §8 and should be checked before any of
this is used in writing.*

---

## Bottom line

The request was a natural alternative geometry to $S^3$ in which the sign is
preserved in the arithmetic and flows through to the geometry. The answer has
three parts, and the first is the one that matters.

**1. The thing that must be transported is not a manifold. It is a
$(\star,{}^*)$ — a product and an involution.** Every case in which geometry is
known to sign a Weil form — Hodge index on $C\times C$, Rosati positivity on
$\operatorname{End}(\mathrm{Jac})$, Riemann bilinear relations for a polarised
weight-1 Hodge structure, positivity of a state on a $C^*$-algebra — is the same
statement: *there is an involution $\dagger$ and $\operatorname{Tr}(x\,x^\dagger)>0$.*
A signature on middle cohomology is one incarnation of that, not the general form.
This reframes mg-8d74's §6: $S^3$'s problem is **not primarily its dimension**. §2
below states it as a lemma — a dictionary whose analysis column contains only
subspaces, projections, norms and scalar functionals is sign-blind *whatever the
dimension of its geometry column*, because none of those objects mentions
$W_\lambda$. A 4-dimensional replacement built the same way would fail identically.
This is a falsifiable prediction about every future proposal, including mine.

**2. The arithmetic sign is already named, and it is the involution.** On the
idele class group the Weil form is $W(f\star f^*)$ with
$$f^*(u)=\overline{f(u^{-1})}/|u| ,\qquad \widehat{f^*}(s)=\overline{\hat f(1-\bar s)} .$$
That involution **is** the functional equation $s\mapsto 1-\bar s$. Weil positivity
is then the single statement that the spectral sum
$\sum_\rho \hat f(\rho)\overline{\hat f(1-\bar\rho)}$ is a sum of
$|\hat f(\rho)|^2$ — which happens exactly when $\rho=1-\bar\rho$, i.e. on the
critical line. **The sign is not something to be found in a geometry; it is
something a geometry must be able to carry, and carrying it means having $\star$
and ${}^*$.** The dictionary at `start.tex:100-127` has neither: six rows, all
subspaces and projections, no product and no adjoint. That is a sharper diagnosis
than "no middle cohomology", and it explains why mg-8d74's invariance argument came
out the way it did.

**3. Ranked candidates. Two carry the sign, two are decoration, and I say which.**

| # | candidate | signature lives in | passes mg-8d74 test? | verdict |
|---|---|---|---|---|
| **C1** | square of the adele class space / scaling site over $\mathbb F_1$ (Connes–Consani) | trace form on correspondences; Hodge-index analogue | **yes** | **Structurally the answer. Not a reduction — it is the open problem, correctly sited.** |
| **C2** | semilocal / archimedean Sonin space (Connes–Consani 2021), prolates as the bridge | positivity of a Hermitian form by factorisation ($W=A^*A$) | **yes** | **The only place a sign is actually *proved*. Actionable now, and cheap.** |
| **C3** | Deninger's foliated dynamical system | leafwise $H^1$, cup product + Hodge $\star$ = polarised weight-1 HS | **yes** | Right shape; the space is not known to exist. |
| **C4** | rational homology sphere $\leftrightarrow \operatorname{Spec}\mathcal O_K$, linking form | $\mathbb Q/\mathbb Z$-valued linking pairing | **no** | **Decoration** — explains why $S^3$, cannot sign a real number. |
| **C5** | 4-dimensional filling, $\eta$-invariant, Dedekind sums | signature of a filling / spectral asymmetry | **no** | **Decoration** — and killable more cheaply than mg-8d74 §6 did. |

**4. mg-8d74 §4's objection to candidate (a) is wrong as stated, and fixing it
lands on C1/C2.** The objection was that no *compact* group acts on the primes.
But positivity by averaging does not need compactness — Bochner's theorem is a
theorem about locally compact abelian groups. The group that acts on the primes is
the idele class group $C_{\mathbb Q}=\mathbb A^\times_{\mathbb Q}/\mathbb Q^\times$;
it is not compact, and it does not merely act on the primes, it is *built out of
them*. §6. The consequence is not a new mechanism: candidate (a), repaired, **is**
the Connes formulation. That is worth knowing precisely because it closes a route
that looked open.

---

## 1. The criteria, restated as a checklist

The work item fixes four. I add a fifth from mg-8d74 §7, because it is the cheapest
and it kills more candidates than the other four combined.

1. **Named, and natural** — what in the CCM/Connes setup *selects* it.
2. **Where the signature lives** — an even-dimensional space with a symmetric
   middle-dimensional form, or an honest substitute.
3. **The flow-through** — the map by which the arithmetic sign *becomes* the
   geometric one, named at least schematically.
4. **A falsifier.**
5. **The Davenport–Heilbronn test** (mg-8d74 §7) — an identifiable step that
   *fails* when the Euler product is removed.

And the self-test, applied at the end to my own candidates: **is any statement in
the proposal false for $-W_\lambda$?** If not, it has reproduced the defect.

---

## 2. What must be transported — a lemma, and why dimension is a symptom

### 2.1 The sign-blindness lemma

> **Lemma.** Let $D$ be a dictionary whose analysis-side entries are all of the
> following kinds: closed subspaces, orthogonal projections, norms of vectors, and
> scalar functionals of the test vector. Then every statement derivable from $D$
> alone is invariant under $W_\lambda\mapsto-W_\lambda$.
>
> *Proof.* None of those objects is a function of $W_\lambda$. $\square$

Trivial, and that is the point: mg-8d74's central result is a corollary of a fact
about the *form* of the dictionary, not about $S^3$. Check
`start.tex:100-127` against it row by row — global compact geometry / two
distinguished directions / geometric concentration / failure to remain in a sector
/ small boundary term / geometric projection. Analysis side: completed spectral
problem, two exceptional Weil directions, prolate concentration, time–band leakage,
$1-\chi_n$, $Q$. **Every entry is a subspace, a projection, a scale, or a
functional.** Six for six.

**Corollary (the prediction).** Replacing $S^3$ by *any* geometry, of *any*
dimension, and building the dictionary the same way, yields a sign-blind chain.
Adding a seventh row of the same kind changes nothing — which is
`s3-reduction-audit.md:321-322` arriving again by a different route.

**Contrapositive (the design rule).** To break the invariance, the dictionary needs
a row whose *analysis* side is a **product** or an **adjoint**. Those are the two
operations out of which "square" is built, and positivity is always a statement
about a cone of squares. Nothing else will do it, because nothing else can produce
a statement that is false for $-W_\lambda$.

This is why criterion 2 should be read at the level of *polarisation* rather than
*middle cohomology*. In each known case:

| setting | involution $\dagger$ | positivity |
|---|---|---|
| curve over $\mathbb F_q$ | transpose of a correspondence $Z\mapsto Z^t$ | $\operatorname{Tr}(Z\circ Z^t)>0$, from Hodge index / Castelnuovo |
| abelian variety | Rosati $x\mapsto x'$ | $\operatorname{Tr}(x x')>0$ |
| polarised weight-1 HS | complex conjugation on $H^1$ | Riemann bilinear relations |
| $C^*$-algebra | $a\mapsto a^*$ | $\varphi(a^*a)\ge0$ for a state |
| **Weil/Connes** | $f^*(u)=\overline{f(u^{-1})}/\lvert u\rvert$ | $W(f\star f^*)\ge0$ — **open** |

The middle-cohomology story is row 1 only. **The general requirement is an
involution and a positive trace.**

### 2.2 Why $S^3$, and why its dimension is a symptom rather than the disease

There is a genuine reason a 3-manifold — and specifically a homology 3-sphere —
turns up here, and the corpus does not state it. Under the arithmetic-topology
dictionary (Mazur, Mumford, Manin; developed by Morishita), $\operatorname{Spec}
\mathbb Z$ behaves like a closed oriented 3-manifold and primes like knots in it,
because $\operatorname{Spec}\mathcal O_K$ has étale cohomological dimension 3 with
duality. And $\operatorname{Spec}\mathbb Z$ corresponds to $S^3$ specifically
because $\mathbb Q$ has **no unramified extensions** (Minkowski), i.e.
$\pi_1^{\text{ét}}(\operatorname{Spec}\mathbb Z)=1$ — matching $\pi_1(S^3)=1$.

So the vanishing $H^1(S^3)=H^2(S^3)=0$ that mg-8d74 §6 identified as the obstruction
is *not an unlucky choice of manifold*. It is the topological shadow of class number
one and Minkowski's theorem. **Choosing a manifold with more cohomology means
choosing a different number field, not a better geometry** — and that is C4, which
fails for an independent reason (§7).

The real structural statement is this. Weil's proof needs a **surface**, obtained as
$C\times_{\mathbb F_q} C$. The product needs a *base*. $\operatorname{Spec}\mathbb Z$
is a final object: there is no base under it, so
$\operatorname{Spec}\mathbb Z\times\operatorname{Spec}\mathbb Z=\operatorname{Spec}
\mathbb Z$, and there is no surface. **Every serious candidate below is a way of
manufacturing a base** — $\mathbb F_1$ (C1), a finite set of places plus a cutoff
(C2), a flow (C3). That is the correct organising principle for the whole question,
and it predicts the ranking before any of the details are examined.

---

## 3. C1 — the square of the adele class space / scaling site

**Rank 1 structurally.** This is where the sign is, correctly sited. It is not a
reduction of anything.

**(1) The candidate, and why it is natural.** Connes' adele class space
$X=\mathbb A_{\mathbb Q}/\mathbb Q^\times$ with the scaling action of
$C_{\mathbb Q}$, and — for the Weil mechanism — the "square" of the associated
$\mathbb F_1$-geometry (Connes–Consani's arithmetic site and scaling site are the
concrete proposals for what that square should be a shadow of). Naturality is not
in question and is not a matter of taste: `start.tex:41-44`'s $E$, $W_\lambda$ and
$Q$ are literally objects of this geometry. $E$ is the arithmetic periodisation
whose Mellin transform carries $\zeta$ (`start.tex:54-62`); $W_\lambda$ is the
truncated Weil form on the idele class group; $Q$ removes the two pole directions
(`start.tex:80-82`). Nothing needs to be imported.

**(2) Where the signature lives.** In the correspondence picture: the trace form
$Z\mapsto\operatorname{Tr}(Z\circ Z^t)$ on divisorial correspondences of the
"surface", which for a genuine surface is signed by Hodge index — signature
$(1,\rho-1)$, hence negative definite on the primitive part. Concretely and without
the surface, its shadow already exists: the trace functional on the convolution
algebra of $C_{\mathbb Q}$, evaluated on the cone of elements $f\star f^*$.

**(3) The flow-through — named.** It is the **trace formula**, and the analogy is
exact rather than decorative:

$$
\underbrace{\#C(\mathbb F_q)=\textstyle\sum_i(-1)^i\operatorname{Tr}(F\mid H^i)}_{\text{Lefschetz}}
\;=\;(\Gamma_F\cdot\Delta)
\qquad\longleftrightarrow\qquad
\underbrace{\textstyle\sum_\rho\hat f(\rho)-\hat f(0)-\hat f(1)}_{\text{spectral}}
\;=\;-\textstyle\sum_v W_v(f) .
$$

Left of each arrow is arithmetic (point counts / zeros); right is geometric
(intersection numbers / a sum over places, i.e. over periodic orbits of the
scaling flow). The sign flows **through the trace formula** — in Weil's case because
the geometric side is a self-intersection and Hodge index signs self-intersections.
Under $Z\leftrightarrow f$, $\circ\leftrightarrow\star$, $Z^t\leftrightarrow f^*$,
$\operatorname{Tr}\leftrightarrow$ the trace formula, the correspondence is
complete **except for the single arrow "Hodge index"**, which requires the surface.

That is the honest content of C1: the flow-through map is fully specified and one
arrow is missing, and the missing arrow is missing for a *stated reason* (§2.2 — no
base). This is strictly better than the state of `start.tex:373-377`, which asks to
"relate $C_\lambda$ to the $S^3$ boundary/intersection quantity" without naming a
map at all — and which mg-8d74 §6 already showed is unavailable, since an
intersection number is locally constant while $C_\lambda$ varies continuously.

**(4) Falsifier.** Any proposed construction of the square must *use* the
multiplicativity of the local factors. Concretely: **if a candidate construction of
$X\times_{\mathbb F_1}X$ and its intersection form goes through without ever using
that $\zeta$ has an Euler product, it is wrong**, because it would apply verbatim to
a Davenport–Heilbronn function and prove a false positivity. This is criterion 5
turned into a one-line audit that can be run against any future construction
without understanding it in detail.

**(5) Davenport–Heilbronn.** Passes, and visibly. The Euler product is exactly what
makes the Weil distribution a **sum over places**, $W=\sum_v W_v$: without it there
are no local factors, no local terms, no geometry of places, and nothing to take
the product of. DH functions have a functional equation and an archimedean factor
but no Euler product, hence no adele-class presentation. The step that fails is the
first one.

**Self-test.** "$W(f\star f^*)\ge0$ for all $f$" is **false** for $-W$. Passes.

**The honest weakness, stated plainly.** C1 is not a reduction. It replaces
`start.tex:373-377` with a correct target rather than an easier one, and the target
is the hardest known open problem in the area. It also **discards $S^3$ entirely** —
under §2.2, $S^3$ is the shadow of $\operatorname{Spec}\mathbb Z$ being a
3-dimensional object with no base, so it is a symptom of the thing C1 has to fix.
Anyone hoping to keep the $S^3$ material should read that as bad news.

---

## 4. C2 — the semilocal / archimedean Sonin space

**Rank 1 for action.** This is the only candidate where a Weil sign has actually
been *proved*, and it is the only one that touches the corpus's own objects.

**(1) The candidate, and why it is natural.** Connes–Consani's proof of Weil
positivity at the archimedean place (*Weil positivity and trace formula: the
archimedean place*, Selecta Math. 27 (2021)), and its semilocal extension to a
finite set $S$ of places. The geometry is $\mathbb A_S/\mathbb Q^\times$ — the
adele class space of a *finite* set of places, which unlike the full one is
tractable. The mechanism runs through the **Sonin space**: the space of functions
vanishing, together with their Fourier transform, on $[-\Lambda,\Lambda]$.

Naturality here is not an analogy — it is an identity. The Sonin projection is the
complement of the time–band concentration projection; its spectral theory *is*
prolate spheroidal theory (Connes–Moscovici on the prolate operator and the zeros
of $\zeta$). The corpus's $1-\chi_4$, $\widehat P$, $h_\lambda$
(`s3.tex:55-78`, `start.tex:138-149`) are objects of this space. **The corpus is
already inside C2's geometry without saying so.**

**(2) Where the signature lives.** Not in middle cohomology — the honest substitute
is a **factorisation**: the semilocal Weil form is shown to be
$W_S=A^*A+(\text{controlled})$ on the relevant space, i.e. positivity by exhibiting
a square. In the taxonomy of §2.1 this is the $C^*$-algebra row: a Hermitian form
polarised by an explicit isometry rather than by a Hodge structure. This is
mechanism (2) of `s3-sign-blindness.md:181` — the one the note listed as
sign-breaking and did not pursue.

**(3) The flow-through — named.** The involution is the same $f\mapsto f^*$; the
"geometry" is the semilocal trace formula, whose geometric side is the sum of local
terms over $v\in S$; and the sign arrives because on the Sonin space the sum of
those local terms is realised as a square. The arithmetic sign becomes the geometric
one *at the cutoff*: the parameter $\Lambda$ that defines the Sonin space is the
corpus's $\lambda$, and $1-\chi_4$ is a leakage across exactly that cutoff. Where
$S^3$ had a dictionary row "small boundary/tunnelling term $\leftrightarrow
1-\chi_n$" with no operator attached (`start.tex:119-121`), C2 has the same scale
attached to an operator with an adjoint.

**(4) Falsifier — and this one is cheap, concrete, and worth doing first.**

> **State which places $W_\lambda$ contains.**
>
> - If $W_\lambda$ is the **archimedean-only** Weil form, then positivity is a
>   *theorem*, and $\operatorname{sign}(C_\lambda)>0$ is forced, not open. A
>   numerical computation returning $C_\lambda<0$ would then falsify either the
>   applicability of that theorem or the corpus's identification of $W_\lambda$ —
>   and either answer is worth more than the current silence.
> - If $W_\lambda$ contains **finitely many primes**, C2 predicts the sign is
>   governed by the semilocal result and gives a route to it.
> - If $W_\lambda$ contains **all places**, C2 does not apply, and the corpus should
>   say so — because then `start.tex:358-371` step 2 is asking for something no
>   known technique supplies.

This is the same shape as, and pairs with, the audit's blocking item #2 — the
definition of $Q$ (`s3-reduction-audit.md:246-257`), which is still unresolved and
still the cheapest high-value item in the corpus. Two definitions, both one
paragraph of writing, jointly gating everything downstream.

**(5) Davenport–Heilbronn.** Passes. The archimedean/semilocal positivity proof
uses the specific local factors at the places in $S$; there are no such local
factors for a DH function. The step that fails is the construction of $A$.

**Self-test.** "$W_S(f\star f^*)\ge0$" is **false** for $-W_S$. Passes.

**Honest weakness.** C2 signs *some* places, and the difficulty of RH is exactly
that positivity at all places simultaneously does not follow from positivity at each
— the local terms are individually manageable and their sum is not. C2 is a real
theorem and not a route to RH. Its value here is different and, for this corpus,
larger: **it is a proved sign, in prolate language, adjacent to the corpus's own
objects**, and it converts "what is the sign of $C_\lambda$?" from an open question
into a question about which form $W_\lambda$ actually is.

---

## 5. C3 — Deninger's foliated dynamical system

**Rank 3. Correct shape; does not exist.**

**(1) The candidate.** Deninger's conjectural picture (ICM 1998, and subsequent):
a 3-dimensional foliated dynamical space $(X,\mathcal F,\phi^t)$ with 2-dimensional
leaves and a flow, whose leafwise cohomology $H^1_{\mathcal F}$ carries the zeros
of $\zeta$ as the spectrum of the infinitesimal generator, with a Lefschetz trace
formula reproducing the explicit formula: closed orbits $\leftrightarrow$ primes,
$H^0$ and $H^2$ $\leftrightarrow$ the two pole terms $\hat f(0)+\hat f(1)$.
It is natural in exactly the sense the work item asks for — it was built to import
the Weil mechanism to $\operatorname{Spec}\mathbb Z$, and it manufactures the missing
base (§2.2) as *the flow direction*: the 3-manifold is the "curve", and the flow
supplies the second factor.

**(2) Where the signature lives.** Genuinely: the leaves are surfaces, so leafwise
$H^1$ has a cup product $H^1\times H^1\to H^2$, and a leafwise Hodge star makes it a
**polarised weight-1 Hodge structure** — Riemann bilinear relations, row 3 of §2.1.
RH becomes the statement that the generator acts with the right spectral symmetry
relative to that polarisation. This is the closest thing to a literal Hodge index
theorem available on the $\mathbb Q$ side.

**(3) The flow-through.** The leafwise Lefschetz trace formula, in the same slot as
Weil's Lefschetz formula in C1's diagram. The involution is Poincaré duality on the
leaves; positivity is $\int_{\text{leaf}}\alpha\wedge\star\bar\alpha>0$.

**(4) Falsifier.** Two, both cheap against a *proposed* construction:
(i) its $H^0$ and $H^2$ must produce *exactly* the two pole terms $\hat f(0)$,
$\hat f(1)$ — not up to constants; (ii) the leafwise polarisation must be
unavailable for DH data. If a construction offers a polarisation that does not see
the Euler product, it proves a false statement.

**(5) Davenport–Heilbronn.** Would pass *if constructed*, since the primes enter as
the closed orbits and their lengths $\log p$ are the geometry. Untestable until
there is a construction.

**Self-test.** "The leafwise pairing is positive-definite, and
$\operatorname{Tr}(\phi\circ\phi^\dagger)>0$" is **false** for the negated form.
Passes.

**Honest weakness, and it is decisive for ranking.** No such space is known to
exist, there is no candidate construction with the required properties, and — unlike
C1 and C2 — nothing in this corpus connects to it. It contributes no computation
and no next step. **It is on this list because it is the correct shape and it shows
what "the sign flows through to the geometry" would look like if fully realised, not
because I am proposing to work on it.**

---

## 6. Candidate (a) revisited — the compactness objection is wrong

`s3-reduction-audit.md:292-298` proposed a unitary representation of a compact group
commuting with $W_\lambda$, "positivity from group averaging (Bochner/Godement)".
mg-8d74 §4 corrected this to: symmetry gives Schur block-diagonality, not
positivity — correct and important — and endorsed the audit's objection that "no
compact group acts on the primes". **That last part does not survive.**

Bochner's theorem is a statement about **locally compact abelian** groups: a
continuous function of positive type on $G$ is the Fourier transform of a positive
measure on $\hat G$. Compactness is nowhere required, and the Bochner–Schwartz
extension covers tempered distributions. The group that acts on the primes is
$C_{\mathbb Q}=\mathbb A^\times_{\mathbb Q}/\mathbb Q^\times$, which is locally
compact abelian and not compact — and which does not merely *act on* the primes,
it is assembled from them.

So the repaired candidate (a) reads:

> $W$ is a distribution on $C_{\mathbb Q}$, and Weil positivity is the statement
> that $W$ is **of positive type**; equivalently, by Bochner–Schwartz, that its
> Fourier transform — a measure on $\widehat{C_{\mathbb Q}}$ supported on the
> zeros — is a **positive** measure.

This is inherently signed: it is false for $-W$. And it is not new — it is Weil
positivity restated, and the restatement is a tautology-grade move. **Its value is
entirely diagnostic**, and there are two diagnoses:

- **The group-averaging route is not blocked by the primes.** It is blocked by the
  fact that once you take the group that does act on the primes, "positivity by
  averaging" *becomes* the open problem rather than a technique for attacking it.
  That is a different and more useful statement than "no compact group acts".
- **It says what a geometry must supply**, and this is the design rule of §2.1 in
  its concrete form: a space whose functions form a $\star$-algebra under
  convolution, with the involution $f^*(u)=\overline{f(u^{-1})}/|u|$. Any candidate
  geometry can be tested against that in one line. $S^3$ as constructed supplies
  neither operation, which is why the chain at `s3.tex:188-211` is invariant.

Recorded as a correction to a prior note, not as a route.

---

## 7. The two decorations, and why I am calling them that

### C4 — rational homology spheres and the linking form

**The good part, and it is genuinely informative.** §2.2's dictionary is not
decoration: it explains *why a 3-manifold, and why a homology sphere*, which the
corpus never justifies. And it suggests an obvious repair — replace
$\operatorname{Spec}\mathbb Z$ by $\operatorname{Spec}\mathcal O_K$ with class number
$>1$, hence $S^3$ by a rational homology sphere $M$ with $H_1(M)$ torsion nonzero.
Such an $M$ *does* carry a nondegenerate **symmetric** middle-dimensional pairing,
the linking form $\lambda\colon H_1(M)_{\mathrm{tors}}\times H_1(M)_{\mathrm{tors}}
\to\mathbb Q/\mathbb Z$. Criterion 2 looks satisfied.

**Why it fails, and the reason is not fixable.** A $\mathbb Q/\mathbb Z$-valued
pairing on a **finite** group has no signature over $\mathbb R$: there is no notion
of a positive or negative eigenvalue, so it cannot sign the real number $C_\lambda$.
Second, and independently, it is discrete — it is determined by the class group and
is locally constant, while $C_\lambda$ varies continuously with $\lambda$
(`s3-sign-blindness.md:338-346`). Third, criterion 3 has no candidate map at all:
nothing connects $\lambda(x,x)$ to $W_\lambda$.

**Self-test: fails.** Every statement about $M$'s linking form is true for
$-W_\lambda$, because none of them mentions $W_\lambda$. This is the mg-8d74 defect
reproduced exactly, and I am reporting it rather than dressing it up. C4 belongs in
this note as an *explanation of $S^3$* (§2.2), not as a candidate.

### C5 — the 4-dimensional filling, the $\eta$-invariant, Dedekind sums

`s3-sign-blindness.md:334-336` named "a 4-dimensional filling ($S^3=\partial B^4$)"
as a route to restore even dimension and middle cohomology, and §6 there developed
the $\eta$-invariant with the round-$S^3$ falsifier $\eta\equiv0$. Three further
observations, each cheaper than that falsifier:

1. **$B^4$ has no middle cohomology either.** $H^2(B^4)=0$; a ball is contractible.
   The filling restores even *dimension* and supplies **no intersection form
   whatsoever**. To get one you need a filling with $H^2\ne0$ — a plumbing, a disc
   bundle over $S^2$, an $E_8$-manifold — and *nothing in the corpus selects one*.
   Criterion 1 fails at the first step.
2. **A signature is an integer.** Whatever filling is chosen, $\operatorname{sign}(X)
   \in\mathbb Z$, and by Novikov additivity it is stable under gluing. $C_\lambda$
   varies continuously. This is `s3-sign-blindness.md:338-346`'s argument, and it
   applies to the filling as well as to the boundary.
3. **Dedekind sums do not know about Euler products.** §6 there noted, correctly,
   that lens-space $\eta$-invariants are Dedekind sums and that this is "the one
   place where 3-manifold eta invariants are known to carry arithmetic content".
   But it is the arithmetic of the modular group and $\eta$-quotients, not of the
   primes of $\zeta$; the same expressions exist with no Euler product anywhere in
   sight. **C5 fails criterion 5** — there is no step in it that breaks when the
   Euler product is removed.

**Self-test: fails.** No statement about $\eta$, a filling, or a Dedekind sum
mentions $W_\lambda$. Sign-blind by construction.

### Considered and dropped in one line each

- **Bost–Connes / KMS states.** Positivity of a state is automatic and says nothing
  about zeros; $\zeta$ appears as a partition function, on the wrong side.
- **Li's criterion ($\lambda_n\ge0$).** A signed reformulation, and a good one, but
  it is not a geometry: there is no space, no involution beyond the one already in
  §2, and nothing for criterion 3 to map.
- **Arakelov geometry on $\operatorname{Spec}\mathcal O_K$.** The Hodge index theorem
  *is* available here (Faltings–Hriljac: the arithmetic intersection pairing is
  negative definite on degree-zero divisors, and equals the Néron–Tate height). It
  is the strongest genuine signature theorem in arithmetic geometry. It fails for
  the reason of §2.2 and no other: it needs an arithmetic *surface*, i.e. a curve
  over $\operatorname{Spec}\mathcal O_K$ — and $\operatorname{Spec}\mathbb Z$ itself
  is not one. This is C1's blocker in its classical form, which is why C1 subsumes
  it.

---

## 8. What I would actually do next

In order, cheapest first. The first two are definitions, not theorems, and they gate
everything else.

1. **State which places $W_\lambda$ contains** (§4). One sentence. It decides whether
   $\operatorname{sign}(C_\lambda)$ is open at all, and it is the falsifier for the
   highest-value candidate.
2. **Define $Q$** — still the audit's item #2 (`s3-reduction-audit.md:246-257`), now
   blocking for a third reason: whether $Q$ is compatible with the $\star$-algebra
   structure of §6 determines whether $QW_\lambda$ is still a form to which any
   positivity argument can apply.
3. **Check C2's literature against the corpus's objects.** If the corpus's
   $\widehat P$, $h_\lambda$ and $1-\chi_4$ are the Sonin/prolate objects of
   Connes–Consani and Connes–Moscovici — which §4 argues they are — then the corpus
   is re-deriving pieces of a published framework, and should be positioned against
   it rather than beside it. This is a literature check, not research.
4. **Only then** consider whether anything in the $S^3$ material survives. On the
   analysis of §2.2 it does not: $S^3$ is the shadow of the problem C1 has to solve.

**External facts used above and not verified (offline).** Connes–Consani, *Weil
positivity and trace formula: the archimedean place*, Selecta Math. 27 (2021), and
its semilocal extension; Connes–Moscovici on the prolate operator and the zeros of
$\zeta$; the arithmetic-topology dictionary ($\operatorname{Spec}\mathcal O_K$
3-dimensional with duality, $\operatorname{Spec}\mathbb Z\leftrightarrow S^3$ via
Minkowski, primes $\leftrightarrow$ knots — Mazur, Morishita); Deninger ICM 1998;
Faltings–Hriljac arithmetic Hodge index; Bochner–Schwartz for tempered distributions
of positive type; symmetry and nondegeneracy of the linking form on a rational
homology 3-sphere; $H^*(B^4)$ and Novikov additivity; Weil's use of
Castelnuovo/Hodge index for $\operatorname{Tr}(Z\circ Z^t)>0$. All are standard;
none should be cited in writing without a check.

---

## 9. Self-test — the mg-8d74 test applied to this note

The work item required this, and the result is mixed by design.

| candidate | a statement it makes | false for $-W_\lambda$? |
|---|---|---|
| C1 | $W(f\star f^*)\ge0$ on the Schwartz space of $C_{\mathbb Q}$ | **yes** |
| C2 | $W_S(f\star f^*)\ge0$ on the Sonin space | **yes** |
| C3 | leafwise pairing polarised; $\operatorname{Tr}(\phi\,\phi^\dagger)>0$ | **yes** |
| C4 | $\lambda(x,x)=c\in\mathbb Q/\mathbb Z$ | **no — sign-blind** |
| C5 | $\eta(M,\alpha)$ equals a Dedekind sum | **no — sign-blind** |
| §2.1 lemma | a subspace/projection dictionary is $W\mapsto-W$ invariant | n/a — it is *about* the invariance |

**Two of five reproduce the defect this ticket was sent to escape, and both are
reported as decoration rather than shipped as proposals.** The three that pass do so
for the same reason, which is the note's actual content: each contains an
**involution**, and a statement about a **square**. That is the only known way for a
statement to be false under $W\mapsto-W$, and it is the property the dictionary at
`start.tex:100-127` lacks.

**The one-sentence answer to the question asked.** The natural alternative geometry
is Connes' own — the adele class space and its $\mathbb F_1$-square (C1), with the
semilocal Sonin space (C2) as the tractable piece where a sign is already proved;
the sign flows through the **trace formula**, carried by the involution
$f^*(u)=\overline{f(u^{-1})}/|u|$, which is the functional equation; and the reason
$S^3$ cannot do this is not that it is odd-dimensional but that it has no product
and no adjoint, being — under the arithmetic-topology dictionary that makes it
natural in the first place — the shadow of the very object whose lack of a base is
the problem.
