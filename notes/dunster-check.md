# Dunster (124)+(107) holds in our regime, at every index we use — and one of his hypotheses does not

Work item mg-ff96. Companion script: [`verify_dunster.py`](verify_dunster.py) (needs `mpmath`;
no `numpy`; imports only `prolate_even` from [`verify_prolate_rate.py`](verify_prolate_rate.py),
so the eigenfunctions on the left of Dunster's equation are built by machinery that has never
seen Dunster). Audits the **one imported input** in the H0 chain:
[`h0-lower-bound.md`](h0-lower-bound.md) §5 (mg-6818), the paper's **G13** and its §§1.4, 1.6,
7.7.

Nothing in `start.tex`, `s3.tex` or the paper was edited. `h0-lower-bound.md` is annotated in
place (HTML comments, no line-count change) and appended to.

**Calibration, before anything else.** *A numerical check is not a proof, and this one does not
make Dunster's theorem ours.* G13 stays an external dependency whatever is below; what changes
is that it is now a **tested** one, evaluated against our own eigenfunctions at our own
bandwidths, with the failure modes it can catch — misreading the equation, and applying it
outside its hypotheses — actually looked for rather than assumed absent. It found one of each.

---

## Bottom line

**1. (107) is verified, and more sharply than it is stated.** At $m=0$,
$a=\lambda\gamma^{-1}+\gamma=\chi_n/c$ and the claim $a=2n+1+O(\gamma^{-1})$ holds at every
index $n=0,2,4,6,8$ and every bandwidth $c=4\pi,\ldots,24\pi$. Better: the $O(\gamma^{-1})$
term is pinned — one formula, no free parameter, five indices at once,
$$\chi_n\;=\;(2n+1)c\;-\;\frac{(2n+1)^2+5}{8}\;+\;O(c^{-1}),$$
confirmed to three digits at $n=0$ and to two at $n=8$, with its own residual converging. §4.
This constant is identified here by measurement; Dunster's (27) states only $O(1)$ for it and
defers to [1, p. 186], and it appears nowhere in this corpus. So the
statement `h0-lower-bound.md` Lemma 3.3 consumes — $\chi_n=(2n+1)c+O(1)$ — is not merely
plausible but pinned, **without** opening Dunster's own source for it (Arscott [1, p. 186]).

**2. (124) is verified, at every index we use, across the whole bandwidth range.** Evaluating
both sides independently — left from the Legendre-coefficient eigensolver, right from mpmath's
parabolic cylinder function — the quantity (124) actually bounds,
$$D(c,n)\;:=\;\sup_{0\le x\le1-\delta_0}\frac{\big|\Phi_n(x)/\Phi_n(0)-\mathrm{RHS}(x)\big|}
{\operatorname{env}U\big(-\tfrac12a,\hat\rho\sqrt{2c}\big)\big/\big|U(-\tfrac12a,0)\big|},$$
satisfies $D\cdot c/\log c$ **bounded and decreasing** at $n=0,2$ and bounded at $n=4,6,8$.
At $n=0$ it runs $0.5997\to0.3900$ over $c=4\pi\to24\pi$. §5.

**3. The agreement, as a ratio.** At $x=0.95$, where $U$ is monotone and the ratio is a fair
number, $\Phi_n(x)/\Phi_n(0)$ divided by Dunster's right-hand side is
$$n=0:\;1.0224899024635093,\qquad n=4:\;1.1939723428917374,\qquad n=8:\;1.5647531827624885$$
at $c=24\pi$, each decreasing monotonically in $c$ at the rate §5 tabulates. **The index-0
agreement is 2.2%, the index-8 agreement is 56%, and both are consistent with (124)** — because
(124)'s error is $O(c^{-1}\log c)$ with a constant that grows fast with $n$, and $n=8$ at
$c\le24\pi$ is nowhere near its asymptotic regime. §5.

**4. The finding: the hypothesis holds where H0 needs it, fails at one cell of our grid, and
the numeric check `h0-lower-bound.md` §5 attaches to it is wrong.** His standing assumption is
not $\lambda<0$. It is (29), at `PSWF_JCA.tex:466`–`:471`,
$$0\;\le\;\sigma\;=\;\sqrt{1+\gamma^{-2}\lambda_n^m(\gamma^2)}\;\le\;\sigma_0\;<\;1,$$
i.e. $\sqrt{\chi_n}/c$ **bounded away from 1**, uniformly — and $\pm\sigma$ are also the
turning points, so §5's "pair of almost coalescent turning points near $x=0$" wants $\sigma$
*small*, not merely $<1$. Measured, $\sigma=1.0199$ at $(c,n)=(4\pi,8)$: $\lambda>0$ there,
which is the case Dunster says is [9]'s and **not this paper's**. The exact threshold is
$c^*_8=13.3006991$, i.e. $\mu^*=2.1168720$. §3.

**Be exact about what `h0-lower-bound.md` got wrong, because it is not what it looks like.**
That note *does* find (29): its §5 writes "$\sigma=\sqrt{1+\gamma^{-2}\lambda}=\sqrt{\chi_n}/c
\in[0,\sigma_0]$, $\sigma_0<1$" — attributing it to his summary §6 rather than to (29) at
`:466`, but the content is there. Three things are nevertheless wrong:

