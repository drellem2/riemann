# Lean formalisation of the elementary layer under Q1

Machine-checked proofs of the load-bearing elementary steps beneath Q1
(Theorem 5.2 of `notes/band-edge-connection.md`). Produced by **mg-a087**.

Everything in this repository is agent-produced and agent-checked. The numerics
have an independent second implementation (mg-9797); until now **the proofs had
nothing**. This is the first machine-checked artefact in the corpus.

It runs *in parallel* with the research chain and gates nothing.

## Reproducing

```sh
lean/scripts/check.sh
```

builds the development and audits the axioms. It exits non-zero if anything
fails, if `sorry` appears in the sources, or if any result depends on `sorryAx`.

* **Lean toolchain:** `leanprover/lean4:v4.29.1` (pinned in `lean-toolchain`)
* **mathlib revision:** `5e932f97dd25535344f80f9dd8da3aab83df0fe6`
  (the `v4.29.1` tag; pinned in `lake-manifest.json`)

If `.lake/packages` is not present, `lake exe cache get` fetches the prebuilt
mathlib oleans — **do not compile mathlib from source**; it is hours instead of
minutes and it saturates the host.

## Reachability, per load-bearing result

**The question mg-7fc6 asked: how far up the paper can Lean reach *without* the
Prüfer-angle infrastructure that stopped mg-a087?** Answer, measured rather than
guessed: **Q2 and the assembly are reachable; Q1, H0 and Q3 are not.** The
dividing line is not "elementary versus hard" — it is whether the argument needs
a *continuous branch of a phase along an ODE-defined curve*.

mg-57a2 then closed the one row that read "probably yes, not attempted":
**Prop. 4.1 is proved**, and it terminates in Q1 exactly where mg-7fc6 predicted.
Formalising it refuted `dilate-sum.md` Lemma 3.1's printed potential — item 7 of
"What formalising changed", below, and the first *incorrect proof* rather than
understated hypothesis this development has found.

| Paper result | Reachable without new mathlib infrastructure? | Reason |
|---|---|---|
| **Lemma `lem:amplitude`** — `\|Φ x\| ≤ \|Φ 1\|` | **yes — done** (mg-a087) | Sturm functional; algebraic, no phase |
| **Lemma 3.1, Lemma 4.1** (first three bounds) | **yes — done** (mg-a087) | explicit coefficient bounds |
| **Thm `thm:q1`** (Q1) | **no** | needs the modified Prüfer angle `θ` with `Φ = ρ sin θ`, i.e. a *continuous* argument along an ODE solution. mathlib has continuous logarithms but not this. Explicitly out of scope for mg-7fc6 |
| **Lemma 4.1** — fourth bound, `θ' ≥ k - f` | **arithmetic half only** (mg-a087) | `k - f ≥ c₋` is proved; `θ' ≥ k - f` is about `θ` |
| **Thm `thm:q2`** (Q2) — the dilate sum | **yes — done, given Q1 and Lemma 3.3** | its two halves are (a) the sawtooth/log dichotomy, which is Abel's limit theorem on the unit circle — mathlib has it — and (b) a series split, harmonic sum and `m⁻²` tail. **Neither is an ODE statement.** Prop. 4.1's two remainder bounds were hypotheses for mg-7fc6 and are now proved (row below) |
| **Thm `thm:q2`** — Prop. 4.1 (the `x⁻²` remainder) | **yes — done** (mg-57a2) | measured, not guessed. mg-7fc6's prediction held: Lemma 3.2's Lagrange system is the Prüfer system's *linear* cousin — `α, β` are explicit algebraic functions of `(u, u')`, globally smooth, **needing no continuous branch** — and it went in as written. Lemma 3.1 (the Liouville form) and Lemma 3.2 (the system, and its `x⁻¹` convergence rate) are proved outright; **Q1** and **Lemma 3.3** (`α_∞ = a₁`, `β_∞ = 0`) are the hypotheses, so it terminates in Q1 exactly as predicted. Lemma 3.2's convergence needed **no integration theory** — an explicit majorant antiderivative plus two monotonicity arguments replaces `∫_X^∞ |α'|`. **Formalising this row found `dilate-sum.md` Lemma 3.1's potential to be wrong** — item 7 below |
| **`dilate-sum.md` Lemma 2.1** (two integrations by parts, Riemann–Lebesgue) and **Lemma 3.3** (`β_∞ = 0`) | **not attempted** | mathlib has Riemann–Lebesgue and integration by parts, so this is reachable in principle; it was left out to keep mg-57a2 inside its scope limit. It is the remaining prose input to Q2 besides Q1, and it is where the finite-Fourier eigenrelation (F) enters |
| **Cor `cor:quantisation`** — `β_∞ ≠ 0` ⟹ `sup t\|G\| = +∞` | **yes — done** (the divergence half) | `∑ cos(mγ)/m = -log(2 sin(γ/2)) → +∞` as `γ → 0⁺` |
| **Thm `thm:q3`** (Q3) | **no** | needs Riemann–von Mangoldt, de la Vallée Poussin's zero-free region, subharmonicity of `\|F\|²` on a strip, and Plancherel on horizontal lines. mathlib has **neither** classical zeta input |
| **Thm `thm:h0`** (H0) | **no** | rests on Dunster (124)+(107) — uniform asymptotics of prolate functions by parabolic cylinder functions. mathlib has no prolate functions, no parabolic cylinder functions, and no coalescing-turning-point theory. Not a Prüfer problem; a *no such special function exists* problem |
| **Cor `cor:upper`** and **Thm `thm:main`** — the assembly | **yes — done** | given the four legs as hypotheses, the `-4π` is real analysis on `μ⁻¹ log`. Instantiated at the paper's own exponents (`Ξ = C μ⁶ log³μ`, `1-χ₂ = C' μ^{9/2} e^{-4πμ}`, `‖g‖² → 0.219…`) so the hypotheses are demonstrably satisfiable |
| **Prop `prop:zetaside`** | **no** | same two missing classical inputs as Q3 |
| **Prop `prop:identity`** | **not attempted** | one line informally, but it needs `F_μ`, the zero set `Z` and `QW_λ` as Lean objects — a definitional layer, not a proof |
| **Prop `prop:noH1`**, **`prop:indefinite`**, **`prop:witness`** | **not attempted** | not on the `-4π` chain |

`#print axioms` reports `[propext, Classical.choice, Quot.sound]` for all **91**
results and `sorryAx` for none. There is no `sorry` anywhere in `Riemann/`.

