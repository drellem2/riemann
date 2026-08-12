# Can the $S^3$ geometry see the sign? — running the audit's test (c)

Work item mg-8d74. Companion script: [`verify_sign_claims.py`](verify_sign_claims.py)
(needs numpy; every number quoted below is its output). Prior work, not re-derived
here: [`s3-reduction-audit.md`](s3-reduction-audit.md) (mg-aedf).

Nothing in `start.tex` or `s3.tex` was edited. References are by line.

**Superseded claims (added 2026-08-12).** One claim in this note has since been
refuted and is annotated in place rather than rewritten: **§4's endorsement of the
audit's "no compact group acts on the primes" objection** (below, and at §4's close)
does **not** stand — see [`signed-geometry-proposals.md`](signed-geometry-proposals.md)
§6 (mg-8599). Nothing else here is affected; in particular §3's central finding, that
the whole `s3.tex` chain is invariant under $W_\lambda\mapsto-W_\lambda$, is untouched
by that correction and stands as written.

---

## Bottom line

**Yes, narrowly — and the narrowness is the finding.**

§5 produces a genuinely signed $S^3$-side statement: a *directed inequality*
($\ge$, not $\asymp$) characterising $h_\lambda$ as a constrained minimiser and
recovering item (iii) as an extremal value. That literally passes the audit's
test (c). It is also useless for the sign that matters, and §3 says exactly why,
in a form that should stop this question being reopened:

> **Every statement in `s3.tex` is invariant under $W_\lambda \mapsto -W_\lambda$.**
> Items (i)–(iii) do not mention $W_\lambda$, $E$, $Q$ or $\zeta$ at all — they are
> statements about $h_\lambda$ and the concentration projector. Item (iv), the only
> one that does mention $W_\lambda$, is an $\asymp$. So the flip that changes
> $\operatorname{sign}(C_\lambda)$ changes nothing in the chain at `s3.tex:188-211`.
> **No refinement of items (i)–(iv) can produce the sign**, because the whole
> system of statements is invariant under the operation that inverts the answer.

The reason is visible in one place: the dictionary at `start.tex:100-127` has six
rows, and **not one puts $W_\lambda$, $E$, $\zeta$, or the primes on the analysis
side.** It is a dictionary of the Hilbert space and its projections. A dictionary
with no entry for the operator cannot report the operator's signature.

§7 gives the hard version of the same point. The structure the $S^3$ model encodes
— functional equation, archimedean factor, test space, concentration — is shared by
the Davenport–Heilbronn functions, which satisfy a Riemann-type functional equation
and **have zeros off the critical line**. Any argument built only from that
structure proves positivity for them too, and so proves nothing. What separates
$\zeta$ from them is the Euler product, and the dictionary has no row for it.

§6 is the constructive half. In the one setting where geometry *is* known to supply
the Weil sign — Weil's function-field proof, via the Hodge index theorem on
$C\times C$ — the sign is a **signature**, which needs an even-dimensional space
with a symmetric middle-dimensional intersection form. $S^3$ is odd-dimensional and
has $H^1=H^2=0$: no middle cohomology, no cycles, no signature. The odd-dimensional
substitute is the **eta invariant**, whose profile matches what is wanted
(real-valued, varies continuously, arises as a *boundary* correction). It also
comes with an immediate falsifier: **for round $S^3$ with trivial coefficients
$\eta \equiv 0$**, so the model as constructed predicts no spectral asymmetry at all.

Two corrections to prior documents, both stated as claims to be checked:

- **Against the audit's candidate (a)** (`s3-reduction-audit.md:293-298`): a compact
  group commuting with $W_\lambda$ would **not** give positivity. It gives Schur
  block-diagonality — a *reindexing* of the sign question. §4. And the corpus
  already contains a worked instance of candidate (a) which delivers exactly zero
  sign information.
  *(2026-08-12: the Schur half of this stands. The part of §4 that additionally
  endorsed the audit's "no compact group acts on the primes" objection does not —
  see the note at the close of §4, and `signed-geometry-proposals.md` §6.)*
