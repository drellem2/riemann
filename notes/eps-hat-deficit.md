# The two constants are not equal — they are the two sides of one inequality, and it is nearly tight

Work item mg-e205. Companion script:
[`verify_eps_deficit.py`](verify_eps_deficit.py) (needs `mpmath`; 1m54s of CPU,
`--quick` 49s, which is what CI runs). Answers a question about
[`sonin-ceiling.md`](sonin-ceiling.md) (mg-0b7a) Bottom-line 2 and the paper's
`thm:deficit`; **changes no number in either**.

mg-e205 was filed on a decimal comparison and said so. Two constants derived by
different routes, in different tickets, for different purposes:

    log(pi) - psi(1/4)         = 5.3721834192    thm:deficit, paper/positivity-obstruction.tex:1147-1152
    eps_hat(0), closed form    = 5.37218344      mg-0b7a, notes/sonin-ceiling.md Bottom-line 2

agreeing an order of magnitude better than $\hat\epsilon(0)$ agreed with the
quadrature it had been validated against. The ticket asked whether that is an
identity, required the numerics to run first because they can refute, and said
that reporting a refutation would be a success.

**It is not an identity. It is an inequality, and the inequality is a theorem.**

---

## Bottom line

**1. REFUTED, at the ninth significant digit.** At 30 digits, on an apparatus
anchored to every printed value Connes–Consani give for it:

$$\hat\epsilon(0)=5.37218343\,5911187547213869\ldots,\qquad
\log\pi-\psi(\tfrac14)=5.37218341\,9225665582232957\ldots$$

They agree to **eight** significant digits and part at the ninth — $\ldots4359$
against $\ldots4192$. The gap is $1.6685521965\times10^{-8}$, relative
$3.1\times10^{-9}$. It is not truncation: rebuilding the whole apparatus at
$(K,n_{\max},\mathrm{dps})=(40,10,30)$, $(55,12,30)$ and $(80,16,40)$ moves
$\hat\epsilon(0)$ by $2.0\times10^{-15}$, $4.0\times10^{-20}$ and
$4.3\times10^{-25}$ — the **coarsest** of those still resolves the gap by seven
orders — and the last term the series keeps is $1.4\times10^{-22}$. §2, CHECK 4.

**2. What is true instead is stronger, for the one purpose the identity was
wanted.** Write $\sigma_S$ for the symbol of Connes–Consani's trace. Theorem
`devil` (`weil-compo.tex:1132`) is
$\operatorname{tr}(\vartheta(f)\mathbf S)=W_\infty(f)+\int f\epsilon\,d^*\rho$,
and $\mathbb R_+^*$ is abelian, so
$\operatorname{tr}(\vartheta(g\star g^*)\mathbf S)=\lVert\mathbf S\vartheta(g)^*\rVert_{HS}^2\ge0$
**is** positivity of $\sigma_S$ pointwise. The archimedean symbol
$W_\infty=-W_{\mathbb R}$ carries is `thm:deficit`'s own $2\vartheta'(t)$. So

