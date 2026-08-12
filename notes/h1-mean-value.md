# Where H1 actually lives: it is not a Plancherel–Pólya bound, and the zeros are not the obstruction

Work item mg-8462. Companion script: [`verify_h1.py`](verify_h1.py) (needs `mpmath`;
no `numpy`; imports the prolate apparatus of [`verify_prolate_rate.py`](verify_prolate_rate.py)).
Attacks **H1**, the one named open analytic problem in
[`../paper/positivity-obstruction.tex`](../paper/positivity-obstruction.tex) — Hypothesis
H1 at `:1242`, gap **G6** at `:1527`, and item **P1** of <!-- mg-6467: those line numbers are the pre-mg-6467 draft. Now: (H1) at `:1421`, and G6 in the "closed since the first draft" block at `:2423`. -->
[`prolate-rate.md`](prolate-rate.md) §11.

Nothing in `start.tex`, `s3.tex` or the paper was edited. `prolate-rate.md` is
annotated in place, append-only.

**Calibration, before anything else.** H1 is a statement about the *magnitude*
$|s(\mu)|$. Proving it would turn `prolate-rate.md`'s and the paper's
**conditional** upper bound $\limsup\mu^{-1}\log s(\mu)\le-4\pi$ into an
**unconditional** one. That is a real improvement to a result we already have and
it is **not progress toward RH**. The matching lower bound is not open — it *is*
RH (`rhready.tex:1145`, paper Thm `thm:boundary`, gap **G10**), and nothing below
touches it. §8 applies the house rule and the answer is *sign-blind*, which is
correct here rather than a defect.

---

## Bottom line

**1. The name is wrong, and the name is what has been hiding the difficulty.**
H1 is labelled "of Plancherel–Pólya type" (paper `:1248`, `prolate-rate.md` §6(c)). <!-- mg-6467: that label is gone from the paper. §1 and §2 of this note are now the paper's §7.1, `:1504`, where the phrase survives only as a quotation of the first draft. -->
Plancherel–Pólya requires two hypotheses and **our configuration satisfies
neither**: the function must be entire of exponential type (equivalently, its
Fourier transform compactly supported), and the sampling points must be
uniformly separated. $\mathcal F_\mu r$ is *not* of exponential type — the spill
$r$ is supported on $(0,\lambda^{-1})$, a *half*-line in the logarithmic
variable, so $\mathcal F_\mu r$ is a Hardy-class function of a half-plane, not a
Paley–Wiener function. And the zeros are not separated: their local density
$\frac1{2\pi}\log\frac{T}{2\pi}$ grows without bound. §2.

The first failure is **structural, not technical**: the spill is non-compactly
supported *precisely because it is a spill*. The very fact that creates the
near-radical vector is the fact that destroys the Paley–Wiener hypothesis. No
repair of the argument can restore it.

**2. The zeros are not the obstruction. The zeta side can be discharged
completely, unconditionally.** Using only Riemann–von Mangoldt
($N(T+1)-N(T)\ll\log T$), the classical de la Vallée Poussin zero-free region,
subharmonicity of $|\mathcal F_\mu r|^2$, and Plancherel on horizontal lines, §3
proves
$$\sum_{\frac12+is\in Z}|\mathcal F_\mu r(s)|^2\;\le\;
\frac{C}{c_0^2}\int_{-1/2}^{1/2}\!\!\int_{\mathbb R}
\log^3(3+|t|)\,\big|\mathcal F_\mu r(t+i\sigma)\big|^2\,dt\,d\sigma ,$$
and each horizontal line is a Plancherel identity for the spill alone. **After
this there are no zeros left in the problem.** What remains is a weighted-$L^2$
tail bound for one explicit special function.

**3. What remains is a statement about prolate spheroidal wave functions off the
interval, with no number theory in it.** Write $\Phi$ for the normalised prolate
combination on $[-1,1]$ at $c=2\pi\mu$, extended to the entire function it is,
and
$$G(t):=\sum_{n\ge1}\Phi(nt),\qquad t>1 .$$
§4 shows H1 **and** the paper's gap **G5** both follow from
> **(P)** $\displaystyle\sup_{t>1}\;t\,|G(t)|\;\le\;K(c)\,|\Phi(1)|$, with $K$ subexponential in $c$.

That is a reduction of two gaps to one hypothesis, and the surviving hypothesis
is about a classical special function that has been studied since 1961 and can
be computed to arbitrary precision — neither of which is true of H1 as stated.

