/-
# Proposition 4.1 — the off-band remainder decays like `x⁻²`

Formalisation of **Proposition 4.1** of `notes/dilate-sum.md` §4 and of the two
lemmas beneath it: **Lemma 3.1** (the Liouville form) and **Lemma 3.2** (the
Lagrange system and its convergence rate).  These are the two bounds that
`Riemann/DilateSum.lean` carried as the hypotheses `hW1`, `hW2` of `theorem_q2`;
`theorem_q2_of_prolate` at the end of this file discharges them.

With `W x := Φ x - a₁ sin(cx)/x`, the informal statement is

> **(i)**  `|W x| ≤ B₁|Φ 1|/x` for `x ≥ 1`,     `B₁ = K₁(c) + 2/(c|μ_Φ|)`;
> **(ii)** `|W x| ≤ B₂|Φ 1|/x²` for `x ≥ √2`,   `B₂ = K₁(c)(6c + 1/√2)`.

## What formalising found: `dilate-sum.md` Lemma 3.1 prints the wrong potential

The note's Lemma 3.1 says `u := √(x²-1) Φ` satisfies `u'' + (c²+ε)u = 0` with

    ε x = (c² - χ + 1)/(x² - 1)                    -- as printed; WRONG

The true potential — `eps` below, and `hasDerivAt_uu'` is the machine-checked
proof — is

    ε x = (c² - χ)/(x² - 1)  +  1/(x² - 1)²        -- `Riemann.Remainder.eps`

The slip is one line of the note's proof: it divides `½(p^{-1/2}p')'` by
`p^{-1/2}` where it must divide by `p^{1/2}`, and with `p = x²-1` that turns an
`(x²-1)⁻²` into an `(x²-1)⁻¹`.  A one-line control needing no machine: at
`c = χ = 0` the equation `((x²-1)Φ')' = 0` has the solution `Φ ≡ 1`, so
`u = √(x²-1)` and `u'' = -(x²-1)^{-3/2}`; the true `ε = (x²-1)^{-2}` gives
`u'' + εu = 0`, while the printed `ε = (x²-1)^{-1}` gives
`u'' + εu = (x²-1)^{-1/2} - (x²-1)^{-3/2} ≠ 0`.

**Nothing downstream changes, and that is checked here rather than asserted.**
`ε` is used for exactly one purpose — the tail bound `∫_X^∞ ε ≤ 3c²/X` of
Lemma 3.2 — and the *true* `ε` satisfies it with room to spare: `eps_le_deriv_MM`
majorises it by `2c²/x² + 4/x⁴`, whose tail is `(2c² + 2/3)/X`, against the
printed potential's `2(c²+1)/X`; both are `≤ 3c²/X` once `c > √2`.  So
Lemma 3.2's `(3.3)`, Proposition 4.1's `B₁` and `B₂`, and Theorem 5.1's `K_P(c)`
are all unaffected.  Recorded in `notes/dilate-sum.md` §13 and in the paper.

## What is proved here and what is a hypothesis

**Proved:** Lemma 3.1 (`hasDerivAt_uu`, `hasDerivAt_uu'`), the Lagrange system
(`al_add_be`, `hasDerivAt_al`, `hasDerivAt_be`), Lemma 3.2's rate
(`abs_sub_al_le`, `abs_sub_be_le`, `tail_le`), and Proposition 4.1
(`prop41_i`, `prop41_ii`).

**Hypotheses — exactly the note's two non-elementary inputs:**

* **Q1** (`hQ1 : ∀ x ≥ 1, x|Φ x| ≤ K₁ P`), `notes/band-edge-connection.md`
  Thm 5.2.  It is behind the Prüfer wall (`lean/README.md`), so Prop. 4.1
  terminates there — which is the shape mg-7fc6 predicted.
* **Lemma 3.3** (`hα : Tendsto α atTop (𝓝 a₁)`, `hβ : Tendsto β atTop (𝓝 0)`).
  These are *not* ODE facts.  `dilate-sum.md` §3 proves them from the
  finite-Fourier eigenrelation **(F)** plus Riemann–Lebesgue, and Corollary 3.4
  shows Q2 is **false** without `β_∞ = 0`.  Keeping them as hypotheses is what
  makes visible that (F) enters part (ii) and nothing else.

Where each hypothesis is spent, as the Lean now records it:

* `prop41_i` uses **Q1 and `|sin| ≤ 1` only** — no ODE, no `α`, no `β`, no (F),
  and not even `0 ≤ χ` or `c > √2`.
* `prop41_ii` uses the ODE, `0 ≤ χ < c²`, `c > √2`, Q1 **and** (F) through `hβ`.

## Sign-blindness (the house rule)

**Sign-blind.**  Under `Φ ↦ -Φ`: `u ↦ -u`, `α ↦ -α`, `β ↦ -β`, `a₁ ↦ -a₁`,
`W ↦ -W`; every conclusion below is a derivative identity, an algebraic
identity, or a bound on a modulus, and all are invariant.  `eps` and `MM` do not
mention `Φ` at all.  **No statement in this file is false for `W_λ ↦ -W_λ`, and
none has a one-signed conclusion.**

## Mathlib

Built against mathlib `5e932f97dd25535344f80f9dd8da3aab83df0fe6` (tag
`v4.29.1`), Lean toolchain `leanprover/lean4:v4.29.1`.
-/
import Riemann.Sturm
import Riemann.DilateSum

namespace Riemann.Remainder

open Set Filter Topology
open Riemann.Prolate (IsSolution qq)
open scoped Real

/-! ## `√(x²-1)`, and why its derivative is written `x·rt/(x²-1)`

Writing `rt' = x/rt` would put `rt` in a denominator and every later identity
would need `rt² = x²-1` to clear it.  Written as `x·rt/(x²-1)` instead, `rt`
occurs linearly in every expression below, and Lemma 3.1's two derivative
identities hold with `rt` treated as a *free indeterminate* — which is why `ring`
closes them, and is a small independent check that the transformation is the one
the note intends. -/

/-- `rt x = √(x²-1)`, the Liouville factor. -/
noncomputable def rt (x : ℝ) : ℝ := Real.sqrt (x ^ 2 - 1)

lemma rt_nonneg (x : ℝ) : 0 ≤ rt x := Real.sqrt_nonneg _

lemma rt_pos {x : ℝ} (hx : 1 < x) : 0 < rt x := Real.sqrt_pos.mpr (by nlinarith)

lemma rt_sq {x : ℝ} (hx : 1 < x) : rt x ^ 2 = x ^ 2 - 1 := Real.sq_sqrt (by nlinarith)

