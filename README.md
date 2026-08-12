# riemann

Work on the Riemann Hypothesis via Connes' spectral approach.

## Goal

Reach the substance of a proof of RH if that turns out to be possible. Failing
that, produce a substantial, publishable improvement on Connes' work — a
sharpening of the positivity obstruction that stands on its own.

## Status

Early. The repository holds two working documents.

- `start.tex` records where the program stands: the setup, the reductions
  attempted so far, the routes that did not work, and a candidate next lemma.
- `s3.tex` restates the reductions the \(S^3\) picture is hoped to supply, in
  proposition form. Its own closing paragraph is the accurate summary: the
  final item is a reduction, not an estimate, and it hands the problem back to
  the arithmetic trace formula.

Nothing in either is a finished result, and no result is claimed here.

`notes/` holds audits of those documents. They do not modify the `.tex` files and
cite them by line.

- `s3-reduction-audit.md` — audits `s3.tex` item (iii) and ranks candidate
  \(S^3\) reductions. Finds that every \(S^3\) statement examined restates a
  classical Slepian statement, and sharpens items (ii) and (iii) to exact
  constants.
- `s3-sign-blindness.md` — asks whether the \(S^3\) geometry can determine the
  sign of the remaining coefficient. Finds that it cannot as constructed: the
  whole chain in `s3.tex` is invariant under \(W_\lambda \mapsto -W_\lambda\).
- `signed-geometry-proposals.md` — proposes alternative geometries in which the
  arithmetic sign flows through to the geometry, ranked. Argues the missing
  ingredient is a product and an involution rather than a higher-dimensional
  manifold, and reports which of its own candidates are sign-blind.
- `citation-audit.md` — verifies the attributions in the other three notes against
  the sources, and settles where this work sits relative to the published
  literature. Finds that the objects of `start.tex` §§1,3 are those of
  Connes–Consani, *Spectral triples and \(\zeta\)-cycles* (2023), in that paper's
  own notation.

The first two have a companion `verify_*.py` (numpy) reproducing their numbers;
the last two are structural and have none. The first three were written offline
and say so; `citation-audit.md` is the pass that checks them.

The specific research target is still being chosen. Expect the contents to
change substantially.

## License

MIT — see [LICENSE](LICENSE).