- **Against `start.tex:373-377`**, which proposes identifying $C_\lambda$ with an
  $S^3$ "boundary/intersection quantity": $C_\lambda$ varies continuously with
  $\lambda$, and an intersection number is locally constant. The intersection
  reading is unavailable unless $C_\lambda$ is asymptotically constant. §6.

---

## 1. Which sign? There are two, and only one is open

The word "sign" covers two different quantities in the corpus, and the first job is
to separate them.

| | quantity | status |
|---|---|---|
| **S-end** | sign of the endpoint term $h_\lambda(0)$ | **settled: negative.** `s3-reduction-audit.md:215` |
| **S-Weil** | $\operatorname{sign}(C_\lambda)$ in $QW_\lambda(Eh_\lambda)=C_\lambda(1-\chi_4)+o(\cdot)$ | **open.** `start.tex:370`, `s3.tex:183` |

Only **S-Weil** is the content of what remains. **S-end** is where a sign already
exists, so it is the natural place to ask whether $S^3$ *explains* signs or merely
accommodates them — that is §2. But note in advance that S-end may not even enter
S-Weil: under one reading of $Q$ (the audit's blocking ambiguity #2,
`s3-reduction-audit.md:246-257`) the endpoint directions are projected away before
$QW_\lambda$ is formed, and then S-end contributes nothing to S-Weil whatsoever.

There is also a textual signal worth recording. Daniel's own Boundary Leakage Lemma
at `start.tex:403-414` states the target as two clauses: a scale clause
($\|QW_\lambda(Eh_\lambda)\|\asymp 1-\chi_4$) and, separately, "*with the
corresponding quadratic contribution having the positivity sign required by Weil's
criterion*". **Every $S^3$ input in the corpus feeds the scale clause.** The sign
clause is appended, and nothing in the chain reaches it. The formulation already
concedes the split this note is about.

---

## 2. Does $S^3$ *explain* the endpoint sign, or accommodate it?

**Verdict: accommodates. The sign is mode-independent, so it carries no information
about the geometry's mode selection — and its two ingredients are both generic.**

Write $r_n := (\int_{-1}^1\psi_n)/\psi_n(0)$, which is convention-free and equals the
Slepian–Pollak eigenvalue $\mu_n = i^n\sqrt{2\pi\Lambda_n/c}$. For
$h=\alpha\psi_0+\beta\psi_m$ normalised by $\hat h(0)=0$,

$$h(0)=\alpha\psi_0(0)\Bigl(1-\frac{r_0}{r_m}\Bigr),\qquad \frac{r_0}{r_m}=i^{-m}\frac{\chi_0}{\chi_m}.$$

The sign factors into two **independent** ingredients:

- **(P) the phase** $\operatorname{sign}(r_0/r_m)=i^{-m}$ — Slepian–Pollak. This is
  the audit's §3 finding. Verified for $m=2,4,\dots,12$ at $c=10,20,50,100,200,400$:
  the pattern $-,+,-,+,-,+$ holds at every $c$ (script, table **(P)**).
- **(X) ground-mode extremality** $\chi_0/\chi_m>1$ for every $m>0$ — because
  $\chi_0$ is the *largest* concentration eigenvalue, so no partner mode can beat it.

Given (P) and (X) the sign law is exact and needs no numerics at all:

$$m\equiv 0\ (4):\ h(0)=\alpha\psi_0(0)\Bigl(1-\tfrac{\chi_0}{\chi_m}\Bigr)<0
\qquad
m\equiv 2\ (4):\ h(0)=\alpha\psi_0(0)\Bigl(1+\tfrac{\chi_0}{\chi_m}\Bigr)>0$$

**for every such $m$.** This sharpens `s3-reduction-audit.md:215`, which derived the
negative sign from $\chi_0>\chi_4$ specifically: the sign does not depend on the
selection of 4 at all. Only the *magnitude*, $1-\chi_0/\chi_m\sim-(1-\chi_m)$, does.