/-- `√(x²-1) ≤ x`.  This is what turns Q1's `x|Φ x| ≤ K₁P` into `|u| ≤ K₁P` —
the step `dilate-sum.md` Lemma 3.2 calls "the bound on `u` is Q1 and only Q1". -/
lemma rt_le {x : ℝ} (hx : 0 ≤ x) : rt x ≤ x := by
  have h : Real.sqrt (x ^ 2 - 1) ≤ Real.sqrt (x ^ 2) := Real.sqrt_le_sqrt (by linarith)
  rwa [Real.sqrt_sq hx] at h

lemma hasDerivAt_rt {x : ℝ} (hx : 1 < x) : HasDerivAt rt (x * rt x / (x ^ 2 - 1)) x := by
  have hne : x ^ 2 - 1 ≠ 0 := by nlinarith
  have hr : rt x ≠ 0 := (rt_pos hx).ne'
  have hsq : rt x ^ 2 = x ^ 2 - 1 := rt_sq hx
  have h : HasDerivAt (fun y : ℝ => y ^ 2 - 1) (2 * x) x := by
    simpa using (hasDerivAt_pow 2 x).sub_const 1
  have h2 : HasDerivAt (fun y : ℝ => Real.sqrt (y ^ 2 - 1))
      (1 / (2 * Real.sqrt (x ^ 2 - 1)) * (2 * x)) x := (Real.hasDerivAt_sqrt hne).comp x h
  have heq : 1 / (2 * Real.sqrt (x ^ 2 - 1)) * (2 * x) = x * rt x / (x ^ 2 - 1) := by
    have hrt : Real.sqrt (x ^ 2 - 1) = rt x := rfl
    rw [hrt, ← hsq]
    field_simp
  rw [heq] at h2
  exact h2

/-! ## Lemma 3.1 — the Liouville form, with the corrected potential -/

/-- **The Liouville potential of `dilate-sum.md` Lemma 3.1, corrected.**

The note prints `(c² - χ + 1)/(x² - 1)`.  The true value is this one; see the
file header, and `hasDerivAt_uu'` for the machine-checked proof. -/
noncomputable def eps (c χ x : ℝ) : ℝ := (c ^ 2 - χ) / (x ^ 2 - 1) + 1 / (x ^ 2 - 1) ^ 2

/-- `u = √(x²-1) Φ`. -/
noncomputable def uu (Φ : ℝ → ℝ) (x : ℝ) : ℝ := rt x * Φ x

/-- `u' = (xΦ + p)/√(x²-1)`, written as `(xΦ + p)·rt/(x²-1)` so that `rt` stays
linear.  With `p = (x²-1)Φ'` this is `xΦ/√(x²-1) + √(x²-1)Φ'`. -/
noncomputable def uu' (Φ p : ℝ → ℝ) (x : ℝ) : ℝ := (x * Φ x + p x) * rt x / (x ^ 2 - 1)

