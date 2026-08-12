/-
# Lemmas 3.1 and 4.1 of `notes/band-edge-connection.md`

The elementary algebraic layer sitting between Lemma 5.1 (`Riemann/Sturm.lean`)
and Theorem 5.2 (Q1).  These are the "four elementary bounds" that the
oscillatory-integral estimate (Proposition 4.2) consumes.

Everything here is about the coefficient functions of the prolate equation and
nothing else; no solution `Φ` appears.  In the notation of
`band-edge-connection.md` §§2–4,

    u = 1/(x²-1),   v = c²/q,   f = (x/2)(u+v),   k = √(q/(x²-1)),

with `q = c²x² - χ` as in `Riemann/Sturm.lean`.

## Where the hypotheses bite

* Lemma 3.1 (`c < k`, `lt_kk`) needs `χ < c²` and `0 < c`.
* `v ≤ 2/x²` (`vv_le`), `f ≤ 2/x` (`ff_le`) and the derivative formula for `k`
  (`hasDerivAt_kk`) need **neither** `0 < c` nor `0 ≤ χ` — only `χ < c²`, and
  `√2 ≤ x` for the two bounds.  The note fixes `c > √2` and `0 ≤ χ < c²`
  throughout §§2–5; these three need strictly less.  A tightening, not a
  correction: the blanket hypotheses hold in the intended application.
* **`0 ≤ χ` is needed exactly once**, for `|k'| ≤ 4c/x³`, and nowhere else — the
  note says so in as many words ("This last step is the only place `χ ≥ 0` is
  used, and it is the only place it is needed"), and formalising confirms it:
  that bound — `abs_deriv_kk_le`, and its `deriv`-form restatement
  `abs_deriv_kk_le'` — is the only statement in either file carrying `0 ≤ χ`.

## Mathlib

Built against mathlib `5e932f97dd25535344f80f9dd8da3aab83df0fe6` (tag
`v4.29.1`), Lean toolchain `leanprover/lean4:v4.29.1`.
-/
import Riemann.Sturm

namespace Riemann.Prolate

open Set Filter Topology

variable (c χ : ℝ)

/-! ## The coefficient functions -/

/-- `u x = 1/(x²-1)`. -/
noncomputable def uu (x : ℝ) : ℝ := 1 / (x ^ 2 - 1)

/-- `v x = c²/q x`. -/
noncomputable def vv (x : ℝ) : ℝ := c ^ 2 / qq c χ x

/-- `f x = (x/2)(u x + v x)`, the logarithmic-derivative coefficient `D'/(4D)`
of `band-edge-connection.md` (2.3). -/
noncomputable def ff (x : ℝ) : ℝ := x / 2 * (uu x + vv c χ x)

/-- `k x = √(q x/(x²-1))`, the local wavenumber of `band-edge-connection.md`
(2.3). -/
noncomputable def kk (x : ℝ) : ℝ := Real.sqrt (qq c χ x / (x ^ 2 - 1))

lemma uu_pos {x : ℝ} (hx : 1 < x) : 0 < uu x := by
  have : (0:ℝ) < x ^ 2 - 1 := by nlinarith
  simp only [uu]; positivity

lemma vv_pos (hc : 0 < c) (hχ : χ < c ^ 2) {x : ℝ} (hx : 1 < x) : 0 < vv c χ x := by
  have := qq_pos c χ hχ hx.le
  simp only [vv]; positivity

/-! ## Lemma 3.1 -/

/-- The identity behind Lemma 3.1: `k² = c² + (c²-χ)u`. -/
lemma sq_kk (hχ : χ < c ^ 2) {x : ℝ} (hx : 1 < x) :
    (kk c χ x) ^ 2 = c ^ 2 + (c ^ 2 - χ) * uu x := by
  have hx1 : (0:ℝ) < x ^ 2 - 1 := by nlinarith
  have hq : (0:ℝ) < qq c χ x := qq_pos c χ hχ hx.le
  have hnn : (0:ℝ) ≤ qq c χ x / (x ^ 2 - 1) := by positivity
  simp only [kk, uu]
  rw [Real.sq_sqrt hnn, qq]
  field_simp
  ring

/-- **Lemma 3.1** (`band-edge-connection.md` §3).  `k > c` on `(1,∞)`. -/
lemma lt_kk (hc : 0 < c) (hχ : χ < c ^ 2) {x : ℝ} (hx : 1 < x) : c < kk c χ x := by
  have hsq : (kk c χ x) ^ 2 = c ^ 2 + (c ^ 2 - χ) * uu x := sq_kk c χ hχ hx
  have hu : 0 < uu x := uu_pos hx
  have hpos : (0:ℝ) < (c ^ 2 - χ) * uu x := mul_pos (by linarith) hu
  have hk0 : 0 ≤ kk c χ x := Real.sqrt_nonneg _
  nlinarith

/-! ## Lemma 4.1 — the four elementary bounds

Throughout, `√2 ≤ x`; the note restricts to this range for §4. -/

lemma two_le_sq {x : ℝ} (hx : Real.sqrt 2 ≤ x) : (2:ℝ) ≤ x ^ 2 := by
  have h0 : (0:ℝ) ≤ Real.sqrt 2 := Real.sqrt_nonneg 2
  nlinarith [Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)]

