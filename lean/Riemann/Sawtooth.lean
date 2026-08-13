/-
# The quantisation dichotomy: the sawtooth is bounded, the cosine sum is not

Formalisation of the two Fourier identities that Theorem `thm:q2` (Q2, the
dilate sum) turns on, and of the contrast between them — paper §7.5, and
`notes/dilate-sum.md` §3, where it is called "the load-bearing line of the note":

> `∑_{m≥1} sin(mγ)/m = (π-γ)/2` for `0 < γ < 2π` **is bounded**, while
> `∑_{m≥1} cos(mγ)/m = -log|2 sin(γ/2)|` **is not**.

That contrast is the whole reason Q2 is true for the prolate *eigenfunctions* and
false for a general solution of the prolate equation: the leading off-band term of
an eigenfunction is a pure sine (`β_∞ = 0`), and a cosine component of any size
would make `sup_{t>1} t|G(t)| = +∞` (Corollary `cor:quantisation`).

## Why this file, and not the ODE

`Riemann/BandEdge.lean` stops below Q1 because a continuous branch of the Prüfer
angle along an ODE-defined curve does not exist in mathlib (mg-a087).  Nothing in
*this* file is an ODE statement: the identities below are proved from Abel's limit
theorem on the unit circle, which mathlib has
(`Complex.tendsto_tsum_powerSeries_nhdsWithin_lt`), plus Dirichlet's test, which
mathlib also has.  That is the sense in which Q2's *quantisation* half is reachable
where Q1's *amplitude* half is not.

## What formalising forced: `HasSum` is the wrong predicate

The series `∑ sin(mγ)/m` is **not** absolutely convergent, so it has no `HasSum`
in Lean's sense (`HasSum` is unconditional convergence of the net of finite partial
sums, which for a real series is equivalent to absolute convergence).  Every
statement below is therefore about `Tendsto (fun N => ∑ n ∈ Finset.range N, …)`,
the limit of the *initial* partial sums.

This is not a Lean artefact and it is not cosmetic.  `dilate-sum.md` §0 already
says `G(t)` is "the limit of the symmetric partial sums" and §5 invokes Dirichlet's
test, so the note is correct; but `notes/dilate-sum.md` §5's proof then writes
`t|G(t)| ≤ (π/2)|a₁| + t ∑_{m≥1} |W(mt)|`, splitting a conditionally convergent
series into two pieces — which is legitimate **only** because the second piece is
absolutely convergent (Prop. 4.1(ii)) and so the first inherits convergence from
the whole.  Formalising makes that dependency explicit rather than implicit; see
`Riemann/DilateSum.lean`, where the split is `hasSum_add_of_tendsto`.

## Sign-blindness (the house rule)

Both identities are **sign-blind**, and in the strong sense: replacing `Φ` by `-Φ`
replaces `a₁` by `-a₁` and `G` by `-G`, and every statement here is an equality or
a bound on a modulus that is invariant under that. `sawtooth_abs_le` bounds `|S|`.
Nothing here has a one-signed conclusion.

## Mathlib

Built against mathlib `5e932f97dd25535344f80f9dd8da3aab83df0fe6` (tag
`v4.29.1`), Lean toolchain `leanprover/lean4:v4.29.1`.
-/
import Mathlib

namespace Riemann.Sawtooth

open Filter Topology Finset
open scoped Real

/-! ## The point on the unit circle -/

/-- `w γ = e^{iγ}`, the point of the unit circle the two series are expanded at. -/
noncomputable def w (γ : ℝ) : ℂ := Complex.exp ((γ : ℂ) * Complex.I)

lemma norm_w (γ : ℝ) : ‖w γ‖ = 1 := by
  simp [w, Complex.norm_exp_ofReal_mul_I]

/-- `sin (γ/2) > 0` for `0 < γ < 2π`.  This is used three times: it is why
`w γ ≠ 1`, why `1 - w γ` lies in the slit plane, and why `log (2 sin (γ/2))` is
defined. -/
lemma sin_half_pos {γ : ℝ} (h0 : 0 < γ) (h2 : γ < 2 * π) : 0 < Real.sin (γ / 2) :=
  Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)

/-- `cos γ = 1 - 2 sin²(γ/2)`. -/
lemma cos_eq_half (γ : ℝ) : Real.cos γ = 1 - 2 * Real.sin (γ / 2) ^ 2 := by
  have h := Real.cos_two_mul' (γ / 2)
  rw [show 2 * (γ / 2) = γ by ring] at h
  rw [h, Real.sin_sq]
  ring