That is decisive for the question asked. **A quantity that takes the same value for
every phase-matched partner mode cannot be evidence that the geometry chose the
right mode.** And neither ingredient is $S^3$: (P) is the $\mathbb{Z}/4$ grading of
the finite Fourier transform (§4), and (X) — "the ground state of a concentration
operator is the best-concentrated mode" — is a Rayleigh-quotient fact true on any
manifold with a Laplacian and a subdomain. Nothing distinguishes $S^3$ from an
interval here.

*Method note.* Computing this sign numerically at $c\ge 20$ returns **noise**:
$\chi_0/\chi_m-1$ is $O(e^{-2c})$ and underflows against $1$. An earlier draft of the
script did exactly that and produced a garbage sign table. This is the same
double-precision ceiling as `s3-reduction-audit.md:259-283`, and here it is a reason
to *derive* the sign rather than measure it — (X) is an ordering, not a measurement.

---

## 3. Why `s3.tex` is sign-blind — the structural statement

This section is the one meant to be permanent.

**Observation.** Consider items (i)–(iv) as listed at `s3.tex:219-241`.

| item | mentions $W_\lambda$, $E$, $Q$, $\zeta$? | invariant under $W_\lambda\mapsto-W_\lambda$? |
|---|---|---|
| (i) $\hat h_\lambda(0)=0$ | no | yes, vacuously |
| (ii) $h_\lambda(0)=O(1-\chi_4)$ | no | yes, vacuously |
| (iii) $\|(1-\hat P)h_\lambda\|^2\asymp 1-\chi_4$ | no | yes, vacuously |
| (iv) $QW_\lambda(Eh_\lambda)\asymp1-\chi_4$ | yes | yes — $\asymp$ compares magnitudes |

Items (i)–(iii) are statements about $h_\lambda$ and the concentration projector
$\hat P$ alone. They remain true *verbatim* if the Weil form is replaced by
$-W_\lambda$, or by any other self-adjoint operator whatsoever, because they never
refer to it. Item (iv) refers to it, and is an $\asymp$, which is invariant under
sign flip on either reading of the notation — as a scalar $\asymp$, or as the norm
$\|QW_\lambda(Eh_\lambda)\|$ that `start.tex:409` actually writes.

Therefore **the entire chain `s3.tex:188-211` is invariant under
$W_\lambda\mapsto-W_\lambda$**, while $\operatorname{sign}(C_\lambda)$ is precisely
what that flip inverts.

**Consequence.** No sharpening of items (i)–(iv) — better constants, exact
asymptotics, uniformity in $\lambda$, upgrading $O$ to $\Theta$ to an exact leading
term — can determine $\operatorname{sign}(C_\lambda)$. This is not a statement about
how hard the remaining work is. It is a statement that the remaining work is *of a
different type*, and that effort spent refining (i)–(iv) is provably not spent on
the sign. The audit's sharpened forms (`s3-reduction-audit.md:165`, `:215`), and §5
of this note, are all subject to it.

**The anticipated objection, and the answer.** *"Of course (i)–(iii) don't mention
$W_\lambda$ — they are inputs. The sign is supposed to come later, from the trace
formula."* Exactly so, and that is the point stated precisely rather than
impressionistically: the $S^3$ contribution is entirely on the **input** side, so
the sign must come from the arithmetic side. The question this work item asks is
whether the geometry can contribute to the sign. The invariance argument answers:
not through any of the four channels it currently uses.

**What would break the invariance.** A statement that is *false* for $-W_\lambda$.
The minimal candidates:

1. $\langle W_\lambda v,v\rangle>0$ for some explicit $v$ — a signed evaluation;
2. $W_\lambda = A^*A + (\text{controlled})$ — a square, hence positive;
3. $W_\lambda$ commutes with $\pi(G)$ **and** its isotypic block eigenvalue is signed.

