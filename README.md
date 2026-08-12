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
anywhere. Build with `pdflatex positivity-obstruction.tex` (three passes). It
now proves, unconditionally, that
\(\limsup_{\mu\to\infty}\mu^{-1}\log s(\mu)\le-4\pi\), quantitatively
\(s(\mu)=O(\mu^{21/2}\log^3\mu\,e^{-4\pi\mu})\) — the first six notes assemble
the picture and the last five are the chain that closes it. The one ingredient
proved by nobody here is Dunster 2017 eq. (124)+(107), whose standing hypothesis
is exactly our regime; it is named in the paper's own voice at the point of use
and is gap **G13**. Note also what is *not* claimed: hypothesis (H1) as printed
in the first draft was **bypassed rather than proved** — its \(\|r\|^2\)
normalisation is ruled out as a target of proof — so "H1 is proved" is the
convenient sentence and it is wrong. Its thesis is that the whole prolate mechanism is invariant under
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
- `h1-mean-value.md` — attacks the one named open analytic problem the above
  produce: the mean-value bound over the zeros, called H1, that makes the
  \(-4\pi\) upper bound conditional. Does **not** prove it. Finds that its name is
  wrong — neither hypothesis of Plancherel–Pólya holds, and the first fails
  structurally, since the spill is non-compactly supported *because* it is a
  spill — and that the zeros are not the obstruction: Riemann–von Mangoldt, the
  classical zero-free region and subharmonicity discharge the zeta side
  unconditionally, leaving a weighted \(L^2\) tail bound for a prolate function
  outside its interval, which also absorbs the companion gap. Proves half of what
  remains, in the regime that applies here and by a three-line Sturm argument:
  \(|\Phi_n(x)|\le|\Phi_n(1)|\) for \(x\ge1\) when \(\chi_n<c^2\). Checks the
  published off-band results against our configuration and finds their hypothesis
  is the negation of ours, so they cannot be borrowed. Records an observed
  identity, \(\Phi_n(1)^2=c(1-\Lambda_n)(1-(2n+1)/(4c)+O(c^{-2}))\), which is what
  calibrates the constant. The residue is stated as an ODE connection problem at
  the band edge — which `band-edge-connection.md` below shows it is not.
  Everything in it is sign-blind, as a statement about \(\sum|\cdot|^2\) must be.
- `band-edge-connection.md` — **proves** the item the above calls "the whole
  remaining content": \(x|\Phi_{n,c}(x)|\le K(c)|\Phi_{n,c}(1)|\) for \(x\ge1\)
  whenever \(\chi_n<c^2\), with \(K(c)=2^{3/4}e^{E(c)}\) *bounded* rather than
  merely subexponential, independent of the index, and decreasing to
  \(2^{3/4}=1.6818\). Along the way it refutes that note's own diagnosis: the
  missing step is **not** a connection through the regular singular point
  \(x=1\), because the factor \(x\) is worth nothing on a bounded interval, so
  the asymptotic argument may start at \(x=\sqrt2\) with its initial amplitude
  supplied by the Sturm lemma — the lemma *is* the connection. What makes it
  close is that \(\chi_n<c^2\) says exactly that there is no turning point
  outside the band, so the phase advances at rate at least \(c\) and one
  integration by parts costs \(O(1/c)\). Records, as observed and not proved,
  that the *sharp* constant is \(O(c^{-1/2})\) and that recovering it does need
  the band-edge connection, which is Bessel of order zero. Does **not** prove H1:
  the sum over dilates, the two flagged steps and H0 are all untouched.
  Sign-blind throughout; it contains no zeta function at all.
- `dilate-sum.md` — **proves** the item the two above leave as the only substantive
  obstacle: the passage from the single-term bound to the sum over dilates,
  \(\sup_{t>1}t|\sum_{m\ge1}\Phi_n(mt)|\le K_P(c)|\Phi_n(1)|\) with
  \(K_P(c)=O(\log c)\). Refutes the previous note's diagnosis of it, which was that
  the off-band remainder had to be made small: the divergence is harmonic, so what
  is needed is **one more power of \(x\), not one less power of \(e^{c}\)** — a
  remainder of exactly the size \(|\Phi(1)|\) is harmless once it decays like
  \(x^{-2}\), and that follows from the single-term bound by one application of
  variation of parameters in the Liouville form. Shows the theorem turns on the
  leading off-band term being a **pure sine**, which is a quantisation statement and
  not an ODE one: a solution of the same equation with a cosine has
  \(\sup_t t|G(t)|=\infty\), so no ODE-only argument could work. Removes the
  computational blocker the previous notes reported by putting the sum on the other
  side of a Poisson summation, where it becomes \(\lfloor\mu t\rfloor+1\) evaluations
  *inside* the interval instead of infinitely many outside it. Reports a latent sign
  defect found in the shared Bessel routine, which is invisible in the moduli the
  earlier notes report and fatal here. Does **not** prove H1: the two flagged steps
  and H0 remain. Sign-blind throughout.