**4. Half of (P) is proved here, in three lines, and it is proved in exactly the
regime we are in.** If $\chi_n<c^2$ then the Sturm–Liouville amplitude
$$V(x)\;=\;\frac{\big((x^2-1)\Phi'(x)\big)^2}{(x^2-1)(c^2x^2-\chi_n)}+\Phi(x)^2$$
is non-increasing on $(1,\infty)$ and $V(1^+)=\Phi(1)^2$, whence
$$|\Phi_n(x)|\;\le\;|\Phi_n(1)|\qquad(x\ge1).$$
$\chi_n<c^2$ holds throughout our range — measured, $\chi_n/c^2=0.020$ to $0.64$
(§5). What the lemma does not give is the decay $1/x$, and the decay is what (P)
needs. §5. <!-- mg-6851: the decay is now PROVED — band-edge-connection.md Thm 5.2. -->

**5. The published literature does not close the other half, and the reason is
that its hypothesis is the negation of ours.** Osipov–Rokhlin, arXiv:1208.4816,
is the sharpest source on prolate functions outside $[-1,1]$. Their two relevant
theorems both assume $\chi_n>c^2$ — the regime of index *above* the plunge — and
we are at $\chi_n\ll c^2$. Their third result, an off-band expansion, is an exact
identity rather than an estimate, and its remainder is the out-of-band leakage of
$t\Phi(t)$, **an object of the same exponential size as the term being bounded**.
This is not a citation that can be repaired by a better search: the estimate does
not exist in our regime. §6.

**6. A clean new identity, observed, that calibrates (P) and makes the reduction
quantitative.** With $\int_{-1}^1\Phi_n^2=1$,
$$\Phi_n(1)^2\;=\;c\,(1-\Lambda_n)\left(1-\frac{2n+1}{4c}+O(c^{-2})\right).$$
Verified to high precision at $n=0,2,4$ for $c=5,\dots,320$: the residual
$(1-\text{ratio})\cdot c$ lands on $0.2507,\,1.2542,\,2.2626$ against the
predicted $0.25,\,1.25,\,2.25$ at $c=320$ (§7). This converts the *exact*
$L^2$ identity $\int_{|x|>1}|\Phi_n|^2=(1-\Lambda_n)/\Lambda_n$ (§4) into the
endpoint normalisation (P) is stated against, and it is what fixes $K=O(1)$
rather than $K=O(e^{c})$ — which is the whole question, since only a
subexponential $K$ buys anything.

**7. Which outcome of the ticket is this?** Outcome **(3)** with an explicit
obstruction map, i.e. (3)+(5). H1 is reduced to a *different* problem, and the
new problem is better on four counts: it contains no zeta zeros; it is about a
classical special function with sixty years of literature; it is numerically
checkable to arbitrary precision (H1 is not — it is an infinite sum over zeros of
a function of size $10^{-55}$); and half of it is now proved. **It is not
outcome (1).** H1 is not proved here and this note does not claim it is. The one
step that would finish it is named in §9 as **Q1**. <!-- mg-6851: Q1 is PROVED, and
it was NOT a connection problem at a regular singular point — band-edge-connection.md. -->

---

## 0. The object, and the two conventions that must not collide

$\lambda>1$, $\mu=\lambda^2$, $c=2\pi\mu$. Following `prolate-rate.md` §6: $\phi$
is the normalised near-radical vector supported in $[-\lambda,\lambda]$,
$\mathcal E\phi=g+r$ with $g=\mathcal E\phi|_{[\lambda^{-1},\lambda]}$ and
$r=\mathcal E\phi|_{(0,\lambda^{-1})}$, and
$$\mathcal F_\mu r(s)=\int_0^{\lambda^{-1}}r(u)\,u^{-is}\,d^*u .$$
Substituting $u=e^{-v}$ and writing $R(v):=r(e^{-v})$, supported on
$[\log\lambda,\infty)$,
$$F(s):=\mathcal F_\mu r(s)=\int_{\log\lambda}^{\infty}R(v)\,e^{isv}\,dv,
\qquad \|r\|_{L^2(d^*u)}^2=\int_{\log\lambda}^\infty|R(v)|^2dv. \tag{0.1}$$
A zero $\rho=\beta+i\gamma$ contributes the point $s_\rho=\gamma+i(\beta-\tfrac12)$,
so $\Im s_\rho\in(-\tfrac12,\tfrac12)$, and $\Im s_\rho=0$ for every $\rho$ **iff
RH**. H1 is
$$\sum_{\rho}|F(s_\rho)|^2\;\le\;\Theta(\lambda)\,\|r\|^2,\qquad
\Theta\ \text{subexponential in}\ \mu. \tag{H1}$$

**Prolate conventions.** $\Phi_n$ denotes the individual prolate function
$\mathit{PS}_{n,0}$ on $[-1,1]$ at bandwidth $c=2\pi\mu$, normalised by
$\int_{-1}^1\Phi_n^2=1$ and extended to the entire function it is; $\Phi$ without
a subscript is the three-mode combination of `prolate-rate.md` §2.1 rescaled to
$[-1,1]$, likewise normalised. $\Lambda_n$ is the Slepian concentration
eigenvalue and $\chi_n$ the eigenvalue of the prolate differential operator.
§§5 and 7 are per-mode statements; §5 shows nothing is lost in passing to the
combination. Two collisions to
keep straight, both of which have already cost this project a correction:

| symbol | here | Connes / CC | Osipov–Rokhlin |
|---|---|---|---|
| concentration eigenvalue | $\Lambda_n$ | $\chi_m^2=\Lambda_{2m}$ | $\mu_n$ |
| finite-FT eigenvalue | $\mu_\Phi$ | — | $\lambda_n$ |
| prolate ODE eigenvalue | $\chi_n$ | — | $\chi_n$ |

**Osipov–Rokhlin's $\mu_n$ is our $\Lambda_n$ and their $\lambda_n$ is our
$\mu_\Phi$.** Their $\chi_n$ agrees with ours. §6 quotes them and the hypothesis
$\chi_n>c^2$ is stated in the common symbol, so no conversion is involved in the
one place it matters.

---

## 1. H1 is not a hypothesis about a class of functions; it is a ratio — *ours*

For each $\lambda$ there is exactly one $r$. So for each fixed $\lambda$, (H1) is
true with $\Theta(\lambda):=\sum_\rho|F(s_\rho)|^2/\|r\|^2$, whatever that number
is — provided only that the sum converges, which it does (§3). **The entire
content of H1 is the growth of that ratio in $\lambda$, and nothing else.**

Two consequences, and the second is the one that matters.

- H1 **cannot be "reduced to a known theorem"** in the abstract. There is no
  class of functions to which a theorem could be applied; a theorem has to be
  applied to *this* $r$, and then what is used is whatever structure $r$ has.
- The normalisation by $\|r\|^2$ is a **red herring**, and worse than that:
  it is unattainable. Point evaluation of a Hardy-class function at a boundary
  point is an unbounded functional (§2), so no argument can bound
  $\sum_\rho|F(s_\rho)|^2$ by $\|r\|^2$ *alone*. Any proof must use decay or
  smoothness of $r$ that $\|r\|$ does not see. `prolate-rate.md` §6(c) says this
  in one clause — "no uniform $\Theta$ exists on $L^2$; (H1) must use the
  specific $r$" — and it is right; the point here is that this observation
  removes the shape of the statement, not just its generality.

The productive move is therefore to drop $\|r\|^2$ and bound the left side
directly against the quantity the corollary actually needs. §4 does that, and it
absorbs gap **G5** for free.

---

## 2. Why no Plancherel–Pólya theorem applies — *ours*

**The theorem.** (Plancherel–Pólya, 1937; classical, *proved*.) If $f$ is entire
of exponential type $\tau$ with $f|_{\mathbb R}\in L^p$, and $\{t_k\}\subset\mathbb R$
is $\delta$-separated, then $\sum_k|f(t_k)|^p\le C(\tau,\delta,p)\|f\|^p_{L^p(\mathbb R)}$.
The relatively-separated version replaces $\delta$-separation by
$\sup_x\#\{k:t_k\in[x,x+1]\}=N<\infty$ and the constant by $CN$.

**Hypothesis (i) fails, structurally.** $\widecheck F=R$ is supported on
$[\log\lambda,\infty)$ — a half-line, not a compact set — so $F$ is not entire of
exponential type. It is holomorphic on a *half-plane*: by (0.1), $F$ is
holomorphic on $\{\Im s>0\}$ for any $R\in L^2$, and, once $R$ decays like
$e^{-v/2}$, on $\{\Im s>-\tfrac12\}$. Modulo the unimodular factor
$e^{is\log\lambda}$ it is a Hardy-space $H^2(\mathbb C^+)$ function with
$\|F\|_{L^2(\mathbb R)}^2=2\pi\|r\|^2$.

The support of $R$ is a half-line because $\mathcal E\phi$ spills all the way
down to $u\to0$ — which is the *definition* of the spill. So the failure is not
an artefact of how $r$ was cut: **the object H1 is about is intrinsically
incapable of satisfying the Paley–Wiener hypothesis.**

**Hypothesis (ii) fails.** The zeros are not $\delta$-separated for any fixed
$\delta>0$ — the mean gap $2\pi/\log(\gamma/2\pi)\to0$ — and they are not
relatively separated with a bounded constant either: $N$ would have to be
$\asymp\log T$, which is unbounded. (Simplicity of the zeros is itself open, so
even positive separation is not available.) This is the reason
`prolate-rate.md` §6(c) expects $\Theta=O(\log\mu)$, and that expectation is
right — but it comes from the *density*, which is Riemann–von Mangoldt, not from
Plancherel–Pólya.

**And under RH the situation is worse, not better.** If RH holds then every
$s_\rho$ is *real* — the sampling points sit exactly on the **boundary** of the
half-plane of holomorphy, where an $H^2$ function has only $L^2$ boundary values
and point evaluation is unbounded. The Carleson-measure machinery that would
replace Plancherel–Pólya for Hardy spaces bounds
$\sum_k|F(z_k)|^2\,\Im z_k$, and that weight vanishes identically under RH. **So
the entire Hardy/Carleson family of theorems is vacuous here, and it is RH that
makes it vacuous.**

*Recorded so it is not misread:* this is a statement about which proof techniques
apply. It is **not** evidence that H1 is false, and it is not a connection
between H1 and RH — see §8.

---

## 3. The zeta side, discharged — *ours*

Everything in this section is unconditional.

**Classical inputs**, both *proved* and both standard:

- **(RvM)** $\#\{\rho:|\gamma_\rho-t|\le1\}\le C_1\log(3+|t|)$, with multiplicity
  (Riemann–von Mangoldt).
- **(ZFR)** $\dfrac{c_0}{\log(3+|\gamma|)}\le\beta\le1-\dfrac{c_0}{\log(3+|\gamma|)}$
  (de la Vallée Poussin, together with the functional equation for the left
  inequality).

**Decay input.** Assume

> **(D)** $|R(v)|\le A\,e^{-v/2}$ for $v\ge\log\lambda$.

(D) makes $F$ holomorphic on $\{\Im s>-\tfrac12\}\supset\{|\Im s|<\tfrac12\}$,
which contains every $s_\rho$. §4 shows (D) is exactly what the prolate structure
supplies.

**Proposition 3.1 (ours).** *Under (D),*
$$\sum_{\rho}|F(s_\rho)|^2\;\le\;\frac{C}{c_0^{2}}
\int_{-1/2}^{1/2}\!\!\int_{\mathbb R}\log^3(3+|t|)\;|F(t+i\sigma)|^2\;dt\,d\sigma .
\tag{3.1}$$

*Proof.* Put $\epsilon_\rho:=\tfrac12\min(1,\beta_\rho,1-\beta_\rho)$, so
$\epsilon_\rho\ge\frac{c_0}{2\log(3+|\gamma_\rho|)}$ by (ZFR), and the disc
$D(s_\rho,\epsilon_\rho)$ lies in $\{|\Im z|<\tfrac12\}$, where $F$ is
holomorphic. $|F|^2$ is subharmonic, so
$|F(s_\rho)|^2\le\frac1{\pi\epsilon_\rho^2}\iint_{D(s_\rho,\epsilon_\rho)}|F|^2dA$.
Sum over $\rho$. A point $z=t+i\sigma$ lies in $D(s_\rho,\epsilon_\rho)$ only if
$|\gamma_\rho-t|\le1$, so by (RvM) it is covered at most $C_1\log(3+|t|)$ times,
and each covering $\rho$ contributes a weight
$\frac1{\pi\epsilon_\rho^2}\le\frac{4\log^2(3+|\gamma_\rho|)}{\pi c_0^2}
\ll\frac{\log^2(3+|t|)}{c_0^2}$, the last step because $|\gamma_\rho-t|\le1$. ∎

**Proposition 3.2 (Plancherel on horizontal lines; classical).** For
$|\sigma|<\tfrac12$,
$$\int_{\mathbb R}|F(t+i\sigma)|^2\,dt\;=\;2\pi\int_{\log\lambda}^{\infty}
|R(v)|^2e^{-2\sigma v}\,dv\;=:\;2\pi\,N(-\sigma). \tag{3.2}$$

So (3.1)+(3.2) reduce H1 to weighted $L^2$ norms of the spill — **no zeros
remain**. Two pieces of bookkeeping, and I flag both rather than claim them:

- **The $\log^3$ weight.** $\log^3(3+|t|)\le C_\delta(1+|t|)^{2\delta}$ for any
  $\delta>0$, so the weighted integral is $\ll_\delta\|R\,e^{-\sigma\cdot}\|^2_{H^{\delta}}$.
  $R$ is bounded with a single jump at $v=\log\lambda$ and is smooth to the right <!-- mg-731c: FALSE. R has a jump at u = lambda/N for EVERY integer N > mu, of size |Phi(1)| N^{-1/2} -- they are §4's own sawtooth. q3-log-weight-and-edge.md Cor. 1.2. -->
  of it, so $R\in H^{\delta}$ for every $\delta<\tfrac12$ and $\delta=\tfrac14$ is <!-- mg-731c: only for delta < 1/2 - alpha, and with a constant mu^{2 delta}. Prop. 2.2 there. -->
  comfortable. **This step needs a bound on $\|R'\|$ of the same character as (D),
  and I have not written it out.** It costs a factor $c$, i.e. poly. <!-- mg-731c: R' is not a function, and between jumps |R'| ~ mu t |R|, GROWING. §2.1 there. The step is not needed: §4 there freezes the weight instead. -->
- **The edges $\sigma\to\pm\tfrac12$.** $N(\alpha)$ diverges as <!-- mg-731c: ONE edge. sigma -> -1/2 (beta -> 0) only; sigma -> +1/2 is harmless. §3.1 there. -->
  $\alpha\uparrow\tfrac12$ under (D) alone, like $(1-2\alpha)^{-1}$. The discs are
  cut off at $\epsilon_\rho\gtrsim1/\log(3+|t|)$ by (ZFR), so the divergence is
  integrated only up to $\tfrac12-\tfrac{c_0}{2\log}$ and contributes a further <!-- mg-731c: NOT a further logarithm in this ordering: (ZFR) puts the edge at height e^{c_0/eta}, where the log^3 above is already (c_0/eta)^3, so int d(eta)/eta is really int d(eta)/eta^4 and DIVERGES. Obs. 3.1 there. -->
  logarithm. **This is the one place a zero-free region is used, and it is used
  only qualitatively.** I have checked the exponents, not written the estimate
  out in full.

Neither flagged step can cost more than a power of $\mu$ and a power of $\log$, <!-- mg-731c: right in conclusion, wrong in route. Xi = O(mu^{9/2} log^3 mu), by truncating the ZERO SUM at height e^{4 pi mu}: see §14. -->
which is all H1 can afford to give away — but "cannot cost more" is my reading of
the exponents, not a completed proof, and it is recorded here as such.

---

## 4. What is left is a prolate tail bound — *ours*

**An exact identity first** (*proved*; classical in substance). With
$\int_{-1}^1\Phi_n^2=1$ and $\Phi_n$ the entire extension, the finite Fourier
relation $\int_{-1}^1\Phi_n(y)e^{icxy}dy=\mu_\Phi\Phi_n(x)$ holds for **all**
$x$, and $\Lambda_n=\frac{c}{2\pi}\mu_\Phi^2$. Hence by Plancherel
$$\int_{|x|>1}|\Phi_n(x)|^2\,dx\;=\;\frac{1-\Lambda_n}{\Lambda_n}. \tag{4.1}$$
*The out-of-band energy of a prolate function is the integral of its own entire
extension outside the interval.* This is what makes the whole reduction possible:
the small quantity $1-\Lambda_n$ and the pointwise size of $\Phi$ off the interval
are the same object.

**The dictionary.** With $\phi(u)=\lambda^{-1/2}\Phi(u/\lambda)$ on
$[-\lambda,\lambda]$ one has $\widehat\phi(\xi)=\lambda^{1/2}\mu_\Phi\,\Phi(\xi/\lambda)$,
so writing $G(t)=\sum_{n\ge1}\Phi(nt)$ and using Poisson exactly as
`prolate-rate.md` §6(b) does,
$$\|r\|^2=\Lambda\!\int_1^\infty\!|G|^2dt,\qquad
N(\alpha)=\Lambda\,\lambda^{2\alpha}\!\int_1^\infty\!|G(t)|^2t^{2\alpha}dt .
\tag{4.2}$$

**Proposition 4.1 (ours).** *Assume* **(P)**: $\sup_{t>1}t|G(t)|\le K(c)|\Phi(1)|$.
*Then (D) holds with $A^2\ll\lambda K^2\Phi(1)^2$, and for $0\le\alpha<\tfrac12$*
$$N(\alpha)\;\le\;\frac{\lambda^{2\alpha}K^2\Phi(1)^2}{1-2\alpha}
\;\overset{\text{(§7)}}{\asymp}\;\frac{\lambda^{2\alpha}K^2\,c\,(1-\Lambda_4)}{1-2\alpha}.$$
*Combined with Prop. 3.1 and $1-\chi_2=\tfrac12(1-\Lambda_4)(1+o(1))$,*
$$\sum_{\rho}|\mathcal F_\mu r(s_\rho)|^2\;\le\;\Xi(\mu)\,(1-\chi_2(\lambda)),
\qquad \Xi=\mathrm{poly}(\mu)\cdot K(c)^2 . \tag{4.3}$$

(4.3) is what the paper's Corollary `cor:upper` consumes. So:

> **(P) with subexponential $K$ implies H1 and G5 together**, and hence
> $\limsup\mu^{-1}\log s(\mu)\le-4\pi$ modulo (H0) alone.

**Two gaps collapse into one, and the one is not about zeros.** Note also that
$\|r\|^2$ never appears in (4.3) — consistent with §1, and the reason G5 comes
along for free: G5 asks for $\|r\|^2=C_1(1-\chi_2)$ with $C_1=O(\log\mu)$, which
was only ever needed as an intermediate.

**The one step inside (P) that is not the single-term bound.** $G$ is a *sum* of
dilates, and the triangle inequality is log-divergent:
$\sum_n\frac{|\Phi(1)|}{nt}$ diverges. The cancellation is the sawtooth — using
Osipov–Rokhlin's exact off-band expansion (§6), the leading part of $G$ is
$$\frac{2\Phi(1)}{c\,t\,\mu_\Phi}\sum_{n\ge1}\frac{\sin(cnt)}{n}
=\frac{2\Phi(1)}{c\,t\,\mu_\Phi}\cdot\pi\left(\tfrac12-\{ct/2\pi\}\right),$$
whose modulus is at most $\frac{\pi|\Phi(1)|}{c\,|\mu_\Phi|\,t}$ — bounded, and of
exactly the shape (P) asserts. **The remainder term of that expansion is not
controlled here** (see §6), so the passage from the single-term bound to (P) is <!-- mg-9d43: Q2 is now PROVED — dilate-sum.md Thm 5.1. -->
*not* completed in this note; it is item **Q2** of §9. This is the honest status <!-- mg-9d43: and §6's reason for rejecting the remainder — "same exponential size" — was the WRONG variable. See §13. -->
and I have not smoothed it: §5 and §7 verify the single-term statement, not (P).

---

## 5. Half of (P), proved — *ours*

**Lemma 5.1.** *Let $\Phi=\Phi_{n,c}$ satisfy the prolate equation
$\big((1-x^2)\Phi'\big)'+(\chi_n-c^2x^2)\Phi=0$ and suppose $\chi_n<c^2$. Then*
$$|\Phi(x)|\;\le\;|\Phi(1)|\qquad\text{for all }x\ge1 .$$

*Proof.* For $x>1$ write $p:=(x^2-1)\Phi'$, $q:=c^2x^2-\chi_n$ and
$D:=(x^2-1)q$. The equation reads $p'=-q\Phi$, and $\chi_n<c^2$ gives $q>0$ on
$[1,\infty)$ and
$$D'=2x\big(2c^2x^2-\chi_n-c^2\big)>0\quad\text{on }[1,\infty),$$
since at $x=1$ the bracket is $c^2-\chi_n>0$ and it increases. Put
$V:=p^2/D+\Phi^2$. Then, using $\Phi'=p/(x^2-1)$,
$$V'=\frac{2pp'}{D}-\frac{p^2D'}{D^2}+2\Phi\Phi'
=-\frac{2pq\Phi}{D}-\frac{p^2D'}{D^2}+\frac{2\Phi p}{x^2-1}
=-\,p^2\frac{D'}{D^2}\;\le\;0 ,$$
the first and third terms cancelling identically because $D=(x^2-1)q$. So $V$ is
non-increasing on $(1,\infty)$. $\Phi$ is entire, so $\Phi'$ is bounded near
$x=1$ and $p(x)\to0$ there while $D(x)\to0$ linearly; hence
$p^2/D\to0$ and $V(1^+)=\Phi(1)^2$. Finally $\Phi^2\le V\le V(1^+)$. ∎

**Per mode, and what that means for the combination.** Lemma 5.1 is about a
single prolate function, since it uses the differential equation; the
near-radical vector is the three-mode combination $\phi=b_0\Phi_0+b_2\Phi_4+b_4\Phi_8$
of `prolate-rate.md` §2.1, which is not an eigenfunction of that operator.
The lemma still applies term by term:
$$|\phi(x)|\le\sum_m|b_m|\,|\Phi_{2m}(1)|\qquad(x\ge1),$$
and by §7's identity $\Phi_n(1)^2\asymp c(1-\Lambda_n)$ with $1-\Lambda_n$
increasing in $n$, so the right-hand side is dominated by the index-4 term —
the same mode that dominates the out-of-band energy in `prolate-rate.md` §6(b),
and for the same reason. **So nothing is lost in passing from modes to the
combination**, and the numbers below are reported per mode because that is what
the lemma is about.

**This is the right regime, and it is the complement of the published one.**
$\chi_n<c^2$ is exactly the condition that fails in Osipov–Rokhlin's theorems
(§6). Measured in `verify_h1.py` CHECK 2, at the prolate indices $n=0,2,4$ that
`prolate-rate.md` §2 forces:

| $c$ | $\chi_0/c^2$ | $\chi_2/c^2$ | $\chi_4/c^2$ |
|---|---|---|---|
| $2\pi\cdot2=12.566$ | $0.0747$ | $0.3724$ | $0.6387$ |
| $2\pi\cdot3=18.850$ | $0.0509$ | $0.2542$ | $0.4448$ |
| $2\pi\cdot5=31.416$ | $0.0311$ | $0.1553$ | $0.2751$ |
| $2\pi\cdot8=50.265$ | $0.0196$ | $0.0980$ | $0.1747$ |

all $<1$, decreasing in $c$ — and $\chi_n\sim(2n+1)c$ against $c^2$, so the
hypothesis of Lemma 5.1 is satisfied for every fixed $n$ once $c$ is large.
**In the limit that matters the lemma always applies.**

**What the lemma does not give.** It gives the amplitude, not the decay. (P) needs
$x|\Phi(x)|$ bounded, and Lemma 5.1 gives only $|\Phi(x)|$ bounded. The WKB
amplitude for this equation is $\Phi\sim\text{const}\cdot D^{-1/4}\asymp(cx)^{-1/2}\cdot$…
— the invariant that is *actually* constant is $\sqrt D\,V$, which satisfies
$$\big(\sqrt D\,V\big)'=\frac{D'}{2\sqrt D}\Big(\Phi^2-\frac{p^2}{D}\Big),$$
sign-indefinite, vanishing only on average over an oscillation. Turning that
average into a bound is a Levinson-type argument. <!-- mg-6851: the rest of this
paragraph claimed it "must be connected through x=1, a regular singular point".
That is WRONG. Q1 is PROVED without it: band-edge-connection.md §6, Thm 5.2. -->

---

## 6. Why the literature does not close it — *primary source, hypotheses checked*

Read as primary source from `arxiv.org/e-print/1208.4816`, file
`test12_arxiv.tex`: **A. Osipov and V. Rokhlin, "Detailed analysis of prolate
quadratures and interpolation formulas"** (Yale; the paper cites its own Yale CS
Technical Reports #1449, #1450 for several of the statements below, and those I
have *not* opened — marked accordingly).

Their $\lambda_n$ is our $\mu_\Phi$ and their $\mu_n$ is our $\Lambda_n$; their
$\chi_n$ is ours. Three results bear on (P), and **each must be checked against
our configuration rather than borrowed for its shape**:

**(a) `thm_psi1_bound` (`:2485`), second-hand in their paper, cited to
[RokhlinXiaoApprox] and the Yale reports.** *"Suppose that $c>0$ is a real
number, and that $\chi_n>c^2$. Then $\tfrac12<\psi_n^2(1)<n+\tfrac12$."*
— **Does not apply.** The hypothesis is $\chi_n>c^2$; we are at
$\chi_n/c^2\le0.64$ (§5). And the conclusion is visibly not ours: our $\Phi_n(1)^2$
is $10^{-52}$, not in $(\tfrac12,n+\tfrac12)$. The two regimes are disjoint and
this is the sharpest possible confirmation that they are.

**(b) `thm_extrema` (`:2497`).** The unconditional half bounds successive
extrema of $\psi_n$ *inside* $(-1,1)$; the half that reaches $|\psi_n(1)|$ again
assumes $\chi_n>c^2$. — **Does not apply**, and in any case it is a statement
about $(-1,1)$, not about $x>1$. Lemma 5.1 is the $x>1$ statement in the
complementary regime, and I did not find it in this paper.

**(c) `lem_psi_for_large_x` (`:4350`), proved there from their integral equation
`eq_prolate_integral2`.** For $x>1$ and $n$ even, **an exact identity**:
$$\psi_n(x)=\frac{2\psi_n(1)}{cx\lambda_n}\left[\sin(cx)+
\frac{1}{\lambda_n\psi_n(1)}\int_{-1}^1\frac{\sin\big(c(x-t)\big)\,\psi_n(t)\,t}{x-t}\,dt\right].$$
— **Applies, and does not suffice.** The paper says so itself, in the sentence
introducing it: the estimates "are meaningful only when $x$ is large compared to
$|\lambda_n|^{-1}$". In our regime the bracket's second term carries
$\psi_n(1)^{-1}\asymp e^{c}$, so the identity is informative only for
$x\gtrsim e^{c}$ — i.e. nowhere near the band edge, which §7 shows is exactly
where the supremum in (P) is attained ($x\approx1.008$).

That remainder is not a nuisance term. Its integral is the sinc kernel applied to
$t\,\psi_n(t)$, i.e. **the out-of-band leakage of $t\Phi(t)$** — an object of the
same exponential size as the quantity being bounded, expanded in the same prolate
family. The identity is therefore a *bootstrap relation among the off-band values
of the whole prolate family*, not an estimate for one of them. **That is the
precise form of the obstruction**, and it is why (P) is not a corollary of
anything published: the literature's off-band results live at $\chi_n>c^2$, and
the one result that lives everywhere is an identity that closes on itself.

---

## 7. The endpoint identity — *observed, not proved*

**Claim (observed).** With $\int_{-1}^1\Phi_n^2=1$,
$$\Phi_n(1)^2\;=\;c\,(1-\Lambda_n)\left(1-\frac{2n+1}{4c}+O(c^{-2})\right).$$

*Where it comes from.* Combine (4.1) with the leading off-band form
$\Phi_n(x)\approx\frac{2\Phi_n(1)\sin(cx)}{cx\,\mu_\Phi}$ and
$\mu_\Phi^2=2\pi\Lambda_n/c$: the naive computation gives
$\Phi_n(1)^2\approx\frac{\pi c}{2}(1-\Lambda_n)$, which is **too large by exactly
$\pi/2$** — the naive form over-counts the tail because it is not valid down to
the band edge. The measured constant is $c$, not $\frac{\pi c}{2}$.

`verify_h1.py` CHECK 1, at 200–320 digits; the last column is what the claimed
$O(c^{-1})$ correction predicts:

| $c$ | $n$ | ratio $\Phi_n(1)^2/\big(c(1-\Lambda_n)\big)$ | $(1-\text{ratio})\cdot c$ | $(2n+1)/4$ |
|---|---|---|---|---|
| $75.398$ | 0 | $0.996645134246$ | $0.252951$ | $0.25$ |
| $75.398$ | 2 | $0.983175871734$ | $1.26851$ | $1.25$ |
| $75.398$ | 4 | $0.969418730520$ | $2.30577$ | $2.25$ |
| $200$ | 0 | $0.998744496662$ | $0.251101$ | $0.25$ |
| $200$ | 2 | $0.993715933474$ | $1.25681$ | $1.25$ |
| $200$ | 4 | $0.988648657679$ | $2.27027$ | $2.25$ |
| $320$ | 0 | $0.999216605363$ | $0.250686$ | $0.25$ |
| $320$ | 2 | $0.996080512845$ | $1.25424$ | $1.25$ |
| $320$ | 4 | $0.992929479657$ | $2.26257$ | $2.25$ |

The residual column converges to $(2n+1)/4$ at all three indices, and the
approach is $O(1/c)$, as an $O(c^{-2})$ next term requires. **This is a numerical
observation, not a theorem**, and no number of values of $c$ makes it one; it is
recorded because it is what calibrates $K$, and because it is sharp enough to be
falsified cheaply by anyone who wants to.

**The single-term decay constant.** `verify_h1.py` CHECK 3 measures
$K_1:=\sup_{x>1}x|\Phi_n(x)|/|\Phi_n(1)|$ over $1<x\le14$ in steps of $0.008$
(strictly interior, so the endpoint is not the answer by construction):

| $c$ | $n=0$ | $n=2$ | $n=4$ | attained near |
|---|---|---|---|---|
| $12.566$ | $0.4987$ | $0.6449$ | $0.7889$ | $x\approx1.008$ |
| $18.850$ | $0.3985$ | $0.3943$ | $0.3981$ | $x\approx1.02$–$1.04$ |
| $31.416$ | $0.4028$ | $0.3981$ | $0.3637$ | $x\approx1.008$ |
| $50.265$ | $0.2262$ | $0.2369$ | $0.2511$ | $x\approx1.02$ |

$K_1<1$ throughout, no growth in $c$ — and the supremum sits **just above the
band edge**. <!-- mg-6851: this grid starts 0.008 ABOVE x=1, and the true sup over
x>=1 is 1, attained AT x=1. Do not quote 0.79 as the constant in Q1; the proved
one is K(c) = 2^{3/4}e^{E(c)}. See band-edge-connection.md §7. --> Also measured:
$\sup_{x>1}|\Phi_n(x)|/|\Phi_n(1)|\le0.79$, consistent with Lemma 5.1 (a grid can
only under-report a supremum; the lemma is what is relied on).

**Numerical hygiene.** CHECK 0 validates the entire extension before it is used:
the spherical-Bessel series is checked against the Legendre series at $x=1$,
agreeing to $10^{-41}$–$10^{-59}$ relative, and is stable when the Miller
recurrence is started 200 indices higher. That check exists because two earlier
drafts of the script were wrong: one started the downward recurrence above
$k_{\max}$ instead of above $z=cx$, and one normalised on $j_0(z)=\sin z/z$,
which is near zero exactly when $x$ is near an integer. The second error survived
the first fix and produced values wrong by $1.5\%$ to $59\%$ — with no symptom,
since the normalisation still "succeeded". The failing column is left in the
script's output on purpose.

---

## 8. The house rule, applied to this note

> **Is any statement in this note false for $-W_\lambda$?**

| item | under $-W_\lambda$ | verdict |
|---|---|---|
| 1. Plancherel–Pólya does not apply | a statement about supports and separation | **sign-blind** |
| 2. Prop. 3.1, the density reduction | $|F|^2$ is unchanged; the sum is unchanged | **sign-blind** |
| 3. Lemma 5.1, the amplitude bound | about the prolate ODE only | **sign-blind** |
| 4. the endpoint identity §7 | about $\Lambda_n$ and $\Phi_n(1)$ only | **sign-blind** |
| 5. (P) $\Rightarrow$ H1 $\Rightarrow$ $\limsup\le-4\pi$ | $QW_\lambda(g,g)$ negates, the *upper* bound on $s$ becomes an upper bound on $-s$ | **sign-blind as a magnitude claim** |

**Every single item is sign-blind, and that is the correct answer.** H1 is a
statement about $\sum_\rho|\mathcal F_\mu r|^2$, a sum of squared moduli; it
cannot distinguish $W$ from $-W$ and was never going to. `prolate-rate.md` §7
already located this: the prolate mechanism governs $|s|$, the sign is elsewhere,
and the elsewhere is RH. **This note lives entirely on the sign-blind side, by
construction, and proving (P) would not move it.**

One consequence worth stating because §2 could be misread: the fact that RH makes
the Hardy/Carleson route vacuous is a fact about *proof technique*, not a
reduction. H1 does not imply RH, is not implied by RH, and does not approach it.
If any argument in this direction ever appears to yield a lower bound on
$s(\mu)$, it is wrong — `prolate-rate.md` §7, and the ticket, are right about
that and this note found nothing that disturbs it.

---

## 9. Open — what would finish it

| # | item | status |
|---|---|---|
| **Q1** | Prove $x|\Phi_{n,c}(x)|\le K|\Phi_{n,c}(1)|$ for $x\ge1$ with $K$ subexponential, in the regime $\chi_n<c^2$. Lemma 5.1 gives the amplitude; what is missing is the WKB decay ~~which must be connected through the **regular singular point $x=1$**~~ (mg-6851: it need not be — the row's diagnosis was wrong) | **PROVED (mg-6851), [`band-edge-connection.md`](band-edge-connection.md) Thm 5.2, with $K(c)=2^{3/4}e^{E(c)}$ *bounded*, $\downarrow2^{3/4}$. Q2 now carries the weight** |
| **Q2** | Pass from the single-term bound (Q1) to (P) for $G=\sum_{n\ge1}\Phi(n\,\cdot)$. The mechanism is the sawtooth $\sum_n n^{-1}\sin(cnt)$ (§4) — right; ~~what must be controlled is the sum of the *remainders* in Osipov–Rokhlin's exact expansion, which is the off-band leakage of $t\Phi(t)$ (§6)~~ (mg-9d43: wrong variable — what is needed is one more power of $x$, not one less power of $e^{c}$) | **PROVED (mg-9d43), [`dilate-sum.md`](dilate-sum.md) Thm 5.1, with $K_P(c)=O(\log c)$. The evaluation cost was on the wrong side of a Poisson summation: `dilate-sum.md` Prop. 6.1 makes $tG(t)$ a sum of $\lfloor\mu t\rfloor+1$ *on-band* values. Q3 now carries the weight** |
| **Q3** | Write out the two flagged steps of §3: ~~the fractional-Sobolev handling of the $\log^3$ weight~~ (mg-731c: its premise is false and the step is not needed), and the $\sigma\to\pm\tfrac12$ edge ~~$\pm$~~ (mg-731c: one edge, and it does not converge in this ordering) | **CLOSED (mg-731c), [`q3-log-weight-and-edge.md`](q3-log-weight-and-edge.md) Thm 4.4, $\Xi=O(\mu^{9/2}\log^3\mu)$ — but NOT routine: one premise false, one ordering divergent, and the repair uses §6(a) of `prolate-rate.md`, which §3 does not name. the $-4\pi$ upper bound now rests on (H0)/Q4 alone. It is (4.3) that is proved, not (H1) as §0 writes it — §1 rules that form out** |
| **Q4** | (H0), $\|g\|^2$ bounded below — untouched here. It is the paper's other half of G6 and ~~is a mean value of $|\zeta(\tfrac12+it)|^2$ against an explicit weight~~ (mg-6818: it is **not**. No mean value of $\zeta$ is involved anywhere in it) | **PROVED (mg-6818), [`h0-lower-bound.md`](h0-lower-bound.md) Thm 6.1: $\|g\|^2\to\|\mathcal E\phi_\infty\|^2=0.2192471995\ldots$, with $\phi_\infty=\sqrt{8/11}(h_4-\sqrt{3/8}h_0)$ — `start.tex:39`'s own vector. $\|g\|^2\ge\int_A^B|\mathcal E\phi|^2d^*u$ over any fixed compact, which is a finite sum of ON-BAND prolate values; the content is that $\phi_\lambda$ does not degenerate, and that is Dunster 2017 (arXiv:1601.00699) eq. (124), whose standing hypothesis $\lambda<0$ IS our $\chi<c^2$. **The $-4\pi$ upper bound is now unconditional**; see §15** |
| **Q5** | Prove the endpoint identity §7, including the constant $c$ (not $\pi c/2$) and the $-(2n+1)/(4c)$ correction. It may well be in Slepian's or Fuchs' asymptotics in some normalisation; I did not find it | **observed only** |

**What this note did not do:** it did not prove H1, and it did not find a
published theorem that proves H1. Anyone quoting it should quote the reduction
and Lemma 5.1, not a resolution.

---

## 10. Provenance

**Read as primary source**, from arXiv LaTeX downloaded 2026-08-12:

- `arxiv.org/e-print/1208.4816`, `test12_arxiv.tex` (Osipov–Rokhlin, *Detailed
  analysis of prolate quadratures and interpolation formulas*): title/authors at
  `:60`–`:66`; the integral equation `eq_prolate_integral2` at `:891`;
  `prop_sharp_simple` and the summary of the tail estimates at `:570`–`:625`;
  `thm_psi1_bound` ($\tfrac12<\psi_n^2(1)<n+\tfrac12$ under $\chi_n>c^2$) at
  `:2485`; `thm_extrema` at `:2497`; the exact off-band expansion
  `lem_psi_for_large_x` at `:4350`–`:4366`.

**Cited by them, not opened by me, and therefore marked:** Rokhlin–Xiao's
approximation paper and Yale CS Technical Reports #1449/#1450, which are where
their §6(a),(b) statements are proved. Nothing in this note rests on those — they
are quoted only to be ruled *out* by their hypotheses, and the hypothesis
$\chi_n>c^2$ is printed in the paper I did read.

**Classical, quoted and used, not re-derived:** Plancherel–Pólya (1937);
Riemann–von Mangoldt $N(T+1)-N(T)\ll\log T$; the de la Vallée Poussin zero-free
region; Plancherel; subharmonicity of $|F|^2$; the finite-Fourier eigenrelation
for prolate functions and $\Lambda_n=\frac{c}{2\pi}\mu_\Phi^2$ (the last two are
`verify_prolate_rate.py`'s apparatus, validated there against Slepian's tabulated
$\Lambda_0(1)=0.57258$).

**Taken from our own notes, not re-derived:** the identity
$QW_\lambda(g,g)=\sum_Z|\mathcal F_\mu r|^2$ and the Poisson/orthogonality
computation of the spill (`prolate-rate.md` §6); the forcing of prolate index 4
(`prolate-rate.md` §2, `index-convention.md`, mg-aedf); $1-\chi_2=\tfrac12(1-\Lambda_4)$
and Connes' asymptotic (`semilocal-gap.md` §5.2, `prolate-rate.md` §3); the
RH-equivalence of the lower bound (`rhready.tex:1145`, `prolate-rate.md` §7).

**Derived here, marked *ours* at the point of use:** the reformulation of H1 as a
ratio and the observation that the $\|r\|^2$ normalisation is unattainable (§1);
that both Plancherel–Pólya hypotheses fail and that the first fails structurally,
and that RH makes the Carleson route vacuous (§2); Prop. 3.1 and the reduction to
weighted $L^2$ norms of the spill (§3); the collapse of H1 and G5 into the single
hypothesis (P), and Prop. 4.1 (§4); Lemma 5.1 and its regime (§5); the reading of
Osipov–Rokhlin's expansion as a bootstrap among off-band prolate values, and the
verification that their hypotheses exclude our regime (§6); the endpoint identity
and its $(2n+1)/4$ correction, observed (§7).

**The claim here that would do the most damage if wrong** is Prop. 4.1's
arithmetic — that (P) implies (4.3) with only polynomial loss — because it is
what makes the reduction worth having. Its exposure is the two flagged steps of
§3, which are exponent-checked rather than written out. The second-most damaging
would be §6's reading of the hypotheses of Osipov–Rokhlin's theorems; that one is
quoted verbatim from the source and the disjointness of the regimes is confirmed
numerically in §5, so it is the better-guarded of the two.

---

## 11. Effect on `prolate-rate.md` and on the paper

`prolate-rate.md` is annotated at §6(c) and §11 (append-only; its conditional
statement is *not* rewritten, and remains correct as stated). The paper is **not**
edited — amending it is a separate ticket, and if it is taken up, the changes
this note supports are:

1. **G5 and G6 are not independent.** Both follow from (P). The gap list should
   say so.
2. **"of Plancherel–Pólya type" should go** (paper `:1248`). It names a theorem <!-- mg-6467: DONE. Paper §7.1 `:1504`; the correct one-line description is in the paper's §7.2 lead. -->
   that cannot apply and points at the zeros, which are not the obstruction. A
   correct one-line description is: *a weighted-$L^2$ tail bound for the entire
   extension of a prolate function outside its interval.*
3. **The sentence "the sum converges only because the zero density is
   logarithmic"** (paper `:1252`) is right, and Prop. 3.1 makes it the actual <!-- mg-6467: DONE. Prop. 3.1 is the paper's Prop. 7.3 at `:1605`, and the density-is-the-mechanism reading is the bullet after it. -->
   mechanism rather than an aside.
4. Neither change touches G10, Theorem `thm:boundary`, or anything about the sign.

---

## 12. Appended by mg-6851 — Q1 is proved, and §5's diagnosis of it was wrong

*Append-only. Nothing above is rewritten; the in-place annotations are HTML
comments and change no line count. Companion note:
[`band-edge-connection.md`](band-edge-connection.md), script
[`verify_q1.py`](verify_q1.py).*

**Q1 is proved.** For every real solution $\Phi$ of the prolate equation analytic at
$x=1$, every $c>\sqrt2$ and every $\chi$ with $0\le\chi<c^2$ (and $\chi_n\ge n(n+1)$,
so the lower bound is free),
$$x|\Phi(x)|\le K(c)|\Phi(1)|\ (x\ge1),\qquad
K(c)=2^{3/4}e^{E(c)},\quad
E(c)=\frac{5\sqrt2}{c-\sqrt2}+\frac{\sqrt2c/3+2}{(c-\sqrt2)^2}.$$
$K$ is **bounded**, not merely subexponential, is independent of the index $n$
throughout $\chi_n<c^2$, and decreases to $2^{3/4}=1.6818$. At our bandwidths
$K=3.379$ ($c=4\pi$) down to $1.861$ ($c=24\pi$). So Prop. 4.1 above has its
hypothesis on the single-term side, and (P) is now **exactly** Q2.

**Three corrections to this note, and the first is the one that matters.**

1. **§5's closing diagnosis is wrong.** "That connection is the whole of what is
   missing" — it is not. The factor $x$ is worth nothing on a bounded interval, so
   the asymptotic argument may start at $x=\sqrt2$, where **Lemma 5.1 itself
   supplies the initial amplitude**. The regular singular point is never crossed.
   Lemma 5.1 does more than this note credits it with: it is not only the amplitude
   half of Q1, it is also the connection.
2. **§5's amplitude identity is right and is the mechanism.** $(\sqrt DV)'$, divided
   by $2\sqrt DV$, is exactly $A'/A=-\frac{D'}{4D}\cos2\theta$ for $A=\rho D^{1/4}$.
   The mean cancels identically; what closes it is that the phase speed satisfies
   $k^2=c^2+\frac{c^2-\chi}{x^2-1}>c^2$, so one integration by parts costs $O(1/c)$.
   **$\chi<c^2$ is exactly "no turning point outside the band"**, which is the same
   fact as §6's finding that Osipov–Rokhlin's regime is the negation of ours.
3. **§7's $K_1\le0.79$ is a grid artefact and should not be quoted as Q1's
   constant.** That grid starts $0.008$ above $x=1$; the supremum of
   $x|\Phi(x)|/|\Phi(1)|$ over $x\ge1$ is $1$, attained at $x=1$. §7 flags the
   exclusion and is not wrong, but the number has since been quoted as if it were
   the constant, including in vision amendment 11 §4.

**What is genuinely a connection problem at the band edge** is the *sharp* constant:
$A\to\sqrt{2/\pi}|\Phi(1)|$ would give $K=O(c^{-1/2})$ rather than $O(1)$, and that
does need the $J_0$ matching at $x=1$. It is **observed, not proved**, filed as Q1′
in `band-edge-connection.md` §9, and **nothing downstream needs it**.

**One hypothesis cell fails, and it is in this note's blind spot.** §5's table stops
at $n=4$; measured at $n=0,\dots,8$, **$\chi_8/c^2=1.040$ at $c=4\pi$** — so the
theorem does not cover prolate index 8 at $\mu=2$ (it does for $\mu\ge3$, and covers
$n=0,2,4,6$ throughout). §5's *text* names the combination
$b_0\Phi_0+b_2\Phi_4+b_4\Phi_8$ while its *table* is at $n=0,2,4$; which is right is
`index-convention.md`'s question (mg-9433 put the corpus's mode at index 4) and was
not re-opened.

**Unchanged:** Q2, Q3, Q4, Q5; §§1–4; the reduction of H1 and G5 to (P); every
sign-blindness verdict in §8. H1 is still not proved.

---

## 13. Appended by mg-9d43 — Q2 is proved, and §§4/6's diagnosis of it was wrong

*Append-only. Nothing above is rewritten; the in-place annotations are HTML comments
and change no line count. Companion note: [`dilate-sum.md`](dilate-sum.md), script
[`verify_q2.py`](verify_q2.py).*

**Q2 is proved.** For every even index $n$, every $c>\sqrt2$ and every $\chi_n$ with
$0\le\chi_n<c^2$,
$$\sup_{t>1}t\Big|\sum_{m\ge1}\Phi_n(mt)\Big|\le K_P(c)\,|\Phi_n(1)|,\qquad
K_P(c)=O(\log c),$$
explicitly $K_P=\frac{\pi}{c|\mu_\Phi|}+B_1(3+\log\frac{B_2}{B_1})$ with
$B_1=K_1+\frac2{c|\mu_\Phi|}$, $B_2=K_1(6c+2^{-1/2})$ and $K_1$ the proved Q1
constant. Numerically $26.5$ at $c=4\pi$, minimum $17.9$ near $c\approx80$, never
above $27$ in this project's range. **So Prop. 4.1 above has its hypothesis, and
what stands between this note and H1 is Q3 alone** (plus Q4/H0, which is separate).

**Four corrections to this note, and the first is the one that matters.**

1. **§4's and §6's diagnosis of Q2 is wrong.** §6 rejects Osipov–Rokhlin's remainder
   because it is "an object of the **same exponential size** as the quantity being
   bounded", and §9's Q2 row repeats it. That is true and it is **not** an
   obstruction. The naive bound fails because $\sum_m\frac1m$ diverges — a
   *harmonic* divergence, caused by the exponent $1$ in $x^{-1}$ and by nothing
   else. The factor $|\Phi(1)|$ sits outside the sum and its size is irrelevant.
   **(P) needs one more power of $x$, not one less power of $e^{c}$**, and a
   remainder of exactly the size $|\Phi(1)|$ costs nothing once it carries $x^{-2}$.
   `dilate-sum.md` Prop. 4.1 supplies exactly that, from Q1 and one application of
   variation of parameters to the Liouville form $u=\sqrt{x^2-1}\,\Phi$.
2. **Q1 is not merely *an* input to Q2; it is *the* input.** Q1 says
   $x|\Phi|\le K_1|\Phi(1)|$, which says exactly that $u=\sqrt{x^2-1}\Phi$ is
   **bounded** — and bounded $u$ against the integrable perturbation
   $\epsilon=\frac{c^2-\chi+1}{x^2-1}$ is what makes the Lagrange coefficients
   converge. §5's Lemma 5.1 alone is **not** enough: it gives
   $|u|\le\sqrt{x^2-1}|\Phi(1)|$, which grows.
3. **§4's sawtooth is the right mechanism, and it is right for a reason this note
   does not state: the leading off-band term is a *pure sine*.**
   $\Phi(x)=\frac{a_1\sin(cx)}{x}+O(x^{-2})$ with **no cosine** —
   $\beta_\infty=0$ — and that is a *quantisation* statement, proved from the
   finite-Fourier eigenrelation, not from the ODE. It is not decoration:
   $\sum_m m^{-1}\cos(cmt)=-\log|2\sin\frac{ct}2|$ is **unbounded**, so a solution of
   the same equation with $\beta_\infty\ne0$ has $\sup_t t|G(t)|=+\infty$.
   **(P) is false for a general solution of the prolate equation and true for the
   eigenfunctions** (`dilate-sum.md` Cor. 3.4), so no ODE-only argument can prove Q2.
4. **§9's Q2 row is wrong about the blocker too.** "The evaluation cost of
   $\Phi(nt)$ for $n$ large defeated it" — the cost was on the wrong side of a
   Poisson summation. With $h=1/(\mu t)$,
   $$t\,G(t)=\frac{1}{2\mu\,\mu_\Phi}\sideset{}{'}\sum_{|k|\le\lfloor\mu t\rfloor}
   \Phi\Big(\frac{k}{\mu t}\Big)-\frac{t\,\Phi(0)}{2}$$
   exactly (`dilate-sum.md` Prop. 6.1): $\lfloor\mu t\rfloor+1$ evaluations of $\Phi$
   **inside** $[-1,1]$, at $O(c)$ each, in place of an infinite conditionally
   convergent sum of off-band values at $O(cmt)$ each. At $\mu=5$, $t=3$ that is
   16 terms. The price is $10^3$–$10^8$ of cancellation, which is what arbitrary
   precision is for.

**A defect found in this note's own apparatus, and it invalidates nothing here.**
`verify_h1.sph_j_all` normalises on the sum rule — its docstring is right about why
$j_0(z)=\sin z/z$ must not be used — and then fixes the remaining **sign** by that
same ill-conditioned quantity. At $c=6\pi$, $x=200$ the test compares against
$\sin z=10^{-118}$, i.e. rounding noise, and returns the wrong global sign. **Every
number this note and `band-edge-connection.md` report from that routine is a
modulus**, in which a global sign flip is invisible, so nothing above changes; it is
fatal only where the explicit leading term is subtracted, which is `dilate-sum.md`
§4. The fixed copy is in `verify_q2.py` and agrees with the original to 0 ulp at
every index for generic $z$.

**Unchanged:** Q3, Q4, Q5; §§1–3; the reduction of H1 and G5 to (P), which
`dilate-sum.md` quotes and does **not** re-verify; every sign-blindness verdict in
§8. **H1 is still not proved** — Q3 is unwritten — but the two substantive items are
now closed and what remains is described in this note's own §9 as routine.

---

## 14. Appended by mg-731c — Q3 is closed, and neither flagged step was what §3 says

*Append-only. Nothing above is rewritten; the in-place annotations are HTML comments
and change no line count. Companion note:
[`q3-log-weight-and-edge.md`](q3-log-weight-and-edge.md), script
[`verify_q3.py`](verify_q3.py).*

**Q3 is closed.** Assuming (P) — proved, Q1+Q2 —
$$\sum_\rho|\mathcal F_\mu r(s_\rho)|^2\le\Xi(\mu)\,(1-\chi_2(\lambda)),\qquad
\Xi(\mu)=O\big(\mu^{9/2}\log^3\mu\big),$$
polynomial, so Prop. 4.1 above consumes it and the paper's
$\limsup\mu^{-1}\log s(\mu)\le-4\pi$ is now conditional on **(H0)/Q4 alone**. That is a
real improvement to a result this project already has and it is **not** progress toward
RH: §8's verdicts are unchanged, every line of the new note is sign-blind, and the
matching lower bound is still RH.

**Said precisely: this is (4.3), not (H1) as §0 writes it.** §1 above proves that no
bound of the form $\Theta(\lambda)\|r\|^2$ can exist, so (H1) *as printed* is not what
was closed and never could be; (4.3) is the estimate that replaced it and the one
Cor. `cor:upper` consumes. **H1's role is discharged; H1 as literally written is
bypassed.** Anyone quoting this should quote (4.3), and the paper's `:1242` should be <!-- mg-6467: DONE. (H1) is now stated at `:1421` and disposed of in §7.1, `:1504`. -->
restated the same way.

**But "routine" was wrong, and it was wrong differently on each step.**

1. **§3's first bullet is FALSE where it is most specific.** "$R$ is bounded with a
   single jump at $v=\log\lambda$ and is smooth to the right of it" — $R$ has a jump at
   $u=\lambda/N$ for **every** integer $N>\mu$, of size exactly $|\Phi(1)|N^{-1/2}$,
   because $\mathcal E\phi(u)=u^{1/2}\sum_{n\le\lambda/u}\phi(nu)$ is a finite sum whose
   terms switch on one at a time and $\phi(\lambda)=\lambda^{-1/2}\Phi(1)\ne0$. Measured
   against one-sided limits at 24 cells, ratio $1.0$ to every printed digit.
   **Those jumps are §4's own sawtooth** $\tfrac12-\{ct/2\pi\}$: §3 and §4 of this note
   contradict each other, and §4 is right. `prolate-rate.md` §6(c) carries the same
   error and is annotated too.
2. **The input the first bullet asks for does not exist.** "A bound on $\|R'\|$ of the
   same character as (D)": $R'$ is not a function (it carries a delta at every jump),
   and between jumps $|R'|\asymp\mu t|R|$ — growing, where (D) decays. What a Sobolev
   route would need is a *derivative* dilate-sum bound, of exactly Q2's type, named (P′)
   in the new note and **not proved anywhere**; the only substitute available today
   costs $\|\Phi'\|_\infty/|\Phi(1)|\asymp e^{c}$, measured $1.3\times10^2$ at $c=4\pi$
   rising to $1.3\times10^{17}$ at $c=16\pi$.
3. **§3's second bullet has one edge, not two.** $N(\alpha)$ diverges only as
   $\alpha\uparrow\tfrac12$, i.e. only as $\sigma\to-\tfrac12$, i.e. only as
   $\beta_\rho\to0$. The $+$ side is harmless, and the pairing $\rho\leftrightarrow1-\bar\rho$
   means the $-$ side cannot be avoided.
4. **The second bullet does not converge in the order it proposes, and the reason is
   the first bullet.** (ZFR) makes the edge at $\eta=\tfrac12-|\sigma|$ draw only on
   $|t|\ge e^{c_0/\eta}$, where the $\log^3(3+|t|)$ weight is *already* $(c_0/\eta)^3$.
   So "a further logarithm", $\int d\eta/\eta$, is really $\int d\eta/\eta^4$, and it has
   no cutoff. **The two flagged steps are not independent and cannot be costed
   separately** — which is exactly how this note costs them.

**What closes it is a truncation, and it uses an input §3 never mentions.** Split the
zero sum at $T_*=\exp(4\pi\mu+O(\log\mu))$. Above $T_*$, use §6(a) of `prolate-rate.md`
— $\mathcal F_\mu r=-\mathcal F_\mu g$ on $Z$ — and the bounded variation of $g$ on a
compact interval in $\log u$; those zeros contribute below the target because
$\Phi(1)^2\ge(1-\Lambda_4)/(2K_1^2C_*^2)$, a **proved** lower bound obtained here from
Q1 and the exact identity (4.1) above, together with Fuchs. Below $T_*$ the $\log^3$
weight is a constant, $O(\mu^3)$, so **no fractional Sobolev theory is needed at all**,
and the same truncation caps the edge at $\eta_*\asymp c_0/\mu$, which is what makes the
"further logarithm" true after all. The whole cost is the $\mu^3$, and it is forced by
the size of the target rather than by any analysis.

**Also closed, in passing: half of Q5.** $\Phi_n(1)^2\ge(1-\Lambda_n)/(2K_1^2\Lambda_n)$
is now proved (Q1 plus (4.1)); the reverse inequality follows from `dilate-sum.md`
Prop. 4.1(ii) and is sketched but not written out. The *constant* $c$ and the
$-(2n+1)/(4c)$ correction remain **observed only**.

**Unchanged:** Q4/(H0), which is untouched by design; §§1–2; the reduction of H1 and G5
to (P); Prop. 3.1 and Prop. 3.2 themselves, which are correct as stated — it is the two
bookkeeping bullets after them that were not. **This is the third inherited misdiagnosis
on this chain** (mg-6851 on §5, mg-9d43 on §§4/6, this on §3), and the pattern is now
three for three: the note was right that something was missing and wrong about what.

---

## 15. Appended by mg-6818 — Q4/(H0) is proved, and §9's description of it was wrong

*Append-only. Nothing above is rewritten; the in-place annotation in §9 is inside the existing
Q4 row and changes no line count. Companion note:
[`h0-lower-bound.md`](h0-lower-bound.md), script [`verify_h0.py`](verify_h0.py).*

**(H0) is proved, and $\|g\|^2$ does not merely stay above zero — it converges.**
$$\lim_{\lambda\to\infty}\|g(\lambda)\|^2=\|\mathcal E\phi_\infty\|^2=0.219247199549\ldots,
\qquad \phi_\infty=\sqrt{\tfrac8{11}}\big(h_4-\sqrt{\tfrac38}h_0\big),$$
measured at $\mu=3,5,8,12,20$ and computed in the limit two independent ways agreeing to $22$
digits. So Cor. `cor:upper` has both its hypotheses, and with Q1+Q2+Q3 **and §A of that note**,
$$\limsup_{\mu\to\infty}\mu^{-1}\log s(\mu)\le-4\pi\quad\textbf{unconditionally},$$
quantitatively $s(\mu)\le(4.5610\ldots+o(1))\,\Xi(\mu)(1-\chi_2)
=O(\mu^{21/2}\log^3\mu\,e^{-4\pi\mu})$. It is **not** progress toward RH: §8's verdicts are
unchanged, every line of the new note is sign-blind, and the matching lower bound is still RH.

**Closing (H0) was not by itself enough, and the shortfall was inherited.** mg-731c's Thm 4.4
bounds the zero sum by $\Phi(1)^2$ and its §4 cost table converts $\Phi(1)^2\to(1-\chi_2)$
citing **§7 above, which is observed** — and §14 above records the needed half as "sketched
but not written out". §A of the new note writes it out, $\Phi_n(1)^2=O(c^{5/2}(1-\Lambda_n))$,
from `dilate-sum.md` Prop. 4.1(ii) and the exact identity (4.1) of §4 above; the cost is $\mu^{3/2}$
over the observed truth, so $\Xi=O(\mu^6\log^3\mu)$ proved in place of $O(\mu^{9/2}\log^3\mu)$
observed. **Anyone printing "unconditional" is quoting §A as well as Q4.**

**Say it in the true sentence, not the convenient one.** §14 already made this point and it
matters more now that nothing is left conditional: **do not write "H1 is proved".** §1 above
proves that no bound of the form $\Theta(\lambda)\|r\|^2$ exists, so (H1) *as printed at* `:1242` <!-- mg-6467: now `:1421`. -->
is false in that form and was bypassed, not proved. What holds is **(4.3)** plus **(H0)**.

**§9's Q4 row was wrong about what (H0) is, and the error is the same shape as the previous
three.** "A mean value of $|\zeta(\tfrac12+it)|^2$ against an explicit weight" — there **is**
such an identity, $\|\mathcal E\phi\|^2=\frac1{2\pi}\int|\Gamma_{\mathbb R}\zeta P_\phi|^2$,
and it is one route to the *whole* norm when only a *lower bound* is wanted.

1. **$\|g\|^2$ is its own integral over its own range, with no $\zeta$ in it.** With
   $u=\lambda/t$ and $S(t)=\sum_{n\le t}\Phi(n/t)$,
   $$\|g\|^2=\int_1^{\mu}\frac{S(t)^2}{t^2}dt,\qquad \|r\|^2=\int_\mu^\infty\frac{S(t)^2}{t^2}dt,$$
   exactly, every argument $n/t$ **on band**. `h0-lower-bound.md` Lemma 2.1. The subtraction
   $\|g\|^2=\|\mathcal E\phi\|^2-\|r\|^2$, which is what makes (H0) look like a statement about
   the whole critical line, is never needed.
2. **A fixed compact window suffices**, because $\|g\|^2\ge\int_A^B|\mathcal E\phi|^2d^*u$ for
   every $[A,B]\subseteq[\lambda^{-1},\lambda]$ — and $\int_{1/2}^2$ recovers $99.9999\%$ of the
   limit. So no uniformity in $\lambda$ over a growing region is at stake either.
3. **The content is that $\phi_\lambda$ does not degenerate.** Seen from the mean-value side the
   same thing: the weight $|P_{\phi_\lambda}|^2$ moves with $\lambda$ and $\zeta$ does not, so it
   is the weight's convergence that decides it. The paper's `:1234` names the difficulty <!-- mg-6467: that gloss is removed; the paper now says this in its own §7.7, `:1950`. -->
   correctly — "$P_\phi$ depends on $\lambda$ and the bound must be uniform" — and then attaches
   it to $\zeta$.
4. **And the corollary never needed "bounded below".** It consumes $\mu^{-1}\log\|g\|^2\to0$;
   any $\|g\|^2\ge e^{-o(\mu)}$ gives the same $-4\pi$.

**The input is published, and the regime that has blocked this chain three times is the one it
covers.** T. M. Dunster, *Asymptotics of prolate spheroidal wave functions*, J. Classical
Analysis 11 (2017), no. 1, 1–21, doi:10.7153/jca-11-01, arXiv:1601.00699, eq. **(124)** with eq. **(107)**: for fixed $m,n$ and
$\gamma\to\infty$, $\mathrm{Ps}_n^m$ is a parabolic cylinder function up to a relative
$O(\gamma^{-1}\log\gamma)$, uniformly on $0\le x\le1-\delta_0$, with explicit error bounds. His
separation constant is $\lambda_{\text{D}}=\chi-c^2$, so **his standing hypothesis
$\lambda_{\text{D}}<0$ is exactly our $\chi_n<c^2$** — the hypothesis §6 above found
Osipov–Rokhlin's theorems *negating*, and the one Lemma 5.1 and Q1 are built on. Dunster states
on his second page that his earlier paper assumed the opposite sign. Via DLMF 12.7.2,
$U(-n-\tfrac12,z)=e^{-z^2/4}\mathit{He}_n(z)$, (124) at $x=X/\lambda$ **is** the Hermite limit
$\lambda^{-1/2}\Phi_n(X/\lambda)\to h_n(X)$.

**What is proved here rather than imported:** the window identity; the localisation; that
$\mathcal E$ is continuous on a fixed window against $\|f\|_2^{1/2}$; the tightness bound
$c^2\int y^2\Phi^2\le\chi$ straight from the prolate equation, which is what stops mass escaping
to infinity; and that $\mathcal E\phi_\infty$ is analytic and non-zero. Only the Hermite limit
itself is imported.

**Nothing above changes.** `prolate-rate.md` §11 item **P2** and §6(d) are annotated in place,
and P2's "why it is open" column was right about the difficulty and wrong about the object.

**Unchanged:** Q5, still observed only in its constant — §A bounds $\Phi_n(1)^2$ from above by
$O(c^{5/2}(1-\Lambda_n))$, $\mu^{3/2}$ away from the truth, and Dunster's §§3–4 (the Bessel
approximations, valid at the band edge) is now the obvious place to look, and was not pursued;
§§1–4; every sign-blindness verdict in §8; the reading (`prolate-rate.md` §0) that
$\epsilon(\lambda)=\min(s^+,s^-)$ is what $QW_\lambda(g,g)/\|g\|^2$ bounds. **This is the fourth
inherited misdiagnosis on this chain** (mg-6851 on §5, mg-9d43 on §§4/6, mg-731c on §3, this on
§9's Q4 row), and the pattern is now four for four: the note was right that something was
missing and wrong about what it was.