$$\boxed{\ \sigma_S(t)=2\vartheta'(t)+\hat\epsilon(t)\ \ge\ 0
\quad\Longrightarrow\quad
\hat\epsilon(0)\ \ge\ -2\vartheta'(0)=\log\pi-\psi(\tfrac14)=5.3721834192\ldots>0\ }$$

**Theorem A's only hypothesis is discharged unconditionally, with a named
constant as the lower bound, and with no numerics in the argument at all.** §3.

**3. The eight digits are not a coincidence. They are $\log(\text{area})=0$.**
The Sonin square $S(a,a)$ is the $c=2\pi a^2$ prolate problem; extrapolating
$\epsilon$ to it gives $\sigma_S(0;a)=2\log a+\delta(a)$ with

| $a$ | $0.7$ | $0.85$ | $1.0$ | $1.2$ | $1.4$ | $\ge1.7$ |
|---|---|---|---|---|---|---|
| $\delta(a)$ | $2.7\cdot10^{-5}$ | $8.6\cdot10^{-7}$ | $1.7\cdot10^{-8}$ | $4.0\cdot10^{-11}$ | $3.7\cdot10^{-14}$ | below the floor |

Connes–Consani's $\epsilon$ is the $a=1$ case, **where $2\log a$ is exactly
zero.** The two constants look equal to eight digits because the square $(1,1)$
is precisely the point at which the cutoff's log-of-area term vanishes, and what
is left is the exponentially small prolate spectral defect at $c=2\pi$. §4.
*The extrapolation past $a=1$ is ours and is not proved* — what makes it
evidence rather than curve-fitting is that $2\log a$ is not fitted and nothing
in the construction knows about it.

**4. "Bounded below" and "indefinite at low frequency" are the same inequality,
read from opposite sides.** $\sigma_S\ge0$ says $-\hat\epsilon(t)\le2\vartheta'(t)$
pointwise. At $t=0$, where $2\vartheta'$ attains its minimum (`thm:deficit`'s own
proof, step (i)) and $\hat\epsilon$ attains its maximum, that reads
$-\hat\epsilon(0)\le-5.3721834192<0$. **The indefiniteness of $-E$ at low
frequency is forced by the archimedean lower bound being the number it is.**
There is no tension to resolve: the ticket's two readings are one statement. §5.

**5. And the near-saturation is where the interesting question now is.**
$\sigma_S(t)$ is positive at every grid point, minimised at $t=0$, and grows like
$\log(t/2\pi)$. Its minimum is $1.67\times10^{-8}$ against a form whose terms are
of order $5$. Connes–Consani's positivity is therefore *almost* degenerate, and
the almost-null direction is zero frequency — the constant direction. §3.3.

**6. What this note does NOT do.** It does not prove $\sigma_S(0)>0$ *strictly*
from anything other than the measurement, it does not identify $\delta(1)$ in
closed form, and it does not prove the $a\ne1$ extrapolation. §6.

---

## 0. Environment, and what is inherited

**Environment.** `mpmath 1.4.1`, `numpy 2.5.2` (unused by this script) under
CPython 3.14 in a virtualenv on macOS 24.6.0 — *not* `/usr/bin/python3`, which
has no `mpmath` on this host. CI's floors are `numpy>=2.0`, `mpmath>=1.3` on
Python 3.12 (README, "The versions these scripts are run on"). Every number here
is arbitrary precision by construction: the quantity this note decides is
$1.7\times10^{-8}$ against constants of order $5$, and mg-aedf established that
this corpus cannot do that class of computation in double.

**Inherited, and re-verified rather than assumed.** The script rebuilds the
$c=2\pi$ prolate apparatus from scratch in `mpmath` — it does not import
mg-d03b's or mg-0b7a's `numpy` code — and CHECK 1 re-anchors it to every printed
Connes–Consani value the corpus has been using:

| anchor | source | ours |
|---|---|---|
| $\lambda(0..5)$ | `weil-compo.tex:969` | all six, worst relative deviation $5.3\times10^{-7}$ (their last printed digit) |
| $\sum\lambda(n)^2=2(\mathrm{Si}(4\pi)/4\pi+1)$ | `:1101` | $2.2374848349418275387$ both sides, difference $2.0\times10^{-30}$ |
| $t(n)=\frac{\lambda^2}{1-\lambda^2}\xi_n(1)^2$ | `:1380` | all five to the printed digits |

The third is the one that matters most here: $t(n)$ is the only anchor that pins
the **normalisation** of $\xi_n$, which is exactly what $A_n$ depends on.

From [`sonin-ceiling.md`](sonin-ceiling.md) §2.1, **kept and re-derived**: the
closed form $\hat\epsilon(0)=2\sum_n\frac{\lambda(n)}{1+\lambda(n)}A_n^2$. From
`thm:deficit`, **kept**: $\vartheta'(t)=\frac12\operatorname{Re}\psi(\tfrac14+\tfrac{it}2)-\frac12\log\pi$,
its minimum at $t=0$, and $-2\vartheta'(0)=\log\pi-\psi(\tfrac14)$.

Vocabulary as in [`semilocal-gap.md`](semilocal-gap.md) §0.

---

## 1. Raising the bar, which is what the ticket asked for first

