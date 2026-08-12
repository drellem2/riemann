# The semilocal gap — what the archimedean proof supplies, and what a finite place lacks

Work item mg-03f0. Companion scripts:
[`verify_semilocal_gap.py`](verify_semilocal_gap.py) and, for §10,
[`verify_arch_positivity.py`](verify_arch_positivity.py) (both need `numpy`).
Continues [`citation-audit.md`](citation-audit.md) (mg-3a9c) and
[`index-convention.md`](index-convention.md) (mg-9433), which between them
established that the corpus's objects are Connes–Consani's and that its
$QW_\lambda$ lies in the **finitely-many-primes** branch — the branch whose
theorem does not exist.

**This is a characterisation, not a proof attempt.** No step below is offered as
progress towards semilocal Weil positivity. Two small verifiable facts fall out
(§3.2, §5.3); they are stated as what they are.

Nothing in `start.tex` or `s3.tex` was edited. References to them are by line.
Sources were read as arXiv LaTeX, downloaded from `arxiv.org/e-print/`; line
numbers of the form `weil-compo.tex:765` are lines of those files. Provenance
is §7, to the standard of `citation-audit.md` §9.

---

## Bottom line

**1. The archimedean sign has exactly one source, and it is a square.**
$\operatorname{Tr}(\vartheta(g)\,\mathbf S\,\vartheta(g)^*)\ge 0$, where $\mathbf S$ is
the orthogonal projection onto the Sonin space. Everything else in
arXiv:2006.13771 — 70 pages of it — is the *comparison* of the Weil functional
with that trace: a trace-remainder $\epsilon(\rho)$, its jump at $\rho=1$, a
compact operator $\mathcal K_I$, a Toeplitz spectral analysis, and a rank-one repair.
The comparison is the work; the sign is one line. §1.

**2. Most of the machinery survives at a finite place. The two things that
carry the sign do not.** The involution, the $\star$-algebra, Boas–Kac, the
operator $Q$, the semilocal trace formula, the radical of the Weil form and the
near-radical construction are all place-independent or already proved
semilocally. What is missing is (i) the diagonalisation of the angle operator
between the two cutoff projections — semilocally there is no Slepian–Pollak, and
supplying one is *precisely* the "semilocal prolate operator" programme; and
(ii) any comparison term at all: no semilocal $\epsilon$, no semilocal
compactness statement, no semilocal spectral analysis. §2, §3.

**3. The prime terms cannot supply a sign, and this is exact, not heuristic.**
The prime contribution to $QW_\lambda$ is $-\Lambda(n)\langle f\mid V(n)f\rangle$
with $V(n)$ the compression of $n^{-1/2}(\vartheta_n+\vartheta_{n^{-1}})$
(Connes–Consani, `Spectraltriples.tex:289`, Prop. `Hilbert`). Multiplication by
$e^{i\pi x/\log n}$ is a unitary of $L^2([\lambda^{-1},\lambda])$ conjugating
$V(n)$ into $-V(n)$: its spectrum is **exactly symmetric about $0$**, on the nose,
at every $\lambda$, before any condition is imposed. Its norm is
$2n^{-1/2}\cos\!\big(\pi/(m+2)\big)$, $m=\lceil L/\log n\rceil-1$ — the Boas–Kac
bound the archimedean paper itself uses. Proved and checked in §3.2.

**4. Place-by-place positivity fails, so "transport the proof to $p$" is not
the right shape of statement. This is *numerical*, and now independently
reproduced.** Connes–Consani report that the archimedean contribution *alone*
changes sign past $L=\log 2$, and that positivity is restored only by adding the
prime $2$ — and that perturbing $2$ to $1.9999$ or $2.0005$ destroys it
(arXiv:2106.01715, `Spectraltriples.tex:542-575`, **numerical**, their word). No
theorem asserts the failure, in that paper or anywhere else the corpus's sources
reach; §10.1 says where that was looked for. But the computation is now rebuilt
from scratch and agrees with theirs on all five numbers it states, so the third
possibility — an artefact of the truncation or of double precision — is
**excluded**: §10.2, and there is an explicit test function at §10.3. The
crossing is at $\mu\approx2.2710$, not immediately past $2$. The required theorem is
about a **cancellation between places**, not about each place. That is a
different and harder object than the one that was proved. §3.3, §10.

**5. CCM's "more precise strategy" is a strategy, and its own two halves are
both deferred.** arXiv:2310.18423 proves the semilocal Sonin space is stable
(Theorem 2) and proposes $\mathbf W_{\lambda,S}=(H+\tfrac12)^2+\lambda^2N_S$ as a
candidate. Its Jacobi coefficients for general $S$ are "deferred to a
forthcoming paper" (`mainc2m24fine.tex:259`); a *second* candidate via the Weil
representation of the metaplectic cover of $SL_2(\mathbb A_S)$ is deferred to the same
(`:270`); and the property that would make either one usable — negative
eigenspace $=$ Sonin space — is described as "another constraint in the search",
not proved. As of Connes' own survey (arXiv:2602.04022, Feb 2026) the proved
positivity is still exactly "support in $[2^{-1/2},2^{1/2}]$, archimedean", and
semilocal positivity appears in no list of next steps. §4.

**6. The corpus's objects sit on the archimedean side of the gap — but its
central unresolved estimate is the bridge quantity, and that is better news than
"it stops short".** `start.tex:39`'s $QW_\lambda(Eh_\lambda)\asymp1-\chi_4$
evaluates the *semilocal* form on an *archimedean-built* vector. That is exactly
the comparison the gap consists of. It is also, in Connes' letters, a published
observation: Connes' 2026 survey reports (`rhready.tex:1149`) "a striking similarity" between the
smallest eigenvalue $\epsilon(\lambda)$ of $QW_\lambda$ and $1-\chi_2(\lambda)$,
which under the index convention settled by mg-9433 **is** the corpus's
$1-\chi_4$. §5.2.

