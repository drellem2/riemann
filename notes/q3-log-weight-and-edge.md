# Q3 is not routine: the $\log^3$ step rests on a false premise, and the edge does not converge as flagged — but the reduction closes anyway

Work item mg-731c. Companion script: [`verify_q3.py`](verify_q3.py) (needs `mpmath`;
no `numpy`; imports the prolate apparatus of [`verify_prolate_rate.py`](verify_prolate_rate.py),
the Legendre apparatus of [`verify_h1.py`](verify_h1.py) and the mode builder of
[`verify_q2.py`](verify_q2.py) — **no off-band evaluation is used anywhere below**, so
the `sph_j_all` sign defect of mg-9d43 cannot reach any number here).
Answers item **Q3** of [`h1-mean-value.md`](h1-mean-value.md) §9: *"write out the two
flagged steps of §3 — the fractional-Sobolev handling of the $\log^3$ weight, and the
$\sigma\to\pm\tfrac12$ edge"*, which that note records as **"open, but routine; poly
cost at worst"**.

Nothing in `start.tex`, `s3.tex` or the paper was edited. `h1-mean-value.md` and
`prolate-rate.md` are annotated in place, line-count-preserving, plus one appended
section to the first.

**Calibration, before anything else.** H1 is a bound on $\sum_\rho|\mathcal F_\mu r|^2$,
a sum of squared moduli. Closing it leaves the paper's and `prolate-rate.md`'s
upper bound $\limsup\mu^{-1}\log s(\mu)\le-4\pi$ conditional on (H0) alone — an
improvement to a result this project already has, and **not progress toward RH**. The matching lower bound is not open; it *is* RH
(`rhready.tex:1145`, paper Thm `thm:boundary`, gap **G10**), and nothing below touches
it. §7 applies the house rule: every line here is sign-blind, which is correct rather
than a defect. If any argument below ever appears to yield a lower bound on $s(\mu)$,
it is wrong.

---

## Bottom line

**1. Both steps are now written out, and the reduction closes — but "routine" is wrong
on both, and each was wrong in a different way.** The conclusion of §3's reduction
survives with an explicit constant,
$$\sum_{\rho}\big|\mathcal F_\mu r(s_\rho)\big|^2\;\le\;\Xi(\mu)\,\big(1-\chi_2(\lambda)\big),
\qquad \Xi(\mu)=O\!\big(\mu^{9/2}\log^3\mu\big),$$
which is (4.3) of `h1-mean-value.md` — **the estimate the paper's Cor. `cor:upper`
actually consumes**, so $\limsup\mu^{-1}\log s(\mu)\le-4\pi$ is now conditional on
**(H0) alone**. §4, Thm 4.4. Said precisely, and not more loosely than this: the
*literal* (H1) of §0, with its $\|r\|^2$ normalisation, is **not** proved and is not
provable — §1 of that note shows the $\|r\|^2$ normalisation is unattainable, and (4.3)
is what replaced it. H1's *role* is discharged; H1 as written is bypassed. The route
that gets there is *not* the route §3 names.

**2. The $\log^3$ step's premise is false, and it is falsified by the same note's own
§4.** §3 says *"$R$ is bounded with a single jump at $v=\log\lambda$ and is smooth to
the right of it"*. It is not. The spill has a jump at $u=\lambda/N$ for **every** integer
$N>\mu$, of size exactly $|\Phi(1)|\,N^{-1/2}$ — measured against one-sided limits at 24
$(c,N)$ cells, ratio $1.0$ to every printed digit (§6, CHECK 1). Those jumps *are* the
sawtooth $\tfrac12-\{ct/2\pi\}$ that §4 uses to prove its own leading term: §3 and §4 of
that note contradict each other, and §4 is the one that is right. §1–§2.

**3. The input §3 asks for does not exist, and the nearest thing that does is
exponentially expensive.** §3 asks for *"a bound on $\|R'\|$ of the same character as
(D)"*. $R'$ is not a function — it carries $\sum_{N>\mu}\Phi(1)N^{-1/2}\delta_{v_N}$ —
and on the smooth pieces $|R'|\asymp\mu t\,|R|$, which **grows** where (D) decays. The
fractional-Sobolev conclusion survives in a weakened form (Prop. 2.2), but only for
$\delta<\tfrac12-\alpha$, with a constant $\mu^{2\delta}$, and conditional on a
*derivative* dilate-sum bound (P′) that nobody has proved. The only bound on that
derivative available from the corpus today is term-by-term, and it is loose by
$\|\Phi'\|_\infty/|\Phi(1)|\asymp e^{c}$ — measured $1.3\times10^2$ at $c=4\pi$ rising to
$1.3\times10^{17}$ at $c=16\pi$ (§6, CHECK 2). **Not poly.** §2.

**4. The edge is one-sided, and in the order §3 takes it the integral diverges.**
$N(\alpha)$ blows up only as $\alpha\uparrow\tfrac12$, i.e. only as $\sigma\downarrow-\tfrac12$,
i.e. only as $\beta\to0$; at $\sigma\to+\tfrac12$ nothing happens. And the two flagged
steps are **not independent**: (ZFR) makes the edge at $\eta=\tfrac12-|\sigma|$ draw only
on $|t|\ge T(\eta)=e^{c_0/\eta}-3$, where the $\log^3$ weight is *already*
$(c_0/\eta)^3$. So §3's *"the divergence is integrated only up to
$\tfrac12-\tfrac{c_0}{2\log}$ and contributes a further logarithm"* — $\int d\eta/\eta$ —
is really $\int d\eta/\eta^{4}$, and it has no cutoff. §3.

**5. Both close together, by an assembly §3 does not name, and the cost is $\mu^3$
rather than a logarithm.** Truncate the *zero sum* at height
$T_*=\exp(4\pi\mu+O(\log\mu))$. Above $T_*$, $\mathcal F_\mu r=-\mathcal F_\mu g$ on $Z$
(`prolate-rate.md` §6(a)) and $g$ is of bounded variation on a compact interval in
$\log u$, so those zeros contribute $\ll\lambda V_*^2\log T_*/T_*$, which is below the
target because $\Phi(1)^2\ge(1-\Lambda_4)/(2K_1^2C_*^2)$ — a **proved** lower bound, from
Q1 and the exact identity (4.1) of that note — and Fuchs. Below $T_*$ the $\log^3$ weight is a
*constant*, $\log^3(3+T_*)=O(\mu^3)$, so no Sobolev theory is needed at all, and the same
truncation caps $|\sigma|$ at $\tfrac12-\eta_*$ with $\eta_*\asymp1/\mu$, which is what
makes §3's "further logarithm" true after all: $\tfrac12\log(1/2\eta_*)=O(\log\mu)$.
**The two flagged steps are one step, and the step is a truncation.** §4.

**6. Which outcome of the ticket is this?** **(3)** and **(2)**, not (1) and not (4).
One step is false as stated (item 2) but its *conclusion* is not needed; the other does
not converge as flagged (item 4) but does converge in a different order. The cost is
poly, as advertised — $\mu^{9/2}$, against an unstated expectation of logarithms — and
§4's reduction still consumes it. The third misdiagnosis in a row on this chain: mg-6851
refuted §5's "connection at the regular singular point", mg-9d43 refuted §9's "control
the Osipov–Rokhlin remainders", and this refutes §3's "single jump, smooth to the right".
**Each time the note was right that something was missing and wrong about what.**

