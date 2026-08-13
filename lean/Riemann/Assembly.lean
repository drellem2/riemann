/-
# The assembly: the four legs give `limsup μ⁻¹ log s(μ) ≤ -4π`

Formalisation of Corollary `cor:upper` and the `limsup` half of Theorem `thm:main`
of `paper/positivity-obstruction.tex`, i.e. of the step that turns the four
load-bearing legs of §7 into the paper's headline conclusion.

The legs themselves are *not* formalised here — they are named as hypotheses.
That is the point of the file: it checks the paper's **logical skeleton**,
independently of whether the legs are prose or machine-checked.  Nothing here
knows what a prolate function, a zeta zero or a Weil form is; the whole content
is that the following six statements about real-valued functions of `μ` imply the
bound, and that the arithmetic of the exponents works out.

    (R)  s μ * G μ ≤ Q μ        the Rayleigh quotient at the test vector g,
                               `G = ‖g‖²`, `Q = QW_λ(g,g)`, `s = λ_min(σ⁺)`
    (I)  Q μ = Zsum μ           Proposition `prop:identity`
    (3)  Zsum μ ≤ Ξ μ * N μ     Theorem `thm:q3`, with `N = 1 - χ₂`
    (0)  `Subexp G`             Theorem `thm:h0`, *in the only form the corollary
                               consumes* — see the note below
    (Ξ)  `Subexp Ξ`             Theorem `thm:q3`'s polynomial bound
    (N)  `μ⁻¹ log (N μ) → -4π`  the Fuchs rate, paper §6.2 (1.2)

## What the corollary consumes of (H0), and why it is worth saying

The paper's remark at `cor:upper` — "only `μ⁻¹ log ‖g‖² → 0`, so *any*
`‖g‖² ≥ e^{-o(μ)}` gives the same `-4π`" — is visible here as the hypothesis
being `Subexp G` and not `∃ δ > 0, ∀ μ, δ ≤ G μ`.  Formalising makes that
distinction structural rather than a remark: `limsup_le_neg_four_pi` cannot be
stated with the stronger hypothesis without weakening the theorem, because the
stronger hypothesis is never unfolded.  `Subexp.of_tendsto_pos` below is the
bridge from what `thm:h0` actually proves (`‖g‖² → 0.219…`) to what is used.

## Sign-blindness (the house rule)

Every statement in this file is **sign-blind**, and vacuously so: `s`, `Q`, `G`,
`Ξ`, `N` are arbitrary real-valued functions, and the file is invariant under any
relabelling of them.  In particular nothing here is false for
`W_λ ↦ -W_λ`: the hypothesis `(R)` is an upper bound on `s μ * G μ`, and an upper
bound on `λ_min` is what the theorem consumes.  No statement here has a
lower-bound conclusion of any kind, so there is nothing for a sign to break.
See `notes/s3-sign-blindness.md` and paper §7.7.

## Mathlib

Built against mathlib `5e932f97dd25535344f80f9dd8da3aab83df0fe6` (tag
`v4.29.1`), Lean toolchain `leanprover/lean4:v4.29.1`.
-/
import Mathlib

namespace Riemann.Assembly

open Filter Topology
open scoped Real

/-! ## Subexponential factors

The paper's word for a factor that the `limsup` does not see.  Note this is a
statement about `μ⁻¹ log`, so it is two-sided: it excludes `e^{εμ}` growth *and*
`e^{-εμ}` decay.  That is what makes it the right hypothesis on `Ξ` (which grows
polynomially) and on `G = ‖g‖²` (which converges to a positive constant). -/

/-- `A` is **subexponential**: `μ⁻¹ log (A μ) → 0` as `μ → ∞`. -/
def Subexp (A : ℝ → ℝ) : Prop :=
  Tendsto (fun μ => Real.log (A μ) / μ) atTop (𝓝 0)

