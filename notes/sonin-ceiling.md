# The ceiling is a theorem — and two of the numbers under it were the even block only

Work item mg-0b7a. Companion script:
[`verify_sonin_ceiling.py`](verify_sonin_ceiling.py) (needs `numpy>=2.0`; 10m18s,
`--quick` 1m02s, which is what CI runs). Continues
[`sonin-margin.md`](sonin-margin.md) (mg-d03b), whose Bottom-line item 7 this note
**proves**, and whose §4 table it **corrects**.

mg-d03b closed on a one-line argument it called *"the one thing that could have been
said without computing anything"*:

> $\epsilon>0$, so $\hat\epsilon(0)=2\int_0^\infty\epsilon(e^y)\,dy=+5.3722>0$, so the
> symbol of $-E$ is **negative at low frequency**. Only a support too short to let
> $\hat g$ into that band can save the inequality.

That is right, and this note makes it a theorem. Doing so required looking at
$\epsilon$'s two unanchored constants, and looking at them turned up that the basis
every script in this corpus uses spans **half** the space Theorem 1 is stated on.

---

## Bottom line

**1. $\epsilon(\rho)\sqrt\rho\to1$ is derivable, and the constant is a reproducing
kernel.** mg-d03b measured it to $0.5\%$ at $\rho=60$, marked it *ours, unanchored*,
and recorded that a derivation attempt returned $37.5$ and was abandoned (§7 there).
Substituting $u=\rho x$ in Connes–Consani's series and using
$\int_1^\infty\mathcal F\xi_n=\tfrac12(1-\lambda(n)^2)\xi_n(0)$ gives
$$\epsilon(\rho)\sqrt\rho\ \longrightarrow\ \tfrac12\sum_n\lambda(n)\,\xi_n(0)^2\ =\ 1,$$
because $\sum_m\lambda_m\psi_m(x)\psi_m(y)=e^{2\pi ixy}$ is the spectral expansion of
the finite-Fourier kernel on $[-1,1]$ — at $x=y=0$ it reads $\sum_m\lambda_m\psi_m(0)^2=1$
— and Connes–Consani normalise $\int_{-1}^1\xi_n^2=2$, not $1$. **The factor of two is
the constant.** Measured: $\sum_n\lambda(n)\xi_n(0)^2=2$ to $1.4\times10^{-14}$. §1.

**2. $\hat\epsilon(0)$ has a closed form, and it does not go through $\epsilon>0$.**
Mellin inversion at the self-dual point $s=\tfrac12$, where the gamma factor
$2\Gamma(s)\cos(\pi s/2)(2\pi)^{-s}$ is exactly $1$, collapses the double integral to
$$\boxed{\ \hat\epsilon(0)\ =\ 2\sum_{n\ge0}\frac{\lambda(n)}{1+\lambda(n)}\,A_n^2,
\qquad A_n=\int_0^1\frac{\xi_n(x)}{\sqrt x}\,dx\ }$$
$=5.37218344$, against $5.37217300$ from mg-d03b's quadrature ($5.37218520$ when that
quadrature is tightened) — two routes sharing only the prolate apparatus. The series is stable by $n=6$. This matters: mg-d03b's argument
rests on $\epsilon>0$ **pointwise**, which this corpus has never proved (Theorem
`devil` proves the *functional* $\operatorname{tr}(\vartheta(f)\mathbf S)$ is positive,
i.e. $W_\infty+E\ge0$ — not $\epsilon\ge0$), and on convergence of
$\int_0^\infty\epsilon(e^y)dy$, which rested on item 1. The closed form needs neither,
and it proves absolute convergence on the way. §2.

**3. The ceiling is a theorem, and its test function is explicit.** §3:

> **Theorem A.** Let $K(y)=\epsilon(e^{|y|})\in L^1(\mathbb R)$ with $\hat K(0)>0$. Let
> $z_1,\dots,z_k$ be any $k$ points of $\mathbb C$ and $\psi\in C_c^\infty(-\tfrac12,\tfrac12)$
> any non-zero bump. Then there is a finite $L_k$ such that for every $L>L_k$ there is
> $g$ supported in $[-L/2,L/2]$ with $\hat g(z_j)=0$ for all $j$ and $E(g)>0$.

The proof is four lines: put $\hat g_L(t)=P(t)\,L\hat\psi(Lt)$ with
$P=\prod_j(t-z_j)$ — admissible by construction, still supported in $[-L/2,L/2]$
because $P$ is a polynomial — and let $L\to\infty$ under the dominating function
$|\hat\epsilon|\le\lVert K\rVert_1$. **The only inputs are $\hat\epsilon(0)>0$ and
integrability**, which are items 1 and 2. Nothing about $\epsilon$'s sign, nothing
about prolates, no numerics.

**4. And it has a rate, which is a Szegő density.** §4. Restricting a form to a
subspace of codimension $k$ destroys at most $k$ negative eigenvalues, so with
$n_-(L)$ the negative inertia of $-E$ on $L^2[-L/2,L/2]$,
$$n_-(L)>k\ \Longrightarrow\ -E \text{ is indefinite on \emph{every} codimension-}k\text{ subspace},$$
hence $\log\mu_c(k)\le\Lambda(k):=\inf\{L:n_-(L)>k\}$, and $\Lambda(k)/k\to\pi/t_0$
because the eigenvalue density of a truncated convolution form is
$|\{t:\hat\epsilon(t)>0\}|/2\pi=t_0/\pi$. Measured $\Lambda(k)$ against $\pi k/t_0$ for
$k=1,\dots,7$: ratios $1.149,\,1.058,\,1.054,\,1.033,\,1.034,\,1.024,\,1.026$, coming
down onto $1$ from above, which is the sign of the $+O(\log)$ Landau–Widom correction.