**7. What is still open here.** Whether $\Xi$ can be brought below $\mu^{9/2}$ (Q3′,
§8). The $\mu^3$ is forced by $\log^3T_*$ and $T_*$ is forced by the *size of the
target*, so any improvement must avoid discarding zeros by height — and §5 checks that
replacing (ZFR) by a zero-density estimate improves the admissible cutoff by a constant
factor only, so that is **not** the route. Nothing downstream needs it.

---

## 0. What is being written out, verbatim

`h1-mean-value.md` §3, the two flagged bullets, quoted in full because the whole of this
note is about what they say:

> - **The $\log^3$ weight.** $\log^3(3+|t|)\le C_\delta(1+|t|)^{2\delta}$ for any
>   $\delta>0$, so the weighted integral is $\ll_\delta\|R\,e^{-\sigma\cdot}\|^2_{H^{\delta}}$.
>   $R$ is bounded with a single jump at $v=\log\lambda$ and is smooth to the right
>   of it, so $R\in H^{\delta}$ for every $\delta<\tfrac12$ and $\delta=\tfrac14$ is
>   comfortable. **This step needs a bound on $\|R'\|$ of the same character as (D),
>   and I have not written it out.** It costs a factor $c$, i.e. poly.
> - **The edges $\sigma\to\pm\tfrac12$.** $N(\alpha)$ diverges as
>   $\alpha\uparrow\tfrac12$ under (D) alone, like $(1-2\alpha)^{-1}$. The discs are
>   cut off at $\epsilon_\rho\gtrsim1/\log(3+|t|)$ by (ZFR), so the divergence is
>   integrated only up to $\tfrac12-\tfrac{c_0}{2\log}$ and contributes a further
>   logarithm. **This is the one place a zero-free region is used, and it is used
>   only qualitatively.** I have checked the exponents, not written the estimate
>   out in full.

Conventions are `h1-mean-value.md` §0 unchanged: $\lambda>1$, $\mu=\lambda^2$,
$c=2\pi\mu$; $\phi$ the normalised three-mode near-radical vector supported in
$[-\lambda,\lambda]$ with $\phi(0)=\widehat\phi(0)=0$; $\Phi(y)=\lambda^{1/2}\phi(\lambda y)$
on $[-1,1]$ with $\int_{-1}^1\Phi^2=1$; $\mathcal E\phi(u)=u^{1/2}\sum_{n>0}\phi(nu)$;
$g=\mathcal E\phi|_{[\lambda^{-1},\lambda]}$, $r=\mathcal E\phi|_{(0,\lambda^{-1})}$;
$F(s)=\mathcal F_\mu r(s)$, $R(v)=r(e^{-v})$, $N(\alpha)=\int_{\log\lambda}^\infty|R|^2e^{2\alpha v}dv$,
$s_\rho=\gamma_\rho+i(\beta_\rho-\tfrac12)$. Throughout I write
$$t:=\frac{e^{v}}{\lambda}\in(1,\infty),\qquad
\eta:=\tfrac12-|\sigma|,\qquad \alpha:=-\sigma,\qquad
\eta_\rho:=\min(\beta_\rho,1-\beta_\rho).$$

---

## 1. The spill, written down exactly: a finite sum of on-band values — *ours (elementary)*

Everything in §2–§4 rests on one two-line computation that `h1-mean-value.md` never
performs.

**Lemma 1.1 (ours).** *For $t>1$ and $u=1/(\lambda t)\in(0,\lambda^{-1})$,*
$$R(v)\;=\;r(u)\;=\;\frac{1}{\lambda\sqrt t}\sum_{1\le n\le \mu t}\Phi\!\Big(\frac{n}{\mu t}\Big),
\qquad v=\log(\lambda t). \tag{1.1}$$
*The sum is finite and **every argument lies in $[0,1]$**: no off-band value of $\Phi$
occurs.*

*Proof.* $\mathcal E\phi(u)=u^{1/2}\sum_{n>0}\phi(nu)$ and
$\phi(x)=\lambda^{-1/2}\Phi(x/\lambda)$ vanishes for $|x|>\lambda$, so only
$n\le\lambda/u=\mu t$ contribute, and $nu/\lambda=n/(\mu t)$. Finally
$u^{1/2}\lambda^{-1/2}=(\lambda t)^{-1/2}\lambda^{-1/2}=(\lambda\sqrt t\,)^{-1}$. $\square$

Write $A(t):=\lambda\sqrt t\,R(t)=\sum_{n\le\mu t}\Phi(n/(\mu t))$ for the bracket.

**Corollary 1.2 (the jump structure — this is the finding).** *$R$ is real-analytic on
each open interval $t\in\big(\tfrac N\mu,\tfrac{N+1}\mu\big)$ and has a jump
discontinuity at every $t=N/\mu$ with $N\in\mathbb Z$, $N>\mu$:*
$$R\Big(\tfrac N\mu^+\Big)-R\Big(\tfrac N\mu^-\Big)\;=\;\frac{\Phi(1)}{\sqrt N},
\qquad\text{equivalently}\qquad
[R]_{v_N}=\frac{\Phi(1)}{\sqrt N}\ \text{ at }\ v_N=\log\frac N\lambda,
\ \text{ i.e. at } u=\frac\lambda N. \tag{1.2}$$

*Proof.* As $t$ increases through $N/\mu$ the term $n=N$ enters (1.1) with argument
$N/(\mu t)=1$, contributing $\Phi(1)$; every other term is analytic there. Divide by
$\lambda\sqrt{N/\mu}=\sqrt N$. $\square$

Three remarks, and the second is the one that matters.

- **These are exactly §4's sawtooth jumps.** $t\in\tfrac1\mu\mathbb Z$ is
  $\{ct/2\pi\}=\{\mu t\}=0$, the jump set of $\tfrac12-\{ct/2\pi\}$. §4 of
  `h1-mean-value.md` derives that sawtooth as the leading behaviour of $G$ and uses it;
  §3 of the same note asserts $R$ is smooth. **Both cannot hold.**
- **The jumps are not a boundary artefact — they are the function.** Measured,
  $|[R]|/|R|$ runs $0.71$ to $1.59$ across all four bandwidths and all $N$ tested
  (§6, CHECK 1). $R$ is a sawtooth of slowly-decaying amplitude whose period,
  $1/\mu$ in $t$, is $e^{-v}/\lambda$ in $v$ — **shrinking**, so the jump density per
  unit $v$ is $\mu t=\lambda e^{v}$ and grows without bound.
- **Consistency with `dilate-sum.md` Prop. 6.1.** That proposition gives
  $tG(t)=\frac{1}{2\mu\mu_\Phi}\sum'_{|k|\le\lfloor\mu t\rfloor}\Phi(k/(\mu t))-\tfrac{t\Phi(0)}2$;
  with $\Phi(0)=0$ this says $A(t)=\mu\mu_\Phi\,tG(t)$, and its jump — two terms
  $k=\pm\lfloor\mu t\rfloor$ entering at value $\Phi(1)$ — is $\Phi(1)/(\mu\mu_\Phi)$,
  which is (1.2) after the same division. Two independent derivations of the same
  number; the script checks it against one-sided limits of (1.1) directly.