/-- `sin γ = 2 sin(γ/2) cos(γ/2)`. -/
lemma sin_eq_half (γ : ℝ) : Real.sin γ = 2 * Real.sin (γ / 2) * Real.cos (γ / 2) := by
  have h := Real.sin_two_mul (γ / 2)
  rw [show 2 * (γ / 2) = γ by ring] at h
  exact h

/-- `Re (1 - w γ) = 1 - cos γ = 2 sin²(γ/2) > 0`.  In particular `1 - w γ ≠ 0` and
`1 - w γ` is in the slit plane, so `Complex.log` is continuous there. -/
lemma one_sub_w_re {γ : ℝ} (h0 : 0 < γ) (h2 : γ < 2 * π) : 0 < (1 - w γ).re := by
  have hs := sin_half_pos h0 h2
  have hcos : Real.cos γ = 1 - 2 * Real.sin (γ / 2) ^ 2 := cos_eq_half γ
  have : (1 - w γ).re = 1 - Real.cos γ := by
    simp [w, Complex.exp_ofReal_mul_I_re]
  rw [this, hcos]
  nlinarith

lemma one_sub_w_ne_zero {γ : ℝ} (h0 : 0 < γ) (h2 : γ < 2 * π) : 1 - w γ ≠ 0 := by
  intro h
  have := one_sub_w_re h0 h2
  rw [h] at this
  simp at this

lemma w_ne_one {γ : ℝ} (h0 : 0 < γ) (h2 : γ < 2 * π) : w γ ≠ 1 := by
  intro h
  exact one_sub_w_ne_zero h0 h2 (by rw [h]; ring)

/-! ## The closed form of `-log (1 - w γ)`

This is where the two identities separate: the real part is the (unbounded)
logarithm and the imaginary part is the (bounded) sawtooth. -/

/-- The polar form `1 - e^{iγ} = 2 sin(γ/2) · e^{i(γ-π)/2}`, written as a single
complex exponential so that `Complex.log_exp` applies. -/
lemma one_sub_w_eq_exp {γ : ℝ} (h0 : 0 < γ) (h2 : γ < 2 * π) :
    1 - w γ =
      Complex.exp ((Real.log (2 * Real.sin (γ / 2)) : ℂ) + ((γ - π) / 2 : ℝ) * Complex.I) := by
  have hs := sin_half_pos h0 h2
  have hpos : (0:ℝ) < 2 * Real.sin (γ / 2) := by linarith
  rw [Complex.exp_add, Complex.exp_ofReal_mul_I, ← Complex.ofReal_exp, Real.exp_log hpos]
  apply Complex.ext
  · have hre : (1 - w γ).re = 1 - Real.cos γ := by
      simp [w, Complex.exp_ofReal_mul_I_re]
    simp only [hre, Complex.mul_re, Complex.add_re, Complex.add_im, Complex.ofReal_re,
      Complex.ofReal_im, Complex.mul_im, Complex.I_re, Complex.I_im]
    have h1 : Real.cos ((γ - π) / 2) = Real.sin (γ / 2) := by
      have : (γ - π) / 2 = γ / 2 - π / 2 := by ring
      rw [this, Real.cos_sub, Real.cos_pi_div_two, Real.sin_pi_div_two]
      ring
    rw [h1, cos_eq_half γ]
    ring
  · have him : (1 - w γ).im = -Real.sin γ := by
      simp [w, Complex.exp_ofReal_mul_I_im]
    simp only [him, Complex.mul_re, Complex.add_re, Complex.add_im, Complex.ofReal_re,
      Complex.ofReal_im, Complex.mul_im, Complex.I_re, Complex.I_im]
    have h1 : Real.sin ((γ - π) / 2) = -Real.cos (γ / 2) := by
      have : (γ - π) / 2 = γ / 2 - π / 2 := by ring
      rw [this, Real.sin_sub, Real.cos_pi_div_two, Real.sin_pi_div_two]
      ring
    rw [h1, sin_eq_half γ]
    ring

/-- `-log (1 - e^{iγ}) = -log (2 sin (γ/2)) + i(π-γ)/2`.  The real part is the
divergent half and the imaginary part is the sawtooth. -/
lemma neg_log_one_sub_w {γ : ℝ} (h0 : 0 < γ) (h2 : γ < 2 * π) :
    -Complex.log (1 - w γ) =
      (-Real.log (2 * Real.sin (γ / 2)) : ℂ) + ((π - γ) / 2 : ℝ) * Complex.I := by
  rw [one_sub_w_eq_exp h0 h2, Complex.log_exp]
  · push_cast
    ring
  · simp only [Complex.add_im, Complex.ofReal_im, Complex.mul_im, Complex.ofReal_re,
      Complex.I_im, Complex.I_re]
    have : (0:ℝ) < π := Real.pi_pos
    norm_num
    linarith
  · simp only [Complex.add_im, Complex.ofReal_im, Complex.mul_im, Complex.ofReal_re,
      Complex.I_im, Complex.I_re]
    have : (0:ℝ) < π := Real.pi_pos
    norm_num
    linarith

