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

| Paper result | Reachable without new mathlib infrastructure? | Reason |
|---|---|---|
| **Lemma `lem:amplitude`** — `\|Φ x\| ≤ \|Φ 1\|` | **yes — done** (mg-a087) | Sturm functional; algebraic, no phase |
| **Lemma 3.1, Lemma 4.1** (first three bounds) | **yes — done** (mg-a087) | explicit coefficient bounds |
| **Thm `thm:q1`** (Q1) | **no** | needs the modified Prüfer angle `θ` with `Φ = ρ sin θ`, i.e. a *continuous* argument along an ODE solution. mathlib has continuous logarithms but not this. Explicitly out of scope for mg-7fc6 |
| **Lemma 4.1** — fourth bound, `θ' ≥ k - f` | **arithmetic half only** (mg-a087) | `k - f ≥ c₋` is proved; `θ' ≥ k - f` is about `θ` |
| **Thm `thm:q2`** (Q2) — the dilate sum | **yes — done, given Prop. 4.1** | its two halves are (a) the sawtooth/log dichotomy, which is Abel's limit theorem on the unit circle — mathlib has it — and (b) a series split, harmonic sum and `m⁻²` tail. **Neither is an ODE statement.** Prop. 4.1's two remainder bounds are hypotheses, because they rest on Q1 |
| **Thm `thm:q2`** — Prop. 4.1 (the `x⁻²` remainder) | **probably yes, not attempted** | Lemma 3.2's Lagrange system is the Prüfer system's *linear* cousin: `α, β` are explicit algebraic functions of `(u, u')`, globally smooth, **needing no continuous branch**. This is the finding that made Q2 look reachable in the first place. Lemma 3.3 additionally needs Riemann–Lebesgue (mathlib has it) and Lemma 2.1's integration by parts. Not attempted because Prop. 4.1(ii) consumes Q1 for `\|u\| ≤ K₁\|Φ(1)\|`, so it would still terminate in the same hypothesis |
| **Cor `cor:quantisation`** — `β_∞ ≠ 0` ⟹ `sup t\|G\| = +∞` | **yes — done** (the divergence half) | `∑ cos(mγ)/m = -log(2 sin(γ/2)) → +∞` as `γ → 0⁺` |
| **Thm `thm:q3`** (Q3) | **no** | needs Riemann–von Mangoldt, de la Vallée Poussin's zero-free region, subharmonicity of `\|F\|²` on a strip, and Plancherel on horizontal lines. mathlib has **neither** classical zeta input |
| **Thm `thm:h0`** (H0) | **no** | rests on Dunster (124)+(107) — uniform asymptotics of prolate functions by parabolic cylinder functions. mathlib has no prolate functions, no parabolic cylinder functions, and no coalescing-turning-point theory. Not a Prüfer problem; a *no such special function exists* problem |
| **Cor `cor:upper`** and **Thm `thm:main`** — the assembly | **yes — done** | given the four legs as hypotheses, the `-4π` is real analysis on `μ⁻¹ log`. Instantiated at the paper's own exponents (`Ξ = C μ⁶ log³μ`, `1-χ₂ = C' μ^{9/2} e^{-4πμ}`, `‖g‖² → 0.219…`) so the hypotheses are demonstrably satisfiable |
| **Prop `prop:zetaside`** | **no** | same two missing classical inputs as Q3 |
| **Prop `prop:identity`** | **not attempted** | one line informally, but it needs `F_μ`, the zero set `Z` and `QW_λ` as Lean objects — a definitional layer, not a proof |
| **Prop `prop:noH1`**, **`prop:indefinite`**, **`prop:witness`** | **not attempted** | not on the `-4π` chain |

`#print axioms` reports `[propext, Classical.choice, Quot.sound]` for all **65**
results and `sorryAx` for none. There is no `sorry` anywhere in `Riemann/`.

### The one-sentence version

> The Prüfer wall blocks **Q1 and nothing else** on the chain. Above it, Q2 is
> blocked only *through* Q1, and the assembly is not blocked at all. What blocks
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
`notes/dilate-sum.md` §12, and repeated here. Items 1–3 are mg-a087's; item 4 is
mg-7fc6's, and items 5–6 are clarifications rather than repairs — stated as such
rather than dressed up.

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

**A deviation, recorded because it is not a transcription.** `dilate-sum.md`
Thm 5.1 splits the remainder sum at `mt = X_*`; `Riemann.DilateSum.tsum_abs_le`
splits at the *index* `⌊X⌋₊`. That is a coarser split (the low set is larger,
since `mt < X` implies `m < X`) and it yields the same constant, because the low
bound is summed against `harmonic ⌊X⌋₊ ≤ 1 + log X` either way.

**No sign, and nothing approaching RH, appears anywhere in this development.**
It is confidence in existing magnitude results and nothing more. Applying the
house rule target by target: `lem:amplitude`, Lemma 3.1, Lemma 4.1, the two
Fourier identities of `Sawtooth.lean`, Theorem `thm:q2` and the whole of
`Assembly.lean` are **every one of them sign-blind** — each is an equality, or a
bound on a modulus, or (in the assembly) invariant under relabelling its
arguments, and **not one of them becomes false under `W_λ ↦ -W_λ`**. Nothing new
was found here that is not sign-blind, which is the answer the thesis of
`paper` §1.2 predicts.
