# The semilocal gap — what the archimedean proof supplies, and what a finite place lacks

Work item mg-03f0. Companion script:
[`verify_semilocal_gap.py`](verify_semilocal_gap.py) (needs `numpy`).
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

**4. Place-by-place positivity is false, so "transport the proof to $p$" is not
the right shape of statement.** Connes–Consani report that the archimedean
contribution *alone* changes sign just past $L=\log 2$, and that positivity is
restored only by adding the prime $2$ — and that perturbing $2$ to $1.9999$ or
$2.0005$ destroys it (arXiv:2106.01715, `Spectraltriples.tex:542-575`, numerical). The required
theorem is about a **cancellation between places**, not about each place. That is
a different and harder object than the one that was proved. §3.3.

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

### 3.3 Place-by-place positivity is false

Connes–Consani, arXiv:2106.01715, the subsections *Sensitivity of Weil positivity,
archimedean place*, *… to the precise value $p=2$* and *Change of sign of smallest
eigenvalue* (`Spectraltriples.tex:542`–`:600`; **numerical**, their computation,
summarised in their own text at `:177` and `:210`):

- the archimedean contribution $-W_{\mathbb R}$ alone is positive up to $L=\log2$ — the
  smallest eigenvalue of the even matrix at $L=\log2$ is $\sim0.00133$ (`:551`) —
  and **changes sign just beyond it** (`:557`, Figure `testeven1`);
- positivity is restored on $\log2\le L<\log3$ by adding the prime $2$; at
  $\mu=3$ the smallest eigenvalue is $<6\times10^{-8}$ (`:568`);
- replacing $2$ by a real parameter $p$, positivity at $\mu=3$ fails for
  $p=1.9999$ and for $p=2.0005$ — an interval of size $<10^{-3}$ (`:574`);
- the pattern repeats at $3$, $4=2^2$, $5$, $7$ (`:576`–`:600`).

Two things follow, and they matter more than their status as numerics suggests,
because the theorem they bracket is only claimed at $\mu=2$.

1. **The archimedean theorem is at the edge of its range.** Theorem 1 of
   arXiv:2006.13771 is stated for support in $[2^{-1/2},2^{1/2}]$, i.e. exactly
   $\mu=2$, $L=\log2$; Connes' 2026 survey still states it that way
   (`rhready.tex:1200`). Just past that value the object it controls is
   reported to go negative. There is no "extend the archimedean theorem to
   larger $\lambda$ first" — the statement to be extended is false.
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
- §3.3: "the archimedean contribution ceases to be **positive** past $\mu=2$ and
  positivity is **restored** by the prime 2" — under a global sign flip this
  becomes a statement about negativity being restored, which is a different
  (and false) claim about the same figures.

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

**Not done, and it would be the natural next check:** I did not reproduce
Connes–Consani's sensitivity figures (`Spectraltriples.tex:548`–`:572`, labels
`testeven`, `testeven1`, `testeven2`, `testeven3`) — the archimedean sign change
past $L=\log2$ and its repair by the prime $2$. §3.3 rests on their statement of their own numerics. It
is the single most consequential **numerical** claim this note leans on, and
unlike the rest of the note it is not checkable in one minute from a paper. It is
also, per `citation-audit.md` §6, in the regime where the corpus's own arithmetic
is unsound, so reproducing it is not a small job.

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
| S1 | Does the semilocal angle operator $P^S\widehat P^SP^S$ have *any* known spectral description, even partial? | I read CCM's semilocal-case section and the survey's *Geometric Perspectives*; neither gives one. Absence over what I read, not proof of absence |
| S2 | Is the archimedean positivity theorem *known* to be sharp at $\mu=2$, or only numerically observed to fail past it? | §3.3 rests on Connes–Consani's figures `testeven1`/`testeven2`. I found no theorem asserting failure |
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