### The one-sentence version

> The Prüfer wall blocks **Q1 and nothing else** on the chain. Above it, Q2 is
> blocked only *through* Q1 — now measured rather than predicted: Prop. 4.1 is
> proved and it terminates in Q1 — and the assembly is not blocked at all. What blocks
> Q3 and H0 is a different and much larger absence: mathlib has neither of the two
> classical facts about the zeros of `ζ`, and no prolate or parabolic-cylinder
> special functions whatsoever.

### Files

* `Riemann/Sturm.lean` — Lemma `lem:amplitude` and the Sturm functional
  `V = p²/D + Φ²`. (mg-a087)
* `Riemann/BandEdge.lean` — Lemmas 3.1 and 4.1: the coefficient functions
  `u, v, f, k` and their bounds and derivatives. (mg-a087)
* `Riemann/Sawtooth.lean` — the quantisation dichotomy: `∑ sin(mγ)/m = (π-γ)/2`
  is bounded, `∑ cos(mγ)/m = -log(2 sin(γ/2))` is not. (mg-7fc6)
* `Riemann/DilateSum.lean` — Theorem `thm:q2` with its explicit constant, given
  Prop. 4.1's two remainder bounds as hypotheses. (mg-7fc6)
* `Riemann/Remainder.lean` — `dilate-sum.md` Lemmas 3.1 and 3.2 and
  **Proposition 4.1**, with Q1 and Lemma 3.3 as hypotheses; and
  `theorem_q2_of_prolate`, which is `DilateSum.theorem_q2` with those two
  hypotheses discharged. Contains the refutation of Lemma 3.1 as printed
  (`printed_potential_not_deriv`). (mg-57a2)
* `Riemann/Assembly.lean` — Corollary `cor:upper` and the `limsup` half of
  Theorem `thm:main`, with the four legs as hypotheses. (mg-7fc6)
* `Riemann/Axioms.lean` — the axiom audit; every claimed result is listed.

## Where it stops, and why