All three require the geometry to assert something *about $W_\lambda$*, i.e. about
the primes. Checking the dictionary at `start.tex:100-127` row by row — global
compact geometry / two distinguished directions / geometric concentration / failure
to remain in a sector / small boundary term / geometric projection — the analysis
column contains the completed spectral problem, the two exceptional Weil
*directions*, prolate concentration, time–band leakage, $1-\chi_n$, and $Q$.
**Not one row contains $W_\lambda$, $E$, $\zeta$, or a prime.** Row 2 names the
exceptional directions (the functionals $h(0)$, $\hat h(0)$), not the form; row 6
names a projection, not the form.

---

## 4. Candidate (a), group averaging — engaged, and corrected

The audit named this as what "the $S^3$ geometry reduces a Connes gap" would have to
mean (`s3-reduction-audit.md:293-298`): a unitary representation of a compact group
on the test space commuting with $W_\lambda$, so that "positivity could then come
from group averaging (Bochner/Godement) rather than from an estimate."

> **Read with the correction (2026-08-12).** The Schur argument below is unaffected,
> but this section closes by endorsing the audit's objection that no *compact* group
> acts on the primes. That objection has since been refuted — averaging does not need
> compactness — so do not invest in it on the way through; see the annotation at the
> close of §4 and `signed-geometry-proposals.md` §6.

**This overstates what a symmetry buys, and the gap matters.**

If $\pi$ is a unitary representation of a compact $G$ and $[W_\lambda,\pi(g)]=0$,
then by Schur $W_\lambda$ is block-scalar on isotypic components,
$\langle W_\lambda h,h\rangle=\sum_\ell w_\ell\|P_\ell h\|^2$. That is genuine
structure — but **the signs of the $w_\ell$ are not determined by $G$.** Bochner and
Godement give positivity for functions of *positive type*,
$\phi(g)=\langle\pi(g)v,v\rangle$; to conclude $W_\lambda\ge0$ by averaging you need
$W_\lambda$ to lie in the cone generated by $\pi(g)^*A^*A\pi(g)$ — that is, you need
to know it is a square. Which is the problem.

So a symmetry converts "one sign of a quadratic form on an infinite-dimensional
space" into "countably many scalar signs $w_\ell$". At the point the corpus actually
stands — a single distinguished direction $h_\lambda$, a single unknown number
$C_\lambda$ — **that reduction buys nothing, because there is already only one sign
in question.** Candidate (a), even fully realised, would not deliver it.

**And the corpus already contains a worked instance of candidate (a).** The finite
Fourier transform on the band-limited space satisfies $F^4=\mathrm{id}$, generating a
$\mathbb{Z}/4$ action whose isotypic components are indexed by the eigenvalues $i^n$;
the prolates are its eigenvectors. The mode-selection rule $m\equiv0\ (4)$ is exactly
the statement that $\psi_0$ and $\psi_m$ **lie in the same $\mathbb{Z}/4$-isotypic
component**. So a compact group *is* acting, it *does* organise the modes, and what
it produces is a selection rule and **exactly zero sign information** — §2. This is
the audit's cautionary case in its strongest form: not a hypothetical, but a
symmetry already doing work in the corpus and demonstrably not signing anything.

The decisive detail: $F$ commutes with the **concentration operator** — that is
Slepian's commuting-operator fact, the reason prolates are computable at all — not
with $W_\lambda$. Likewise the $\mathbb{Z}/2$ of inversion $u\mapsto1/u$ (the
functional equation, and the "simple-even" of `start.tex:157`) block-diagonalises
into even/odd and does not sign the even block. **The groups that act are symmetries
of $\hat P$; candidate (a) asks for a symmetry of $W_\lambda$. That difference is the
entire gap**, and it is the same input-side/operator-side split as §3.

The audit's own objection — $W_\lambda$ carries the primes and no compact group acts
on those — stands. What is added here is that we now know what the consolation prize
looks like, because we already have it.