lemma one_lt_of_sqrt_two_le {x : ℝ} (hx : Real.sqrt 2 ≤ x) : 1 < x := by
  have := two_le_sq hx
  nlinarith [Real.sqrt_nonneg 2, hx]

/-- `u ≤ 2/x²`, because `x² - 1 ≥ x²/2` when `x² ≥ 2`. -/
lemma uu_le {x : ℝ} (hx : Real.sqrt 2 ≤ x) : uu x ≤ 2 / x ^ 2 := by
  have h2 : (2:ℝ) ≤ x ^ 2 := two_le_sq hx
  have hx1 : (0:ℝ) < x ^ 2 - 1 := by linarith
  have hx2 : (0:ℝ) < x ^ 2 := by linarith
  rw [uu, div_le_div_iff₀ hx1 hx2]
  nlinarith

/-- `v ≤ 2/x²`, because `q > c²(x²-1) ≥ c²x²/2`. -/
lemma vv_le (hχ : χ < c ^ 2) {x : ℝ} (hx : Real.sqrt 2 ≤ x) :
    vv c χ x ≤ 2 / x ^ 2 := by
  have h2 : (2:ℝ) ≤ x ^ 2 := two_le_sq hx
  have hx2 : (0:ℝ) < x ^ 2 := by linarith
  have hx1 : 1 < x := one_lt_of_sqrt_two_le hx
  have hq : (0:ℝ) < qq c χ x := qq_pos c χ hχ hx1.le
  rw [vv, div_le_div_iff₀ hq hx2, qq]
  nlinarith [mul_nonneg (sq_nonneg c) (by linarith : (0:ℝ) ≤ x ^ 2 - 2)]

/-- The first bound of **Lemma 4.1**: `f ≤ 2/x` for `x ≥ √2`. -/
lemma ff_le (hχ : χ < c ^ 2) {x : ℝ} (hx : Real.sqrt 2 ≤ x) :
    ff c χ x ≤ 2 / x := by
  have hx1 : 1 < x := one_lt_of_sqrt_two_le hx
  have hx0 : (0:ℝ) < x := by linarith
  have hu := uu_le hx
  have hv := vv_le c χ hχ hx
  have h4 : (2:ℝ) / x ^ 2 + 2 / x ^ 2 = 4 / x ^ 2 := by ring
  have hsum : uu x + vv c χ x ≤ 4 / x ^ 2 := by linarith
  have : x / 2 * (uu x + vv c χ x) ≤ x / 2 * (4 / x ^ 2) :=
    mul_le_mul_of_nonneg_left hsum (by linarith)
  simp only [ff]
  calc x / 2 * (uu x + vv c χ x) ≤ x / 2 * (4 / x ^ 2) := this
    _ = 2 / x := by field_simp; ring