The ticket's step 2 was *"evaluate both to 25+ digits, because it is cheap and it
can refute."* It is cheap, and it did.

Two things had to be right before the digits meant anything.

**The apparatus.** Built from the Legendre eigenproblem for
$-\partial((1-x^2)\partial)+c^2x^2$ at $c=2\pi$ — the same construction
`verify_sonin_trace.py` uses — in `mpmath` at 30 digits, with
$\lambda(n)=\sqrt2\,\beta_0/\psi_n(0)$ from
$\lambda_n\psi_n(0)=\int_{-1}^1\psi_n$, and $\xi_n=\sqrt2\,\psi_{2n}$ because
Connes–Consani normalise $\int_{-1}^1\xi_n^2=2$. CHECK 1 is the anchoring; §0
has the table.

**$A_n$.** $\int_0^1\xi_n(x)x^{-1/2}dx$ is a sum of
$J_k=\int_0^1x^{-1/2}P_k(x)dx$, and

$$J_k=\frac{\sqrt\pi\,\Gamma(s)}{2^s\Gamma(\frac{s-k+1}2)\Gamma(\frac{s+k}2+1)}
\bigg|_{s=1/2}=\frac{(-1)^{k/2}\,2}{2k+1}\qquad(k\text{ even}),$$

the Gamma expression collapsing by reflection. So **$A_n$ is an exact rational
combination of the Legendre coefficients**, $A_n=2\sum_k(-1)^{k/2}\beta_k/\sqrt{2k+1}$,
with no quadrature anywhere in it. CHECK 2 checks the collapse at
$k=0,2,4,10,40$ and $A_n$ against direct quadrature (substituting $x=v^2$, which
removes the endpoint singularity and leaves a polynomial) at $n=0,1,3,6$ —
agreement to $3\times10^{-29}$ or better. The values reproduce mg-0b7a's §2.2
table to its printed digits.

### 1.1 The one analytic step, checked without assuming it

mg-0b7a's closed form rests on exactly one non-elementary step:

$$B_n:=\int_1^\infty\frac{\mathcal F\xi_n(u)}{\sqrt u}du=(1-\lambda(n))A_n,$$

from $\int_0^\infty u^{-1/2}\mathcal Ff(u)du=\int_0^\infty x^{-1/2}f(x)dx$ — the
Fourier gamma factor $G(s)=2\Gamma(s)\cos(\pi s/2)(2\pi)^{-s}$ being exactly $1$
at the self-dual $s=\tfrac12$ — together with $\mathcal F\xi_n=\lambda(n)\xi_n$
on $[0,1]$.