> **Superseded, 2026-08-12 (mg-8599).** The sentence above does **not** stand, and is
> left in place only as the record of what this note concluded.
> [`signed-geometry-proposals.md`](signed-geometry-proposals.md) §6 (see also its
> Bottom line, item 4) shows the objection fails as stated: **positivity by averaging
> does not require compactness** — Bochner's theorem is a theorem about *locally
> compact abelian* groups, and Bochner–Schwartz extends it to tempered distributions.
> The group that acts on the primes is the idele class group
> $C_{\mathbb Q}=\mathbb A^\times_{\mathbb Q}/\mathbb Q^\times$, which is locally
> compact abelian and not compact — and which does not merely act on the primes, it is
> built out of them.
>
> The correction **closes** a route rather than opening one, which is why it is worth
> stating precisely. Repaired, candidate (a) says that $W$ is a distribution on
> $C_{\mathbb Q}$ and that Weil positivity is the statement that $W$ is of positive
> type — i.e. candidate (a) **coincides with Connes' own formulation**. It is Weil
> positivity restated, not a new mechanism: group averaging is not blocked by the
> primes, it simply *becomes* the open problem once you take the group that does act
> on them. So this is a live claim being retired, not good news being withheld.
>
> Unaffected by this: the Schur block-diagonality argument earlier in §4 (a symmetry
> gives a reindexing of the sign question, not positivity), the $\mathbb{Z}/4$ worked
> instance, and §3's central finding that the whole `s3.tex` chain is invariant under
> $W_\lambda\mapsto-W_\lambda$. `signed-geometry-proposals.md` §6 endorses the Schur
> correction explicitly; only the compactness clause is withdrawn.

---

## 5. The one signed statement I can produce — and where it sits

Test (c) asked for *any* $S^3$/prolate statement that is not sign-blind. Here is one.
It is real, it is checkable, and it is on the input side.

**Observation (variational form of item (iii)).** Let $\mathcal{E}$ be the even
sector and set

$$\nu(c):=\min\bigl\{\|(1-\hat P)h\|_2^2\ :\ h\in\mathcal{E},\ \|h\|_2=1,\ \hat h(0)=0,\ h(0)=0\bigr\}.$$

Then, numerically for $c=10,\dots,14$:

| $c$ | $d_4=1-\Lambda_4$ | $\nu(c)$ | $\nu/d_4$ | overlap with $h_\lambda$ | $h_\lambda$ excess |
|---|---|---|---|---|---|
| 10 | 2.554e-2 | 1.993e-2 | 0.7803 | 0.99994 | 4.0e-3 |
| 12 | 1.413e-3 | 1.080e-3 | 0.7642 | 1.00000 | 2.3e-4 |
| 14 | 6.052e-5 | 4.576e-5 | 0.7562 | 1.00000 | 1.3e-5 |

Three things follow.

1. **$h_\lambda$ is characterised, not merely given.** `start.tex:147` introduces it
   as "the CCM choice of coefficients". It is, to leading order, the *unique* even
   unit vector annihilated by both endpoint functionals with least leakage — its
   excess over the true minimum falls by a factor $\sim4$ per unit $c$.
2. **The variational problem selects mode 4**, independently of the $i^n$ route.
   By the ticket's own standard this is **consistency, not content** — it reproduces
   a known fact by a different route, exactly the trap the mode-4 finding warns
   about. Recorded as a cross-check, claimed as nothing more.
3. **Item (iii) becomes a directed inequality.** For every even unit $h$ with both
   endpoint functionals vanishing, $\|(1-\hat P)h\|_2^2\ \ge\ \nu(c)$. That is a
   $\ge$, not an $O$/$\Theta$/$\asymp$ — the first such statement in the
   $S^3$–prolate chain other than the exact zero of item (i).

**Evidence it is not an artefact.** The independent check is the Lagrange secular
equation, which predicts the *single*-constraint minimum to lie in $(d_0,d_2)$; at
$c=10$ the code returns $7.385\text{e-}5\in(4.4\text{e-}8,\,1.07\text{e-}4)$, so the
constrained-minimisation routine is doing what it claims.