**5. So the constant is not $25\%$ out. It is an upper bound, and the measurement is
below it.** mg-d03b compared its measured slope $0.7523$ of $\log\mu_c$ in $k$ against
$2\pi/t_0=0.9986$ and called the constant $25\%$ out. On the even block — which is what
it computed — item 4 reads $\log\mu_c(k)\le\Lambda_{\rm even}(k)$ with
$\Lambda_{\rm even}(k)/k\to2\pi/t_0$, and every one of mg-d03b's four rows satisfies it:
$1.0166\le1.0561$, $1.8203\le2.0637$, $2.5658\le3.0679$, $3.2757\le4.0700$.
**$0.7523<0.9986$ is the slack in an inequality, not an error in a prediction.** What
the slack measures is that the conditions $\hat g(ij/2)=0$ are *inefficient*: they are
not aligned with the negative eigenvectors, so the codimension-$k$ subspace already
contains a negative direction before $n_-$ has climbed past $k$. §4.

**6. The cosine basis is the even block, and the odd block breaks first.** $E$ is a
convolution form, so $E(g)=E(g_{\rm ev})+E(g_{\rm odd})$ — the cross term is odd in $t$
against an even $\hat\epsilon$. Every script in this corpus works in
$\xi_n=\cos(2\pi ny/L)$, which spans the even block **alone**. Theorem 1 is stated for
$g\in C_c^\infty(\mathbb R_+^*)$ with no parity condition, so the odd block is
admissible and is missing. Adding it (§5):

| codim $k$ | $\mu_c(k)$, mg-d03b (even only) | $\mu_c(k)$, even $+$ odd |
|---|---|---|
| $1$ — $\hat g(0)=0$ | $2.7634$ | $\mathbf{1.7708}$ |
| $2$ — **Theorem 1's** | $6.1739$ | $\mathbf{2.7543}$ |
| $3$ | $13.011$ | $4.1400$ |
| $4$ | $26.461$ | $6.0237$ |

$N=120$; each falls by $\le0.6\%$ from its $N=60$ counterpart, as mg-d03b's did.

**7. Two of mg-d03b's headline statements do not survive that, and both are
sign-sensitive.** §5.3.
 - *"Theorem 1's conclusion holds to $\mu=6.17$, three times its stated hypothesis
   $\mu\le2$."* It holds to $\mu=2.754$ — **a factor $1.38$, not $3.09$.** The
   hypothesis is much closer to sharp than mg-d03b says. It is still not sharp, and
   still not vacuous.
 - *"$\hat g(0)=0$ alone gives $-E\ge0$ up to $\mu=2.763$, so at $\mu\le2$ the second
   condition $\hat g(i/2)=0$ buys nothing."* **False.** $\mu_c(1)=1.771<2$: an odd $g$
   satisfies $\hat g(0)=0$ for free, so one condition is no condition at all on half
   the space. The second condition is doing real work inside Theorem 1's own range —
   which is [`sonin-trace.md`](sonin-trace.md) §6's reading, that mg-d03b half-retired.

**8. What is still not available is the same half as before.** Nothing here proves
$-E\ge0$ *below* $\mu_c$. Theorem A is one-sided by construction; item 4's inequality
runs one way; truncation raises eigenvalues, so a negative truncated eigenvalue
certifies one for the full form and not the converse. **Every $\mu_c$ in this corpus,
mg-d03b's and this note's, is an upper bound on a threshold whose lower half is
unproved.** §6.

---

## 0. What is inherited, and what is re-verified

From [`sonin-trace.md`](sonin-trace.md) (mg-5210) and
[`sonin-margin.md`](sonin-margin.md) (mg-d03b), and **re-verified rather than assumed**
by importing their code unchanged:

- Theorem `devil` (`weil-compo.tex:1132`) and therefore that Theorem 1 is exactly
  "$-E\ge0$ on $\{\hat g(0)=\hat g(i/2)=0\}$ for $\mu\le2$". **Kept.**
- $\epsilon$ (`weil-compo.tex:1373`), the $c=2\pi$ prolate apparatus and its five
  printed anchors. **Kept**; this script imports `ProlateExact`, `EpsTable`, `Symbol`,
  `E_matrix`, `cond_row` and `bisect` from mg-d03b's script rather than rebuilding them,
  so every column here reads against that note's.
- $t_0=6.29177$, the zero of $\hat\epsilon$; $\hat\epsilon(0)=5.3722$;
  $\hat\epsilon(t)\sim-2\epsilon'(1^+)/t^2$. **Kept**, and $\hat\epsilon(0)$ is now
  anchored a second way (§2).
- "$8.7\times10^{-5}$ is the truncation order"; the minimiser is the top cosine mode;
  the `conditions()` endpoint defect. **Kept**, untouched, all sign-blind.
- The $\mu_c(k)$ table and Bottom-line items 5 and 6 of mg-d03b. **Corrected** — §5.

Vocabulary as in [`semilocal-gap.md`](semilocal-gap.md) §0.

**Notation.** $L=\log\mu$; $g$ is supported in $[-L/2,L/2]$ in the additive coordinate
$u=\log\rho$; $K(y):=\epsilon(e^{|y|})$;
$$E(g)=\iint g(u)g(v)K(u-v)\,du\,dv=\frac1{2\pi}\int_{\mathbb R}|\hat g(t)|^2\hat\epsilon(t)\,dt,
\qquad \hat g(t)=\int g(u)e^{-itu}du .$$
Theorem 1's conditions are $\hat g(ij/2)=0$, i.e. $\int g(u)e^{ju/2}du=0$, for
$j=0,\dots,k-1$; $k=2$ is Theorem 1's.

---

## 1. $\epsilon(\rho)\sqrt\rho\to1$, derived

mg-d03b §7 lists this as *computed here and NOT independently anchored*, with the note
that an attempt to derive the constant from the large-$\omega$ expansion of
$\mathcal F\xi_n$ gave $37.5$ and was abandoned. The derivation does not go through the
large-$\omega$ expansion.

