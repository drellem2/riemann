/-
# Lemma 5.1 — the Sturm amplitude is non-increasing

Formalisation of Lemma 5.1 of `notes/h1-mean-value.md` §5, quoted as Lemma 5.1 in
`notes/band-edge-connection.md` §1, where it is the single most load-bearing
elementary step under Q1 (Theorem 5.2).

The informal statement:

> Let `Φ` satisfy the prolate equation `((1-x²)Φ')' + (χ - c²x²)Φ = 0` and suppose
> `χ < c²`.  Then `|Φ x| ≤ |Φ 1|` for all `x ≥ 1`.

The proof puts `p := (x²-1)Φ'`, `q := c²x² - χ`, `D := (x²-1)q`, and shows that
`V := p²/D + Φ²` has `V' = -p²D'/D² ≤ 0` with `V 1⁺ = (Φ 1)²`.

## What this file does and does not assume

Nothing here knows that `Φ` is a prolate function.  Following
`band-edge-connection.md` §0, the only facts used are that `Φ` solves the ODE and
is real; the eigenvalue condition that singles out `Φ n` is never used.  We work
throughout with the first-order system of `band-edge-connection.md` (2.1),

    Φ' = p/(x²-1),    p' = -q Φ,

taking `p` as a primitive object rather than deriving it.  On `(1,∞)` this is
equivalent to the second-order equation, and it avoids having to assert that
`(x²-1)Φ'` is differentiable — which on the informal side is a consequence of the
equation itself.

## Hypotheses, as formalising sharpened them

Two things the informal proof leaves implicit had to be made explicit; both are
recorded in `notes/band-edge-connection.md` §12 (appended by this work).