/-! ## Convergence of the partial sums (Dirichlet's test) -/

/-- The geometric partial sums of `w γ` are bounded, uniformly in `n`. -/
lemma norm_geom_sum_le {γ : ℝ} (h0 : 0 < γ) (h2 : γ < 2 * π) (n : ℕ) :
    ‖∑ i ∈ range n, w γ ^ (i + 1)‖ ≤ 2 / ‖1 - w γ‖ := by
  have hne : w γ ≠ 1 := w_ne_one h0 h2
  have hden : (0:ℝ) < ‖1 - w γ‖ := by
    simpa [norm_pos_iff] using one_sub_w_ne_zero h0 h2
  have hgeom : ∑ i ∈ range n, w γ ^ (i + 1) = w γ * ((w γ ^ n - 1) / (w γ - 1)) := by
    rw [← geom_sum_eq hne n, Finset.mul_sum]
    exact Finset.sum_congr rfl fun i _ => by ring
  rw [hgeom, norm_mul, norm_w, one_mul, norm_div]
  have hnum : ‖w γ ^ n - 1‖ ≤ 2 := by
    calc ‖w γ ^ n - 1‖ ≤ ‖w γ ^ n‖ + ‖(1:ℂ)‖ := norm_sub_le _ _
      _ = 2 := by rw [norm_pow, norm_w]; norm_num
  have hsub : ‖w γ - 1‖ = ‖1 - w γ‖ := by rw [← norm_neg, neg_sub]
  rw [hsub]
  gcongr

/-- Dirichlet's test: the partial sums of `∑ w^n / n` converge. -/
lemma cauchySeq_partial {γ : ℝ} (h0 : 0 < γ) (h2 : γ < 2 * π) :
    CauchySeq fun N => ∑ n ∈ range N, w γ ^ n / (n : ℂ) := by
  rw [← cauchySeq_shift 1]
  have hkey : CauchySeq fun N => ∑ i ∈ range N, ((1 / (i + 1 : ℝ)) • (w γ ^ (i + 1))) := by
    refine Antitone.cauchySeq_series_mul_of_tendsto_zero_of_bounded
      (f := fun i => 1 / (i + 1 : ℝ)) (z := fun i => w γ ^ (i + 1)) ?_ ?_
      (norm_geom_sum_le h0 h2)
    · intro a b hab
      have hab' : (a : ℝ) ≤ b := Nat.cast_le.mpr hab
      exact one_div_le_one_div_of_le (by positivity) (by linarith)
    · exact tendsto_one_div_add_atTop_nhds_zero_nat
  have heqf : (fun N => ∑ i ∈ range N, ((1 / (i + 1 : ℝ)) • (w γ ^ (i + 1))))
      = fun N => ∑ n ∈ range (N + 1), w γ ^ n / (n : ℂ) := by
    funext N
    rw [Finset.sum_range_succ']
    simp only [pow_zero, Nat.cast_zero, div_zero, add_zero]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Complex.real_smul]
    push_cast
    field_simp
  rw [heqf] at hkey
  exact hkey

/-- The Abel-summation step: the limit of the partial sums of `∑ w^n/n` is
`-log (1 - w)`.