*Not* independent, and I initially recorded it as though it were: $\nu/d_4$ drifts
towards $8/11=0.7273$, the constant the audit obtained from Hermite limits
(`s3-reduction-audit.md:165`). That agreement is **implied by** the overlap
$\to 1$ — once the minimiser is $h_\lambda$, its leakage is $h_\lambda$'s leakage and
the constant must match. The overlap is the observation; the constant is its
consequence, not a second witness.

**Now the two caveats, which are the actual point.**

- **It is invariant under $W_\lambda\mapsto-W_\lambda$.** It mentions $h$ and
  $\hat P$; it does not mention $W_\lambda$. §3 applies to it unchanged. It is a
  signed statement on the wrong side of the problem.
- **Even this needs an arithmetic input.** The restriction to $\mathcal{E}$ is
  essential: over all modes, $\psi_1$ satisfies *both* constraints identically
  (odd prolates vanish at $0$ and integrate to $0$) and leaks $d_1$, smaller than
  $d_4$ by $\sim c^{3}$. Evenness comes from the functional equation
  (`start.tex:157`), not from the geometry. **The one signed statement available
  borrows its hypothesis from the arithmetic side.**

**Also recorded (negative, and it closes a route).** $h_\lambda$ is **not** the
leakage minimiser under $\hat h(0)=0$ alone: that minimum is $7.4\text{e-}5$ at
$c=10$ against $h_\lambda$'s $2.0\text{e-}2$, i.e. of order $d_2$, smaller than $d_4$
by $\asymp c^{-2}$ (Fuchs). So there is no *one*-constraint extremal principle
selecting $h_\lambda$, and the intuitively appealing reading "the geometry picks the
least-leaky admissible direction" is **false as stated**. $h_\lambda$ trades leakage
for endpoint suppression; two constraints are needed, and both are Weil-side.

*Status:* numerics only, in the narrow double-precision window $c\le14$. The proof
route is standard (Lagrange secular equation $\det M(\nu)=0$ with
$M_{ij}(\nu)=\sum_n u^{(i)}_nu^{(j)}_n/(d_n-\nu)$, plus Fuchs asymptotics for $d_n$),
and the extension to all $c$ is a conjecture, not a theorem.

---

## 6. How geometry is *known* to produce the Weil sign — and why $S^3$ cannot

The question "can a geometry sign the Weil form" has one affirmative answer in the
literature, and it is worth measuring the $S^3$ model against it rather than against
nothing.

**The known mechanism.** For a curve $C$ over a finite field, RH is a theorem, and
Weil's proof obtains the required positivity from the **Hodge index theorem** on the
surface $C\times C$: the intersection form on a smooth projective surface has
signature $(1,\rho-1)$, hence is negative definite on the primitive part, which is
the positivity needed for correspondences. The sign there is a **signature** — a
topological invariant of a symmetric bilinear form on middle-dimensional cohomology.

**Why it is structurally unavailable on $S^3$.** A signature of that kind requires an
even-dimensional space with a symmetric middle-dimensional intersection form. $S^3$
is odd-dimensional; worse, $H^1(S^3;\mathbb{Q})=H^2(S^3;\mathbb{Q})=0$. There is no
middle cohomology, no symmetric intersection form, and no cycles to intersect. **The
specific mechanism by which geometry is known to deliver the Weil sign does not
exist on $S^3$ as a manifold.** Any sign in the model must come from somewhere else:
from a 4-dimensional filling ($S^3=\partial B^4$), from a quotient or a bundle, or
from added structure not present in the corpus.