lemma ff_nonneg (hc : 0 < c) (hχ : χ < c ^ 2) {x : ℝ} (hx : 1 < x) : 0 ≤ ff c χ x := by
  have hu := uu_pos hx
  have hv := vv_pos c χ hc hχ hx
  simp only [ff]
  exact mul_nonneg (by linarith) (by linarith)

/-! ### Derivatives -/

/-- `u' = -2x u²`. -/
lemma hasDerivAt_uu {x : ℝ} (hx : 1 < x) :
    HasDerivAt uu (-(2 * x) * (uu x) ^ 2) x := by
  have hx1 : (x ^ 2 - 1 : ℝ) ≠ 0 := by nlinarith
  have h : HasDerivAt (fun y : ℝ => y ^ 2 - 1) (2 * x) x := by
    simpa using (hasDerivAt_pow 2 x).sub_const 1
  have hinv := h.inv hx1
  show HasDerivAt (fun y : ℝ => 1 / (y ^ 2 - 1)) (-(2 * x) * (uu x) ^ 2) x
  simp only [uu, one_div]
  convert hinv using 1
  field_simp

/-- `v' = -2x v²`, from `q' = 2c²x`. -/
lemma hasDerivAt_vv (hχ : χ < c ^ 2) {x : ℝ} (hx : 1 < x) :
    HasDerivAt (vv c χ) (-(2 * x) * (vv c χ x) ^ 2) x := by
  have hq : qq c χ x ≠ 0 := (qq_pos c χ hχ hx.le).ne'
  have h : HasDerivAt (qq c χ) (c ^ 2 * (2 * x)) x := by
    unfold qq
    simpa using ((hasDerivAt_pow 2 x).const_mul (c ^ 2)).sub_const χ
  have hdiv := (hasDerivAt_const x (c ^ 2)).div h hq
  show HasDerivAt (fun y : ℝ => c ^ 2 / qq c χ y) (-(2 * x) * (vv c χ x) ^ 2) x
  simp only [vv]
  convert hdiv using 1
  field_simp
  ring

/-- `f' = ½(u+v) - x²(u²+v²)`, a difference of two non-negative terms. -/
lemma hasDerivAt_ff (hχ : χ < c ^ 2) {x : ℝ} (hx : 1 < x) :
    HasDerivAt (ff c χ)
      (1 / 2 * (uu x + vv c χ x) - x ^ 2 * ((uu x) ^ 2 + (vv c χ x) ^ 2)) x := by
  have hu := hasDerivAt_uu hx
  have hv := hasDerivAt_vv c χ hχ hx
  have hx2 : HasDerivAt (fun y : ℝ => y / 2) (1 / 2) x := by
    simpa using (hasDerivAt_id x).div_const 2
  have h := hx2.mul (hu.add hv)
  show HasDerivAt (fun y : ℝ => y / 2 * (uu y + vv c χ y))
    (1 / 2 * (uu x + vv c χ x) - x ^ 2 * ((uu x) ^ 2 + (vv c χ x) ^ 2)) x
  refine h.congr_deriv ?_
  simp only [Pi.add_apply]
  ring

/-- The second bound of **Lemma 4.1**: `|f'| ≤ 8/x²` for `x ≥ √2`.

