/-
# Q2's summation step: the cancellation that replaces `+∞` by `π/2`

Formalisation of the mechanism of Theorem `thm:q2` (`dilate-sum.md` Thm 5.1):
given the off-band splitting

    Φ x = a₁ sin(cx)/x + W x

and the second remainder bound of `dilate-sum.md` Prop. 4.1(ii), the dilate sum
`G t = ∑_{m≥1} Φ(mt)` converges for every `t > 1` and

    t |G t| ≤ (π/2)|a₁| + t ∑_{m≥1} |W(mt)| .

**This is where Q2 is won or lost.**  The triangle inequality applied to the
leading term gives `∑_m |a₁|/(mt) = +∞` — a harmonic divergence
(`notes/dilate-sum.md` §1).  What replaces `+∞` by `π/2` is the sawtooth
cancellation of `Riemann/Sawtooth.lean`, and it is available only because the
leading term is a *pure sine*: `β_∞ = 0`, the quantisation statement.  A cosine
component of any size would put `-log|2 sin(ct/2)|` here instead, which is
unbounded (`Riemann.Sawtooth.tendsto_cos_sum_value_atTop`).

The remaining piece — the explicit constant `K_P(c) = O(log c)`, i.e. bounding
`t ∑_m |W(mt)|` by `B₁P(1 + log X) + 2B₂P/X` — is `tsum_abs_le` below.

## What is a hypothesis here and what is not

Nothing about prolate functions is used.  `hsplit`, `hW1`, `hW2` are the
conclusions of `dilate-sum.md` §§2–4, which rest on Q1 and on the finite-Fourier
eigenrelation; those are *not* formalised (see `lean/README.md`'s reachability
table — Q1 needs the Prüfer angle).  What is formalised is that Theorem 5.1
follows from them, and that the reduction `ct ↦ γ = ct mod 2π` is legitimate.

## Sign-blindness (the house rule)

**Sign-blind.**  Under `Φ ↦ -Φ` we have `a₁ ↦ -a₁`, `W ↦ -W`, `S ↦ -S`, and
every statement below is an equality or a bound on a modulus, all invariant.  No
conclusion here is one-signed.

## Mathlib

Built against mathlib `5e932f97dd25535344f80f9dd8da3aab83df0fe6` (tag
`v4.29.1`), Lean toolchain `leanprover/lean4:v4.29.1`.
-/
import Riemann.Sawtooth

namespace Riemann.DilateSum

open Filter Topology Finset
open scoped Real

/-! ## The reduction `ct ↦ γ = ct mod 2π`

`dilate-sum.md` §5 writes `γ := ct mod 2π ∈ [0,2π)` and then treats
`sin(cmt)` as `sin(mγ)` for every `m`.  That step is `2π`-periodicity of `sin`
along the *integer* multiples `m·k`, and it is worth having separately because it
is the one place the argument uses that `m` ranges over integers rather than
reals. -/

/-- `ct` reduced mod `2π`: there is `γ ∈ [0,2π)` with `sin(c·mt) = sin(mγ)` for
every natural `m`. -/
lemma exists_gamma (c t : ℝ) :
    ∃ γ : ℝ, 0 ≤ γ ∧ γ < 2 * π ∧
      ∀ m : ℕ, Real.sin (c * ((m : ℝ) * t)) = Real.sin ((m : ℝ) * γ) := by
  have hτ : (0:ℝ) < 2 * π := by positivity
  set r : ℝ := c * t / (2 * π) with hr
  set k : ℤ := ⌊r⌋ with hk
  refine ⟨Int.fract r * (2 * π), ?_, ?_, ?_⟩
  · exact mul_nonneg (Int.fract_nonneg r) hτ.le
  · calc Int.fract r * (2 * π) < 1 * (2 * π) := by
          exact mul_lt_mul_of_pos_right (Int.fract_lt_one r) hτ
      _ = 2 * π := one_mul _
  · intro m
    have hct : c * t = Int.fract r * (2 * π) + (k : ℝ) * (2 * π) := by
      have hfr : (k : ℝ) + Int.fract r = r := by rw [hk]; exact Int.floor_add_fract r
      have : Int.fract r = r - (k : ℝ) := by linarith
      rw [this, hr]
      field_simp
      ring
    have hmul : c * ((m : ℝ) * t) =
        (m : ℝ) * (Int.fract r * (2 * π)) + ((m * k : ℤ) : ℝ) * (2 * π) := by
      have : c * ((m : ℝ) * t) = (m : ℝ) * (c * t) := by ring
      rw [this, hct]
      push_cast
      ring
    rw [hmul, Real.sin_add_int_mul_two_pi]