**7. One audit row is superseded and one open item closes.**
`citation-audit.md` §4.2 row 14 records $1-\chi_4$-as-the-controlling-scale as
*corpus-specific*, correctly for the 2023 paper it checked; the 2026 survey
identifies the rate. And U4 (Fuchs' constant, never checked) closes: mg-aedf's
constant and Connes' independently-stated asymptotic for the same quantity agree
to twelve decimals at every $L$, which also corroborates the index convention
from a third source. §5.3, and check 2 of the script.

---

## 0. Vocabulary

Used strictly below. The A2 defect this ticket is built on was a stated strategy
read as a companion theorem; the risk of reproducing it one level up is real.

| word | means |
|---|---|
| **proved** | a theorem with a proof in a published or arXived paper, cited by label and line |
| **announced** | the authors say they will do it, or that it can be done; no proof given. Includes "forthcoming paper", "we expect", "suggests the program" |
| **numerical** | supported by the authors' computation, presented as evidence. Not a theorem, and in this corpus not automatically trustworthy either (mg-aedf: drift mode 5) |
| **ours** | derived here. Marked at every occurrence |

---

## 1. What the archimedean proof actually uses

Source: A. Connes, C. Consani, *Weil positivity and trace formula, the
archimedean place*, Selecta Math. (N.S.) **27** (2021) no. 4, Paper 77, 70 pp.;
arXiv:2006.13771, source file `weil-compo.tex`. **Proved.**

The theorem (`:125`, Theorem 1): for $g\in C_c^\infty(\mathbb R_+^*)$ with support in
$[2^{-1/2},2^{1/2}]$ and $\widehat g(i/2)=\widehat g(0)=0$,
$$W_\infty(g*g^*)\;\ge\;\operatorname{Tr}\big(\vartheta(g)\,\mathbf S\,\vartheta(g)^*\big).$$
The sharp form (`:1958`, Thm. `mainthmfine`) drops the condition at $0$ at the cost of
$-c\,|\widehat g(0)|^2$ with $13<c<17$ (`:2002`).

### 1.1 The chain, ingredient by ingredient

| # | ingredient | where | what it does |
|---|---|---|---|
| **I1** | Weil's criterion, reduced to compactly supported test functions and finitely many linear conditions $\tilde g(z)=0$, $z\in F\supset\{0,1\}$, $F\cap Z=\emptyset$ | `:2075` (Prop. `mainprop`), after Yoshida | makes the problem local-in-$\lambda$ and gives a **fixed finite** budget of admissible conditions |
| **I2** | The twist $\Delta^{1/2}f(x)=x^{1/2}f(x)$, converting $f\mapsto\bar f^{\sharp}$ into the $C^*$-involution $f\mapsto f^*$, and Mellin-on-the-critical-line into Fourier | `:111` | this is the $(\star,{}^*)$ of the vision document. Without it there is no square to exhibit |
| **I3** | Boas–Kac: a positive-definite $f$ supported in $I$ has a convolution square root supported in $\sqrt I$ | `:674` (Prop. `boaskac`) | lets "positive definite" be replaced by "$=g*g^*$" without losing the support restriction |
| **I4** | The operator $Q=-(\rho\partial_\rho)^2+\tfrac14$, and Prop. `vanishing2`: $\phi\ge0$ on $C_c^\infty(I)\cap\mathcal J$ $\iff$ $\phi\circ Q\ge0$ on $C_c^\infty(I)$ | `:712-715`, `:747` | implements the vanishing conditions $\widehat f(\pm i/2)=0$ *without* changing the support, by multiplying $\widehat f$ by $z^2+\tfrac14$ |
| **I5** | $W_\infty(f)=-\tfrac12\operatorname{tr}(\widehat f\,u^*\mathrm{d}u)$, via Schwartz kernels and quantized calculus; the split of the first quadrant into a small square $\Delta$ and a big square $\Sigma$ | §1, `:239`–`:487` | turns the explicit formula's archimedean term into an operator trace, and localises the obstruction in $\Delta$ |
| **I6** | The trace-remainder $\delta(\rho)$, explicit in the sine integral; $L:=D+W_\infty=\operatorname{tr}(\vartheta(f)P\widehat PP)$ is positive **with no support restriction** | `:494`, `:585` (Cor. `corlittlesq`) | first square: a trace of a product of two positive operators |
| **I7** | $\delta'$ jumps from $-1$ to $+1$ at $\rho=1$, so $Q\delta=-2\delta_1+\text{smooth}$, so $D\circ Q$ is represented by $-2\,\mathrm{id}+K_I$ with $K_I$ Hilbert–Schmidt | `:765` (Thm. `thmqkey1`) | **essential negativity**: all but finitely many directions are already fine |
| **I8** | Moving $\Delta$ inside $\Sigma$: the pair of projections $\mathcal P_1,\widehat{\mathcal P}_1$ generates a representation of the infinite dihedral group $\mathbb Z\ltimes\mathbb Z/2$, whose non-trivial irreducibles are 2-dimensional and **labelled by the eigenvalues of the prolate differential operator**, the trivial part being the Sonin space | §4, `:873`–`:1193`; Thm. `devil` at `:1132` | replaces $L-D$ by $S-E$ with $S=\operatorname{tr}(\vartheta(f)\mathbf S)$ still positive and $E\le D$. **This is where prolate theory enters, and it enters as a diagonalisation** |
| **I9** | $\epsilon'(1^+)\approx22.9965$ (`:1384`), so $E\circ Q$ is represented by $\mathcal N_I=-2\epsilon'(1^+)(\mathrm{id}-\mathcal K_I)$, $\mathcal K_I$ compact (`:1403`) — a *different* operator from I7's $K_I$, and the one the endgame analyses; the spectrum of $\mathcal K_I$ on $I=[\tfrac12,2]$ computed by discretising $\mathbb R_+^*$ to $q^{\mathbb Z}$, identifying a Toeplitz matrix, and approximating by a finite-rank $T$ | §5–§6 | the endgame |

### 1.2 Where the sign comes from

Only from **I6** and **I8**: $P\widehat PP\ge0$ and $\mathbf S=\mathbf S^*=\mathbf S^2$, so
$\operatorname{tr}(\vartheta(g)\mathbf S\vartheta(g)^*)=\|\mathbf S\vartheta(g)^*\|_{HS}^2\ge0$.
An involution and a square, in the vision document's sense. Everything else is
sign-*preserving bookkeeping*: I4 keeps positivity while imposing conditions, I7
and I9 bound a remainder.

The abstract of arXiv:2006.13771 says this in one sentence (`:86`): *"The root of
the positivity is the trace of the scaling action compressed onto the orthogonal
complement of the range of the cutoff projections associated to the cutoff in
phase space, for $\Lambda=1$."*

Note also **what supplies the sign is not the prolate functions.** They supply
the *labels* of the two-dimensional pieces in I8, i.e. the bookkeeping that makes
$E$ computable. `citation-audit.md` §4.5 already recorded the analogous fact on
the CC 2023 side ("the construction only uses the prolate vectors without any
reference to $QW_\lambda$"). It is worth stating in the sharper form: **prolate
theory is the coordinate system, not the mechanism.**

### 1.3 The endgame turns on three numbers, all specific to $I=[\tfrac12,2]$

From `:1881`–`:1944`:

1. $\mathcal K_I$ has **exactly one** eigenvalue $>1$, and only just: $\lambda_{\max}=1.05158$.
2. The next one is $\lambda_2=0.686494$, so the complement has a gap $c=1-\lambda_2>0.2278$.
3. The offending eigenvector $\zeta$ satisfies $\langle\zeta\mid\xi_0\rangle\approx0.94865$,
   where $\xi_0$ is the constant function — i.e. **the bad direction is 95%
   aligned with the character $\widehat g\mapsto\widehat g(0)$**, which I1 permits
   as a condition.

Lemma `first` (`:1900`) then says a rank-one negative $-b|\langle\zeta\mid\xi\rangle|^2$
can be absorbed by $a|\langle\xi_0\mid\xi\rangle|^2+c\|P_\zeta\xi\|^2$ **iff**
$b(a+c)\le a(b+c)|\langle\zeta\mid\xi_0\rangle|^2$ — a condition on the overlap.
With $b=0.05158$, $c>0.2278$ and overlap $0.94865$ it holds, with room. Change
any of the three numbers materially and the proof stops.

That is the shape of the archimedean endgame: **a finite-dimensional bad
subspace, a spectral gap on its complement, and an alignment between each bad
direction and an admissible linear condition.** Any semilocal analogue must
produce all three.

---

## 2. What survives at a finite place

| ingredient | status semilocally | note |
|---|---|---|
| **I1** Weil's criterion | **proved**, and it is *why* the semilocal setting is the right one: Connes' survey states that proving positivity for $Y_S$, all finite $S$, is equivalent to RH (`rhready.tex:371-374`) | unchanged. But see §3.4: the budget $F$ is fixed once and for all |
| **I2** the twist and the involution | **survives verbatim** — it is a statement about $C_c^\infty(\mathbb R_+^*)$, which is the *same algebra* at every place. The places enter only through which distribution is being tested | the $(\star,{}^*)$ is not the missing ingredient |
| **I3** Boas–Kac | **survives verbatim**, same reason | |
| **I4** the operator $Q$ | **survives verbatim**. $Q=-(\rho\partial_\rho)^2+\tfrac14$ acts on test functions on $\mathbb R_+^*$; Prop. `vanishing2` is stated for an arbitrary functional $\phi$ and an arbitrary symmetric interval | see §5.4 — this bears on Gate 2 |
| **I5** the trace-formula representation | **proved semilocally**, and this is Connes 1999. The survey states it (`rhready.tex:1233-1238`) in the form $-\sum_{v\in S}W_v(f)=\log(TW)f(1)+\operatorname{Trace}\big(\vartheta(f)(1-P^S_T-\widehat P^S_W)\big)$, "perfectly analogous" to the archimedean case, with $P^S,\widehat P^S$ built from the semilocal module | **the framework is not the gap** |
| **I6** positivity of $\operatorname{tr}(\vartheta(f)\mathbf S_S)$ | **survives trivially as positivity**: $\mathbf S_S$, the projection onto $\mathfrak S_\lambda(X_S,\alpha)$, is an orthogonal projection in a Hilbert space, so $\operatorname{tr}(\vartheta(g)\mathbf S_S\vartheta(g)^*)\ge0$ regardless. **What does not survive is the comparison** — no semilocal $\delta$, $\epsilon$, or $L$ is defined anywhere | §3.1 |
| the radical of $QW$ contains $\operatorname{range}\mathcal E$ | **proved**, and it is a statement about the *global/semilocal* form, not the archimedean piece (Connes 1999; quoted at `Spectraltriples.tex:699`, `rhready.tex:1160`) | the corpus's near-null direction rests on this, and it is on the right side of the gap |
| the Sonin space itself | **proved semilocally, as a space**: CCM Theorem 2 (`mainc2m24fine.tex:1022`) gives a *hilbertian* isomorphism $\theta_S:\mathfrak S_\lambda(\mathbb R,e_\infty)\to\mathfrak S_\lambda(X_S,\alpha)$ | "hilbertian", not unitary — CCM are explicit that $\eta_S$ is not unitary (`:845` Rem., (i)) and that the pairing is $\langle\theta_S f\mid\eta_S g\rangle=\langle f\mid g\rangle$ (`:1000`). So the reservoir exists; its *metric relation to the archimedean one* is a duality, not an isometry |
| **I7** essential negativity | **not established.** There is no semilocal $\delta$, hence no jump, hence no $-2\,\mathrm{id}+K$ | §3.1 |
| **I8** the dihedral decomposition | **half survives.** A pair of projections always decomposes (this is Halmos, not arithmetic). What is missing is the *labels*: the spectrum of $P^S\widehat P^SP^S$ | §3.1 — this is the whole of the semilocal-prolate-operator programme |
| **I9** the spectral analysis | **not attempted anywhere** | |

**One local fact worth recording because it is concrete and cuts against the
naive picture.** CCM prove (`mainc2m24fine.tex:910`, Prop. `soninppp`) that at a finite
prime the $\mathbb Z_p^*$-invariant part of $\mathfrak S_1(\mathbb Q_p,e_p)$ is **one-dimensional**,
spanned by $\sigma_p=\epsilon_0-\tfrac1p\epsilon_1$, self-dual under $\mathcal F_{e_p}$. So
"the infinite reservoir of positivity" has no finite-place analogue as a local
object; the semilocal Sonin space gets its size entirely from the archimedean
tensor factor, with each finite place contributing one line. **Proved**, and it
is why the semilocal Sonin space is isomorphic to the archimedean one rather
than larger.

---

## 3. What does not survive — four statements

### 3.1 There is no semilocal Slepian–Pollak, and that is the gap

The archimedean argument needs, at I8, not merely that $\mathcal P_\lambda$ and
$\widehat{\mathcal P}_\lambda$ are two projections, but that the angle operator
$\mathcal P_\lambda\widehat{\mathcal P}_\lambda\mathcal P_\lambda$ is **diagonalised by an explicitly
known family** — the prolate spheroidal wave functions — with an explicitly known
spectrum, and that a *differential operator* commutes with it. That is the
Bell Labs miracle (Slepian–Pollak 1961); Connes' 2026 survey calls it exactly
that (`rhready.tex:1293`: *"the miraculous existence, discovered by the Bell Labs
group, of a differential operator $PW_\lambda$ commuting with the angle
operator"*).

Semilocally, $P^S_T$ and $\widehat P^S_W$ exist and the trace formula holds
(I5, **proved**). The spectrum of $P^S\widehat P^SP^S$ is **not known**. The
entire content of "find the semilocal analogue of the prolate operator" is:
produce the operator that would make it computable. CCM say so
(`mainc2m24fine.tex:197-198`, **announced**): *"the fact that the expected UV
behavior is realized by the negative spectrum of the prolate operator suggests
the tantalizing program of finding the semilocal analogue of the prolate
operator. We expect that the use of such operator-theoretic tools in the
semilocal case opens a way to handle Weil's positivity as in [CCweil]."*

So the gap, in one sentence: **the archimedean proof buys its sign with a
compression and pays for it with a diagonalisation; semilocally the compression
is free and the diagonalisation does not exist.**

### 3.2 The prime term is exactly indefinite — *ours*

Connes–Consani, `Spectraltriples.tex:289` (Prop. `Hilbert`, **proved**), write
the corpus's own object as
$$QW_\lambda(f,f)=\underbrace{\int|\widehat f(t)|^2\frac{2\theta'(t)}{2\pi}dt}_{=\,W_\infty(f^**f)}
+\;2\Re\big(\widehat f(\tfrac i2)\overline{\widehat f(-\tfrac i2)}\big)
\;-\sum_{1<n\le\lambda^2}\Lambda(n)\,\langle f\mid V(n)f\rangle,$$
$$\langle f\mid V(n)g\rangle=n^{-1/2}\big((f^**g)(n)+(f^**g)(n^{-1})\big).$$

Put $x=\log u$, $L=2\log\lambda=\log\mu$, $a=\log n$. Then $V(n)$ is the
compression to $L^2([-\tfrac L2,\tfrac L2])$ of $n^{-1/2}(T_a+T_a^*)$, $T_a$ the
translation by $a$. Multiplication by $e^{i\pi x/a}$ is a unitary of that space
and conjugates $T_a$ into $-T_a$. Hence:

> **Observation (ours, elementary).** $V(n)$ is unitarily equivalent to $-V(n)$.
> Its spectrum is exactly symmetric about $0$, at every $\lambda$, and
> $\|V(n)\|=2n^{-1/2}\cos\!\big(\pi/(m+2)\big)$ with $m=\lceil L/\log n\rceil-1$.

Check 1 of the script confirms both (spectrum symmetric to $10^{-15}$; the norm
matches the closed form at every row, on the full space and on the even sector
that carries Connes–Consani's matrix $\sigma^+$). The closed form is the
Boas–Kac bound the archimedean paper itself invokes at `weil-compo.tex:842`.

Three consequences, and one warning.

- **No compression of a projection can produce the prime terms.** A compression
  $\vartheta(g)\Pi\vartheta(g)^*$ is positive; $V(n)$ is symmetric about zero. So
  the mechanism of §1.2 does not extend to them, even in principle.
- **The prime terms do not get weaker as $\lambda$ grows.** $\|V(n)\|$ increases
  with $L$ towards its ceiling $2n^{-1/2}$. Adding places does not add a small
  perturbation to a proved inequality; it adds a full-strength indefinite term.
- **The number of them grows like $\pi(\mu)+O(\sqrt\mu)$** — one for each prime
  power $n\le\mu=\lambda^2$.
- **Warning, and it is the house rule applied to my own paragraph.** "Exactly
  indefinite" is *invariant* under $W\mapsto-W$. It is a statement that a sign
  cannot come from here, not a statement about which sign. It is admissible as a
  negative result and must not be quoted as if it explained anything about the
  direction of the inequality.

### 3.3 Place-by-place positivity fails — observed and reproduced, not proved

> **STATUS, 2026-08-12 (mg-555b).** The heading used to read *"is false"*. It is
> demoted to *"fails"* because no theorem asserts it — §10.1 records where that
> was looked for, and the authors themselves present it as *"the first fact we
> **report from the numerical computations**"* (`:543`). It is **not** demoted
> further, because §10.2 rebuilds their computation independently and it agrees
> on all five numbers it states; §10.3 exhibits a test function on which one can see it
> without any matrix at all. Read every bullet below as **numerical**, and read
> §10 before quoting any of them.

Connes–Consani, arXiv:2106.01715, the subsections *Sensitivity of Weil positivity,
archimedean place*, *… to the precise value $p=2$* and *Change of sign of smallest
eigenvalue* (`Spectraltriples.tex:542`–`:600`; **numerical**, their computation,
summarised in their own text at `:177` and `:210`). All four figures below were
reproduced in §10.2; the reproduced value is given after each:

- the archimedean contribution $-W_{\mathbb R}$ alone is positive up to $L=\log2$ — the
  smallest eigenvalue of the even matrix at $L=\log2$ is $\sim0.00133$ (`:551`;
  **ours: $0.00133$**) — and **changes sign beyond it**, at $\mu\approx2.2710$
  (`:557`, Figure `testeven1`; their own prose puts the crossing at $2.27$ at
  `:568`, and that is the number, not $2$);
- positivity is restored on $\log2\le L<\log3$ by adding the prime $2$; at
  $\mu=3$ the smallest eigenvalue is $<6\times10^{-8}$ (`:568`; **ours:
  $5.55\times10^{-8}$**);
- replacing $2$ by a real parameter $p$, positivity at $\mu=3$ fails for
  $p=1.9999$ and for $p=2.0005$ — an interval of size $<10^{-3}$ (`:574`;
  **ours: the admissible window is $[1.9999995,\,2.00043]$, width
  $4.4\times10^{-4}$**). Note what this sharpness is *about*: it is the width of
  the admissible window in the **parameter $p$**, not a tolerance to which the
  repair holds;
- the pattern repeats at $3$, $4=2^2$, $5$, $7$ (`:576`–`:600`; **ours: at
  $\mu=3.5$, $\infty+2$ gives $-1.19\times10^{-2}$ and $\infty+2+3$ gives
  $+2.48\times10^{-10}$**).

Two things follow, and they matter more than their status as numerics suggests,
because the theorem they bracket is only claimed at $\mu=2$.

1. **The archimedean theorem is at the edge of its range.** Theorem 1 of
   arXiv:2006.13771 is stated for support in $[2^{-1/2},2^{1/2}]$, i.e. exactly
   $\mu=2$, $L=\log2$; Connes' 2026 survey still states it that way
   (`rhready.tex:1200`). Past that value the object it controls goes negative,
   at $\mu\approx2.2710$ — a margin of $0.271$, or $0.127$ in $L$. There is no
   "extend the archimedean theorem to larger $\lambda$ first": there is nowhere
   to extend it *to*, because the statement fails at $\mu\approx2.271$. **Corrected
   2026-08-12 (mg-555b):** this item previously said "just past that value" and
   "the statement to be extended is false". The first was imprecise — the margin
   is real, if small — and the second overstated a numerical fact as a proved
   one. Neither correction changes the conclusion, which is item 2.
2. **The semilocal statement is about cancellation between places, not about
   places.** Neither $Q_\infty$ (beyond $\mu=2$) nor any $-\Lambda(n)V(n)$
   (§3.2, at any $\mu$) is a positive form. Only the sum is — conjecturally,
   since that is RH.

Independently and **proved**: arXiv:2006.13771's Remark at `weil-compo.tex:842`, item (ii), shows the *simpler* route already fails at $\mu=2$ — $D\circ Q$ is not
negative on $[\tfrac12,2]$; the limit computed there is $\sim+2.98699$. That is
why I8 exists at all.

### 3.4 The condition budget is fixed; the near-radical is not — *ours*

Weil's criterion (I1) fixes a finite set $F$ **once**, and then demands positivity
for **all** $\lambda$ under only the conditions $\tilde g(z)=0$, $z\in F$. The
archimedean endgame spent exactly one such condition ($\widehat g(0)=0$) on
exactly one bad direction, and could only do so because of the $0.94865$
alignment (§1.3).

Meanwhile the dimension of the near-radical grows: Connes–Consani record
$1+\nu(\mu)\sim2\mu$ small eigenvalues of the angle operator
(`Spectraltriples.tex:189`), and correspondingly a *finite but growing* number of
minuscule eigenvalues of $QW_\lambda$ — at $\mu=11$ the smallest is
$2.389\times10^{-48}$ (`:178`, **numerical**).

Nothing here is a contradiction — under RH every one of those eigenvalues is
positive and no condition is needed. The point is about the **method**: I7's
compactness gives "finitely many bad directions *for each fixed $\lambda$*",
which is not the same as "at most $|F|$ bad directions, uniformly in $\lambda$,
each aligned with an element of $F$". Supplying that uniformity is a requirement
the archimedean case never had to face, because it was proved at a single
$\lambda$.

---

## 4. What CCM's strategy adds, and what it leaves open

Source: A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave
operators: semilocal adelic operators*, arXiv:2310.18423 (Oct 2023, rev. May
2024), source `mainc2m24fine.tex`.

### 4.1 Proved there

- **Theorem 1** (`:244`, = Props. `groundstate` and `httransfoS`): the semilocal Hardy–Titchmarsh
  transform $\mathcal V_S=\mathcal M_S\circ\mathcal U_S$ puts the cyclic pair $(\mathcal S,\xi_S)$ in
  canonical form, on $L^2(\mathbb R,dm_S)$ with
  $dm_S(s)=\big|\prod_{v\in S}L_v(\tfrac12-is)\big|^2ds$ — the measure is the
  square modulus of the product of local Euler factors on the critical line.
- **Theorem 2** (`:1022`): $\theta_S$ is a hilbertian isomorphism
  $\mathfrak S_\lambda(\mathbb R,e_\infty)\to\mathfrak S_\lambda(X_S,\alpha)$ — *stability of the
  semilocal Sonin space under enlarging $S$*.
- **Prop. `soninppp`** (`:910`): the $\mathbb Z_p^*$-invariant part of $\mathfrak S_1(\mathbb Q_p,e_p)$ is
  one-dimensional (§2 above).
- A metaplectic / enveloping-algebra description of the archimedean prolate
  operator (`:1148`), and a rigidity result: the discrepancy coefficients $d_n$
  vanish precisely for $(\mathcal S,\xi_\infty)$ (`:1312`).

### 4.2 The strategy, quoted rather than paraphrased

`:197-198`, **announced**:

> *"the operator theoretic aspect of the present paper provides a more precise
> strategy for addressing the semilocal Weil positivity by comparing the trace
> functional associated to the operator — which is automatically positive for a
> selfadjoint operator — with the Weil functional. The conditioning, by the
> radical of the Weil quadratic form, that worked for the scaling operator in the
> infrared case will be implemented automatically by the orthogonality of the
> positive and the negative part of the spectrum of the semilocal prolate
> operator, whose corresponding negative eigenspace was identified in [CM] to the
> Sonin space."*

What this adds over 2006.13771 is real and worth naming: it proposes that the
*conditioning* — the ad-hoc finite set of linear conditions of §1.3 and §3.4 —
should come for free, as the spectral projection of a single self-adjoint
operator. That is a genuine structural idea, and it is the answer to §3.4's
uniformity problem *if* the operator exists.

Note what the sentence does **not** contain: any comparison term. "Comparing the
trace functional with the Weil functional" is I6+I9 — the 60 pages that were the
work at the archimedean place. Semilocally the comparison has not been begun.

### 4.3 What is deferred, and why there are two candidates

The candidate is $\mathbf W_{\lambda,S}=(H+\tfrac12)^2+\lambda^2N_S$ (`:843`),
$N_S$ the grading of the orthogonal polynomials for $dm_S$. Deferred:

- **its Jacobi coefficients for general $S$** — "deferred to a forthcoming paper"
  (`:259`). Without them the spectrum is not computable, so the property that
  makes it usable is not checkable;
- **whether its negative eigenspace is the semilocal Sonin space**. The
  archimedean fact (Connes–Moscovici, PNAS 2022, up to a finite-dimensional
  discrepancy) is described as *"another constraint in the search of the
  semilocal analogue"* (`:266`) — i.e. a test the candidate must pass, not a
  proved property;
- **a second candidate**, via *"the Weil representation of the metaplectic cover
  of the algebraic group $SL_2(\mathbb A_S)$"*, also to a forthcoming paper (`:270`).

Why a second candidate at all: because the first is not canonical. CCM's own
Remark (`:845`) records that $N_S\circ\eta_S\ne\eta_S\circ N_\infty$ unless
$S=\{\infty\}$; that there is *another guess* — multiplication by $|x|_S^2$ plus
its Fourier conjugate; and that the two disagree, with the discrepancy computed
explicitly at `:848-863`. So the semilocal Hermite operator is guess-dependent,
and an adelically canonical construction is wanted. **That is what the deferred
second candidate is for.**

### 4.4 Status as of Connes' own 2026 survey

A. Connes, *The Riemann Hypothesis: past, present and a letter through time*,
arXiv:2602.04022 (Feb 2026), source `rhready.tex`. Checked because it is the
principals' current statement of where the programme is.

- The proved archimedean positivity is still stated with the same hypotheses:
  *"the compression of the scaling $\vartheta(f)$ to Sonin's space was shown to be
  the root of Weil's positivity at the archimedean place on test functions with
  support in the interval $[2^{-1/2},2^{1/2}]$"* (`:1298`), and the theorem is
  restated verbatim at `:1198-1200`.
- The semilocal trace formula is presented (`:1228`–`:1240`) — the framework, not
  a positivity result.
- The survey's own subsection *Remaining steps* (`:1174`) lists exactly two missing items,
  and **neither is semilocal positivity**: (i) that the smallest eigenvalue of
  $QW_\lambda$ is simple with even eigenvector; (ii) that $k_\lambda$ is a good
  enough approximation of $\theta_x$.
- No paper introducing the second candidate had appeared as of this pass (**re-checked
  against primary sources 2026-08-12, still not found — §9**); the
  most recent CCM paper, *Zeta Spectral Triples* (arXiv:2511.22755, Nov 2025), is
  on a different construction and mentions neither the Weil representation nor
  semilocal positivity. A further CCM paper, *Riemann Zeros via Weil Forms: From
  Prolate Functions to Cohomology*, is cited as **in preparation** (`:1478`).

**Conclusion of §4, and it is the ticket's question 3.** CCM add a *shape* for
the conditioning step and a proved stability theorem for the space the sign would
have to live in. They do not add a comparison, a sign, or a computable operator.
Three years after the archimedean theorem, and two and a half after
arXiv:2310.18423, the semilocal case remains **announced**.

---

## 5. Where the corpus's objects sit

### 5.1 On the archimedean side of the gap

Every object the corpus manipulates — $\widehat P$, $\chi_n$, $h_{0,\lambda}$,
$h_{4,\lambda}$, the concentration eigenvalues, $\|(1-\widehat P)h_\lambda\|^2$ —
is data of the **archimedean** angle operator $\mathcal P_\lambda\widehat{\mathcal P}_\lambda\mathcal P_\lambda$
on $L^2(\mathbb R)^{\mathrm{ev}}$. That is the diagonalisation that exists (§3.1). The
corpus contains no semilocal projection, no $X_S$, no $L_p$ factor, no $dm_S$,
and no Sonin space at all (`citation-audit.md` §4.2 row 15).

So: the corpus's *tools* are entirely on the proved side. Its *target*
(`start.tex:39`) is on the other side.

### 5.2 The corpus's central estimate is the bridge quantity — and it is Connes' own figure

$QW_\lambda$ is the semilocal form (it contains the primes $p\le\lambda^2$;
mg-9433 established this verbatim). $\mathcal E h_\lambda$ is built from archimedean
prolate data. So `start.tex:39`'s
$$QW_\lambda(Eh_\lambda)\asymp1-\chi_4$$
is *the semilocal form evaluated on an archimedean-built vector* — an instance of
exactly the comparison §3.1 says is missing. That is a better place to be
standing than "beside the literature".

It is also, in the principals' letters, already published as an observation.
arXiv:2602.04022, subsection *The Poisson formula and the approximation $k_\lambda$ of
$\theta_x$* (`rhready.tex:1144-1160`), at `:1149`:

> *"The numerical computation of the smallest eigenvalue $\epsilon(\lambda)$ of
> $A_\lambda$ … shows that $\epsilon(\lambda)$ tends exponentially fast to $0$ as
> a function of $\mu=\lambda^2$. In fact a careful analysis reveals a striking
> similarity (Figure …) between the behavior of $\epsilon(\lambda)$ and of the
> angular function $1-\chi_2(\lambda)$."*

with, in the same paragraph, $1-\chi_2\sim\frac{2^{14}}{3}\sqrt2\,\pi^5e^{-4\pi e^L+9L/2}$
from Fuchs, and the footnote $\chi_k(\lambda)^2=\Lambda_{2k}(c)$, $c=2\pi\lambda^2$.
By that footnote **Connes' $\chi_2$ is prolate index 4, i.e. the corpus's
$\chi_4$** (`index-convention.md`). And the survey's $k_\lambda:=\mathcal E(h_\lambda)$
with $h_\lambda$ *"the only linear combination of $h_{0,\lambda},h_{4,\lambda}$
with vanishing integral"* (`:1159`) is `start.tex:138-153` and `:171` — same
letters, same construction, same $k_\lambda$.

Three consequences, stated separately because they have different signs:

1. **The identification of the scale is not the corpus's.** `start.tex:39` and
   `:88-91` assert that the defect is controlled by a prolate concentration
   eigenvalue; that is now a published statement with a published asymptotic.
   (`citation-audit.md` §4.6 found the *pointer* "Figure 4" unsupported and that
   stands — the survey has two figures and neither is numbered 4.)
2. **The corpus's version is a different quantity, and weaker in one direction.**
   Connes compares the *smallest eigenvalue* $\epsilon(\lambda)$ to $1-\chi_2$;
   `start.tex:39` compares the *value of the form at $\mathcal E h_\lambda$*. By the
   variational principle the second is $\ge$ the first (after normalisation), so
   the corpus's estimate would give Connes' upper bound and not his lower bound.
   Recording this because it is the difference between "reproducing a figure" and
   "proving half of what the figure shows" — and the second is a real, if small,
   thing to aim at.
3. **It does not immediately deliver the survey's remaining step (ii).**
   $k_\lambda\approx\theta_x$ would follow from a Rayleigh-quotient bound *plus* a
   spectral gap; but the near-radical is $\sim2\mu$-dimensional with all its
   eigenvalues minuscule (§3.4), so the gap is minuscule too and the variational
   argument gives almost nothing. This is an obstruction the corpus has not
   noticed and should.

### 5.3 An audit row superseded, and U4 closed — *ours*

`citation-audit.md` §4.2 row 14 reads: *"$1-\chi_4$ as the controlling scale …
not used. Connes–Consani report the smallest eigenvalue $s(L)$ decaying
exponentially in $\mu=e^L$ … with no identification of the rate.
**corpus-specific.**"* That was correct for arXiv:2106.01715, the paper it
checked. It is not correct as a statement about the literature: arXiv:2602.04022
(`rhready.tex:1149-1150`) identifies the rate, names it $1-\chi_2$, and gives the Fuchs asymptotic.
§4.4 item 1 of that note ("the mirrored endpoint constraint and its
quantification") is untouched by this; row 14 is not.

Separately, `citation-audit.md` §7 item **U4** — mg-aedf's Fuchs constant
$4\sqrt\pi\,8^nc^{n+1/2}e^{-2c}/n!$, source confirmed, constant never checked —
**closes**. Connes states the asymptotic for $1-\chi_2$ independently; with
$\chi=\sqrt\Lambda$ so that $1-\chi_2=(1-\Lambda_4)/2$, the two expressions must
agree exactly if both are right. Check 2 of the script: ratio
$1.000000000000$ at $L=1.0,1.5,2.0,2.5,3.0$. This also corroborates
`index-convention.md` from a third source, independently of both documents it
used.

### 5.4 The two places the corpus touches the missing ingredient

Not "it stops short" without qualification. There are exactly two contacts, and
one of them is a recorded failure.

- **`start.tex:264-273`.** *"For the prolate Sturm–Liouville operator $L_c$ and
  the relevant concentration projector $P$, $[L_c,P]=0$. When the prime part of
  the explicit formula is written in terms of multiplicative translations,
  commutator matrix elements localize to boundary-crossing strips."* The first
  half is the Bell Labs miracle (§3.1) at the archimedean place. The second half
  is about $V(n)$ — the object of §3.2 — and it is the right instinct: the prime
  terms are translations, and translations interact with a support cutoff at the
  boundary. What it is not is a sign: §3.2 shows $V(n)$'s spectrum is exactly
  symmetric, so no localisation statement about it can produce one on its own.
- **`start.tex:292-295`.** *"Prime–archimedean cancellation at low frequency. A
  direct symbol calculation does not yield the hoped-for cancellation; the
  completed prime and $\Gamma$-terms can reinforce rather than cancel there."*
  This is an attempt at exactly the cancellation §3.3 says the semilocal theorem
  must be about, and it is honestly reported as having failed. Given §3.3 — that
  the required cancellation is sharp to $10^{-3}$ in $p$ at $\mu=3$ — a symbol
  calculation at low frequency failing is what one should expect. The negative
  result is consistent with the literature and worth keeping.

**And one thing to hand to Daniel with Gate 2** (`citation-audit.md` §4.3,
mg-9433 §2). Both prior findings stand: in arXiv:2106.01715, $QW_\lambda$ is one
symbol and no operator $Q$ exists. But an operator $Q$ *does* exist in the
archimedean paper — $Q=-(\rho\partial_\rho)^2+\tfrac14$ at `weil-compo.tex:712-715`,
with Prop. `vanishing2` at `:747` making precomposition with it equivalent to
imposing $\widehat f(\pm i/2)=0$ while preserving support and positivity. It acts
on the **test function**, before the functional, and the two directions it
handles are the same two directions as $\mathcal S_0^{\mathrm{ev}}$'s
$f(0)=\widehat f(0)=0$, in a different normalisation. So `start.tex:41-44`'s
reading — "$Q$ removes the expected low-dimensional exceptional sector" — has a
real referent in the literature; it is just in a *different paper* from the one
supplying $QW_\lambda$, and the coincidence of the letter $Q$ across the two is a
trap. Recording, not resolving: Gate 2 is Daniel's.

### 5.5 What would have to be true for the corpus to contribute

In the corpus's own objects, and matching the archimedean template of §1.3:

| | requirement | corpus status |
|---|---|---|
| **(A)** | `(*)` with a **sign**: $QW_\lambda(\mathcal E h_\lambda)=C_\lambda(1-\chi_4)+o(1-\chi_4)$ with $C_\lambda\ge c>0$ | already written down at `start.tex:358-368`; **unproved**. This is the sign-carrying form; the abstract's `:39` is not (§6) |
| **(B)** | the same for the whole family $\mathcal E(\varphi_m)$, $m\le\nu(\mu)\sim2\mu$, not for $m=4$ alone | not attempted. Positivity needs every near-null direction; the corpus's vector is one of $\sim2\mu$ |
| **(C)** | a lower bound on $QW_\lambda$ on the orthogonal complement of that span, uniform in $\lambda$ — the analogue of $1-\lambda_2>0.2278$ | not attempted, and not visible in the corpus's vocabulary |
| **(D)** | arithmetic that survives the regime: the quantities are $\sim10^{-48}$ at $\mu=11$, and mg-aedf bounds double precision as meaningless at $c=20$, i.e. $\mu\approx3.2$ | **currently fails.** `citation-audit.md` §6 records CCM at 200 digits |

(A) alone would be a small, honest, publishable contribution to the *other* live
route — the survey's remaining step (ii) — subject to §5.2 item 3. (A)+(B)+(C)
would be a semilocal positivity theorem, which is the thing nobody has. The
distance between them is the honest measure of the gap.

---

## 6. The house rule, applied to this note

> **Is any statement in it false for $-W_\lambda$?**

Checked line by line; the outcome is mixed and is reported as such.

**Sign-sensitive (false under $W\mapsto-W$), and these carry the note:**

- §1.2: the sign comes from $\operatorname{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)\ge0$.
  Under $W_\infty\mapsto-W_\infty$ the theorem would read
  $-W_\infty(g*g^*)\ge\operatorname{Tr}(\cdots)\ge0$, contradicting the positivity
  Yoshida proved by explicit computation. Involution and square, as required.
- §1.1 I7 and I9: $\epsilon'(1^+)\approx+22.9965$, so $\mathcal N_I=-2\epsilon'(1^+)(\mathrm{id}-\mathcal K_I)$
  is *negative* up to finitely many directions, which is the direction needed for
  $W_\infty=S-E$. Flip the sign and the argument gives the opposite conclusion.
- §1.3: $\lambda_{\max}>1$ (not $<1$) is what forces a condition at all; the
  inequality $b(a+c)\le a(b+c)|\langle\zeta\mid\xi_0\rangle|^2$ is not symmetric
  in the sign of $b$.
- §3.3: "the archimedean contribution ceases to be **positive** past
  $\mu=2.271$ and positivity is **restored** by the prime 2" — under a global
  sign flip this becomes a statement about negativity being restored, which is a
  different (and false) claim about the same figures. §10.2 re-runs the
  computation with the sign conventions rebuilt from the explicit formula rather
  than inherited, which is the strongest form of this check the section admits.

**Sign-blind, and flagged in place rather than removed:**

- §3.2, the indefiniteness of $V(n)$. Invariant by construction. Its role is
  purely negative — it excludes a mechanism — and §3.2's fourth bullet says so.
- §2's survival table rows for I2, I3, I4: "this object is place-independent" is
  a statement about an object, not about a sign. Correct, and load-bearing only
  as a way of narrowing where the gap is.

**And the same test turned on the corpus, which is the point of §5.5(A):**
`start.tex:39`'s $QW_\lambda(Eh_\lambda)\asymp1-\chi_4$ is **sign-blind** — an
order-of-magnitude relation, satisfied equally by $-QW_\lambda$. `start.tex:361-368`'s
$QW_\lambda(Eh_\lambda)=C_\lambda(1-\chi_4)+o(1-\chi_4)$ with $0<c\le C_\lambda\le C$
is **not**. The corpus's own route already contains the sign-carrying version;
its abstract leads with the one that does not. That is worth fixing in
`start.tex`, and is on the list for Daniel rather than for us.

---

## 7. Provenance

To the standard of `citation-audit.md` §9, so rows above can be weighted.

**Read as primary source, in full or in the cited sections, from arXiv LaTeX
downloaded from `arxiv.org/e-print/`:**

- `weil-compo.tex` (arXiv:2006.13771). Introduction in full (`:85`–`:238`); the
  support-and-boundary-conditions section in full (`:663`–`:872`); the
  small-square section at statement level (`:488`–`:662`); the proof of Theorem 1
  in full (`:1873`–`:2010`); the explicit-formula and positivity-criterion
  appendices (`:2033`–`:2086`). The sections in between were read at **statement
  level only** — Thm. `devil`, Prop. `propcompact`, and the numbers at `:1384`,
  `:1678`, `:1726`. Their proofs I did not read.
- `mainc2m24fine.tex` (arXiv:2310.18423). Abstract and introduction in full
  (`:162`–`:274`); the semilocal-case section from `:825` to `:1030` in full.
  The cyclic-pair, archimedean and metaplectic sections not read.
- `Spectraltriples.tex` (arXiv:2106.01715). Introduction `:160`–`:200`; the
  semi-local Weil quadratic form and its Hilbert-space statement `:206`–`:300`;
  the three sensitivity subsections `:542`–`:600`. Consistent with, and
  extending, what `citation-audit.md` §10 read of the same file.
- `rhready.tex` (arXiv:2602.04022). the subsections of *The strategy and the next small steps*
  (`:1041`–`:1175`) and of *Geometric Perspectives* (`:1176`–`:1311`) in full, conclusion and the bibliography entries cited.

**Rests on an abstract or on metadata, not the body:** arXiv:2511.22755 (*Zeta
Spectral Triples*) — abstract and metadata only, via its arXiv page; used only
for the negative statement in §4.4 that it does not contain the second candidate.
The claim "no paper introducing the second candidate had appeared" is a **search
result**, not a proof of absence: arXiv full-text search, the math.NT recent
listing, and Connes' own 2026 bibliography, none of which show one. Weight
accordingly. **Upgraded 2026-08-12 (mg-6d7e): still a negative, but no longer a
search result — §9 gives the sources and the method.**

**Derived here, not taken from any source:** the unitary equivalence
$V(n)\sim-V(n)$ and the norm formula (§3.2); the condition-budget observation
(§3.4); the Rayleigh-quotient direction and the gap obstruction (§5.2 items 2
and 3); the U4 closure by cross-check (§5.3); the whole of §5.5. Each is marked
*ours* at the point of use.

~~**Not done, and it would be the natural next check:** I did not reproduce
Connes–Consani's sensitivity figures (`Spectraltriples.tex:548`–`:572`, labels
`testeven`, `testeven1`, `testeven2`, `testeven3`) — the archimedean sign change
past $L=\log2$ and its repair by the prime $2$. §3.3 rests on their statement of their own numerics. It
is the single most consequential **numerical** claim this note leans on, and
unlike the rest of the note it is not checkable in one minute from a paper. It is
also, per `citation-audit.md` §6, in the regime where the corpus's own arithmetic
is unsound, so reproducing it is not a small job.~~
**DONE 2026-08-12 (mg-555b): §10.2 and [`verify_arch_positivity.py`](verify_arch_positivity.py).**
All five of their reported numbers reproduced. §3.3
no longer rests on their statement of their own numerics. The last sentence
above was half right: the *repaired* eigenvalues are indeed in the regime
`citation-audit.md` §6 warns about ($10^{-8}$ down to $10^{-12}$) and are
reported as reproductions rather than verifications; the *sign change itself* is
not — it happens at $10^{-3}$ against $O(1)$ entries, and it was a small job.

**The claim in this note that would do the most damage if wrong** is §5.2 — that
Connes' $1-\chi_2$ is the corpus's $1-\chi_4$, and hence that the identification
of the scale is published. It rests on the footnote at `rhready.tex:1150`
($\chi_k(\lambda)^2=\Lambda_{2k}(c)$, $c=2\pi\lambda^2$) plus
`index-convention.md`, and it is independently confirmed by check 2 of the
script: two constants written down by different people for two quantities agree
to twelve decimals only if the quantities are the same.

---

## 8. Open, and left open deliberately

| # | item | why it is open |
|---|---|---|
| S1 | ~~Does the semilocal angle operator $P^S\widehat P^SP^S$ have *any* known spectral description, even partial?~~ **ANSWERED 2026-08-12 (mg-0bd7): partially yes, and the partial is sharply located — §11** | was: absence over CCM's semilocal section and the survey's *Geometric Perspectives*. Now: at **one** non-archimedean place the pair is completely and explicitly described by Burnol (IMRN 2000), and the angle operator there is **degenerate** — the two cutoffs commute. Semilocally nothing: the cutoff is by the *product* module, so it does not factor, and Connes 1999 substitutes a construction ($\psi\mapsto\psi\otimes1_R$) for a spectrum at exactly that step. §11 says where I looked |
| S2 | ~~Is the archimedean positivity theorem *known* to be sharp at $\mu=2$, or only numerically observed to fail past it?~~ **ANSWERED 2026-08-12 (mg-555b): only numerically observed — and now independently reproduced. §10** | was: rests on Connes–Consani's figures, no theorem found. Now: no theorem exists (§10.1 says where I looked and how the authors' own prose describes the figures), the numerics are theirs *and* ours (§10.2), an explicit witness function needs no matrix (§10.3), and the sharpness is at $\mu=2.271$, not $2$ |
| S3 | ~~Has the second candidate semilocal prolate operator appeared since Feb 2026?~~ **RE-CHECKED against primary sources 2026-08-12 (mg-6d7e): NOT FOUND. A clean negative — §9** | was §7: search-result-level evidence only. Now: author listings for all three principals enumerated, the survey's LaTeX read for the words themselves, version histories checked. §9 says where I looked, so the next person can tell this negative from an unexamined one |
| S4 | Does the corpus's `start.tex:264-273` commutator localisation have a semilocal analogue — i.e. does $[\mathbf W_{\lambda,S},P^S]=0$ for either CCM candidate? | This is the natural corpus-side question raised by §3.1 and §5.4, and answering it needs the deferred Jacobi coefficients. Recorded, not pursued: it is a proof attempt, and this ticket is not |
| S5 | ~~`citation-audit.md` §4.2 row 14 and §4.4 need the narrowing of §5.3 applied in place~~ **DONE 2026-08-12 (mg-6d7e)** | row 14 now states the narrowing itself rather than pointing here, and §4.4 carries an end note scoping it: one entry joins that section's "removed because published" paragraph, and all five numbered items — item 1 included — stand. One correction to this note's own framing is recorded in §9 |

---

## 9. Appendix — S5 applied, S3 re-checked (added 2026-08-12, mg-6d7e)

*Appended. Nothing above is deleted; the two rows closed are annotated in place in §8,
and §4.4 and §7 point here. Both items are branch-independent: they are worth having
whichever of the vision document's (a)/(b)/(c) directions the project takes.*

### 9.1 S5 — the row-14 narrowing, applied in place

`citation-audit.md` §4.2 row 14 now **states** the narrowing instead of pointing at this
note, and §4.4 carries an end note scoping it. What changed there:

- **Row 14.** The "not used" cell now says *not used in arXiv:2106.01715*, and carries
  the survey's sentence, the Fuchs asymptotic and the index footnote inline, so a reader
  who never follows a link is not left with a verdict that reads as current.
  "corpus-specific" is struck rather than deleted.
- **§4.4.** One entry — the identification of the controlling scale — joins that
  section's *"removed from an earlier draft, because they are published"* paragraph.
  **No numbered item leaves the list**, so the item numbers other notes cite are stable.
- **§11.** Two sentences corrected; see 9.2.

**The distinction the annotation preserves.** Row 14 was **right about the paper it
checked** and wrong only as a claim about the literature. Those are different statements
and only the second is false. This corpus will keep producing findings of that shape —
a check against a named source, phrased as though it ranged over everything — and the
repair is to restore the scope, not to strike the finding.

### 9.2 A correction to this note's own framing of that row — *ours*

§5.3 above, and `citation-audit.md` §11's heading, present row 14 as a **correct finding
that decayed because a new source appeared**. That framing is wrong, and it flatters us.

arXiv:2602.04022 is dated **3 Feb 2026**. `citation-audit.md` was written **2026-08-12**
and says so at its head. The survey therefore predates the audit by six months — and
`citation-audit.md` §6 lists it, in its own words, as *"Connes' own current survey — the
natural place to check positioning before writing"*. The audit named the source, said it
was the right one to read, and did not open it.

So row 14 is a **scoping defect**, not a decayed finding: a check against one paper
written as a claim about the literature. §11's heading is corrected in place. §5.3's
"That was correct for arXiv:2106.01715, the paper it checked" is accurate as it stands
and is left alone; it is the *decay* reading — which appears in §11's old heading and in
the vision document's amendment 3 §5 — that is unsupported.

Recording this rather than quietly fixing the heading, because the two failure modes want
different responses. A decayed finding needs re-checking on a schedule. A source named
and not opened needs nothing but opening it, and the audit's own §7 discipline of
recording what was **not** reached would have caught it.

### 9.3 S3 — the second candidate has not appeared

**Answer: not found as of 2026-08-12.** CCM's second candidate semilocal prolate
operator — the one via *"the Weil representation of the metaplectic cover of the
algebraic group $SL_2(\mathbb A_S)$"*, deferred at `mainc2m24fine.tex:270` (Oct 2023,
rev. May 2024) — has not appeared, and is not cited as existing by anything the
principals have published since.

This is the **expected** outcome and it is a complete answer. What follows is where I
looked, so that the next person can tell this negative apart from nobody having looked.

**1. arXiv author listings, all three principals, enumerated to the present.**

| author | everything since Connes' survey (arXiv:2602.04022, 3 Feb 2026) |
|---|---|
| Connes | arXiv:2602.15941 (17 Feb 2026, w. Consani, *On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb Z}$*); arXiv:2606.06604 (4 Jun 2026, w. Consani, *On the Absolute Geometry of $\mathrm{Spec}\,\mathbb Z$*) |
| Consani | the same two, and nothing else — checked on her own listing, not inferred from his |
| Moscovici | **nothing since arXiv:2511.22755** (27 Nov 2025, *Zeta Spectral Triples*) |

Moscovici's silence is the load-bearing row: he is a co-author on **every** paper in the
prolate-operator line (arXiv:2112.05500, arXiv:2310.18423, arXiv:2403.01247,
arXiv:2511.22755), and the deferred candidate is an operator-theoretic construction of
exactly that kind. Both 2026 Connes–Consani papers are the absolute-geometry arc —
perfectoid fields, the Fargues–Fontaine curve, the arithmetic site. Neither abstract
contains *prolate*, *semilocal*, *Weil positivity*, *Weil representation* or
*metaplectic*. Read at **abstract level**, with arXiv:2606.06604's reference list also
read from its HTML rendering: Scholze, Fargues–Fontaine, Lurie and the arithmetic-site
papers, no CCM prolate entry, nothing marked *in preparation*. I did not read either body.

**2. The survey's own text, read as primary source — not its abstract.** I downloaded
`arxiv.org/e-print/2602.04022` and read `rhready.tex` (1861 lines, dated 3 Feb 2026).
Occurrence counts over the whole file: `metaplectic` **0**, `Metaplectic` **0**,
`Weil representation` **0**, `SL_2` **0**. `SL(2` occurs once, at `:692`, as
$H/PSL(2,\mathbb Z)$ in the Selberg-trace-formula discussion — unrelated. So the survey
does not cite the second candidate as existing; **it does not mention it at all.** That
is stronger than §4.4's original statement, which rested on the survey's *Remaining
steps* subsection not listing semilocal positivity.

**3. Version histories, so a silent revision cannot hide one.** arXiv:2602.04022 is
**v1 only** (3 Feb 2026) — it has not been revised, so it cannot have acquired a citation
since. arXiv:2511.22755 is likewise **v1 only** (27 Nov 2025).

**4. The survey's bibliography, entry by entry, for forthcoming CCM work.** Exactly one
CCM item is marked *in preparation*: `\bibitem{c2m2b}` at `rhready.tex:1478-1480`,
*Riemann Zeros via Weil Forms: From Prolate Functions to Cohomology*. **It is not the
second candidate.** It is cited once, at `:1145`, for the existence of the operator
$A_\lambda$ with $QW_\lambda(f,f)=\langle A_\lambda f\mid f\rangle$ — the infrared
object, archimedean-side. An arXiv title search finds no paper of that title as of
2026-08-12 either, so *it* has not appeared. The other two CCM entries are
arXiv:2310.18423 (`c2m`, published Ann. Funct. Anal. **15** (2024) no. 4, Paper 87) and
arXiv:2511.22755 (`c2mzeta`, to appear, CIRM proceedings).

**5. Metadata search.** arXiv `abs:prolate AND abs:semilocal` returns arXiv:2310.18423
and nothing else. `all:prolate AND cat:math.NT`, newest first, has nothing by any of the
three after arXiv:2310.18423.

**What this negative does not cover, stated so it is not over-read.** arXiv and the
principals' arXiv-posted bibliographies only. A journal-only publication, a seminar
announcement, or a preprint on a personal page would not show up — I could not reach
`math.jhu.edu/~kc/Publ2026.pdf` or `alainconnes.org/publications` (both HTTP 403), which
are the two places such a thing would surface first and are the obvious next check for
anyone who wants to tighten this. And absence of a *citation* is not absence of a
*result*: CCM could hold it unpublished.

**Consequence for the direction question: none.** The vision document's amendment 3 §6
puts (a)/(b)/(c) with Daniel. Had the second candidate appeared it would have changed
that question and this note would lead with it. It has not. Two years and nine months
after arXiv:2310.18423 deferred it, and six months after a survey by the senior author
that does not mention it, **both halves of CCM's "more precise strategy" remain
deferred** and §4's conclusion stands unchanged: the semilocal case is still
**announced**.

---

## 10. Appendix — S2 answered (added 2026-08-12, mg-555b)

*Appended. Nothing above is deleted; §3.3, the bottom line's item 4, §6, §7 and §8's row
S2 are annotated in place and point here. Companion script:
[`verify_arch_positivity.py`](verify_arch_positivity.py), four checks, ~2.5 min.*

**The question (§8, S2).** Is the failure of archimedean-only positivity past $\mu=2$
(1) a theorem, (2) a numerical observation, or (3) an artefact of the truncation or the
numerics?

**The answer: (2), and firmly not (3).** No theorem asserts the failure — 10.1 says where
I looked and how the authors describe their own figures. The observation is sound: 10.2
rebuilds the computation from the explicit formula and matches Connes–Consani on all five numbers
they report, and 10.3 exhibits a single test function on which the archimedean
form is negative, with no matrix and no truncation in the argument. One correction to our
own text falls out: the crossing is at $\mu=2.271$, not "just past $2$" (10.4).

### 10.1 No theorem — where I looked, and the mood of the prose

The distinction this ticket turns on is between *"we observe"* and *"one shows"*. Every
occurrence of the failure in the corpus's sources is the first.

**1. arXiv:2106.01715 (`Spectraltriples.tex`, 1958 lines), the paper the figures are in.**
Three statements of the fact, in three registers, and all three name the numerics:

> `:543`, opening the subsection itself: *"The first fact we **report from the numerical
> computations** is that the archimedean contribution **fails to remain positive** when
> extended a bit beyond the value $L=\log 2$."*
>
> `:177`, the introduction: *"… we **test numerically** this positivity for
> larger values of $\lambda$, **showing** that the contribution from the archimedean place
> alone **ceases to be positive** in the upper part of the interval
> $\log(\lambda^2)\in[\log2-0.2,\log2+0.2]\sim[0.493,0.893]$."*
>
> `:210`, the section summary: *"… we **find that** the archimedean contribution
> $-W_{\mathbb R}$ … **ends to be positive** if computed in an interval extending slightly
> beyond the value $L=\log2$ (Figure `testeven1`)."* Two sentences later, of the
> companion claims: *"we **report graphical evidence**."*

The verbs are indicative — *fails*, *ceases*, *ends to be* — so the authors do assert the
fact; they are not hedging it. What they never do is *prove* it. There is **no theorem,
proposition, lemma or corollary environment anywhere in `:540`–`:640`**, the three
sensitivity subsections in full; the sections consist of six figures and the prose around
them. Checked mechanically, not by eye.

**2. arXiv:2006.13771 (`weil-compo.tex`, 2496 lines), the archimedean positivity paper.**
Sharpness of Theorem 1 is **never asserted**, and two nearby statements are easy to
mistake for it:

- `:853`, Remark `improve` (ii) — **a genuine theorem, about a different object**: *"The
  functional $D\circ Q$ is not negative on $[2^{-1},2]$"*, proved by constructing a
  positive-definite $f$ supported in $[-\log2,\log2]$ with $D_+(Q_+f)>0$, limit
  $\sim+2.98699$. This is about the *remainder* $D$, i.e. about why the paper needs §4's
  dihedral decomposition at all. It says nothing about $W_\infty$.
- `:1427` — the largest eigenvalue of $\mathcal K_I$ *"is less than $1$ … this no longer
  holds true when the interval length gets closer to $\log 2$"*. That is the **method**
  degrading at the endpoint, not positivity failing past it. It is why the rank-one repair
  of §1.3 exists.

And the paper's own reason for the interval cuts the other way. `:114`: *"In this paper we
consider the simplest instance of this strategy, namely when the support of the test
function is contained in the interval $(1/2,2)$ **so that rational primes are not
involved**."* The interval is chosen for **convenience** — it is the largest one on which
the problem is purely archimedean — and is nowhere claimed to be the boundary of validity.
So the paper neither asserts sharpness nor rests on it.

**3. arXiv:2310.18423 (`mainc2m24fine.tex`), CCM.** Does not mention the sensitivity
figures, the failure, or arXiv:2106.01715's numerics at all. Grepped for *sensitiv*,
*fails to*, *ceases*, *beyond the value*, *log 2* — nothing relevant.

**4. arXiv:2602.04022 (`rhready.tex`), Connes' 2026 survey.** Restates Theorem 1 with the
same hypotheses twice (`:1198-1200`, and again in prose at `:1298`) and **never mentions
that the archimedean form goes negative past that range**, in the *Remaining steps*
subsection or anywhere else. If sharpness were known as a theorem, the survey is where it
would appear.

**What this negative does not cover.** The positivity at $\mu=2$ predates
arXiv:2006.13771: *"This result was proved in [Yoshida] by reducing it to an explicit
computation"* (`weil-compo.tex:118`), and Connes–Consani add *"In [Yoshida], the positivity
was shown to hold for $\lambda=\sqrt2$ **using numerical analysis**"* (`:177`). **H. Yoshida,
*On Hermitian forms attached to zeta functions*, Adv. Stud. Pure Math. 21 (1992) 281–325,
I did not read** — it is not on arXiv and I could not reach it. It is the one place a
sharpness statement could be hiding, and it is the obvious next check for anyone who wants
to tighten this. Beyond that: arXiv sources only, four papers, read as LaTeX.

### 10.2 Their computation, rebuilt — possibility (3) is excluded

Connes–Consani give the semilocal form as $\psi^\#=W_{0,2}^\#-W_{\mathbb R}^\#-\sum_pW_p^\#$
(`Spectraltriples.tex:414`), in their own orthonormal basis (`:385`), with the archimedean
integral carried out at `:532`. That is enough to rebuild the even matrix $\sigma^+$ from
scratch, which the script does — sign conventions taken from the explicit formula rather
than inherited from §3.3, so this is also the strongest available form of §6's house-rule
check.

| Connes–Consani | source | ours |
|---|---|---|
| smallest eigenvalue at $L=\log2$, $\sim0.00133$ | `:551`, Fig. `testeven` | $0.0013303$ at $N=80$, $0.0013296$ at $N=160$ |
| archimedean-alone crossing at $\mu=2.27$ | `:568`, Fig. `testeven2` | $\mu^*=2.271017$ at $N=160$, still decreasing in $N$ |
| $\infty+2$ at $\mu=3$, $<6\times10^{-8}$ | `:568` | $5.55\times10^{-8}$ |
| admissible $p$-window at $\mu=3$, width $<10^{-3}$ | `:574`, Fig. `testeven3` | $[1.9999995,\,2.00043]$, width $4.4\times10^{-4}$ |
| prime $3$ repairs past $\mu=3$ | `:579`, Fig. `testeven4` | $\mu=3.5$: $\infty{+}2=-1.19\times10^{-2}$, $\infty{+}2{+}3=+2.48\times10^{-10}$ |

The second row is the one that carries weight, because **$2.27$ was not a number I aimed
at** — I computed the crossing and then found it written in their prose. Their
window for the crossing, $L\in[0.493,0.893]$ (`:177`), contains $L^*=0.82023$, in its
"upper part" as they say.

**Why (3) is excluded, and it is not just "the numbers agree".**

- **Truncation cannot manufacture the failure.** Restricting a quadratic form to a subspace
  can only *raise* its smallest eigenvalue. So a negative truncated eigenvalue certifies a
  negative one for the full form; truncation can hide a failure of positivity, never invent
  one. The computed values behave accordingly — monotone decreasing in $N$
  ($0.0013847\to0.0013296$ for $N=10\to160$ at $L=\log2$), and $\mu^*$ likewise decreasing.
- **Double precision is not load-bearing for the sign change.** The matrix entries are
  $O(1)$, the spectrum at $N=160$ runs $[1.3\times10^{-3},\,5.5]$, and every number is
  quadrature-converged to ten digits. This is four orders of magnitude away from the regime
  `citation-audit.md` §6 records (CCM at 200 digits, eigenvalues $\sim10^{-48}$ at
  $\mu=11$).
- **The rows that *are* in that regime are flagged as such.** The repaired eigenvalues of
  rows 3–5 run $10^{-8}$ down to $10^{-12}$, leaving two to four digits of margin. The
  script says so and reports them as **reproductions, not verifications**: past $\mu\approx4$
  they want extended precision. Nothing in §3.3 or here leans on them — the load-bearing
  claim is the *negative* values, which are $O(10^{-2})$ to $O(10^{-5})$.

### 10.3 A witness, and why failure had to come eventually — *ours*

Two things the reproduction does not by itself give: a statement independent of any matrix,
and a reason.

**The witness.** Take $f(x)=\cos(\pi x/L)+\kappa\cos(3\pi x/L)$ on $[-L/2,L/2]$ (additive
coordinate $x=\log u$), continuous on $\mathbb R$ since both modes vanish at the endpoints,
with $\kappa$ fixed by $\int f(x)\cosh(x/2)\,dx=0$. For real even $f$ that integral is
$\widehat f(\pm i/2)$, so the boundary term of Prop. `Hilbert` vanishes exactly and the
archimedean value is $-W_{\mathbb R}$ alone. Evaluating it is three one-dimensional
quadratures. It **crosses zero at $\mu=3.5581$ and is negative at every larger $\mu$
tested** ($4.06$, $4.48$, $7.39$); at $\mu=4.0552$ it is $-0.646$ against
$\|f\|^2=6.48$. A weaker threshold than the true $2.271$ — it is one fixed vector, not the
bottom eigenvector — but no truncation and no eigenvalue is involved, and one can write the
function down in a line.

**The reason.** Connes–Consani's own Prop. `Hilbert` (`:289`) puts the archimedean part on
the Fourier side as
$$\int|\widehat f(t)|^2\frac{2\theta'(t)}{2\pi}\,dt+2\Re\big(\widehat f(\tfrac i2)\overline{\widehat f(-\tfrac i2)}\big),$$
$\theta$ the Riemann–Siegel theta function. **$\theta'$ is negative on $|t|<6.2898$**
($\theta'(0)=-2.68609$; first zero $6.2898360$, computed in the script). So the Weil density
is negative in a neighbourhood of $t=0$, and the only thing stopping a test function from
living there is the uncertainty principle: a short support forces $\widehat f$ to spread
past the crossing, where $\theta'>0$. Lengthening the support removes that obstruction.

That is a **mechanism, not a proof** — it says failure at large $L$ is structurally
expected and says nothing about where. But it settles the shape of the answer: the
archimedean form is *not* a positive form that happens to be verified on a small interval;
it is an indefinite form whose positivity on a small interval is an uncertainty-principle
effect. Turning this into a theorem — an explicit family of test functions with an explicit
threshold — looks routine and is not attempted here.

**House rule.** Both halves are sign-sensitive: $\theta'<0$ near $t=0$ (not $>0$) is what
makes the density hostile, and the witness's value is $-0.646$ (not $+0.646$). Under
$W\mapsto-W$ both statements become false.

### 10.4 The sites, and what changed at each

The strong form — *"place-by-place positivity is **false**"*, *"changes sign **just past**
$\mu=2$"* — appears in five places. Three are in this repository and are fixed on this
branch; two are not and are listed for whoever owns them.

| site | was | now |
|---|---|---|
| `semilocal-gap.md` §3.3 heading | "is false" | "fails — observed and reproduced, not proved", with a status block and per-bullet reproduced values |
| `semilocal-gap.md` bottom line, item 4 | "is false"; "just past $L=\log2$" | "fails … **numerical**, and now independently reproduced"; crossing at $\mu\approx2.2710$ |
| `semilocal-gap.md` §3.3 item 1 | "just past that value"; "the statement to be extended is false" | margin of $0.271$ in $\mu$ stated; "fails at $\mu=2.271$" |
| **vision document `:61-62`** (CEILING DROPS, mg-03f0) | "changes sign just past $\mu=2$, repaired only by the prime 2 and only to within $10^{-3}$" | **not ours to edit — flagged.** Two repairs wanted: the crossing is $\mu=2.271$; and *"repaired … only to within $10^{-3}$"* misreads the source. $10^{-3}$ is the width of the admissible window in the **parameter $p$** at $\mu=3$ (`:574`) — a sharpness in $p$, not a residue left by the repair |
| **vision document `:378-381`** (Amendment 3 §3) | "Place-by-place positivity is FALSE"; same $10^{-3}$ phrasing | **not ours to edit — flagged.** Same two repairs. The finding itself stands and is stronger than when written: it now has an independent reproduction behind it |

**What does *not* change.** The structural conclusion — that the semilocal theorem must be
about cancellation *between* places rather than assembly of per-place positives — is
untouched, and §3.3's item 2 is the sentence that carries it. It rests on two facts:
that no $-\Lambda(n)V(n)$ is of one sign (§3.2, which is **proved**, ours, and elementary),
and that $Q_\infty$ is not positive beyond $\mu=2.271$ (numerical, now doubly so). The
demotion is of one word in the second, and the ceiling drop mg-03f0 recorded stands.

**Watching the exculpatory reading**, as the ticket asks. The tempting conclusion here is
"the strong wording was a fair reading of the sources, so nothing went wrong". It is not
quite. The sources say *"we report from the numerical computations"* in the very sentence
that opens the subsection §3.3 cites; the word **numerical** is in §3.3's own header line,
and the note's §0 vocabulary table defines it and warns that in this corpus it is *"not
automatically trustworthy either"*. The strong wording was available to be caught at
writing time from material already on the page. What was genuinely unavailable was the
reproduction — and that turned out to be a small job, not a hard one — §7 said the opposite
and was wrong about it.

### 10.5 Secondary — `citation-audit.md` §7 item U7

The ticket allows this only if the same read answers it. It does, for the negative half.

**U7 asks** whether Connes–Consani anywhere size the residual $\widehat\varphi(0)$ — the
Fourier-side endpoint condition their prolate combinations satisfy only approximately.
**Answer: no, and the source says so in its own words.** Their construction is at
`Spectraltriples.tex:744`:
$\phi_{2n}:=\psi_{2n}\psi_0(0)-\psi_0\psi_{2n}(0)$ — imposing $\phi_{2n}(0)=0$ *exactly*.
The other condition is handled at `:746`: *"For $1<n\le\nu(\mu)$ one may **approximate**
$\mathcal F(\phi_n)$ by $(-1)^n\phi_n$ and, using the Poisson formula, **act as if**
$\mathcal E(\phi_n)$ would fulfill the equality …"*. No error term is given there or
anywhere the construction is used. The only quantitative material about the deviation is
Figure `chimum` (caption at `:739`) — *graphs* of $\chi(\mu,m)$ — and the prose *"one only
retains the values of $m$ for which the characteristic value $\chi(\mu,m)$ … is almost
equal to $1$"*, *"$\chi(\mu,m)\sim1$ for $m\le\nu(\mu)$"* (`:729`–`:733`).

Two places that look like they should contain it and do not, checked because their titles
promise it:

- the appendix **"Size of $\mathcal F_\mu\circ w$(Prolate)"** (`:1547`) is about the
  $\lambda\to\infty$ **Hermite** limit, where $\mathcal F(h_{2m})=(-1)^mh_{2m}$ holds
  exactly and so the analogous families $\psi^{\rm ev}_\ell$ satisfy *both* conditions
  exactly (`:1563`). There is no residual there to size;
- Connes' 2026 survey does give a quantitative statement in this area — $\widehat k_\lambda
  \to\widehat k$ controlled by $c\lambda^{-1/2-\alpha}(1-2\alpha)^{-1}$ on
  $\Im z=\alpha$ (`rhready.tex:1172`) — but that bounds the convergence of $k_\lambda$ to
  $\mathcal E(h)$, a different quantity. Not the residual.

**So U7 closes as a negative**, and `citation-audit.md` §4.4 item 1 keeps standing on it —
but on a *sourced* negative now ("they say they act as if") rather than on "~40 pages
skimmed".

**One thing falls out, and it is *ours* and deliberately not pushed further.** The residual
is not merely unsized in the literature; it is available in closed form from the identity
Connes–Consani display a few lines earlier (`:727`, the classical prolate relation, in
their $\lambda$-normalisation
$\int_{-\lambda}^{\lambda}\psi_{m,\lambda}(\xi)e^{2\pi i\xi y}d\xi=(-1)^m\chi(\mu,m)\psi_{m,\lambda}(y)$,
where the right-hand $\psi_{m,\lambda}$ is the un-truncated prolate function).
Applying it to $\phi_{2n}$ termwise gives
$$\widehat{\phi_{2n}}(0)=\big[\chi(\mu,2n)-\chi(\mu,0)\big]\,\psi_0(0)\,\psi_{2n}(0),$$
so the residual is governed by a **difference of characteristic values** — exactly the
quantities their Figure `chimum` plots. That is one line of algebra from their own display
and it is why nobody needed to state it separately; it is *not* a claim that the sizing is
in the paper. Whether it delivers the corpus's $\asymp1-\chi_4$ (`start.tex:177-186`,
`citation-audit.md` §4.4 item 1) needs `index-convention.md` applied to the two indices and
a numerical check of $\psi_0(0)\psi_{2n}(0)$ against $1-\chi$, **neither of which this note
does**. Recorded as a lead, not a result.

---

## 11. Appendix — S1 answered (added 2026-08-12, mg-0bd7)

*Appended. Nothing above is deleted; the S1 row in §8 is annotated in place. §3.1's
"the spectrum of $P^S\widehat P^SP^S$ is **not known**" and §2's I8 row are left
untouched and remain correct: both are statements about the **semilocal** operator,
and §11.2–§11.4 below leave them standing. What changes is that the **single
finite place** is no longer an open question — it is settled, and the answer is that
the object is degenerate there.*

**Answer: partially yes.** At one non-archimedean place the pair
$(P_\Lambda,\widehat P_\Lambda)$ has a complete, explicit, published spectral
description — and its content is that the angle operator is **trivial**. Semilocally
there is still nothing, and §11.2 identifies the exact definitional reason the
one-place result does not transfer. This is a more useful answer than the clean
negative §8 expected, because the two halves point in opposite directions.

### 11.1 One finite place: completely described, and degenerate — Burnol 1999

J.-F. Burnol, *Scattering on the p-adic field and a trace formula*,
arXiv:math/9901051 (12 Jan 1999, rev. 31 Jan 1999), **IMRN 2000 no. 2, 57–70**.
Source file `scatteringV2.tex`, read as primary source (320 lines). **Proved.**

Burnol's last section is titled *Exact evaluation of a trace considered by Connes*
and takes **Connes' own operator**, not an analogue (`:246-250`):

> Connes considers the operator $\widetilde{P_\Lambda}P_\Lambda U(f)$ where
> $P_\Lambda$ is orthogonal projection to functions with support in
> $|x|\leq\Lambda$, $\widetilde{P_\Lambda}$ is its Fourier conjugate […] He shows
> (also at an archimedean place) that it is of trace class, has a main logarithmic
> divergency and a constant term which is the local term of the Explicit Formula and
> a $o(1)$ error term. **In the non-archimedean case his proof actually gives the
> exact value for $\Lambda$ large enough.**

The reference is to Connes 1999, Theorem 3 of Section V — i.e. the semilocal trace
formula this note's I5 row rests on. Burnol sets $\Lambda=q^n$, $Q_n:=\widetilde{P_n}P_n$,
and decomposes by the characters $\chi$ of the unit group. **Theorem XI** (`:255-260`)
gives the kernel of $Q_n^\chi$ in closed form in every case. What matters here is not
the kernel but what the *proof* (`:262-268`) says about the two projections
separately:

- **Ramified $\chi$** (`:262`): *"The action of $P_n$ is orthogonal projection to the
  span of $\{z^j, j\leq n\}$ while the action of $\widetilde{P_n}$ is by Theorem I
  orthogonal projection to the span of $\{z^j, j\geq e(\chi) + \delta -n\}$."* Two
  projections onto coordinate subspaces of **the same orthonormal basis**.
- **Trivial $\chi$, $2n\geq\delta$** (`:264`), with $\omega_j$ the normalised
  indicator of the ball of radius $q^j$ and $L^2_1={\cal L}_n\oplus{\cal K}_n\oplus{\cal M}_n$:
  *"$P_n$ cuts off ${\cal M}_n$, $\widetilde{P_n}$ cuts off ${\cal L}_n$, **so they
  commute** and their combination $Q_n$ is just orthogonal projection to
  ${\cal K}_n$."* The word is Burnol's, not mine.
- **Trivial $\chi$, $0\leq2n<\delta$** (`:266`): here they do *not* commute; $Q_n$ is
  the rank-one operator $\phi\mapsto q^{-(\delta-2n)/2}\langle\omega_n|\phi\rangle\,\omega_m$,
  $m=\delta-n$. $\delta$ is the different exponent, so **this case is empty over
  $\mathbb Q_p$**, where $\delta=0$.

> **Reading (ours, and marked as such because Burnol does not phrase it this way).**
> Over $\mathbb Q_p$ — $\delta=0$, so $2n\ge\delta$ always — the two cutoff
> projections commute at every $\Lambda=p^n$. A commuting pair has
> $P\widehat PP=P\widehat P$, a projection; its spectrum is contained in $\{0,1\}$;
> Connes' angle $\Theta$ (defined at math/9811068 `:2735-2739` by
> $\mathrm{Sin}(\Theta)=|P_1-P_2|$) takes only the values $0$ and $\pi/2$. There are
> **no non-trivial angles, no plunge region, and hence no prolate family to find**.
> The finite-dimensional space ${\cal K}_n$ is the whole story, and Burnol gives its
> dimension (Theorem V, `:164`).

So the single-finite-place question is not open, and has not been since 1999. It is
answered **completely** — and the answer is that the object degenerates.

**Independent corroboration from a different literature, abstract-level only.**
K. Abhinav, Q. Jahan, *Gabor Orthonormal Bases with Maximal Localization and Gabor
Frame Operator on Local Fields*, arXiv:2606.31355 (30 Jun 2026), abstract: *"an
explicit construction of a Gabor orthonormal bases for a local field $K$ that provides
maximal localization in both time and frequency. **Such a localization is not true in
case of $\mathbb R$ due to the uncertainty principle.**"* Same phenomenon, reached
from signal processing rather than from Tate's thesis. I read the abstract only.

### 11.2 Why the one-place result does not transfer — the cutoff is by the *product* module

This is the load-bearing distinction and it is definitional, so it is checkable
without doing any mathematics. From Connes' 2026 survey, the endnote attached to the
semilocal trace formula (`rhready.tex:1236-1240`), which is where $P^S_T$ and
$\widehat P^S_W$ are defined:

> the projections $P_T^S$ and $\widehat P_W^S$ are defined as in the archimedean case
> **using the module** […] ${\rm Mod}_S(u):=|(u_v)_{v\in S}|_S=\prod|u|_v\in\mathbb R_+$

$P^S_T$ cuts off the set $\{x\in\mathbb A_S : \prod_{v\in S}|x_v|_v\le T\}$. That is a
single condition on a **product** of local absolute values, not a condition at each
place, so $P^S_T\neq\bigotimes_{v\in S}P_{T_v}$ and Burnol's place-by-place
computation says nothing about it. CCM use the same module and are explicit that the
region is not a product — `mainc2m24fine.tex:766-767` states only an **inclusion**,
$\eta_S(P_\lambda)\subset P^S_\lambda$, and its proof (`:778-781`) gets there by the
one-way implication $\lambda<|x|=|y||u|\le|u|\Rightarrow|u|>\lambda$.

**Consequence, stated flatly:** the one-place triviality of §11.1 is evidence that
whatever difficulty the semilocal angle operator has is located **entirely in the
coupling between places through the product module**, not in any individual place.
Each finite place on its own contributes a commuting pair and one line of Sonin space
(§2's local fact, CCM Prop. `soninppp`).

### 11.3 Connes 1999 substitutes a construction for a spectrum at exactly this step

A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann
zeta function*, arXiv:math/9811068, Selecta Math. **5** (1999) 29–106. Source file
`zeta.tex` (5468 lines), read as primary source.

Connes states the archimedean spectrum in full — Slepian–Pollak's plunge description,
`:2809-2815`: the eigenvalues $\lambda_n$ of $P_\Lambda\widehat P_\Lambda P_\Lambda$
*"are decreasing very slowly from $\lambda_0\sim1$ until the value $n\sim4\Lambda^2$
of the index $n$, they then decrease from $\sim1$ to $\sim0$ in an interval of length
$\sim\log(\Lambda)$ and then stay close to $0$"* — and uses it to define the subspace
$B_\Lambda$. Immediately afterwards (`:2823-2830`):

> We now know what is the subspace $B_\Lambda$ for the single place $\infty$, and to
> obtain it **for an arbitrary set of places (containing the infinite one), we just
> use the same rule as in the case of function fields**, i.e. we consider the map
> $\psi\mapsto\psi\otimes1_R$, which suffices when we deal with the Riemann zeta
> function.

That sentence is the whole of the semilocal prescription in the 1999 paper, and it is
a **construction, not a spectrum**: at the archimedean place $B_\Lambda$ is the span
of the prolate functions $\psi_n$, $n\le4\Lambda^2$, cut off where the eigenvalues
plunge; semilocally it is the image of that span under tensoring with $1_R$. Nothing
is computed about the eigenvalues of the semilocal pair, then or since. The map
$\psi\mapsto\psi\otimes1_R$ is CCM's $\eta_S$, and it is exactly the map §2 records as
*"hilbertian", not unitary*. **This is the sharpest available statement of the gap,
and it is in Connes' own text.**

For completeness: the only other spectral remark in `zeta.tex` about this operator is
`:2951-2977`, where Connes notes that the eigenvalues of $\Theta$ *"also play a key
role in the theory of random unitary matrices"* via Mehta's expansion of $E(n,s)$ in
the eigenvalues of $\widehat{P_\pi}P_t$. Archimedean, and a remark rather than a
result used.

### 11.4 CCM 2024: an explicit semilocal spectral measure — for a different operator

The nearest thing to a semilocal spectral description in the literature is real, and
it is worth stating precisely how far it falls short, because "CCM have nothing
semilocal" would be wrong. From `mainc2m24fine.tex` (arXiv:2310.18423 v2, 4 May 2024;
Ann. Funct. Anal. **15** (2024) no. 4, Paper 87), read as primary source:

| what | where | status |
|---|---|---|
| An explicit semilocal spectral measure $dm_S(s):=\big\vert\prod_{v\in S}L_v(\tfrac12-is)\big\vert^2\,ds$, and a unitary ${\cal V}_S:L^2(X_S)^{K_S}\to L^2(\mathbb R,dm_S)$ putting the cyclic pair $(\mathfrak{Scal},\xi_S)$ in canonical form | `:787-790` (eq. `ms`), `:791-805` (Prop. `httransfoS`) | **proved** |
| The pair is even; the grading is the semilocal Fourier transform ${\cal F}_S$ | `:793` | **proved** |
| A semilocal Hermite operator $N_S$, eigenfunctions $\eta_S(P^S_n(x)e^{-\pi x^2})$, and $\mathfrak{Scal}$ a hermitian Jacobi matrix in that basis | `:828-840` (Thm. `hermsemiloc`) | **proved** |
| The candidate $\mathbf W_{\lambda,S}=(H+\tfrac12)^2+\lambda^2N_S$ | `:843` | **definition** |
| The Jacobi coefficients for general $S$ | `:259` | **deferred**: *"The computation of the coefficients of the hermitian Jacobi matrix of the cyclic pair for a general $S$ as above is deferred to a forthcoming paper."* |

So there *is* an explicit spectral object semilocally, and its ingredients are the
local $L$-factors on the critical line. **But it diagonalises the scaling operator
$\mathfrak{Scal}$ with cyclic vector $\xi_S$, not $P^S\widehat P^SP^S.$** The link
that would make it a spectral description of the angle operator is precisely the one
that is missing:

- **No commutation is claimed anywhere in the paper.** I grepped `commut` over all
  1474 lines of `mainc2m24fine.tex`. Every hit is about the grading $\gamma$
  anticommuting with $D$, the spectral-triple commutators $[D,f]$, or the two
  commutative diagrams. **There is no statement that $\mathbf W_{\lambda,S}$ commutes
  with $P^S_\lambda$ or $\widehat P^S_\lambda$** — which is what I8 needs and what
  §3.1 says is absent.
- CCM themselves call the Sonin-space match a **constraint on the search**, not a
  theorem (`:266`): the archimedean coincidence of the Sonin space with the negative
  part of the prolate spectrum *"gives another constraint in the search of the
  semilocal analogue of the prolate operator."*
- Remark `care` (`:845-861`) records the two ways the transport fails:
  $N_S\circ\eta_S\neq\eta_S\circ N_\infty$ unless $S=\{\infty\}$, and
  $|\bullet|_S^2\,\eta_S(f)\neq\eta_S(|\bullet|^2f)$, worked out for $S=\{p,\infty\}$.

This is the same shape as §4's finding one level down: an **announced** strategy with
a proved framework under it and the computable content deferred.

### 11.5 Where I looked and found nothing — so this can be told from an unexamined negative

The standard is §9.3's. Searches quoted; counts are what the interfaces returned on
2026-08-12.

**1. arXiv full-text metadata, the two obvious names.** `all:"prolate" AND
all:"p-adic"` → **0 results**. `all:"Slepian" AND all:"p-adic"` → **0 results**.
`all:"prolate" AND (all:"adele" OR all:"adelic")` → **2 results**, both the same
group and both false friends (next item). `all:"Sonin space"` → 6 results: CCM
arXiv:2112.05500 and arXiv:2310.18423, two Burnol papers, Connes–Consani
arXiv:2008.10974, and Blower arXiv:math/0605010 (unitary-ensemble spectral edges) —
nothing new.

**2. False friends, named because they are what a repeat of this search will hit
first.**

- **"Adelic Grassmannian" is not adelic.** Casper–Grünbaum–Yakimov–Zurrián,
  *Reflective prolate-spheroidal operators and the adelic Grassmannian*
  (arXiv:2003.11616), and its companion arXiv:1909.01448, are about **Wilson's
  adelic Grassmannian** of the KP hierarchy. The word has no relation to the adeles
  of a number field. This is genuinely the deepest modern work on *why* commuting
  differential operators exist for time-band limiting (bispectrality / Darboux), and
  it is the right place to look for a mechanism — but it is not a p-adic or adelic
  result and gives nothing about $P^S\widehat P^SP^S$. Abstract-level.
- **"p-adic uncertainty principle" mostly means the wrong Hilbert space.**
  arXiv:2506.18913 (*p-adic Ghobber-Jaming Uncertainty Principle*) and
  arXiv:2210.10941 (*Spectral theory of p-adic Hermite operator*) work in Hilbert
  spaces **over** a p-adic ground field, not in $L^2(\mathbb Q_p,\mathbb C)$, which is
  the space this note's operator acts on. Abstract-level; not pursued further.
- **"Local field" collides with neurophysiology.** `abs:"local field" AND
  abs:"time-frequency"` returns local field *potentials* — six of six hits. Any search
  in this area must pin the number-theoretic sense.

**3. Citation-forward from Burnol's paper.** Semantic Scholar lists **13** citations
of arXiv:math/9901051. **Eight are Burnol's own** later papers. The rest are Volovich
(2019, integrable systems), Khrennikov (2018, ultrametric pseudodifferential
equations), Chacón-Cortés (2015, p-adic Laplacians), Biane (2009, OPUC and discrete
Painlevé) — p-adic mathematical physics and orthogonal polynomials. **None extends
the computation to several places, and none mentions the semilocal setting.**

**4. Neither CCM nor Connes cites the paper that answers the one-place case.** I
checked both bibliographies directly. `mainc2m24fine.tex` cites Burnol at `:1413`,
`:1415`, `:1417` and `rhready.tex` at `:1380-1393`; in both cases the entries are the
**same three** archimedean/de Branges papers — the two C. R. Acad. Sci. notes on
Sonine spaces (2001, 2002) and the J. Théor. Nombres Bordeaux paper (2004). The
p-adic scattering paper does not appear in either. That is not a criticism — the
Sonine papers are what they need — but it means the one-place computation is
**outside the corpus's citation graph**, and it is why §8's original absence-finding
missed it.

**5. Citation-forward from CCM's semilocal paper, for the deferred coefficients.**
Semantic Scholar lists **9** citations of arXiv:2310.18423: Connes' own survey and
*Zeta Spectral Triples*, Connes–van Suijlekom, Suzuki (2023, *On the Hilbert space
derived from the Weil distribution*), Meynig (2025, spheroidal eigenvalue asymptotics),
Groskin (2026), Glazunov (2026, ×2). **None computes the semilocal Jacobi
coefficients.** Consistent with §9.3's finding that the forthcoming paper has not
appeared.

**What this negative does not cover.** arXiv and Semantic Scholar. Semantic Scholar's
citation lists are not exhaustive and under-report non-arXiv venues, so a
journal-only paper could be missed; the two personal pages §9.3 could not reach
(`math.jhu.edu/~kc`, `alainconnes.org`) were not retried. I read Burnol's other
1998–2003 local-field papers (arXiv:math/9811040 *Spectral Analysis of the local
Conductor Operator*, arXiv:math/9812012 *…local Commutator Operators*,
arXiv:math/0001013 *An adelic causality problem related to abelian L-functions*, J.
Number Theory **87** (2001) 253–269) **at abstract level only**. They are the nearest
adjacent objects — the conductor operator $H=\log|q|+\log|p|$ and its commutators,
whose spectral functions Burnol identifies with the logarithmic derivative of the
Tate–Gel'fand–Graev Gamma function on the critical line — but they are an *additive*
combination of the two localisations, not the *compression* $P\widehat PP$, and I did
not read their bodies. `math/0001013` is adelic and Lax–Phillips and is the single
most likely place for a semilocal statement to be hiding; **it is the obvious next
check for anyone who wants to tighten this.**

### 11.6 Consequence for the direction question

Recorded, not argued — the (a)/(b)/(c) call is Daniel's (vision document, amendment
5). The two facts that bear on it:

- **(a) is not work on an untouched object at one finite place.** That case is closed
  and degenerate, and has been since Burnol 1999. Anyone starting there would
  rediscover a commuting pair.
- **(a) *is* work on an untouched object semilocally**, and §11.2 says why the two
  are not the same question: the semilocal cutoff is a single condition on the product
  module. So the named gap — cancellation between places — and the missing spectral
  description are **the same difficulty seen twice**, which is a point in (a)'s
  favour, not against it.

Per the ticket, no mathematics was attempted; §11.1's one derived sentence is marked
as a reading and does nothing but restate Burnol's own word "commute".