The proof is the note's: `f'` is a difference of two non-negative terms, bounded
by `2/x²` and `8/x²` respectively, so the difference is bounded by the larger. -/
lemma abs_deriv_ff_le (hc : 0 < c) (hχ : χ < c ^ 2) {x : ℝ} (hx : Real.sqrt 2 ≤ x) :
    |1 / 2 * (uu x + vv c χ x) - x ^ 2 * ((uu x) ^ 2 + (vv c χ x) ^ 2)| ≤ 8 / x ^ 2 := by
  have hx1 : 1 < x := one_lt_of_sqrt_two_le hx
  have hx0 : (0:ℝ) < x := by linarith
  have hx2 : (0:ℝ) < x ^ 2 := by positivity
  have hu := uu_le hx
  have hv := vv_le c χ hχ hx
  have hup := (uu_pos hx1).le
  have hvp := (vv_pos c χ hc hχ hx1).le
  -- `A := ½(u+v) ∈ [0, 2/x²]`
  have hA0 : (0:ℝ) ≤ 1 / 2 * (uu x + vv c χ x) := by linarith
  have hA : 1 / 2 * (uu x + vv c χ x) ≤ 2 / x ^ 2 := by
    have h4 : (2:ℝ) / x ^ 2 + 2 / x ^ 2 = 4 / x ^ 2 := by ring
    linarith
  -- `B := x²(u²+v²) ∈ [0, 8/x²]`
  have hB0 : (0:ℝ) ≤ x ^ 2 * ((uu x) ^ 2 + (vv c χ x) ^ 2) := by positivity
  have hB : x ^ 2 * ((uu x) ^ 2 + (vv c χ x) ^ 2) ≤ 8 / x ^ 2 := by
    have hu2 : (uu x) ^ 2 ≤ (2 / x ^ 2) ^ 2 := by nlinarith
    have hv2 : (vv c χ x) ^ 2 ≤ (2 / x ^ 2) ^ 2 := by nlinarith
    have hsum : (uu x) ^ 2 + (vv c χ x) ^ 2 ≤ 2 * (2 / x ^ 2) ^ 2 := by linarith
    have hstep : x ^ 2 * ((uu x) ^ 2 + (vv c χ x) ^ 2) ≤ x ^ 2 * (2 * (2 / x ^ 2) ^ 2) :=
      mul_le_mul_of_nonneg_left hsum hx2.le
    have : x ^ 2 * (2 * (2 / x ^ 2) ^ 2) = 8 / x ^ 2 := by field_simp; ring
    linarith
  have h8 : (0:ℝ) < 8 / x ^ 2 := by positivity
  have h28 : (2:ℝ) / x ^ 2 ≤ 8 / x ^ 2 := by
    rw [div_le_div_iff_of_pos_right hx2]; norm_num
  rw [abs_le]
  constructor <;> linarith

/-- `k' = -x(c²-χ)u²/k`.