**What makes the spill decay is $\widehat\phi(0)=0$, and it is visible in (1.1).**
The finite sum in (1.1) is a Riemann-type sum for $\mu t\int_0^1\Phi$; the admissibility
condition $\widehat\phi(0)=0$ is exactly $\int_0^1\Phi=0$, which kills that secular term
and leaves an $O(|\Phi(1)|)$ remainder. Without it $R$ would grow like $\sqrt t$ and (D)
would be false. Both conditions are verified to $10^{-121}$ in CHECK 0.

---

## 2. Step A: the $\log^3$ weight — *the premise is false, and the repair is not poly*

### 2.1 What is false

**(A1) "a single jump at $v=\log\lambda$, smooth to the right of it".** False by
Cor. 1.2: there is a jump at $v_N=\log(N/\lambda)$ for **every** integer $N>\mu$, and
$v_{\lceil\mu\rceil}$ is the *first* of infinitely many, not the only one. The endpoint
jump §3 has in mind is the one at $t=1$ ($R$ rising from $0$); §3 sees it because
`prolate-rate.md` §6(c) records it — *"smooth on $(0,\lambda^{-1})$ but has a jump at the
endpoint"* — and that sentence has the same defect.

**(A2) "a bound on $\|R'\|$ of the same character as (D)".** False, twice over.
$R'$ is not a function: as a distribution it contains
$\sum_{N>\mu}\Phi(1)N^{-1/2}\delta_{v_N}$. And between jumps it does not decay: from
(1.1), $R=A/(\lambda\sqrt t)$ with
$$A'(t)\;=\;-\frac1t\sum_{1\le n\le\mu t}\Psi\!\Big(\frac n{\mu t}\Big),
\qquad \Psi(x):=x\,\Phi'(x), \tag{2.1}$$
whose size is $\asymp\mu|\Phi(1)|$ — measured range of $|A'|/(\mu|\Phi(1)|)$ over one
inter-jump interval: $0.02$ to $26$ across four bandwidths (§6, CHECK 2). Hence
$|R'|\asymp\mu t\,|R|\asymp\lambda e^{v/2}$, which **grows** where (D) decays. The
requested input is not merely unwritten; it is not true.

*(Why $\asymp\mu|\Phi(1)|$ and not $\to-\mu\Phi(1)$: after differentiation the second
off-band term $a_2\cos(cx)/x^2$ of `dilate-sum.md` §3 contributes at the same order,
since $c\,a_2\asymp2\pi\mu\Phi(1)/\mu_\Phi$. The claim used below is only that the ramp
is $O(\mu|\Phi(1)|)$ and not $O(|\Phi(1)|)$, which is what CHECK 2 measures.)*

### 2.2 What survives, and at what price

The *conclusion* $R\in H^\delta$ is not lost — a sawtooth is in $H^\delta$ for
$\delta<\tfrac12$ — but the weighted version, which is what (3.1) needs, degrades in two
ways that the single-jump picture cannot show.

**Hypothesis (P′) (named here; not proved anywhere).** *There is $K_D(c)$ with*
$$\Big|\frac{d}{dt}\Big[\lambda\sqrt t\,R(t)\Big]\Big|\;\le\;\mu\,K_D(c)\,|\Phi(1)|
\qquad\text{for all }t>1,\ t\notin\tfrac1\mu\mathbb Z. \tag{P′}$$

**Proposition 2.2 (ours).** *Assume (P) and (P′), let $0<\alpha<\tfrac12$ and
$0<\delta<\tfrac12-\alpha$, and put $\psi_\alpha(v):=e^{\alpha v}R(v)\mathbf 1_{v\ge\log\lambda}$,
$\mathcal K:=\sqrt{\mu\Lambda}\,K_P|\Phi(1)|$ (the (P)-bound on $|A|$). Then*
$$\int_{\mathbb R}(1+|t|)^{2\delta}\big|F(t-i\alpha)\big|^2dt\;\ll\;
\lambda^{2\alpha-2}\,\mu^{2\delta}\left[
\frac{\mathcal K^{2}+\alpha^{-1}\Phi(1)^2(1+K_D^{2})}{1-2\alpha-2\delta}
+\frac{\mathcal K^{2}}{\delta\,(1-2\alpha)}\right],$$
*with an absolute implied constant. (At $\alpha=0$ the factor $\alpha^{-1}$ is replaced
by a logarithm.)*

*Proof.* Write $\Psi_\alpha(t):=\lambda^{\alpha-1}t^{\alpha-1/2}A(t)$ for $t\ge1$ and $0$
below, so $\psi_\alpha(v)=\Psi_\alpha(t)$ and $dv=dt/t$; then
$\|\psi_\alpha\|_2^2=\lambda^{2\alpha-2}\int_1^\infty t^{2\alpha-2}|A|^2dt
\le\lambda^{2\alpha-2}\mathcal K^2/(1-2\alpha)$, which is $N(\alpha)$. Use the classical
identity $\|\psi\|^2_{\dot H^\delta}=C_\delta'\int_0^\infty h^{-1-2\delta}\omega(h)^2dh$
with $\omega(h)^2=\|\psi(\cdot+h)-\psi\|_2^2$, and
$\omega(h)^2=\int_1^\infty|\Psi_\alpha(te^h)-\Psi_\alpha(t)|^2\tfrac{dt}t$.

For $h\ge1/\mu$ use $\omega(h)^2\le4\|\psi_\alpha\|_2^2$. For $h<1/\mu$ split at
$T_h:=1/(\mu h)>1$. Beyond $T_h$, bound as in the saturated case and translate the
integral: $\int_{T_h}^\infty\le4\lambda^{2\alpha-2}\mathcal K^2T_h^{2\alpha-1}/(1-2\alpha)
\asymp\lambda^{2\alpha-2}\mathcal K^2(\mu h)^{1-2\alpha}/(1-2\alpha)$. Below $T_h$ the
shift $t(e^h-1)\le eh\,T_h\le e/\mu$ crosses at most one jump, so
$|\Psi_\alpha(te^h)-\Psi_\alpha(t)|$ is at most the jump at the crossed point plus
$\sup|t\Psi_\alpha'|\,h$. The jump at $t_N=N/\mu$ is
$\lambda^{\alpha-1}t_N^{\alpha-1/2}|\Phi(1)|$ by (1.2) and is met on a $t$-set of measure
$\le t_Nh$, so, using $\sum_{1\le t_N\le T}t_N^{2\alpha-1}\le\mu T^{2\alpha}/(2\alpha)$,
the jump part of $\omega(h)^2$ is
$\ll\lambda^{2\alpha-2}\Phi(1)^2\mu^{1-2\alpha}h^{1-2\alpha}/(2\alpha)$. For the smooth
part, $|t\Psi_\alpha'|\le\lambda^{\alpha-1}t^{\alpha-1/2}(\tfrac12|A|+t|A'|)$, and with
(P′) its contribution is
$\ll h^2\lambda^{2\alpha-2}\mu^2K_D^2\Phi(1)^2T_h^{2\alpha+1}
\asymp\lambda^{2\alpha-2}K_D^2\Phi(1)^2\mu^{1-2\alpha}h^{1-2\alpha}$ — the *same* order
as the jump part, which is Cor. 1.2's statement that the ramp compensates the jumps.
Now integrate: $\int_0^{1/\mu}h^{-1-2\delta}(\mu h)^{1-2\alpha}dh=\mu^{2\delta}/(1-2\alpha-2\delta)$
and $\int_{1/\mu}^\infty h^{-1-2\delta}dh=\mu^{2\delta}/(2\delta)$. Finally
$\int(1+|t|)^{2\delta}|\hat\psi|^2\asymp\|\psi\|_2^2+\|\psi\|^2_{\dot H^\delta}$
(classical), and $F(t-i\alpha)=\hat\psi_\alpha(-t)$ by (0.1). $\square$