Everything else in the closed form is a substitution and a Fubini. So this is the
step that could carry a factor, and CHECK 3 checks **both halves against numbers
that assume neither**: the eigen-relation off zero (at $\omega=0.7$, where
mg-0b7a's route never evaluates it), and $B_n$ by direct oscillatory quadrature
of $\int_1^\infty\mathcal F\xi_n(u)u^{-1/2}du$, with
$\mathcal F\xi_n$ from $\int_{-1}^1P_k(x)e^{izx}dx=2i^kj_k(z)$.

| $n$ | eigen-relation, rel. | $B_n$ quadosc | $(1-\lambda)A_n$ | rel. |
|---|---|---|---|---|
| 0 | $2.8\cdot10^{-30}$ | $6.474873892738176\cdot10^{-5}$ | $6.474873892738175\cdot10^{-5}$ | $2.4\cdot10^{-16}$ |
| 1 | $4.2\cdot10^{-31}$ | $0.02284663810697679$ | $0.02284663810697679$ | $2.3\cdot10^{-18}$ |
| 2 | $4.7\cdot10^{-29}$ | $-0.3082987251444618$ | $-0.3082987251444618$ | $1.3\cdot10^{-19}$ |
| 3 | $2.0\cdot10^{-30}$ | $0.4388989305101084$ | $0.4388989305101084$ | $7.4\cdot10^{-20}$ |

**mg-0b7a's closed form is correct.** The refutation below is therefore about
the two constants, not about the formula for one of them.

---

## 2. The refutation

$$\hat\epsilon(0)=5.372183435911187547213869\ldots$$
$$\log\pi-\psi(\tfrac14)=5.372183419225665582232957\ldots$$
$$\text{difference}=1.66855219649809\times10^{-8},\qquad\text{relative }3.106\times10^{-9}.$$

**Eight significant digits agree; the ninth does not.** The ticket asked for the
digit and that is the digit.

Two things say this is not an artefact.

- **Not series truncation.** The last term kept ($n=13$) is
  $1.4\times10^{-22}$, which is $8.5\times10^{-15}$ of the gap.
- **Not the basis and not the precision.** CHECK 4 rebuilds the entire apparatus
  three more times and prints the spread against the headline value:

  | $K$ | $n_{\max}$ | dps | $\hat\epsilon(0)$ | $|\Delta|$ |
  |---|---|---|---|---|
  | $40$ | $10$ | $30$ | $5.3721834359111855738$ | $2.0\cdot10^{-15}$ |
  | $55$ | $12$ | $30$ | $5.3721834359111875472$ | $4.0\cdot10^{-20}$ |
  | $80$ | $16$ | $40$ | $5.3721834359111875472$ | $4.3\cdot10^{-25}$ |

  The coarsest still resolves the $1.7\times10^{-8}$ by seven orders.

And the note this refutes could not have seen it: mg-0b7a's two quadratures were
$5.37217300$ and $5.37218520$, which bracket both candidates. **A $10^{-6}$
instrument cannot decide a $10^{-8}$ question**, and the ticket was right to
require the digits first. What it could not have anticipated is that raising the
bar would not end the matter.

---

## 3. What is true: an inequality, and it is proved

### 3.1 The symbol

Both sides of Theorem `devil` are distributions in $f$ on $\mathbb R_+^*$. Write
$\hat f(t)=\int f(e^y)e^{-ity}dy$; then every term is a Fourier multiplier and

$$\operatorname{tr}(\vartheta(f)\mathbf S)=\frac1{2\pi}\int\hat f(t)\,\sigma_S(t)\,dt,
\qquad \sigma_S=\sigma_\infty+\hat\epsilon,$$

with $\sigma_\infty$ the symbol of $W_\infty=-W_{\mathbb R}$. That symbol is
`thm:deficit`'s own: the theorem's proof is *"(ii) the boundary term is a square,
(iii) Plancherel"*, i.e. $\sigma^{\rm arch}=W_{0,2}-W_{\mathbb R}$ splits as a
non-negative boundary term plus a multiplier, and the multiplier is
$2\vartheta'(t)=\operatorname{Re}\psi(\tfrac14+\tfrac{it}2)-\log\pi$. Hence

$$\sigma_S(t)=2\vartheta'(t)+\hat\epsilon(t).$$

### 3.2 Positivity, which is elementary

$\mathbb R_+^*$ is abelian, so
$\operatorname{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)=\operatorname{tr}(\vartheta(g\star g^*)\mathbf S)$
with no ordering question ([`sonin-trace.md`](sonin-trace.md) §1.2 already says
this), and $\mathbf S=\mathbf S^*=\mathbf S^2$ makes the left side
$\lVert\mathbf S\vartheta(g)^*\rVert_{HS}^2\ge0$. Since
$\widehat{g\star g^*}=|\hat g|^2$ ranges over the non-negative functions,
**$\sigma_S(t)\ge0$ pointwise** ($\sigma_S$ is continuous, so a.e. is
everywhere). This is Theorem `devil`'s positivity clause, and it needs nothing
beyond $\mathbf S$ being an orthogonal projection.

### 3.3 The consequence, and how tight it is

$$\hat\epsilon(0)=\sigma_S(0)-2\vartheta'(0)\ \ge\ -2\vartheta'(0)=\log\pi-\psi(\tfrac14)=5.3721834192\ldots>0.$$

CHECK 5 measures $\sigma_S$:

| $t$ | $2\vartheta'(t)$ | $\hat\epsilon(t)$ | $\sigma_S(t)$ |
|---|---|---|---|
| $0$ | $-5.372183419226$ | $5.372183435911$ | $1.6686\cdot10^{-8}$ |
| $0.5$ | $-3.332004594681$ | $3.332004630307$ | $3.5626\cdot10^{-8}$ |
| $2$ | $-1.161557090968$ | $1.161557781960$ | $6.9099\cdot10^{-7}$ |
| $5$ | $-0.230118218246$ | $0.230178087901$ | $5.9870\cdot10^{-5}$ |
| $2\pi$ | $-0.001060180174$ | $0.001364500606$ | $3.0432\cdot10^{-4}$ |
| $10$ | $+0.464290626865$ | $-0.449037184954$ | $1.5253\cdot10^{-2}$ |
| $50$ | $+2.074129271185$ | $-0.013704975119$ | $2.0604$ |

positive everywhere, **minimised at $t=0$**, and growing like $\log(t/2\pi)$
because $\hat\epsilon\in L^1$ decays and $2\vartheta'(t)\sim\log(t/2\pi)$.

So $\hat\epsilon(t)$ tracks $-2\vartheta'(t)$ to eight or nine digits across the
whole low-frequency band, not only at $t=0$; and $\sigma_S(0)=1.67\times10^{-8}$
is the **whole** of the disagreement mg-e205 found. The gap in §2 *is* the trace
symbol at zero frequency.

Two remarks worth carrying.

**The gamma factor really is the shared object — the ticket's step 1 was right
about the mechanism.** $G(s)=\Gamma_{\mathbb R}(s)/\Gamma_{\mathbb R}(1-s)$, so
$|G(\tfrac12+it)|=1$ and
$$G(\tfrac12+it)=e^{2i\vartheta(t)},$$
$\vartheta$ being the Riemann–Siegel theta. The same $G$ that is $1$ at
$s=\tfrac12$ (which is what collapses $B_n$, §1.1) has
$G'/G(\tfrac12)=2\vartheta'(0)$, which is `thm:deficit`'s constant. Both sides do
pass through one object at the self-dual point. They are just not equal there.
CHECK 5 prints $|G|$ and $\arg G/2$.

**Connes–Consani's positivity is nearly degenerate, and the almost-null direction
is the constant.** $\min_t\sigma_S=\sigma_S(0)=1.67\times10^{-8}$ against terms
of order $5$. That is a fact about their theorem which this corpus did not have,
and it is the reason two independently derived decimals looked identical.

---

## 4. Where the eight digits come from

$S(a,b)$ scales — $\vartheta(\lambda)S(a,b)\vartheta(\lambda)^{-1}=S(\lambda a,b/\lambda)$
— so the family depends only on $ab$, and $S(a,a)$ is the $c=2\pi a^2$ prolate
problem. Under $x=au$ the finite-Fourier operator on $[-a,a]$ has
$\lambda_n^{(a)}=a\,\lambda_n^{(c)}$, and $A_n$ is $a$-free. The Mellin step of
§1.1 is unchanged, because $s=\tfrac12$ is self-dual whatever $a$ is. So the
closed form extends verbatim, with $\lambda\mapsto\lambda^{(a)}$:

$$\hat\epsilon_a(0)=2\sum_n\frac{\lambda^{(a)}_n}{1+\lambda^{(a)}_n}A_n^2 .$$

CHECK 6 measures $\sigma_S(0;a)=\hat\epsilon_a(0)-(\log\pi-\psi(\tfrac14))$:

| $a$ | $c=2\pi a^2$ | $\sigma_S(0;a)$ | $2\log a$ | $\delta=\sigma_S-2\log a$ | $1-\lambda_0^{(a)}$ |
|---|---|---|---|---|---|
| $0.7$ | $3.079$ | $-0.71332308662$ | $-0.71334988788$ | $2.68\cdot10^{-5}$ | $1.1\cdot10^{-2}$ |
| $0.85$ | $4.540$ | $-0.32503700380$ | $-0.32503785900$ | $8.55\cdot10^{-7}$ | $7.6\cdot10^{-4}$ |
| $1.0$ | $6.283$ | $1.6685521965\cdot10^{-8}$ | $0$ | $1.67\cdot10^{-8}$ | $2.9\cdot10^{-5}$ |
| $1.2$ | $9.048$ | $0.36464311363$ | $0.36464311359$ | $3.96\cdot10^{-11}$ | $1.4\cdot10^{-7}$ |
| $1.4$ | $12.315$ | $0.67294447324$ | $0.67294447324$ | $3.70\cdot10^{-14}$ | $2.4\cdot10^{-10}$ |
| $1.7$ | $18.158$ | $1.0612565021$ | $1.0612565021$ | *floor* | $2.5\cdot10^{-15}$ |
| $2.0$ | $25.133$ | $1.3862943614$ | $1.3862943611$ | *floor* | $2.6\cdot10^{-21}$ |

$$\boxed{\ \sigma_S(0;a)=2\log a+\delta(a),\qquad \delta(a)>0\text{ and falling with }1-\lambda_0^{(a)}\ }$$

$2\log a=\log(ab)$ is the log-of-area term any cutoff trace formula carries, and
**Connes–Consani's $\epsilon$ is the one square where it is exactly zero.** That
is the whole of the coincidence: $\hat\epsilon(0)$ and $-2\vartheta'(0)$ agree to
eight digits at $a=1$ and to no digits at all at $a=2$, and nothing about the
first case is more fundamental than the second.

**Two honest limits on this table.**

- **The $a\ne1$ extrapolation is ours and is not proved.** Connes–Consani state
  $\epsilon$ at $a=1$. What makes the table evidence rather than curve-fitting is
  that $2\log a$ is not fitted — nothing in the construction knows about it — and
  it accounts for $\sigma_S(0;a)$ to $3.7\times10^{-14}$ in a quantity of size
  $0.67$.
- **The last two rows are noise, and are labelled so.** Past $a=1.4$, $\delta$
  falls under the script's own eigenproblem error, which grows with the Legendre
  order. The $a=1.7$ row comes out **negative** ($-1.9\times10^{-15}$) and the
  $a=2.0$ row comes out **larger** ($+2.7\times10^{-10}$) than it — noise growing
  with $K$, not a residual growing with $a$. CHECK 6 cuts by half-width and not
  by magnitude for exactly that reason, and reads those two rows as zero rather
  than as measurements.

---

## 5. The two readings do not conflict

The ticket asked whether *"bounded below"* (`thm:deficit`) and *"inherently
indefinite at low frequency"* (`sonin-ceiling.md` Theorem A) are compatible
readings of one number, and said that if they conflict, that is a defect in one
of them and the more valuable finding.

**They do not conflict, and they are not two readings.** They are one inequality
seen from its two sides. $\sigma_S\ge0$ is

$$-\hat\epsilon(t)\ \le\ 2\vartheta'(t)\qquad\text{for all }t,$$

the left side being the symbol of $-E$ and the right the archimedean symbol. At
$t=0$ — where $2\vartheta'$ attains its minimum (`thm:deficit`'s proof, step (i))
and $\hat\epsilon$ attains its maximum — it reads
$-\hat\epsilon(0)\le2\vartheta'(0)=-5.3721834192<0$.