/-! ## Summability of the remainder

The `x^{-2}` bound of Prop. 4.1(ii) is what makes the remainder series
*absolutely* convergent, and that is what licenses splitting the conditionally
convergent series `∑ Φ(mt)` into a sawtooth and a remainder at all. -/

/-- The remainder series is absolutely convergent.  Only the `x^{-2}` bound is
used, and only for `x` large, so the finitely many small terms are irrelevant. -/
lemma summable_abs_W {t P B₂ X : ℝ} {W : ℝ → ℝ}
    (ht : 1 < t)
    (hW2 : ∀ x : ℝ, X ≤ x → |W x| ≤ B₂ * P / x ^ 2) :
    Summable fun m : ℕ => |W (((m : ℝ) + 1) * t)| := by
  have ht0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  set K : ℕ := ⌈X⌉₊ with hK
  -- comparison series `B₂P/t² · (m+K+1)^{-2}`, summable because `∑ (m+1)^{-2}` is
  have hbase : Summable fun m : ℕ => 1 / (((m : ℝ) + 1) ^ 2) := by
    have h := (summable_nat_add_iff 1).mpr
      (Real.summable_one_div_nat_pow.mpr (by norm_num : 1 < 2))
    refine h.congr fun m => ?_
    push_cast
    ring
  have hcomp : Summable fun m : ℕ => B₂ * P / t ^ 2 * (1 / (((m : ℝ) + 1) ^ 2)) :=
    hbase.mul_left _
  -- the bound, valid for every `m` once the index is shifted past `K`
  rw [← summable_nat_add_iff K]
  refine Summable.of_nonneg_of_le (fun m => abs_nonneg _) (fun m => ?_)
    ((summable_nat_add_iff K).mpr hcomp)
  have hle : X ≤ (((m + K : ℕ) : ℝ) + 1) * t := by
    have h1 : X ≤ (K : ℝ) := Nat.le_ceil X
    have h2 : (K : ℝ) ≤ ((m + K : ℕ) : ℝ) := by push_cast; linarith [Nat.cast_nonneg (α := ℝ) m]
    have h3 : (1:ℝ) ≤ (((m + K : ℕ) : ℝ) + 1) := by
      have : (0:ℝ) ≤ ((m + K : ℕ) : ℝ) := Nat.cast_nonneg _
      linarith
    nlinarith
  have hpos : (0:ℝ) < (((m + K : ℕ) : ℝ) + 1) := by
    have : (0:ℝ) ≤ ((m + K : ℕ) : ℝ) := Nat.cast_nonneg _
    linarith
  calc |W ((((m + K : ℕ) : ℝ) + 1) * t)|
      ≤ B₂ * P / ((((m + K : ℕ) : ℝ) + 1) * t) ^ 2 := hW2 _ hle
    _ = B₂ * P / t ^ 2 * (1 / (((m + K : ℕ) : ℝ) + 1) ^ 2) := by
        rw [mul_pow]; field_simp

/-! ## Theorem 5.1's mechanism -/

/-- **Theorem `thm:q2`, the summation step.**  For every `t > 1` the dilate sum
`∑_{m≥1} Φ(mt)` converges, and

    t |∑_{m≥1} Φ(mt)| ≤ (π/2)|a₁| + t ∑_{m≥1} |W(mt)| .