**A consequence for `start.tex:373-377`,** which proposes identifying $C_\lambda$
with "the $S^3$ boundary/intersection quantity". $C_\lambda$ depends on the
continuous parameter $\lambda$, and every ingredient computed so far
($1-\chi_4$, $8/11$, $\nu(c)$) varies continuously with it. **An intersection number
is locally constant.** So $C_\lambda$ cannot be an intersection number unless it is
constant in $\lambda$ — the identification is available only for
$\lim_{\lambda\to\infty}C_\lambda$, if that exists, and then it is a statement about
the limit rather than about the geometry at finite $\lambda$. Step 3 of the route
forward should be restated accordingly, or dropped.

**The right shape of object in odd dimensions, and its falsifier.** The
odd-dimensional analogue of the signature is the Atiyah–Patodi–Singer **eta
invariant** — literally a measure of spectral asymmetry,
$\eta(s)=\sum_k\operatorname{sign}(\mu_k)|\mu_k|^{-s}$. Its profile is a
surprisingly good match for what is wanted: it is signed by construction; it is
real-valued rather than integral, so it *may* vary with $\lambda$; and it arises
precisely as a **boundary correction term** in the index theorem for a manifold with
boundary — which is the language `start.tex:237,258-262` already uses.

That match is suggestive, and it is **not** a mechanism. What makes it worth writing
down is that it comes with an immediate, cheap falsifier:

> **For the round $S^3$ with trivial coefficients, $\eta\equiv 0$.** The round metric
> admits an orientation-reversing isometry and $\eta$ is odd under orientation
> reversal; equivalently, the Dirac spectrum on round $S^3$ is
> $\pm(\tfrac32+k)$ with equal multiplicities, exactly symmetric.

So if the model's sphere is the round $S^3$ with trivial coefficients, this route is
dead on arrival: the natural signed geometric boundary invariant *vanishes*, and
cannot be a nonzero $C_\lambda$. To get a nonvanishing one requires leaving that
setting — a lens-space quotient $S^3/\Gamma$, a nontrivial flat connection, or a
non-round metric. Of these, the lens spaces are the interesting case: their eta
invariants are given by **Dedekind-sum** expressions, which is the one place where
3-manifold eta invariants are known to carry arithmetic content.

**Concrete ask:** state which $S^3$ the model uses — round or not, trivial
coefficients or not, quotient or not. If round with trivial coefficients, §6 is
closed. If not, the eta invariant is computable and can be compared against
$C_\lambda$, which would be a nontrivial numerical agreement of the kind the audit
asked for at `s3-reduction-audit.md:318-319`.

*Citations unverified — this audit, like mg-aedf, was run offline.* The load-bearing
facts are standard (Hodge index / Weil's function-field proof; $H^*(S^3)$; APS eta;
the round-$S^3$ Dirac spectrum; APS II for lens spaces), but should be checked before
any of §6 is used in writing.

---

## 7. The discipline any sign argument must survive

This is the cheapest test in the note and it should be applied to every future
candidate, including the ones above.

**A geometric sign mechanism that does not use the Euler product cannot work.**

The Davenport–Heilbronn functions are Dirichlet series with periodic coefficients
(modulus 5) satisfying a Riemann-type functional equation — completed with the same
archimedean factor $\pi^{-s/2}\Gamma(s/2)$ as $\zeta$, differing only in conductor —
and they have **infinitely many zeros off the critical line**. They lack an Euler
product. Weil positivity therefore *fails* for them, and the analogue of $C_\lambda$
must come out with the wrong sign in some direction.

Now read the dictionary at `start.tex:100-127` again. Every structure it names —
completed spectral problem, exceptional directions, concentration, leakage, boundary
scale, projection — is present for a Davenport–Heilbronn function exactly as for
$\zeta$. So:

> **Any argument assembled from the dictionary's contents proves positivity for
> Davenport–Heilbronn too, and hence proves nothing.**

This is not an argument that the $S^3$ programme is wrong. It is a *test*: it says
where the load must be carried. A proposed sign mechanism must have an identifiable
step that **fails** when the Euler product is removed. If you cannot point to that
step, the mechanism is vacuous regardless of how geometric it looks.