**Three consequences, none of them in §3.**

1. **$\delta<\tfrac12-\alpha$ is forced, not $\delta<\tfrac12$.** The Sobolev exponent
   available at height $\sigma$ shrinks to $0$ at the edge. This is the *first* place the
   two flagged steps touch, and it is why they cannot be costed separately.
2. **The constant carries $\mu^{2\delta}$**, from the jump spacing $1/\mu$ — invisible in
   a single-jump picture, where the constant would be $O(1)$.
3. **(P′) is a genuine open lemma of Q2's type, not bookkeeping.** It is a dilate-sum
   bound for $x\Phi'(x)$ rather than $\Phi(x)$, and `dilate-sum.md` proves nothing about
   it. What *is* provable today is the term-by-term bound from (2.1),
   $$|A'(t)|\;\le\;\mu\,\|\Psi\|_{L^\infty[0,1]}\;\le\;\mu\,\|\Phi'\|_{L^\infty[-1,1]},
   \qquad \|\Phi_n'\|_\infty\le\sqrt{c^3/(\pi\Lambda_n)}$$
   (the second from the finite-Fourier eigenrelation: $\Phi_n'(x)=\mu_\Phi^{-1}\int_{-1}^1
   icy\Phi_n(y)e^{icxy}dy$, so $|\Phi_n'|\le c\|\Phi_n\|_{L^1}/|\mu_\Phi|\le
   c\sqrt2/|\mu_\Phi|$ and $|\mu_\Phi|=\sqrt{2\pi\Lambda_n/c}$). That is (P′) with
   $K_D=\|\Phi'\|_\infty/|\Phi(1)|$, and since $|\Phi(1)|\asymp c^{11/4}e^{-c}$ while
   $\|\Phi'\|_\infty$ is polynomial, $K_D\asymp e^{c}$ up to a power of $c$. Measured:
   $1.3\times10^2,\ 2.5\times10^4,\ 2.3\times10^9,\ 1.3\times10^{17}$ at
   $c=4\pi,6\pi,10\pi,16\pi$, with $\log K_D/c=0.39,0.54,0.68,0.78$ rising toward $1$
   (§6, CHECK 2). **$K_D^2\asymp e^{2c}=e^{4\pi\mu}$ is exactly the reciprocal of the
   quantity being bounded**, so this route as it stands destroys the whole estimate.
   The Euler–Maclaurin/Koksma alternative — bound $\sum_{n\le M}\Psi(n/M)$ by
   $M\int_0^1\Psi+\operatorname{Var}(\Psi)$ — fails for the *same* reason, and
   `dilate-sum.md` §6 has already recorded that reason one derivative down: its kernel
   pairs with $\int_{-1}^1|\Phi'|=O(c^{1/4})$, which is "$e^{+\Theta(c)}$ times too
   large relative to $|\Phi(1)|$". **(P′) will need an off-band argument of §§3–5's
   kind, exactly as (P) did.** That is why it is a lemma and not bookkeeping.

**So step A, on the route §3 names, is: false premise, missing lemma, and — with the
only currently available substitute for that lemma — exponential.** §4 does not use any
of it.

---

## 3. Step B: the $\sigma$ edge — *one-sided, and divergent in the order §3 takes it*

### 3.1 There is one edge, not two

$N(\alpha)=\int_{\log\lambda}^\infty|R|^2e^{2\alpha v}dv$ diverges only as
$\alpha\uparrow\tfrac12$. For $\alpha\le0$, $e^{2\alpha v}\le\lambda^{2\alpha}\le1$ on the
support, so $N(\alpha)\le N(0)$ — nothing happens. Since $\alpha=-\sigma$ and
$\sigma=\beta_\rho-\tfrac12$:

> **the singular edge is $\sigma\to-\tfrac12$ alone, i.e. $\beta_\rho\to0$;
> $\sigma\to+\tfrac12$ ($\beta_\rho\to1$) is harmless.**

§3's "$\sigma\to\pm\tfrac12$" is symmetric and the situation is not. It cannot be dodged
by discarding one side: the zeros come in pairs $\rho,1-\bar\rho$, so the harmless side
is populated exactly as densely as the singular one.

### 3.2 The two flags multiply

**Observation 3.1 (ours; elementary).** *Take the order §3 proposes — keep
$\log^3(3+|t|)$ inside the integral, and let (ZFR) cut the $\sigma$-range at each $t$.
By (ZFR) a zero with $\eta_\rho\le\eta$ has $\log(3+|\gamma_\rho|)\ge c_0/\eta$, so after
Fubini the bound reads*
$$\mathcal I=\int_{-1/2}^{1/2}\left(\int_{|t|\ge T(\eta)}\log^3(3+|t|)\,
\big|F(t+i\sigma)\big|^2dt\right)d\sigma,\qquad T(\eta)=e^{c_0/\eta}-3,$$
*and on the inner region $\log^3(3+|t|)\ge(c_0/\eta)^3$. Hence*
$$\mathcal I\;\ge\;\Big(\frac{c_0}{\eta}\Big)^{3}\!\!\int_{-1/2}^{1/2}\!\!
\int_{|t|\ge T(\eta)}\big|F(t+i\sigma)\big|^2\,dt\,d\sigma
\quad\Longrightarrow\quad
\mathcal I<\infty\ \text{ requires }\
\int_{|t|\ge T(\eta)}\!|F(t+i\sigma)|^2dt=O(\eta^{3+\epsilon}).$$

That is the whole point: §3's estimate of the edge, *"a further logarithm"*, is
$\int_{\eta_{\min}}^{1/2}\frac{d\eta}{\eta}$, which is what one gets by treating the
$\log^3$ weight as $\eta$-free. It is not $\eta$-free — it is evaluated at the height
(ZFR) forces — and the correct integrand is $\eta^{-4}$. Arithmetically, at $c_0=1$:
$\int_\eta^{1/2}\frac{de}{e}$ runs $1.61,3.91,6.21,8.52$ as $\eta$ runs
$10^{-1},\dots,10^{-4}$, while $\int_\eta^{1/2}\frac{de}{e^4}$ runs
$3.3\times10^2,\ 3.3\times10^5,\ 3.3\times10^8,\ 3.3\times10^{11}$ (§6, CHECK 3).