Mathlib's Abel limit theorem is stated at the point `1`, so it is applied to the
coefficient sequence `n ↦ w^n/n` and the *real* variable `x → 1⁻`; the power series
value `∑ (xw)^n/n = -log (1 - xw)` is the ordinary Taylor series of `-log`, valid
because `‖xw‖ = x < 1`. -/
theorem tendsto_partial_sum {γ : ℝ} (h0 : 0 < γ) (h2 : γ < 2 * π) :
    Tendsto (fun N => ∑ n ∈ range N, w γ ^ n / (n : ℂ)) atTop
      (𝓝 (-Complex.log (1 - w γ))) := by
  obtain ⟨l, hl⟩ := cauchySeq_tendsto_of_complete (cauchySeq_partial h0 h2)
  -- Abel: the power series tends to `l` as `x → 1⁻`
  have habel : Tendsto (fun x : ℝ => ∑' n : ℕ, (w γ ^ n / (n : ℂ)) * (x : ℂ) ^ n)
      (𝓝[<] 1) (𝓝 l) := by
    have h := Complex.tendsto_tsum_powerSeries_nhdsWithin_lt hl
    rw [tendsto_map'_iff] at h
    exact h
  -- the power series is `-log (1 - xw)`
  have hval : ∀ x : ℝ, 0 < x → x < 1 →
      ∑' n : ℕ, (w γ ^ n / (n : ℂ)) * (x : ℂ) ^ n = -Complex.log (1 - (x : ℂ) * w γ) := by
    intro x hx hx1
    have hz : ‖(x : ℂ) * w γ‖ < 1 := by
      rw [norm_mul, norm_w, mul_one, Complex.norm_real, Real.norm_eq_abs, abs_of_pos hx]
      exact hx1
    have hts : HasSum (fun n : ℕ => ((x : ℂ) * w γ) ^ n / (n : ℂ))
        (-Complex.log (1 - (x : ℂ) * w γ)) := by
      exact Complex.hasSum_taylorSeries_neg_log hz
    have := hts.tsum_eq
    rw [← this]
    exact tsum_congr fun n => by rw [mul_pow]; ring
  -- and `-log (1 - xw) → -log (1 - w)` by continuity of `log` on the slit plane
  have hcont : Tendsto (fun x : ℝ => -Complex.log (1 - (x : ℂ) * w γ)) (𝓝[<] 1)
      (𝓝 (-Complex.log (1 - w γ))) := by
    have hslit : 1 - w γ ∈ Complex.slitPlane := Or.inl (one_sub_w_re h0 h2)
    have h1 : Tendsto (fun x : ℝ => 1 - (x : ℂ) * w γ) (𝓝[<] 1) (𝓝 (1 - w γ)) := by
      have : Continuous fun x : ℝ => 1 - (x : ℂ) * w γ := by fun_prop
      simpa using (this.tendsto 1).mono_left nhdsWithin_le_nhds
    exact ((continuousAt_clog hslit).tendsto.comp h1).neg
  have heq : Tendsto (fun x : ℝ => ∑' n : ℕ, (w γ ^ n / (n : ℂ)) * (x : ℂ) ^ n)
      (𝓝[<] 1) (𝓝 (-Complex.log (1 - w γ))) := by
    refine hcont.congr' ?_
    filter_upwards [Ioo_mem_nhdsLT (show (0:ℝ) < 1 by norm_num)] with x hx
    exact (hval x hx.1 hx.2).symm
  have : l = -Complex.log (1 - w γ) := tendsto_nhds_unique habel heq
  rwa [this] at hl

/-! ## The two real identities -/

/-- `w γ ^ n / n` has real part `cos(nγ)/n` and imaginary part `sin(nγ)/n`,
including at `n = 0` where both sides are `0` by Lean's `x/0 = 0`. -/
lemma pow_div_re_im (γ : ℝ) (n : ℕ) :
    (w γ ^ n / (n : ℂ)).re = Real.cos (n * γ) / n ∧
    (w γ ^ n / (n : ℂ)).im = Real.sin (n * γ) / n := by
  have hpow : w γ ^ n = Complex.exp ((((n : ℝ) * γ : ℝ) : ℂ) * Complex.I) := by
    rw [w, ← Complex.exp_nat_mul]
    congr 1
    push_cast
    ring
  have hcast : (n : ℂ) = ((n : ℝ) : ℂ) := by push_cast; ring
  rw [hpow, hcast]
  constructor
  · rw [Complex.div_ofReal_re, Complex.exp_ofReal_mul_I_re]
  · rw [Complex.div_ofReal_im, Complex.exp_ofReal_mul_I_im]

/-- **The sawtooth.**  For `0 < γ < 2π`,
`∑_{n≥1} sin(nγ)/n = (π-γ)/2` — as a limit of initial partial sums; the series is
not absolutely convergent. -/
theorem tendsto_sin_sum {γ : ℝ} (h0 : 0 < γ) (h2 : γ < 2 * π) :
    Tendsto (fun N => ∑ n ∈ range N, Real.sin (n * γ) / n) atTop (𝓝 ((π - γ) / 2)) := by
  have h := (Complex.continuous_im.tendsto _).comp (tendsto_partial_sum h0 h2)
  rw [neg_log_one_sub_w h0 h2] at h
  simp only [Function.comp_def, Complex.add_im, Complex.neg_im, Complex.ofReal_im,
    Complex.mul_im, Complex.ofReal_re, Complex.I_im, Complex.I_re, neg_zero, mul_one,
    mul_zero, add_zero, zero_add] at h
  refine h.congr fun N => ?_
  rw [Complex.im_sum]
  exact Finset.sum_congr rfl fun n _ => (pow_div_re_im γ n).2

/-- **The divergent half.**  For `0 < γ < 2π`,
`∑_{n≥1} cos(nγ)/n = -log (2 sin (γ/2))`. -/
theorem tendsto_cos_sum {γ : ℝ} (h0 : 0 < γ) (h2 : γ < 2 * π) :
    Tendsto (fun N => ∑ n ∈ range N, Real.cos (n * γ) / n) atTop
      (𝓝 (-Real.log (2 * Real.sin (γ / 2)))) := by
  have h := (Complex.continuous_re.tendsto _).comp (tendsto_partial_sum h0 h2)
  rw [neg_log_one_sub_w h0 h2] at h
  simp only [Function.comp_def, Complex.add_re, Complex.neg_re, Complex.ofReal_re,
    Complex.mul_re, Complex.ofReal_im, Complex.I_re, Complex.I_im, mul_zero, mul_one,
    sub_zero, add_zero] at h
  refine h.congr fun N => ?_
  rw [Complex.re_sum]
  exact Finset.sum_congr rfl fun n _ => (pow_div_re_im γ n).1

/-! ## The dichotomy

These are the two statements Q2 consumes.  The first is the bound that makes
Theorem `thm:q2` true; the second is Corollary `cor:quantisation`, i.e. the reason
no argument from the prolate differential equation alone can prove it. -/

/-- **The sawtooth bound, in the form Theorem `thm:q2` consumes.**  For every
`γ ∈ [0, 2π)` the partial sums of `∑ sin(nγ)/n` converge, to a limit of modulus at
most `π/2`.  The resonance `γ = 0` is included and there the limit is `0` — every
term vanishes identically — which is the case `dilate-sum.md` §7 CHECK 0 records a
first draft of the numerics getting wrong. -/
theorem sawtooth_abs_le {γ : ℝ} (h0 : 0 ≤ γ) (h2 : γ < 2 * π) :
    ∃ S : ℝ, |S| ≤ π / 2 ∧
      Tendsto (fun N => ∑ n ∈ range N, Real.sin (n * γ) / n) atTop (𝓝 S) := by
  rcases eq_or_lt_of_le h0 with rfl | h0'
  · refine ⟨0, by rw [abs_zero]; positivity, ?_⟩
    have hz : (fun N : ℕ => ∑ n ∈ range N, Real.sin ((n : ℝ) * 0) / (n : ℝ))
        = fun _ : ℕ => (0:ℝ) := by
      funext N; simp
    rw [hz]
    exact tendsto_const_nhds
  · refine ⟨(π - γ) / 2, ?_, tendsto_sin_sum h0' h2⟩
    rw [abs_le]
    constructor <;> [linarith [Real.pi_pos]; linarith [Real.pi_pos]]

/-- **Corollary `cor:quantisation`.**  The cosine sum is unbounded: as `γ → 0⁺`
its value `-log (2 sin (γ/2))` tends to `+∞`.

This is the precise sense in which `β_∞ = 0` is load-bearing.  A solution of the
prolate equation with a cosine component of *any* nonzero size has
`sup_{t>1} t|G(t)| = +∞`, because `ct mod 2π` comes arbitrarily close to `0`; so
`thm:q2` is a statement about eigenfunctions, not about the differential
equation. -/
theorem tendsto_cos_sum_value_atTop :
    Tendsto (fun γ : ℝ => -Real.log (2 * Real.sin (γ / 2))) (𝓝[>] 0) atTop := by
  have hinner : Tendsto (fun γ : ℝ => 2 * Real.sin (γ / 2)) (𝓝[>] 0) (𝓝[>] 0) := by
    refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _ ?_ ?_
    · have : Continuous fun γ : ℝ => 2 * Real.sin (γ / 2) := by fun_prop
      simpa using (this.tendsto 0).mono_left nhdsWithin_le_nhds
    · filter_upwards [Ioo_mem_nhdsGT (show (0:ℝ) < π from Real.pi_pos)] with γ hγ
      have hγ1 : (0:ℝ) < γ := hγ.1
      have hγ2 : γ < π := hγ.2
      have hs := sin_half_pos hγ1 (by linarith [Real.pi_pos])
      simp only [Set.mem_Ioi]
      linarith
  exact tendsto_neg_atBot_atTop.comp (Real.tendsto_log_nhdsGT_zero.comp hinner)

end Riemann.Sawtooth