The same test in a milder form: any mechanism that signs $C_\lambda$ without
arithmetic input, and that does not visibly break when applied to a generic
direction, would prove Weil positivity in all directions — i.e. RH. Be
correspondingly suspicious.

---

## 8. The experiment that would settle it, and what blocks it

There is one measurement that decides whether the $S^3$/prolate decomposition can
carry sign information about $W_\lambda$, as opposed to about $\hat P$.

**Compute the matrix $M_{mn}:=\langle W_\lambda E\psi_m,\ E\psi_n\rangle$** for small
even $m,n$ at moderate $c$. Then:

- If $M$ is near-diagonal in the prolate basis, the decomposition *is* adapted to the
  Weil form, and $\operatorname{sign}(C_\lambda)$ reduces to
  $\operatorname{sign}(M_{44})$ — one number. That would be a real reduction, and it
  would be the first evidence that the geometry's basis is more than a convenient
  coordinate system.
- If $|M_{04}|\gtrsim\sqrt{M_{00}M_{44}}$, the cross term is not negligible, its sign
  is undetermined by anything in the corpus, and the decomposition demonstrably
  carries no sign information. §3 would then be confirmed by measurement rather than
  by inspection.

**This is blocked, and by the audit's already-identified cheapest item.** $M$ cannot
be written down until `start.tex:44`'s $Q$ — "removes the expected low-dimensional
exceptional sector" — is pinned to a definition (`s3-reduction-audit.md:246-257`).
That was already the highest-value/lowest-cost item on the audit's list; it is now
blocking for a second, independent reason. Note the two readings give different
experiments, not just different constants: if $Q$ removes the endpoint directions
then §2's sign is irrelevant to $M$ entirely.

Separately, §5 and the audit's §5 both apply: any numerical work here needs the
Legendre/Bouwkamp route plus extended precision, since the sinc-kernel route is
meaningless past $c\approx14$.

---

## 9. Summary for the ticket

The task asked for either a signed $S^3$ statement with a mechanism and a falsifier,
or a reasoned account of why $S^3$ as constructed cannot see signs. The answer is
mostly the second, with a genuine but misplaced instance of the first.

| | result | where |
|---|---|---|
| Does $S^3$ explain the endpoint sign (S-end)? | **No — accommodates.** The sign is the same for every phase-matched mode, so it carries no information about mode selection; its ingredients are Slepian–Pollak and generic ground-state extremality. | §2 |
| Can any refinement of items (i)–(iv) reach S-Weil? | **No, structurally.** The whole chain is invariant under $W_\lambda\mapsto-W_\lambda$. | §3 |
| Would candidate (a) deliver a sign? | **No.** Symmetry gives Schur block-diagonality, not positivity — and the corpus already has an instance ($\mathbb{Z}/4$ of the finite Fourier transform) that signs nothing. | §4 |
| Is there *any* non-sign-blind statement? | **Yes, one** — a variational $\ge$ characterising $h_\lambda$ and recovering item (iii) as an extremal value. It is on the input side and borrows evenness from the functional equation. | §5 |
| Could a geometry sign the Weil form at all? | **Known to be possible only via signature (Hodge index, function-field).** Unavailable on $S^3$: odd-dimensional, $H^1=H^2=0$. Odd-dimensional substitute is eta, which vanishes for round $S^3$. | §6 |
| What must any future candidate survive? | **The Davenport–Heilbronn test.** Every structure in the dictionary is present for a function with zeros off the line. | §7 |
| What would settle it empirically? | Near-diagonality of $\langle W_\lambda E\psi_m,E\psi_n\rangle$. **Blocked on the $Q$ definition** — the audit's item #2, now blocking for a second reason. | §8 |

**Recommendation.** Treat the sign as an arithmetic quantity and stop routing it
through the geometry. The two cheapest unblocking moves are unchanged from the prior
audit and are now better motivated: **define $Q$** (§8), and **state which $S^3$**
(§6). Everything else in the geometric direction is, on the evidence here, a
dictionary.