**Lemma 4.1's fourth bound** is `θ' ≥ k - f ≥ c - 2/x ≥ c₋`. The second and
third inequalities are `phase_speed_lower` and are proved. The first is a
statement about the Prüfer angle `θ`, which does not exist in this development —
see below.

**Lemma 2.1 (the modified Prüfer system) is the wall.** It needs a continuous
branch `θ` with `Φ = ρ sin θ` and `p/√D = ρ cos θ`. Constructing a *continuous*
argument along a curve, and differentiating it, is the missing ingredient;
mathlib has the machinery for continuous logarithms/arguments but wiring it to
an ODE-defined curve is a substantial piece of work in its own right and is not
a matter of translating the note. Without `θ` there is no Corollary 2.2, no
Proposition 4.2 and no Theorem 5.2.

**Mathlib has essentially nothing on prolate spheroidal wave functions or WKB
asymptotics**, which is why this development is bottom-up and why mg-a087's
ticket asked for it to be. mg-a087 attempted nothing above Lemma 4.1; mg-7fc6
went *around* rather than through, which is what the reachability table records.

**mg-7fc6's finding about the wall: it is narrower than it looked.** The Prüfer
angle is needed for Q1 and for nothing else on the `-4π` chain. Two reasons:

* **Q2's ODE input does not need a continuous phase.** `dilate-sum.md` Lemma 3.2
  writes `u = α sin(cx) + β cos(cx)`, `u' = c(α cos(cx) - β sin(cx))`. Solving,
  `α` and `β` are *explicit algebraic functions of `(u, u')`* — globally defined,
  smooth, single-valued. Nothing has to be lifted along a curve. Reading Q2's
  argument as "the Prüfer system again" is what made it look blocked; the
  Lagrange system is the Prüfer system's linear cousin and it is free.
* **The assembly needs no ODE at all.** `cor:upper` is an inequality between
  real-valued functions of `μ`.

**What blocks Q3 and H0 is not this wall and is much bigger.** Q3 needs
Riemann–von Mangoldt and de la Vallée Poussin, neither of which is in mathlib;
H0 needs parabolic cylinder functions and coalescing-turning-point asymptotics,
of which mathlib has nothing at all. Those are not "one more lemma" — they are
research-library-scale absences, and no reordering of this development reaches
them.

**Non-vacuity is not formalised.** The theorems are conditional on
`IsSolution c χ Φ p` being inhabited. That the prolate equation *has* solutions
on `(1,∞)` follows from Picard–Lindelöf, but mathlib's ODE existence theory was
not wired up here, so the development does not exhibit a witness. What it *does*
check is `isSolution_of_secondOrder`: that the first-order system really is the
second-order equation, sign for sign. That is the check whose failure would have
made everything else vacuous.

## What formalising changed in the informal statements

Recorded in `notes/band-edge-connection.md` §13, `notes/h1-mean-value.md` §16 and
`notes/dilate-sum.md` §§12–13, and repeated here. Items 1–3 are mg-a087's; item 4
is mg-7fc6's, and items 5–6 are clarifications rather than repairs — stated as
such rather than dressed up. **Item 7 is mg-57a2's and is different in kind from
all of them: an incorrect proof, the first formalisation has found here.**

**What every item below has in common, and it is worth knowing before you start a
formalisation ticket: the defect was in what a statement *said*, never in anything
derived from it.** So nothing downstream went red in any of these — the class has
no natural detector, and it is found only by re-deriving a printed statement
deliberately. `notes/statement-defects.md` states the class and the two practices
that caught item 7 (a cheap independent instrument *before* the expensive one; a
machine-checked rather than argued "nothing else changes"). Read it before
pointing this development at a new note — that note is where the second of the
project's two standing checks lives, the house rule below being the first.

1. **Lemma 5.1's use of "Φ is analytic at `x=1`" splits into two independent
   hypotheses**, and the note's remark that "boundedness near `x=1` would do"
   names only one of them. The proof needs *both*
   * `Φ'` bounded on a right-neighbourhood of `1` — this is what makes
     `p²/D → 0`, since `p²/D = (x²-1)(Φ')²/q`; and
   * `Φ` right-continuous at `1` — without which `V(1⁺) = Φ(1)²` does not
     follow even though `p²/D → 0`.

   In `abs_le_abs_one` these are the separate hypotheses `hM` and `hcont`.
   Analyticity gives both at once, so nothing is wrong in the note; but
   "boundedness near `x=1` would do" is not by itself enough, and the second
   half is the one a reader would skip.

2. **Three hypotheses in the note's Lemma 4.1 are not needed where they are
   stated.** The note fixes `c > √2` and `0 ≤ χ < c²` for all of §§2–5. In fact:
   * `vv_le` (`v ≤ 2/x²`) and `ff_le` (`f ≤ 2/x`) need neither `0 < c` nor
     `0 ≤ χ` — only `χ < c²` and `√2 ≤ x`;
   * `hasDerivAt_kk` (the formula `k' = -x(c²-χ)u²/k`) needs neither.

   This is a tightening, not a correction: the note's blanket hypotheses are
   true in the intended application. It is recorded because it localises what
   each bound actually rests on.

