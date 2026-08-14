# riemann

[![lean](https://github.com/drellem2/riemann/actions/workflows/lean.yml/badge.svg?branch=main)](https://github.com/drellem2/riemann/actions/workflows/lean.yml?query=branch%3Amain)
[![verifiers](https://github.com/drellem2/riemann/actions/workflows/verifiers.yml/badge.svg?branch=main)](https://github.com/drellem2/riemann/actions/workflows/verifiers.yml?query=branch%3Amain)
[![paper](https://github.com/drellem2/riemann/actions/workflows/paper.yml/badge.svg?branch=main)](https://github.com/drellem2/riemann/actions/workflows/paper.yml?query=branch%3Amain)

Work on the Riemann Hypothesis via Connes' spectral approach.

Everything here is agent-produced. The three badges are the part a stranger can
check without taking anyone's word for it: **lean** re-runs the Lean build, the
`sorry` grep and the axiom audit on a clean machine, **verifiers** re-runs
the numerical scripts, and **paper** builds the LaTeX documents from scratch.
What they do and do not cover is set out under
[Continuous integration](#continuous-integration) — read that before reading a
green tick as more than it is.

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
- `sonin-trace.md` — how big the Sonin trace is, which nobody had asked. It is the
  only object in Connes–Consani's archimedean theorem that carries a sign, and it is
  computable: their own Theorem `devil` gives
  \(\operatorname{tr}(\vartheta(f)\mathbf S)=W_\infty(f)+\int f\epsilon\,d^*\rho\)
  with \(\epsilon\) an explicit prolate series, so the gap in their Theorem 1 is exactly
  \(-E\) and the theorem is one line about a quadratic form. Rebuilds \(\epsilon\) and
  reproduces all five of their printed anchors for it. Finds that the trace is the same
  order as the Weil functional (73% of it on the corpus's two-mode prolate vector, flat
  in \(\mu\)), that its floor decays at \(-3.06\) per unit \(\mu\) against the corpus's
  \(-4\pi=-12.57\), and that the \(\epsilon\) apparatus lives at a **fixed** bandwidth
  \(c=2\pi\) while the corpus's lives at \(c=2\pi\mu\) — so "our \(\lambda\) is their Sonin
  cutoff" is true of the 2023 paper and false of the 2021 theorem. Produces three
  statements that are **not** sign-blind, where the corpus had none.
- `sonin-margin.md` — the sequel that retires `sonin-trace.md`'s central number. The
  \(8.7\times10^{-5}\) is not a margin: \(-E\) is compact, so its eigenvalues accumulate
  at \(0\), and the smallest eigenvalue at \(N\) cosine modes is
  \(\epsilon'(1^+)L^2/2\pi^2N^2\) — the closed form reproduces all eight printed rows at
  \(N=40,80,160\), twenty-four cells within \(0.15\%\). The minimising direction is the
  top basis vector. It also finds and fixes a wrong endpoint in that script's second
  vanishing condition, which no output of it could see. What **is** truncation-stable is
  the inertia, and by it Connes–Consani's Theorem 1 holds past its stated
  \(\mu\le2\), is *false* past that, and each further condition buys a fixed factor in
  the support, for a reason readable off the symbol \(\hat\epsilon\). Four statements
  that are not sign-blind. **Two of its numbers are corrected by `sonin-ceiling.md`**:
  its \(\mu_c(k)\) are the even block only, so "holds to \(\mu=6.17\), three times the
  hypothesis" is \(\mu=2.75\) and a factor \(1.38\), and "one condition suffices at
  \(\mu\le2\)" is false. Read the two together.
- `sonin-ceiling.md` — makes `sonin-margin.md`'s closing one-liner a theorem, and finds
  what it was resting on. **Theorem A**: if \(\hat g\) is required to vanish at any
  \(k\) points of \(\mathbb C\) — which is what \(\hat g(0)=\hat g(i/2)=0\) is — then
  \(\hat g=P\hat\phi\) with \(P\) the vanishing polynomial and \(\phi\) a scaled bump is
  admissible by construction, and dominated convergence gives \(E(g)>0\) for all large
  support. **So the archimedean route has a ceiling at every codimension, and the only
  inputs are \(\hat\epsilon(0)>0\) and integrability.** Both are then supplied: the
  asymptotic \(\epsilon(\rho)\sqrt\rho\to1\) that `sonin-margin.md` marked unanchored is
  derived (the constant is the finite-Fourier kernel's spectral expansion at the origin,
  and a factor two in Connes–Consani's normalisation), and \(\hat\epsilon(0)\) is given a
  closed form \(2\sum\lambda(n)A_n^2/(1+\lambda(n))\) by Mellin inversion at the
  self-dual point — which needs neither \(\epsilon>0\) pointwise (never proved here)
  nor that asymptotic. The rate is a Szegő density: \(\log\mu_c(k)\le\Lambda(k)\sim\pi
  k/t_0\), so `sonin-margin.md`'s constant was never \(25\%\) out — it bounds. And the
  cosine basis every script here uses is the **even block**: adding the odd one moves
  \(\mu_c(2)\) from \(6.17\) to \(2.75\) and \(\mu_c(1)\) below \(2\). Three statements
  that are not sign-blind, two of them corrections.
- `eps-hat-deficit.md` — is \(\hat\epsilon(0)\) the same constant as `thm:deficit`'s
  \(-2\vartheta'(0)=\log\pi-\psi(\tfrac14)\)? The two printed decimals agree to eight
  digits. **No**: at 30 digits they part at the ninth, \(5.372183435911\ldots\) against
  \(5.372183419225\ldots\), a gap of \(1.67\times10^{-8}\) that survives every
  truncation. But the **inequality** is a theorem. The symbol of Connes–Consani's trace
  is \(\sigma_S=2\vartheta'+\hat\epsilon\), and \(\mathbf S=\mathbf S^*=\mathbf S^2\)
  makes it \(\ge0\), so \(\hat\epsilon(0)\ge\log\pi-\psi(\tfrac14)>0\) —
  **`sonin-ceiling.md`'s Theorem A now rests on a proved theorem and a named constant,
  not on a computation.** The eight digits are not luck either: at the square \(S(a,a)\)
  the gap is \(2\log a+\delta\) with \(\delta\) exponentially small, and \(a=1\) is
  where \(\log(\text{area})\) vanishes. And "\(\sigma^{\rm arch}\) is bounded below" and
  "\(-E\) is indefinite at low frequency" turn out to be one inequality read from its
  two sides, not two facts in tension.
- `statement-defects.md` — method, not mathematics, and the shortest note here. Every
  formalisation run so far has found the same class of defect: **the printed statement
  does not match the argument beneath it** — a hypothesis doing two jobs, a hypothesis
  omitted, a formula that is false — while everything derived from it was correct, so
  nothing downstream ever went red and no instrument complained. Records the class, and
  the two practices that caught the last one: run a cheap independent instrument before
  the expensive one, and machine-check the claim that nothing downstream moves rather
  than arguing it. It sits beside the house rule as the project's second standing check.

`s3-reduction-audit.md`, `s3-sign-blindness.md`, `semilocal-gap.md`,
`sonin-trace.md`, `sonin-margin.md` and `sonin-ceiling.md` have companion
`verify_*.py` scripts (numpy; `semilocal-gap.md` has two); `index-convention.md`,
`deficit-repair.md`, `prolate-rate.md`, `h1-mean-value.md`,
`band-edge-connection.md`, `dilate-sum.md`, `q3-log-weight-and-edge.md`,
`eps-hat-deficit.md` and
`h0-lower-bound.md` and `dunster-check.md` have ones using
`mpmath` in arbitrary precision and no numpy; `independent-recheck.md`'s uses the Python standard
library alone, which is the point of it;
`signed-geometry-proposals.md` and `statement-defects.md` are structural and have none,
and `citation-audit.md` is too
except for one `mpmath` check (its §7 item U8). The first three notes were written offline and say so;
`citation-audit.md` is the pass that checks them, `index-convention.md` closes one item
it left open and `semilocal-gap.md` closes another.

The specific research target is still being chosen. Expect the contents to
change substantially.

## Continuous integration

Three GitHub Actions workflows run on every pull request, and on every push to
`main` that changes anything outside `docs/**`. They re-run checks that already
existed in this repository; they do not add new ones. Nothing here is a proof of
anything — it is evidence that the artefacts still do what the notes say they
do, produced by a machine that is not the one that wrote them.

### One run per sha on `main`, and none for docs-only pushes

Each push to `main` gets its **own** concurrency group, keyed on the sha, so no
run can displace another and every commit that changes code carries its own
verdict. Before 2026-08-14 this was not true and the record had holes in it:
GitHub permits only one *pending* run per group, so a second push landing while
a run was in flight evicted the first from the queue before it started. It
happened to `7314936`, which was cancelled ten seconds after it was created with
zero jobs run, and at fourteen merges a day it was not rare. A displaced run
leaves a `cancelled` row that reads exactly like a deliberate cancellation, so
the holes were not visible from the run list. Pull requests still coalesce under
a shared group — a superseded branch push has no independent value.

The other half is that `docs/**` pushes no longer open runs at all. Regenerating
`docs/roadmap.md` is a five-line edit and it was building Lean, building the
paper and running nineteen verifier jobs several times a day, each of those runs
able to evict a merge's. The filter is `docs/**` and not `**.md` on purpose:
`notes/*.md` is the corpus and this file records which verifier scripts run on
reduced grids, so a change to either is a change CI should re-run. It applies to
the `push` trigger only, so a docs-only *pull request* still gets all three
checks.

### `lean` — the Lean development

[`.github/workflows/lean.yml`](.github/workflows/lean.yml) runs
[`lean/scripts/check.sh`](lean/scripts/check.sh) unmodified. That script builds
the development, greps the sources for `sorry`, and runs the axiom audit; it
exits non-zero if the build fails, if `sorry` appears, or if any result depends
on `sorryAx`. A green tick means the log ends in

```
check.sh: OK — 91 results, none depending on sorryAx
```

**mathlib is never compiled from source.** The workflow uses
[`leanprover/lean-action`](https://github.com/leanprover/lean-action), which
installs the pinned toolchain (`lean/lean-toolchain`) and runs `lake exe cache
get` to fetch prebuilt oleans for the pinned revision
(`lean/lake-manifest.json`). This is the same warning `lean/README.md` gives for
local use, and it is the reason the job takes minutes rather than hours: a
measured **3m55s** with a cold cache and **2m11s** with a warm one, of which
`check.sh` itself is about 40s.

### `verifiers` — the numerical scripts

[`.github/workflows/verifiers.yml`](.github/workflows/verifiers.yml) runs **all
nineteen** `notes/verify_*.py` scripts, one GitHub job each, so the run page names
every script it ran and how long it took. Nothing is silently skipped. Each of
those jobs then re-runs its own script with one decision forced negative and
requires it to go red, and a twentieth job runs [the same control for all
nineteen at once](#the-exit-code-contract) — because **the signal CI reads is the
exit status, and an exit status that cannot be shown to fail is a green tick that
means nothing.** What a script prints is not checked; see [what is checked, and
what is only printed](#what-is-checked-and-what-is-only-printed).

Twelve run on their **full grid** — the same run you would get locally with no
arguments. Seven run on the **reduced grid** their own `--quick` / `QUICK=1`
switch selects, because their full grids exceed a sane per-push budget. The
reduced mode coarsens the grid (fewer bandwidths \(c\), larger step). Where it
*also* drops a wired check, the script's own docstring names which one and the
table below says so — `verify_sonin_ceiling.py` drops a \(N=60\) against
\(N=120\) comparison that needs both truncations by construction, and
`verify_eps_deficit.py` drops a claim about half-widths its reduced grid has no
row for. **Do not read "reduced grid" as "every check still ran".**

| script | CI runs | time on a runner |
|---|---|---|
| `verify_semilocal_gap.py` | full grid | 11s |
| `verify_prolate_claims.py` | full grid | 13s |
| `verify_sign_claims.py` | full grid | 14s |
| `verify_arch_positivity.py` | full grid | 2m05s |
| `verify_h1.py` | full grid | 2m09s |
| `verify_citation_u8.py` | full grid | 3m16s |
| `verify_q3.py` | full grid | 3m16s |
| `verify_index_convention.py` | full grid | 3m56s |
| `verify_dunster.py` | full grid | 4m52s |
| `verify_q2.py` | full grid | 7m32s |
| `verify_independent_recheck.py` | full grid | 9m28s |
| `verify_sonin_trace.py` | full grid | 2m54s — measured on a laptop, not yet on a runner |
| `verify_sonin_margin.py` | `--quick` | 34s, against 4m59s for the full grid — measured on a laptop, not yet on a runner |
| `verify_sonin_ceiling.py` | `--quick` | 1m02s, against 10m18s for the full grid — measured on a laptop, not yet on a runner; `--quick` drops one wired check |
| `verify_eps_deficit.py` | `--quick` | 49s of CPU, against 1m54s for the full grid — measured on a loaded laptop, not yet on a runner; `--quick` drops one wired check |
| `verify_prolate_rate.py` | `--quick` | 2m17s, against 18m41s for the full grid |
| `verify_deficit_repair.py` | `--quick` | 4m58s, against 20m10s for the full grid |
| `verify_q1.py` | `--quick` | 2m02s, against 25m31s for the full grid |
| `verify_h0.py` | `QUICK=1` | 2m01s; the full grid exceeds 30m |

Those times are measured, not estimated: a run with the then sixteen on
their full grids was made, and fourteen passed — `verify_h0.py` was still going
when it was cancelled at thirty minutes; `verify_sonin_margin.py`,
`verify_sonin_ceiling.py` and `verify_eps_deficit.py` were each timed the same
way when they were added. Reducing these seven takes the whole workflow from over
twenty-five minutes to under ten, which is the reason for the split.

**To get the full grid for the last seven, run them locally without the switch.**
That is the run the notes record, and CI does not perform it.

### The versions these scripts are run on

**NumPy 2.0 or newer, mpmath 1.3 or newer, on Python 3.12** — that is what CI
installs and the only combination the whole suite is exercised on. The NumPy
floor is hard: `verify_sonin_trace.py`, `verify_sonin_margin.py` and
`verify_sonin_ceiling.py` call `np.trapezoid`, the name `np.trapz`
was renamed to when NumPy 2.0 removed the old one.

Until 2026-08-13 nothing here said any of that. The workflow installed bare
`numpy mpmath`, no note or README named a version, and `verify_sonin_trace.py`
merged to `main` calling `np.trapz` — deprecated across NumPy's whole 1.x series
and deleted in 2.0. It passed on the machine that wrote it, which still had a
1.x where the old name existed, and died on the runner twelve seconds in with
`module 'numpy' has no attribute 'trapz'`. Neither machine was wrong, because
nothing had said which one was right.

**Floors, not pins**, deliberately. Pinning exact versions in the workflow would
have made that run green and left the defect standing, for whoever next ran the
scripts on a current NumPy to find without a CI run to tell them why. The
environment moving under us is the thing that caught it — within minutes of the
merge, on a machine that is not the one that wrote the code, which is the entire
point of running them there. A floor states the contract without freezing the
environment against the next such removal.

A floor nothing enforces is a floor nothing enforces, so
[`test_exit_codes.py`](#the-exit-code-contract) reads it before it runs anything
and reports a NumPy below 2.0 exactly the way it reports a missing `mpmath`:
**NOT RUN**, exit 2, a statement about the machine. Left to itself a 1.x box
would report `verify_sonin_trace.py`'s contract as broken, on the strength of an
`AttributeError` that says nothing about the contract at all.

The rename itself is inert, and this was measured rather than assumed: on one
and the same NumPy, `np.trapezoid` supplied as an alias for `np.trapz` gives
this script's output byte for byte, and the two functions' implementations
differ only in whitespace. What *does* move between NumPy 1.25 and 2.5 is the
seventh significant digit of CHECK 2's smallest eigenvalue (`min Sonin` at
\(\mu\ge2.2\), a relative change of \(4\times10^{-7}\)) — LAPACK, not this
repository. Every figure `sonin-trace.md` quotes is unaffected: the five
Connes–Consani anchors of CHECK 1 are identical on both, and the note's own
tables are quoted to three significant figures.

### The exit-code contract

**Every script exits non-zero when a check it states comes out wrong.** That was
not true until 2026-08-13: twelve of the then fifteen printed their verdict — words
like `REFUTED` or `MISMATCH`, or a measured value against a bound — into a table
cell and then exited 0 regardless, so `python verify_q1.py; echo $?` printed 0
whether the check passed or refuted itself. The reproduction command below could
not fail. It can now.

The contract lives in [`notes/verdict.py`](notes/verdict.py), which each script
imports; the printed tables are unchanged, byte for byte, on a passing run. On a
failing run the script writes the list of failed checks to **stderr** — stdout,
which the notes cite by line, stays as it was — and exits 1.

What is wired is what a script *states*: a printed verdict word, a measured
quantity against a bound the note proves, an identity whose residual it says must
vanish. What is deliberately not wired is a quantity a script reports rather than
bounds — several are labelled OBSERVED in the notes and have no threshold to
test — and any cell the notes document as allowed to fail. Each script says at
the top of its source which of its checks are wired and which are not, and why.

That the contract can fail is itself tested, per script, by
[`notes/test_exit_codes.py`](notes/test_exit_codes.py): it runs each of the
nineteen with `VERIFY_SELFTEST_FORCE_FAIL=1`, which forces the first decision the
script reaches to come out negative, and requires a non-zero exit naming that
check. A script that imported the contract but never used it would reach no
decision, exit 0, and be reported as a failure by that test. The three fastest
are also run unforced and must exit 0.

A third, **static** control runs before either, needs no imports, and covers
every decision rather than only the first: every string literal equal to a verdict
word must be an argument of a `.word(...)` call, and every script must end in
`VD.finish()`. It is what replaced CI's output grep — see [what is checked, and
what is only printed](#what-is-checked-and-what-is-only-printed). Requiring the
`finish()` matters because the forced runs cannot see a missing one: `verdict.py`
calls `finish` itself at the forced decision, so a script that dropped the call at
the end of `__main__` would pass the forced control and silently discard every
failure a later decision recorded.

**That test runs in CI**, as the `exit-code contract (positive control)` job of
the `verifiers` workflow — the same badge, because what it guards is the exit
status of the same nineteen scripts. A control only a human remembers to run
decays into the state this repository was in before 2026-08-13, and it decays
without anything going red. The forced runs stop at the first decision, so the
job is cheap: **1m00s and 1m34s** on two runs on a developer machine, and **54s**
with the static control added, against twenty-plus minutes for the grids above.

It distinguishes a broken contract from a machine that cannot run the scripts at
all. On a box without `mpmath` every one of the nineteen dies at import and exits
1, which reads as nineteen broken contracts; that reading is wrong and the fix is
one `pip install`. So the test checks the imports the selected scripts need
before running anything, reports what is missing and what to install, and exits
**2** — a status that says the contract was not tested, as distinct from the 1
that says it failed. Anything that dies of `ModuleNotFoundError` anyway is
reported under `NOT RUN` rather than counted as a failure. The static control has
run by then either way, so a 2 still carries a verdict about the source.

**The four scripts CI runs on a reduced grid had their wired checks verified
against their FULL grids by hand when the contract was written — all four exit 0
with nothing on stderr, `verify_h0.py` taking 44 minutes. CI does not repeat
that.** So a threshold that is right on the reduced grid and drifts on the full
one will not be caught by a green tick; it is caught by whoever next runs the
full grid, which is the run the notes record. Of the two added since,
`verify_sonin_ceiling.py` was checked the same way when it was written — full
grid, exit 0, nothing on stderr — and `verify_sonin_margin.py` was not.

#### What is checked, and what is only printed

**The exit status is the contract. A script's output is not checked.** Its prose
may say `REFUTED`, `MISMATCH` or `Traceback` as often as the corpus needs it to,
because this corpus records what it has overturned. Editing a docstring or a
`print` in `notes/verify_*.py` does not touch CI; editing a `VD.check`/`VD.word`
call, a threshold, or the `VD.finish()` that ends the script does.

Until 2026-08-14 that was not so. CI also grepped each script's captured output
for `Traceback|REFUTED|MISMATCH` and failed the job on a match — and **a detector
that greps output for a failure word cannot tell "this run refuted a claim" from
"this text mentions that a claim was refuted": the two are the same bytes.**
`19947c9` added three correct sentences to `verify_sonin_margin.py` recording what
mg-0b7a had refuted, and turned `main` red on a script that exits 0. The polecat
that wrote them verified what it changed and was blind to this, because the
wrapper's contract was about text while the script's was about exit status, and
nothing said there were two. That grep gets *worse* as the notes get more honest,
so it is gone (mg-a682).

Two words were already excluded from it by hand, for the same reason one word
short — see [what a green tick does not mean](#what-a-green-verifiers-tick-does-not-mean).

Removing it costs little, because it was never much of a signal. `verify_q1.py`
and `verify_eps_deficit.py` are the only scripts that can print `REFUTED` and
`verify_independent_recheck.py` the only one that can print `MISMATCH`; the other
sixteen state their verdicts in prose — "R > D at every mu", "ratios above 1
refute the lemma" — with the numbers left to a reader. So the word half of that
grep could only ever have caught a wrong *result* in three of the nineteen, and
in all three `verdict.py` computes the printed word and the exit status from the
same boolean, so they cannot drift apart.

`verify_eps_deficit.py` is where the difference stops being academic: **its
passing verdict word IS `REFUTED`**, because the refutation is what it went to
find, so every clean run of it prints the word. `verify_q1.py`'s passing word is
`ok` and it prints `REFUTED` only when something is wrong; this is the first
script in the corpus for which the two are the other way round. Under the removed
grep a green run of it would have turned `main` red every time — the same
outcome `19947c9`'s three sentences of prose produced, arrived at from the
opposite direction. The `Traceback` half needed no cover at all: the interpreter exits
non-zero whenever it prints one, and `set -o pipefail` in the workflow is what
carries that status across the `tee`.

What the grep did still cover is a verdict word printed *outside* that
machinery — a bare `print("REFUTED")`, which is the pre-2026-08-13 defect exactly.
`test_exit_codes.py` now covers that **statically**, and covers every decision in
every script rather than only the first: every string literal equal to a verdict
word must be an argument of a `.word(...)` call, and every script must end in
`VD.finish()`. That draws the verdict/prose line where the two actually differ —
a verdict is the word alone, as a value; prose is the word inside a sentence — and
not in the output, where they do not differ at all. What it does not catch is a
verdict word assembled rather than written (`"REFUT" + "ED"`, an f-string); no
script does that.

Each of the nineteen `verify` jobs also runs the forced-negative control for its
own script, in its own job, right after the run it is meant to validate. So a
green job says "this script ran clean **and** its failure path is live on this
runner", not "this script ran".

### What a green `verifiers` tick does not mean

Two failure words mark cells that are *allowed* to fail, so the exit-code
contract does not gate on them — and they were the two words hand-excluded from
CI's output grep back when there was one. `(FAILS)` is one: on its full grid
`verify_q1.py` prints exactly one such cell,

```
12.56637   0.07472     0.3724      0.6387      0.8627      1.04 (FAILS)  11.7997
```

which is the ratio \(r\ge 1\) row, the same documented boundary as the
\(\mu^*=2.1169\) threshold and the index-8 cell that `verify_q1.py` and
`dunster-check.md` already flag. Gating on `(FAILS)` would paint the badge red
for something the notes already record and explain. `NO` — the negative branch in
`verify_h1.py` and `verify_semilocal_gap.py` — is excluded for the same reason,
pre-emptively: it did not occur in any run made here, on either grid. Neither
word is in `BAD_WORDS` in `notes/test_exit_codes.py`, which is where that
exclusion now lives; adding a word there is a claim that no passing run may ever
print it as a cell.

Note that the `(FAILS)` cell above appears on the **full** grid, which CI does
not run for `verify_q1.py`; the reduced grid does not reach it. That is one more
reason the reduced runs are weaker than the full ones, and another reason to run
the full grids locally. It is also why the exit-code contract was checked on
that full grid rather than reasoned about: the run prints the cell and exits 0,
so the exclusion is measured.

So: a green tick means **every script still runs to completion on a clean
machine, every check any of them states came out right, and every one of them was
shown on that same runner to be able to report a wrong one.** It does not mean a
human or a machine re-derived the mathematics, and it is not a substitute for
reading the notes. Most of what these scripts print is measurement rather than verdict, and
those numbers are checked against the notes by a reader, not by CI.

### `paper` — the LaTeX documents

[`.github/workflows/paper.yml`](.github/workflows/paper.yml) builds
`paper/positivity-obstruction.tex` and `start.tex` from scratch on a clean
machine, three `pdflatex` passes each — the same command this README documents.
There is no bibtex step: the paper's bibliography is inline
(`\begin{thebibliography}`), so the passes resolve it.

**Exiting 0 is not the check.** In `-interaction=nonstopmode` pdflatex exits 0
while dropping undefined macros and leaving gaps in the text, so each job also
reads the log of the last pass and fails on an undefined control sequence, an
undefined reference or citation, or a request to rerun. The reference and
citation checks are made **after the last pass only**: one pass reports 218
undefined references and 63 undefined citations in the paper, and both numbers
are artefacts of running one pass. After the third there are none.

This workflow exists because the paper spent time on `main` in a state where
`pdflatex -halt-on-error` produced **no PDF at all** — `\C` and `\widecheck`
were used and never defined — while both other badges stayed green. A green
`paper` tick means a stranger who clones the repository and runs pdflatex gets
the PDF; it says nothing whatever about what is in it.

`s3.tex` is not built, and is not missing by oversight: it is a section fragment
with no preamble, not a standalone document, and nothing includes it.

### Reproducing the same checks locally

```sh
cd paper && pdflatex positivity-obstruction.tex   # three passes; no bibtex
                                                  # (the bibliography is inline)

lean/scripts/check.sh                 # the Lean build, sorry grep and axiom audit

pip install "numpy>=2.0" "mpmath>=1.3"   # numpy for five scripts, mpmath for
                                         # most; the floors are not optional --
                                         # see "The versions these scripts are
                                         # run on" above
cd notes && python verify_q1.py       # any verifier; run from `notes/`
echo $?                               # 0 iff every check it states came out right

cd notes && python test_exit_codes.py # ~2 min: proves each script can still fail
echo $?                               # 0 pass, 1 a contract failed, 2 not run
```

The verifiers must be run with `notes/` as the working directory — several
import their siblings by bare module name. `verify_independent_recheck.py` needs
neither numpy nor mpmath, which is the point of it.

If the `pip install` line above was skipped, `test_exit_codes.py` says so and
exits 2 rather than reporting nineteen failures: without `mpmath` every script
dies at import and exits 1, and a run that never happened is not a contract that
does not work.

## License

MIT — see [LICENSE](LICENSE).