/-- `μ⁻¹ log μ → 0`, the only analytic input any of the `Subexp` lemmas needs. -/
lemma tendsto_log_div_atTop : Tendsto (fun μ : ℝ => Real.log μ / μ) atTop (𝓝 0) :=
  Real.isLittleO_log_id_atTop.tendsto_div_nhds_zero

/-- A function with a positive limit is subexponential. -/
lemma Subexp.of_tendsto_pos {A : ℝ → ℝ} {a : ℝ} (ha : 0 < a)
    (h : Tendsto A atTop (𝓝 a)) : Subexp A := by
  have hlog : Tendsto (fun μ => Real.log (A μ)) atTop (𝓝 (Real.log a)) :=
    (Real.continuousAt_log ha.ne').tendsto.comp h
  have hinv : Tendsto (fun μ : ℝ => μ⁻¹) atTop (𝓝 0) := tendsto_inv_atTop_zero
  have := hlog.mul hinv
  simpa [div_eq_mul_inv] using this

/-- A positive constant is subexponential. -/
lemma Subexp.const {C : ℝ} (hC : 0 < C) : Subexp (fun _ => C) :=
  Subexp.of_tendsto_pos hC tendsto_const_nhds

/-- **The sandwich.**  Anything eventually between a positive constant and a
polynomial is subexponential.  This is the workhorse: it covers
`Ξ μ = C μ⁶ log³μ` and the prefactor `C μ^{9/2}` of the Fuchs rate without any
explicit log arithmetic. -/
lemma Subexp.of_sandwich {A : ℝ → ℝ} {c C : ℝ} {k : ℕ} (hc : 0 < c) (hC : 0 < C)
    (h1 : ∀ᶠ μ in atTop, c ≤ A μ)
    (h2 : ∀ᶠ μ in atTop, A μ ≤ C * μ ^ k) : Subexp A := by
  have hmin : Tendsto (fun μ : ℝ => Real.log c / μ) atTop (𝓝 0) := by
    have h : Tendsto (fun μ : ℝ => Real.log c * μ⁻¹) atTop (𝓝 (Real.log c * 0)) :=
      tendsto_const_nhds.mul tendsto_inv_atTop_zero
    simp only [mul_zero] at h
    exact h.congr fun μ => (div_eq_mul_inv _ _).symm
  have hmaj : Tendsto (fun μ : ℝ => (Real.log C + k * Real.log μ) / μ) atTop (𝓝 0) := by
    have h : Tendsto
        (fun μ : ℝ => Real.log C * μ⁻¹ + k * (Real.log μ / μ)) atTop (𝓝 (Real.log C * 0 + k * 0)) :=
      (tendsto_const_nhds.mul tendsto_inv_atTop_zero).add
        (tendsto_const_nhds.mul tendsto_log_div_atTop)
    simp only [mul_zero, add_zero] at h
    refine h.congr fun μ => ?_
    field_simp
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hmin hmaj ?_ ?_
  · filter_upwards [h1, eventually_gt_atTop (0:ℝ)] with μ hA hμ
    have hpos : (0:ℝ) < A μ := lt_of_lt_of_le hc hA
    gcongr
  · filter_upwards [h1, h2, eventually_gt_atTop (1:ℝ)] with μ hA hA2 hμ
    have hμ0 : (0:ℝ) < μ := lt_trans zero_lt_one hμ
    have hpos : (0:ℝ) < A μ := lt_of_lt_of_le hc hA
    have hlog : Real.log (A μ) ≤ Real.log C + k * Real.log μ := by
      have := Real.log_le_log hpos hA2
      rwa [Real.log_mul hC.ne' (by positivity), Real.log_pow] at this
    gcongr

/-- `Subexp` is closed under quotients, which is how `Ξ / ‖g‖²` enters. -/
lemma Subexp.div {A B : ℝ → ℝ} (hA : Subexp A) (hB : Subexp B)
    (hA0 : ∀ᶠ μ in atTop, A μ ≠ 0) (hB0 : ∀ᶠ μ in atTop, B μ ≠ 0) :
    Subexp (fun μ => A μ / B μ) := by
  have h := hA.sub hB
  rw [sub_zero] at h
  refine h.congr' ?_
  filter_upwards [hA0, hB0] with μ h1 h2
  rw [Real.log_div h1 h2, sub_div]

/-! ## The exponential rate of a product `P μ · e^{-Lμ}`

This is the shape the Fuchs asymptotic `1 - χ₂ ∼ C μ^{9/2} e^{-4πμ}` has, and it
is where the `-4π` comes from. -/

/-- If `P` is subexponential and positive then `μ ↦ P μ * e^{-Lμ}` has rate exactly `-L`. -/
lemma tendsto_logRate_mul_exp {P : ℝ → ℝ} {L : ℝ} (hP : Subexp P)
    (hP0 : ∀ᶠ μ in atTop, P μ ≠ 0) :
    Tendsto (fun μ => Real.log (P μ * Real.exp (-L * μ)) / μ) atTop (𝓝 (-L)) := by
  have h : Tendsto (fun μ : ℝ => Real.log (P μ) / μ + -L) atTop (𝓝 (0 + -L)) :=
    hP.add tendsto_const_nhds
  rw [zero_add] at h
  refine h.congr' ?_
  filter_upwards [hP0, eventually_gt_atTop (0:ℝ)] with μ h1 hμ
  rw [Real.log_mul h1 (Real.exp_ne_zero _), Real.log_exp, add_div]
  congr 1
  field_simp

/-! ## The engine -/

/-- The pointwise half of the engine: `μ⁻¹ log s` is eventually below
`μ⁻¹ log A + μ⁻¹ log B`, whose limit is `L`. -/
lemma logRate_le_aux {s A B : ℝ → ℝ} {L : ℝ}
    (hspos : ∀ᶠ μ in atTop, 0 < s μ)
    (hApos : ∀ᶠ μ in atTop, 0 < A μ)
    (hBpos : ∀ᶠ μ in atTop, 0 < B μ)
    (hle : ∀ᶠ μ in atTop, s μ ≤ A μ * B μ)
    (hA : Subexp A)
    (hB : Tendsto (fun μ => Real.log (B μ) / μ) atTop (𝓝 L)) :
    (fun μ => Real.log (s μ) / μ) ≤ᶠ[atTop]
      (fun μ => Real.log (A μ) / μ + Real.log (B μ) / μ) ∧
    Tendsto (fun μ => Real.log (A μ) / μ + Real.log (B μ) / μ) atTop (𝓝 L) := by
  refine ⟨?_, ?_⟩
  · filter_upwards [hspos, hApos, hBpos, hle, eventually_gt_atTop (0:ℝ)]
      with μ h1 h2 h3 h4 hμ
    have hlog : Real.log (s μ) ≤ Real.log (A μ) + Real.log (B μ) := by
      rw [← Real.log_mul h2.ne' h3.ne']
      exact Real.log_le_log h1 h4
    rw [← add_div]
    gcongr
  · have := hA.add hB
    rwa [zero_add] at this

/-- **The engine of `cor:upper`**, in the form that carries no side condition.
If `0 < s μ ≤ A μ * B μ` eventually, `A` is subexponential and `B` has
exponential rate `L`, then for every `ε > 0` we eventually have
`s μ ≤ e^{(L+ε)μ}`.

This is the whole of the paper's `limsup` step, with the two factors named: `A`
collects everything the `limsup` cannot see (`Ξ`, and `1/‖g‖²`), and `B` is the
one factor that carries the rate (`1 - χ₂`).

This `ε`-form is the *primary* statement, and it is strictly stronger than the
`limsup` form below — see the note on `limsup_logRate_le`. -/
theorem eventually_log_le {s A B : ℝ → ℝ} {L : ℝ}
    (hspos : ∀ᶠ μ in atTop, 0 < s μ)
    (hApos : ∀ᶠ μ in atTop, 0 < A μ)
    (hBpos : ∀ᶠ μ in atTop, 0 < B μ)
    (hle : ∀ᶠ μ in atTop, s μ ≤ A μ * B μ)
    (hA : Subexp A)
    (hB : Tendsto (fun μ => Real.log (B μ) / μ) atTop (𝓝 L))
    {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ μ in atTop, Real.log (s μ) ≤ (L + ε) * μ := by
  obtain ⟨key, hvlim⟩ := logRate_le_aux hspos hApos hBpos hle hA hB
  have hv : ∀ᶠ μ in atTop, Real.log (A μ) / μ + Real.log (B μ) / μ ≤ L + ε := by
    have := hvlim.eventually (eventually_lt_nhds (by linarith : L < L + ε))
    exact this.mono fun _ h => h.le
  filter_upwards [key, hv, eventually_gt_atTop (0:ℝ)] with μ h1 h2 hμ
  have : Real.log (s μ) / μ ≤ L + ε := le_trans h1 h2
  calc Real.log (s μ) = Real.log (s μ) / μ * μ := by field_simp
    _ ≤ (L + ε) * μ := by gcongr

/-- **The engine of `cor:upper`**, in the paper's `limsup` form.

The extra hypothesis `hbelow` — that `μ⁻¹ log s(μ)` is eventually bounded below —
is *not* an artefact of the proof, and it is a small thing that formalising
surfaced.  `Filter.limsup` here takes values in `ℝ`, where `limsup u` is
`sInf {a | ∀ᶠ μ, u μ ≤ a}`; if `μ⁻¹ log s(μ) → -∞` that set is all of `ℝ` and
Lean's junk convention returns `0`, so the conclusion `limsup ≤ L` would be
*false* in that degenerate case.  Read in `[-∞,∞]`, as a mathematician reads it,
no side condition is needed.  `eventually_log_le` above is the statement that
carries the content and needs nothing; this one is here because it is the shape
the paper writes down.

`hbelow` is harmless in the application: it says only that `s(μ)` does not decay
superexponentially, and `s(μ) > 0` with `s(μ) ≈ e^{-4πμ}` measured (paper §8.2). -/
theorem limsup_logRate_le {s A B : ℝ → ℝ} {L : ℝ}
    (hspos : ∀ᶠ μ in atTop, 0 < s μ)
    (hApos : ∀ᶠ μ in atTop, 0 < A μ)
    (hBpos : ∀ᶠ μ in atTop, 0 < B μ)
    (hle : ∀ᶠ μ in atTop, s μ ≤ A μ * B μ)
    (hA : Subexp A)
    (hB : Tendsto (fun μ => Real.log (B μ) / μ) atTop (𝓝 L))
    (hbelow : ∃ b : ℝ, ∀ᶠ μ in atTop, b ≤ Real.log (s μ) / μ) :
    limsup (fun μ => Real.log (s μ) / μ) atTop ≤ L := by
  obtain ⟨key, hvlim⟩ := logRate_le_aux hspos hApos hBpos hle hA hB
  obtain ⟨b, hb⟩ := hbelow
  have hvle : ∀ᶠ μ in atTop, Real.log (A μ) / μ + Real.log (B μ) / μ ≤ L + 1 := by
    have := hvlim.eventually (eventually_lt_nhds (by linarith : L < L + 1))
    exact this.mono fun _ h => h.le
  have hcob : IsCoboundedUnder (· ≤ ·) atTop (fun μ => Real.log (s μ) / μ) :=
    isCoboundedUnder_le_of_eventually_le atTop hb
  have hbdd : IsBoundedUnder (· ≤ ·) atTop
      (fun μ => Real.log (A μ) / μ + Real.log (B μ) / μ) := ⟨L + 1, hvle⟩
  calc limsup (fun μ => Real.log (s μ) / μ) atTop
      ≤ limsup (fun μ => Real.log (A μ) / μ + Real.log (B μ) / μ) atTop :=
        limsup_le_limsup key hcob hbdd
    _ = L := hvlim.limsup_eq

/-! ## Corollary `cor:upper` -/

/-- **Corollary `cor:upper`** (paper §6.6), with the four legs as hypotheses.

`s` is `λ_min(σ⁺)`, `G` is `‖g‖²`, `Q` is `QW_λ(g,g)`, `Zsum` is
`∑_ρ |F_μ r(s_ρ)|²`, `Ξ` is the truncation constant of `thm:q3` and `N` is
`1 - χ₂(λ)`.

The hypotheses are, in the paper's order of dependence: the Rayleigh bound at the
test vector (`hRayleigh`), Proposition `prop:identity` (`hidentity`), Theorem
`thm:q3` (`hQ3`), `thm:h0` in the form the corollary consumes (`hG`), `thm:q3`'s
polynomial bound (`hΞ`), and the Fuchs rate (`hN`). -/
theorem eventually_log_le_neg_four_pi {s G Q Zsum Ξ N : ℝ → ℝ}
    (hspos : ∀ᶠ μ in atTop, 0 < s μ)
    (hGpos : ∀ᶠ μ in atTop, 0 < G μ)
    (hΞpos : ∀ᶠ μ in atTop, 0 < Ξ μ)
    (hNpos : ∀ᶠ μ in atTop, 0 < N μ)
    (hRayleigh : ∀ᶠ μ in atTop, s μ * G μ ≤ Q μ)
    (hidentity : ∀ᶠ μ in atTop, Q μ = Zsum μ)
    (hQ3 : ∀ᶠ μ in atTop, Zsum μ ≤ Ξ μ * N μ)
    (hG : Subexp G) (hΞ : Subexp Ξ)
    (hN : Tendsto (fun μ => Real.log (N μ) / μ) atTop (𝓝 (-(4 * π))))
    {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ μ in atTop, Real.log (s μ) ≤ (-(4 * π) + ε) * μ := by
  refine eventually_log_le (A := fun μ => Ξ μ / G μ) (B := N) hspos ?_ hNpos ?_ ?_ hN hε
  · filter_upwards [hΞpos, hGpos] with μ h1 h2 using div_pos h1 h2
  · -- `s ≤ (Ξ/G) · N` is the three inequalities chained and then divided by `G > 0`
    filter_upwards [hGpos, hRayleigh, hidentity, hQ3] with μ hG0 hR hI h3
    rw [div_mul_eq_mul_div, le_div_iff₀ hG0]
    calc s μ * G μ ≤ Q μ := hR
      _ = Zsum μ := hI
      _ ≤ Ξ μ * N μ := h3
  · exact hΞ.div hG (hΞpos.mono fun _ h => h.ne') (hGpos.mono fun _ h => h.ne')

/-- **Corollary `cor:upper`**, in the paper's `limsup` form.  See
`limsup_logRate_le` for what `hbelow` is doing and why it is not an artefact. -/
theorem limsup_le_neg_four_pi {s G Q Zsum Ξ N : ℝ → ℝ}
    (hspos : ∀ᶠ μ in atTop, 0 < s μ)
    (hGpos : ∀ᶠ μ in atTop, 0 < G μ)
    (hΞpos : ∀ᶠ μ in atTop, 0 < Ξ μ)
    (hNpos : ∀ᶠ μ in atTop, 0 < N μ)
    (hRayleigh : ∀ᶠ μ in atTop, s μ * G μ ≤ Q μ)
    (hidentity : ∀ᶠ μ in atTop, Q μ = Zsum μ)
    (hQ3 : ∀ᶠ μ in atTop, Zsum μ ≤ Ξ μ * N μ)
    (hG : Subexp G) (hΞ : Subexp Ξ)
    (hN : Tendsto (fun μ => Real.log (N μ) / μ) atTop (𝓝 (-(4 * π))))
    (hbelow : ∃ b : ℝ, ∀ᶠ μ in atTop, b ≤ Real.log (s μ) / μ) :
    limsup (fun μ => Real.log (s μ) / μ) atTop ≤ -(4 * π) := by
  refine limsup_logRate_le (A := fun μ => Ξ μ / G μ) (B := N) hspos ?_ hNpos ?_ ?_ hN hbelow
  · filter_upwards [hΞpos, hGpos] with μ h1 h2 using div_pos h1 h2
  · filter_upwards [hGpos, hRayleigh, hidentity, hQ3] with μ hG0 hR hI h3
    rw [div_mul_eq_mul_div, le_div_iff₀ hG0]
    calc s μ * G μ ≤ Q μ := hR
      _ = Zsum μ := hI
      _ ≤ Ξ μ * N μ := h3
  · exact hΞ.div hG (hΞpos.mono fun _ h => h.ne') (hGpos.mono fun _ h => h.ne')

/-! ## The paper's own exponents, instantiated

The corollary above is only as good as the satisfiability of its hypotheses, so
here they are discharged at the paper's own numbers:

* `Ξ μ = CΞ · μ⁶ · (log μ)³` — Theorem `thm:q3`, proved column;
* `N μ = CN · μ^{9/2} · e^{-4πμ}`, written `CN · μ⁴ · √μ · e^{-4πμ}` to stay
  inside `ℝ`-valued powers — the Fuchs rate of paper §6.2;
* `G μ → 0.219247199549…` — Theorem `thm:h0`.

The point of this theorem is that the exponent arithmetic of the paper closes:
the polynomial factors `μ^6 log³μ` and `μ^{9/2}` are exactly the ones the paper
carries, and they are invisible to the `limsup`. -/
/-- `1 ≤ log μ ≤ μ` for `μ ≥ e`: the only fact about `log` the sandwich needs. -/
lemma eventually_log_bracket : ∀ᶠ μ : ℝ in atTop, 1 ≤ Real.log μ ∧ Real.log μ ≤ μ := by
  filter_upwards [eventually_ge_atTop (Real.exp 1)] with μ hμ
  have hμ1 : (1:ℝ) ≤ μ := le_trans (Real.one_le_exp zero_le_one) hμ
  refine ⟨?_, ?_⟩
  · rw [← Real.log_exp 1]; exact Real.log_le_log (Real.exp_pos 1) hμ
  · linarith [Real.log_le_sub_one_of_pos (lt_of_lt_of_le zero_lt_one hμ1)]

/-- `Ξ μ = CΞ μ⁶ log³μ` — Theorem `thm:q3`'s proved column — is subexponential:
it lies between `CΞ` and `CΞ μ⁹`. -/
lemma subexp_paper_Xi {CΞ : ℝ} (hCΞ : 0 < CΞ) :
    Subexp (fun μ => CΞ * μ ^ 6 * (Real.log μ) ^ 3) := by
  refine Subexp.of_sandwich (c := CΞ) (C := CΞ) (k := 9) hCΞ hCΞ ?_ ?_
  · filter_upwards [eventually_log_bracket, eventually_ge_atTop (1:ℝ)] with μ hl hμ1
    have h6 : (1:ℝ) ≤ μ ^ 6 := one_le_pow₀ hμ1
    have h3 : (1:ℝ) ≤ (Real.log μ) ^ 3 := one_le_pow₀ hl.1
    have hbig : (1:ℝ) ≤ μ ^ 6 * (Real.log μ) ^ 3 := by nlinarith
    calc CΞ = CΞ * 1 := (mul_one _).symm
      _ ≤ CΞ * (μ ^ 6 * (Real.log μ) ^ 3) := mul_le_mul_of_nonneg_left hbig hCΞ.le
      _ = CΞ * μ ^ 6 * (Real.log μ) ^ 3 := by ring
  · filter_upwards [eventually_log_bracket, eventually_ge_atTop (1:ℝ)] with μ hl hμ1
    have h3 : (Real.log μ) ^ 3 ≤ μ ^ 3 :=
      pow_le_pow_left₀ (by linarith [hl.1]) hl.2 3
    have h : μ ^ 6 * (Real.log μ) ^ 3 ≤ μ ^ 9 := by
      calc μ ^ 6 * (Real.log μ) ^ 3 ≤ μ ^ 6 * μ ^ 3 :=
            mul_le_mul_of_nonneg_left h3 (by positivity)
        _ = μ ^ 9 := by ring
    calc CΞ * μ ^ 6 * (Real.log μ) ^ 3 = CΞ * (μ ^ 6 * (Real.log μ) ^ 3) := by ring
      _ ≤ CΞ * μ ^ 9 := mul_le_mul_of_nonneg_left h hCΞ.le

/-- The Fuchs prefactor `CN μ^{9/2}` is subexponential: between `CN` and `CN μ⁵`. -/
lemma subexp_paper_prefactor {CN : ℝ} (hCN : 0 < CN) :
    Subexp (fun μ => CN * μ ^ 4 * Real.sqrt μ) := by
  refine Subexp.of_sandwich (c := CN) (C := CN) (k := 5) hCN hCN ?_ ?_
  · filter_upwards [eventually_ge_atTop (1:ℝ)] with μ hμ1
    have hs : (1:ℝ) ≤ Real.sqrt μ := by
      rw [show (1:ℝ) = Real.sqrt 1 by simp]
      exact Real.sqrt_le_sqrt hμ1
    have h4 : (1:ℝ) ≤ μ ^ 4 := one_le_pow₀ hμ1
    have hbig : (1:ℝ) ≤ μ ^ 4 * Real.sqrt μ := by nlinarith
    calc CN = CN * 1 := (mul_one _).symm
      _ ≤ CN * (μ ^ 4 * Real.sqrt μ) := mul_le_mul_of_nonneg_left hbig hCN.le
      _ = CN * μ ^ 4 * Real.sqrt μ := by ring
  · filter_upwards [eventually_ge_atTop (1:ℝ)] with μ hμ1
    have hμ0 : (0:ℝ) ≤ μ := by linarith
    have hs : Real.sqrt μ ≤ μ := by
      nlinarith [Real.sq_sqrt hμ0, Real.sqrt_nonneg μ,
        show (1:ℝ) ≤ Real.sqrt μ by
          rw [show (1:ℝ) = Real.sqrt 1 by simp]; exact Real.sqrt_le_sqrt hμ1]
    have h : μ ^ 4 * Real.sqrt μ ≤ μ ^ 5 := by
      calc μ ^ 4 * Real.sqrt μ ≤ μ ^ 4 * μ := mul_le_mul_of_nonneg_left hs (by positivity)
        _ = μ ^ 5 := by ring
    calc CN * μ ^ 4 * Real.sqrt μ = CN * (μ ^ 4 * Real.sqrt μ) := by ring
      _ ≤ CN * μ ^ 5 := mul_le_mul_of_nonneg_left h hCN.le

theorem eventually_log_le_at_paper_exponents
    {s G Q Zsum : ℝ → ℝ} {CΞ CN g₀ : ℝ}
    (hCΞ : 0 < CΞ) (hCN : 0 < CN) (hg₀ : 0 < g₀)
    (hspos : ∀ᶠ μ in atTop, 0 < s μ)
    (hGpos : ∀ᶠ μ in atTop, 0 < G μ)
    (hRayleigh : ∀ᶠ μ in atTop, s μ * G μ ≤ Q μ)
    (hidentity : ∀ᶠ μ in atTop, Q μ = Zsum μ)
    (hQ3 : ∀ᶠ μ in atTop,
      Zsum μ ≤ (CΞ * μ ^ 6 * (Real.log μ) ^ 3) *
        ((CN * μ ^ 4 * Real.sqrt μ) * Real.exp (-(4 * π) * μ)))
    (hG : Tendsto G atTop (𝓝 g₀))
    {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ μ in atTop, Real.log (s μ) ≤ (-(4 * π) + ε) * μ := by
  have hPpos : ∀ᶠ μ : ℝ in atTop, (0:ℝ) < CN * μ ^ 4 * Real.sqrt μ := by
    filter_upwards [eventually_gt_atTop (0:ℝ)] with μ hμ
    have : (0:ℝ) < Real.sqrt μ := Real.sqrt_pos.mpr hμ
    positivity
  refine eventually_log_le_neg_four_pi (G := G) (Q := Q) (Zsum := Zsum)
    (Ξ := fun μ => CΞ * μ ^ 6 * (Real.log μ) ^ 3)
    (N := fun μ => (CN * μ ^ 4 * Real.sqrt μ) * Real.exp (-(4 * π) * μ))
    hspos hGpos ?_ ?_ hRayleigh hidentity hQ3 (Subexp.of_tendsto_pos hg₀ hG)
    (subexp_paper_Xi hCΞ) ?_ hε
  · filter_upwards [eventually_log_bracket, eventually_gt_atTop (0:ℝ)] with μ hl hμ
    have h1 : (0:ℝ) < Real.log μ := lt_of_lt_of_le zero_lt_one hl.1
    positivity
  · filter_upwards [hPpos] with μ h
    exact mul_pos h (Real.exp_pos _)
  · exact tendsto_logRate_mul_exp (subexp_paper_prefactor hCN)
      (hPpos.mono fun _ h => h.ne')

/-- **Theorem `thm:main`, at the paper's own exponents, in `limsup` form.** -/
theorem limsup_le_neg_four_pi_at_paper_exponents
    {s G Q Zsum : ℝ → ℝ} {CΞ CN g₀ : ℝ}
    (hCΞ : 0 < CΞ) (hCN : 0 < CN) (hg₀ : 0 < g₀)
    (hspos : ∀ᶠ μ in atTop, 0 < s μ)
    (hGpos : ∀ᶠ μ in atTop, 0 < G μ)
    (hRayleigh : ∀ᶠ μ in atTop, s μ * G μ ≤ Q μ)
    (hidentity : ∀ᶠ μ in atTop, Q μ = Zsum μ)
    (hQ3 : ∀ᶠ μ in atTop,
      Zsum μ ≤ (CΞ * μ ^ 6 * (Real.log μ) ^ 3) *
        ((CN * μ ^ 4 * Real.sqrt μ) * Real.exp (-(4 * π) * μ)))
    (hG : Tendsto G atTop (𝓝 g₀))
    (hbelow : ∃ b : ℝ, ∀ᶠ μ in atTop, b ≤ Real.log (s μ) / μ) :
    limsup (fun μ => Real.log (s μ) / μ) atTop ≤ -(4 * π) := by
  have hPpos : ∀ᶠ μ : ℝ in atTop, (0:ℝ) < CN * μ ^ 4 * Real.sqrt μ := by
    filter_upwards [eventually_gt_atTop (0:ℝ)] with μ hμ
    have : (0:ℝ) < Real.sqrt μ := Real.sqrt_pos.mpr hμ
    positivity
  refine limsup_le_neg_four_pi (G := G) (Q := Q) (Zsum := Zsum)
    (Ξ := fun μ => CΞ * μ ^ 6 * (Real.log μ) ^ 3)
    (N := fun μ => (CN * μ ^ 4 * Real.sqrt μ) * Real.exp (-(4 * π) * μ))
    hspos hGpos ?_ ?_ hRayleigh hidentity hQ3 (Subexp.of_tendsto_pos hg₀ hG)
    (subexp_paper_Xi hCΞ) ?_ hbelow
  · filter_upwards [eventually_log_bracket, eventually_gt_atTop (0:ℝ)] with μ hl hμ
    have h1 : (0:ℝ) < Real.log μ := lt_of_lt_of_le zero_lt_one hl.1
    positivity
  · filter_upwards [hPpos] with μ h
    exact mul_pos h (Real.exp_pos _)
  · exact tendsto_logRate_mul_exp (subexp_paper_prefactor hCN)
      (hPpos.mono fun _ h => h.ne')

end Riemann.Assembly
