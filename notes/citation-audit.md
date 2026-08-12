# Citation audit, and the positioning question against Connes–Consani

Work item mg-3a9c. Audits the attributions in
[`s3-reduction-audit.md`](s3-reduction-audit.md) (mg-aedf),
[`s3-sign-blindness.md`](s3-sign-blindness.md) (mg-8d74) and
[`signed-geometry-proposals.md`](signed-geometry-proposals.md) (mg-8599), and settles the
question those notes could not: whether the corpus is re-deriving published work.

Nothing in `start.tex` or `s3.tex` was edited. References to them are by line.

**This note was written with web access on 2026-08-12.** It is the pass the other three
notes each ask for in their closing caveat. Where a source could not be reached, that is
said in §7 rather than papered over.

---

## Bottom line

**1. Part A. Twenty-five attributions checked: nineteen hold as stated, five are narrower
than our text claims, one is not supported by the cited object.** (13 rows in §2, 11 in
§3, plus `start.tex:88-91`'s "Figure 4" in §4.6, which is the unsupported one.) The five
narrowings are all in §2; none of them touches the internal mathematics, all of them touch
what may be written down. Nine further items could not be settled and are listed in §7 —
they are results too. **As of 2026-08-12 eight of those nine are closed** (U6 mg-9433; U4, and §4.2 row 14, mg-03f0; U7 mg-555b; U1, U2, U3, U8, U9 mg-882b — §12). **U5 alone is open, and it is Daniel's**: it asks what the corpus meant, not what a source says.

**2. Part B. Yes — and considerably more strongly than
`signed-geometry-proposals.md` §4 guessed.** §4 argued that the corpus's $\widehat P$,
$h_\lambda$ and $1-\chi_4$ "are objects of" Connes–Consani's geometry. That understates
it. The corpus's $E$, $\widehat P$, $\chi_n$, $\lambda$, the codimension-two test space,
the two-mode prolate combination, and the near-null direction itself are **the objects of
Connes–Consani, *Spectral triples and $\zeta$-cycles*, Enseign. Math. 69 (2023) 93–148
(arXiv:2106.01715), §3 — in that paper's own letters.** `start.tex:54-58` is its
equation (3.1). `start.tex:80-82` is its $\mathcal S_0^{ev}$. The "striking almost-null
direction" of `start.tex:88` is that paper's abstract. The full object-by-object table is
§4.2.

**3. There is a notation collision, and it has swallowed a definitional gate.** In
Connes–Consani, $W_\lambda$ is the **prolate operator** and $QW_\lambda$ is a *single
symbol* for the **Weil quadratic form** at scale $\lambda$. `start.tex:208-210` reads
$QW_\lambda$ as $Q \circ W_\lambda$ — "$W_\lambda$ the truncated Weil form, $Q$ the
projection away from the exceptional sector". `s3.tex:122` splits the same symbol the
other way ("$Q$ the Weil quadratic form, $W_\lambda$ the finite/prolate operator"). §4.3.
This bears directly on Gate 2 and I have not attempted to resolve it — it is Daniel's.

**4. The residue is real but small, and it is not where the corpus thinks it is.** What
is not in the published work: the *quantification* of a step Connes–Consani take
approximately (their $\varphi_n$ satisfy one endpoint condition exactly and the other only
up to prolate error; `start.tex:169-196` makes that trade explicit, one-sided, and sized),
mg-aedf's exact constant $\tfrac{8}{11}$, mg-aedf's arithmetic-precision bound, and the
$S^3$ overlay — which mg-8d74 already established is sign-blind. §4.4. The corpus's "main
new structural result" (`start.tex:198`) is a sharpening of a published construction, not
a new one, and should be written as such.

**5. arXiv:2607.02828 (Groskin) is not a collision, but its cutoff and ours are the same
construction under a $2\pi$ rescaling.** §5. And the corner is not empty: there is an
active 2025–26 literature on the truncated Weil form (§6), in which a *prolate-basis*
implementation is explicitly recorded as not yet done by anyone. That is the one place
the corpus's numerics are not duplicated.

---

## 1. What "verified" means in the tables below

Three outcomes, per the work item:

| mark | meaning |
|---|---|
| **holds** | the source states the claim; reference given, with theorem/page where the claim is specific enough to have one |
| **narrower** | the source states something weaker or in a smaller setting than our text claims. The reference is real; the support is partial. **This is the outcome the pass exists to find.** |
| **unsupported** | the cited object does not say it |

A citation that exists is not a citation that supports the claim, and "standard" is not a
verification. Every **narrower** row below survived a first pass that would have called it
confirmed.

---

## 2. Part A — the nine load-bearing facts of `signed-geometry-proposals.md:653-663`

| # | claim, as our text states it | outcome | reference |
|---|---|---|---|
| A1 | Connes–Consani, *Weil positivity and trace formula: the archimedean place*, Selecta Math. 27 (2021) | **holds** | Selecta Math. (N.S.) **27** (2021), no. 4, Paper No. 77, 70 pp.; DOI [10.1007/s00029-021-00689-4](https://doi.org/10.1007/s00029-021-00689-4); arXiv:2006.13771 (24 Jun 2020) |
| A2 | "…and its semilocal extension" | **narrower** | §2.1 |
| A3 | positivity there is by a factorisation $W_S = A^*A + (\text{controlled})$ (`signed-geometry-proposals.md:345-347`) | **narrower** | §2.2 |
| A4 | Sonin space = functions vanishing with their Fourier transform on $[-\Lambda,\Lambda]$ (`:294-295`) | **holds** | arXiv:2006.13771 §1: the Sonin space is the orthogonal complement of the range of the cutoff projection at $\Lambda=1$, i.e. even $L^2(\mathbb R)$ functions which "together with their Fourier transform, vanish identically in $[-1,1]$"; called there "the well-known infinite dimensional Sonin's space" |
| A5 | Connes–Moscovici on the prolate operator and the zeros of $\zeta$ | **holds** | arXiv:2112.05500, *Prolate spheroidal operator and Zeta* (10 Dec 2021) = A. Connes, H. Moscovici, *The UV prolate spectrum matches the zeros of zeta*, **PNAS 119** (2022) e2123174119, DOI [10.1073/pnas.2123174119](https://doi.org/10.1073/pnas.2123174119). Precise content: the restriction of the self-adjoint extension $W$ to the complement of $J$ has *negative* eigenvalues whose UV behaviour reproduces the **squares** of the zeros; the eigenfunctions lie in the Sonin space |
| A6 | the Sonin projection's spectral theory *is* prolate theory (`:298-300`) | **holds, and stronger than claimed** | Connes–Consani–Moscovici, arXiv:2310.18423 §1: the Sonin space "was identified in [12] to the Sonin space" as the negative eigenspace of the prolate operator, "up to a finite dimensional possible discrepancy" |
| A7 | arithmetic-topology dictionary: $\operatorname{Spec}\mathcal O_K$ 3-dimensional with duality; $\operatorname{Spec}\mathbb Z \leftrightarrow S^3$ via Minkowski; primes $\leftrightarrow$ knots (Mazur, Morishita) | **narrower** | §2.3 |
| A8 | Deninger, ICM 1998 | **holds** (programme statement); **unverified at page level** | C. Deninger, *Some analogies between number theory and dynamical systems on foliated spaces*, Doc. Math., Extra Vol. ICM Berlin 1998, Vol. I, 163–186. §7 item U2 |
| A9 | Faltings–Hriljac arithmetic Hodge index: pairing negative definite on degree-zero divisors, equals Néron–Tate height (`:598-599`) | **narrower** | §2.4 |
| A10 | Bochner–Schwartz for tempered distributions of positive type (`:484-486`) | **narrower** | §2.5 |
| A11 | linking form on a rational homology 3-sphere is symmetric and nondegenerate, $\mathbb Q/\mathbb Z$-valued on $H_1$ torsion (`:546-548`) | **holds** | Standard; e.g. Friedl–Leidy–Nagel–Powell, *Linking forms revisited*, Pure Appl. Math. Q. **12** (2016) no. 4 (arXiv:1708.03754) §2: for a rational homology 3-sphere $Y$, $\lambda\colon H_1(Y;\mathbb Z)\times H_1(Y;\mathbb Z)\to\mathbb Q/\mathbb Z$ is nonsingular and symmetric, and $H_1$ is all torsion |
| A12 | $H^2(B^4)=0$; Novikov additivity (`:570-578`) | **holds** | $B^4$ is contractible, so $H^*(B^4)=H^*(\mathrm{pt})$ — no citation required. Novikov additivity: if two compact oriented $4k$-manifolds are glued by an orientation-reversing diffeomorphism of their **whole** boundaries, the signature of the union is the sum. (Wall non-additivity applies only when gluing along a *proper* piece of the boundary; our text does not use that case, so the caveat does not bite.) |
| A13 | Weil's use of Castelnuovo / Hodge index for $\operatorname{Tr}(Z\circ Z^t)>0$ (`:136`, `s3-sign-blindness.md:364-369`) | **holds** | Weil's 1948 proof of RH for curves over $\mathbb F_q$ obtains positivity of the trace form on correspondences from the **Castelnuovo–Severi inequality** — Castelnuovo's $\sigma(D,D)\ge 0$ for a divisor on $C_1\times C_2$, with equality iff $D$ has valence zero — equivalently the Hodge index theorem on the surface. Survey: J.S. Milne, *The Riemann Hypothesis over Finite Fields: From Weil to the Present Day* (arXiv:1509.00797) §3 |

### 2.1 A2 — the semilocal case is not proved

`signed-geometry-proposals.md:289-290` cites "…and its semilocal extension" as if it were
a companion theorem, and `:64` calls C2 "the only place a sign is actually *proved*".

What arXiv:2006.13771 proves is the **archimedean place**. Its own framing: "We explore in
great details the simplest case of the single archimedean place… All the ingredients and
tools used make sense in the general semi-local case, where Weil positivity implies RH."
That is a stated strategy, not a theorem. Connes–Consani–Moscovici (arXiv:2310.18423 §1),
three years later, still describe the semilocal case as a programme: their paper "provides
a more precise strategy for addressing the semilocal Weil positivity", and defers a second
candidate semilocal prolate operator "to a forthcoming paper".

**Consequence for our text.** `signed-geometry-proposals.md:64` and `:275-276`, and the
vision document's "C2 signs *some* places", should read: the sign is proved **at the
archimedean place**; the semilocal case is an announced strategy. This does not change the
C2 ranking — an archimedean theorem is still the only proved sign in the list — but it
removes a plural.

### 2.2 A3 — the mechanism is a compression, not an exhibited square

`signed-geometry-proposals.md:345-347` states that the semilocal Weil form "is shown to be
$W_S=A^*A+(\text{controlled})$ on the relevant space, i.e. positivity by exhibiting a
square."

No such factorisation appears. What arXiv:2006.13771 proves (Theorem 1, for test functions
with support in $[2^{-1/2},2^{1/2}]$ and $\hat f$ vanishing at $0$ and $i/2$) is
$$W_\infty(g\star g^*)\;\ge\;\operatorname{Tr}\bigl(\vartheta(g)\,\mathbf S\,\vartheta(g)^*\bigr),$$
where $\mathbf S$ is the projection onto the Sonin space and $\vartheta$ the scaling
action; the difference between the Weil distribution and this "Sonin trace" is expanded in
prolate spheroidal wave functions and controlled by hermitian **Toeplitz matrix** theory.

The distinction matters in exactly one direction and it is the direction §2.1 of that note
cares about. The right-hand side *is* of the form $\operatorname{Tr}(x\,x^*)$, so the
taxonomy placement — the $C^*$-algebra row of the table at
`signed-geometry-proposals.md:134-140` — **survives**; the sign really does come from an
involution and a square, and the note's structural reading is right. What does not survive
is the sentence "positivity by exhibiting a square" applied to $W_S$ itself: the Weil form
is *bounded below by* a manifestly positive trace, and the gap is what the Toeplitz
argument controls. Written as our note has it, a reader would look for an $A$ and not find
one.

### 2.3 A7 — the dictionary, with two caveats, one of which bites

- **"$\operatorname{Spec}\mathcal O_K$ is 3-dimensional with duality"** — holds in
  substance: Artin–Verdier duality gives a perfect duality in étale cohomology for
  $0\le r\le 3$, and $\operatorname{Spec}\mathcal O_K$ has étale cohomological dimension 3.
  **Caveat that bites:** at the prime 2, if $K$ has a real embedding, the mod-2 étale
  cohomological dimension of $\mathcal O_K$ is *infinite*, and the clean 3-dimensional
  statement holds away from 2 (or for totally imaginary $K$). $\mathbb Q$ has a real place,
  so this caveat applies to precisely the case
  `signed-geometry-proposals.md:149-154` invokes. It does not damage the argument there —
  which only needs "why a 3-manifold, and why a homology sphere" — but the sentence as
  written is unconditional and the theorem is not.
- **"$\operatorname{Spec}\mathbb Z\leftrightarrow S^3$ via Minkowski"** — the arithmetic
  half is a theorem: Minkowski's discriminant bound gives $|d_K|>1$ for $K\neq\mathbb Q$,
  hence $\mathbb Q$ has no nontrivial unramified extension, hence
  $\pi_1^{\text{ét}}(\operatorname{Spec}\mathbb Z)=1$. The *identification* with $S^3$ is a
  dictionary entry (the M²KR dictionary — Mazur, Morishita, Kapranov, Reznikov), not a
  theorem, and it is one-directional: simple connectivity does not by itself pick out
  $S^3$ among closed 3-manifolds except through Poincaré–Perelman. Our text at `:152-154`
  says "corresponds… because", which reads as an implication. It is an analogy.
- **primes $\leftrightarrow$ knots (Mazur, Morishita)** — holds. Morishita, *Knots and
  Primes: An Introduction to Arithmetic Topology*, Springer Universitext, 2012 (Japanese
  original 2009), is the standing reference; Mazur's originating notes (*Remarks on the
  Alexander polynomial*, c. 1963–64) are unpublished, which is worth stating when citing
  them. The Legendre symbol $\leftrightarrow$ linking number entry is the one our
  §2.2/§7 leans on and it is the book's central example.

### 2.4 A9 — negative *semi*-definite

`signed-geometry-proposals.md:598-599` says the arithmetic intersection pairing is
"negative definite on degree-zero divisors, and equals the Néron–Tate height".

The Faltings–Hriljac theorem (Faltings, *Calculus on arithmetic surfaces*, Ann. of Math.
(2) **119** (1984) 387–424; Hriljac, *Heights and Arakelov's intersection theory*, Amer. J.
Math. **107** (1985) 23–38) states that for an arithmetic divisor whose restriction to the
generic fibre has degree zero, the arithmetic self-intersection equals **minus** the
Néron–Tate height, hence is $\le 0$ — negative *semi*-definite, becoming definite only
after quotienting by the vertical/torsion classes on which the height vanishes. "Negative
definite" is an over-claim by exactly that kernel.

The note's *use* of the theorem is unaffected, and its own diagnosis at `:601-604` is
correct and worth keeping: the theorem needs an arithmetic **surface**, i.e. a curve over
$\operatorname{Spec}\mathcal O_K$, and $\operatorname{Spec}\mathbb Z$ is not one.

### 2.5 A10 — Bochner–Schwartz is a theorem on $\mathbb R^n$

`signed-geometry-proposals.md:484-486` writes: "Bochner's theorem is a statement about
locally compact abelian groups… and the Bochner–Schwartz extension covers tempered
distributions." Two statements are being run together, and only the first is at that
generality.

- **Bochner on LCA groups** — holds, and the note's correction of mg-8d74 §4 stands
  entirely: a continuous function of positive type on a locally compact abelian $G$ is the
  Fourier transform of a positive measure on $\hat G$, and **compactness is nowhere
  required**. mg-8d74's "no compact group acts on the primes" objection really does fail
  for the reason `signed-geometry-proposals.md:476-490` gives.
- **Bochner–Schwartz** — holds as a theorem *on $\mathbb R^n$*: a tempered distribution of
  positive type is the Fourier transform of a positive tempered measure. I could not find a
  reference for the distributional version on a general LCA group, and the repaired
  candidate (a) at `:494-497` applies it to $C_{\mathbb Q}=\mathbb A^\times/\mathbb Q^\times$,
  which is not $\mathbb R^n$. Logged as unresolved in §7 (U1). Since that passage is
  explicitly "diagnostic, not a route" (`:521`), nothing downstream depends on it — but the
  sentence should not be written as though a single named theorem covered the step.

---

## 3. Part A — attributions in the other two notes

The work item asked for a sweep beyond §8's list. These are the load-bearing ones.

| # | claim | outcome | reference |
|---|---|---|---|
| B1 | Slepian–Pollak finite-Fourier eigenrelation, $\mu_n=i^n\sqrt{2\pi\Lambda_n/c}$ (`s3-reduction-audit.md:220-222`, `s3-sign-blindness.md:109,116`) | **holds** | D. Slepian, H.O. Pollak, *Prolate spheroidal wave functions, Fourier analysis and uncertainty — I*, Bell System Tech. J. **40** (1961) 43–63. Independently corroborated: Connes–Consani state the same relation in the form $\widetilde{\mathcal F}(\psi_{m,\lambda})=\chi_m\psi_{m,\lambda}$ on $[-\lambda,\lambda]$ with $\chi_m$ "very close to $(-1)^m$ provided $m<2\lambda^2$" (arXiv:2106.01715 §3) — see §4.2 row 6 |
| B2 | fixed-index large-$c$ Hermite limit for prolates (`s3-reduction-audit.md:155-156`) | **holds** (source), **unverified** (uniform-error version) | D. Slepian, *Some asymptotic expansions for prolate spheroidal wave functions*, J. Math. and Phys. **44** (1965) 99–140. §7 item U3 |
| B3 | rigorous bounds: Bonami–Karoui, Osipov–Rokhlin–Xiao (`s3-reduction-audit.md:157`) | **holds** | A. Bonami, A. Karoui, *Uniform approximation and explicit estimates for the prolate spheroidal wave functions*, Constr. Approx. **43** (2016), Springer. A. Osipov, V. Rokhlin, H. Xiao, *Prolate Spheroidal Wave Functions of Order Zero: Mathematical Tools for Bandlimited Approximation*, Applied Math. Sciences **187**, Springer, 2013 — this is reference [16] of Connes–Consani–Moscovici arXiv:2310.18423, i.e. the same source the principals use |
| B4 | Fuchs/Slepian asymptotic $1-\Lambda_n(c)\sim 4\sqrt\pi\,8^n c^{n+1/2}e^{-2c}/n!$ (`s3-reduction-audit.md:179`) | **holds** (source), **unverified** (exact constant) | W.H.J. Fuchs, *On the eigenvalues of an integral equation arising in the theory of band-limited signals*, J. Math. Anal. Appl. **9** (1964) 317–330. §7 item U4 |
| B5 | Hodge index / Weil function-field proof; signature $(1,\rho-1)$ (`s3-sign-blindness.md:364-369`) | **holds** | as A13 |
| B6 | $H^1(S^3;\mathbb Q)=H^2(S^3;\mathbb Q)=0$ (`s3-sign-blindness.md:373`) | **holds** | standard; no citation required |
| B7 | APS eta invariant as the odd-dimensional signed invariant, arising as a boundary correction (`s3-sign-blindness.md:391-397`) | **holds** | M.F. Atiyah, V.K. Patodi, I.M. Singer, *Spectral asymmetry and Riemannian geometry* I–III, Math. Proc. Cambridge Philos. Soc. **77** (1975) 43–69; **78** (1975) 405–432; **79** (1976) 71–99 |
| B8 | round $S^3$, trivial coefficients: Dirac spectrum $\pm(\tfrac32+k)$ with equal multiplicities, hence $\eta\equiv0$ (`s3-sign-blindness.md:402-405`) | **holds** | The Dirac spectrum of the round $S^3$ is $\pm(\tfrac32+k)$, $k\ge0$, with multiplicity $(k+1)(k+2)$ on each sign — symmetric, so $\eta\equiv0$. See e.g. arXiv:1605.08589, *Spectral analysis of the Dirac operator on a 3-sphere*. The note's second argument (orientation-reversing isometry, $\eta$ odd under orientation reversal) is independent and also correct |
| B9 | lens-space eta invariants are Dedekind-sum expressions (`s3-sign-blindness.md:411-413`) | **holds** | APS II; explicit modern form via Bär's formula for spherical space forms — see arXiv:1504.03121, *Properties of the Dirac spectrum on three dimensional lens spaces* |
| B10 | Davenport–Heilbronn: Riemann-type functional equation, no Euler product, zeros off the critical line (`s3-sign-blindness.md:44-45,453-457`) | **holds** | H. Davenport, H. Heilbronn (1936). The function is $D(s)=\tfrac{1-i\kappa}{2}L(s,\chi)+\tfrac{1+i\kappa}{2}L(s,\bar\chi)$; it satisfies the functional equation, has no Euler product, has infinitely many zeros on the critical line **and** zeros off it. Numerics: Spira; see *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp. **76** (2007) |
| B11 | Bochner/Godement give positivity for functions of positive type; Schur gives block-diagonality, not signs (`s3-sign-blindness.md:223-226`) | **holds** | as A10, first bullet |

**Note on B1.** mg-aedf calls the phase rule "the one structural finding" of that note
(`s3-reduction-audit.md:217`, `:240-242`). The underlying fact — that the finite-Fourier
characteristic value alternates in sign with the mode index — is stated by Connes–Consani
themselves, in the form $\chi_m\simeq(-1)^m$ for $\psi_{m,\lambda}:=\mathrm{PS}_{2m,0}$
(their index $m$ is half the prolate index, so $(-1)^m=i^{2m}=i^n$: the two statements are
the same statement). What is *not* in Connes–Consani is mg-aedf's **use** of it — the
selection of mode 4 as the least-leaky even prolate whose phase matches mode 0, and the
$\{0,2\}$-versus-$\{0,4\}$ comparison at `s3-reduction-audit.md:227-238`. Connes–Consani
use the sign to split the even and odd matrices, not to select a mode. mg-aedf's framing
("Any $S^3$ derivation of '4' will at best reproduce it") stands; the sentence that it is
new does not.

---

## 4. Part B — the positioning verdict

### 4.1 Which papers "CCM" and "the 2023 trace formula" refer to

The corpus says "CCM" throughout and "the 2023 trace formula" at `start.tex:46,242,425`,
without ever naming a paper. Resolved:

| corpus phrase | what it is |
|---|---|
| "CCM" / "the CCM vector" / "CCM numerics" | **Connes–Consani**, *Spectral triples and $\zeta$-cycles*, Enseign. Math. **69** (2023) no. 1–2, 93–148; arXiv:2106.01715. This is the paper with the small eigenvalues, the prolate construction, and the numerics |
| "the 2023 trace formula" | ambiguous. Two candidates: the same CC 2023 paper, or **Connes–Consani–Moscovici**, *Zeta zeros and prolate wave operators*, arXiv:2310.18423 (Oct 2023). The underlying **semilocal trace formula** is neither: it is A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (N.S.) **5** (1999), no. 1, 29–106. §7 item U5 |
| "Connes–Consani–Moscovici (CCM) finite approximations" (`start.tex:25-26`) | the finite approximations are Connes–Consani's (2023); Moscovici joins for arXiv:2310.18423 and for the prolate-operator work (A5) |

Recommendation: the corpus should stop writing "CCM" for a two-author paper.

### 4.2 The object-by-object correspondence

All right-hand entries are from Connes–Consani, arXiv:2106.01715 §3 unless marked.

| # | corpus | published | verdict |
|---|---|---|---|
| 1 | $E(f)(u)=u^{1/2}\sum_{n\ge1}f(nu)$, `start.tex:54-58` | $\mathcal E(f)(x)=x^{1/2}\sum_{n>0}f(nx)$, eq. (3.1) | **identical, same letter** |
| 2 | "codimension-two space of test functions, the two removed directions corresponding to the familiar pole/end-point obstructions", `start.tex:80-82` | $\mathcal S_0^{ev}\subset\mathcal S(\mathbb R)$, even Schwartz $f$ with $f(0)=\hat f(0)=0$ — the stated **domain of $\mathcal E$** | **identical** |
| 3 | $\widehat P$, `s3.tex:62` | $\widehat P_\lambda$, the conjugate of $P_\lambda$ by the Fourier transform | **identical, same letter** |
| 4 | prolate concentration, $\|(1-\widehat P)h_\lambda\|^2$, `s3.tex:62-67` | $P_\lambda\widehat P_\lambda P_\lambda$ diagonalised by the prolates (Slepian–Pollak); the "angle" of the two projections | **identical** |
| 5 | $\lambda$, and $c$ in the verification scripts | $\lambda>1$, support $[\lambda^{-1},\lambda]$, $\mu=\lambda^2$, circle length $L=2\log\lambda$; prolate parameter $\gamma=2\pi\lambda^2$ | **identical**, with $c_{\text{ours}}=2\pi\mu$ — see §5 |
| 6 | $\chi_n$, "the relevant prolate concentration eigenvalue", `start.tex:44,148` | $\chi(\mu,m)=2\lambda S^{(1)}_{2m,0}(2\pi\mu,1)$, the **finite-Fourier characteristic value**, $\simeq(-1)^m$ for $m\le\nu(\mu)$ | **identical, same letter** — and note the sign. `verify_prolate_claims.py:73` sets `chi = sqrt(lam)`, which is $|\chi_m|$; the sign is mg-aedf §3's phase rule |
| 7 | $\nu(c)$ (`s3-sign-blindness.md:353`) | $\nu(\mu)\approx 2\mu$, the count of small eigenvalues; "$\nu(\mu)=2\mu-1$ works well when $\mu$ is a small half integer" | **identical, same letter** |
| 8 | $h_\lambda=\alpha h_{0,\lambda}+\beta h_{4,\lambda}$, `start.tex:138-145`; "the CCM choice of coefficients" | $\varphi_{2n}(x):=\psi_{2n}(x)\psi_0(0)-\psi_0(x)\psi_{2n}(0)$ — the two-mode prolate combinations **vanishing at 0** | **same construction, mirrored endpoint.** §4.4 |
| 9 | $k_\lambda=E(h_\lambda)$, `start.tex:151-153` | $\mathcal E(\varphi_n)$, components computed by eq. (3.4), then Gram–Schmidt to orthonormal $\varepsilon_n$; Definition 3.1 | **identical** |
| 10 | "a striking almost-null direction", "the numerical near-kernel", `start.tex:88,202` | "We exhibit very small eigenvalues of the quadratic form associated to the Weil explicit formulas restricted to test functions whose support is within a fixed interval" — the paper's **abstract** | **identical phenomenon, published 2021/2023** |
| 11 | *why* it is nearly null — the corpus gives no reason beyond the two endpoint cancellations | "the radical of $QW$ **contains the range of the map $\mathcal E$**"; hence $\mathcal E$ of anything lands in the "near radical", $QW_\lambda(g)\ll\|g\|^2$ | **published mechanism, and the corpus does not state it.** §4.5 |
| 12 | $W_\lambda$, "the truncated Weil operator/form", `start.tex:42,208` | $W_\lambda$ = the **prolate operator**, eq. (3.3): $(W_\lambda\psi)(q)=-\partial((\lambda^2-q^2)\partial)\psi+(2\pi\lambda q)^2\psi$. Same symbol in Connes–Consani–Moscovici arXiv:2310.18423 eq. (2),(4),(5) | **notation collision.** §4.3 |
| 13 | $Q$, "removes the expected low-dimensional exceptional sector", `start.tex:43,210,125` | no such operator. $QW_\lambda$ is one symbol: the **Weil quadratic form** on test functions supported in $[\lambda^{-1},\lambda]$ | **misparse.** §4.3 |
| 14 | $1-\chi_4$ as the controlling scale, `start.tex:34,39,186` | not used *in arXiv:2106.01715*: Connes–Consani report the smallest eigenvalue $s(L)$ decaying **exponentially in $\mu=e^L$** (Figures 18–21, §2.5) with no identification of the rate. **But the rate is identified elsewhere in the literature.** Connes, arXiv:2602.04022 (`rhready.tex:1149`), reports *"a striking similarity … between the behavior of $\epsilon(\lambda)$ and of the angular function $1-\chi_2(\lambda)$"*, gives the Fuchs asymptotic $1-\chi_2\sim\frac{2^{14}}3\sqrt2\,\pi^5e^{-4\pi e^L+9L/2}$, and by its own footnote $\chi_k(\lambda)^2=\lambda_{2k}$ its $\chi_2$ is prolate index 4 — the corpus's $\chi_4$ ([`index-convention.md`](index-convention.md)) | ~~**corpus-specific.**~~ **NARROWED 2026-08-12 (mg-03f0), applied in place (mg-6d7e): read the verdict as "not in arXiv:2106.01715", which is all this row checked.** The row is **right about its paper and wrong only as a claim about the literature** — the two are not the same statement, and "corpus-specific" reads as the second. Note what this is *not*: the survey is Feb 2026 and predates this pass, and §6 of this note names it as the place to check. A scoping defect, not a decayed finding. §4.4 (end note) and §11; full account [`semilocal-gap.md`](semilocal-gap.md) §5.2–5.3 |
| 15 | Sonin space | negative eigenspace of the prolate operator (A5, A6). Absent from `start.tex` and `s3.tex` entirely | **published object the corpus does not use** |

**Verdict.** `signed-geometry-proposals.md:301-302` — "The corpus is already inside C2's
geometry without saying so" — is correct, and understated. It is not that the corpus's
objects *belong to* that geometry; they are that paper's objects, in that paper's letters,
performing that paper's construction. The corpus should be positioned **against**
Connes–Consani 2023, not beside it. Concretely: `start.tex` §1 and §3 are exposition of
arXiv:2106.01715 §3 and should be written as such, with the citation.

### 4.3 The notation collision — $QW_\lambda$ is one symbol

This is the single most consequential finding of the pass, so it is stated plainly.

In Connes–Consani (arXiv:2106.01715 §3, and throughout §2.5, Figures 22–24):

- $W_\lambda$ is the **prolate differential operator** of eq. (3.3), the Slepian–Pollak
  operator commuting with $P_\lambda\widehat P_\lambda P_\lambda$. It is positive
  self-adjoint and its eigenfunctions are the prolate spheroidal wave functions. It has
  nothing to do with Weil.
- $QW_\lambda$ is a **single symbol** — $Q$ for *quadratic form*, $W$ for *Weil* — denoting
  the Weil quadratic form restricted to test functions supported in
  $[\lambda^{-1},\lambda]$. It is what "$QW_\lambda(g)\ll\|g\|^2$" means at their `:197`,
  and what Figure 22's caption "Eigenvector for the smallest eigenvalue of $QW_\lambda^+$"
  refers to. The same convention holds in Connes–Consani–Moscovici arXiv:2310.18423, where
  the Weil form is written $Q_n$ and $W_\lambda$ is again the prolate operator.

The corpus splits this symbol, and does so inconsistently:

- `start.tex:41-44` and `:208-210` read it as $Q\circ W_\lambda$ with "$W_\lambda$ the
  truncated Weil operator/form" and "$Q$ removes the expected low-dimensional exceptional
  sector".
- `s3.tex:122` reads it the other way: "Let $Q$ denote the Weil quadratic form,
  $W_\lambda$ the relevant finite/prolate operator". This assignment matches
  Connes–Consani for $W_\lambda$ and for $Q$'s *meaning*, while still treating them as two
  objects.

Under the published reading, `start.tex:39`'s central unresolved estimate
$QW_\lambda(Eh_\lambda)\asymp 1-\chi_4$ is simply "**the Weil quadratic form evaluated at
$\mathcal E(h_\lambda)$** is of order $1-\chi_4$" — a statement about one number, with no
projection $Q$ anywhere in it, and directly comparable to Connes–Consani's Figures 18–21.

**This bears on Gate 2 and I have not resolved it.** Per the work item, Gate 2 (what $Q$
removes) is Daniel's, and the reading above is a fact about Connes–Consani's notation, not
a decision about what `start.tex` intends. Two things are worth handing over with it:
(i) if $Q$ is real and separate, it needs a definition that Connes–Consani do not supply;
(ii) if it is not, then the corpus's "codimension-two space" at `start.tex:80-82` is
already the whole of the removal, because $\mathcal E$'s domain $\mathcal S_0^{ev}$ **is**
$\{f(0)=\hat f(0)=0\}$ — the two removed directions are conditions on the test function,
imposed before $\mathcal E$ is applied, not a projection applied after $W_\lambda$.
mg-8d74's observation at `s3-sign-blindness.md:89-91` — that under one reading of $Q$ the
endpoint items do not enter at all — is the same fork seen from the other side.

Likewise for Gate 1 (which places $W_\lambda$ contains): under the published reading,
$QW_\lambda$ is the Weil form on test functions supported in $[\lambda^{-1},\lambda]$, and
Connes–Consani's own Figures 7–17 show it acquiring the contribution of the prime $p$ as
$\mu$ passes $p$. That is the "**finitely many primes**" branch of
`signed-geometry-proposals.md:388-390` — the primes $p\le\mu=\lambda^2$. I record that
this is what the literature's object does; whether it is what `start.tex` means is Gate 1
and remains Daniel's.

### 4.4 What in the corpus is NOT accounted for by the published work

This is the only place a new contribution can live, so it is stated conservatively —
anything I found in the literature has been removed from the list. **Narrowed 2026-08-12; the note after the list scopes it. All five items below stand.**

1. **The mirrored endpoint constraint, and its quantification.** Connes–Consani build
   $\varphi_{2n}$ to satisfy $\varphi(0)=0$ *exactly*, and rely on the prolate
   near-eigenfunction property $\widetilde{\mathcal F}\psi\simeq\pm\psi$ to make
   $\hat\varphi(0)$ small — which they need, since $\mathcal E$'s domain requires
   **both** conditions. They never size the residual. The corpus imposes
   $\hat h_\lambda(0)=0$ exactly (`start.tex:171`) and derives
   $h_\lambda(0)=\alpha h_{0,\lambda}(0)(\chi_4-\chi_0)/\chi_4=O(1-\chi_4)$
   (`start.tex:177-186`). **The trade is the same trade with the endpoints swapped; the
   sizing of the residual is not in Connes–Consani.** So `start.tex:189-196`'s
   "exceptional sector $=0+O(1-\chi_4)$" is a *quantification of a step the published
   construction takes approximately*, which is a real if modest contribution — and it is
   not the "main new structural result" `start.tex:198` claims. mg-aedf independently
   showed (`s3-reduction-audit.md:269-272`) that the two boxed identities are one fact,
   which is consistent with this reading.
2. **mg-aedf's exact constant.**
   $\|(1-\widehat P)h_\lambda\|_2^2=\tfrac8{11}(1-\Lambda_4)(1+O(c^{-4}))$
   (`s3-reduction-audit.md:207`), with $|\beta|^2\to 8/11$ from the fixed-index Hermite
   limit. I found nothing of this shape in the literature. It is small, it is checkable,
   and it is ours.
3. **mg-aedf's arithmetic bound.** That `start.tex:180-181` holds to 8 digits at $c\le12$,
   is ~10% wrong at $c=16$ and meaningless at $c=20$ in double precision
   (`s3-reduction-audit.md`, and the vision document's settled table). This is a fact about
   the corpus's own numerics; nobody else would publish it, and it is the reason the
   corpus's numbers cannot currently be quoted. Note that the published groups work at
   200-digit precision (§6).
4. **The $S^3$ / arithmetic-topology overlay.** Genuinely absent from this literature —
   and mg-8d74 already established it is invariant under $W_\lambda\mapsto-W_\lambda$, so
   it is a residue with no value. Recorded for completeness, not as an asset.
5. **The sign-blindness lemma as an audit rule** (`signed-geometry-proposals.md:104-109`) and
   the Davenport–Heilbronn test (`s3-sign-blindness.md` §7). Trivial as mathematics; not
   standard as a stated discipline. Worth keeping as method, not claimable as a result.

**Removed from an earlier draft of this list**, because they are published: the phase rule
(§3, note on B1); the codimension-two test space; the identification of the near-null
direction with $\mathcal E$ of a prolate combination; the exponential decay of the smallest
eigenvalue.

> **NARROWING APPLIED IN PLACE, 2026-08-12 (mg-03f0, applied mg-6d7e). Scope: one entry
> joins the "removed because published" paragraph. Nothing leaves the numbered list.**
>
> The entry is **the identification of the controlling scale** — §4.2 row 14. Connes,
> arXiv:2602.04022 (`rhready.tex:1149`), names the rate as $1-\chi_2$ = the corpus's
> $1-\chi_4$ and gives its asymptotic; the same paragraph (`:1159`) defines
> $k_\lambda:=\mathcal E(h_\lambda)$ with $h_\lambda$ *"the only linear combination of
> $h_{0,\lambda},h_{4,\lambda}$ with vanishing integral"*, which is `start.tex:138-153`
> and `:171` in the same letters. That is the whole of the change.
>
> **Item 1 stands, and the reason is worth stating because it is easy to get backwards.**
> Item 1's claim is the *sizing* of the endpoint residual: imposing $\hat h_\lambda(0)=0$
> exactly leaves $h_\lambda(0)$, and `start.tex:177-186` sizes it as $O(1-\chi_4)$. The
> survey states the construction and not the sizing, so the residual is unbounded in the
> literature — and now for the principals' own $k_\lambda$, since `:1159` shows they make
> the same endpoint choice the corpus does. Item 1's second half is therefore *sharper*
> after the narrowing, not weaker. What the narrowing does cost item 1 is the implicit
> suggestion in its first half that the endpoint *swap* is the corpus's own move: it is
> not, it is the survey's too. The residue is the quantification, exactly as item 1 says.
> §7 item U7 — whether anyone sizes the residual — ~~remains **open**~~ **CLOSED as a
> negative, 2026-08-12 (mg-555b): they do not, and the source says so in its own words
> ("act as if"). See §7 and [`semilocal-gap.md`](semilocal-gap.md) §10.5.** Item 1 rests
> on it and is unchanged in substance; what changes is that the support is now a sourced
> negative instead of a skim.
>
> Items 2–5 are untouched, and this narrowing bears on none of them.

### 4.5 The one thing the corpus is missing that the published work has

`start.tex` never says **why** $E h_\lambda$ is nearly null. It offers the two endpoint
cancellations and then asks for the tunnelling estimate. Connes–Consani give a reason in
one line: *the radical of the Weil quadratic form contains the range of $\mathcal E$*
(arXiv:2106.01715 §3), so $\mathcal E$ of **anything** in $\mathcal S_0^{ev}$ is in the
near radical, and the prolate input is needed only to force the support into
$[\lambda^{-1},\lambda]$ — which is what the Slepian–Pollak approximate intersection
$P_\lambda\cap^0\widehat P_\lambda$ is for. They are explicit that the construction "only
uses the prolate vectors without any reference to $QW_\lambda$".

If that is right, then the smallness has nothing to do with the geometry and only
partly to do with the prolate leakage: it is the range of $\mathcal E$. Whether the
*residual* is $\asymp 1-\chi_4$ is exactly the corpus's open question and is not answered
there. Recorded, not pursued — this is where the ticket's scope ends.

### 4.6 The "Figure 4" attribution — unsupported

`start.tex:88-91`: "CCM's finite-$\lambda$ calculations reveal a striking almost-null
direction. Their numerical Figure 4 suggests that its defect is controlled by a prolate
concentration eigenvalue."

Checked in all three candidate papers:

- **Connes–Consani, arXiv:2106.01715 (the paper with the numerics).** Figure 4 is
  "Coefficient of $\theta_{\mathrm{sym}}(0)/2$. Its value at $L=\log2$ is 2.00963" — part
  of §2's archimedean-contribution analysis. It is not about the near-null direction and
  says nothing about a concentration eigenvalue. The figures that *do* show the near-null
  behaviour are **Figures 18–21** (§2.5, "Semi-local Weil quadratic form, small
  eigenvalues"): $\log s(L)$ against $\mu=e^L$, exponential decay, with the count of small
  eigenvalues growing like $\mu$ (Figure 20). Figures 22–24 show the eigenvectors, and
  Figures 26–41 the agreement of the $\varepsilon_n$ with them.
- **Connes–Consani, arXiv:2006.13771 (Selecta).** Figure 4 is "Graph of
  $2\theta'(t)+\hat\delta(t)$ in $[-1,1]$" — a non-negativity check.
- **Connes–Consani–Moscovici, arXiv:2310.18423.** Contains no figures.

So the sentence is unsupported as written. The *phenomenon* is real and published (row 10
of §4.2); the pointer is wrong, and the second half — "controlled by a prolate
concentration eigenvalue" — is the corpus's own interpretation, which the cited source does
not make. `start.tex:88-91` should point at Figures 18–21 and attribute the interpretation
to itself. (Constraint respected: not edited. Reported.)

---

## 5. The Groskin lead — settled

**arXiv:2607.02828**, Akiva Groskin, *A finite Guinand–Weil dictionary and archimedean tail
order for the truncated Weil quadratic form* (2 Jul 2026; math.NT, math.SP).

**Not a collision, as the work item guessed** — no prolate functions, no Sonin space, no
sign analysis. Its two theorems are (i) every real even Galerkin coefficient vector $v$
determines in closed form a band-limited Guinand–Weil test function whose zero sum equals
$\langle v,Qv\rangle$ exactly, and (ii) the omitted archimedean tail beyond the Galerkin
band is a totally positive Cauchy–Stieltjes increment, giving a two-sided certification
rule with an explicit budget $B_T\sim(2N+1)\rho\log T/(\pi^2T)$, $\rho=2\pi/\log c$. It
explicitly disclaims any RH consequence.

**But the cutoffs are the same construction, and this is worth knowing.** Groskin's $c$ is
the **prime cutoff** of the Connes–van Suijlekom truncation: it bounds the primes $p\le c$
entering the von Mangoldt sum, and the form acts on $L^2([0,L])$ with $L=\log c$.
Connes–Consani's cutoff is the support bound: test functions in $[\lambda^{-1},\lambda]$,
circle length $L=2\log\lambda=\log\mu$ with $\mu=\lambda^2$ — and their Figures 7–17 show
the prime $p$ entering exactly as $\mu$ passes $p$. So $L_{\text{CvS}}=L_{\text{CC}}$ gives

$$c_{\text{Groskin}} \;\longleftrightarrow\; \mu=\lambda^2, \qquad
c_{\text{ours}}=\gamma=2\pi\lambda^2=2\pi\,c_{\text{Groskin}} ,$$

the last equality because Connes–Consani's prolate parameter is $\gamma=2\pi\lambda^2$ and
that is what `verify_prolate_claims.py` calls $c$. *(~~This dictionary is argued here from
the two definitions; neither paper states it.~~ **CORRECTED 2026-08-12, mg-882b: Groskin does state $\lambda^2=c$ — `main.tex:433`, `:1095` of arXiv:2605.20224 — and the remaining factor $2\pi$ is now measured. §7 U8, §12.**)*

Two consequences:

- **mg-aedf's numerics are at a much smaller cutoff than the published ones.** $c\le20$
  in our scripts is $\mu\le3.2$ — only the primes 2 and 3 contributing, and the very
  bottom-left of Connes–Consani's Figures 18–21, which run to $\mu\approx8$. Groskin's
  $c=13\ldots100$ is $c_{\text{ours}}=82\ldots628$. The corpus has never computed in the
  regime the literature reports.
- **The Galerkin band $N$ is a second truncation the corpus does not have.** Groskin's
  truncation is two-parameter ($c$ and $N$); the corpus truncates only in $c$ and works in
  the **prolate** basis rather than a Fourier/Galerkin one. So the constructions coincide
  in the cutoff and differ in the discretisation.

---

## 6. The corner is not empty — a sweep

The corpus has assumed it is alone here. It is not. Live work on the truncated Weil form /
prolate–zeta intersection, found on this pass:

| ref | what |
|---|---|
| Connes–Consani, arXiv:2106.01715, Enseign. Math. **69** (2023) 93–148 | the small eigenvalues, the prolate construction, the numerics. **The corpus's actual base paper** |
| Connes–Consani, Selecta Math. **27** (2021), arXiv:2006.13771 | Weil positivity at the archimedean place, via the Sonin space |
| Connes–Moscovici, PNAS **119** (2022) e2123174119, arXiv:2112.05500 | UV prolate spectrum $\leftrightarrow$ zeros of $\zeta$ |
| Connes–Consani–Moscovici, arXiv:2310.18423 (Oct 2023, rev. May 2024) | semilocal prolate operator; stability of the semilocal Sonin space; strategy for semilocal Weil positivity |
| Connes–van Suijlekom, Comm. Math. Phys. **383** (2021) 2021–2067, and *Quadratic forms, real zeros and echoes of the spectral action* (2026) | the truncation whose cutoff is a prime bound; a $C^*$-algebraic proof of a Carathéodory–Fejér corollary. The ground state of the truncated Weil matrix has Fourier–Mellin zeros provably on the critical line |
| Connes–Consani–Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755 (2025) | $D^{(\lambda,N)}_{\log}$; convergence of regularised determinants towards $\Xi$ |
| Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096 (Jun 2026) | unifies Yoshida (1992), Bombieri (2001, 2003), Connes–Consani (2023), CCM (2025+) via the screw function; studies the distributional Weil form by continuous functions |
| Groskin, arXiv:2605.20224 (May 2026), arXiv:2607.02828 (Jul 2026) | first public implementation of the CvS Galerkin matrix, $c=13\ldots67$ and $c=100$, $N$ up to 250; the finite Guinand–Weil dictionary |
| arXiv:2607.24830, arXiv:2601.12133 (2026) | numerical realisation of Suzuki's operator; spectral analysis of $D^{(\lambda,N)}_{\log}$ |
| Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, arXiv:2602.04022 (2026) | Connes' own current survey — the natural place to check positioning before writing |

Two facts from this sweep are directly actionable:

1. **Precision.** Connes–Consani–Moscovici compute at **200 digits**; Groskin reports a
   smallest-positive even-sector eigenvalue $\sim10^{-334}$ at $c=100$, $N=250$. mg-aedf's
   finding that the corpus's numerics are meaningless in double precision at $c=20$ is not
   a marginal caveat — it is a two-orders-of-magnitude gap in *methodology* from everyone
   else working on the same object.
2. **The one open niche, and the corpus is standing in it.** Groskin (arXiv:2605.20224)
   states plainly: "A prolate-basis implementation of the CvS Galerkin would be a genuinely
   distinct path in the literature — potentially valuable as an independent cross-check —
   but is not yet reported by any group." The corpus works in the prolate basis. That is
   the only place found on this pass where the corpus's *technique*, as opposed to its
   objects, is not duplicated.

---

## 7. Unresolved — recorded, not dropped

| # | item | why unresolved |
|---|---|---|
| U1 | ~~Bochner–Schwartz on a general LCA group~~ **CLOSED 2026-08-12, mg-882b — the theorem exists, at exactly that generality** | A. Wawrzyńczyk, *On tempered distributions and Bochner–Schwartz theorem on arbitrary locally compact Abelian groups*, Colloq. Math. **19** (1968) no. 2, 305–318. Theorem 4.2 (p. 315): *"Let $G$ be a separable group. Every positive-definite element $T\in\mathbf D'(G)$ is represented by a positive Borel measure $m$"*, $T(\varphi)=\int\hat\varphi\,dm$ — with the **Remark**, same page, *"The assumption of separability can be removed."* Theorem 4.3 (p. 316): *"The measure $m$ can be extended in a unique way to a tempered distribution on $\Gamma$"*, i.e. $m$ is tempered. Together these are Bochner–Schwartz on an arbitrary LCA group, and they are **stronger** than our use needs: the hypothesis is a positive-definite $T\in\mathbf D'(G)$, not a tempered one. $C_{\mathbb Q}$ is second countable, so the separability caveat does not bite either way. Read from the scanned journal PDF. §12 |
| U2 | ~~Deninger ICM 1998 at page level~~ **CLOSED 2026-08-12, mg-882b — confirmed against the text, page by page** | Read from the Documenta Mathematica PostScript of the article itself (`Deninger.MAN.ps`, dated 1998-11-10). **p. 168:** $H^0(\text{"Spec }\mathbb Z\text{"},\mathbb R)=\mathbb R$ with $\Theta=0$; $H^1$ infinite-dimensional, spectrum of $\Theta$ = the non-trivial zeros; $H^2=\mathbb R$ with $\Theta=\mathrm{id}$. **p. 170,** Proposition 3.2 and eq. (5): $\Phi(0)-\sum_{\hat\xi(\rho)=0}\Phi(\rho)+\Phi(1)=\sum_p\log p\sum_k\varphi(k\log p)+\int_0^\infty\varphi(t)(1-e^{-2t})^{-1}dt$, reformulated as $\sum_i(-1)^i\operatorname{Tr}(\Theta\mid H^i)_{\text{dis}}$; **p. 171** eq. (6) is the sheaf-theoretic Lefschetz form. **p. 181:** closed orbits $\leftrightarrow$ primes with $l(\gamma)=\log p$; leaves two-dimensional; *"Thus 'Spec Z' … should have dimension three"*. One notation caveat: Deninger's $\Phi(s)=\int\varphi(t)e^{ts}dt$, not a Fourier hat. §12 |
| U3 | ~~Slepian 1965 uniform-error version of the Hermite limit~~ **CLOSED 2026-08-12, mg-882b, as a NEGATIVE — it is not there, and the literature says so** | I could not open Slepian 1965 (Wiley, DOI 10.1002/sapm196544199, HTTP 403; no other copy found — the search is described in §12). What settles it is a specialist's characterisation in print, from a paper this corpus has **already** imported and read at source level: Dunster, arXiv:1601.00699 = J. Classical Anal., `PSWF_JCA.tex:175-181`, *"The literature contains many asymptotic approximations and expansions (see [2], [7], [14], [21], [23], **[31]**, [35], [40]), but most are heuristic, all parameters fixed except $\gamma$, and with little or no error analysis"* — and **[31] is Slepian 1965** (31st `\bibitem`, verified by count). "All parameters fixed except $\gamma$" is the fixed-index regime; "little or no error analysis" is the negation of a uniform-error statement. Concurring: Bonami–Karoui (2016) is still *"push[ing] forward the uniform approximation error bounds"* in 2014, and cites Slepian 1965 in its bibliography but **nowhere in its body**. §12 |
| U4 | ~~Fuchs 1964, the exact constant $4\sqrt\pi\,8^nc^{n+1/2}e^{-2c}/n!$~~ **CLOSED 2026-08-12, mg-03f0** *(struck here 2026-08-12, mg-882b: the closure was recorded only in the right-hand cell, so this table read open while the record said closed — see §12)* | Source confirmed (JMAA **9** (1964) 317–330); the constant not checked against the paper. mg-aedf verified the $c^{-4}$ *ratio* numerically at $c=8\ldots14$ and reported the constant "converging (slow)" (`s3-reduction-audit.md:183-185`), which is consistent with but not a check of the formula **CLOSED 2026-08-12, mg-03f0 — the constant is right.** Connes states the asymptotic for the same quantity independently (arXiv:2602.04022, `rhready.tex:1149-1150`); with $\chi=\sqrt\Lambda$ the two expressions agree to twelve decimals at every $L$. See [`semilocal-gap.md`](semilocal-gap.md) §5.3 and check 2 of `verify_semilocal_gap.py`. |
| U5 | "the 2023 trace formula" (`start.tex:46,242,425`) — **OPEN, and Daniel's** | Two candidates (§4.1), and the phrase is used for the thing to be *specialised to $h_\lambda$* at `start.tex:244-246,425`. Which paper is meant determines whether step 1 of `start.tex:348-356` is a computation in Connes–Consani 2023 or in CCM 2310.18423. Only Daniel can say. **Deliberately left open by mg-882b**, which closed every other row: this one asks what the corpus's author intended, not what a source says, and no amount of reading settles it. It is the only row in this table that is not a question about the literature |
| U6 | ~~whether the corpus's $h_{4,\lambda}$ means prolate index 4 or Connes–Consani's index $m=4$~~ **CLOSED 2026-08-12, mg-9433 — prolate index 4** | Their $\psi_{m,\lambda}:=\mathrm{PS}_{2m,0}$, so their $m$ is half the prolate index, and the collision was real. But `start.tex:138-145` transcribes **Connes–Consani–Moscovici's** $\psi^+_\ell:=h_{4\ell}-\frac{h_{4\ell}(0)}{h_0(0)}h_0$ at $\ell=1$ (arXiv:2310.18423 source line 624), in Hermite functions indexed in full — same letter $h$, both subscripts, and "the CCM choice of coefficients" is that formula. mg-aedf's constants stand. Note the method: `start.tex:180-181` **cannot** discriminate — it holds exactly for every $m\equiv0\bmod4$ — so this was settled from the sources, not numerically. See §10 and [`index-convention.md`](index-convention.md) |
| U7 | whether Connes–Consani anywhere size the residual $\hat\varphi(0)$ | ~~I read §3 and §2.5 and the abstract … absence of evidence over ~40 pages skimmed, not a proof of absence.~~ **CLOSED 2026-08-12 (mg-555b): they do not, and it is now a sourced negative rather than a skim.** The construction is `Spectraltriples.tex:744` ($\phi_{2n}:=\psi_{2n}\psi_0(0)-\psi_0\psi_{2n}(0)$, imposing $\phi_{2n}(0)=0$ exactly) and the other condition is disposed of at `:746` in their own words — *"one may **approximate** $\mathcal F(\phi_n)$ by $(-1)^n\phi_n$ and … **act as if**"* — with no error term there or where the construction is used. The two places whose titles promise a sizing do not contain one: the appendix *"Size of $\mathcal F_\mu\circ w$(Prolate)"* (`:1547`) is the $\lambda\to\infty$ **Hermite** limit, where both conditions hold *exactly* (`:1563`); and the survey's $c\lambda^{-1/2-\alpha}(1-2\alpha)^{-1}$ (`rhready.tex:1172`) bounds $\hat k_\lambda\to\hat k$, a different quantity. §4.4 item 1 still rests on this and is now on firmer ground. Full account, with a closed-form lead marked *ours*: [`semilocal-gap.md`](semilocal-gap.md) §10.5 |
| U8 | ~~the $c_{\text{ours}}=2\pi c_{\text{Groskin}}$ dictionary~~ **CLOSED 2026-08-12, mg-882b — the dictionary is right, and "neither paper states it" was wrong** | Two halves. **(a) $c_{\text{Groskin}}=\lambda^2=\mu$ is stated by Groskin**, arXiv:2605.20224 `main.tex:433` (*"adopt the convention $\lambda^2=c$ from CCM throughout"*), `:1095` (*"With $\lambda^2=c$, this is $L=\log c$, so $e^L=c$"*), and `:284-287` (*"For a cutoff parameter $c$ (controlling the primes $p\le c$ …), set $L=\log c$. The quadratic form acts on $L^2([0,L])$"*) — so §5's parenthetical is corrected in place. **(b) the factor $2\pi$ is measured**, [`verify_citation_u8.py`](verify_citation_u8.py): the corpus's own arbitrary-precision eigensolver gives $1-\sqrt{\Lambda_4(\kappa\mu)}$ agreeing with Connes' asymptotic (a function of $\mu$ alone) only at $\kappa=2\pi$ — the neighbours $2,\pi,4\pi$ are wrong by $10^{9}$ to $10^{53}$ across $\mu=4\ldots10$. Corroborated after the fact by Connes' own footnote at `rhready.tex:1149`: *"$\chi_k(\lambda)^2=\lambda_{2k}(a)$ with $a=\sqrt{2\pi}\lambda$"*, i.e. $a^2=2\pi\lambda^2$. §12 |
| U9 | ~~Bonami–Karoui volume/pages~~ **CLOSED 2026-08-12, mg-882b — 15–45** | Constr. Approx. **43** (2016), no. 1, **15–45**; DOI [10.1007/s00365-015-9295-1](https://doi.org/10.1007/s00365-015-9295-1); published online 17 Jun 2015, in print Feb 2016. From the publisher's own Crossref deposit (`api.crossref.org/works/10.1007/s00365-015-9295-1`), not from a search-result summary; the Springer article page itself refuses unauthenticated fetches. Preprint arXiv:1405.3676. §12 |

---

## 8. What this changes, per document

Not edits — a list for whoever writes next. `start.tex` and `s3.tex` are not to be edited
(work-item constraint) and have not been.

**`start.tex`.**
- §1 and §3 need a citation to Connes–Consani, arXiv:2106.01715 / Enseign. Math. 69 (2023).
  `:54-58` is that paper's (3.1); `:80-82` is its $\mathcal S_0^{ev}$; `:88` is its abstract.
- `:88-91` "Figure 4" is unsupported; the near-null figures are 18–21 (§4.6).
- `:198` "This is the main new structural result" overstates: §4.4 item 1.
- `:41-44`, `:208-210` split $QW_\lambda$; §4.3. Gate 2.
- "CCM" is a two-author paper for everything the corpus uses; §4.1.

**`s3.tex`.**
- `:122` splits $QW_\lambda$ differently from `start.tex`; §4.3.
- `:55-78` is Slepian–Pollak double orthogonality, as mg-aedf already found
  (`s3-reduction-audit.md:98`); Connes–Consani cite the same source (their §3).

**`s3-reduction-audit.md`.** B1–B4 hold; ~~U3, U4, U6 open~~ **all three now closed — U6 by
mg-9433, U4 by mg-03f0, U3 by mg-882b as a negative (§12); annotated there in place.** §3's note on B1: the phase fact is in Connes–Consani; the mode-4 *selection* is not.

**`s3-sign-blindness.md`.** B5–B11 all hold, including the round-$S^3$ falsifier. The
"citations unverified" caveat at `:421-424` can be replaced by a pointer to this note.

**`signed-geometry-proposals.md`.** A1, A4–A6, A11–A13 hold. A2, A3, A7, A9, A10 need the
narrowings of §2.1–§2.5. §4's central claim is confirmed and should be strengthened (§4.2).
Its §8 item 3 — the ticket this note answers — is done, and its answer is yes.

> **Applied to the three notes, 2026-08-12 (mg-2179).** The three paragraphs above are
> no longer a to-do list: the narrowings, the caveat replacement and the §4 strengthening
> have been made in place in the notes themselves, each annotation naming the audit row
> (A2, A3, A7, A9, A10, B1–B4, §4.2, §4.3) that licenses it. Nothing was deleted — the
> original over-claims stand alongside their narrowings, so this note's findings remain
> checkable against the text they corrected. `start.tex` and `s3.tex` were **not**
> touched: the six defects listed above for them are reported to Daniel by pm-riemann.
> Every line anchor in this note that pointed into a changed note was renumbered and
> re-verified against the passage it describes; one anchor (A9's `:465-467`, §2.4) was
> found to have been two lines past the claim it quotes and now reads `:598-599`, and
> the `s3-sign-blindness.md` caveat anchor just above, which mg-687b's renumbering pass
> missed, was `:379-382` and is corrected here.

---

## 9. This note, audited by its own rule

A citation audit is a document full of citations, so it is subject to the defect it
remedies. Recorded so a reader can weight the rows above:

**Bibliographic data taken from a primary source I read** — Connes–Consani–Moscovici's own
bibliography (arXiv:2310.18423, refs [7],[10],[11],[12],[16]) and Connes–Consani's
(arXiv:2106.01715): A1, A5, A6, B3 (Osipov–Rokhlin–Xiao), B1 (Slepian–Pollak pages), the
Connes 1999 semilocal trace formula, Enseign. Math. 69 (2023) 93–148.

**Bibliographic data taken from a search result, not a primary source**: A8 (Deninger,
Doc. Math. page range), A9 (Faltings, Ann. of Math. **119** (1984) 387–424; Hriljac, Amer.
J. Math. **107** (1985) 23–38), A11, A13, B2, B4, B7 (APS volumes/pages — note that
sources disagree on whether part II is dated 1975 or 1976), B8–B10, and the §6 table.
Volumes and pages there are one remove from the journal.

**Content claims I checked against the actual text of the paper**, not against an abstract
or a summary: everything in §4.2, §4.3, §4.5, §4.6 (read in arXiv:2106.01715, extracted
from the PDF), §2.2 (arXiv:2006.13771), §4.1 and A6 (arXiv:2310.18423, extracted from the
PDF), §5 (arXiv:2607.02828 and arXiv:2605.20224 abstracts and metadata).

**Content claims resting on an abstract, a summary, or secondary literature**: A2's
semilocal status (the papers' own framing sentences, which I did read, but not their full
bodies), A7's Artin–Verdier caveat, A8 (see U2), B2, B4 (see U3, U4), the §6 one-line
descriptions.

**The claim in this note that would do the most damage if wrong** is §4.3 — that
$QW_\lambda$ is a single symbol in Connes–Consani. It rests on reading their §3 and the
Figure 22–24 captions ("Eigenvector for the smallest eigenvalue of $QW_\lambda^+$"), where
no operator $Q$ is ever introduced and $W_\lambda$ is defined by their eq. (3.3) as the
prolate operator. It is checkable in one minute by anyone with the paper, which is the
standard the rest of this note is written to.

---

## 10. Appendix — U6 closed, and §4.3 checked against source (added 2026-08-12, mg-9433)

*Appended. Nothing above is deleted; the U6 row in §7 is annotated in place.
Full account: [`index-convention.md`](index-convention.md).*

### U6 is closed: prolate index 4

`start.tex:138-145` transcribes **Connes–Consani–Moscovici's**
$\psi^+_\ell:=h_{4\ell}-\frac{h_{4\ell}(0)}{h_0(0)}h_0$ at $\ell=1$ (arXiv:2310.18423,
source `mainc2m24fine.tex` line 624), built from **Hermite** functions in the full
index — CCM state $\fourier_{e_\R}(h_{2m})=(-1)^mh_{2m}$ at line 622 and transport the
$h_{2n}$ to finite $\lambda$ as the prolate operator's eigenfunctions at line 616. Same
letter $h$, both subscripts, and "the CCM choice of coefficients" (`start.tex:147`) is
that formula's $-h_4(0)/h_0(0)$. mg-aedf's constants stand unchanged.

**Correction to §4.2 row 8.** That row maps `start.tex:138-145` to Connes–Consani's
$\varphi_{2n}$. The *construction* correspondence is right and the "mirrored endpoint"
verdict is right — CC impose $\varphi_n(0)=0$ and carry the residual on the Fourier
side; the corpus imposes $\widehat h_\lambda(0)=0$ and carries it at the endpoint. But
the **labelling** the corpus uses is CCM's, not CC's, and that is the whole of U6: under
CC's $\psi_{m,\lambda}:=\mathrm{PS}_{2m,0}$ the same object is $\psi_{2,\lambda}$, not
$\psi_{4,\lambda}$.

**Method note, because it matters for anyone re-checking.** `start.tex:180-181` —
the identity that looked like a discriminator — **cannot** settle this. In arbitrary
precision it holds exactly for **every** partner mode $m\equiv0\pmod4$ and fails for
every $m\equiv2\pmod4$; it is equivalent to $i^{\,m}=+1$ and carries one bit. U6 was
settled from the sources, not numerically.

### §4.3 confirmed from primary source, both halves

The claim §9 flags as the most damaging if wrong. Read from `Spectraltriples.tex`
(arXiv:2106.01715 LaTeX source), not from rendered HTML:

- **line 169:** "By semi-local Weil quadratic form we mean the restriction $QW_\lambda$
  of the sesquilinear form …". $QW_\lambda$ is a single symbol, defined as the Weil
  quadratic form. No operator $Q$ appears in the paper.
- **lines 713, 717:** `({\bf W}_{\lambda}\psi)(q)=-\partial((\lambda^2-q^2)\partial)\ldots`;
  "The operator ${\bf W}_{\lambda}$ … is selfadjoint and positive and its eigenfunctions
  are the prolate spheroidal wave functions."

And the mechanism of the corpus's error is now visible: `W_\lambda` occurs 41 times in
that file, **every one inside `QW_\lambda`**, while the prolate operator occurs 4 times
and only in **bold**, `{\bf W}_{\lambda}`. Two different objects in one section,
separated by a font. §4.3 stands as written and can be quoted.

### Gate 1's published-reading answer is now verbatim, not inferred

§4.4 / the vision document read *finitely many primes* off Figures 7–17. Line 169 says
it: $QW_\lambda$ "only involves primes less than, say, $\lambda^2$". That is the middle
branch of `signed-geometry-proposals.md:388-389`, and it upgrades the partial answer at
`:399-404` from a reading of figures to a statement in the text. Still Daniel's to
confirm that it is what `start.tex` means.

### Provenance of this appendix

All four items above are from arXiv LaTeX sources downloaded from `arxiv.org/e-print/`
and read directly — `Spectraltriples.tex` (2106.01715) and `mainc2m24fine.tex`
(2310.18423, 99,875 bytes, dated 2024-05-04). Line numbers are lines of those files.
This is a stronger provenance than §9 records for the same passages, which is why items
this note left open can be closed here. It is not the published journal text.

---

## 11. Appendix — two rows revisited from a source this pass named but did not open (added 2026-08-12, mg-03f0; heading corrected mg-6d7e — the survey predates this pass, see §6)

*Appended. Nothing above is deleted; the two rows affected are annotated in place,
line-count-preserving, and both point here. Full account:
[`semilocal-gap.md`](semilocal-gap.md).*

This pass checked arXiv:2006.13771, arXiv:2106.01715 and arXiv:2310.18423. It did
not check **A. Connes, *The Riemann Hypothesis: past, present and a letter through
time*, arXiv:2602.04022 (Feb 2026)** — §6 lists it as "Connes' own current survey —
the natural place to check positioning before writing", and that advice turns out
to have been right twice.

### §4.2 row 14 — narrowed, not overturned

Row 14 calls $1-\chi_4$-as-the-controlling-scale **corpus-specific**, on the
grounds that Connes–Consani report the smallest eigenvalue decaying exponentially
in $\mu$ "with no identification of the rate". That is accurate for
arXiv:2106.01715. It is not accurate about the literature: the 2026 survey
(`rhready.tex:1149-1150`) reports *"a striking similarity between the behavior of
$\epsilon(\lambda)$ and of the angular function $1-\chi_2(\lambda)$"*, gives the
Fuchs asymptotic for it, and — by the footnote $\chi_k(\lambda)^2=\Lambda_{2k}(c)$
— its $\chi_2$ is prolate index 4, i.e. the corpus's $\chi_4$
([`index-convention.md`](index-convention.md)).

The same survey writes $k_\lambda:=\mathcal E(h_\lambda)$ with $h_\lambda$ "the
only linear combination of $h_{0,\lambda},h_{4,\lambda}$ with vanishing integral"
(`:1159`) — which is `start.tex:138-153` and `:171`, same letters, same
construction. So the corpus is not only inside Connes–Consani 2023; its
distinguished vector and its controlling scale are both objects of the *current*
programme. **§4.4's residue list is unaffected — all five items, item 1 included; the
narrowing adds an entry to that section's "removed because published" paragraph and
takes nothing out of the list. Applied in place mg-6d7e; see the note at the end of §4.4.**

### §7 item U4 — closed

The Fuchs constant $4\sqrt\pi\,8^nc^{n+1/2}e^{-2c}/n!$
(`s3-reduction-audit.md:179`), recorded here as source-confirmed but
constant-unchecked, is **right**. Connes states
$1-\chi_2\sim\frac{2^{14}}{3}\sqrt2\,\pi^5e^{-4\pi e^L+9L/2}$ for the same
quantity; with $c=2\pi e^L$ and $1-\chi_2=(1-\Lambda_4)/2$ the two are the same
expression, and the ratio is $1.000000000000$ at $L=1.0,\dots,3.0$
(`verify_semilocal_gap.py`, check 2). This is documentary corroboration by a
third party rather than a reading of Fuchs' paper, which is why it also
independently corroborates the index convention: two constants written down by
different people for two quantities agree exactly only if the quantities are the
same one.

---

## 12. Appendix — §7 closed out: U1, U2, U3, U8, U9, and U4's row (added 2026-08-12, mg-882b)

*Appended. Nothing above is deleted; the six §7 rows affected are annotated in place,
line-count-preserving, and each points here. Companion script for U8:
[`verify_citation_u8.py`](verify_citation_u8.py).*

**Every remaining bibliographic row in §7 is now closed.** U1 and U2 close as
confirmations, U3 as a negative, U8 as a confirmation that also corrects §5, U9 as a
page range. **U5 is left open and is Daniel's** — it asks what `start.tex` meant, not
what a source says, and §7's row now says so.

Three of the five went the way the row expected. Two did not, and they are the ones
worth reading: **U3 is a clean negative** — the uniform-error statement is not in
Slepian 1965, and a specialist says so in print — and **U8's row contained a false
premise**, since one of the two papers it says states nothing does state half the
dictionary.

---

### 12.1 The bookkeeping defect, and the converse check

**The defect.** mg-03f0 closed U4 — mg-aedf's Fuchs constant agrees with Connes'
independently stated asymptotic to twelve decimals — and recorded the closure in the
row's *right-hand* cell only. The item cell was never struck through the way U6's and
U7's were, so §7's table read `U4 … open` while §11 and
[`semilocal-gap.md`](semilocal-gap.md) §5.3 read `U4 … closed`. Struck here.

Nothing about the mathematics changed; what was wrong was the thing a reader scans
first. That is the whole reason it mattered.

**The converse: is anything marked closed that was not?** No. All three prior closures
re-verified, from the arXiv LaTeX sources downloaded fresh for this pass:

| row | closed by | re-verified how | verdict |
|---|---|---|---|
| U4 | mg-03f0 | `rhready.tex:1149` read verbatim — the footnote and the displayed asymptotic $1-\chi_2\sim\frac{2^{14}}3\sqrt2\,\pi^5e^{-4\pi e^L+9L/2}$ are both on that line; and `verify_semilocal_gap.py` check 2 re-run here, ratio `1.000000000000` at $L=1.0,1.5,2.0,2.5,3.0$ | **genuinely closed** |
| U6 | mg-9433 | `mainc2m24fine.tex` **99,875 bytes, dated 2024-05-04** — exactly what §10 records — lines 616 (*"the eigenfunctions … are approximated by … the Hermite functions $\{h_{2n}\}$"*), 622 (*"$\fourier_{e_\R}(h_{2m})$ is $(-1)^mh_{2m}$"*), 624 ($\psi^+_\ell:=h_{4\ell}-\frac{h_{4\ell}(0)}{h_0(0)}h_0$) all read verbatim | **genuinely closed** |
| U7 | mg-555b | `Spectraltriples.tex:744` ($\phi_{2n}:=\psi_{2n}\psi_0(0)-\psi_0\psi_{2n}(0)$), `:746` (*"one may approximate … and … act as if"*), `:1547` (`\section{Size of $\fourier_\mu\circ w$(Prolate)}`), `:1563`, and `rhready.tex:1172` — all read verbatim | **genuinely closed** |

§10's own anchors were checked at the same time and also hold: `Spectraltriples.tex:169`
carries *both* sentences §10 quotes from it (*"…it only involves primes less than, say,
$\lambda^2$. By semi-local Weil quadratic form we mean the restriction $QW_\lambda$ of
the sesquilinear form"* — one long source line), `:713` and `:717` are the prolate
operator, and §10's font argument is exact: `QW_\lambda` occurs **41** times in that file
and `{\bf W}_{\lambda}` **4**, the counts §10 states.

One further page range checked while the tooling was up, because §3 marks it as taken
second-hand: **B1's Slepian–Pollak I is 43–63**, per the publisher's Crossref deposit for
DOI 10.1002/j.1538-7305.1961.tb03976.x. (Bonami–Karoui's own bibliography prints 43–64.
Ours is right and theirs is a typo.)

So the table had drifted once, in presentation, and not twice.

---

### 12.2 U1 — Bochner–Schwartz on a general LCA group: the theorem exists

§2.5 could find no reference for the *distributional* Bochner–Schwartz theorem on a
general LCA group, which is what `signed-geometry-proposals.md:484-497` applies to
$C_{\mathbb Q}$. There is one, and it is a paper whose title is the question:

> **A. Wawrzyńczyk**, *On tempered distributions and Bochner–Schwartz theorem on
> arbitrary locally compact Abelian groups*, **Colloq. Math. 19** (1968), no. 2,
> **305–318**.

Read from the scanned journal PDF (Polish Digital Mathematics Library, `cm19222.pdf`,
14 pages, pp. 305–318), not from a review. Its §4:

- **Definition 4.1** (p. 315) defines $\mathbf S'(G)$, the tempered distributions on an
  arbitrary LCA $G$, as the continuous linear functionals on the space $\mathbf S(G)$
  built in §3. Its abstract (p. 305): *"Our definition of the space $\mathbf S(G)$ is
  equivalent to the one given by Bruhat [1]. Theorems announced by him, the proofs of
  which have never been published in details, are formulated and proved in part 3 of the
  present paper."* Positive-definiteness is $T(\varphi^**\varphi)\ge0$,
  $\varphi\in\mathbf D(G)$.
- **Theorem 4.2** (p. 315), attributed there to Maurin: *"Let $G$ be a separable group.
  Every positive-definite element $T\in\mathbf D'(G)$ is represented by a positive Borel
  measure $m$ as follows: $T(\varphi)=\int\hat\varphi(\gamma)\,dm(\gamma)$."* Followed
  immediately by: *"**Remark.** The assumption of separability can be removed."*
- **Theorem 4.3** (p. 316): *"The measure $m$ can be extended in a unique way to a
  tempered distribution on $\Gamma$."*

4.2 and 4.3 together are exactly the statement §2.5 wanted: a positive-definite
distribution on an LCA group is the Fourier transform of a positive **tempered** measure
on the dual. Two things are worth stating precisely, because both cut in our favour:

1. **The hypothesis is weaker than our use needs.** 4.2 takes $T\in\mathbf D'(G)$ — a
   distribution, not assumed tempered. Positive-definiteness itself buys the
   temperedness of the representing measure. So the sentence at
   `signed-geometry-proposals.md:484-486` does not need to be hedged at all on this
   point.
2. **The separability caveat does not bite.** $\mathbb A_{\mathbb Q}$ is second
   countable ($\mathbb Q$ is countable), hence so are $\mathbb A^\times_{\mathbb Q}$ and
   the quotient $C_{\mathbb Q}$ — and the Remark removes the hypothesis anyway.

**What this changes.** §2.5's second bullet, and the U1 half of the annotation at
`signed-geometry-proposals.md:508-514`, should now read *holds*, with this citation. It
changes nothing downstream — that passage is diagnostic by its own statement — which is
the same thing §2.5 said, and remains the honest weight to give it. What it removes is a
hedge: "likely fine (Weil's own framework), but not checked" was the right thing to write
in ignorance and is now simply superseded.

---

### 12.3 U2 — Deninger ICM 1998, confirmed against the text

Obtained as the Documenta Mathematica article file itself — `Deninger.MAN.ps` (471,866
bytes uncompressed, internal timestamp 1998-11-10), from an EMIS mirror, converted to
text locally. Every page number below is the article's own running head; the footer on
every page reads *"Documenta Mathematica · Extra Volume ICM 1998 · I · 163–186"*, which
confirms the page range as well.

What §5(1) of `signed-geometry-proposals.md` asserts, item by item:

| claim at `signed-geometry-proposals.md:429-436` | where it is | verdict |
|---|---|---|
| 3-dimensional space, 2-dimensional leaves | **p. 181**: *"The leaves on 'Spec Z' … should be two … dimensional in a suitable sense … Thus 'Spec Z' … should have dimension three"*, and *"There are to be one-codimensional foliations"* | **holds** |
| leafwise $H^1$ carries the zeros as the spectrum of the infinitesimal generator | **p. 168**: *"$H^1(\text{"Spec }\mathbb Z\text{"};\mathbb R)$ is infinite dimensional, the spectrum of $\Theta$ consisting of the non-trivial zeroes $\rho$ of $\zeta(s)$ with their multiplicities"* | **holds** |
| Lefschetz trace formula reproducing the explicit formula | **p. 170** eq. (5) and **p. 171** eq. (6): $\sum_i(-1)^i\operatorname{Tr}(\Theta\mid H^i)_{\text{dis}}=\sum_{p\le\infty}\operatorname{Tr}(\Theta\mid R_p)_{\text{dis}}$, *"a sheaf theoretic Lefschetz trace formula"* | **holds** |
| closed orbits $\leftrightarrow$ primes | **p. 181**: *"The closed orbits should correspond to the prime numbers such that $l(\gamma)=\log p$"* | **holds** |
| $H^0$ and $H^2$ $\leftrightarrow$ the two pole terms | **p. 168**: $H^0=\mathbb R$ with $\Theta=0$, $H^2=\mathbb R$ with $\Theta=\mathrm{id}$; **p. 170**, Proposition 3.2: $\Phi(0)-\sum_{\hat\xi(\rho)=0}\Phi(\rho)+\Phi(1)=\sum_p\log p\sum_{k\ge1}\varphi(k\log p)+\int_0^\infty\frac{\varphi(t)}{1-e^{-2t}}dt$. Since $\langle\operatorname{Tr}(\Theta\mid H)_{\text{dis}},\varphi\rangle=\sum_{\theta\in\operatorname{sp}\Theta}\Phi(\theta)$, the eigenvalue $0$ on $H^0$ contributes $\Phi(0)$ and the eigenvalue $1$ on $H^2$ contributes $\Phi(1)$, both with sign $+$ | **holds** |

**One notation caveat, and it is ours not his.** Our text writes the two pole terms as
$\hat f(0)+\hat f(1)$. Deninger's transform is $\Phi(s)=\int_{\mathbb R}\varphi(t)e^{ts}\,dt$
— a two-sided Laplace transform of the test function, evaluated at the *poles* $s=0,1$ of
$\hat\zeta$. The pairing our text describes is exactly right; the hat is a convention
imported from the explicit-formula literature and is not Deninger's. Worth one word if
that sentence is ever written up.

**What this changes.** The U2 half of the "Still open" bullet at
`signed-geometry-proposals.md:680-683` is discharged, and §9's placement of A8 moves: the
Deninger content is now *checked against the actual text of the paper*, not resting on
secondary literature. The A8 **bibliographic** entry (Doc. Math. Extra Vol. ICM I,
163–186) is now also primary — read off the article's own running footer.

---

### 12.4 U3 — the uniform-error version is not in Slepian 1965

**This is the negative, and it is stated plainly per the work item.**

**The search, described so it can be told apart from nobody having looked.** Slepian,
*Some asymptotic expansions for prolate spheroidal wave functions*, J. Math. and Phys.
**44** (1965) 99–140, is Wiley, DOI `10.1002/sapm196544199`. Both the DOI and the direct
`onlinelibrary.wiley.com` URL return **HTTP 403** unauthenticated. No preprint exists (the
paper predates arXiv by 26 years); it is not in the Internet Archive's Bell System
Technical Journal collection, which covers BSTJ and not J. Math. and Phys.; and searches
for a full-text copy returned only the paywall. **I did not read Slepian 1965.**

**What settles it anyway** is that a specialist has characterised that literature in
print, in a paper *this corpus has already downloaded, read at LaTeX-source level, and
depends on* — Dunster, arXiv:1601.00699 (J. Classical Anal.), the source of the G13 import
audited in [`dunster-check.md`](dunster-check.md). `PSWF_JCA.tex:175-181`:

> *"Despite being studied extensively over the decades there are significant gaps in the
> literature on the rigorous analysis of their asymptotic behavior… The literature
> contains many asymptotic approximations and expansions (see [2], [7], [14], [21], [23],
> **[31]**, [35], [40]), but most are heuristic, all parameters fixed except $\gamma$, and
> with little or no error analysis."*

**[31] is Slepian 1965** — verified by counting `\bibitem`s in the source, the 31st, and
by reading the entry: *"D. Slepian, Some asymptotic expansions for prolate spheroidal wave
functions, J. Math. Phys., 44 (1965), 99–140."* The two clauses are exactly the two things
mg-aedf's sentence needed and did not have: *"all parameters fixed except $\gamma$"* is
the fixed-index regime with no uniformity in the index, and *"little or no error
analysis"* is the negation of an error bound. Dunster's own contribution is billed against
precisely that gap — *"error bounds are available for all approximations"*, uniformly for
$0\le m\le n\le 2\pi^{-1}\gamma(1-\delta)$.

Concurring, from a second primary source: Bonami–Karoui (arXiv:1405.3676 = Constr. Approx.
**43** (2016) 15–45) open by saying *"In several applications, uniform estimates of the
$\psi_{n,c}$ in $n$ and $c$, are needed. **To progress in this direction**, we push forward
the uniform approximation error bounds"* — in 2014. And they cite Slepian 1965 in their
bibliography and **nowhere in their body**: it is not the source they build the uniform
bounds on.

**So `s3-reduction-audit.md:155-158` is narrower than written.** *"has rigorous
uniform-error versions in the literature (Slepian 1965 for the asymptotic; Bonami–Karoui
and Osipov–Rokhlin–Xiao for rigorous bounds)"* — read strictly, that sentence already
assigns the *asymptotic* to Slepian and the *rigorous bounds* to the other two, and in that
reading it survives. Read as the U3 row read it — that the uniform-error version is
Slepian's — it does not. B2 stays **holds (source), narrower (uniformity)**: Slepian 1965
is the right citation for the fixed-index Hermite limit and the wrong one for uniformity in
it, and the right ones for uniformity are Bonami–Karoui 2016, Osipov–Rokhlin–Xiao 2013, and
Dunster 2017.

**And there is a separate reason not to lean on uniformity here, which mg-aedf found and
this pass did not have to.** `verify_prolate_claims.py` test H measures
$\psi_0(0)\sim(c/\pi)^{1/4}$: measured $\psi_0(0)/c^{1/4}=0.7434,\,0.7474,\,0.7497,\,0.7504,\,0.7508,\,0.7509$
at $c=10,20,50,100,200,400$, against $\pi^{-1/4}=0.7511$. So the constant in
`start.tex:189-196`'s $h_\lambda(0)=O(1-\chi_4)$ **grows like $c^{1/4}$** and is not
uniform — and that is a property of the prolate functions themselves, not of the quality of
anyone's error bound. A fully uniform Slepian would not have supplied a uniform constant
there. The two questions look like one question and are not.

**What this changes for the paper: nothing, and check that this is right.** §4.4 item 2 —
$|\beta|^2\to8/11$ — is a *limit*, and the fixed-index Hermite limit is enough to establish
a limit; what a uniform-error version would buy is a *rate*, which nothing in the corpus
currently quotes. The place uniformity is load-bearing is `s3.tex:75-77`'s lower bound,
which needs $|b_\lambda|$ bounded below — and `verify_prolate_claims.py` block A already
notes that only the lower half needs a uniformity claim. That claim now has Bonami–Karoui
and Osipov–Rokhlin–Xiao behind it and not Slepian. Reported; `s3.tex` not edited.

---

### 12.5 U8 — the dictionary holds, and the row's premise did not

U8 records *"Neither paper states it. One numerical check would settle it."* The second
sentence was right. The first was not.

**(a) Groskin states the $c\leftrightarrow\lambda^2$ half, in his own words.** Read from
the arXiv LaTeX source of arXiv:2605.20224 (`main.tex`), which is a stronger provenance
than §9 records for §5 — that section rested on abstracts and metadata:

- **`:284-287`** — *"For a cutoff parameter $c$ (controlling the primes $p\le c$ in the
  prime-sum piece below; $c$ itself need not be prime …), set $L=\log c$. The quadratic
  form acts on $L^2([0,L])$."* This is §5's reading of Groskin's cutoff, verbatim.
- **`:433`** — *"We identify the two via this construction and adopt the convention
  $\lambda^2=c$ from CCM throughout."*
- **`:1095`** — *"where, as defined in [Connes 2026] §6.4, $L=2\log\lambda$ is the length
  of the support interval $[\lambda^{-1},\lambda]$… **With $\lambda^2=c$, this is
  $L=\log c$, so $e^L=c$.**"*
- **`:2263`** — *"Euler products over primes $p\le\lambda^2=c$."*

So $c_{\text{Groskin}}=\lambda^2=\mu$ is not an inference from two definitions; it is
Groskin's stated convention, attributed by him to CCM. §5's parenthetical is corrected in
place.

The companion paper agrees: arXiv:2607.02828 `main.tex:199-202`, *"Fix $c>1$, put
$L=\log c$, $\Delta=L/2\pi$, $\rho=2\pi/L$"*, with `:63` and `:103` calling $c$ the prime
cutoff.

**(b) The factor $2\pi$ is what was left, and it is now measured.**
[`verify_citation_u8.py`](verify_citation_u8.py) takes the corpus's own arbitrary-precision
Legendre eigensolver (imported from [`verify_prolate_rate.py`](verify_prolate_rate.py), so
it has never seen this dictionary), computes $1-\sqrt{\Lambda_4(\kappa\mu)}$ for candidate
scale factors $\kappa$, and compares against Connes' asymptotic — which is a function of
$\mu$ alone and has no free scale in it. Working precision **`mp.dps = 320`**, Legendre
truncation $K=\lceil c\rceil+90$.

$\log_{10}$ of measured $/$ predicted:

| $\kappa$ | $\mu=4$ | $\mu=6$ | $\mu=8$ | $\mu=10$ |
|---|---|---|---|---|
| $1$ | $+12.70$ | $+22.61$ | $+32.35$ | $+41.81$ |
| $2$ | $+11.88$ | $+19.72$ | $+27.27$ | $+34.77$ |
| $\pi$ | $+9.22$ | $+14.81$ | $+20.32$ | $+25.81$ |
| $\mathbf{2\pi}$ | $\mathbf{-0.151}$ | $\mathbf{-0.097}$ | $\mathbf{-0.072}$ | $\mathbf{-0.057}$ |
| $4\pi$ | $-20.55$ | $-31.44$ | $-42.34$ | $-53.25$ |

The check is decisive rather than merely consistent: a wrong $\kappa$ is wrong by
$e^{2(2\pi-\kappa)\mu}$, so the nearest neighbours miss by nine to fifty-three orders of
magnitude and the miss *grows* with $\mu$. At $\kappa=2\pi$ the ratio is
$0.7070,\,0.7997,\,0.8479,\,0.8774,\,0.8973$ at $\mu=4,6,8,10,12$, rising towards 1 with
$(1-\text{ratio})\cdot c=7.36,\,7.55,\,7.64,\,7.70,\,7.74$ — an $O(1/c)$ shortfall, which is
what a leading-order asymptotic should leave and is a shape no wrong $\kappa$ could
produce. Digits unchanged across `dps` 200/320/420 and $K=c+40/90/160$.

**And then, after the fact, the factor turns out to be printed too.** Connes'
footnote on the same line that carries the asymptotic (`rhready.tex:1149`) reads
*"Note that $\chi_k(\lambda)^2=\lambda_{2k}(a)$ **with $a=\sqrt{2\pi}\,\lambda$** in the
notations of this theorem"* — so the Fuchs-convention bandwidth is
$a^2=2\pi\lambda^2=2\pi\mu$, which is $c_{\text{ours}}$. The measurement and the footnote
are independent and agree.

**So the full dictionary $c_{\text{ours}}=2\pi\,c_{\text{Groskin}}$ holds**, and §5's two
consequences stand unchanged: the corpus's $c\le20$ is $\mu\le3.2$, the very bottom-left of
Connes–Consani's Figures 18–21; and Groskin's $c=13\ldots100$ is $c_{\text{ours}}=82\ldots628$.

**One thing the check cannot do, stated because the row will be read as if it could.** It
measures *our* $c$ against *Connes'* $\lambda$. The bridge to *Groskin's* $c$ is (a) and is
documentary. Nothing computed here touches the CvS Galerkin matrix.

---

### 12.6 U9 — Bonami–Karoui, 15–45

**A. Bonami, A. Karoui**, *Uniform approximation and explicit estimates for the prolate
spheroidal wave functions*, **Constr. Approx. 43** (2016), no. 1, **15–45**. DOI
[10.1007/s00365-015-9295-1](https://doi.org/10.1007/s00365-015-9295-1); published online 17
June 2015, in print February 2016; ISSN 0176-4276 / 1432-0940. Preprint arXiv:1405.3676.

Taken from the **publisher's own Crossref deposit** (`api.crossref.org/works/10.1007/s00365-015-9295-1`),
which is the metadata Springer registered for the article — not a search-result summary.
The Springer article page itself returns a `303` to an authentication endpoint for an
unauthenticated fetch, so this is the best available primary bibliographic record short of
the printed journal.

---

### 12.7 U5, left open

U5 asks which paper *"the 2023 trace formula"* means at `start.tex:46,242,425`. Every other
row in §7 was a question about the literature and could be answered by reading it. This one
is a question about what the corpus's author intended, and the two candidates (§4.1) are
both real papers that both contain something that could be meant. **Left open, marked as
Daniel's in the row itself.** Nothing in this pass touched it and nothing should.

---

### 12.8 This appendix under §9's rule

The three-way split, applied to the rows above.

**Content claims checked against the actual text of the source**, read directly and not
through a review, abstract or summary: **U1** (Wawrzyńczyk 1968, scanned journal PDF,
§4 read); **U2** (Deninger, the Documenta Mathematica PostScript of the article, all cited
pages read); **U3**'s positive half (Dunster, `PSWF_JCA.tex` arXiv source; Bonami–Karoui
arXiv PDF, abstract and bibliography); **U8** (both Groskin arXiv LaTeX sources; Connes
`rhready.tex`); and the whole of §12.1's converse table (`Spectraltriples.tex`,
`mainc2m24fine.tex`, `rhready.tex`, all downloaded from `arxiv.org/e-print/` for this pass).

**Bibliographic data taken from a primary record that is not the printed journal**: **U9**
(Springer's Crossref deposit); B1's page range (Crossref); U1's pp. 305–318 and U2's pp.
163–186 (the articles' own running heads, which is the printed journal, and so stronger).

**Claims I could not check against the source, and have marked as such**: **U3's subject
itself** — Slepian 1965 is paywalled and I did not read it. The negative rests on Dunster's
published characterisation of the literature *including* Slepian 1965 by number, and on
Bonami–Karoui's framing. That is a documented second-hand negative, not a reading of
Slepian, and the U3 row says so. **If someone with Wiley access ever opens it, that is the
one row here worth re-opening.**

**This appendix's provenance is stronger than §9 records for §5**, which rested on the
Groskin abstracts and metadata; §5's factual content is now read from both papers' LaTeX
sources. Two §5/§6 claims verified verbatim in passing, though neither is a §7 row:
`main.tex:284-287` of arXiv:2605.20224 for §5's account of the cutoff, and `:645-648` for
§6's quoted *"A prolate-basis implementation of the CvS Galerkin would be a genuinely
distinct path in the literature — potentially valuable as an independent cross-check — but
is not yet reported by any group."*

**The claim in this appendix that would do the most damage if wrong** is §12.4's negative,
because it is the only one asserting that something is *absent* from a paper I have not
read. It is checkable in one minute by anyone with Wiley access, which is the standard the
rest of this note is written to.

---

### 12.9 What this changes, per document

Not edits to `start.tex`, `s3.tex` or the paper — none were touched.

**`citation-audit.md` (this note).** §7 rows U1, U2, U3, U4, U5, U8, U9 annotated in place;
§5's parenthetical corrected in place; §8's `s3-reduction-audit.md` line corrected in place.
Line count unchanged; this appendix appended.

**`s3-reduction-audit.md`.** Its header still listed U3, U4, U6 as open when U4 and U6 had
been closed by mg-03f0 and mg-9433 — the same drift as U4's row, in the mirror. Corrected in
place, together with the §2 U3 and U4 blocks.

**`signed-geometry-proposals.md`.** The U1 annotation (§6) and the U2 bullet (§8) are
discharged; annotated in place.

**`start.tex` / `s3.tex` — reported, not edited.** Nothing here is new work for them beyond
what §8 already lists. The one addition: if `s3.tex:75-77`'s lower bound is ever written up,
its uniformity citation is Bonami–Karoui / Osipov–Rokhlin–Xiao / Dunster, **not** Slepian
1965 (§12.4).