- its own §0 and Bottom line 4 print the hypothesis as **"$\lambda<0$"**, which is the weaker
  statement, and that is the form any reader of the summary carries away;
- the numeric check attached to it — "the corpus's measured $\chi_n/c^2$ runs $0.020$ to $0.64$
  (`h1-mean-value.md` §5), so $\sigma\le0.8$ with room" — is **false at index 8**. That range
  was measured at $n\le4$ — and demonstrably so: its two endpoints are exactly the
  $(\mu,n)=(2,4)$ cell, $\sigma^2=0.799166^2=0.6387$, and the $(\mu,n)=(8,0)$ cell,
  $\sigma^2=0.139986^2=0.0196$. Indices 6 and 8 were never in it. The corpus's test vector
  carries index 8, and at $(\mu,n)=(3,8)$ — a row of the note's *own* §7 CHECK 6 table —
  $\sigma=0.883$;
- at $(\mu,n)=(2,8)$, $\sigma>1$ and the hypothesis fails outright.

**The failing cell is not new to this repository**: `verify_q1.py` CHECK 6 prints it and its
comment names it, "index 8 is the one that can fail in the range this project computes"
(mg-6851). What is new is that the same cell fails *Dunster's* hypothesis too, and that §5's
"with room" does not carry it across. §3.

**5. It does not damage H0, and the reason is structural.** (E) enters `h0-lower-bound.md`
Thm 6.1 only in step (i), a **$\lambda\to\infty$ limit at fixed $n$**; the finite-$\mu$ tables
of its §7 are measurements, not applications of (E). Since $\sigma_n(c)\to0$ for fixed $n$, the
hypothesis holds for every $c>c^*_n$ and the limit is taken well inside it. What must change is
the *sentence* in §5, not the theorem. §7.

**6. The corpus's own step from (124) to (E) is verified separately, and it is the cheaper
half.** Splitting the total error into Dunster's part $e_D$ and the three simplifications
`h0-lower-bound.md` §5 makes ($\hat\rho\sqrt{2c}\to2\sqrt\pi X$, prefactor $\to1$,
$a\to2n+1$), $e_D$ decays at the rate (124) claims, $e_C$ like $c^{-1}$, and $c\,e_T$
converges to $0.1536$ ($n=0$) through
$6.794$ ($n=8$). **(E) holds with $O(c^{-1})$, one power of $\log c$ better than claimed** —
which reproduces `h0-lower-bound.md` §7 CHECK 7's conclusion from a different direction. §6.

But note **the two errors partly cancel**: at $n=4$, $c=24\pi$, $e_D=0.1031$ and $e_C=0.0923$
while $e_T=0.0315$. So CHECK 7's good agreement was *not* evidence that (124) itself is
accurate — the intermediate is three times worse than the endpoint. §6.

**7. Two things inside the import were never opened, and one of them is new.** (124)'s
$O(\gamma^{-1}\log\gamma)$ is Dunster's own [10], the double-turning-point theory — flagged as
unopened in `h0-lower-bound.md` §10 H0-1, correctly. **(107)'s $O(\gamma^{-1})$ is a second
external dependency that §5 does not mention**: it comes from (27) at `:455`–`:461`, which
Dunster attributes to [1, p. 186] = Arscott 1964. §4 tests it numerically instead of opening
it, which is the best that is available here. §3(c).

**Which outcome of the ticket is this?** **(1)** and **(4)**: agreement to the claimed rate
across the whole range at every index, *plus* a hypothesis whose numeric check was wrong —
stated in its full strength for the first time, with the one cell of our grid where it fails
and the threshold $\mu^*_n$ that says where. Not **(3)** — nothing disagrees. Not **(2)**
either, though it is close: the range does not degrade, the *index* does, and §5 says where.

---

## 0. Provenance, and the one thing to check before quoting a line number

Read as primary source from `arxiv.org/e-print/1601.00699`, single LaTeX file `PSWF_JCA.tex`,
**1858 lines, md5 `667bb99e219c21468128dcbc222228fb`**. Every `:NNNN` below is a line of that
file. `h0-lower-bound.md` §5 records no hash; its anchors land within two to six lines of the
objects it names, so it is the same file, and the exact anchors are restated in §1.

Equations in the arXiv source are labelled `eq1`…`eq134` sequentially and rendered with
`\numberwithin{equation}{section}` (`:111`). So the printed numbering in the arXiv PDF is
sectional, and "(124)" and "(107)" are the **journal's** numbering, which the labels track.
Anyone re-checking should search `\label{eq124}`, not a printed "(124)".

---

## 1. The two equations, verbatim

> **(107)**, `:1296`–`:1299`:
> ```latex
> \begin{equation}
> a=\lambda\gamma^{-1}+\gamma=2\left(  {n-m+{\tfrac{1}{2}}}\right)
> +{O}\left(  {\gamma^{-1}}\right)  , \label{eq107}%
> \end{equation}
> ```
> followed at `:1300`–`:1301` by: *"the $O(\gamma^{-1})$ term being valid for fixed $m$ and $n$
> and $\gamma\rightarrow\infty$. In particular, $a$ is bounded."*

