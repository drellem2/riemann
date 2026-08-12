/-
Axiom audit.  Every result claimed as formalised is listed here; `#print axioms`
must report only `propext`, `Classical.choice`, `Quot.sound` for each — in
particular never `sorryAx`.

Run `lake build Riemann.Axioms` and read the output; `scripts/check.sh`
does this and greps for `sorryAx`.
-/
import Riemann.Sturm
import Riemann.BandEdge

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