- `q3-log-weight-and-edge.md` — writes out the two steps the first of these notes
  calls routine, and finds that **neither is what that note says it is**. The
  \(\log^3\)-weight step rests on a false premise: the spill is not smooth to the
  right of one jump, it jumps at \(u=\lambda/N\) for *every* integer \(N>\mu\) — the
  same sawtooth that makes `dilate-sum.md` work, so **two sections of one note
  contradict each other**. The edge is one-sided, and does not converge in the order
  proposed, because the zero-free region puts it where the \(\log^3\) weight is
  already large; the two steps are not independent and cannot be costed separately.
  Closes both anyway, by a different route: truncate the zero sum at \(e^{4\pi\mu}\),
  freeze the weight below it, and use a **proved** lower bound on \(\Phi(1)^2\) that
  follows from the single-term bound. No fractional Sobolev theory anywhere,
  \(\Xi=O(\mu^{9/2}\log^3\mu)\). Insists on the precise statement: it is estimate
  (4.3) that is proved, **not (H1) as written**. Sign-blind throughout.
- `h0-lower-bound.md` — closes the last condition, and the note it inherits named
  the wrong object: (H0) is **not** a mean value of \(|\zeta(1/2+it)|^2\) — *there
  is no zeta in it at all*. \(\|g\|^2\) is its own integral over its own range, and
  is bounded below by the integral over any fixed compact window, on which
  \(\mathcal E\phi\) is a finite sum of **on-band** prolate values. What (H0)
  requires is that the prolate vector does not degenerate, and it does not:
  \(\|g\|^2\to\|\mathcal E\phi_\infty\|^2=0.219247199549\ldots\) with
  \(\phi_\infty=\sqrt{8/11}(h_4-\sqrt{3/8}h_0)\), which is `start.tex:39`'s own
  vector in its Hermite limit. So **the \(-4\pi\) upper bound is unconditional**.
  One input is imported and proved by nobody here — Dunster 2017
  (arXiv:1601.00699) eq. (124)+(107), whose standing hypothesis \(\lambda<0\) is
  exactly our \(\chi<c^2\), the regime this chain has needed throughout and the
  negation of the one the neighbouring literature works in. Its appendix supplies
  the conversion the previous note had left sketched, at a cost of \(\mu^{3/2}\);
  anyone printing "unconditional" is quoting that appendix too. Sign-blind
  throughout, and the matching lower bound is still RH.
- `dunster-check.md` — the second reader on that one imported input. Reads (124) and
  (107) back out of the arXiv LaTeX and evaluates **both sides independently** at
  \(c=4\pi\ldots24\pi\) and prolate indices \(n=0,2,4,6,8\). Both hold: the
  quantity (124) bounds, times \(c/\log c\), stays bounded at every index, and
  (107) is pinned to its next coefficient,
  \(\chi_n=(2n+1)c-\frac{(2n+1)^2+5}{8}+O(1/c)\). Two corrections. Dunster's
  standing hypothesis is not \(\lambda<0\) but his (29), \(\sqrt{\chi_n}/c\le
  \sigma_0<1\) with \(\sigma_0\) fixed; and at \((\mu,n)=(2,8)\) that **fails**
  — \(\sigma=1.0199\), the threshold being \(\mu^*=2.1169\) — the same cell
  `verify_q1.py` already flags for Q1. Theorem 6.1 is a \(\lambda\to\infty\) limit
  at fixed \(n\) and is untouched; the sentence describing the hypothesis is not.
  Also: (107) is itself a citation (Arscott [1, p. 186]), so the chain is two deep,
  not one. **A numerical check is not a proof** — the import stays external, it is
  now tested. Sign-blind throughout.

`s3-reduction-audit.md`, `s3-sign-blindness.md` and `semilocal-gap.md` have companion
`verify_*.py` scripts (numpy; `semilocal-gap.md` has two); `index-convention.md`,
`deficit-repair.md`, `prolate-rate.md`, `h1-mean-value.md`,
`band-edge-connection.md`, `dilate-sum.md`, `q3-log-weight-and-edge.md` and
`h0-lower-bound.md` and `dunster-check.md` have ones using
`mpmath` in arbitrary precision and no numpy; `independent-recheck.md`'s uses the Python standard
library alone, which is the point of it;
`signed-geometry-proposals.md` and `citation-audit.md` are
structural and have none. The first three notes were written offline and say so;
`citation-audit.md` is the pass that checks them, `index-convention.md` closes one item
it left open and `semilocal-gap.md` closes another.

The specific research target is still being chosen. Expect the contents to
change substantially.

## License

MIT — see [LICENSE](LICENSE).