So the negativity of $-E$'s symbol at low frequency **is** the statement that the
archimedean form's worst direction costs what `thm:deficit` says it costs. It is
not an independent obstruction that happens to have the same size; it is the same
bound, saturated to eight digits at the one frequency where both extremes sit.
`thm:deficit` bounds how bad the archimedean side gets; Theorem A observes that
$-E$ must be at least that bad somewhere; the second follows from the first plus
Theorem `devil`.

**What this buys `sonin-ceiling.md`.** Theorem A's hypothesis
$\hat\epsilon(0)>0$ was, in mg-0b7a, *"a computation, not a sign argument"* —
finitely many explicitly computed terms, which the note called the strongest form
in which this corpus could hold it (§2.2 there). It is now a corollary of a
proved theorem, with a named constant:

$$\hat\epsilon(0)\ \ge\ \log\pi-\psi(\tfrac14)\ >\ 0 .$$

**A one-line cross-reference is proposed, not written.** `paper/` is read-only
for this ticket. If a reader is to find this from `thm:deficit`, the sentence
belongs after the theorem's proof, and is something like: *"the same constant is
a lower bound for $\hat\epsilon(0)$, by positivity of
$\operatorname{tr}(\vartheta(f)\mathbf S)$; the two differ by
$1.7\times10^{-8}$."* Daniel's call, and his file.