* **`χ < c²` suffices for Lemma 5.1; `0 ≤ χ` is not needed.**  This is what the
  note says, and it survives formalisation.  (`0 ≤ χ` *is* needed further up, at
  Lemma 4.1's bound on `|k'|` — see `Riemann/BandEdge.lean`.)
* **`Φ` analytic at `x = 1` is used only through two consequences**, and only
  those two are assumed here: `Φ` is continuous at `1` from the right, and `Φ'`
  is bounded near `1⁺`.  The note itself says as much ("boundedness near `x=1`
  would do"); making it a hypothesis is what lets the limit `V 1⁺ = (Φ 1)²` be
  proved rather than gestured at.

## Mathlib

Built against mathlib `5e932f97dd25535344f80f9dd8da3aab83df0fe6` (tag
`v4.29.1`), Lean toolchain `leanprover/lean4:v4.29.1`.
-/
import Mathlib

namespace Riemann.Prolate

open Set Filter Topology

variable (c χ : ℝ)

/-! ## The coefficients `q`, `D`, `D'` -/

/-- `q x = c²x² - χ`, the coefficient of `Φ` in the equation `p' = -qΦ`. -/
noncomputable def qq (x : ℝ) : ℝ := c ^ 2 * x ^ 2 - χ

/-- `D x = (x²-1) · q x`. -/
noncomputable def DD (x : ℝ) : ℝ := (x ^ 2 - 1) * qq c χ x

/-- `D' x = 2x(2c²x² - χ - c²)`, the derivative of `D`; see `hasDerivAt_DD`.
This is (1.1) of `band-edge-connection.md`. -/
noncomputable def DD' (x : ℝ) : ℝ := 2 * x * (2 * c ^ 2 * x ^ 2 - χ - c ^ 2)

lemma qq_pos (hχ : χ < c ^ 2) {x : ℝ} (hx : 1 ≤ x) : 0 < qq c χ x := by
  have h : (0:ℝ) ≤ c ^ 2 * (x ^ 2 - 1) :=
    mul_nonneg (sq_nonneg c) (by nlinarith)
  simp only [qq]; nlinarith

lemma DD_pos (hχ : χ < c ^ 2) {x : ℝ} (hx : 1 < x) : 0 < DD c χ x :=
  mul_pos (by nlinarith) (qq_pos c χ hχ hx.le)

/-- (1.1) of `band-edge-connection.md`: `D' > 0` on `[1,∞)`, because the bracket
is `≥ c² - χ > 0`.  Note that `0 ≤ χ` is *not* required. -/
lemma DD'_pos (hχ : χ < c ^ 2) {x : ℝ} (hx : 1 ≤ x) : 0 < DD' c χ x := by
  have h : (0:ℝ) ≤ c ^ 2 * (x ^ 2 - 1) := mul_nonneg (sq_nonneg c) (by nlinarith)
  have h2 : (0:ℝ) < 2 * c ^ 2 * x ^ 2 - χ - c ^ 2 := by nlinarith
  simp only [DD']
  exact mul_pos (by linarith) h2

lemma hasDerivAt_DD (x : ℝ) : HasDerivAt (DD c χ) (DD' c χ x) x := by
  have h : HasDerivAt (fun y : ℝ => (y ^ 2 - 1) * (c ^ 2 * y ^ 2 - χ))
      ((2 * x) * (c ^ 2 * x ^ 2 - χ) + (x ^ 2 - 1) * (c ^ 2 * (2 * x))) x := by
    have h1 : HasDerivAt (fun y : ℝ => y ^ 2 - 1) (2 * x) x := by
      simpa using (hasDerivAt_pow 2 x).sub_const 1
    have h2 : HasDerivAt (fun y : ℝ => c ^ 2 * y ^ 2 - χ) (c ^ 2 * (2 * x)) x := by
      simpa using ((hasDerivAt_pow 2 x).const_mul (c ^ 2)).sub_const χ
    exact h1.mul h2
  unfold DD qq DD'
  convert h using 1
  ring

/-! ## The system, and the Sturm functional `V` -/

/-- The prolate equation `((1-x²)Φ')' + (χ - c²x²)Φ = 0` on `(1,∞)`, written as the
first-order system (2.1) of `band-edge-connection.md` with `p = (x²-1)Φ'`. -/
structure IsSolution (c χ : ℝ) (Φ p : ℝ → ℝ) : Prop where
  hΦ : ∀ x ∈ Ioi (1:ℝ), HasDerivAt Φ (p x / (x ^ 2 - 1)) x
  hp : ∀ x ∈ Ioi (1:ℝ), HasDerivAt p (-(qq c χ x) * Φ x) x

/-- **Faithfulness check.**  `IsSolution` really is the prolate equation and not
something else: if `Φ` has derivative `dΦ` on `(1,∞)` and `(1-x²)dΦ` has
derivative `-(χ - c²x²)Φ` there — which is
`((1-x²)Φ')' + (χ - c²x²)Φ = 0` — then `(Φ, (x²-1)dΦ)` is an `IsSolution`.

This is the one statement in the file whose failure would make every other
statement vacuous, so it is worth having.  The sign is the thing to watch:
`p = (x²-1)Φ' = -(1-x²)Φ'`, so `p' = +(χ - c²x²)Φ = -qΦ`. -/
lemma isSolution_of_secondOrder {Φ dΦ : ℝ → ℝ}
    (hd : ∀ x ∈ Ioi (1:ℝ), HasDerivAt Φ (dΦ x) x)
    (hode : ∀ x ∈ Ioi (1:ℝ),
      HasDerivAt (fun y => (1 - y ^ 2) * dΦ y) (-(χ - c ^ 2 * x ^ 2) * Φ x) x) :
    IsSolution c χ Φ (fun y => (y ^ 2 - 1) * dΦ y) := by
  constructor
  · intro x hx
    have hx' : (1:ℝ) < x := hx
    have hx1 : (x ^ 2 - 1 : ℝ) ≠ 0 := by nlinarith
    refine (hd x hx).congr_deriv ?_
    field_simp
  · intro x hx
    have h := (hode x hx).neg
    have heq : (fun y : ℝ => (y ^ 2 - 1) * dΦ y)
        =ᶠ[nhds x] (fun y : ℝ => -((1 - y ^ 2) * dΦ y)) :=
      Filter.Eventually.of_forall (fun y => by ring)
    exact (h.congr_of_eventuallyEq heq).congr_deriv (by simp only [qq]; ring)

/-- `V = p²/D + Φ²`, the Sturm functional of `h1-mean-value.md` §5. -/
noncomputable def V (Φ p : ℝ → ℝ) (x : ℝ) : ℝ := (p x) ^ 2 / DD c χ x + (Φ x) ^ 2

/-- The computation at the heart of Lemma 5.1: the first and third terms of `V'`
cancel identically because `D = (x²-1)q`, leaving `V' = -p²D'/D²`. -/
lemma hasDerivAt_V (hχ : χ < c ^ 2) {Φ p : ℝ → ℝ} (hs : IsSolution c χ Φ p)
    {x : ℝ} (hx : 1 < x) :
    HasDerivAt (V c χ Φ p) (-(p x) ^ 2 * DD' c χ x / (DD c χ x) ^ 2) x := by
  have hq : qq c χ x ≠ 0 := (qq_pos c χ hχ hx.le).ne'
  have hx1 : (x ^ 2 - 1 : ℝ) ≠ 0 := by nlinarith
  have hD : DD c χ x ≠ 0 := (DD_pos c χ hχ hx).ne'
  have hpd : HasDerivAt p (-(qq c χ x) * Φ x) x := hs.hp x hx
  have hΦd : HasDerivAt Φ (p x / (x ^ 2 - 1)) x := hs.hΦ x hx
  have hnum : HasDerivAt (fun y => (p y) ^ 2)
      (2 * p x * (-(qq c χ x) * Φ x)) x := by
    simpa using hpd.pow 2
  have hquot : HasDerivAt (fun y => (p y) ^ 2 / DD c χ y)
      ((2 * p x * (-(qq c χ x) * Φ x) * DD c χ x - (p x) ^ 2 * DD' c χ x)
        / (DD c χ x) ^ 2) x :=
    hnum.div (hasDerivAt_DD c χ x) hD
  have hsq : HasDerivAt (fun y => (Φ y) ^ 2) (2 * Φ x * (p x / (x ^ 2 - 1))) x := by
    simpa using hΦd.pow 2
  have := hquot.add hsq
  refine this.congr_deriv ?_
  simp only [DD, qq, DD'] at *
  field_simp
  ring

/-- `V` is non-increasing on `(1,∞)`. -/
lemma antitoneOn_V (hχ : χ < c ^ 2) {Φ p : ℝ → ℝ} (hs : IsSolution c χ Φ p) :
    AntitoneOn (V c χ Φ p) (Ioi 1) := by
  have hderiv : ∀ x ∈ Ioi (1:ℝ),
      HasDerivAt (V c χ Φ p) (-(p x) ^ 2 * DD' c χ x / (DD c χ x) ^ 2) x :=
    fun x hx => hasDerivAt_V c χ hχ hs hx
  refine antitoneOn_of_deriv_nonpos (convex_Ioi 1) ?_ ?_ ?_
  · exact fun x hx => (hderiv x hx).continuousAt.continuousWithinAt
  · rw [interior_Ioi]
    exact fun x hx => ((hderiv x hx).differentiableAt).differentiableWithinAt
  · rw [interior_Ioi]
    intro x hx
    rw [(hderiv x hx).deriv]
    have h1 : (0:ℝ) ≤ (p x) ^ 2 * DD' c χ x :=
      mul_nonneg (sq_nonneg _) (DD'_pos c χ hχ (le_of_lt hx)).le
    have h2 : (0:ℝ) < (DD c χ x) ^ 2 := pow_pos (DD_pos c χ hχ hx) 2
    rw [div_nonpos_iff]
    right
    exact ⟨by linarith, h2.le⟩

lemma sq_le_V (hχ : χ < c ^ 2) {Φ p : ℝ → ℝ} {x : ℝ} (hx : 1 < x) :
    (Φ x) ^ 2 ≤ V c χ Φ p x := by
  have : (0:ℝ) ≤ (p x) ^ 2 / DD c χ x :=
    div_nonneg (sq_nonneg _) (DD_pos c χ hχ hx).le
  simp only [V]; linarith

/-! ## The boundary value `V 1⁺ = (Φ 1)²`

This is where analyticity of `Φ` at `x = 1` is used in the informal proof.  We
assume only its two consequences: right-continuity of `Φ` at `1`, and boundedness
of `Φ' = p/(x²-1)` near `1⁺`. -/

/-- `p²/D → 0` as `x → 1⁺`.  Writing `p = (x²-1)Φ'`, we have
`p²/D = (x²-1)(Φ')²/q`, which is `O(x²-1)`. -/
lemma tendsto_ratio (hχ : χ < c ^ 2) {p : ℝ → ℝ} {M : ℝ}
    (hM : ∀ᶠ x in 𝓝[>] (1:ℝ), |p x / (x ^ 2 - 1)| ≤ M) :
    Tendsto (fun x => (p x) ^ 2 / DD c χ x) (𝓝[>] (1:ℝ)) (𝓝 0) := by
  have hq1 : qq c χ 1 ≠ 0 := (qq_pos c χ hχ le_rfl).ne'
  -- the majorant `g x = (x²-1)M²/q x` is continuous at `1` with value `0`
  have hqcont : ContinuousAt (fun y : ℝ => qq c χ y) 1 := by
    unfold qq; fun_prop
  have hgc : ContinuousAt (fun y : ℝ => (y ^ 2 - 1) * M ^ 2 / qq c χ y) 1 :=
    ContinuousAt.div (by fun_prop) hqcont hq1
  have hg : Tendsto (fun y : ℝ => (y ^ 2 - 1) * M ^ 2 / qq c χ y) (𝓝[>] (1:ℝ)) (𝓝 0) := by
    have h : Tendsto (fun y : ℝ => (y ^ 2 - 1) * M ^ 2 / qq c χ y) (𝓝[>] (1:ℝ))
        (𝓝 (((1:ℝ) ^ 2 - 1) * M ^ 2 / qq c χ 1)) := hgc.continuousWithinAt
    have hz : ((1:ℝ) ^ 2 - 1) * M ^ 2 / qq c χ 1 = 0 := by norm_num
    rwa [hz] at h
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hg ?_ ?_
  · filter_upwards [self_mem_nhdsWithin] with x hx
    exact div_nonneg (sq_nonneg _) (DD_pos c χ hχ hx).le
  · filter_upwards [hM, self_mem_nhdsWithin] with x hxM hx
    have hx1 : (0:ℝ) < x ^ 2 - 1 := by simp only [mem_Ioi] at hx; nlinarith
    have hqx : (0:ℝ) < qq c χ x := qq_pos c χ hχ (le_of_lt hx)
    have hkey : (p x) ^ 2 / DD c χ x = (x ^ 2 - 1) * (p x / (x ^ 2 - 1)) ^ 2 / qq c χ x := by
      simp only [DD]
      field_simp
    rw [hkey]
    have h1 := (abs_le.mp hxM).1
    have h2 := (abs_le.mp hxM).2
    have hsq : (p x / (x ^ 2 - 1)) ^ 2 ≤ M ^ 2 := by nlinarith
    exact div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_left hsq hx1.le) hqx.le

/-- `V 1⁺ = (Φ 1)²`. -/
lemma tendsto_V (hχ : χ < c ^ 2) {Φ p : ℝ → ℝ} {M : ℝ}
    (hcont : ContinuousWithinAt Φ (Ioi 1) 1)
    (hM : ∀ᶠ x in 𝓝[>] (1:ℝ), |p x / (x ^ 2 - 1)| ≤ M) :
    Tendsto (V c χ Φ p) (𝓝[>] (1:ℝ)) (𝓝 ((Φ 1) ^ 2)) := by
  have h1 := tendsto_ratio c χ hχ hM
  have h2 : Tendsto (fun x => (Φ x) ^ 2) (𝓝[>] (1:ℝ)) (𝓝 ((Φ 1) ^ 2)) :=
    (hcont.tendsto).pow 2
  simpa using h1.add h2

/-! ## Lemma 5.1 -/

/-- **Lemma 5.1** (`h1-mean-value.md` §5).  If `χ < c²` then `|Φ x| ≤ |Φ 1|` for
all `x ≥ 1`.

`hcont` and `hM` are the two consequences of analyticity of `Φ` at `x = 1` that
the informal proof actually uses. -/
theorem abs_le_abs_one (hχ : χ < c ^ 2) {Φ p : ℝ → ℝ} (hs : IsSolution c χ Φ p)
    {M : ℝ} (hcont : ContinuousWithinAt Φ (Ioi 1) 1)
    (hM : ∀ᶠ x in 𝓝[>] (1:ℝ), |p x / (x ^ 2 - 1)| ≤ M)
    {x : ℝ} (hx : 1 ≤ x) : |Φ x| ≤ |Φ 1| := by
  rcases eq_or_lt_of_le hx with rfl | hx'
  · exact le_rfl
  have hVle : V c χ Φ p x ≤ (Φ 1) ^ 2 := by
    refine ge_of_tendsto (tendsto_V c χ hχ hcont hM) ?_
    filter_upwards [Ioo_mem_nhdsGT_of_mem ⟨le_rfl, hx'⟩] with y hy
    exact antitoneOn_V c χ hχ hs (mem_Ioi.mpr hy.1) (mem_Ioi.mpr hx') hy.2.le
  have hsq : (Φ x) ^ 2 ≤ (Φ 1) ^ 2 := le_trans (sq_le_V c χ hχ hx') hVle
  have := Real.sqrt_le_sqrt hsq
  rwa [Real.sqrt_sq_eq_abs, Real.sqrt_sq_eq_abs] at this

/-- The form the amplitude bound is quoted in at `band-edge-connection.md` §5:
`ρ(√2)² = V(√2) ≤ (Φ 1)²`. -/
theorem V_le_sq_one (hχ : χ < c ^ 2) {Φ p : ℝ → ℝ} (hs : IsSolution c χ Φ p)
    {M : ℝ} (hcont : ContinuousWithinAt Φ (Ioi 1) 1)
    (hM : ∀ᶠ x in 𝓝[>] (1:ℝ), |p x / (x ^ 2 - 1)| ≤ M)
    {x : ℝ} (hx : 1 < x) : V c χ Φ p x ≤ (Φ 1) ^ 2 := by
  refine ge_of_tendsto (tendsto_V c χ hχ hcont hM) ?_
  filter_upwards [Ioo_mem_nhdsGT_of_mem ⟨le_rfl, hx⟩] with y hy
  exact antitoneOn_V c χ hχ hs (mem_Ioi.mpr hy.1) (mem_Ioi.mpr hx) hy.2.le

end Riemann.Prolate
