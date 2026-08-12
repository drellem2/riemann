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

## Status, per target

The ticket asked for an honest per-target report. Here it is.

| Target | Status |
|---|---|
| **Lemma 5.1** — Sturm amplitude non-increasing, `\|Φ x\| ≤ \|Φ 1\|` | **compiles, no `sorry`** |
| **Lemma 3.1** — `k > c` on `(1,∞)` | **compiles, no `sorry`** |
| **Lemma 4.1** — first three bounds (`f ≤ 2/x`, `\|f'\| ≤ 8/x²`, `\|k'\| ≤ 4c/x³`) | **compiles, no `sorry`** |
| **Lemma 4.1** — fourth bound, `θ' ≥ k - f` | **arithmetic half only** (see below) |
| **Lemma 2.1** — the modified Prüfer system | **not attempted** (see below) |
| **Proposition 4.2** — the oscillatory integral | **not attempted** |
| **Theorem 5.2** — Q1 | **not attempted** |

`#print axioms` reports `[propext, Classical.choice, Quot.sound]` for all 26
results and `sorryAx` for none. There is no `sorry` anywhere in `Riemann/`.

### Files

* `Riemann/Sturm.lean` — Lemma 5.1 and the Sturm functional `V = p²/D + Φ²`.
* `Riemann/BandEdge.lean` — Lemmas 3.1 and 4.1: the coefficient functions
  `u, v, f, k` and their bounds and derivatives.
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
asymptotics**, which is why this development is bottom-up and why the ticket
asked for it to be. Nothing above Lemma 4.1 was attempted.

**Non-vacuity is not formalised.** The theorems are conditional on
`IsSolution c χ Φ p` being inhabited. That the prolate equation *has* solutions
on `(1,∞)` follows from Picard–Lindelöf, but mathlib's ODE existence theory was
not wired up here, so the development does not exhibit a witness. What it *does*
check is `isSolution_of_secondOrder`: that the first-order system really is the
second-order equation, sign for sign. That is the check whose failure would have
made everything else vacuous.

## What formalising changed in the informal statements

Recorded in `notes/band-edge-connection.md` §13 and `notes/h1-mean-value.md`
§16, and repeated here.

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

**No sign, and nothing approaching RH, appears anywhere in this development.**
It is confidence in existing magnitude results and nothing more.