lemma hasDerivAt_uu {c χ : ℝ} {Φ p : ℝ → ℝ} (hsol : IsSolution c χ Φ p)
    {x : ℝ} (hx : 1 < x) : HasDerivAt (uu Φ) (uu' Φ p x) x := by
  have hne : x ^ 2 - 1 ≠ 0 := by nlinarith
  have hdef : uu Φ = fun y => rt y * Φ y := rfl
  have h := (hasDerivAt_rt hx).mul (hsol.hΦ x hx)
  rw [hdef]
  convert h using 1
  simp only [uu']
  field_simp

/-- **Lemma 3.1 of `dilate-sum.md`, corrected.**  `u'' + (c² + ε)u = 0` on
`(1,∞)`, with `ε` the potential of `eps` — *not* the `(c²-χ+1)/(x²-1)` the note
prints.  See the file header for the discrepancy and for why nothing downstream
moves. -/
lemma hasDerivAt_uu' {c χ : ℝ} {Φ p : ℝ → ℝ} (hsol : IsSolution c χ Φ p)
    {x : ℝ} (hx : 1 < x) :
    HasDerivAt (uu' Φ p) (-(c ^ 2 + eps c χ x) * uu Φ x) x := by
  have hne : x ^ 2 - 1 ≠ 0 := by nlinarith
  have hnum : HasDerivAt (fun y : ℝ => y * Φ y + p y)
      (1 * Φ x + x * (p x / (x ^ 2 - 1)) + -(qq c χ x) * Φ x) x :=
    ((hasDerivAt_id x).mul (hsol.hΦ x hx)).add (hsol.hp x hx)
  have hden : HasDerivAt (fun y : ℝ => y ^ 2 - 1) (2 * x) x := by
    simpa using (hasDerivAt_pow 2 x).sub_const 1
  have h := (hnum.mul (hasDerivAt_rt hx)).div hden hne
  simp only [Pi.mul_apply] at h
  have hdef : uu' Φ p = fun y => (y * Φ y + p y) * rt y / (y ^ 2 - 1) := rfl
  rw [hdef]
  convert h using 1
  simp only [uu, eps, qq]
  field_simp
  ring

/-- **The negative control for the correction, machine-checked.**

`hasDerivAt_uu'` proves that `eps` *is* the potential.  That alone does not show
the note's printed `(c²-χ+1)/(x²-1)` is *wrong* rather than an equivalent
rewriting, so here is the separating instance.  Take `c = χ = 0`, where the
equation `((x²-1)Φ')' = 0` has the solution `Φ ≡ 1` with `p ≡ 0`; then
`u = √(x²-1)`, and at `x = 2` the true `u''` is `-√3/9` while the printed
potential demands `-√3/3`.

Together with `hasDerivAt_uu'` and uniqueness of derivatives, this is a complete
refutation of Lemma 3.1 as printed. -/
lemma printed_potential_not_deriv :
    ¬ HasDerivAt (uu' (fun _ : ℝ => (1:ℝ)) (fun _ : ℝ => (0:ℝ)))
        (-((0:ℝ) ^ 2 + ((0:ℝ) ^ 2 - 0 + 1) / ((2:ℝ) ^ 2 - 1))
          * uu (fun _ : ℝ => (1:ℝ)) 2) 2 := by
  intro hbad
  have hsol : IsSolution 0 0 (fun _ : ℝ => (1:ℝ)) (fun _ : ℝ => (0:ℝ)) := by
    constructor
    · intro x _
      simpa using hasDerivAt_const x (1:ℝ)
    · intro x _
      simpa [qq] using hasDerivAt_const x (0:ℝ)
  have hgood := hasDerivAt_uu' hsol (by norm_num : (1:ℝ) < 2)
  have huniq := hgood.unique hbad
  have hr : (0:ℝ) < uu (fun _ : ℝ => (1:ℝ)) 2 := by
    have h := rt_pos (by norm_num : (1:ℝ) < 2)
    simpa [uu] using h
  rw [show eps (0:ℝ) 0 2 = 1 / 9 by norm_num [eps]] at huniq
  norm_num at huniq
  linarith

/-! ## Lemma 3.2 — the Lagrange system

`dilate-sum.md` Lemma 3.2 solves `u = α sin(cx) + β cos(cx)`,
`u' = c(α cos(cx) - β sin(cx))` for `(α, β)`.  The solution is *explicit*:

    α = u sin(cx) + u' cos(cx)/c,    β = u cos(cx) - u' sin(cx)/c ,

single-valued, globally defined algebraic functions of `(u, u')`.  **Nothing is
lifted along a curve**, which is the whole reason this file exists and Q1's
Prüfer angle does not (`lean/README.md`). -/

/-- `α = u sin(cx) + u' cos(cx)/c`. -/
noncomputable def al (c : ℝ) (U V : ℝ → ℝ) (x : ℝ) : ℝ :=
  U x * Real.sin (c * x) + V x * Real.cos (c * x) / c

/-- `β = u cos(cx) - u' sin(cx)/c`. -/
noncomputable def be (c : ℝ) (U V : ℝ → ℝ) (x : ℝ) : ℝ :=
  U x * Real.cos (c * x) - V x * Real.sin (c * x) / c

/-- `u = α sin(cx) + β cos(cx)`: the defining relation, and it needs **no
hypothesis whatever** — not even `c ≠ 0`, since the two `u'/c` terms cancel
identically. -/
lemma al_add_be (c : ℝ) (U V : ℝ → ℝ) (x : ℝ) :
    al c U V x * Real.sin (c * x) + be c U V x * Real.cos (c * x) = U x := by
  simp only [al, be]
  have h := Real.sin_sq_add_cos_sq (c * x)
  linear_combination U x * h

lemma hasDerivAt_sin_mul (c x : ℝ) :
    HasDerivAt (fun y : ℝ => Real.sin (c * y)) (c * Real.cos (c * x)) x := by
  have h : HasDerivAt (fun y : ℝ => c * y) c x := by
    simpa using (hasDerivAt_id x).const_mul c
  have h2 := (Real.hasDerivAt_sin (c * x)).comp x h
  simpa [mul_comm] using h2

lemma hasDerivAt_cos_mul (c x : ℝ) :
    HasDerivAt (fun y : ℝ => Real.cos (c * y)) (-(c * Real.sin (c * x))) x := by
  have h : HasDerivAt (fun y : ℝ => c * y) c x := by
    simpa using (hasDerivAt_id x).const_mul c
  have h2 := (Real.hasDerivAt_cos (c * x)).comp x h
  have : -Real.sin (c * x) * c = -(c * Real.sin (c * x)) := by ring
  simpa [this] using h2

/-- `α' = -(ε/c) u cos(cx)`, which is (3.2) of `dilate-sum.md`. -/
lemma hasDerivAt_al {c E : ℝ} {U V : ℝ → ℝ} {x : ℝ} (hc : c ≠ 0)
    (hU : HasDerivAt U (V x) x) (hV : HasDerivAt V (-(c ^ 2 + E) * U x) x) :
    HasDerivAt (al c U V) (-(E / c) * U x * Real.cos (c * x)) x := by
  have h1 : HasDerivAt (fun y => U y * Real.sin (c * y))
      (V x * Real.sin (c * x) + U x * (c * Real.cos (c * x))) x :=
    hU.mul (hasDerivAt_sin_mul c x)
  have h2 : HasDerivAt (fun y => V y * Real.cos (c * y) / c)
      ((-(c ^ 2 + E) * U x * Real.cos (c * x) + V x * -(c * Real.sin (c * x))) / c) x :=
    (hV.mul (hasDerivAt_cos_mul c x)).div_const c
  have h := h1.add h2
  have hdef : al c U V = fun y => U y * Real.sin (c * y) + V y * Real.cos (c * y) / c := rfl
  rw [hdef]
  convert h using 1
  field_simp
  ring

/-- `β' = (ε/c) u sin(cx)`, which is (3.2) of `dilate-sum.md`. -/
lemma hasDerivAt_be {c E : ℝ} {U V : ℝ → ℝ} {x : ℝ} (hc : c ≠ 0)
    (hU : HasDerivAt U (V x) x) (hV : HasDerivAt V (-(c ^ 2 + E) * U x) x) :
    HasDerivAt (be c U V) (E / c * U x * Real.sin (c * x)) x := by
  have h1 : HasDerivAt (fun y => U y * Real.cos (c * y))
      (V x * Real.cos (c * x) + U x * -(c * Real.sin (c * x))) x :=
    hU.mul (hasDerivAt_cos_mul c x)
  have h2 : HasDerivAt (fun y => V y * Real.sin (c * y) / c)
      ((-(c ^ 2 + E) * U x * Real.sin (c * x) + V x * (c * Real.cos (c * x))) / c) x :=
    (hV.mul (hasDerivAt_sin_mul c x)).div_const c
  have h := h1.sub h2
  have hdef : be c U V = fun y => U y * Real.cos (c * y) - V y * Real.sin (c * y) / c := rfl
  rw [hdef]
  convert h using 1
  field_simp
  ring

/-! ## The majorant, and Lemma 3.2's rate `(3.3)`

`dilate-sum.md` Lemma 3.2 bounds `∫_X^∞ ε` by `2(c²+1)/X` and concludes
`|α X - α_∞| + |β X - β_∞| ≤ 6cK₁|Φ(1)|/X`.  Formalised here **without any
integration theory**: `MM` is an explicit majorant *antiderivative*, `-MM' ≥ ε`
pointwise on `[√2,∞)`, and a two-sided monotonicity argument replaces
`∫_X^∞ |α'|`. -/

/-- `M x = 2c²/x + 4/(3x³)`, an explicit antiderivative of `-(2c²/x² + 4/x⁴)`,
which majorises the corrected `ε` on `[√2,∞)`. -/
noncomputable def MM (c x : ℝ) : ℝ := 2 * c ^ 2 / x + 4 / (3 * x ^ 3)

lemma MM_nonneg {c x : ℝ} (hx : 0 < x) : 0 ≤ MM c x := by
  have h1 : (0:ℝ) ≤ 2 * c ^ 2 / x := by positivity
  have h2 : (0:ℝ) ≤ 4 / (3 * x ^ 3) := by positivity
  simp only [MM]
  linarith

lemma hasDerivAt_MM (c : ℝ) {x : ℝ} (hx : 0 < x) :
    HasDerivAt (MM c) (-(2 * c ^ 2 / x ^ 2 + 4 / x ^ 4)) x := by
  have hx0 : x ≠ 0 := hx.ne'
  have h1 : HasDerivAt (fun y : ℝ => 2 * c ^ 2 / y) ((0 * x - 2 * c ^ 2 * 1) / x ^ 2) x :=
    (hasDerivAt_const x (2 * c ^ 2)).div (hasDerivAt_id x) hx0
  have hcube : HasDerivAt (fun y : ℝ => 3 * y ^ 3) (3 * (3 * x ^ 2)) x := by
    simpa using (hasDerivAt_pow 3 x).const_mul (3:ℝ)
  have hne : (3:ℝ) * x ^ 3 ≠ 0 := by positivity
  have h2 : HasDerivAt (fun y : ℝ => 4 / (3 * y ^ 3))
      ((0 * (3 * x ^ 3) - 4 * (3 * (3 * x ^ 2))) / (3 * x ^ 3) ^ 2) x :=
    (hasDerivAt_const x (4:ℝ)).div hcube hne
  have h := h1.add h2
  have hdef : MM c = fun y : ℝ => 2 * c ^ 2 / y + 4 / (3 * y ^ 3) := rfl
  rw [hdef]
  convert h using 1
  field_simp
  ring

/-- `ε ≥ 0` on `(1,∞)`, from `χ ≤ c²`.  (The *printed* potential also needs this;
the corrected one is even more comfortably positive, carrying an extra square.) -/
lemma eps_nonneg {c χ : ℝ} (hχ : χ ≤ c ^ 2) {x : ℝ} (hx : 1 < x) : 0 ≤ eps c χ x := by
  have h1 : (0:ℝ) < x ^ 2 - 1 := by nlinarith
  have h2 : (0:ℝ) ≤ (c ^ 2 - χ) / (x ^ 2 - 1) := div_nonneg (by linarith) h1.le
  have h3 : (0:ℝ) ≤ 1 / (x ^ 2 - 1) ^ 2 := by positivity
  simp only [eps]
  linarith

/-- **The corrected `ε` is majorised by `-MM'`.**  This single inequality is the
entire downstream footprint of Lemma 3.1, and it is why the note's slip changes
nothing: with the printed potential the same step gives `2c²/x² + 2/x²`, with the
true one `2c²/x² + 4/x⁴`, and both feed the same `3c²/x` at the next line. -/
lemma eps_le_deriv_MM {c χ : ℝ} (hχ0 : 0 ≤ χ) {x : ℝ} (hx : 2 ≤ x ^ 2) :
    eps c χ x ≤ 2 * c ^ 2 / x ^ 2 + 4 / x ^ 4 := by
  have hx2 : (0:ℝ) < x ^ 2 := by linarith
  have hd : (0:ℝ) < x ^ 2 - 1 := by linarith
  have h1 : (c ^ 2 - χ) / (x ^ 2 - 1) ≤ 2 * c ^ 2 / x ^ 2 := by
    rw [div_le_div_iff₀ hd hx2]
    nlinarith [sq_nonneg c, sq_nonneg x]
  have hx4 : (0:ℝ) < x ^ 4 := by nlinarith
  have hd2 : (0:ℝ) < (x ^ 2 - 1) ^ 2 := pow_pos hd 2
  have h2 : 1 / (x ^ 2 - 1) ^ 2 ≤ 4 / x ^ 4 := by
    rw [div_le_div_iff₀ hd2 hx4]
    nlinarith
  simp only [eps]
  linarith

/-- `M x ≤ 3c²/x` on `[√2,∞)` when `c² ≥ 2`: this is `dilate-sum.md`'s
`∫_X^∞ ε ≤ 3c²/X`, reached through the corrected potential. -/
lemma MM_le {c x : ℝ} (hc : 2 ≤ c ^ 2) (hx2 : 2 ≤ x ^ 2) (hx : 0 < x) :
    MM c x ≤ 3 * c ^ 2 / x := by
  have h : 4 / (3 * x ^ 3) ≤ c ^ 2 / x := by
    rw [div_le_div_iff₀ (by positivity) hx]
    have h1 : (2:ℝ) * x ≤ x ^ 3 := by nlinarith
    nlinarith [h1, hc, hx]
  have he : 3 * c ^ 2 / x = 2 * c ^ 2 / x + c ^ 2 / x := by ring
  simp only [MM]
  linarith

/-! ## Replacing `∫_X^∞ |α'|` by a monotonicity argument -/

/-- If `|f'| ≤ k·(-g')` throughout `[X,∞)`, then `|f y - f x| ≤ k(g x - g y)` for
`X ≤ x ≤ y`.  Applied with `f = α`, `g = M` this is Lemma 3.2's `(3.3)` in Cauchy
form, proved from `f + kg` antitone and `f - kg` monotone — no integration
theory, and no need to know in advance that the limits exist.

Note it does **not** need `0 ≤ k`: the two monotonicity arguments only ever use
`|f'| ≤ k·(-g')` through `abs_le`. -/
lemma abs_sub_le_of_deriv_le {f g f' g' : ℝ → ℝ} {X k : ℝ}
    (hf : ∀ z ∈ Ici X, HasDerivAt f (f' z) z)
    (hg : ∀ z ∈ Ici X, HasDerivAt g (g' z) z)
    (hbd : ∀ z ∈ Ici X, |f' z| ≤ k * -g' z)
    {x y : ℝ} (hx : X ≤ x) (hxy : x ≤ y) :
    |f y - f x| ≤ k * (g x - g y) := by
  have hA : AntitoneOn (fun z => f z + k * g z) (Ici X) := by
    refine antitoneOn_of_hasDerivWithinAt_nonpos (f' := fun z => f' z + k * g' z)
      (convex_Ici X) ?_ ?_ ?_
    · intro z hz
      exact ((hf z hz).add ((hg z hz).const_mul k)).continuousAt.continuousWithinAt
    · intro z hz
      rw [interior_Ici] at hz
      have hzI : z ∈ Ici X := Set.mem_Ici.mpr (le_of_lt (Set.mem_Ioi.mp hz))
      exact ((hf z hzI).add ((hg z hzI).const_mul k)).hasDerivWithinAt
    · intro z hz
      rw [interior_Ici] at hz
      have hzI : z ∈ Ici X := Set.mem_Ici.mpr (le_of_lt (Set.mem_Ioi.mp hz))
      have h := (abs_le.mp (hbd z hzI)).2
      simp only
      linarith
  have hB : MonotoneOn (fun z => f z - k * g z) (Ici X) := by
    refine monotoneOn_of_hasDerivWithinAt_nonneg (f' := fun z => f' z - k * g' z)
      (convex_Ici X) ?_ ?_ ?_
    · intro z hz
      exact ((hf z hz).sub ((hg z hz).const_mul k)).continuousAt.continuousWithinAt
    · intro z hz
      rw [interior_Ici] at hz
      have hzI : z ∈ Ici X := Set.mem_Ici.mpr (le_of_lt (Set.mem_Ioi.mp hz))
      exact ((hf z hzI).sub ((hg z hzI).const_mul k)).hasDerivWithinAt
    · intro z hz
      rw [interior_Ici] at hz
      have hzI : z ∈ Ici X := Set.mem_Ici.mpr (le_of_lt (Set.mem_Ioi.mp hz))
      have h := (abs_le.mp (hbd z hzI)).1
      simp only
      linarith
  have hxI : x ∈ Ici X := Set.mem_Ici.mpr hx
  have hyI : y ∈ Ici X := Set.mem_Ici.mpr (le_trans hx hxy)
  have h1 : f y + k * g y ≤ f x + k * g x := hA hxI hyI hxy
  have h2 : f x - k * g x ≤ f y - k * g y := hB hxI hyI hxy
  rw [abs_le]
  constructor <;> linarith

/-! ## Lemma 3.2's rate, and Lemma 3.3 as a hypothesis -/

section Rate

variable {c χ K₁ P : ℝ} {Φ p : ℝ → ℝ}

/-- Q1 gives `|u| ≤ K₁P` on `(1,∞)` — the step `dilate-sum.md` Lemma 3.2 calls
"the bound on `u` is Q1 and only Q1".  `h1-mean-value.md`'s `|Φ| ≤ |Φ 1|` would
give `|u| ≤ √(x²-1)|Φ 1|`, which grows. -/
lemma abs_uu_le (hQ1 : ∀ x : ℝ, 1 ≤ x → x * |Φ x| ≤ K₁ * P) {x : ℝ} (hx : 1 < x) :
    |uu Φ x| ≤ K₁ * P := by
  have h0 : (0:ℝ) ≤ rt x := rt_nonneg x
  have hle : rt x ≤ x := rt_le (by linarith)
  calc |uu Φ x| = rt x * |Φ x| := by
        simp only [uu, abs_mul, abs_of_nonneg h0]
    _ ≤ x * |Φ x| := mul_le_mul_of_nonneg_right hle (abs_nonneg _)
    _ ≤ K₁ * P := hQ1 x hx.le

/-- Lemma 3.2's `(3.3)` for `α`, in Cauchy form.  Everything here is ODE;
**the eigenrelation (F) is not used**. -/
lemma abs_sub_al_le (hc : Real.sqrt 2 < c) (hχ0 : 0 ≤ χ) (hχ : χ < c ^ 2)
    (hP : 0 ≤ P) (hK₁ : 0 ≤ K₁) (hsol : IsSolution c χ Φ p)
    (hQ1 : ∀ x : ℝ, 1 ≤ x → x * |Φ x| ≤ K₁ * P)
    {x y : ℝ} (hx : Real.sqrt 2 ≤ x) (hxy : x ≤ y) :
    |al c (uu Φ) (uu' Φ p) y - al c (uu Φ) (uu' Φ p) x|
      ≤ K₁ * P / c * (MM c x - MM c y) := by
  have hs2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hs2pos : (0:ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  have hs2gt : (1:ℝ) < Real.sqrt 2 := by nlinarith
  have hc0 : (0:ℝ) < c := lt_trans hs2pos hc
  have hcne : c ≠ 0 := hc0.ne'
  have hk : (0:ℝ) ≤ K₁ * P / c := by positivity
  refine abs_sub_le_of_deriv_le (f := al c (uu Φ) (uu' Φ p)) (g := MM c)
    (f' := fun z => -(eps c χ z / c) * uu Φ z * Real.cos (c * z))
    (g' := fun z => -(2 * c ^ 2 / z ^ 2 + 4 / z ^ 4)) (X := Real.sqrt 2)
    (k := K₁ * P / c) ?_ ?_ ?_ hx hxy
  · intro z hz
    have hz1 : 1 < z := lt_of_lt_of_le hs2gt hz
    exact hasDerivAt_al hcne (hasDerivAt_uu hsol hz1) (hasDerivAt_uu' hsol hz1)
  · intro z hz
    exact hasDerivAt_MM c (lt_of_lt_of_le hs2pos hz)
  · intro z hz
    have hzge : Real.sqrt 2 ≤ z := hz
    have hz1 : 1 < z := lt_of_lt_of_le hs2gt hzge
    have hz2 : 2 ≤ z ^ 2 := by nlinarith [hs2pos, hzge]
    have hE0 : (0:ℝ) ≤ eps c χ z := eps_nonneg hχ.le hz1
    have hEc : (0:ℝ) ≤ eps c χ z / c := div_nonneg hE0 hc0.le
    have hEle : eps c χ z ≤ 2 * c ^ 2 / z ^ 2 + 4 / z ^ 4 := eps_le_deriv_MM hχ0 hz2
    have hU : |uu Φ z| ≤ K₁ * P := abs_uu_le hQ1 hz1
    have hmain : |-(eps c χ z / c) * uu Φ z * Real.cos (c * z)|
        ≤ K₁ * P / c * (2 * c ^ 2 / z ^ 2 + 4 / z ^ 4) := by
      calc |-(eps c χ z / c) * uu Φ z * Real.cos (c * z)|
          = eps c χ z / c * |uu Φ z| * |Real.cos (c * z)| := by
            rw [abs_mul, abs_mul, abs_neg, abs_of_nonneg hEc]
        _ ≤ eps c χ z / c * (K₁ * P) * 1 :=
            mul_le_mul (mul_le_mul_of_nonneg_left hU hEc) (Real.abs_cos_le_one _)
              (abs_nonneg _) (mul_nonneg hEc (mul_nonneg hK₁ hP))
        _ = K₁ * P / c * eps c χ z := by ring
        _ ≤ K₁ * P / c * (2 * c ^ 2 / z ^ 2 + 4 / z ^ 4) :=
            mul_le_mul_of_nonneg_left hEle hk
    simpa using hmain

/-- Lemma 3.2's `(3.3)` for `β`.  Same proof, same constant, same hypotheses;
**(F) is not used here either** — it enters only at `tail_le`'s `hβ`. -/
lemma abs_sub_be_le (hc : Real.sqrt 2 < c) (hχ0 : 0 ≤ χ) (hχ : χ < c ^ 2)
    (hP : 0 ≤ P) (hK₁ : 0 ≤ K₁) (hsol : IsSolution c χ Φ p)
    (hQ1 : ∀ x : ℝ, 1 ≤ x → x * |Φ x| ≤ K₁ * P)
    {x y : ℝ} (hx : Real.sqrt 2 ≤ x) (hxy : x ≤ y) :
    |be c (uu Φ) (uu' Φ p) y - be c (uu Φ) (uu' Φ p) x|
      ≤ K₁ * P / c * (MM c x - MM c y) := by
  have hs2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hs2pos : (0:ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  have hs2gt : (1:ℝ) < Real.sqrt 2 := by nlinarith
  have hc0 : (0:ℝ) < c := lt_trans hs2pos hc
  have hcne : c ≠ 0 := hc0.ne'
  have hk : (0:ℝ) ≤ K₁ * P / c := by positivity
  refine abs_sub_le_of_deriv_le (f := be c (uu Φ) (uu' Φ p)) (g := MM c)
    (f' := fun z => eps c χ z / c * uu Φ z * Real.sin (c * z))
    (g' := fun z => -(2 * c ^ 2 / z ^ 2 + 4 / z ^ 4)) (X := Real.sqrt 2)
    (k := K₁ * P / c) ?_ ?_ ?_ hx hxy
  · intro z hz
    have hz1 : 1 < z := lt_of_lt_of_le hs2gt hz
    exact hasDerivAt_be hcne (hasDerivAt_uu hsol hz1) (hasDerivAt_uu' hsol hz1)
  · intro z hz
    exact hasDerivAt_MM c (lt_of_lt_of_le hs2pos hz)
  · intro z hz
    have hzge : Real.sqrt 2 ≤ z := hz
    have hz1 : 1 < z := lt_of_lt_of_le hs2gt hzge
    have hz2 : 2 ≤ z ^ 2 := by nlinarith [hs2pos, hzge]
    have hE0 : (0:ℝ) ≤ eps c χ z := eps_nonneg hχ.le hz1
    have hEc : (0:ℝ) ≤ eps c χ z / c := div_nonneg hE0 hc0.le
    have hEle : eps c χ z ≤ 2 * c ^ 2 / z ^ 2 + 4 / z ^ 4 := eps_le_deriv_MM hχ0 hz2
    have hU : |uu Φ z| ≤ K₁ * P := abs_uu_le hQ1 hz1
    have hmain : |eps c χ z / c * uu Φ z * Real.sin (c * z)|
        ≤ K₁ * P / c * (2 * c ^ 2 / z ^ 2 + 4 / z ^ 4) := by
      calc |eps c χ z / c * uu Φ z * Real.sin (c * z)|
          = eps c χ z / c * |uu Φ z| * |Real.sin (c * z)| := by
            rw [abs_mul, abs_mul, abs_of_nonneg hEc]
        _ ≤ eps c χ z / c * (K₁ * P) * 1 :=
            mul_le_mul (mul_le_mul_of_nonneg_left hU hEc) (Real.abs_sin_le_one _)
              (abs_nonneg _) (mul_nonneg hEc (mul_nonneg hK₁ hP))
        _ = K₁ * P / c * eps c χ z := by ring
        _ ≤ K₁ * P / c * (2 * c ^ 2 / z ^ 2 + 4 / z ^ 4) :=
            mul_le_mul_of_nonneg_left hEle hk
    simpa using hmain

/-- **Lemma 3.2's `(3.3)`.**  `|α x - α_∞| + |β x - β_∞| ≤ 6cK₁P/x` for `x ≥ √2`,
with `α_∞ = a₁` and `β_∞ = 0` supplied by Lemma 3.3 (`hα`, `hβ`) — the one place
in this file where the finite-Fourier eigenrelation **(F)** is used. -/
lemma tail_le (hc : Real.sqrt 2 < c) (hχ0 : 0 ≤ χ) (hχ : χ < c ^ 2)
    (hP : 0 ≤ P) (hK₁ : 0 ≤ K₁) (hsol : IsSolution c χ Φ p)
    (hQ1 : ∀ x : ℝ, 1 ≤ x → x * |Φ x| ≤ K₁ * P)
    {a₁ : ℝ}
    (hα : Tendsto (al c (uu Φ) (uu' Φ p)) atTop (𝓝 a₁))
    (hβ : Tendsto (be c (uu Φ) (uu' Φ p)) atTop (𝓝 0))
    {x : ℝ} (hx : Real.sqrt 2 ≤ x) :
    |al c (uu Φ) (uu' Φ p) x - a₁| + |be c (uu Φ) (uu' Φ p) x - 0|
      ≤ 6 * c * K₁ * P / x := by
  have hs2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hs2pos : (0:ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  have hs2gt : (1:ℝ) < Real.sqrt 2 := by nlinarith
  have hc0 : (0:ℝ) < c := lt_trans hs2pos hc
  have hc2 : (2:ℝ) ≤ c ^ 2 := by nlinarith
  have hx0 : (0:ℝ) < x := lt_of_lt_of_le hs2pos hx
  have hx2 : (2:ℝ) ≤ x ^ 2 := by nlinarith
  have hk : (0:ℝ) ≤ K₁ * P / c := by positivity
  have key : ∀ (F : ℝ → ℝ) (L : ℝ), Tendsto F atTop (𝓝 L) →
      (∀ y : ℝ, x ≤ y → |F y - F x| ≤ K₁ * P / c * (MM c x - MM c y)) →
      |F x - L| ≤ K₁ * P / c * MM c x := by
    intro F L hL hbd
    have hev : ∀ᶠ y in atTop, |F y - F x| ≤ K₁ * P / c * MM c x := by
      filter_upwards [eventually_ge_atTop x, eventually_gt_atTop (0:ℝ)] with y hy hy0
      have h := hbd y hy
      have hM : (0:ℝ) ≤ MM c y := MM_nonneg hy0
      nlinarith
    have htend : Tendsto (fun y => |F y - F x|) atTop (𝓝 |L - F x|) :=
      (hL.sub_const (F x)).abs
    have h := le_of_tendsto htend hev
    rwa [abs_sub_comm] at h
  have hA := key _ _ hα (fun y hy => abs_sub_al_le hc hχ0 hχ hP hK₁ hsol hQ1 hx hy)
  have hB := key _ _ hβ (fun y hy => abs_sub_be_le hc hχ0 hχ hP hK₁ hsol hQ1 hx hy)
  have hMM : MM c x ≤ 3 * c ^ 2 / x := MM_le hc2 hx2 hx0
  have h1 : K₁ * P / c * MM c x ≤ K₁ * P / c * (3 * c ^ 2 / x) :=
    mul_le_mul_of_nonneg_left hMM hk
  have h2 : K₁ * P / c * (3 * c ^ 2 / x) = 3 * c * K₁ * P / x := by
    field_simp
  have h3 : 6 * c * K₁ * P / x = 2 * (3 * c * K₁ * P / x) := by ring
  linarith

end Rate

/-! ## Proposition 4.1 -/

/-- **Proposition 4.1(i) of `dilate-sum.md`.**  `|W x| ≤ (K₁ + A₁)P/x` for
`x ≥ 1`, where `A₁P` bounds `|a₁|`; the note's `B₁ = K₁ + 2/(c|μ_Φ|)` is this
with `A₁ = 2/(c|μ_Φ|)`, since `|a₁| = 2|Φ(1)|/(c|μ_Φ|)`.

**This is what formalising localises about part (i).**  It uses Q1 and
`|sin| ≤ 1` and *nothing else*: no ODE, no Lagrange system, no `β_∞ = 0`, no
`0 ≤ χ`, no `χ < c²`, no `c > √2` — indeed no hypothesis on `c` at all.  Part
(ii) is where all of that is spent. -/
theorem prop41_i {c a₁ K₁ A₁ P : ℝ} {Φ W : ℝ → ℝ}
    (ha₁ : |a₁| ≤ A₁ * P)
    (hQ1 : ∀ x : ℝ, 1 ≤ x → x * |Φ x| ≤ K₁ * P)
    (hsplit : ∀ x : ℝ, 1 ≤ x → Φ x = a₁ * Real.sin (c * x) / x + W x)
    {x : ℝ} (hx : 1 ≤ x) :
    |W x| ≤ (K₁ + A₁) * P / x := by
  have hx0 : (0:ℝ) < x := lt_of_lt_of_le zero_lt_one hx
  have hW : W x = Φ x - a₁ * Real.sin (c * x) / x := by
    have h := hsplit x hx
    linarith
  have hsin : |a₁ * Real.sin (c * x) / x| ≤ |a₁| / x := by
    rw [abs_div, abs_of_pos hx0, abs_mul, div_le_div_iff₀ hx0 hx0]
    nlinarith [Real.abs_sin_le_one (c * x), abs_nonneg a₁, abs_nonneg (Real.sin (c * x)), hx0,
      mul_nonneg (abs_nonneg a₁) hx0.le]
  have hΦ : |Φ x| ≤ K₁ * P / x := by
    rw [le_div_iff₀ hx0, mul_comm]
    exact hQ1 x hx
  have hstep : |a₁| / x ≤ A₁ * P / x := by
    rw [div_le_div_iff₀ hx0 hx0]
    nlinarith [ha₁, hx0]
  have htri : |Φ x - a₁ * Real.sin (c * x) / x| ≤ |Φ x| + |a₁ * Real.sin (c * x) / x| := by
    have h := abs_add_le (Φ x) (-(a₁ * Real.sin (c * x) / x))
    simpa [sub_eq_add_neg] using h
  calc |W x| = |Φ x - a₁ * Real.sin (c * x) / x| := by rw [hW]
    _ ≤ |Φ x| + |a₁ * Real.sin (c * x) / x| := htri
    _ ≤ K₁ * P / x + A₁ * P / x := by linarith
    _ = (K₁ + A₁) * P / x := by ring

/-- **Proposition 4.1(ii) of `dilate-sum.md`.**  `|W x| ≤ K₁(6c + 1/√2)P/x²` for
`x ≥ √2`.

Every hypothesis is genuinely spent: the ODE (`hsol`), `0 ≤ χ < c²` and `c > √2`
(through `eps_nonneg`, `eps_le_deriv_MM`, `MM_le`), **Q1** (`hQ1`, for
`|u| ≤ K₁P`) and **Lemma 3.3** (`hα`, `hβ`) — the last of which is where the
finite-Fourier eigenrelation (F) enters, and without which the statement is
false by `dilate-sum.md` Cor. 3.4. -/
theorem prop41_ii {c χ K₁ P a₁ : ℝ} {Φ p W : ℝ → ℝ}
    (hc : Real.sqrt 2 < c) (hχ0 : 0 ≤ χ) (hχ : χ < c ^ 2)
    (hP : 0 ≤ P) (hK₁ : 0 ≤ K₁)
    (hsol : IsSolution c χ Φ p)
    (hQ1 : ∀ x : ℝ, 1 ≤ x → x * |Φ x| ≤ K₁ * P)
    (hα : Tendsto (al c (uu Φ) (uu' Φ p)) atTop (𝓝 a₁))
    (hβ : Tendsto (be c (uu Φ) (uu' Φ p)) atTop (𝓝 0))
    (hsplit : ∀ x : ℝ, 1 ≤ x → Φ x = a₁ * Real.sin (c * x) / x + W x)
    {x : ℝ} (hx : Real.sqrt 2 ≤ x) :
    |W x| ≤ K₁ * (6 * c + 1 / Real.sqrt 2) * P / x ^ 2 := by
  have hs2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hs2pos : (0:ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  have hs2gt : (1:ℝ) < Real.sqrt 2 := by nlinarith
  have hx0 : (0:ℝ) < x := lt_of_lt_of_le hs2pos hx
  have hxne : x ≠ 0 := hx0.ne'
  have hx1 : (1:ℝ) < x := lt_of_lt_of_le hs2gt hx
  have hx2 : (2:ℝ) ≤ x ^ 2 := by nlinarith
  have hr : (0:ℝ) < rt x := rt_pos hx1
  have hrne : rt x ≠ 0 := hr.ne'
  have hrsq : rt x ^ 2 = x ^ 2 - 1 := rt_sq hx1
  have hrle : rt x ≤ x := rt_le hx0.le
  -- `0 ≤ x/rt x - 1 ≤ 1/x²`
  have hratio0 : (0:ℝ) ≤ x / rt x - 1 := by
    have h : (1:ℝ) ≤ x / rt x := (one_le_div hr).mpr hrle
    linarith
  have hcube : x * x ^ 2 ≤ (1 + x ^ 2) * rt x := by
    have hprod : ((1 + x ^ 2) * rt x - x * x ^ 2) * ((1 + x ^ 2) * rt x + x * x ^ 2)
        = x ^ 4 - x ^ 2 - 1 := by
      linear_combination (1 + x ^ 2) ^ 2 * hrsq
    have hpos : (0:ℝ) < (1 + x ^ 2) * rt x + x * x ^ 2 := by positivity
    have hnum : (0:ℝ) ≤ x ^ 4 - x ^ 2 - 1 := by nlinarith [hx2]
    nlinarith [hprod, hpos, hnum]
  have hratio : x / rt x - 1 ≤ 1 / x ^ 2 := by
    rw [sub_le_iff_le_add, div_le_iff₀ hr,
      show (1 / x ^ 2 + 1) * rt x = (1 + x ^ 2) * rt x / x ^ 2 by field_simp,
      le_div_iff₀ (by positivity : (0:ℝ) < x ^ 2)]
    linarith [hcube]
  -- the splitting of `dilate-sum.md` §4, multiplied through by `x`
  have hW' : x * W x = x * Φ x - a₁ * Real.sin (c * x) := by
    have h := hsplit x hx1.le
    have h2 : x * Φ x = x * (a₁ * Real.sin (c * x) / x + W x) := by rw [← h]
    rw [h2]
    field_simp
    ring
  have hxrt : x / rt x * uu Φ x = x * Φ x := by
    simp only [uu]
    field_simp
  have hrepr := al_add_be c (uu Φ) (uu' Φ p) x
  have hkey : x * W x = (x / rt x - 1) * uu Φ x
      + ((al c (uu Φ) (uu' Φ p) x - a₁) * Real.sin (c * x)
        + (be c (uu Φ) (uu' Φ p) x - 0) * Real.cos (c * x)) := by
    rw [hW']
    linear_combination -hxrt - hrepr
  -- bound each piece
  have hU : |uu Φ x| ≤ K₁ * P := abs_uu_le hQ1 hx1
  have htail := tail_le hc hχ0 hχ hP hK₁ hsol hQ1 hα hβ hx
  have hb1 : |(x / rt x - 1) * uu Φ x| ≤ 1 / x ^ 2 * (K₁ * P) := by
    rw [abs_mul, abs_of_nonneg hratio0]
    exact mul_le_mul hratio hU (abs_nonneg _) (by positivity)
  have hb2 : |(al c (uu Φ) (uu' Φ p) x - a₁) * Real.sin (c * x)
      + (be c (uu Φ) (uu' Φ p) x - 0) * Real.cos (c * x)| ≤ 6 * c * K₁ * P / x := by
    refine le_trans (abs_add_le _ _) (le_trans ?_ htail)
    have h1 : |(al c (uu Φ) (uu' Φ p) x - a₁) * Real.sin (c * x)|
        ≤ |al c (uu Φ) (uu' Φ p) x - a₁| := by
      rw [abs_mul]
      nlinarith [Real.abs_sin_le_one (c * x), abs_nonneg (al c (uu Φ) (uu' Φ p) x - a₁),
        abs_nonneg (Real.sin (c * x))]
    have h2 : |(be c (uu Φ) (uu' Φ p) x - 0) * Real.cos (c * x)|
        ≤ |be c (uu Φ) (uu' Φ p) x - 0| := by
      rw [abs_mul]
      nlinarith [Real.abs_cos_le_one (c * x), abs_nonneg (be c (uu Φ) (uu' Φ p) x - 0),
        abs_nonneg (Real.cos (c * x))]
    linarith
  have hxW : x * |W x| ≤ 1 / x ^ 2 * (K₁ * P) + 6 * c * K₁ * P / x := by
    have habs : |x * W x| = x * |W x| := by rw [abs_mul, abs_of_pos hx0]
    rw [← habs, hkey]
    exact le_trans (abs_add_le _ _) (add_le_add hb1 hb2)
  -- assemble: `x²|W| ≤ K₁P/x + 6cK₁P ≤ K₁P(6c + 1/√2)`
  have hstep : x ^ 2 * |W x| ≤ K₁ * P / x + 6 * c * K₁ * P := by
    have h := mul_le_mul_of_nonneg_left hxW hx0.le
    have e1 : x * (x * |W x|) = x ^ 2 * |W x| := by ring
    have e2 : x * (1 / x ^ 2 * (K₁ * P)) = K₁ * P / x := by field_simp
    have e3 : x * (6 * c * K₁ * P / x) = 6 * c * K₁ * P := by field_simp
    rw [e1, mul_add, e2, e3] at h
    exact h
  have hKP : (0:ℝ) ≤ K₁ * P := mul_nonneg hK₁ hP
  have hinv : 1 / x ≤ 1 / Real.sqrt 2 := one_div_le_one_div_of_le hs2pos hx
  have hfin : K₁ * P / x ≤ K₁ * P * (1 / Real.sqrt 2) := by
    have he : K₁ * P / x = K₁ * P * (1 / x) := by ring
    rw [he]
    exact mul_le_mul_of_nonneg_left hinv hKP
  rw [le_div_iff₀ (by positivity : (0:ℝ) < x ^ 2)]
  nlinarith [hstep, hfin]

/-! ## Theorem `thm:q2` with Proposition 4.1 discharged

`DilateSum.theorem_q2` took `hW1` and `hW2` as hypotheses.  Here they are the
conclusions of `prop41_i` and `prop41_ii`, so what remains are exactly **Q1** and
**Lemma 3.3** — which is `dilate-sum.md`'s own account of where Q2 rests. -/

/-- **Theorem 5.1 of `dilate-sum.md` (Theorem `thm:q2`), resting on Q1 and the
eigenrelation rather than on Prop. 4.1.**

The split point `X` is left free subject to `√2 ≤ X`, so the note's
`X_* = max(√2, B₂/B₁)` — the choice that makes the constant
`K_P(c) = O(log c)` — is an instance. -/
theorem theorem_q2_of_prolate {c χ t a₁ K₁ A₁ P X : ℝ} {Φ p W : ℝ → ℝ}
    (ht : 1 < t) (hc : Real.sqrt 2 < c) (hχ0 : 0 ≤ χ) (hχ : χ < c ^ 2)
    (hX : Real.sqrt 2 ≤ X)
    (hP : 0 ≤ P) (hK₁ : 0 ≤ K₁) (hA₁ : 0 ≤ A₁)
    (hsol : IsSolution c χ Φ p)
    (ha₁ : |a₁| ≤ A₁ * P)
    (hQ1 : ∀ x : ℝ, 1 ≤ x → x * |Φ x| ≤ K₁ * P)
    (hα : Tendsto (al c (uu Φ) (uu' Φ p)) atTop (𝓝 a₁))
    (hβ : Tendsto (be c (uu Φ) (uu' Φ p)) atTop (𝓝 0))
    (hsplit : ∀ x : ℝ, 1 ≤ x → Φ x = a₁ * Real.sin (c * x) / x + W x) :
    ∃ S : ℝ,
      Tendsto (fun N => ∑ m ∈ Finset.range N, Φ (((m : ℝ) + 1) * t)) atTop (𝓝 S) ∧
      t * |S| ≤ π * |a₁| / 2
        + (K₁ + A₁) * P * (1 + Real.log X)
        + 2 * (K₁ * (6 * c + 1 / Real.sqrt 2)) * P / X := by
  have hs2 : Real.sqrt 2 ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hs2pos : (0:ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  have hs2ge : (1:ℝ) ≤ Real.sqrt 2 := by nlinarith
  have hX1 : (1:ℝ) ≤ X := le_trans hs2ge hX
  have hc0 : (0:ℝ) < c := lt_trans hs2pos hc
  exact DilateSum.theorem_q2 (c := c) (t := t) (a₁ := a₁) (P := P)
    (B₁ := K₁ + A₁) (B₂ := K₁ * (6 * c + 1 / Real.sqrt 2)) (X := X)
    (Φ := Φ) (W := W)
    ht hP (by linarith) (by positivity) hX1 hsplit
    (fun x hx => prop41_i ha₁ hQ1 hsplit hx)
    (fun x hx => prop41_ii hc hχ0 hχ hP hK₁ hsol hQ1 hα hβ hsplit (le_trans hX hx))

end Riemann.Remainder