Note that `0 < c` is *not* needed for the derivative formula itself — only for
the bound `abs_deriv_kk_le` that consumes it, where `k > c` is used. -/
lemma hasDerivAt_kk (hχ : χ < c ^ 2) {x : ℝ} (hx : 1 < x) :
    HasDerivAt (kk c χ)
      (-(2 * x) * (c ^ 2 - χ) * (uu x) ^ 2 / (2 * kk c χ x)) x := by
  have hx1 : (0:ℝ) < x ^ 2 - 1 := by nlinarith
  have hq : (0:ℝ) < qq c χ x := qq_pos c χ hχ hx.le
  have hw : (0:ℝ) < qq c χ x / (x ^ 2 - 1) := by positivity
  -- `w = q/(x²-1)` has `w' = -2x(c²-χ)u²`, by Lemma 3.1's identity
  have hueq : ∀ y : ℝ, 1 < y → qq c χ y / (y ^ 2 - 1) = c ^ 2 + (c ^ 2 - χ) * uu y := by
    intro y hy
    have hy1 : (y ^ 2 - 1 : ℝ) ≠ 0 := by nlinarith
    simp only [uu, qq]; field_simp; ring
  have hw' : HasDerivAt (fun y : ℝ => qq c χ y / (y ^ 2 - 1))
      (-(2 * x) * (c ^ 2 - χ) * (uu x) ^ 2) x := by
    have hcomp : HasDerivAt (fun y : ℝ => c ^ 2 + (c ^ 2 - χ) * uu y)
        ((c ^ 2 - χ) * (-(2 * x) * (uu x) ^ 2)) x :=
      ((hasDerivAt_uu hx).const_mul (c ^ 2 - χ)).const_add (c ^ 2)
    have heq : (fun y : ℝ => qq c χ y / (y ^ 2 - 1))
        =ᶠ[nhds x] (fun y : ℝ => c ^ 2 + (c ^ 2 - χ) * uu y) := by
      filter_upwards [eventually_gt_nhds hx] with y hy using hueq y hy
    exact (hcomp.congr_of_eventuallyEq heq).congr_deriv (by ring)
  have := (Real.hasDerivAt_sqrt hw.ne').comp x hw'
  simp only [kk]
  convert this using 1
  field_simp

/-- The third bound of **Lemma 4.1**: `|k'| ≤ 4c/x³` for `x ≥ √2`.

**This is the only statement in the file that needs `0 ≤ χ`** — it is used to get
`c² - χ ≤ c²`, without which the factor is unbounded.  See
`band-edge-connection.md` §4. -/
lemma abs_deriv_kk_le (hc : 0 < c) (hχ0 : 0 ≤ χ) (hχ : χ < c ^ 2)
    {x : ℝ} (hx : Real.sqrt 2 ≤ x) :
    |-(2 * x) * (c ^ 2 - χ) * (uu x) ^ 2 / (2 * kk c χ x)| ≤ 4 * c / x ^ 3 := by
  have hx1 : 1 < x := one_lt_of_sqrt_two_le hx
  have hx0 : (0:ℝ) < x := by linarith
  have hk : c < kk c χ x := lt_kk c χ hc hχ hx1
  have hk0 : (0:ℝ) < kk c χ x := lt_trans hc hk
  have hu := uu_le hx
  have hup := (uu_pos hx1).le
  have hx2 : (0:ℝ) < x ^ 2 := by positivity
  have hcχ : (0:ℝ) ≤ c ^ 2 - χ := by linarith
  have hu2n : (0:ℝ) ≤ (uu x) ^ 2 := sq_nonneg _
  have hprod : (0:ℝ) ≤ x * (c ^ 2 - χ) * (uu x) ^ 2 :=
    mul_nonneg (mul_nonneg hx0.le hcχ) hu2n
  have hprod' : (0:ℝ) ≤ x * c ^ 2 * (uu x) ^ 2 :=
    mul_nonneg (mul_nonneg hx0.le (sq_nonneg c)) hu2n
  -- `|k'| = x(c²-χ)u²/k`
  have habs : |-(2 * x) * (c ^ 2 - χ) * (uu x) ^ 2 / (2 * kk c χ x)|
      = x * (c ^ 2 - χ) * (uu x) ^ 2 / kk c χ x := by
    rw [abs_div, abs_of_nonneg (by positivity : (0:ℝ) ≤ 2 * kk c χ x)]
    rw [show -(2 * x) * (c ^ 2 - χ) * (uu x) ^ 2
        = -(2 * (x * (c ^ 2 - χ) * (uu x) ^ 2)) by ring]
    rw [abs_neg, abs_of_nonneg (by linarith : (0:ℝ) ≤ 2 * (x * (c ^ 2 - χ) * (uu x) ^ 2))]
    field_simp
  rw [habs]
  -- `x(c²-χ)u²/k ≤ x c² u² / c = c x u² ≤ c x (2/x²)² = 4c/x³`
  have hχu : (0:ℝ) ≤ x * χ * (uu x) ^ 2 :=
    mul_nonneg (mul_nonneg hx0.le hχ0) hu2n
  have hnum : x * (c ^ 2 - χ) * (uu x) ^ 2 ≤ x * c ^ 2 * (uu x) ^ 2 := by nlinarith [hχu]
  have hstep1 : x * (c ^ 2 - χ) * (uu x) ^ 2 / kk c χ x
      ≤ x * c ^ 2 * (uu x) ^ 2 / c := div_le_div₀ hprod' hnum hc hk.le
  have hu2 : (uu x) ^ 2 ≤ (2 / x ^ 2) ^ 2 := by nlinarith
  have hstep2 : x * c ^ 2 * (uu x) ^ 2 / c ≤ 4 * c / x ^ 3 := by
    have hxc : x * c ^ 2 * (uu x) ^ 2 / c = c * x * (uu x) ^ 2 := by field_simp
    rw [hxc]
    have : c * x * (uu x) ^ 2 ≤ c * x * (2 / x ^ 2) ^ 2 :=
      mul_le_mul_of_nonneg_left hu2 (by positivity)
    have heq : c * x * (2 / x ^ 2) ^ 2 = 4 * c / x ^ 3 := by field_simp; ring
    linarith
  linarith

/-! ### The phase-speed bound

The fourth bound of Lemma 4.1 is `θ' ≥ k - f ≥ c - 2/x ≥ c₋`.  The first
inequality is a statement about the Prüfer angle `θ` (see the remark at the end
of this file); the arithmetic content, which is what §4 actually consumes, is the
second and third and is proved here. -/

/-- `k - f ≥ c - 2/x ≥ c - √2` for `x ≥ √2`. -/
lemma phase_speed_lower (hc : 0 < c) (hχ : χ < c ^ 2) {x : ℝ} (hx : Real.sqrt 2 ≤ x) :
    c - 2 / x ≤ kk c χ x - ff c χ x ∧ c - Real.sqrt 2 ≤ c - 2 / x := by
  have hx1 : 1 < x := one_lt_of_sqrt_two_le hx
  have hx0 : (0:ℝ) < x := by linarith
  have hk := lt_kk c χ hc hχ hx1
  have hf := ff_le c χ hχ hx
  refine ⟨by linarith, ?_⟩
  -- `2/x ≤ 2/√2 = √2`
  have hs2 : (0:ℝ) < Real.sqrt 2 := Real.sqrt_pos.mpr (by norm_num)
  have h : 2 / x ≤ 2 / Real.sqrt 2 := by
    apply div_le_div_of_nonneg_left (by norm_num) hs2 hx
  have heq : 2 / Real.sqrt 2 = Real.sqrt 2 := by
    rw [eq_comm, eq_div_iff hs2.ne']
    rw [← Real.sqrt_mul_self (by norm_num : (0:ℝ) ≤ 2)]
    norm_num [Real.mul_self_sqrt]
  linarith [heq ▸ h]

/-- `c₋ := c - √2 > 0` when `c > √2`. -/
lemma c_neg_pos {c : ℝ} (hc : Real.sqrt 2 < c) : 0 < c - Real.sqrt 2 := by linarith

/-! ### Lemma 4.1 restated in terms of `deriv`

`abs_deriv_ff_le` and `abs_deriv_kk_le` are stated about the explicit derivative
expressions, which is what the `HasDerivAt` lemmas produce.  These corollaries
restate them about `deriv`, so that the bounds read exactly as Lemma 4.1 does. -/

/-- **Lemma 4.1**, second bound: `|f'| ≤ 8/x²`. -/
lemma abs_deriv_ff_le' (hc : 0 < c) (hχ : χ < c ^ 2) {x : ℝ} (hx : Real.sqrt 2 ≤ x) :
    |deriv (ff c χ) x| ≤ 8 / x ^ 2 := by
  rw [(hasDerivAt_ff c χ hχ (one_lt_of_sqrt_two_le hx)).deriv]
  exact abs_deriv_ff_le c χ hc hχ hx

/-- **Lemma 4.1**, third bound: `|k'| ≤ 4c/x³`.  Needs `0 ≤ χ`. -/
lemma abs_deriv_kk_le' (hc : 0 < c) (hχ0 : 0 ≤ χ) (hχ : χ < c ^ 2)
    {x : ℝ} (hx : Real.sqrt 2 ≤ x) :
    |deriv (kk c χ) x| ≤ 4 * c / x ^ 3 := by
  rw [(hasDerivAt_kk c χ hχ (one_lt_of_sqrt_two_le hx)).deriv]
  exact abs_deriv_kk_le c χ hc hχ0 hχ hx

end Riemann.Prolate