3. **`0 ≤ χ` is used exactly once, and the note is exactly right about it.**
   The note says of `|k'| ≤ 4c/x³`: "This last step is the only place `χ ≥ 0` is
   used, and it is the only place it is needed." Formalising confirms this
   precisely — that bound (`abs_deriv_kk_le`, and its `deriv`-form restatement
   `abs_deriv_kk_le'`) is the only statement in either file carrying the
   hypothesis `0 ≤ χ`. mg-6851 had already tightened the theorem's hypothesis
   from `χ < c²` to `0 ≤ χ < c²` after first stating it without; this is the
   independent confirmation that the tightening was both necessary and
   sufficient.

4. **Corollary `cor:upper` is stated with an incomplete hypothesis list, and the
   missing item is a second external citation.** The corollary assumes (H0) and
   the `Ξ(μ)(1-χ₂)` bound, and concludes `limsup μ⁻¹ log s(μ) ≤ -4π`. But that
   conclusion also needs the *rate* `μ⁻¹ log(1-χ₂(λ)) → -4π`, which is Fuchs'
   1964 asymptotic in the form Connes cites it (paper §5.2) — an import the paper
   lists under "Not read". The corollary as written names neither the rate nor
   Fuchs.

   This is structural rather than stylistic: `Riemann.Assembly.limsup_le_neg_four_pi`
   **cannot be stated** without its `hN` hypothesis, because `Ξ` and `‖g‖²` are
   both subexponential and nothing else in the hypotheses mentions `4π`. So the
   `4π` in Theorem `thm:main` enters through Fuchs and only through Fuchs.
   Consequence for the ledger: `thm:main`'s attribution line reads "\proved
   modulo \cite{Dunster2017} eq. (124)+(107)" and should name **two** imports,
   not one. Nothing about "unconditional" changes — Fuchs is proved and classical
   — but the citation count in a paper that is otherwise careful to count them
   was one short.

5. **What `cor:upper` consumes of (H0) is `Subexp ‖g‖²`, not a lower bound.** The
   paper already says this in prose ("only `μ⁻¹ log ‖g‖² → 0`, so *any*
   `‖g‖² ≥ e^{-o(μ)}` gives the same `-4π`"). Formalising makes it structural:
   the hypothesis of `limsup_le_neg_four_pi` *is* `Subexp G`, and the strong form
   is never unfolded. A confirmation, not a repair.

6. **The `limsup` in Theorem `thm:main` must be read in `[-∞,∞]`, and the
   `ε`-form is the statement that carries the content.** Lean's `Filter.limsup`
   into `ℝ` returns a junk value when the sequence is unbounded below, so the
   `ℝ`-valued reading of `thm:main` needs the side condition that `s(μ)` does not
   decay superexponentially. This is a **convention artefact, not a defect in the
   paper**: every mathematician reads a `limsup` as valued in `[-∞,∞]`, where no
   side condition is needed. It is recorded only because the primary Lean
   statement is therefore `eventually_log_le_neg_four_pi` — "for every `ε > 0`,
   eventually `log s(μ) ≤ (-4π+ε)μ`" — which is what the chain actually gives,
   is strictly stronger than any `limsup` reading, and is the sentence worth
   quoting.

7. **`dilate-sum.md` Lemma 3.1 prints the wrong Liouville potential — the first
   *incorrect proof* this development has found.** The note (and paper §7.5)
   state that `u := √(x²-1) Φ` satisfies `u'' + (c²+ε)u = 0` with
   `ε = (c²-χ+1)/(x²-1)`. It does not. The true potential is

   ```
   ε(x) = (c²-χ)/(x²-1) + 1/(x²-1)²
   ```

   The note's proof divides `½(p^{-1/2}p')'` by `p^{-1/2}` where the preceding
   line licenses `p^{1/2}`; with `p = x²-1` that turns an `(x²-1)⁻²` into an
   `(x²-1)⁻¹`. Both halves are machine-checked: `Remainder.hasDerivAt_uu'` proves
   the corrected identity, and `Remainder.printed_potential_not_deriv` refutes
   the printed one at the separating instance `c = χ = 0`, `Φ ≡ 1`, `x = 2`
   (there `u = √(x²-1)`, `u'' = -(x²-1)^{-3/2}`, and only the corrected `ε`
   annihilates it).

   **Nothing downstream moves, and that is checked and not argued.** `ε` is
   consumed at exactly one point — the tail bound `∫_X^∞ ε` of Lemma 3.2 — and
   the true `ε` satisfies it with *more* room than the printed one:
   `(2c² + 2/3)/X` against `2(c²+1)/X`, both below the `3c²/X` actually used
   (`Remainder.eps_le_deriv_MM`, `Remainder.MM_le`). `B₁`, `B₂`, `K_P(c)` and
   every number in `dilate-sum.md` §7 stand as printed.

   Why it survived two notes and a formalisation ticket, since that is the part
   worth keeping: the two potentials **agree to leading order as `x → ∞`**, which
   is the only regime the argument uses, so no asymptotic check separates them;
   `notes/verify_q2.py` checks the *conclusions* of Lemmas 3.2–3.3 and Prop. 4.1
   and **never evaluates `ε`**, so no grid could catch it; and mg-7fc6 stopped one
   lemma short, taking the off-band splitting as a hypothesis, so Lemma 3.1 was
   never presented to the compiler. It was reachable only by formalising
   *downward* into the step nobody had a reason to doubt.