> **(124)**, `:1426`–`:1439`:
> ```latex
> \begin{equation}%
> \begin{array}
> [c]{l}%
> \operatorname{Ps}_{n}^{m}\left(  {x,\gamma^{2}}\right)  =\dfrac
> {\operatorname{Ps}_{n}^{m}\left(  {0,\gamma^{2}}\right)  }{U\left(
> {-{\frac{1}{2}}a,0}\right)  }\left(  {\dfrac{\rho}{x}}\right)  ^{1/2}\left(
> {1-x^{2}}\right)  ^{-1/4}\\
> \times\left[  {U\left(  {-{\frac{1}{2}}a,\hat{{\rho}}\sqrt{2\gamma}}\right)
> +{O}\left(  {\gamma^{-1}\ln\left(  \gamma\right)  }\right)
> \operatorname{env}U\left(  {-{\frac{1}{2}}a,\hat{{\rho}}\sqrt{2\gamma}%
> }\right)  }\right]  ,
> \end{array}
> \label{eq124}%
> \end{equation}
> ```
> followed at `:1440`: *"as $\gamma\rightarrow\infty$, uniformly for
> $0\leq x\leq1-\delta_{0}$."*

The auxiliary quantities, all needed to evaluate the right-hand side:

| eq. | line | statement |
|---|---|---|
| (1) | `:117`–`:122` | $(1-z^2)y''-2zy'+\big(\lambda-\frac{\mu^2}{1-z^2}+\gamma^2(1-z^2)\big)y=0$ |
| (19) | `:359`–`:364` | $\int_{-1}^1\{\mathrm{Ps}_n^m\}^2dx=\frac{2(n+m)!}{(2n+1)(n-m)!}$ — **Legendre's normalisation, not ours** |
| (29) | `:466`–`:471` | $0\le\sigma=\sqrt{1+\gamma^{-2}\lambda_n^m(\gamma^2)}\le\sigma_0<1$ |
| (108) | `:1305`–`:1309` | $\tfrac12\rho^2=\int_0^x t(1-t^2)^{-1/2}dt=1-\sqrt{1-x^2}$ |
| (111) | `:1320`–`:1323` | $\phi(\rho)=-\dfrac{a\rho}{4-\zeta^2}$ — see the typo note below |
| (116) | `:1357`–`:1360` | $\hat\rho=\rho+\gamma^{-1}\Phi(\rho)$ |
| (117) | `:1362`–`:1366` | $\Phi(\rho)=\dfrac1{2\rho}\displaystyle\int_0^\rho\phi(v)dv=\dfrac{a\ln(1-\tfrac14\rho^2)}{4\rho}$ |
| (120) | `:1387`–`:1393` | $\hat\varepsilon_1=O(\gamma^{-1}\ln\gamma)\operatorname{env}U$, then "uniformly for $0\le x\le1-\delta_0$" at `:1393` |
| — | `:924`–`:926` | *"the envelope function $\operatorname{env}$ is defined for the parabolic cylinder functions by [27, eq. 14.15.23]"* — DLMF 14.15.23, and see the caveat below |

**Two typographical $\zeta$-for-$\rho$ slips, and why they matter.** (111) as printed has
$\phi(\rho)=-a\rho/(4-\zeta^2)$ and (110) at `:1315`–`:1319` has the term $\gamma\zeta\phi(\rho)$,
whereas (118) at `:1368`–`:1372` has $\gamma\rho\phi(\rho)$. $\zeta$ is §4's Liouville variable
and does not occur in §5; both must be read as $\rho$. The reading is **forced** by (117): with
$\phi(v)=-av/(4-v^2)$, $\frac1{2\rho}\int_0^\rho\phi = \frac{a}{4\rho}\ln(1-\tfrac14\rho^2)$,
which is (117) exactly as printed. It is also **tested** — see §5's last table, where dropping
the (116)+(117) correction destroys the convergence. This is the kind of thing a numerical
check is for: the correction is $O(\gamma^{-1})$, the same order as the claimed error, so
reading it wrongly would not have been visible in the theorem's shape.

**One thing here is second-hand, and it is named.** DLMF 14.15.23 was not read in its own
rendering; its content — $\operatorname{env}U(-c,x)=\{U^2+\bar U^2\}^{1/2}$ for $0\le x\le X_c$
and $2U(-c,x)$ beyond, with $X_c$ the largest positive root of $U(-c,x)=\bar U(-c,x)$ — reached
this note through a fetch. Two guards. (a) The two-branch shape is confirmed internally: env
must jump by exactly $\sqrt2$ at $X_c$, and CHECK 0(f) measures the jump as $\sqrt2-1$ to
$5\times10^{-13}$, which would not happen if $X_c$ or the branches were wrong. (b) The
conclusion does not depend on it: replacing env by $2U$ throughout, or by
$\{U^2+\bar U^2\}^{1/2}$ throughout, moves $D$ by at most a factor $\sqrt2$ and does not touch
its decay rate, which is the whole of §5's finding. $\bar U$ itself is *not* second-hand — it is
pinned to Dunster's own (75)/(76) in CHECK 0(e).