**And the tail is not small — *observed*, not proved.** By `prolate-rate.md` §1 step 1
and §6(a),
$$F(s)=\mathcal F_\mu(\mathcal E\phi)(s)-\mathcal F_\mu g(s),\qquad
\mathcal F_\mu(\mathcal E\phi)(s)=\pi^{-\frac14+\frac{is}2}\Gamma\big(\tfrac14-\tfrac{is}2\big)
\zeta\big(\tfrac12-is\big)P_\phi(s),$$
and on the line $\Im s=\sigma$ the zeta factor is evaluated at real part
$\tfrac12+\sigma=\eta$. There $|\zeta|$ has mean square growing like $|t|^{1-2\eta}$,
which exactly cancels the $|t|^{-2\eta}$ that the tail integral would need: with
$|F|\asymp|\zeta|/|t|$ (the $1/|t|$ from $P_\phi$, whose $\phi$ is compactly supported and
of bounded variation), $\int_{|t|>T}|F|^2\asymp D_\eta T^{-2\eta}$, and at
$T=T(\eta)=e^{c_0/\eta}$ that is $D_\eta e^{-2c_0}$ — **a constant as $\eta\to0$, not
$O(\eta^{3})$.** So $\mathcal I=+\infty$ and the ordering yields nothing.

The $\zeta$ half of that is classical and is checked in CHECK 4 against
$M(T)=\zeta(2\eta)+K(\eta)(2^{2-2\eta}-1)T^{1-2\eta}$ (Titchmarsh Thm 7.2(A), **quoted
from memory and not opened**, so the check tests the formula as much as the arithmetic):
measured/predicted lies in $[0.96,1.03]$ at eight cells, with the local exponent
descending to $0.775$ against the predicted $0.8$ at $\eta=0.1$ and to $0.487$ against
$0.5$ at $\eta=0.25$ — from above, as the negative constant $\zeta(2\eta)$ requires. The
step from that to $|F|$ is the observed part, and §4 does not use it: it is here to say
that the divergence in Observation 3.1 is not an artefact of a lossy bound.

---

## 4. Both steps close, together, and the mechanism is a truncation — *ours*

The repair is to stop bounding the whole zero sum by one integral. Two inputs are used
that §3 does not mention, and neither is new to the project.

### 4.1 The high zeros: the identity that made §6 possible, used again

**Lemma 4.1 (ours).** *Let $g_0(w):=g(e^{-w})$ on $[-L,L]$, $L=\log\lambda$, extended by
zero, and put*
$$V_*\;:=\;\operatorname{Var}_{\mathbb R}(g_0)\;+\;L\,\|g_0\|_\infty\;<\;\infty .$$
*Then for every $T_*\ge3$,*
$$\sum_{|\gamma_\rho|>T_*}\big|F(s_\rho)\big|^2\;\le\;
\frac{C_2\,\lambda\,V_*^2\,\log T_*}{T_*}. \tag{Q3.1}$$

*Proof.* $\mathcal F_\mu(\mathcal E\phi)$ vanishes on $Z$ (`prolate-rate.md` §1 step 1),
so $F(s_\rho)=-\mathcal F_\mu g(s_\rho)$ — this is precisely the identity §6(a) uses to
write $QW_\lambda(g,g)=\sum_Z|\mathcal F_\mu r|^2$. Substituting $u=e^{-w}$,
$\mathcal F_\mu g(t+i\sigma)=\int_{-L}^{L}g_0(w)e^{-\sigma w}e^{itw}dw$, the Fourier
transform of a compactly supported function of bounded variation, so it is at most
$\operatorname{Var}(g_0e^{-\sigma\cdot}\mathbf 1_{[-L,L]})/|t|\le\lambda^{1/2}V_*/|t|$ for
$|\sigma|\le\tfrac12$, using $\operatorname{Var}(fg)\le\|f\|_\infty\operatorname{Var}(g)+
\|g\|_\infty\operatorname{Var}(f)$ and $\operatorname{Var}(e^{-\sigma\cdot})\le L\lambda^{1/2}$
on $[-L,L]$. $g$ is of bounded variation because, by the argument of Lemma 1.1, $g_0$ is
a finite sum of at most $\lfloor\mu\rfloor$ real-analytic pieces with jumps at
$u=\lambda/n$, $n\le\mu$. Then sum $|\gamma_\rho|^{-2}$ over $|\gamma_\rho|>T_*$ using
Riemann–von Mangoldt and partial summation. $\square$

$V_*$ is measured at $1.52$–$1.73$ across $\mu=2,\dots,8$ — bounded, not merely
polynomial (§6, CHECK 5; grid-limited, hence an under-report). All that is used below is
$V_*=e^{o(\mu)}$.

### 4.2 The low zeros: Prop. 3.1 with the weight frozen

**Lemma 4.2 (ours).** *For $T_*\ge3$ put $\eta_*:=\dfrac{c_0}{2\log(4+T_*)}$. Then,
under (D),*
$$\sum_{|\gamma_\rho|\le T_*}\big|F(s_\rho)\big|^2\;\le\;
\frac{C_3\,\log^3(4+T_*)}{c_0^{2}}
\int_{|\sigma|\le\frac12-\eta_*}\int_{\mathbb R}\big|F(t+i\sigma)\big|^2\,dt\,d\sigma. \tag{Q3.2}$$

*Proof.* Exactly `h1-mean-value.md` Prop. 3.1, with one change: bound
$\log(3+|\gamma_\rho|)$ by $\log(3+T_*)$ *before* integrating rather than keeping it under
the integral. With $\epsilon_\rho=\tfrac12\eta_\rho$, (ZFR) gives
$\epsilon_\rho\ge\eta_*$, so the subharmonicity weight is
$\frac1{\pi\epsilon_\rho^2}\le\frac{1}{\pi\eta_*^2}=\frac{4\log^2(4+T_*)}{\pi c_0^2}$; every
covering disc has $|\gamma_\rho-t|\le\tfrac14$ and $|\gamma_\rho|\le T_*$, so the
multiplicity is $\le C_1\log(4+T_*)$; and every disc lies in
$|\Im z|\le|\Im s_\rho|+\epsilon_\rho=\tfrac12-\tfrac{\eta_\rho}2\le\tfrac12-\eta_*$,
which is where the $\sigma$-range comes from. $\square$

**This is the step that retires the fractional-Sobolev problem entirely.** With the
weight frozen there is no $t$-dependent factor left inside, so Plancherel on horizontal
lines (§3, Prop. 3.2) applies as it stands and nothing about the smoothness of $R$ is
ever needed. The price is that $\log^3(4+T_*)$ is now a constant that must be paid in
full — $O(\mu^3)$, since $T_*$ will be exponentially large.

### 4.3 Choosing $T_*$: a proved lower bound on $\Phi(1)^2$

**Lemma 4.3 (ours; from Q1 and the exact identity).** *For an even index $n$ with
$\chi_n<c^2$,*
$$\Phi_n(1)^2\;\ge\;\frac{1-\Lambda_n}{2K_1(c)^2\,\Lambda_n}\;\ge\;\frac{1-\Lambda_n}{2K_1(c)^2}.$$