**Sign-sensitivity** ([`sign-sensitivity-generator.md`](sign-sensitivity-generator.md)).
The inequality $\hat\epsilon(0)\ge-2\vartheta'(0)$ is **not** sign-blind: it
reverses under $W_\lambda\mapsto-W_\lambda$, because $\sigma_S\ge0$ is a
statement about which way the trace points. §2's refutation **is** sign-blind:
two numbers differ at the ninth digit whichever way the form is oriented. The
generator's polarity applies as mg-baa9 states it — the presentation carries the
sign, and this note has one of each.

---

## 6. Provenance, and what is unverified

**Provenance of the question.** mg-e205 says, in its own words, *"I found this by
comparing two printed decimals... No derivation."* That was a good instinct and
a bad hypothesis, and the ticket's own instruction — run the digits first,
because they can refute — is what made it cheap to find out. Total cost was one
`mpmath` script.

**Unverified, and named as such.**

1. **$\sigma_S(0)>0$ strictly** is measured, not proved. The proof gives $\ge0$;
   nothing here rules out an exact cancellation that the measurement is too
   coarse to see — except that the measurement is not coarse ($1.67\times10^{-8}$
   against a numerical floor of $10^{-24}$), so this is a formality.
2. **$\delta(1)=1.6685521965\times10^{-8}$ is not identified in closed form.** It
   falls with $1-\lambda_0^{(a)}$ but not proportionally to it, nor to
   $(1-\lambda_0)^2$; the ratios $\delta/(1-\lambda_0)$ across the resolved rows
   are $2.5\cdot10^{-3},\,1.1\cdot10^{-3},\,5.8\cdot10^{-4},\,2.8\cdot10^{-4},\,1.5\cdot10^{-4}$
   — falling, so $\delta$ is $o(1-\lambda_0)$ and nothing sharper is claimed.