Write $c_n=\lambda(n)/(1-\lambda(n)^2)$. On $[-1,1]$ the analytic continuation
$\xi_n^{\rm an}$ *is* $\xi_n$, and past $1$ it is $\mathcal F\xi_n/\lambda(n)$, so
`weil-compo.tex:1373` reads
$$\epsilon(\rho)=\sqrt\rho\sum_n c_n\int_{1/\rho}^1\xi_n(x)\,\mathcal F\xi_n(\rho x)\,dx
\quad\overset{u=\rho x}{=}\quad \frac1{\sqrt\rho}\sum_n c_n\int_1^\rho
\xi_n(u/\rho)\,\mathcal F\xi_n(u)\,du .$$
As $\rho\to\infty$, $\xi_n(u/\rho)\to\xi_n(0)$; the error is $O(1/\rho)$ because
$|\xi_n(u/\rho)-\xi_n(0)|=O((u/\rho)^2)$ and $\mathcal F\xi_n(u)$ is
$O(1/u)$ **with oscillation** — one integration by parts against
$\mathcal F\xi_n(u)=u^{-1}(a_n\cos2\pi u+b_n\sin2\pi u)+O(u^{-2})$ turns the naive
$O(1)$ into $O(1/\rho)$. And
$$\int_1^\infty\mathcal F\xi_n=\tfrac12\Big(\underbrace{\int_{\mathbb R}\mathcal F\xi_n}_{=\ \xi_n(0)}
-\underbrace{\int_{-1}^1\mathcal F\xi_n}_{=\ \lambda(n)\int_{-1}^1\xi_n\ =\ \lambda(n)^2\xi_n(0)}\Big)
=\tfrac12(1-\lambda(n)^2)\,\xi_n(0),$$
the two evaluations being Fourier inversion at $0$ and the finite-Fourier eigenrelation
(`weil-compo.tex:966`) at $\omega=0$. The coefficient collapses:
$$\epsilon(\rho)\sqrt\rho\ \longrightarrow\ \sum_n c_n\,\xi_n(0)\cdot\tfrac12(1-\lambda(n)^2)\xi_n(0)
=\tfrac12\sum_n\lambda(n)\,\xi_n(0)^2 .$$

