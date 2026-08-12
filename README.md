# riemann

Work on the Riemann Hypothesis via Connes' spectral approach.

## Goal

Reach the substance of a proof of RH if that turns out to be possible. Failing
that, produce a substantial, publishable improvement on Connes' work — a
sharpening of the positivity obstruction that stands on its own.

## Status

`paper/positivity-obstruction.tex` is a **draft** assembling the notes below into
one standalone document: *The prolate mechanism is sign-blind — a sharpening of
the positivity obstruction*. It is not a submission and nothing has been sent
anywhere. Build with `pdflatex positivity-obstruction.tex` (three passes; 27
pages). Its thesis is that the whole prolate mechanism is invariant under
\(QW_\lambda \mapsto -QW_\lambda\), so it explains why the smallest eigenvalue is
minuscule and says nothing about why it is positive — which is what forces the
missing lower bound to carry the arithmetic content, and that content is RH. It
carries a status word (proved / announced / observed / conjectural) and an
attribution on every load-bearing claim, a table of routes closed with their
thresholds, and the house rule applied to itself. It also carries the
independent recheck below: what the second implementation corroborates, what it
cannot — both implementations read the same paper — and the erratum in the
literature that no result here depends on.

Early. The repository also holds two working documents.

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
- `index-convention.md` — settles which prolate mode the corpus's \(h_{4,\lambda}\)
  denotes, an ambiguity the citation audit left open and on which every constant in
  `s3-reduction-audit.md` depends. Finds prolate index 4, and finds that the identity
  at `start.tex:180-181` cannot decide it: in arbitrary precision that identity holds
  exactly for every mode \(\equiv 0 \bmod 4\).
- `semilocal-gap.md` — the branch the corpus's \(QW_\lambda\) lives in is the one
  whose theorem does not exist. Names, ingredient by ingredient, what the proved
  archimedean argument supplies and what a finite place lacks: the sign there comes
  from one compression of a projection, and is paid for with a diagonalisation
  (Slepian–Pollak) that has no semilocal counterpart. Finds that the prime terms are
  *exactly* indefinite, that place-by-place positivity fails, and that the corpus's
  central unresolved estimate is the bridge quantity across that gap — and is also,
  in Connes' own 2026 survey, a published observation. Its appendix §9 records the
  second candidate semilocal prolate operator, deferred by Connes–Consani–Moscovici
  in 2023, as **not having appeared as of 2026-08-12**, and describes the search that
  looked, so the negative can be told apart from nobody having checked. Its appendix
  §10 settles whether the failure of archimedean-only positivity is a theorem: it is
  not — **no theorem asserts it**, and §10.1 says where that was looked for — but it
  is not an artefact either, because §10.2 rebuilds Connes–Consani's computation from
  the explicit formula and matches it on all five numbers it reports, including a
  crossing at \(\mu\approx2.271\) that appears in their own prose. §10.3 gives an
  explicit test function on which the archimedean form is negative, and the reason it
  had to be: the Weil density \(2\theta'(t)/2\pi\) is negative on \(|t|<6.29\).
- `deficit-repair.md` — quantifies, past that threshold, the archimedean deficit
  against what the primes supply. Finds that the deficit is *bounded*, uniformly in
  \(\mu\), by \(\log\pi-\psi(1/4)=5.3721834\ldots\) and saturates there; that on the
  archimedean worst direction the primes over-repair, but by a relative margin that
  closes (\(R/D\) falls from \(1.68\) to \(1.015\) between \(\mu=3\) and \(\mu=20\));
  and that positivity is nevertheless decided on a third direction, the near-radical
  one, where the archimedean contribution is *positive*, the primes *negative*, and
  the two agree to about \(5.2\) decimal digits per unit of \(\mu\) — a rate
  consistent with \(4\pi/\log 10=5.4575\), the constant behind a decay
  Connes–Consani plot as a figure and never name (narrowed by `prolate-rate.md`:
  true of arXiv:2106.01715, but the rate, the power and the constant are named in
  Connes' Feb 2026 survey, and are his). The resulting statement — a proof
  must exhibit an exact-to-\(e^{-4\pi\mu}\) cancellation between two quantities of
  size \(\approx0.025\log\mu\), with every prime power below \(\mu\) individually
  indispensable — is a sharpening of the positivity obstruction that does not depend
  on the semilocal theorem.
- `prolate-rate.md` — asks whether that decay is genuinely governed by a prolate
  concentration defect, and if so which one. Finds that it is, but at prolate index
  **4**, not index 0: the index is forced by the domain \(f(0)=\widehat f(0)=0\) of
  Connes' summation map together with the finite-Fourier phase, and it is
  Connes–Consani's own \(\phi_2\). Against the index-0 defect the ratio is
  \(5\times10^{8}\) to \(2.8\times10^{10}\) and grows by a factor \(56\); against the
  index-4 defect it is \(7.6\) to \(13.0\), and after the truncation bias is
  extrapolated away it has no trend left. Records that the rate \(4\pi\) itself
  **cannot discriminate** — Fuchs' \(e^{-2c}\) does not depend on the index, so every
  candidate passes that test — and that the power \(9/2\) and the constant, which do
  discriminate, are already published in Connes' 2026 survey. Carries Connes–Consani's
  construction to an identity: the Weil form at the prolate vector *is* the Weil form
  of the part that falls outside the window. And finds that the rate cannot be made a
  theorem: a rate is two-sided, and its lower half is a positive lower bound on the
  Weil form for all \(\lambda\), which is equivalent to RH.
- `independent-recheck.md` — rechecks the numerics of the two notes above from the
  definitions, by a second implementation written without reading their scripts and
  sharing with them no arithmetic library, no transcendental function and no
  eigensolver. Reproduces every published number to every digit printed. Corrects
  three cosmetic cells and finds one erratum in the literature: Connes–Consani's own
  printed closed form for the even-sector boundary term is a factor \(2\) smaller
  than the table it is derived from — an error that does not reach this repository,
  because neither implementation uses that formula. Tests the one identity both
  implementations had taken on trust, the normalisation behind the \(5.3721834\)
  bound, and confirms it to 18 digits. States what the exercise does *not*
  establish: both implementations read the same paper, and a shared misreading is
  invisible to it.

`s3-reduction-audit.md`, `s3-sign-blindness.md` and `semilocal-gap.md` have companion
`verify_*.py` scripts (numpy; `semilocal-gap.md` has two); `index-convention.md`,
`deficit-repair.md` and `prolate-rate.md` have ones using `mpmath` in arbitrary
precision and no numpy; `independent-recheck.md`'s uses the Python standard
library alone, which is the point of it;
`signed-geometry-proposals.md` and `citation-audit.md` are
structural and have none. The first three notes were written offline and say so;
`citation-audit.md` is the pass that checks them, `index-convention.md` closes one item
it left open and `semilocal-gap.md` closes another.

The specific research target is still being chosen. Expect the contents to
change substantially.

## License

MIT — see [LICENSE](LICENSE).