*Proof.* Q1 (`band-edge-connection.md` Thm 5.2) gives $x|\Phi_n(x)|\le K_1|\Phi_n(1)|$
for $x\ge1$, so
$\int_{|x|>1}|\Phi_n|^2\le2K_1^2\Phi_n(1)^2\int_1^\infty x^{-2}dx=2K_1^2\Phi_n(1)^2$;
compare with the exact identity $\int_{|x|>1}|\Phi_n|^2=(1-\Lambda_n)/\Lambda_n$
(`h1-mean-value.md` (4.1)). $\square$

For the three-mode combination the same argument with hypothesis **(C)** of
`dilate-sum.md` §5 — $\sum_m|b_m||\Phi_{n_m}(1)|\le C_*|\Phi(1)|$, already carried by
everything downstream — gives $\Phi(1)^2\ge b_2^2(1-\Lambda_4)/(2K_1^2C_*^2)$. ((C) is
measured, not proved; rather than quote the number I re-ran `verify_q2.check4` here and
got $C_*=1.0529,\,1.0089,\,1.0023,\,1.0008$ at $c=4\pi,6\pi,10\pi,16\pi$ — falling to
$1$, so the combination costs essentially nothing.) With Fuchs' asymptotic
$1-\Lambda_4\sim4\sqrt\pi\,8^4c^{9/2}e^{-2c}/4!$ — quoted from `prolate-rate.md` §2,
which quotes Fuchs' Theorem 1; **I did not open Fuchs** — this is
$$\log\frac{1}{\Phi(1)^2}\;\le\;2c+O(\log c)\;=\;4\pi\mu+O(\log\mu). \tag{Q3.3}$$
**This is a lower bound on a prolate concentration defect, not on $s(\mu)$.** It is
classical, sign-blind, and carries no arithmetic content; see §7.

Measured, $\Phi(1)^2/(1-\Lambda_4)$ is $7.08,\,12.08,\,21.36,\,35.13$ at
$c=4\pi,6\pi,10\pi,16\pi$, i.e. $\approx0.7c$ — §7's observed identity of
`h1-mean-value.md`, which the proof does **not** use: only the bounded-below direction
of Lemma 4.3 is needed, and that is proved.

### 4.4 The theorem

**Theorem 4.4 (Q3, both steps, ours).** *Assume* **(P)** *— proved: Q1 (mg-6851) plus Q2
(mg-9d43), `dilate-sum.md` Thm 5.1 and Cor. 5.2. Choose $T_*\ge3$ with*
$$\frac{C_2\lambda V_*^2\log T_*}{T_*}\;\le\;\Phi(1)^2 . \tag{Q3.4}$$
*Then*
$$\sum_{\rho}\big|\mathcal F_\mu r(s_\rho)\big|^2\;\le\;
\left[\frac{2\pi C_3\log^3(4+T_*)}{c_0^{2}}\,K_P(c)^2
\left(\frac12+\frac\lambda2\log\frac{1}{2\eta_*}\right)+1\right]\Phi(1)^2,
\qquad \eta_*=\frac{c_0}{2\log(4+T_*)} .$$

*Proof.* Split the sum at $|\gamma_\rho|=T_*$. The high part is $\le\Phi(1)^2$ by
Lemma 4.1 and (Q3.4). For the low part apply Lemma 4.2, then Prop. 3.2 of
`h1-mean-value.md` — $\int_{\mathbb R}|F(t+i\sigma)|^2dt=2\pi N(-\sigma)$ — then
Prop. 4.1 of that note: $N(\alpha)\le\lambda^{2\alpha}K_P^2\Phi(1)^2/(1-2\alpha)$ for
$0\le\alpha<\tfrac12$, and $N(\alpha)\le N(0)\le K_P^2\Phi(1)^2$ for $\alpha\le0$. The
$\sigma>0$ half contributes $\le\tfrac12K_P^2\Phi(1)^2$ and the $\sigma<0$ half
$$\int_0^{\frac12-\eta_*}\frac{\lambda^{2\alpha}K_P^2\Phi(1)^2}{1-2\alpha}\,d\alpha
\;\le\;\frac{\lambda}{2}\,K_P^2\Phi(1)^2\log\frac{1}{2\eta_*}. \qquad\square$$

**Corollary 4.5 (the estimate (4.3) of `h1-mean-value.md`).** *By (Q3.3) and $V_*=e^{o(\mu)}$, (Q3.4) holds with
$\log T_*=4\pi\mu+O(\log\mu)$, whence $\log^3(4+T_*)=(4\pi)^3\mu^3(1+o(1))$,
$\eta_*\asymp c_0/(8\pi\mu)$ and $\log(1/2\eta_*)=O(\log\mu)$, so*
$$\sum_\rho\big|\mathcal F_\mu r(s_\rho)\big|^2\;\le\;
O\!\big(\mu^{7/2}\log\mu\cdot K_P(c)^2\big)\;\Phi(1)^2 .$$
*In the normalisation of `h1-mean-value.md` (4.3) — converting $\Phi(1)^2\asymp c(1-\Lambda_4)$
and $1-\chi_2=\tfrac12(1-\Lambda_4)(1+o(1))$ exactly as Prop. 4.1 already does, and no
more than it does — this is $\Xi(\mu)(1-\chi_2)$ with*
$$\Xi(\mu)\;=\;O\!\big(\mu^{9/2}\log\mu\cdot\log^2c\big)\;=\;O\!\big(\mu^{9/2}\log^3\mu\big),$$
*using $K_P=O(\log c)$. $\Xi$ is polynomial, hence subexponential, so Prop. 4.1's
conclusion stands:* $\limsup_{\mu\to\infty}\mu^{-1}\log s(\mu)\le-4\pi$ *modulo* **(H0)
alone**, *and with it the paper's gap G5.*

Four things about Corollary 4.5 that should not be over-read.

- **This is (4.3), not (H1) as §0 writes it.** (H1) asks for
  $\sum_\rho|F(s_\rho)|^2\le\Theta\|r\|^2$; §1 of `h1-mean-value.md` proves that no such
  bound can exist, since point evaluation of a Hardy-class function on the boundary is
  unbounded. (4.3) is the statement that replaced it and is the one Cor. `cor:upper`
  consumes. **H1's role is discharged; H1 as literally written is not proved and will
  not be.** Anyone quoting this note should quote (4.3).

- The conversion in the last step is the *only* place §7's observed endpoint identity
  enters, and it enters exactly where `h1-mean-value.md` Prop. 4.1 already put it. The
  theorem itself is stated against $\Phi(1)^2$ and is free of it.
- $(1-\chi_2)$ appears on the right-hand side; no lower bound on $s(\mu)$ appears
  anywhere. §7.
- **(H0) is untouched.** It is a mean value of $|\zeta(\tfrac12+it)|^2$ against an
  explicit weight, it is the other half of the paper's G6, and it is item Q4. Nothing
  here bears on it.

---

## 5. What it costs, and why the cost is where it is