**And that sum is $2$, not $1$, and the reason is the normalisation.** The finite
Fourier operator $F\eta(\omega)=\int_{-1}^1\eta(x)e^{2\pi ix\omega}dx$ is normal with
real eigenfunctions, so its kernel has the spectral expansion
$e^{2\pi ixy}=\sum_m\lambda_m\psi_m(x)\psi_m(y)$ over an $L^2[-1,1]$-**orthonormal**
prolate basis; at $x=y=0$, and since the odd $\psi_m$ vanish there,
$$\sum_{m\ \rm even}\lambda_m\psi_m(0)^2=1 .$$
Connes–Consani's $\xi_n$ are normalised in *their* inner product
$\langle\eta\mid\xi\rangle=\int_0^\infty$, i.e. $\int_0^1\xi_n^2=1$ and so
$\int_{-1}^1\xi_n^2=2$ (`verify_sonin_trace.Prolate`'s own docstring says so). Hence
$\xi_n=\sqrt2\,\psi_{2n}$ and $\sum_n\lambda(n)\xi_n(0)^2=2$.

$$\boxed{\ \lim_{\rho\to\infty}\epsilon(\rho)\sqrt\rho=\tfrac12\sum_n\lambda(n)\xi_n(0)^2=1\ }$$

CHECK 1 measures $\int_{-1}^1\xi_n^2=2$ to $10^{-15}$, $\sum_n\lambda(n)\xi_n(0)^2=2$ to
$1.4\times10^{-14}$, and the approach $\big(1-\epsilon(\rho)\sqrt\rho\big)\rho\to0.33$,
which is the $O(1/\rho)$ the argument predicts. **Sign-blind.**

**Level of rigour.** Two interchanges are stated and not carried out in $\varepsilon$–$\delta$
here: $\lim$ inside $\int_1^\rho$ (the oscillation estimate above) and $\lim$ inside
$\sum_n$ ($|\lambda(n)|$ is $10^{-19}$ by $n=9$, so the tail is dominated by any
polynomial bound on $\xi_n(0)$). Neither is delicate. §2's route to the one thing this
asymptotic was used for — convergence — avoids both.

---

## 2. $\hat\epsilon(0)$ in closed form

### 2.1 The identity

$\hat\epsilon(0)=2\int_1^\infty\epsilon(\rho)\,d^*\rho$. Substituting $u=\rho x$ and
exchanging the order of integration — the region is $\{x\in(0,1),\ \rho>1/x\}$ —
$$\hat\epsilon(0)=2\sum_n c_n\,A_n B_n,\qquad
A_n=\int_0^1\frac{\xi_n(x)}{\sqrt x}dx,\qquad
B_n=\int_1^\infty\frac{\mathcal F\xi_n(u)}{\sqrt u}du .$$
Now the classical Mellin pair for even functions,
$$\int_0^\infty u^{s-1}\,\mathcal Ff(u)\,du=2\Gamma(s)\cos(\tfrac{\pi s}2)(2\pi)^{-s}
\int_0^\infty x^{-s}f(x)\,dx,$$
has gamma factor $2\sqrt\pi\cdot\tfrac{\sqrt2}2\cdot(2\pi)^{-1/2}=1$ **exactly at
$s=\tfrac12$**, the self-dual point. So
$\int_0^\infty u^{-1/2}\mathcal F\xi_n(u)du=A_n$; and on $[0,1]$,
$\mathcal F\xi_n=\lambda(n)\xi_n$, so $\int_0^1u^{-1/2}\mathcal F\xi_n=\lambda(n)A_n$ and
$$B_n=(1-\lambda(n))\,A_n,\qquad
c_nA_nB_n=\frac{\lambda(n)(1-\lambda(n))}{1-\lambda(n)^2}A_n^2=\frac{\lambda(n)}{1+\lambda(n)}A_n^2 .$$

$$\boxed{\ \hat\epsilon(0)=2\sum_{n\ge0}\frac{\lambda(n)}{1+\lambda(n)}\,A_n^2\ }$$

**Convergence is part of the identity, not an input to it.** Fubini needs only
$\int_0^1|\xi_n|x^{-1/2}dx<\infty$ (a polynomial against $x^{-1/2}$) and
$\int_1^\infty|\mathcal F\xi_n(u)|u^{-1/2}du<\infty$, which follows from
$|\mathcal F\xi_n(u)|\le C_n/u$ — one integration by parts, $C_n$ explicit in
$\xi_n(1)$ and $\lVert\xi_n'\rVert_{L^1}$ — giving an absolutely convergent
$\int u^{-3/2}$. So **the integral defining $\hat\epsilon(0)$ converges absolutely, and
neither §1's asymptotic nor $\epsilon\ge0$ is needed to say so.**

### 2.2 It agrees with the quadrature, and it is not termwise positive

CHECK 2, with $A_n$ by $x=v^2$ on a 960-node composite Gauss rule:

| $n$ | $\lambda(n)$ | $A_n$ | term | partial sum |
|---|---|---|---|---|
| 0 | $+0.9999714$ | $2.262065$ | $+5.116864$ | $5.116864$ |
| 1 | $-0.9794847$ | $0.0115418$ | $-0.0127201$ | $5.104144$ |
| 2 | $+0.5240859$ | $0.6478033$ | $+0.2886086$ | $5.392753$ |
| 3 | $-0.0589766$ | $0.4144565$ | $-0.0215311$ | $5.371222$ |
| 4 | $+0.0027323$ | $0.4253201$ | $+0.0009858$ | $5.372207$ |
| 5 | $-7.629\cdot10^{-5}$ | $0.3994936$ | $-2.435\cdot10^{-5}$ | $5.3721830$ |
| 6 | $+1.439\cdot10^{-6}$ | $0.3757363$ | $+4.064\cdot10^{-7}$ | $5.3721834$ |

$$\hat\epsilon(0)=5.37218344\quad\text{against}\quad
\begin{cases}5.37217300 & \text{`Symbol`, }Y=4.5,\ 110\text{ panels (the script's default)}\\
5.37218520 & \text{`Symbol`, }Y=6,\ 220\text{ panels}\end{cases}$$
from mg-d03b's quadrature — $1.9\times10^{-6}$ and $3.3\times10^{-7}$ relative, and the
deviation falls as the quadrature is tightened, which is what it should do if the closed
form is the exact value. Two routes sharing only the prolate apparatus: one is a
transform of $\epsilon$ on a $y$-grid, the other a Mellin identity and six inner
products.

Two things to read off the table. The tail from $n=6$ is $4.1\times10^{-7}$ against a
value of $5.37$: **the sign of $\hat\epsilon(0)$ is decided by finitely many explicitly
computable terms**, which is the strongest form in which this corpus can hold
"$\hat\epsilon(0)>0$". And the series is *not* termwise positive —
$\lambda(1)/(1+\lambda(1))=-47.8$, and only $A_1=0.0115$ keeps that term from swamping
the sum. Positivity here is a computation, not a sign argument.

### 2.3 What this replaces

mg-d03b's argument was *"$\epsilon>0$, so $\hat\epsilon(0)>0$"*. Two things in that were
not established:

- **$\epsilon>0$ pointwise is not proved in this corpus.** Theorem `devil` says the
  *functional* $f\mapsto\operatorname{tr}(\vartheta(f)\mathbf S)$ is positive, which is
  $W_\infty+E\ge0$ on positive $f$ — a statement about a sum, not about $\epsilon$'s
  sign. $\epsilon>0$ is observed numerically in mg-5210 and mg-d03b and is very likely
  a theorem of Connes–Consani's; it is not one this corpus has.
- **Convergence rested on §1**, which mg-d03b explicitly marked unanchored.

§2.1 needs neither. This is the `statement-defects.md` pattern in a mild form: a
correct conclusion resting on two premises that the instrument pointed at it never
exercised, because the instrument computed the same number either way.

---

## 3. The ceiling

### 3.1 Theorem A

> **Theorem A.** Let $K\in L^1(\mathbb R)$ be even with $\hat K(0)>0$, and let $E$ be the
> associated form. Fix $k\ge0$ and points $z_1,\dots,z_k\in\mathbb C$. Then there is
> $L_k<\infty$ such that for every $L>L_k$ there exists $g\in C_c^\infty$ with
> $\operatorname{supp}g\subseteq[-L/2,L/2]$, $\hat g(z_1)=\dots=\hat g(z_k)=0$, and
> $E(g)>0$ — i.e. $-E$ is indefinite on the codimension-$k$ subspace.

*Proof.* ($E$ is read as the Hermitian form $\frac1{2\pi}\int|\hat g|^2\hat\epsilon$, so
$g$ may be complex; the construction below is real whenever $P$ is a real polynomial in
$t^2$, which is the case for Theorem 1's conditions.) Fix
$\psi\in C_c^\infty(-\tfrac12,\tfrac12)$, $\psi\ne0$, and put
$P(t)=\prod_{j\le k}(t-z_j)$, $\hat g_L(t):=P(t)\,L\,\hat\psi(Lt)$. Since $P$ is a
polynomial, $g_L$ is a finite linear combination of derivatives of $\psi(\cdot/L)$, so
$\operatorname{supp}g_L\subseteq[-L/2,L/2]$ and $g_L\in C_c^\infty$; and
$\hat g_L(z_j)=0$ by construction. Let $r$ be the order of vanishing of $P$ at $0$ and
$P_\ast=\lim_{t\to0}t^{-r}P(t)\ne0$. With $s=Lt$,
$$L^{2r-1}E(g_L)=\frac1{2\pi}\int_{\mathbb R}\Big|L^{r}P(s/L)\Big|^2|\hat\psi(s)|^2\,\hat\epsilon(s/L)\,ds .$$
The integrand converges pointwise to $|P_\ast|^2s^{2r}|\hat\psi(s)|^2\hat\epsilon(0)$;
it is dominated, for $L\ge1$, by $C(1+|s|)^{2k}|\hat\psi(s)|^2\lVert K\rVert_1$, which
is integrable because $\hat\psi$ is Schwartz. Dominated convergence gives
$$L^{2r-1}E(g_L)\ \longrightarrow\ \hat\epsilon(0)\,|P_\ast|^2\cdot\frac1{2\pi}\int s^{2r}|\hat\psi(s)|^2ds\ >\ 0. \qquad\square$$

Three remarks.

- **The inputs are exactly $\hat\epsilon(0)>0$ and $K\in L^1$** — §2 and §2.1. Nothing
  about $\epsilon$'s pointwise sign, nothing about prolates, nothing numerical.
- **It applies verbatim to Theorem 1's conditions**, which are $\hat g(ij/2)=0$: point
  evaluations of $\hat g$. For an even $g$ take $\psi$ even and
  $P(t)=\prod_{j<k}(t^2+j^2/4)$; then $r=2$ and the limit of $L^3E(g_L)$ is
  $\hat\epsilon(0)\big(\prod_{j=1}^{k-1}j^2/4\big)^2\lVert\psi''\rVert^2$.
- **It says nothing about where.** $L_k$ is not effective in any useful sense from this
  proof, and CHECK 3 shows how bad it is in practice: the standard bump gives
  $E(g_L)>0$ from $\mu\approx4.3$ at $k=1$ (true $\mu_c=1.77$) and from
  $\mu\approx8\times10^5$ at $k=4$ (true $6.02$). A bump is a bad prolate. What the
  theorem buys is a proof where there was an eigenvalue.

CHECK 3 exhibits the limit: at $L=160$, $L^3E(g_L)$ is within $20\%$ of the predicted
constant at every $k=1,\dots,4$, approaching from below at $k=1$ and above at $k\ge2$.

### 3.2 Codimension $0$ is a one-liner, and it makes $\mu_c$ well defined

$-E$ is indefinite on the *whole* space at every $L>0$, and this needs neither $\epsilon>0$
nor $\hat\epsilon$: $\epsilon(1)=0$ and $\epsilon'(1^+)=22.9965>0$ (`weil-compo.tex:1367`,
a printed constant), so $K>0$ on some $(0,y_0)$, so for $L<y_0$
$$E(\mathbf 1_{[-L/2,L/2]})=\int_{-L}^{L}(L-|y|)K(y)\,dy>0 .$$
And the infimum of $E$'s Rayleigh quotient over any of these admissible sets is
**monotone non-increasing in $L$** — a test function admissible at $L_1$ is admissible
at every $L_2>L_1$ by extension by zero, and $E$, $\lVert g\rVert^2$ and every condition
$\int ge^{ju/2}$ are all independent of $L$. So indefiniteness at small $L$ propagates
to all $L$, reproducing mg-d03b's "indefinite at every $\mu$ computed" row as a
theorem.

That monotonicity is also what makes $\mu_c(k)$ *a threshold* — the set of $\mu$ where
positivity holds is an interval $(0,\mu_c]$ or $(0,\mu_c)$ — and therefore what makes
bisecting for it legitimate. mg-d03b bisects and does not say this; it is a one-line
lemma and it is load-bearing.

---

## 4. The rate, and what the $25\%$ was

### 4.1 The inequality

Let $n_-(L)$ be the number of negative eigenvalues of $-E$ on $L^2[-L/2,L/2]$. By
min–max, restricting a quadratic form to a subspace of codimension $k$ removes at most
$k$ negative eigenvalues, so $-E$ restricted to **any** codimension-$k$ subspace has at
least $n_-(L)-k$ negative eigenvalues. Hence, for the conditions $\hat g(ij/2)=0$ and
for any others,
$$\log\mu_c(k)\ \le\ \Lambda(k):=\inf\{L:n_-(L)>k\}.$$

$\Lambda(k)$ is finite and grows linearly: the eigenvalue distribution of a truncated
convolution form on an interval of length $L$ is governed by its symbol (Kac–Murdock–Szegő;
Landau's theorem for the sinc kernel is the same statement for the concentration
operator), so
$$\frac{n_-(L)}{L}\ \longrightarrow\ \frac1{2\pi}\big|\{t:\hat\epsilon(t)>0\}\big|=\frac{2t_0}{2\pi}=\frac{t_0}{\pi},
\qquad \frac{\Lambda(k)}{k}\ \longrightarrow\ \frac{\pi}{t_0}=0.49932 .$$
On the **even block** — half the degrees of freedom — the density halves and
$\Lambda_{\rm even}(k)/k\to2\pi/t_0=0.99863$, **which is mg-d03b's constant.**

A proof of the lower bound $n_-(L)\gtrsim t_0L/\pi$ that does not invoke Szegő is the
prolate one, and it is worth recording because it is the quantitative form of Theorem A.
Fix $\delta<t_0$, let $c=\inf_{|t|\le\delta}\hat\epsilon>0$, and let $\mathcal S$ be the
span of the eigenfunctions of the time-band-limiting operator $P_{[-L/2,L/2]}B_\delta
P_{[-L/2,L/2]}$ with eigenvalue $>1-\eta$. For $g\in\mathcal S$ the in-band energy is
$\ge(1-\eta)\lVert g\rVert^2$, so
$E(g)\ge\big(c(1-\eta)-\lVert\hat\epsilon\rVert_\infty\eta\big)\lVert g\rVert^2>0$ as
soon as $\eta<c/(c+\lVert\hat\epsilon\rVert_\infty)$ — and $E>0$ on **all** of
$\mathcal S$, so $n_-(L)\ge\dim\mathcal S$, which is $\delta L/\pi+O(\log L)$ by
Landau–Widom. Letting $\delta\uparrow t_0$ gives the constant.

### 4.2 Measured

CHECK 4, $N=60$, bisecting the $k$-th eigenvalue in $L$:

| $k$ | $\Lambda(k)$ | $\pi k/t_0$ | ratio | $\Lambda_{\rm even}(k)$ | $2\pi k/t_0$ | ratio |
|---|---|---|---|---|---|---|
| 1 | $0.57379$ | $0.49932$ | $1.1491$ | $1.05613$ | $0.99863$ | $1.0576$ |
| 2 | $1.05613$ | $0.99863$ | $1.0576$ | $2.06373$ | $1.99727$ | $1.0333$ |
| 3 | $1.57808$ | $1.49795$ | $1.0535$ | $3.06787$ | $2.99590$ | $1.0240$ |
| 4 | $2.06373$ | $1.99727$ | $1.0333$ | $4.06999$ | $3.99454$ | $1.0189$ |
| 5 | $2.58131$ | $2.49659$ | $1.0339$ | — | — | — |
| 6 | $3.06787$ | $2.99590$ | $1.0240$ | — | — | — |
| 7 | $3.58732$ | $3.49522$ | $1.0263$ | — | — | — |

The even column stops at $k=4$ because $\Lambda_{\rm even}(5)\approx5.1$ is past the
$\mu\le60$ ceiling this script's $\epsilon$ table is built to; the script prints a dash
rather than the bracket end, which is the failure mode a bisection has when its answer is
outside its bracket.

Both ratios come down onto $1$ **from above**, which is the sign of the $+O(\log)$
correction. And $\Lambda_{\rm even}(k)=\Lambda(2k)$ to six figures at $k=1,2,3$
($1.05613$, $2.06373$, $3.06787$). Since the full spectrum is the union of the two
blocks', that is the statement that the two blocks' thresholds strictly **interlace**,
$\Lambda_{\rm ev}(0)<\Lambda_{\rm odd}(0)<\Lambda_{\rm ev}(1)<\Lambda_{\rm odd}(1)<\cdots$
— §5's decomposition, read off the spectrum rather than the kernel.

### 4.3 So the constant was never $25\%$ out

mg-d03b §5 reports measured slope $0.7523$ against $2\pi/t_0=0.9986$ and says *"the
shape is right and the constant is $25\%$ out"*, offering the $2\pi/t_0$ as a count of
resolution cells and not a derivation. It is a derivation — of an **upper bound** — and
every row of that note satisfies it:

| $k$ | $\log\mu_c(k)$, mg-d03b | $\Lambda_{\rm even}(k)$ | slack |
|---|---|---|---|
| 1 | $1.01646$ | $1.05613$ | $0.03967$ |
| 2 | $1.82033$ | $2.06373$ | $0.24340$ |
| 3 | $2.56580$ | $3.06787$ | $0.50208$ |
| 4 | $3.27567$ | $4.06999$ | $0.79432$ |

**$0.7523<0.9986$ is what an upper bound looks like.** The slack is not error, it is
information: it measures how far the conditions $\hat g(ij/2)=0$ are from being aligned
with the negative eigenvectors of $-E$. Aligned conditions would achieve
$\log\mu_c(k)=\Lambda(k)$; these do not, and the misalignment grows with $k$.

Two further things the table makes visible that a single least-squares slope hides.
The increments of mg-d03b's $\log\mu_c$ are $0.804,\,0.746,\,0.710$ — **decreasing** —
so $0.7523$ is not a converged asymptotic slope but an average over a range where the
slope is still falling. And on the full space (§5) the increments are
$0.442,\,0.408,\,0.375$ against $\pi/t_0=0.499$: the same picture, one block down.
**The geometric growth is measured over $k\le4$; only the upper bound on its rate is a
theorem.**

---

## 5. The cosine basis is the even block

### 5.1 The form splits, and half of it is not computed

$E(g)=\int_{\mathbb R}A_g(y)K(y)\,dy$ with $A_g$ the autocorrelation. Split
$g=g_{\rm ev}+g_{\rm odd}$: then $\hat g_{\rm ev}$ is even and $\hat g_{\rm odd}$ is
odd, so $|\hat g|^2=|\hat g_{\rm ev}|^2+|\hat g_{\rm odd}|^2+2\Re(\hat g_{\rm ev}\overline{\hat g_{\rm odd}})$
with the cross term odd in $t$; against an even $\hat\epsilon$ it integrates to zero.
So
$$E(g)=E(g_{\rm ev})+E(g_{\rm odd}),\qquad \lVert g\rVert^2=\lVert g_{\rm ev}\rVert^2+\lVert g_{\rm odd}\rVert^2 :$$
**$-E$ is block diagonal, and its spectrum is the union of the two blocks'.**

The basis this corpus uses — `verify_arch_positivity._h`, and every script that imports
it — is $\xi_0=L^{-1/2}$, $\xi_n=(-1)^n\sqrt{2/L}\cos(2\pi ny/L)$. That is a basis for
the **even block alone**. Theorem 1 is stated for $g\in C_c^\infty(\mathbb R_+^*)$ on a
symmetric interval $[2^{-1/2},2^{1/2}]$ with no parity condition, so odd $g$ are
admissible and have never been computed.

The conditions couple the blocks: $\hat g(0)=\int g$ depends only on $g_{\rm ev}$, and
$\hat g(i/2)=\int g_{\rm ev}\cosh(u/2)+\int g_{\rm odd}\sinh(u/2)$ on both. In
particular **an odd $g$ satisfies $\hat g(0)=0$ automatically**, which is where §5.3's
second correction comes from.

### 5.2 The odd machinery, checked three ways

CHECK 5(a). The sine analogue `_h_odd` is `_h` with
$\sin a x\sin b(x-t)=\tfrac12[\cos((a-b)x+bt)-\cos((a+b)x-bt)]$ in place of the cosine
identity; `cond_row_odd` is the corresponding closed form for
$\int\eta_n(y)e^{jy/2}dy$.

| what | against | deviation |
|---|---|---|
| `_h_odd(L,N,t)` | direct quadrature of $\int_{t-L/2}^{L/2}\eta_n(x)\eta_m(x-t)dx$ | $1.1\times10^{-9}$ |
| `_h` (control, same comparison) | ditto for the cosines | $1.1\times10^{-9}$ |
| `cond_row_odd`, $j=1,2$ | direct integration on a $2\times10^5$-point grid | $2.1\times10^{-10}$ |
| $E$ on an explicit mixed $g$ | brute-force $2$D quadrature of $\iint g(u)g(v)K(u-v)$ | $8.9\times10^{-6}$ relative |

The last row is the one that matters: it checks the **decomposition** and the odd
matrix at once, against a computation that knows nothing about parity or bases; its
$8.9\times10^{-6}$ is the accuracy of the $2001^2$ trapezoid against the kernel's kink at
$u=v$, not a disagreement — at $4001^2$ it falls to $2.2\times10^{-6}$.

### 5.3 The corrected table, and the two statements that fall

CHECK 5(b), $-E$ on the full space, count of negative eigenvalues then the most
negative, at $N=60$ (nine of the script's eleven rows). $N=120$ agrees in every
**count** and to $2.4\times10^{-3}$ in every value — see §7 on why that is
$2.4\times10^{-3}$ and not mg-d03b's $10^{-3}$:

| $\mu$ | codim 0 | codim 1 | codim 2 | codim 3 | codim 4 |
|---|---|---|---|---|---|
| $1.5$ | 1, $-0.8012$ | 0 | 0 | 0 | 0 |
| $2$ | 2, $-1.3411$ | **1, $-0.0719$** | 0 | 0 | 0 |
| $2.5$ | 2, $-1.6541$ | 1, $-0.2770$ | 0 | 0 | 0 |
| $3$ | 3, $-1.8667$ | 2, $-0.4380$ | 1, $-0.0339$ | 0 | 0 |
| $4$ | 3, $-2.1520$ | 2, $-0.6585$ | 1, $-0.2116$ | 0 | 0 |
| $6$ | 4, $-2.4818$ | 3, $-0.9178$ | 2, $-0.4473$ | 1, $-0.1660$ | 0 |
| $8$ | 5, $-2.6798$ | 4, $-1.0764$ | 3, $-0.5924$ | 2, $-0.3032$ | 1, $-0.1052$ |
| $20$ | 6, $-3.1807$ | 5, $-1.4983$ | 4, $-0.9701$ | 4, $-0.6676$ | 3, $-0.4584$ |
| $50$ | 8, $-3.5505$ | 7, $-1.8478$ | 6, $-1.2746$ | 5, $-0.9563$ | 5, $-0.7429$ |

Every codim-0 count is exactly mg-d03b's plus the odd block's, and every most-negative
eigenvalue in the codim-0 column is mg-d03b's unchanged — the even block still supplies
the deepest direction. The **counts** are what move, and they move the thresholds.

CHECK 5(c), $\mu_c(k)$ at $N=120$:

$$\mu_c(1)=1.7708,\qquad \mu_c(2)=2.7543,\qquad \mu_c(3)=4.1400,\qquad \mu_c(4)=6.0237$$

against mg-d03b's $2.7634,\ 6.1739,\ 13.011,\ 26.461$. Each falls by $\le0.6\%$ from
$N=60$, as that note's did, and each is an upper bound falling in $N$ for the same
reason.

**Correction 1.** *"Theorem 1's conclusion holds to $\mu=6.17$, three times its stated
hypothesis $\mu\le2$. So $\mu\le2$ is an artefact of the proof."* — mg-d03b Bottom-line
item 4. It holds to $\mu=2.754$: **a factor $1.38$ on the stated $\mu\le2$, not $3.09$;
$1.46$ in $\log\mu$, not $2.63$.** $\mu\le2$ is still not sharp and still not vacuous, but "artefact of the
proof" is a much smaller claim than that note makes. Connes–Consani's hypothesis is
close to the truth.

**Correction 2.** *"$\hat g(0)=0$ alone gives $-E\ge0$ up to $\mu=2.763$ — past the
whole of Theorem 1's support range. At $\mu\le2$ the second condition $\hat g(i/2)=0$
buys **nothing** for the sign of $-E$."* — mg-d03b Bottom-line item 5, and its §4.3.
**False.** $\mu_c(1)=1.771<2$, and the table above shows the codimension-one form
already carrying a negative eigenvalue $-0.0719$ at $\mu=2$ exactly. The mechanism is
the cheapest possible: *an odd $g$ satisfies $\hat g(0)=0$ for free*, so imposing that
one condition constrains nothing at all on half the space. mg-5210 §6's reading — "they
are not decoration, they are the theorem", of **both** conditions — stands, and
mg-d03b's refinement of it does not.

Both corrections are to statements that are **FALSE for $W_\lambda\to-W_\lambda$**.
Not, this time, to the framing this ticket was dispatched under: item 7's ceiling
argument survived contact and is §3. What did not survive is two numbers standing beside
it, and the defect under them is again a **sign-blind object feeding a signed
conclusion** — here a basis, which is about as sign-blind as an object gets. That is
exactly the warning mg-d03b's own §6 ends on, and this note is its second instance.

---

## 6. House rule

| statement | false for $W_\lambda\to-W_\lambda$? |
|---|---|
| §1: $\epsilon(\rho)\sqrt\rho\to\frac12\sum\lambda(n)\xi_n(0)^2=1$ | no — about $\epsilon$ alone. **Sign-blind** |
| §2: $\hat\epsilon(0)=2\sum\frac{\lambda(n)}{1+\lambda(n)}A_n^2=5.3722>0$ | no. Sign-blind |
| §3: **Theorem A** — for every $k$ there is a finite $L$ past which $E$ has a positive direction in $\{\hat g(ij/2)=0\}$ | no. Sign-blind |
| §3.2: $-E$ is indefinite at codimension $0$ at every $\mu>0$; $\mu_c(k)$ is a threshold | no. Sign-blind |
| §4: $\log\mu_c(k)\le\Lambda(k)$, $\Lambda(k)\sim\pi k/t_0$ | no. Sign-blind |
| §5.1: $E$ splits over even $+$ odd $g$; the corpus's basis is the even block | no. Sign-blind |
| §5.3: **Theorem 1's conclusion holds to $\mu=2.754$, a factor $1.38$ on its stated $\mu\le2$ — not the factor $3.09$ mg-d03b prints** | **YES.** The trace is fixed under the substitution and $W_\infty$ is not |
| §5.3: **it is false from $\mu=2.754$ on** | **YES**, same reason |
| §5.3: **at $\mu\le2$ one condition is NOT enough; mg-d03b's item 5 is false** | **YES**, same reason |

**The ceiling itself is sign-blind, and its consequence is not.** "$E$ is inherently
indefinite at low frequency once the support is long enough" says nothing whatever
about $W$; "so Theorem 1's inequality must fail eventually" says everything. The work
item asked for the ceiling theorem to be flagged loudly if it were not sign-blind, and
it is: what is not sign-blind is the sentence that reads it back into the corpus. That
is the shape mg-5210 identified and mg-d03b confirmed — introduce $W_\infty$ as a term
in an identity and the signed statements appear at the last step, on top of entirely
sign-blind machinery.

And the warning that goes with it, now with a second instance. Every non-sign-blind
statement in this note rests on sign-blind machinery, and §5's defect **was** that
machinery: a basis. `_h` is as sign-blind as a function gets, and choosing it as the
whole space rather than half of it moved two signed thresholds by factors of $1.6$ and
$2.2$.

---

## 7. Provenance, and what is unverified

**Re-verified, not inherited.** mg-d03b's `ProlateExact`, `EpsTable`, `Symbol`,
`E_matrix`, `cond_row`, `restrict` and `bisect` are imported unchanged; $t_0$ and
$\hat\epsilon(0)$ are recomputed from them. $\hat\epsilon(0)$ now has two independent
routes (§2.2) where it had one.

**Proved here.** Theorem A (§3.1). The codimension-$0$ statement and the monotonicity
that makes $\mu_c$ a threshold (§3.2). The inequality $\log\mu_c(k)\le\Lambda(k)$ (§4.1).
The even/odd decomposition of $E$ (§5.1). The closed form for $\hat\epsilon(0)$ and the
absolute convergence of its integral (§2.1) — modulo $|\mathcal F\xi_n(u)|\le C_n/u$,
which is one integration by parts, and summability in $n$, which $|\lambda(n)|\le10^{-19}$
at $n=9$ settles in practice and which is not proved here with constants.

**Derived here, with two interchanges stated and not executed.** §1's asymptotic. See
§1's closing paragraph; §2 does not depend on it.

**Cited, not proved.** The Szegő/Landau–Widom density used for
$\Lambda(k)/k\to\pi/t_0$ (§4.1). The prolate route given alongside it is complete except
for the same citation (the Landau–Widom eigenvalue count), and both are standard.

**Computed here, and NOT independently anchored.**

- Every number in §5. They rest on `_h_odd` and `E_matrix_odd`, which are anchored
  against direct quadrature and against a brute-force $2$D evaluation of the kernel
  (§5.2), and on `EpsTable`, anchored by mg-d03b. The **combination** has no external
  check; what it has is that the even half of it reproduces mg-d03b's table cell for
  cell.
- $\mu_c(4)=6.02$ is comfortably inside the $\mu\le60$ ceiling this $\epsilon$ table is
  built to, unlike mg-d03b's $26.46$; $\Lambda_{\rm even}(4)=4.07$ is not far from
  $\log 60=4.09$, which is why CHECK 4 stops the even column at $k=4$.
- The cosine-plus-sine basis is still not $C_c^\infty$ — mg-5210 §8's caveat, unchanged
  and inherited. Theorem A's test function *is* $C_c^\infty$, which is one reason to
  have it.
- **The odd block converges more slowly in $N$ than the even one**, and the script says
  so: $\eta_n=\sin(2\pi ny/L)$ imposes $g(\pm L/2)=0$, which the form does not, so its
  coefficients decay like $1/n$. Between $N=60$ and $N=120$ the *counts* in §5.3's table
  are identical at every row — that is what the inertia argument uses — but the
  eigenvalue *values* agree to $2.4\times10^{-3}$ where mg-d03b's even-only table holds to
  $10^{-3}$. $\mu_c$ is unaffected at the three figures quoted: its drift is $\le0.6\%$,
  the same as mg-d03b's.

**Not attempted.** The semilocal case — out of scope by the work item, and now with a
sharper reason to look: §5's split is a statement about a convolution form, and the
prime terms add $\cos(mt\log p)$ to the symbol without changing that, so the odd block
is missing from the semilocal computation too. Anything Lean. Any paper edit. **A lower
bound on any $\mu_c$** — see item 8 of the Bottom line; that half is where a positivity
proof would live and nothing here touches it.

**Open, and the obvious next measurement.** Whether `verify_arch_positivity.py`'s other
columns — the ones about $W_\infty$ and $\sigma$, not about $E$ — are also even-block
statements, and whether any conclusion in the corpus turns on it. §5.1's argument is
about $E$; $W_\infty$ is a different form and its parity behaviour was not examined
here.