**Normalisation.** (19) is not ours ($\int_{-1}^1\Phi_n^2=1$). It drops out: (124) is
normalised at $x=0$, so it is a statement about **shape** and carries no normalisation at all.
`h0-lower-bound.md` §5 says this and is right; `verify_dunster.py` CHECK 3 uses only ratios, so
it never assumes it.

---

## 2. The symbol dictionary, re-derived rather than accepted

Matching (1) at $\mu_{\text{D}}=m=0$ against ours,
$((1-y^2)\Phi')'+(\chi-c^2y^2)\Phi=0$, i.e. $(1-y^2)\Phi''-2y\Phi'+(\chi-c^2y^2)\Phi=0$:
$$\gamma=c,\qquad \lambda_{\text{D}}=\chi-c^2,\qquad \mu_{\text{D}}=m=0 .$$
This agrees with `h0-lower-bound.md` §0 and is **checked, not quoted**: CHECK 1(a) feeds our
$\Phi_n$ into (1) *as printed*, with those substitutions, and measures the residual. At
$c=8\pi$, $y=0.41$, $|{\rm residual}|/(c^2|\Phi|)$ is $10^{-38}$ at every index — round-off at
40 working digits. A wrong dictionary would not do that.

Two further identifications, both checked:

- **Index.** Our $\Phi_n$ is the $(n/2)$-th eigenvector of the even Legendre tridiagonal. That
  this is Dunster's $\mathrm{Ps}_n^0$ is verified from the $\gamma\to0$ limit: at $c=10^{-3}$,
  $\chi_n\to n(n+1)$ to seven digits and $\Phi_n/\bar P_n\to\pm1$ at $n=0,2,4,6,8$. CHECK 0(a).
- **Sign.** `prolate_even` fixes $\Phi_n(0)>0$, so $\Phi_n=-\bar P_n$ at $n\equiv2\pmod4$.
  (124) is a ratio statement normalised at $x=0$ and cannot see the overall sign.

And the hypothesis correspondence, re-derived: $\sigma=\sqrt{1+\gamma^{-2}\lambda_{\text D}}
=\sqrt{1+(\chi-c^2)/c^2}=\sqrt{\chi}/c$, so
$$\lambda_{\text D}<0\iff\chi<c^2\iff\sigma<1 .$$
mg-6818's correspondence is confirmed. §3 is why it is not the whole hypothesis.

---

## 3. The hypothesis audit — *this is the finding*

### 3.1 (29) is stronger than $\lambda<0$, and one cell of our grid violates even $\lambda<0$

$\sigma=\sqrt{\chi_n}/c$, measured (CHECK 1(b)):

| $\mu$ | $c$ | $n=0$ | $n=2$ | $n=4$ | $n=6$ | $n=8$ |
|---|---|---|---|---|---|---|
| $2$ | $12.566$ | $0.27335$ | $0.61022$ | $0.79917$ | $0.92881$ | **$1.01988$** |
| $3$ | $18.850$ | $0.22563$ | $0.50421$ | $0.66695$ | $0.78806$ | $0.88318$ |
| $4$ | $25.133$ | $0.19644$ | $0.43910$ | $0.58321$ | $0.69280$ | $0.78202$ |
| $6$ | $37.699$ | $0.16123$ | $0.36046$ | $0.48052$ | $0.57337$ | $0.65063$ |
| $8$ | $50.265$ | $0.13999$ | $0.31299$ | $0.41795$ | $0.49970$ | $0.56829$ |
| $10$ | $62.832$ | $0.12540$ | $0.28039$ | $0.37478$ | $0.44859$ | $0.51078$ |
| $12$ | $75.398$ | $0.11459$ | $0.25622$ | $0.34270$ | $0.41049$ | $0.46777$ |

The thresholds $c^*_n$ at which $\chi_n(c)=c^2$, by bisection:

| $n$ | $0$ | $2$ | $4$ | $6$ | $8$ |
|---|---|---|---|---|---|
| $c^*_n$ | none | $3.7900074$ | $6.9829708$ | $10.146592$ | $13.300699$ |
| $\mu^*_n=c^*_n/2\pi$ | — | $0.6032$ | $1.1114$ | $1.6149$ | $2.1169$ |

($n=0$ never crosses: $\chi_0(c)=\tfrac13c^2+O(c^4)$, so $\sigma\to1/\sqrt3$ as $c\to0$ and
decreases from there.)

So at index 8 the paper does not apply below $\mu=2.1169$, and $c=4\pi$ ($\mu=2$) is below it.
`verify_q1.py` CHECK 6 already prints this cell as `(FAILS)` for Q1's own hypothesis and its
comment names it; `h0-lower-bound.md` §5 does not carry it across, quoting instead
`h1-mean-value.md` §5's $\chi_n/c^2\le0.64$, which was measured at $n\le4$. **Every entry of
the $\sigma$ table above is a number the corpus could have printed at any time; none of them
had been.**

Note also what (29) asks beyond $\sigma<1$: $\sigma_0$ is a **fixed** constant, so the bound
must be uniform over whatever family of $(c,n)$ one applies the theorem to; and since $\pm\sigma$
are the turning points (`:483`–`:487`) and §5 is built for "a pair of almost coalescent turning
points near $x=0$" (`:1303`–`:1304`), the *quality* of (124) degrades as $\sigma\uparrow1$ even
where it formally applies. §5's $n=6,8$ rows are that degradation, measured.

### 3.2 The other local hypotheses of §5, one at a time

| # | hypothesis | line | ours |
|---|---|---|---|
| (i) | *"With the exception of §5"*, results are uniform for $0\le m\le n\le2\pi^{-1}\gamma(1-\delta)$. §5 **is** the exception — it is the fixed-$m,n$ section, and (107)'s $O(\gamma^{-1})$ is "valid for fixed $m$ and $n$" | `:138`–`:146`, `:1284`, `:1300` | $n\in\{0,2,4,6,8\}$ fixed — **OK** |
| (ii) | (124) is derived under *"$\mathrm{Ps}_n^m$ (and hence $m+n$) is even"*; the odd case is (125) | `:1396`–`:1397` | $m=0$, $n$ even — **OK**, and we never use (125) |
| (iii) | $\lambda\to-\infty$, assumed for the whole paper, from [1, p. 186] | `:136`–`:138` | $\lambda\sim-\gamma^2$ at fixed $n$ — **OK** |
| (iv) | $\mu=m$, $\nu=n$ integers: the eigenvalue case | `:131`–`:135` | **OK** |
| (v) | $\delta_0\in(0,1-\sigma_0)$ arbitrary. This binds $\delta_0$ from **above**, so $0\le x\le1-\delta_0$ may be taken as large as we like; the constant depends on $\delta_0$ | `:783`–`:787` | **OK**, and §5 measures the $\delta_0$-dependence |
| (vi) | The error bounds behind (120) are Dunster's [10] | `:1381`–`:1391` | **still unopened** — as `h0-lower-bound.md` §10 H0-1 says |
| (vii) | (107)'s $O(\gamma^{-1})$ rests on (27), attributed to [1, p. 186] = Arscott 1964 | `:455`–`:461` | **still unopened, and not previously flagged** — §4 tests it instead |

(vii) is the one `h0-lower-bound.md` misses. Its §10 records the unopened [10]; it does not
record that (107) is itself a citation. The chain is therefore two deep, not one:
$$\text{H0}\;\leftarrow\;\text{(E)}\;\leftarrow\;\text{(124)},\text{(107)}\;\leftarrow\;
\text{Dunster [10]},\ \text{Arscott [1, p.186]} .$$

---

## 4. (107), verified — and its constant identified

$a=\chi_n/c$ from our eigensolver against $2n+1$. The middle column is what (107) asserts is
$O(\gamma^{-1})$; the last is the residual against the classical next term, which must go to
zero if $\chi_n=(2n+1)c-\frac{(2n+1)^2+5}8+O(c^{-1})$ (CHECK 2):

| $\mu$ | $c$ | $n$ | $a$ | $c\,(a-2n-1)$ | $+\frac{(2n+1)^2+5}8$ |
|---|---|---|---|---|---|
| $2$ | $12.566$ | $0$ | $0.93898909735908$ | $-0.7666856$ | $-0.0166856$ |
| $12$ | $75.398$ | $0$ | $0.99001927295133$ | $-0.7525291$ | $-0.0025291$ |
| $2$ | $12.566$ | $4$ | $8.0257167413125$ | $-12.243205$ | $-1.4932045$ |
| $12$ | $75.398$ | $4$ | $8.8550425127471$ | $-10.929537$ | $-0.1795371$ |
| $2$ | $12.566$ | $8$ | $13.070999109747$ | $-49.373281$ | $-12.623281$ |
| $12$ | $75.398$ | $8$ | $16.497415774033$ | $-37.893958$ | $-1.1439579$ |

Predicted limits $-\frac{(2n+1)^2+5}8$: $-0.75$, $-3.75$, $-10.75$, $-21.75$, $-36.75$ at
$n=0,2,4,6,8$. The residual column falls like $c^{-1}$ at every index — at $n=0$,
$c\times(\text{residual})$ runs $-0.2097,\ -0.2014,\ -0.1976,\ -0.1940,\ -0.1924,\ -0.1913,
-0.1907$, i.e. converging. **(107) is verified, with its next coefficient, on the whole grid,
including the $(\mu,n)=(2,8)$ cell where (124) does not apply** — (107) needs only fixed $n$
and $\gamma\to\infty$, not (29).

**Why this is not curve-fitting.** One formula with no free parameter fits five indices at
once, and its own residual converges. $c\times(\text{residual})$ across $n=0,2,4,6,8$:
$$\mu=10:\ -0.191,\ -2.919,\ -13.666,\ -39.401,\ -87.762;\qquad
\mu=12:\ -0.191,\ -2.902,\ -13.534,\ -38.879,\ -86.243 .$$
Five independent numbers per row, and the row moves by $2\%$ while $c$ moves by $20\%$. The
$-\frac{(2n+1)^2+5}8$ is **identified here by measurement**, not quoted: it is the shape a
harmonic-oscillator expansion of (106) gives, and Dunster's own (27) at `:455`–`:461` states
only $O(1)$ for it, deferring the constant to [1, p. 186]. It appears nowhere in this corpus.

*This is a verification, not a reproduction: `h0-lower-bound.md` §7 CHECK 6 reports
$\chi_n/((2n+1)c)$ approaching 1, which is (107) to leading order only. The $-\frac{(2n+1)^2+5}8$
does not appear anywhere in the corpus.*

---

## 5. (124), verified — the numbers

Working precision **40 digits**; CHECK 5 repeats the whole computation at 25 and 60 digits and
at Legendre truncations $K=\lfloor c\rfloor+90$ and $+130$: at $(\mu,n,x)=(8,4,0.5)$ all three
of $a$, LHS, RHS agree to **20 printed digits across all six combinations**. The evaluations are
not near-cancelling — the smallest quantity anywhere is $\Phi_8(0.95)/\Phi_8(0)\approx5\times
10^{-15}$ at $c=24\pi$ — so 40 digits is ample and the stability table shows it.

**$D$, the quantity (124) bounds** (defined in Bottom line 2; $\delta_0=0.05$, 200-point grid
quadratic in $x$; CHECK 3):

| $\mu$ | $c$ | | $n=0$ | $n=2$ | $n=4$ | $n=6$ | $n=8$ |
|---|---|---|---|---|---|---|---|
| $2$ | $12.566$ | $D$ | $0.120787$ | $0.353176$ | $0.647749$ | $1.37204$ | $3.32860$ |
| | | $Dc/\log c$ | $0.5997$ | $1.7535$ | $3.2160$ | $6.8121$ | $16.526$ |
| $4$ | $25.133$ | $D$ | $0.0612545$ | $0.195927$ | $0.443478$ | $0.636026$ | $0.941853$ |
| | | $Dc/\log c$ | $0.4775$ | $1.5273$ | $3.4570$ | $4.9579$ | $7.3418$ |
| $8$ | $50.265$ | $D$ | $0.0323248$ | $0.108638$ | $0.268528$ | $0.483136$ | $0.673607$ |
| | | $Dc/\log c$ | $0.4148$ | $1.3940$ | $3.4456$ | $6.1994$ | $8.6435$ |
| $12$ | $75.398$ | $D$ | $0.0223594$ | $0.0767360$ | $0.192847$ | $0.360828$ | $0.561476$ |
| | | $Dc/\log c$ | $0.3900$ | $1.3384$ | $3.3636$ | $6.2936$ | $9.7933$ |

$Dc/\log c$ is bounded at every index. It is monotone decreasing at $n=0,2$; at $n=4$ it peaks
at $3.487$ ($\mu=6$) and falls; at $n=6,8$ it is still rising at $\mu=12$ but decelerating
($n=8$: $8.643,\ 9.451,\ 9.793$ at $\mu=8,10,12$ — increments $0.81$ then $0.34$). **Nothing in
the range is inconsistent with $O(c^{-1}\log c)$, and nothing establishes the $\log$ is needed
either:** $Dc$ at $n=0$ runs $1.518,\ 1.518,\ 1.539,\ 1.586,\ 1.625,\ 1.658,\ 1.686$ — growing
$11\%$ while $c$ grows sixfold and $\log c$ grows $71\%$. Over $c\le24\pi$ the data cannot
separate $c^{-1}$ from $c^{-1}\log c$, and this note does not claim to.

**The ratio, with digits.** $\big(\Phi_n(x)/\Phi_n(0)\big)/\mathrm{RHS}(x)$ at $x=0.9$ and
$x=0.95$ — both beyond the turning point $x=\sigma$ for every cell except $(\mu\le3,n=8)$, so
$U$ is monotone there, has no zeros, and the ratio is a fair number. (A ratio at small $x$ would
be dominated by proximity to a zero of $U$, where (124)'s additive-against-the-envelope error
makes it unbounded by design; those are reported as $D$ instead.)

| $\mu$ | $n=0$, $x{=}0.95$ | $n=4$, $x{=}0.95$ | $n=8$, $x{=}0.95$ |
|---|---|---|---|
| $2$ | $1.1214921977618099$ | $1.4867167441605162$ | $-2.348030877771784$ *(29) fails* |
| $3$ | $1.0809782195916486$ | $1.5133948768479875$ | $-0.82187070799221582$ |
| $4$ | $1.0616120455472951$ | $1.4460663869220404$ | $0.86873021467584767$ |
| $6$ | $1.0423054218695828$ | $1.3376733405902885$ | $1.6264361755566089$ |
| $8$ | $1.032513539335031$ | $1.2700953614132937$ | $1.6775389099737071$ |
| $10$ | $1.0265375668835608$ | $1.2254755222975241$ | $1.6264379995963433$ |
| $12$ | $1.0224899024635093$ | $1.1939723428917374$ | $1.5647531827624885$ |

At $x=0.95$ the envelope is $2U$ and the prefactor is $1.99$, so $|{\rm ratio}-1|\approx D$
there; the two tables are the same statement seen twice, which is the check that the envelope
was computed right (e.g. $n=8$, $\mu=12$: $D=0.5615$ and $|{\rm ratio}-1|=0.5648$).

**Read the $n=8$ column as pre-asymptotic, not as a failure.** At $\mu=2,3$ the ratio is
*negative*: Dunster's error term exceeds his main term at the band edge, so (124) carries no
information there — which is exactly what $D=3.33$ and $D=1.81$ say, and is consistent, not
contradictory. From $\mu=6$ on the sign is right and the ratio falls monotonically. $\sigma$ is
still $0.468$ at $\mu=12$, the turning points are nowhere near $x=0$, and $Dc/\log c$ is
bounded throughout.

**Where the supremum sits, and the $\delta_0$-dependence.** `argmax` is $x=1-\delta_0$ in 29 of
the 35 cells: the worst disagreement is at the **right endpoint**, which is exactly where
Dunster's own split at `:783`–`:787` hands over to the Bessel approximation (61). So the
constant depends on $\delta_0$, and must blow up as $\delta_0\to0$. Measured at $n=4$:

| $\delta_0$ | $\mu=2$ | $\mu=3$ | $\mu=4$ | $\mu=6$ |
|---|---|---|---|---|
| $0.5$ | $0.647685$ | $0.424884$ | $0.314436$ | $0.206689$ |
| $0.3$ | $0.647132$ | $0.424736$ | $0.314722$ | $0.206834$ |
| $0.1$ | $0.647564$ | $0.424647$ | $0.314053$ | $0.236373$ |
| $0.05$ | $0.646690$ | $0.510415$ | $0.443478$ | $0.335714$ |
| $0.02$ | $0.952252$ | $0.845483$ | $0.690764$ | $0.499309$ |
| $0.01$ | $1.397010$ | $1.196000$ | $0.942465$ | $0.658274$ |

Flat for $\delta_0\ge0.3$, still nearly flat at $0.1$ — the interior controls — and growing
below it. This is (v) of §3.2
behaving exactly as printed, and it means our use of (124), which lives at $x=X/\lambda=O(\lambda^{-1})$,
is in the flat regime and never sees the edge constant.

**Is the variable perturbation (116)+(117) doing work?** It is $O(\gamma^{-1})$, the same order
as the claimed error, so a check that passed with $\hat\rho$ replaced by $\rho$ would not have
tested our reconstruction of (117) past (111)'s typo. It does not pass. $D$ at $\delta_0=0.1$:

| $n$ | $\mu$ | with $\hat\rho$ | with $\rho$ | ratio |
|---|---|---|---|---|
| $0$ | $2$ | $0.0825461$ | $0.155726$ | $1.887$ |
| $0$ | $12$ | $0.0163816$ | $0.0880697$ | $5.376$ |
| $4$ | $2$ | $0.647564$ | $0.840982$ | $1.299$ |
| $4$ | $12$ | $0.141739$ | $1.11128$ | $7.840$ |

Without (116)+(117) the error **stops decaying** ($n=4$: $0.841,\ 1.160,\ 1.215,\ 1.199,\
1.111$ at $\mu=2,3,4,6,12$) while with it the error falls like $c^{-1}$. The reading of (117)
is therefore confirmed by measurement as well as by consistency with (111).

---

## 6. (124) $\Rightarrow$ (E), the corpus's own step — verified separately

`h0-lower-bound.md` §5 turns (124) into its (E) by three simplifications at $x=X/\lambda$:
$\hat\rho\sqrt{2c}\to2\sqrt\pi X$, prefactor $\to1$, $a\to2n+1$. Those are **ours**, so a
failure there is this repository's and not Dunster's. CHECK 4 splits the error:
$$e_D=\sup\big|\tfrac{\Phi_n(X/\lambda)}{\Phi_n(0)}-\mathrm{RHS}_{(124)}\big|,\quad
e_C=\sup\big|\mathrm{RHS}_{(124)}-\tfrac{h_n(X)}{h_n(0)}\big|,\quad
e_T=\sup\big|\tfrac{\Phi_n(X/\lambda)}{\Phi_n(0)}-\tfrac{h_n(X)}{h_n(0)}\big|$$
over $|X|\le\min(4,\lambda(1-\delta_0))$.

| $n$ | $\mu$ | $e_D$ | $c\,e_D/\log c$ | $e_C$ | $c\,e_C$ | $e_T$ | $c\,e_T$ |
|---|---|---|---|---|---|---|---|
| $0$ | $2$ | $0.0221403$ | $0.10993$ | $0.0140371$ | $0.17640$ | $0.0130785$ | $0.16435$ |
| $0$ | $12$ | $0.00357507$ | $0.06236$ | $0.00214531$ | $0.16175$ | $0.00203660$ | $0.15356$ |
| $4$ | $2$ | $0.895152$ | $4.44437$ | $0.886651$ | $11.1420$ | $0.281288$ | $3.53477$ |
| $4$ | $12$ | $0.103112$ | $1.79848$ | $0.0922647$ | $6.95660$ | $0.0315102$ | $2.37581$ |
| $8$ | $12$ | $0.395547$ | $6.89915$ | $0.373214$ | $28.1397$ | $0.0901125$ | $6.79432$ |

$c\,e_D/\log c$ decreases monotonically at every index (at $n=8$, after its $\mu=3$ peak). $c\,e_C$ and
$c\,e_T$ converge to finite limits — $c\,e_T\to0.1536,\ 1.0398,\ 2.3758,\ 4.2905,\ 6.7943$ at
$n=0,2,4,6,8$. So **(E) holds with $O(c^{-1})$, one $\log$ better than the note claims for it**;
that reproduces `h0-lower-bound.md` §7 CHECK 7 ("$O(1/c)$, with no $\log c$ visible") from a
different normalisation, and this is a *reproduction*, not an independent verification, of that
conclusion.

**The caution.** $e_D$ and $e_C$ are each roughly three times $e_T$ and they largely cancel. So
CHECK 7's clean $O(1/c)$ was **not** evidence that (124) is accurate at those bandwidths, and
should not have been read as such. §5 is the evidence.

**One range remark.** (E) is asserted on $|X|\le R$; the part of it inside Dunster's interval is
$|X|\le\lambda(1-\delta_0)$, which at $R=4$, $\delta_0=0.05$ needs $\mu\ge17.7$. At every
bandwidth in this ticket's range, CHECK 7's $|X|\le4$ window therefore extends past where (124)
says anything. Outside it the corpus's $\phi$ is identically zero and $h_n$ is $10^{-22}$ at
$X=4$, so nothing turned on it — but the window is not a test of (E) out there, and the table
above reports the honest $X_{\max}$ per row.

---

## 7. What this changes, and what it does not

**Does not change.** Theorem 6.1 of `h0-lower-bound.md`, the $-4\pi$ upper bound, or G13's
status as an external dependency. (E) enters Thm 6.1 only in step (i), a $\lambda\to\infty$
limit at fixed $n$; $\sigma_n(c)\to0$ for fixed $n$, so (29) holds for every $c>c^*_n$ and the
limit is taken well inside the hypothesis. The $(\mu,n)=(2,8)$ cell is outside Dunster's paper,
and no step of Thm 6.1 evaluates (E) there.

**Changes.** Two sentences of `h0-lower-bound.md` §5, and one row of its §10:

1. §0's and Bottom line 4's *"his standing hypothesis $\lambda<0$"* understates (29), which
   §5's own text has right further down. The hypothesis is $\sigma\le\sigma_0<1$ with
   $\sigma_0$ fixed, $\sigma=\sqrt{\chi_n}/c$, and $\pm\sigma$ are the turning points.
2. *"the corpus's measured $\chi_n/c^2$ runs 0.020 to 0.64 … so $\sigma\le0.8$ with room"* is
   false at index 8: $\sigma=0.883$ at $\mu=3$ — a row of the note's own §7 CHECK 6 — and
   $\sigma=1.020$ at $\mu=2$, where the hypothesis fails outright. The correct sentence names
   $c^*_8=13.3007$ and observes that Thm 6.1 is a limit and therefore unaffected.
3. §10 H0-1 should record **two** unopened sources, not one: Dunster [10] for (124)'s error
   bounds, and Arscott [1, p. 186] for (107)'s, via (27).

**The paper.** Per this ticket's constraints nothing in `start.tex`, `s3.tex` or `paper/` was
touched. If §§1.4, 1.6, 7.7 or G13 print "$\lambda<0$" as the hypothesis, the same correction
applies there, and it is a separate pass.

---

## 8. The house rule, applied to this note

> **Is any statement in this note false for $-W_\lambda$?**

| item | under $-W_\lambda$ | verdict |
|---|---|---|
| 1. §1's transcription | a quotation from a 2017 paper on special functions | **sign-blind** |
| 2. §2's dictionary and residual | a statement about an ODE | **sign-blind** |
| 3. §3's hypothesis audit and $c^*_n$ | statements about $\chi_n$ and $c$ | **sign-blind** |
| 4. §4's (107) | an eigenvalue asymptotic | **sign-blind** |
| 5. §5's (124) and §6's (E) | approximations to a special function | **sign-blind** |
| 6. §7's "does not change Thm 6.1" | Thm 6.1 is a norm limit; `h0-lower-bound.md` §8 already found it sign-blind | **sign-blind** |

Every item is sign-blind, as it must be: nothing here mentions $W_\lambda$, and the object
being checked is a prolate spheroidal wave function.

---

## 9. Open

| # | item | status |
|---|---|---|
| **D-1** | Dunster [10], the double-turning-point theory carrying (124)'s explicit error bounds. Still not opened. Opening it would turn $O(c^{-1}\log c)$ into a constant and make §5's tables a *test* of a bound rather than of a rate | **unopened** |
| **D-2** | Arscott [1, p. 186], (27)'s source and hence (107)'s. §4 tests the conclusion to its next coefficient; the source is not read | **unopened, newly flagged** |
| **D-3** | $Dc$ vs $Dc/\log c$: over $c\le24\pi$ the data cannot decide whether the $\log c$ in (124) is real. Deciding it needs $c$ an order of magnitude larger, which the $K=\lfloor c\rfloor+90$ eigensolver will reach but slowly | **open, and cheap** |
| **D-4** | $n=6,8$ are pre-asymptotic on the whole range ($\sigma\ge0.41$ at $\mu=12$). `h0-lower-bound.md` Remark 6.3 says the theorem does not depend on the index-8 mode, which is why this is a remark and not a defect — but any *quantitative* use of (E) at index 8 below $\mu\approx20$ would be resting on a 56% approximation | **measured; not a defect of the chain as written** |
| **D-5** | The paper's §§1.4, 1.6, 7.7 and G13 wording, per §7. Not touched here | **for a separate pass** |