3. **The $a\ne1$ formula is an extrapolation** of Connes–Consani's $\epsilon$,
   as §4 says. The $a=1$ column is theirs; the rest is ours.
4. **$\sigma_\infty=2\vartheta'(t)$ is read off `thm:deficit`'s proof**, not
   re-derived from Weil's local term here. It is however confirmed to eight or
   nine digits at every $t$ in the CHECK 5 grid by an entirely separate
   computation, and a wrong sign or normalisation would make $\sigma_S$ negative
   at large $t$; it is not.
5. **$\sigma_S\ge0$ is checked on a grid, not proved to have no zero off it.**
   The proof in §3.2 covers all $t$; the grid is illustration.

**One thing this note breaks, recorded here because nothing else would say so.**
`verify_eps_deficit.py` prints `REFUTED` **on a clean run**, as its passing
verdict word — every other script in the corpus prints `ok` on the good branch and
a verdict word only when something is wrong. `notes/test_exit_codes.py`'s
`BAD_WORDS` comment said, until this branch, that adding a word to that list was a
claim *"no passing run may ever print it as a cell"*; that is no longer true and
the comment now says so. The static wiring check is unaffected — it requires the
literal to be wired to a decision, not which branch prints it. Under the CI grep
mg-a682 removed, a **green** run of this script would have turned `main` red every
time, which is the same outcome `19947c9`'s prose produced, reached from the
opposite direction.

**Deviation from the work item's letter, recorded because it is one.** mg-e205's
acceptance said *"a note in `notes/`, nothing else touched."* This branch also
adds the companion script to `.github/workflows/verifiers.yml`, to
`notes/test_exit_codes.py`'s `SCRIPTS`, and to README's verifier table. Adding an
unwired `notes/verify_*.py` would have made README's existing sentence — that CI
runs **all** the `notes/verify_*.py` scripts — false, which is a worse outcome
than the extra diff. `paper/` and `docs/` are untouched, which is what the
constraint was protecting.