The `π/2` is the entire content.  Bounding the leading term
`a₁ sin(cmt)/(mt)` termwise gives `|a₁| ∑_m 1/m = +∞`; what makes the sum finite
is `Riemann.Sawtooth.sawtooth_abs_le`, and that lemma is about a *sine*.  Put a
cosine of any size in the leading term and the corresponding quantity is
`-log|2 sin(ct/2)|`, unbounded over `t > 1`
(`Riemann.Sawtooth.tendsto_cos_sum_value_atTop`).

`hsplit` and `hW2` are `dilate-sum.md` §4's definition of `W` and its
Prop. 4.1(ii); neither is formalised here (both rest on Q1). -/
theorem exists_limit_and_bound {c t a₁ P B₂ X : ℝ} {Φ W : ℝ → ℝ}
    (ht : 1 < t)
    (hsplit : ∀ x : ℝ, 1 ≤ x → Φ x = a₁ * Real.sin (c * x) / x + W x)
    (hW2 : ∀ x : ℝ, X ≤ x → |W x| ≤ B₂ * P / x ^ 2) :
    ∃ S : ℝ,
      Tendsto (fun N => ∑ m ∈ range N, Φ (((m : ℝ) + 1) * t)) atTop (𝓝 S) ∧
      t * |S| ≤ π * |a₁| / 2 + t * ∑' m : ℕ, |W (((m : ℝ) + 1) * t)| := by
  have ht0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  obtain ⟨γ, hγ0, hγ2, hγ⟩ := exists_gamma c t
  obtain ⟨Sγ, hSγbd, hSγ⟩ := Sawtooth.sawtooth_abs_le hγ0 hγ2
  have hsumA : Summable fun m : ℕ => |W (((m : ℝ) + 1) * t)| := summable_abs_W ht hW2
  have hsumW : Summable fun m : ℕ => W (((m : ℝ) + 1) * t) := hsumA.of_abs
  set S₂ : ℝ := ∑' m : ℕ, W (((m : ℝ) + 1) * t) with hS₂def
  -- each argument `(m+1)t` is `≥ 1`, so `hsplit` applies at every term
  have harg : ∀ m : ℕ, (1:ℝ) ≤ ((m : ℝ) + 1) * t := by
    intro m
    have h1 : (1:ℝ) ≤ (m : ℝ) + 1 := by
      have : (0:ℝ) ≤ (m : ℝ) := Nat.cast_nonneg _
      linarith
    nlinarith
  -- the leading term, rewritten through `γ`
  have hlead : ∀ m : ℕ,
      a₁ * Real.sin (c * (((m : ℝ) + 1) * t)) / (((m : ℝ) + 1) * t)
        = a₁ / t * (Real.sin (((m : ℝ) + 1) * γ) / ((m : ℝ) + 1)) := by
    intro m
    have hs := hγ (m + 1)
    have hcast : ((m + 1 : ℕ) : ℝ) = (m : ℝ) + 1 := by push_cast; ring
    rw [hcast] at hs
    have hne : ((m : ℝ) + 1) ≠ 0 := by
      have : (0:ℝ) ≤ (m : ℝ) := Nat.cast_nonneg _
      positivity
    rw [hs]
    field_simp
  -- the leading partial sums converge to `(a₁/t) Sγ`
  have hLtend : Tendsto
      (fun N => ∑ m ∈ range N, a₁ * Real.sin (c * (((m : ℝ) + 1) * t)) / (((m : ℝ) + 1) * t))
      atTop (𝓝 (a₁ / t * Sγ)) := by
    have hshift : Tendsto
        (fun N => ∑ n ∈ range (N + 1), Real.sin ((n : ℝ) * γ) / (n : ℝ)) atTop (𝓝 Sγ) :=
      hSγ.comp (tendsto_add_atTop_nat 1)
    have := hshift.const_mul (a₁ / t)
    refine this.congr fun N => ?_
    rw [Finset.mul_sum, Finset.sum_range_succ']
    simp only [Nat.cast_zero, div_zero, mul_zero, add_zero, zero_mul]
    refine Finset.sum_congr rfl fun m _ => ?_
    have hcast : ((m + 1 : ℕ) : ℝ) = (m : ℝ) + 1 := by push_cast; ring
    rw [hcast, hlead m]
  -- add the remainder
  have hRtend : Tendsto (fun N => ∑ m ∈ range N, W (((m : ℝ) + 1) * t)) atTop (𝓝 S₂) :=
    hsumW.hasSum.tendsto_sum_nat
  refine ⟨a₁ / t * Sγ + S₂, ?_, ?_⟩
  · refine (hLtend.add hRtend).congr fun N => ?_
    rw [← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun m _ => (hsplit _ (harg m)).symm
  · have habs : |a₁ / t * Sγ + S₂| ≤ |a₁| / t * (π / 2) + |S₂| := by
      refine le_trans (abs_add_le _ _) ?_
      have h1 : |a₁ / t * Sγ| = |a₁| / t * |Sγ| := by
        rw [abs_mul, abs_div, abs_of_pos ht0]
      have h2 : |a₁| / t * |Sγ| ≤ |a₁| / t * (π / 2) :=
        mul_le_mul_of_nonneg_left hSγbd (by positivity)
      rw [h1]
      linarith
    have hS₂le : |S₂| ≤ ∑' m : ℕ, |W (((m : ℝ) + 1) * t)| := by
      have hnorm : Summable fun m : ℕ => ‖W (((m : ℝ) + 1) * t)‖ := by
        simp only [Real.norm_eq_abs]; exact hsumA
      have h := norm_tsum_le_tsum_norm hnorm
      simp only [Real.norm_eq_abs] at h
      rw [hS₂def]
      exact h
    calc t * |a₁ / t * Sγ + S₂| ≤ t * (|a₁| / t * (π / 2) + |S₂|) :=
          mul_le_mul_of_nonneg_left habs ht0.le
      _ = π * |a₁| / 2 + t * |S₂| := by field_simp
      _ ≤ π * |a₁| / 2 + t * ∑' m : ℕ, |W (((m : ℝ) + 1) * t)| := by
          have := mul_le_mul_of_nonneg_left hS₂le ht0.le
          linarith

/-! ## The explicit constant

`dilate-sum.md` §5 bounds `t ∑_m |W(mt)|` by splitting at `mt = X_*` and using
Prop. 4.1(i) below and (ii) above.  Formalised here with the split taken at the
*index* `⌊X⌋₊` rather than at `mt = X`, which is a coarser split (the low set is
larger, since `mt < X` implies `m < X`) and gives the same constant, because the
low bound is summed against the harmonic sum `harmonic ⌊X⌋₊ ≤ 1 + log X` either
way.  Recorded because it is a deviation from the note's proof, not a
transcription of it. -/

/-- The `m^{-2}` tail, by telescoping `1/(m+1)² ≤ 1/m - 1/(m+1)`.  Sharper than
`Finset.sum_Ioo_inv_sq_le`'s `2/K` and it avoids reindexing. -/
lemma sum_range_inv_sq_shift_le {K : ℕ} (hK : 1 ≤ K) (n : ℕ) :
    ∑ i ∈ range n, 1 / (((K + i : ℕ) : ℝ) + 1) ^ 2 ≤ 1 / (K : ℝ) - 1 / ((K + n : ℕ) : ℝ) := by
  induction n with
  | zero => simp
  | succ n ih =>
      have hKn : (1:ℝ) ≤ ((K + n : ℕ) : ℝ) := by
        have : (1:ℕ) ≤ K + n := le_trans hK (Nat.le_add_right K n)
        exact_mod_cast this
      have hstep : 1 / (((K + n : ℕ) : ℝ) + 1) ^ 2
          ≤ 1 / ((K + n : ℕ) : ℝ) - 1 / ((K + (n + 1) : ℕ) : ℝ) := by
        have hcast : ((K + (n + 1) : ℕ) : ℝ) = ((K + n : ℕ) : ℝ) + 1 := by push_cast; ring
        rw [hcast]
        set a : ℝ := ((K + n : ℕ) : ℝ) with ha
        have h1 : 1 / (a + 1) ^ 2 ≤ 1 / (a * (a + 1)) := by
          refine one_div_le_one_div_of_le (by positivity) ?_
          nlinarith
        have h2 : 1 / a - 1 / (a + 1) = 1 / (a * (a + 1)) := by
          field_simp
          ring
        linarith
      rw [Finset.sum_range_succ]
      linarith [ih]

/-- **The explicit constant of Theorem `thm:q2`.**  `t ∑_{m≥1} |W(mt)|` is bounded
by `B₁P(1 + log X) + 2B₂P/X`, which with the `π|a₁|/2` of
`exists_limit_and_bound` is the paper's `K_P(c)|Φ(1)|`. -/
theorem tsum_abs_le {t P B₁ B₂ X : ℝ} {W : ℝ → ℝ}
    (ht : 1 < t) (hP : 0 ≤ P) (hB₁ : 0 ≤ B₁) (hB₂ : 0 ≤ B₂) (hX : 1 ≤ X)
    (hW1 : ∀ x : ℝ, 1 ≤ x → |W x| ≤ B₁ * P / x)
    (hW2 : ∀ x : ℝ, X ≤ x → |W x| ≤ B₂ * P / x ^ 2) :
    t * ∑' m : ℕ, |W (((m : ℝ) + 1) * t)| ≤ B₁ * P * (1 + Real.log X) + 2 * B₂ * P / X := by
  have ht0 : (0:ℝ) < t := lt_trans zero_lt_one ht
  have hX0 : (0:ℝ) < X := lt_of_lt_of_le zero_lt_one hX
  set M : ℕ := ⌊X⌋₊ with hM
  have hM1 : 1 ≤ M := Nat.one_le_iff_ne_zero.mpr (by
    simpa [hM] using (Nat.floor_pos.mpr hX).ne')
  have hMR : (1:ℝ) ≤ (M : ℝ) := by exact_mod_cast hM1
  have hMX : (M : ℝ) ≤ X := Nat.floor_le hX0.le
  have hXM : X < (M : ℝ) + 1 := by
    have := Nat.lt_floor_add_one X
    simpa [hM] using this
  -- `X ≤ 2M`, which is what turns `1/M` into `2/X`
  have hX2M : X ≤ 2 * (M : ℝ) := by nlinarith
  -- each argument is `≥ 1`
  have harg : ∀ m : ℕ, (1:ℝ) ≤ ((m : ℝ) + 1) * t := by
    intro m
    have h1 : (1:ℝ) ≤ (m : ℝ) + 1 := by
      have : (0:ℝ) ≤ (m : ℝ) := Nat.cast_nonneg _
      linarith
    nlinarith
  -- it suffices to bound every partial sum
  have hkey : ∀ N : ℕ, t * ∑ m ∈ range N, |W (((m : ℝ) + 1) * t)|
      ≤ B₁ * P * (1 + Real.log X) + 2 * B₂ * P / X := by
    intro N
    rw [Finset.mul_sum]
    have hsplit := Finset.sum_filter_add_sum_filter_not (range N) (fun m => m < M)
      (fun m => t * |W (((m : ℝ) + 1) * t)|)
    rw [← hsplit]
    -- low part: `hW1` gives `t|W| ≤ B₁P/(m+1)`, summed to `B₁P · harmonic M`
    have hlow : ∑ m ∈ (range N).filter (fun m => m < M), t * |W (((m : ℝ) + 1) * t)|
        ≤ B₁ * P * (1 + Real.log X) := by
      have hsub : (range N).filter (fun m => m < M) ⊆ range M := by
        intro m hm
        simp only [Finset.mem_filter, Finset.mem_range] at hm ⊢
        exact hm.2
      have hterm : ∀ m ∈ range M, t * |W (((m : ℝ) + 1) * t)| ≤ B₁ * P / ((m : ℝ) + 1) := by
        intro m _
        have hm1 : (0:ℝ) < (m : ℝ) + 1 := by
          have : (0:ℝ) ≤ (m : ℝ) := Nat.cast_nonneg _
          linarith
        have h := hW1 _ (harg m)
        calc t * |W (((m : ℝ) + 1) * t)| ≤ t * (B₁ * P / (((m : ℝ) + 1) * t)) :=
              mul_le_mul_of_nonneg_left h ht0.le
          _ = B₁ * P / ((m : ℝ) + 1) := by field_simp
      have hnn : ∀ m ∈ range M, m ∉ (range N).filter (fun m => m < M) →
          (0:ℝ) ≤ t * |W (((m : ℝ) + 1) * t)| := fun m _ _ => by positivity
      calc ∑ m ∈ (range N).filter (fun m => m < M), t * |W (((m : ℝ) + 1) * t)|
          ≤ ∑ m ∈ range M, t * |W (((m : ℝ) + 1) * t)| :=
            Finset.sum_le_sum_of_subset_of_nonneg hsub hnn
        _ ≤ ∑ m ∈ range M, B₁ * P / ((m : ℝ) + 1) := Finset.sum_le_sum hterm
        _ = B₁ * P * ∑ m ∈ range M, 1 / ((m : ℝ) + 1) := by
            rw [Finset.mul_sum]; exact Finset.sum_congr rfl fun m _ => by ring
        _ ≤ B₁ * P * (1 + Real.log X) := by
            have hharm : ∑ m ∈ range M, 1 / ((m : ℝ) + 1) = ((harmonic M : ℚ) : ℝ) := by
              rw [harmonic]
              push_cast
              exact Finset.sum_congr rfl fun m _ => by rw [one_div]
            rw [hharm]
            exact mul_le_mul_of_nonneg_left (harmonic_floor_le_one_add_log X hX)
              (by positivity)
    -- high part: `hW2` applies because `m ≥ ⌊X⌋₊` and `t > 1` force `(m+1)t > X`
    have hhigh : ∑ m ∈ (range N).filter (fun m => ¬ m < M), t * |W (((m : ℝ) + 1) * t)|
        ≤ 2 * B₂ * P / X := by
      have hset : (range N).filter (fun m => ¬ m < M) = Finset.Ico M N := by
        ext m
        simp only [Finset.mem_filter, Finset.mem_range, Finset.mem_Ico, not_lt]
        omega
      have hterm : ∀ m ∈ Finset.Ico M N, t * |W (((m : ℝ) + 1) * t)|
          ≤ B₂ * P / t * (1 / ((m : ℝ) + 1) ^ 2) := by
        intro m hm
        have hmM : (M : ℝ) ≤ (m : ℝ) := by
          exact_mod_cast (Finset.mem_Ico.mp hm).1
        have hm1 : (0:ℝ) < (m : ℝ) + 1 := by
          have : (0:ℝ) ≤ (m : ℝ) := Nat.cast_nonneg _
          linarith
        have hXle : X ≤ ((m : ℝ) + 1) * t := by nlinarith
        have h := hW2 _ hXle
        calc t * |W (((m : ℝ) + 1) * t)| ≤ t * (B₂ * P / (((m : ℝ) + 1) * t) ^ 2) :=
              mul_le_mul_of_nonneg_left h ht0.le
          _ = B₂ * P / t * (1 / ((m : ℝ) + 1) ^ 2) := by rw [mul_pow]; field_simp
      have htail : ∑ m ∈ Finset.Ico M N, 1 / ((m : ℝ) + 1) ^ 2 ≤ 1 / (M : ℝ) := by
        rw [Finset.sum_Ico_eq_sum_range]
        have h := sum_range_inv_sq_shift_le hM1 (N - M)
        have hnn : (0:ℝ) ≤ 1 / ((M + (N - M) : ℕ) : ℝ) := by positivity
        linarith
      calc ∑ m ∈ (range N).filter (fun m => ¬ m < M), t * |W (((m : ℝ) + 1) * t)|
          = ∑ m ∈ Finset.Ico M N, t * |W (((m : ℝ) + 1) * t)| := by rw [hset]
        _ ≤ ∑ m ∈ Finset.Ico M N, B₂ * P / t * (1 / ((m : ℝ) + 1) ^ 2) :=
            Finset.sum_le_sum hterm
        _ = B₂ * P / t * ∑ m ∈ Finset.Ico M N, 1 / ((m : ℝ) + 1) ^ 2 := by
            rw [Finset.mul_sum]
        _ ≤ B₂ * P / t * (1 / (M : ℝ)) :=
            mul_le_mul_of_nonneg_left htail (by positivity)
        _ ≤ 2 * B₂ * P / X := by
            have hBP : (0:ℝ) ≤ B₂ * P := mul_nonneg hB₂ hP
            have hM0 : (0:ℝ) < (M : ℝ) := by linarith
            have step1 : B₂ * P / t * (1 / (M : ℝ)) ≤ B₂ * P * (1 / (M : ℝ)) := by
              refine mul_le_mul_of_nonneg_right ?_ (by positivity)
              rw [div_le_iff₀ ht0]
              nlinarith
            have step2 : (1:ℝ) / (M : ℝ) ≤ 2 / X := by
              rw [le_div_iff₀ hX0, div_mul_eq_mul_div, div_le_iff₀ hM0]
              linarith
            calc B₂ * P / t * (1 / (M : ℝ)) ≤ B₂ * P * (1 / (M : ℝ)) := step1
              _ ≤ B₂ * P * (2 / X) := mul_le_mul_of_nonneg_left step2 hBP
              _ = 2 * B₂ * P / X := by ring
    linarith
  have hnn : ∀ m : ℕ, (0:ℝ) ≤ |W (((m : ℝ) + 1) * t)| := fun m => abs_nonneg _
  have hbound : ∀ N : ℕ, ∑ m ∈ range N, |W (((m : ℝ) + 1) * t)|
      ≤ (B₁ * P * (1 + Real.log X) + 2 * B₂ * P / X) / t := by
    intro N
    rw [le_div_iff₀ ht0, mul_comm]
    exact hkey N
  have h := Real.tsum_le_of_sum_range_le hnn hbound
  calc t * ∑' m : ℕ, |W (((m : ℝ) + 1) * t)|
      ≤ t * ((B₁ * P * (1 + Real.log X) + 2 * B₂ * P / X) / t) :=
        mul_le_mul_of_nonneg_left h ht0.le
    _ = B₁ * P * (1 + Real.log X) + 2 * B₂ * P / X := by field_simp

/-- **Theorem `thm:q2` (`dilate-sum.md` Thm 5.1), assembled.**  With the two
remainder bounds of Prop. 4.1 and the splitting of §4, the dilate sum converges
for every `t > 1` and

    t |G t| ≤ (π/2)|a₁| + B₁ P (1 + log X) + 2 B₂ P / X ,

which is `K_P(c)|Φ(1)|` with `K_P` the constant of the paper. -/
theorem theorem_q2 {c t a₁ P B₁ B₂ X : ℝ} {Φ W : ℝ → ℝ}
    (ht : 1 < t) (hP : 0 ≤ P) (hB₁ : 0 ≤ B₁) (hB₂ : 0 ≤ B₂) (hX : 1 ≤ X)
    (hsplit : ∀ x : ℝ, 1 ≤ x → Φ x = a₁ * Real.sin (c * x) / x + W x)
    (hW1 : ∀ x : ℝ, 1 ≤ x → |W x| ≤ B₁ * P / x)
    (hW2 : ∀ x : ℝ, X ≤ x → |W x| ≤ B₂ * P / x ^ 2) :
    ∃ S : ℝ,
      Tendsto (fun N => ∑ m ∈ range N, Φ (((m : ℝ) + 1) * t)) atTop (𝓝 S) ∧
      t * |S| ≤ π * |a₁| / 2 + B₁ * P * (1 + Real.log X) + 2 * B₂ * P / X := by
  obtain ⟨S, hS, hb⟩ := exists_limit_and_bound (c := c) ht hsplit hW2
  refine ⟨S, hS, ?_⟩
  have := tsum_abs_le ht hP hB₁ hB₂ hX hW1 hW2
  linarith

end Riemann.DilateSum