| | source | cost |
|---|---|---|
| discarding the zeros above $T_*$ | Lemma 4.1 + (Q3.3) | $\log T_*=4\pi\mu+O(\log\mu)$ |
| the $\log^3$ weight, frozen | Lemma 4.2 | $\log^3(4+T_*)=O(\mu^{3})$ |
| the $\sigma$ edge, cut at $\eta_*$ | Thm 4.4 | $\tfrac\lambda2\log\frac1{2\eta_*}=O(\mu^{1/2}\log\mu)$ |
| (P)'s constant | `dilate-sum.md` Thm 5.1 | $K_P^2=O(\log^2c)$ |
| $\Phi(1)^2\to(1-\chi_2)$ | §7 of `h1-mean-value.md`, observed | $O(\mu)$ |

**$\mu^3$ is the whole cost, and it comes from the target's own size.** $T_*$ cannot be
reduced: the discarded zeros contribute $\asymp1/T_*$ and the target is
$\asymp e^{-4\pi\mu}$, so $\log T_*\ge4\pi\mu$ is forced by Fuchs. Hence
$\log^3(4+T_*)\asymp\mu^3$ is forced *on this route*, and any improvement must avoid
discarding zeros by height at all.

**A zero-density estimate is not the way out** — checked rather than assumed. Replacing
(ZFR) by $N(1-\eta_0,T)\ll T^{3\eta_0}\log^5T$ (Ingham) in Lemma 4.1 lets the discarded
set be $\{\eta_\rho\le\eta_0\}$ instead of $\{|\gamma_\rho|>T_*\}$; partial summation
gives $\sum\gamma^{-2}\ll e^{3c_0-2c_0/\eta_0}(c_0/\eta_0)^5$, and requiring this to be
$\le\Phi(1)^2\asymp e^{-4\pi\mu}$ forces $\eta_0\le c_0/(2\pi\mu)$ — better than
$\eta_*\asymp c_0/(8\pi\mu)$ by a factor $4$, i.e. by a constant. The exponent does not
move.

**What would move it** is a bound on $\int_{|t|\asymp X}|F(t+i\sigma)|^2dt$ localised in
$X$, which is what Prop. 2.2 would give and what (P′) blocks. So the two halves of this
note are the same question seen twice: the $\mu^3$ is the price of not having a
derivative dilate-sum lemma. That is Q3′ in §8, and **nothing downstream needs it**.

---

## 6. Numerics — what was measured, and what it can and cannot do

`verify_q3.py`, arbitrary precision (mpmath), 120 digits in CHECKs 0–1, 80 in CHECK 2,
25–60 elsewhere. Runtime 84 s. Every prolate value used is **on band**: (1.1) makes the
spill a finite sum of values of $\Phi$ on $[0,1]$, computed from the Legendre/Bouwkamp
series, so no spherical-Bessel evaluation occurs and the `verify_h1.sph_j_all` sign
defect (mg-9d43 §"A defect found in this note's own apparatus") cannot reach any number
here.

| check | what it establishes | verdict |
|---|---|---|
| 0 | $\Phi(0)$ and $\int_{-1}^1\Phi$ vanish to $10^{-121}$; $\Phi(1)\neq0$; $\Phi(1)^2/(1-\Lambda_4)=7.08\to35.13$ over $c=4\pi\to16\pi$ | the vector is admissible and the spill is discontinuous |
| 1 | measured jump of $R$ at $t=N/\mu$ vs. $|\Phi(1)|N^{-1/2}$: **ratio $1.0$ at all 24 cells**; $|[R]|/|R|\in[0.71,1.59]$ | **§3's premise is false**, and the jumps are the function |
| 2 | $|A'|/(\mu|\Phi(1)|)\in[0.02,26]$; $\|\Phi'\|_\infty/|\Phi(1)|=1.3\!\times\!10^2\to1.3\!\times\!10^{17}$ | $|R'|\asymp\mu t|R|$; the provable substitute for (P′) is exponential |
| 3 | $\int_\eta^{1/2}de/e$ vs $\int_\eta^{1/2}de/e^4$; and $\log^3(3+T_*)$, $\eta_*$, $\log(1/2\eta_*)$ at $\mu=2,5,12,50$ | arithmetic only: the two flags multiply, and the repair's cost is poly |
| 4 | $(1/T)\int_T^{2T}|\zeta(\eta+it)|^2$ vs the classical prediction: meas/pred $\in[0.96,1.03]$, local exponent $\to1-2\eta$ from above | supports the *observed* tail claim of §3.2 |
| 5 | $V_*\in[1.52,1.73]$ and $\|\Phi\|_\infty\in[1.12,1.67]$ for $\mu=2,\dots,8$ | Lemma 4.1's input is bounded, not merely poly |

**What the numerics cannot do.** CHECK 1 is a measurement at finitely many $(c,N)$; the
jump structure is *proved* in Cor. 1.2 and the table is a check on the proof, not its
substance. CHECK 2's suprema are grid-limited and therefore under-report. CHECK 4 is
about $\zeta$, not about $F$: the step from the mean square of $\zeta$ to the tail of
$|F|$ is the observed part of §3.2 and is **not** measured here. CHECK 3 contains no
zeta and no prolate function at all — it is arithmetic laid out so the exponent claim can
be checked by inspection.

---

## 7. The house rule, applied to this note

> **Is any statement in this note false for $-W_\lambda$?**

| item | under $-W_\lambda$ | verdict |
|---|---|---|
| 1. Cor. 1.2, the jump structure of the spill | a statement about $\operatorname{supp}\phi$ and $\Phi(1)$ | **sign-blind** |
| 2. Prop. 2.2 and (P′) | about $\Phi$ and $\Phi'$ on $[0,1]$ | **sign-blind** |
| 3. Obs. 3.1, the divergence of the flagged ordering | about $|F|^2$ and a zero-free region | **sign-blind** |
| 4. Lemma 4.1, the high zeros | $|\mathcal F_\mu g|$ is a modulus | **sign-blind** |
| 5. Lemma 4.3, $\Phi_n(1)^2\ge(1-\Lambda_n)/2K_1^2$ | a *lower* bound — on a **concentration defect**, not on $s$ | **sign-blind** |
| 6. Thm 4.4 / Cor. 4.5, (4.3) and the $-4\pi$ bound modulo (H0) | $QW_\lambda$ negates; an upper bound on $|s|$ stays an upper bound on $|{-s}|$ | **sign-blind as a magnitude claim** |

**Every item is sign-blind, and that is the correct answer.** Row 5 deserves the extra
sentence because it is the only lower bound in the note and lower bounds are where this
project has agreed to be suspicious: $1-\Lambda_n$ is a prolate concentration defect
whose two-sided asymptotic is Fuchs' theorem from 1964, it is available for
$\pm W_\lambda$ alike, and it says nothing whatever about the sign of the Weil form.
The RH-equivalent lower bound is on $s(\mu)$, a different object, and nothing here
approaches it. `prolate-rate.md` §7 and `h1-mean-value.md` §8 are right about that and
this note found nothing that disturbs them.

---

## 8. Open — what Q3 does not close

