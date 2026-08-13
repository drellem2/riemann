/-
Axiom audit.  Every result claimed as formalised is listed here; `#print axioms`
must report only `propext`, `Classical.choice`, `Quot.sound` for each — in
particular never `sorryAx`.

Run `lake build Riemann.Axioms` and read the output; `scripts/check.sh`
does this and greps for `sorryAx`.
-/
import Riemann.Sturm
import Riemann.BandEdge
import Riemann.Sawtooth
import Riemann.DilateSum
import Riemann.Remainder
import Riemann.Assembly

namespace Riemann.Prolate

-- Lemma 5.1 and its components
#print axioms Riemann.Prolate.qq_pos
#print axioms Riemann.Prolate.DD_pos
#print axioms Riemann.Prolate.DD'_pos
#print axioms Riemann.Prolate.hasDerivAt_DD
#print axioms Riemann.Prolate.isSolution_of_secondOrder
#print axioms Riemann.Prolate.hasDerivAt_V
#print axioms Riemann.Prolate.antitoneOn_V
#print axioms Riemann.Prolate.sq_le_V
#print axioms Riemann.Prolate.tendsto_ratio
#print axioms Riemann.Prolate.tendsto_V
#print axioms Riemann.Prolate.abs_le_abs_one
#print axioms Riemann.Prolate.V_le_sq_one

-- Lemmas 3.1 and 4.1
#print axioms Riemann.Prolate.sq_kk
#print axioms Riemann.Prolate.lt_kk
#print axioms Riemann.Prolate.uu_le
#print axioms Riemann.Prolate.vv_le
#print axioms Riemann.Prolate.ff_le
#print axioms Riemann.Prolate.hasDerivAt_uu
#print axioms Riemann.Prolate.hasDerivAt_vv
#print axioms Riemann.Prolate.hasDerivAt_ff
#print axioms Riemann.Prolate.abs_deriv_ff_le
#print axioms Riemann.Prolate.hasDerivAt_kk
#print axioms Riemann.Prolate.abs_deriv_kk_le
#print axioms Riemann.Prolate.abs_deriv_ff_le'
#print axioms Riemann.Prolate.abs_deriv_kk_le'
#print axioms Riemann.Prolate.phase_speed_lower

end Riemann.Prolate

namespace Riemann.Sawtooth

-- The quantisation dichotomy (Q2's load-bearing line, `dilate-sum.md` §3)
#print axioms Riemann.Sawtooth.norm_w
#print axioms Riemann.Sawtooth.sin_half_pos
#print axioms Riemann.Sawtooth.cos_eq_half
#print axioms Riemann.Sawtooth.sin_eq_half
#print axioms Riemann.Sawtooth.one_sub_w_re
#print axioms Riemann.Sawtooth.one_sub_w_ne_zero
#print axioms Riemann.Sawtooth.w_ne_one
#print axioms Riemann.Sawtooth.one_sub_w_eq_exp
#print axioms Riemann.Sawtooth.neg_log_one_sub_w
#print axioms Riemann.Sawtooth.norm_geom_sum_le
#print axioms Riemann.Sawtooth.cauchySeq_partial
#print axioms Riemann.Sawtooth.tendsto_partial_sum
#print axioms Riemann.Sawtooth.pow_div_re_im
#print axioms Riemann.Sawtooth.tendsto_sin_sum
#print axioms Riemann.Sawtooth.tendsto_cos_sum
#print axioms Riemann.Sawtooth.sawtooth_abs_le
#print axioms Riemann.Sawtooth.tendsto_cos_sum_value_atTop

end Riemann.Sawtooth

namespace Riemann.DilateSum

-- Theorem `thm:q2` (`dilate-sum.md` Thm 5.1), given Prop. 4.1 as hypotheses
#print axioms Riemann.DilateSum.exists_gamma
#print axioms Riemann.DilateSum.summable_abs_W
#print axioms Riemann.DilateSum.exists_limit_and_bound
#print axioms Riemann.DilateSum.sum_range_inv_sq_shift_le
#print axioms Riemann.DilateSum.tsum_abs_le
#print axioms Riemann.DilateSum.theorem_q2

end Riemann.DilateSum

namespace Riemann.Remainder

-- Lemmas 3.1 and 3.2 and Proposition 4.1 of `dilate-sum.md`, given Q1 and Lemma 3.3
-- (`printed_potential_not_deriv` is the refutation of Lemma 3.1's printed potential)
#print axioms Riemann.Remainder.rt_nonneg
#print axioms Riemann.Remainder.rt_pos
#print axioms Riemann.Remainder.rt_sq
#print axioms Riemann.Remainder.rt_le
#print axioms Riemann.Remainder.hasDerivAt_rt
#print axioms Riemann.Remainder.hasDerivAt_uu
#print axioms Riemann.Remainder.hasDerivAt_uu'
#print axioms Riemann.Remainder.printed_potential_not_deriv
#print axioms Riemann.Remainder.al_add_be
#print axioms Riemann.Remainder.hasDerivAt_sin_mul
#print axioms Riemann.Remainder.hasDerivAt_cos_mul
#print axioms Riemann.Remainder.hasDerivAt_al
#print axioms Riemann.Remainder.hasDerivAt_be
#print axioms Riemann.Remainder.MM_nonneg
#print axioms Riemann.Remainder.hasDerivAt_MM
#print axioms Riemann.Remainder.eps_nonneg
#print axioms Riemann.Remainder.eps_le_deriv_MM
#print axioms Riemann.Remainder.MM_le
#print axioms Riemann.Remainder.abs_sub_le_of_deriv_le
#print axioms Riemann.Remainder.abs_uu_le
#print axioms Riemann.Remainder.abs_sub_al_le
#print axioms Riemann.Remainder.abs_sub_be_le
#print axioms Riemann.Remainder.tail_le
#print axioms Riemann.Remainder.prop41_i
#print axioms Riemann.Remainder.prop41_ii
#print axioms Riemann.Remainder.theorem_q2_of_prolate

end Riemann.Remainder

namespace Riemann.Assembly

-- Corollary `cor:upper` and the `limsup` half of Theorem `thm:main`
#print axioms Riemann.Assembly.tendsto_log_div_atTop
#print axioms Riemann.Assembly.Subexp.of_tendsto_pos
#print axioms Riemann.Assembly.Subexp.const
#print axioms Riemann.Assembly.Subexp.of_sandwich
#print axioms Riemann.Assembly.Subexp.div
#print axioms Riemann.Assembly.tendsto_logRate_mul_exp
#print axioms Riemann.Assembly.logRate_le_aux
#print axioms Riemann.Assembly.eventually_log_le
#print axioms Riemann.Assembly.limsup_logRate_le
#print axioms Riemann.Assembly.eventually_log_le_neg_four_pi
#print axioms Riemann.Assembly.limsup_le_neg_four_pi
#print axioms Riemann.Assembly.eventually_log_bracket
#print axioms Riemann.Assembly.subexp_paper_Xi
#print axioms Riemann.Assembly.subexp_paper_prefactor
#print axioms Riemann.Assembly.eventually_log_le_at_paper_exponents
#print axioms Riemann.Assembly.limsup_le_neg_four_pi_at_paper_exponents

end Riemann.Assembly