8. **Prop. 4.1(i) needs no hypothesis on `c`, `χ` or the ODE.** It is Q1 plus
   `|sin| ≤ 1`. `Remainder.prop41_i` carries neither `IsSolution` nor `0 ≤ χ < c²`
   nor `√2 < c` nor `β_∞ = 0`; every standing hypothesis of `dilate-sum.md` §0
   beyond Q1 is spent in part (ii) and nowhere else. Same shape as items 2–3
   above: a localisation, not a correction.

9. **The eigenrelation (F) enters Prop. 4.1 through `β_∞ = 0` and nothing else.**
   All of Lemma 3.2 (`abs_sub_al_le`, `abs_sub_be_le`) is pure ODE; (F) appears
   only as `tail_le`'s `hβ` hypothesis. `dilate-sum.md` §3's Corollary 3.4 says
   exactly this, and it is now structural rather than asserted.

**A deviation, recorded because it is not a transcription.** `dilate-sum.md`
Thm 5.1 splits the remainder sum at `mt = X_*`; `Riemann.DilateSum.tsum_abs_le`
splits at the *index* `⌊X⌋₊`. That is a coarser split (the low set is larger,
since `mt < X` implies `m < X`) and it yields the same constant, because the low
bound is summed against `harmonic ⌊X⌋₊ ≤ 1 + log X` either way.

**A second deviation, same kind.** `dilate-sum.md` Lemma 3.2 proves `(3.3)` by
integrating `|α'| ≤ (ε/c)K₁|Φ(1)|` from `X` to `∞`. `Riemann/Remainder.lean`
uses **no integration theory at all**: `MM c x = 2c²/x + 4/(3x³)` is an explicit
majorant antiderivative with `-MM' ≥ ε` pointwise on `[√2,∞)`, and
`abs_sub_le_of_deriv_le` gets `|α y - α x| ≤ k(M x - M y)` from `α + kM` antitone
and `α - kM` monotone. Same constant, and the *existence* of `α_∞`, `β_∞` is not
needed — Lemma 3.3 supplies their values as a hypothesis.

**No sign, and nothing approaching RH, appears anywhere in this development.**
It is confidence in existing magnitude results and nothing more. Applying the
house rule target by target: `lem:amplitude`, Lemma 3.1, Lemma 4.1, the two
Fourier identities of `Sawtooth.lean`, Theorem `thm:q2`, the whole of
`Remainder.lean` (under `Φ ↦ -Φ`: `u ↦ -u`, `α ↦ -α`, `β ↦ -β`, `a₁ ↦ -a₁`,
`W ↦ -W`, and `eps`/`MM` mention no `Φ` at all) and the whole of
`Assembly.lean` are **every one of them sign-blind** — each is an equality, or a
bound on a modulus, or (in the assembly) invariant under relabelling its
arguments, and **not one of them becomes false under `W_λ ↦ -W_λ`**. Nothing new
was found here that is not sign-blind, which is the answer the thesis of
`paper` §1.2 predicts.

That test — *is the statement false for `-W_λ`?* — is the project's first standing
check. The second is `notes/statement-defects.md`: *does the printed statement say
what the argument beneath it proves?* They fail in opposite directions and neither
substitutes for the other, so apply both.