| # | item | status |
|---|---|---|
| **Q3′** | Bring $\Xi$ below $\mu^{9/2}$. §5 shows the $\mu^3$ is $\log^3T_*$ with $T_*$ forced by Fuchs, and that a zero-density estimate buys only a constant. The route that would work is a $t$-localised bound on $\int|F(t+i\sigma)|^2dt$, i.e. Prop. 2.2, i.e. (P′) | **open; nothing downstream needs it** |
| **(P′)** | $\big|\frac{d}{dt}[\lambda\sqrt t\,R(t)]\big|\le\mu K_D(c)|\Phi(1)|$ with $K_D$ subexponential — a dilate-sum bound for $x\Phi'(x)$, of exactly Q2's type. Measured true with $K_D\in[0.02,26]$; the only proved bound is $K_D=\|\Phi'\|_\infty/|\Phi(1)|\asymp e^{c}$ | **open, and it is a lemma, not bookkeeping** |
| **Q4/(H0)** | $\|g\|^2$ bounded below. Untouched here, by design | **open, unchanged** |
| **Q5** | The endpoint identity $\Phi_n(1)^2=c(1-\Lambda_n)(1-\frac{2n+1}{4c}+\dots)$. **Half of it is now proved**: Lemma 4.3 gives $\Phi_n(1)^2\ge(1-\Lambda_n)/(2K_1^2\Lambda_n)$, and the reverse inequality $\Phi_n(1)^2\ll c(1-\Lambda_n)$ follows from `dilate-sum.md` Prop. 4.1(ii) by integrating $|a_1\sin(cx)/x|^2$ against the $x^{-2}$ remainder — not written out here. The *constant* $c$ and the $-(2n+1)/4c$ correction remain observed | **partially closed; the constant is still observed only** |
| — | The internal contradiction between §3 and §4 of `h1-mean-value.md`, and the same defect in `prolate-rate.md` §6(c) | **annotated in place by this note** |

---

## 9. Provenance

**Proved here, marked *ours* at the point of use:** Lemma 1.1 and Cor. 1.2, the exact
finite on-band form of the spill and its jump structure (§1); the two refutations of §3's
first bullet (§2.1); Prop. 2.2, the weighted fractional-Sobolev bound with its
$\delta<\tfrac12-\alpha$ constraint and $\mu^{2\delta}$ constant (§2.2); the derivative
identity (2.1) and the bound $\|\Phi_n'\|_\infty\le\sqrt{c^3/\pi\Lambda_n}$ (§2.2); the
one-sidedness of the edge (§3.1); Observation 3.1 (§3.2); Lemmas 4.1, 4.2, 4.3,
Theorem 4.4 and Corollary 4.5 (§4); the density-estimate computation of §5.

**Taken from this project's own notes, quoted and not re-derived:** $\mathcal E$, the
vanishing of $\mathcal F_\mu(\mathcal E\phi)$ on $Z$, and $\mathcal F_\mu g=-\mathcal F_\mu r$
on $Z$ (`prolate-rate.md` §1 step 1, §6(a)); the admissibility conditions and the
three-mode vector (`prolate-rate.md` §2.1); Prop. 3.1, Prop. 3.2, Prop. 4.1, (4.1) and
the endpoint identity of §7 (`h1-mean-value.md` §§3,4,7); Q1 and $K_1(c)=2^{3/4}e^{E(c)}$
(`band-edge-connection.md` Thm 5.2); (P), $K_P=O(\log c)$, Prop. 4.1(ii), Prop. 6.1 and
hypothesis (C) (`dilate-sum.md` Thms 5.1, 5.2, §§4,6); $1-\chi_2=\tfrac12(1-\Lambda_4)(1+o(1))$
(`semilocal-gap.md` §5.2).

**Classical, quoted and used, not re-derived:** Riemann–von Mangoldt; the de la Vallée
Poussin zero-free region (only $c_0>0$ is used; the numerical $c_0=0.18$ in CHECK 3 is
**illustrative and is not quoted from a source I opened**); Plancherel; subharmonicity;
the Fourier decay $|\hat f(t)|\le\operatorname{Var}(f)/|t|$ for compactly supported $f$ of
bounded variation; the $\dot H^\delta$ modulus-of-continuity identity.

**Second-hand, and marked because none of these was opened here.** Fuchs' asymptotic for
$1-\Lambda_n$ — taken from `prolate-rate.md` §2, which quotes Fuchs' Theorem 1, and used
only in the *lower*-bound direction (4.3), where all that is needed is the exponent
$2c$. Ingham's zero-density estimate $N(\sigma,T)\ll T^{3(1-\sigma)/(2-\sigma)}\log^5T$
— **from memory**; it appears only in §5 and only to rule a route *out*, so a weaker or
sharper form changes nothing. Titchmarsh Thm 7.2(A) for the mean square of $\zeta$ off
the critical line — **from memory**; it appears only in the *observed* half of §3.2 and
in CHECK 4, which tests it (measured/predicted $\in[0.96,1.03]$, so the recollection is
at least arithmetically right). Hypothesis (C) of `dilate-sum.md` — re-measured here
rather than quoted (§4.3).

**The claim here that would do the most damage if wrong** is Cor. 1.2, because §2's two
refutations and §4's whole assembly rest on it. Its exposure is small: it is two lines
from the definition of $\mathcal E$ and the compact support of $\phi$, it is confirmed
against one-sided limits at 24 cells to every printed digit, it agrees with an
independent derivation through `dilate-sum.md` Prop. 6.1, and it agrees with
`h1-mean-value.md` §4's own sawtooth. **The second-most damaging** is the *observed*
half of §3.2 — that the tail of $|F|$ does not decay in $\eta$ — but nothing in §4 uses
it: it is there to show that Observation 3.1's divergence is real rather than an artefact
of a lossy bound, and if it were wrong the only casualty would be the word "divergent",
not the repair.

---

## 10. Effect on the other notes and on the paper

`h1-mean-value.md` is annotated in place at §3's two bullets and at §9's Q3 row
(HTML comments, line-count preserving) and carries one appended section, §14.
`prolate-rate.md` §6(c) is annotated at the sentence *"smooth on $(0,\lambda^{-1})$ but
has a jump at the endpoint"*, which has the same defect as §3's first bullet — and whose
next clause, *"so $\mathcal F_\mu r$ decays only like $|s|^{-1}$ and the sum converges
only because the zero density is logarithmic"*, remains right, and is right for the
reason §4 makes precise.

The paper is **not** edited. If the batched pass is taken up, the changes this note
supports are:

1. **The estimate H1 was introduced to supply can be stated as a theorem** — (4.3),
   with $\Xi=O(\mu^{9/2}\log^3\mu)$ (Cor. 4.5) — leaving the $-4\pi$ upper bound
   conditional on (H0) alone. G5 and G6's first half go with it; G6's second half,
   (H0), does not. The hypothesis **as printed** (`:1242`), with its $\|r\|^2$, should <!-- mg-6467: now `:1421`, and the paper carries (4.3) in its place — Thm 7.8, §7.6. -->
   not be called proved: §1 of `h1-mean-value.md` shows that form is unattainable, and
   the paper should carry (4.3) in its place.
2. **The $-4\pi$ upper bound becomes conditional on (H0) alone.** It does not become
   unconditional, and it is still an upper bound on a magnitude: Thm `thm:boundary` and
   G10 are untouched, and the sentence saying so should stay exactly as strong as it is.
3. If §3's two bullets are ever quoted, they should be quoted with their corrections:
   the spill is a sawtooth with infinitely many jumps, and the edge is one-sided.
