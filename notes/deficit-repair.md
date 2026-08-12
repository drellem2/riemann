# The archimedean deficit against the prime repair

Work item mg-7606. Companion script:
[`verify_deficit_repair.py`](verify_deficit_repair.py) (needs `mpmath`; no
`numpy`). Continues [`semilocal-gap.md`](semilocal-gap.md) §10 (mg-555b), which
established that archimedean-only Weil positivity fails past $\mu=2.2710$ and
that the failure is an uncertainty-principle effect. This note asks the question
that leaves open: **past the threshold, how does the archimedean deficit compare
with what the primes supply?**

Everything below is in arbitrary precision. That is not caution. The quantity
that settles the competition is $\sim10^{-48}$ at $\mu=11$ against matrix entries
of order $1$ — Connes–Consani's own figure, `Spectraltriples.tex:178` — so double
precision cannot represent the answer, let alone resolve it.
[`citation-audit.md`](citation-audit.md) §6 records the same regime from the
other side: CCM compute at 200 digits.

Nothing in `start.tex` or `s3.tex` was edited. Per vision amendment 5 the
literature's definitions are used throughout: $QW_\lambda$ is one symbol, the
Weil quadratic form on test functions supported in $[\lambda^{-1},\lambda]$, and
it contains the primes $p\le\lambda^2$. There is no operator $Q$.

---

## Bottom line

**1. The archimedean deficit is bounded, uniformly in $\mu$, and it saturates.**
For every $\mu$,
$$\lambda_{\min}(\sigma^{\mathrm{arch}})\;\ge\;2\vartheta'(0)\;=\;\psi(\tfrac14)-\log\pi\;=\;-5.3721834192\ldots$$
so the deficit $D(\mu):=-\lambda_{\min}(\sigma^{\mathrm{arch}})$ never exceeds
$5.3721834\ldots$; and it approaches that value ($D(10^{20})=5.2834963$). This is
a **proof**, given Connes–Consani's Proposition `Hilbert` (`:289`, proved there),
and the three further ingredients are each one line — §2. Their own proof of that
proposition says $\vartheta'$ is "lower bounded" and never extracts the constant.

**So the deficit is not the growing quantity.** Whatever makes the semilocal
problem hard, it is not that the archimedean side runs away.

**2. On the archimedean bad direction the primes over-repair — but by a margin
that is closing.** With $v_{\rm arch}$ the minimiser of $\sigma^{\mathrm{arch}}$
and $R(\mu):=-\sum_pW_p(v_{\rm arch})$, one finds $R(\mu)>D(\mu)$ at every $\mu$
computed. The absolute slack $R-D$ oscillates in $0.01$–$0.05$; the *relative*
excess $R/D$ falls from $1.678$ at $\mu=3$ to $1.015$ at $\mu=20$. So the primes
have room on this direction, and the room is closing. §3.

**3. But positivity is not decided there, and on the direction where it is
decided the signs are the other way round.** The full form's own bottom
eigenvector $v_\mu$ is *not* $v_{\rm arch}$. Splitting the Rayleigh quotient at
$v_\mu$:
$$\underbrace{\sigma^{\mathrm{arch}}(v_\mu)}_{>0}\;+\;\underbrace{\Big(-\textstyle\sum_pW_p(v_\mu)\Big)}_{<0}\;=\;s(\mu)>0 .$$
The archimedean part is the **credit** and the primes are the **debit** — the
deficit/repair picture with its signs reversed. §4.

**4. The two halves are each $\approx0.025\log\mu$ and they cancel at rate
$4\pi$.** Fitting $\log_{10}s(\mu)=-A\mu+B\log_{10}\mu+D$ over $\mu=5,\dots,12$
gives $A=5.4635\pm0.052$, against
$$\frac{4\pi}{\log10}=5.4575054\ldots$$
— consistent within $0.12$ standard errors. The error bar is $\sim1\%$, so this is
consistency and not a three-digit measurement of $4\pi$. The constant $4\pi$ is $2c/\mu$ at Slepian
time–bandwidth $c=2\pi\lambda^2=2\pi\mu$, which is Connes–Consani's *own* prolate
parameter (`:184`). They plot $\log s$ against $\mu$ and call the behaviour
"exponential" (`:645`); **no rate is given there or anywhere else in the paper.**
§5.

**5. The shape of the balance, which is what the ticket asked for.** A semilocal
positivity theorem must establish that two quantities of size
$\approx0.025\log\mu$ agree to
$$\frac{4\pi}{\log10}\,\mu\;-\;B\log_{10}\mu\;-\;D\;+\;\log_{10}(0.025\log\mu)\;\approx\;5.46\,\mu \quad\text{decimal digits,}$$
and agree *with the correct sign*. Measured: $15.6$ digits at $\mu=5$ rising to
$52.0$ at $\mu=12$ — an average of $5.21$ digits per unit of $\mu$ across that
range, the leading rate being $5.46$ once the $B\log_{10}\mu$ term is separated
out. **No argument that controls either side to within a fixed relative error, or
to within any fixed power of $\mu$, can produce this.** §6.

**6. Every prime power below $\mu$ is load-bearing, quantified.** Omit any single
$p^m<\mu$ and the form goes negative by $0.10$ to $0.84$ — **fifty-three orders of
magnitude** above the $5.5\times10^{-54}$ that survives when all are present.
Connes–Consani display this graphically and only up to $\lambda^2\sim7$
(`:576`–`:600`); §4.3 gives numbers, at $\mu=12$.

**Which outcome of the ticket is this?** Principally **(1) — they balance,
tightly** — with (2) true in a strict but weakening sense on the archimedean bad
direction alone. Outcome (3) does not occur. The content the ticket asked for is
the *shape* of the balance, and the finding is that it is not shaped the way the
question's two columns suggest: the deciding cancellation is on a different
direction, with the signs the other way round, and at a rate $4\pi$.

---

## 0. Vocabulary, and exactly what is being computed

$L=2\log\lambda=\log\mu$. Test functions have support in
$[\lambda^{-1},\lambda]$, i.e. in $[-L/2,L/2]$ after $x=\log u$.

Connes–Consani's semi-local Weil quadratic form (`Spectraltriples.tex:414`,
eq. `bombtestsum`) is $QW_\lambda(f,g)=\psi^\#(h)$ with
$h=\xi_n\star\xi_m^*+\xi_m\star\xi_n^*$ and
$\psi^\#=W_{0,2}^\#-W_{\mathbb R}^\#-\sum_pW_p^\#$. Their matrix
$\sigma=\sigma^+\oplus\sigma^-$ splits by the parity of $u\mapsto u^{-1}$; this
note works, as their sensitivity sections do, in the even sector $\sigma^+$, in
their basis (`:385`, eq. `basis`)
$$\xi_0=L^{-1/2},\qquad \xi_n=(-1)^n\sqrt{2/L}\,\cos(2\pi nx/L).$$

Four objects, all functions of $\mu$:

| symbol | definition | in words |
|---|---|---|
| $\sigma^{\mathrm{arch}}$ | $W_{0,2}-W_{\mathbb R}$ | their "archimedean contribution" (`§sectsensitive`): $QW_\lambda$ with **every** prime term dropped |
| $D(\mu)$ | $-\lambda_{\min}(\sigma^{\mathrm{arch}})$ | **the archimedean deficit**: how negative the archimedean side gets. $D>0$ exactly for $\mu>2.2710$ |
| $R(\mu)$ | $-\sum_pW_p(v_{\rm arch})$, $v_{\rm arch}$ the minimiser of $\sigma^{\mathrm{arch}}$ | **the prime repair**: what the primes supply *on the direction the archimedean side is worst* |
| $s(\mu)$ | $\lambda_{\min}\big(\sigma^{\mathrm{arch}}-\sum_pW_p\big)$ | what survives |

$D$ and $R$ are the ticket's two quantities. $s$ is the thing they are competing
to control, and §4 is the discovery that the competition between $D$ and $R$ is
not what controls it.

---

## 1. Method

### 1.1 The matrix entries are elementary — *ours*

`verify_arch_positivity.py` (mg-555b) builds $h_{nm}(t)$ by quadrature, at a cost
of $O(N^2)$ integrals. In arbitrary precision that is unaffordable. It is also
unnecessary. From Connes–Consani's Lemma (`:392`, `polarize` (i)),
$(\varphi_1\star\varphi_2^*)(t)=\int_{t-L/2}^{L/2}\varphi_1(x)\varphi_2(x-t)\,dx$,
both factors are cosines and $a_kL=2\pi k$ kills every boundary term. With
$g_0=1/\sqrt2$, $g_n=1$ $(n\ge1)$ and $a_k=2\pi k/L$:
$$h_{nm}(t)=g_ng_m\,\hat h_{nm}(t),\qquad t\in[0,L],$$
$$\hat h_{nm}(t)=\frac2\pi\,\frac{m\sin(a_mt)-n\sin(a_nt)}{n^2-m^2}\ (n\ne m),
\qquad
\hat h_{nn}(t)=\frac2L\Big[(L-t)\cos(a_nt)-\frac{\sin(a_nt)}{a_n}\Big],$$
$$\hat h_{00}(t)=\frac{4(L-t)}{L}.$$

Two consequences, and the second is the point.

- $h_{nm}(0)=2\delta_{nm}$ is now *visible* rather than checked.
- Every entry of $W_{0,2}$ and of $W_{\mathbb R}$ is a fixed linear combination
  of the $O(N)$ scalars $\int w\sin(a_ky)$, $\int w\,(L-y)\cos(a_ky)$ and their
  $W_{\mathbb R}$ analogues. So the matrix costs $O(N)$ quadratures rather than
  $O(N^2)$, and **the prime matrices cost no quadrature at all**. That factor of
  $N$ is what puts $N=100$ at $120$ digits inside a coffee break, and it is why
  this note exists in arbitrary precision at all.

Check 0 of the script validates the closed form three ways: $h_{nm}(0)=2\delta$
to $5\times10^{-51}$; the quadrature against an independent closed form for
$\int_0^L2\cosh(y/2)\sin(a_ky)\,dy$ to $10^{-50}$ at 50 digits; and the three
Connes–Consani numbers mg-555b reproduced ($0.001330$ at $\mu=2$ against their
$\sim0.00133$; the sign change at $\mu^*=2.27118$ against their $2.27$;
$5.757\times10^{-8}$ at $\mu=3$ with $p=2$ against their $<6\times10^{-8}$).

### 1.2 Truncation is variational, and it cuts one way

Restricting a quadratic form to a subspace can only *raise* its smallest
eigenvalue, so $\lambda_{\min}(N)$ decreases in $N$. Therefore:

- a **negative** truncated eigenvalue certifies a negative one for the full form.
  That is why §2 (quantities of size $10^{-2}$ to $5$) is a **verification**.
- a **positive** truncated eigenvalue is only an **upper bound**. So every $s(\mu)$
  below is an upper bound on the true one, and the honest reading is the
  *exponent*, not the mantissa. §5 shows the mantissa still moving at $N=120$
  while the exponent has settled, and says so.

### 1.3 Stability under increasing precision

The ticket's standing requirement. Same $L=\log8$, same $N=60$, three working
precisions (check 6):

| dps | $D(8)$ | $s(8)$ |
|---|---|---|
| $40$ | $0.624359994002551113$ | $5.21118021234320404\times10^{-33}$ |
| $80$ | $0.624359994002551113$ | $5.21118034929881616\times10^{-33}$ |
| $140$ | $0.624359994002551113$ | $5.21118034929881616\times10^{-33}$ |

$D$ does not move at all. $s$ is correct to eight digits at $40$ dps and stops
moving thereafter — which is the arithmetic one expects, since a quantity of size
$10^{-33}$ read off matrix entries of order $1$ has exactly $40-33=7$ digits of
room at $40$ dps. Double precision has $16-33<0$ digits of room, which is not a
loss of accuracy but an absence of any. That is the whole reason this script is
in `mpmath` and the reason `verify_arch_positivity.py`'s check 3 carried the
caveat it did.

### 1.4 Reproduction, verification, and second-hand numbers

Drawn to mg-555b's standard, and the ticket's.

- **Verifications**: §2 entirely (the deficit, and the bound it saturates); the
  Fourier-side identity of §2.1, checked to $8$ digits in the normalisation
  actually used; §3 (the repair, quantities of order $10^{-1}$).
- **Reproductions, not verifications**: every $s(\mu)$, and in particular the
  match with Connes–Consani's $2.389\times10^{-48}$ at $\mu=11$. §5 says exactly
  what part of that number is reproduced and what part is not.
- **Strongly indicated, not proved**: the identification of the decay rate as
  $4\pi$ (§5). It is a $0.11\%$ agreement between a least-squares fit and a
  constant derived from Connes–Consani's own prolate identification plus the
  classical Slepian/Fuchs asymptotic. It is not a derivation.
- **No second-hand numbers.** `Spectraltriples.tex` was downloaded from
  `arxiv.org/e-print/2106.01715` and every quoted line was read in the source;
  §8. The $2.389\times10^{-48}$ reached me through `semilocal-gap.md` §3.4 and
  was re-opened at `:178` before use, per the standing caution.

---

## 2. The archimedean deficit is bounded, and saturates — *ours*

### 2.1 The bound

Connes–Consani, Proposition `Hilbert` (`Spectraltriples.tex:289`, **proved**):
$$QW_\lambda(f,f)=\int|\widehat f(t)|^2\,\frac{2\vartheta'(t)}{2\pi}\,dt
\;+\;2\Re\big(\widehat f(\tfrac i2)\overline{\widehat f(-\tfrac i2)}\big)
\;-\sum_{1<n\le\lambda^2}\Lambda(n)\langle f\mid V(n)f\rangle .$$
The first two terms are $\sigma^{\mathrm{arch}}$. Three one-line facts:

1. **$\vartheta'$ attains its minimum at $t=0$, and this is elementary.**
   $\vartheta'(t)=\tfrac12\Re\psi(\tfrac14+\tfrac{it}2)-\tfrac12\log\pi$, and
   $\frac{d}{dt}\Re\psi(\tfrac14+\tfrac{it}2)=-\tfrac12\Im\psi'(\tfrac14+\tfrac{it}2)$.
   Now $\psi'(z)=\sum_{k\ge0}(z+k)^{-2}$, and at $z=\tfrac14+\tfrac{it}2$ each
   term has imaginary part $-t(k+\tfrac14)/|z+k|^4<0$ for $t>0$. So
   $\Im\psi'<0$, $\vartheta'$ is **strictly increasing on $t>0$**, and
   $\inf_t\vartheta'=\vartheta'(0)=-2.68609170961\ldots$ (For the record, the same
   $\vartheta'$ is negative exactly on $|t|<6.289836$ — mg-555b's constant,
   recomputed here.)
2. **On the even sector the boundary term is a square.** For real $f$ even under
   $u\mapsto u^{-1}$, $\widehat f(\tfrac i2)=\widehat f(-\tfrac i2)=\int F\cosh(x/2)\,dx$
   is real, so the term is $2\big(\int F\cosh(x/2)dx\big)^2\ge0$.
3. **Plancherel** in this normalisation: $\int|\widehat f(t)|^2dt/2\pi=\|f\|^2$.

Hence for every $\mu$ and every unit $f$ in the even sector,
$$\sigma^{\mathrm{arch}}(f,f)\;\ge\;2\vartheta'(0)\,\|f\|^2,\qquad\text{i.e.}\qquad
\boxed{\;D(\mu)\;<\;-2\vartheta'(0)\;=\;\log\pi-\psi(\tfrac14)\;=\;5.3721834192\ldots\;}$$

Facts 1–3 are proved above. What is *not* re-proved here is Proposition
`Hilbert` itself; it is proved in their paper. The normalisation is the one place
this could silently go wrong by a factor of $2$, so it is **checked and not
assumed**: check 1 of the script evaluates both sides on $f=\xi_1$, for which
$\widehat f$ is closed-form, and finds agreement to $2\times10^{-8}$ at $\mu=2$
and $1\times10^{-8}$ at $\mu=20$ (the $t$-integral converges only like
$\log t/t^2$, so its tail is added from its asymptotic form; the residual is that
tail). Plancherel is confirmed at $0.999999998$. There is no extra factor.

### 2.2 The deficit saturates the bound

| $\mu$ | $L$ | $D(\mu)$, $N=160$ |
|---|---|---|
| $3$ | $1.09861$ | $0.07397889$ |
| $5$ | $1.60944$ | $0.37270355$ |
| $11$ | $2.39790$ | $0.77466583$ |
| $20$ | $2.99573$ | $1.02682548$ |
| $10^2$ | $4.60517$ | $1.62332472$ |
| $10^3$ | $6.90776$ | $2.44603691$ |
| $10^6$ | $13.8155$ | $4.23599851$ |
| $10^9$ | $20.7233$ | $4.87322925$ |
| $10^{12}$ | $27.6310$ | $5.10422655$ |
| $10^{20}$ | $46.0517$ | $5.28349631$ |
| bound | | $5.37218341923\ldots$ |

$D$ is increasing in $\mu$ — as it must be: the supports are nested, the form is
the same form, so $\lambda_{\min}$ can only fall. Over the computed range it
grows like $\log L=\log\log\mu$; a fit gives $D\approx2.5\log\log\mu-2.33$, which
is descriptive only and is not offered as a law. The statement that stands is the
bound and the saturation.

**Why this matters more than it looks.** The natural reading of "archimedean
positivity fails past $\mu=2.271$, and the primes repair it" is that the thing to
be repaired grows without limit and the repair must grow to match. It does not.
The archimedean side is negative by at most $5.3722$, ever, on a unit vector. The
difficulty is not magnitude.

---

## 3. On the archimedean bad direction, the primes over-repair — *ours*

$D(\mu)$ is attained at some $v_{\rm arch}$. What the primes supply *there* is
$R(\mu)=-\sum_pW_p(v_{\rm arch})$. Since
$s(\mu)\le\sigma^{\mathrm{arch}}(v_{\rm arch})-\sum_pW_p(v_{\rm arch})=R-D$ and
$s>0$ under RH, positivity forces $R>D$; the question is by how much. Check 3 of
the script, $N=60$ at $40$ digits:

| $\mu$ | $D(\mu)$ | $R(\mu)$ | $R-D$ | $R/D$ |
|---|---|---|---|---|
| $3$ | $0.07393778$ | $0.12404900$ | $0.05011122$ | $1.6777$ |
| $4$ | $0.23972403$ | $0.26633090$ | $0.02660687$ | $1.1110$ |
| $5$ | $0.37262595$ | $0.41590755$ | $0.04328161$ | $1.1162$ |
| $6$ | $0.47506903$ | $0.48993904$ | $0.01487000$ | $1.0313$ |
| $8$ | $0.62435999$ | $0.64978693$ | $0.02542693$ | $1.0407$ |
| $10$ | $0.73104987$ | $0.74250899$ | $0.01145912$ | $1.0157$ |
| $12$ | $0.81337243$ | $0.83273410$ | $0.01936168$ | $1.0238$ |
| $16$ | $0.93617534$ | $0.94601094$ | $0.00983560$ | $1.0105$ |
| $20$ | $1.02672849$ | $1.04224568$ | $0.01551719$ | $1.0151$ |

$R>D$ at every $\mu$ computed, so the primes over-repair here. But read the last
column rather than the fourth: **the relative excess is closing**, from $1.678$ at
$\mu=3$ to $1.015$ at $\mu=20$, and the absolute slack neither grows nor decays
cleanly — it oscillates in $0.010$–$0.050$, with the local minima at $\mu=6,10,16$
and maxima just after a new prime power enters.

So on this direction the ticket's outcome (2) holds strictly — the repair does
outgrow the deficit — but only just, and by less and less. If the semilocal
question were the question of §0's two columns it would be answered in the
affirmative, on a margin of $1.5\%$ at $\mu=20$ and falling.

It is not that question, and §4 is why.

---

## 4. The balance is on a third direction, and its signs are reversed — *ours*

### 4.1 The measurement

The bottom eigenvector $v_\mu$ of the *full* form is not $v_{\rm arch}$. Splitting
the Rayleigh quotient there, at $N=100$ and $120$ digits:

| $\mu$ | $\sigma^{\mathrm{arch}}(v_\mu)$ | $-\sum_pW_p(v_\mu)$ | $s(\mu)$ | $\log_{10}s$ | digits |
|---|---|---|---|---|---|
| $5$ | $+0.03958194$ | $-0.03958194$ | $1.005\times10^{-17}$ | $-16.998$ | $15.60$ |
| $6$ | $+0.04538231$ | $-0.04538231$ | $8.211\times10^{-23}$ | $-22.086$ | $20.74$ |
| $7$ | $+0.04959492$ | $-0.04959492$ | $7.731\times10^{-28}$ | $-27.112$ | $25.81$ |
| $8$ | $+0.05273312$ | $-0.05273312$ | $4.581\times10^{-33}$ | $-32.339$ | $31.02$ |
| $9$ | $+0.05520046$ | $-0.05520046$ | $3.135\times10^{-38}$ | $-37.504$ | $36.25$ |
| $10$ | $+0.05719477$ | $-0.05719477$ | $1.784\times10^{-43}$ | $-42.749$ | $41.51$ |
| $11$ | $+0.05882638$ | $-0.05882638$ | $1.226\times10^{-48}$ | $-47.912$ | $46.68$ |
| $12$ | $+0.06018733$ | $-0.06018733$ | $5.531\times10^{-54}$ | $-53.257$ | $52.04$ |

"digits" is $\log_{10}\big(|\sigma^{\mathrm{arch}}(v_\mu)|/s(\mu)\big)$: the
number of decimal digits to which the two halves agree.

### 4.2 What to read off it

**The signs are the other way round.** On the direction that decides positivity
the archimedean contribution is **positive** and the prime contribution is
**negative**. The phrase "the primes repair the archimedean deficit" describes
§3's direction and is *false* on this one, where the primes are the entire threat
and the archimedean side is what holds the form up.

This is not a contradiction: they are different vectors and both statements are
true of their own. But it means the ticket's two columns are not the two sides of
the balance, and it explains why the comfortable margin of §3 buys nothing.

**Both halves are small and grow slowly.** $|\sigma^{\mathrm{arch}}(v_\mu)|$ is
$0.0396$ at $\mu=5$ and $0.0602$ at $\mu=12$; divided by $\log\mu$ it sits between
$0.0242$ and $0.0255$ across the whole range, so it is $\approx0.025\log\mu$. Both
halves are two orders below the deficit $D$ of §2 — the near-radical direction is
not where the archimedean form is bad, it is where it is *nearly flat*.

**The reply to mg-0bd7, which asked exactly this.** pm-riemann's mail on
`semilocal-gap.md` §11 asked whether the deficit and the repair scale alike or
are of different kind, given that at a single finite place the angle operator is
degenerate (Burnol 1999). The answer this note can give: **they do not compete at
all.** The deficit is bounded and saturates (§2); the repair on that direction
exceeds it with a growing margin (§3); and the near-cancellation that decides
positivity is a *third* pair of quantities, on a *third* direction, two orders
smaller, with the signs reversed. Whatever the finite places are contributing, it
is not a term of the same kind fighting the archimedean deficit to a draw.

### 4.3 Every prime power is load-bearing

Connes–Consani show graphically, up to $\lambda^2\sim7$, that "when $\lambda^2$
grows past a prime power and one ignores its contribution, the quadratic form
$QW_\lambda$ fails to remain positive" (`:177`, figures at `:576`–`:600`). Here
that is a number. At $\mu=12$, $N=60$, $70$ digits, dropping one prime power at a
time:

| omitted | $\lambda_{\min}$ |
|---|---|
| none | $+9.19\times10^{-54}$ |
| $2$ | $-0.71226224$ |
| $3$ | $-0.83688017$ |
| $4$ | $-0.34656987$ |
| $5$ | $-0.71772943$ |
| $7$ | $-0.59699566$ |
| $8$ | $-0.17682307$ |
| $9$ | $-0.24427816$ |
| $11$ | $-0.10260697$ |

(The "none" row is the $N=60$ upper bound; §4.1's $N=100$ value at $\mu=12$ is
$5.53\times10^{-54}$, consistent — a looser truncation gives a larger bound.)

Omit any single $p^m<\mu$ and the form goes negative by $0.10$ to $0.84$ —
**fifty-three orders of magnitude** above the $5.5\times10^{-54}$ that survives
when all are present. There is no dominant prime, no ordering by size ($3$ costs
more than $2$; $11$, the largest, costs least but still $10^{52}$ times the
residue), and no tail that can be estimated crudely at any cutoff below $\mu$.

---

## 5. The law: the rate is $4\pi$ — *ours*

Connes–Consani state the decay as a **figure**:

> "Pushing the computations further and increasing the precision, one obtains an
> estimate of the size of the smallest eigenvalue $s(L)$ of the even matrix, as a
> function of $\mu=\exp L$. One finds an exponential behavior, as reported in
> Figures `testeven6` and `testeven7`, where $\log s(L)$ is plotted in terms of
> $\mu=\exp L$." (`:645`)

**No rate is given there or anywhere else in the paper.** The ticket's standing
instruction is to prefer an exhibit to a figure; here the missing object is a
constant, so:

Least squares on §4.1, $\mu=5,\dots,12$:
$$\log_{10}s(\mu)=-A\mu+B\log_{10}\mu+D,\qquad A=5.4635,\ B=5.322,\ D=6.589,$$
with residual rms $0.042$ and max $|{\rm residual}|=0.056$ in $\log_{10}$ units,
and standard errors $A\pm0.052$, $B\pm0.96$, $D\pm0.44$. (The two-parameter fit
$-A\mu+D$ gives $A=5.179$ and visibly worse residuals; the $\log\mu$ term is
real.) Against this:

**The prediction.** Connes–Consani identify the near-radical vectors as prolate:
$\psi_{m,\lambda}(x)=\mathit{PS}_{2m,0}(2\pi\lambda^2,x/\lambda)$ (`:184`), i.e.
Slepian time–bandwidth $c=2\pi\lambda^2=2\pi\mu$, and the smallness of $s$ as the
smallness of the angle-operator eigenvalues, which are the prolate concentration
defects $1-\Lambda_m(c)$. The classical Slepian/Fuchs asymptotic
$1-\Lambda_0(c)\sim4\sqrt{\pi c}\,e^{-2c}$ then gives a rate $2c/\mu=4\pi$:
$$\frac{4\pi}{\log10}=5.4575054\ldots$$

$A-4\pi/\log10 = +0.0060$, against a standard error on $A$ of $0.052$: **consistent
within $0.12\sigma$.** Two caveats, both against over-reading that.

- The error bar is $\sim1\%$, not $0.1\%$. Over so short a grid $\mu$ and
  $\log_{10}\mu$ are $0.992$ collinear, so $A$ and $B$ are strongly correlated and
  the individual $B=5.32\pm0.96$ is barely determined at all. What the fit
  measures well is $A$; what it does not measure is $A$ to three digits.
- The truncation bias runs the *wrong way for comfort*. $s(N)$ is an upper bound
  and the bound is looser at larger $\mu$, so the measured $A$ is an
  **under**-estimate: the true rate is if anything *above* $4\pi/\log10$, not at
  it. The agreement is therefore evidence for the identification and not a
  confirmation of it, and settling the difference needs $s$ converged in $N$
  (open item T3).

**Status of this identification.** Indicated, not proved, and the wording
matters. The fit is over eight points at one truncation level, spanning a factor
$2.4$ in $\mu$; the fitted prefactor $B=5.32\pm0.96$ does *not* match the
$\tfrac12$ that $\sqrt c$ would give, so the subleading structure is not the
naive one and the argument above is a heuristic for the leading rate only.

What is claimed is exactly this: **the decay Connes–Consani plot without naming
is exponential in $\mu$ at a rate consistent with $4\pi$, which is the Slepian
rate at their own prolate parameter $c=2\pi\mu$.** What is not claimed is that
the rate *is* $4\pi$; T2 and T3 in §9 are the two things that would settle it.

> **NARROWED 2026-08-12 by mg-fcb8 — [`prolate-rate.md`](prolate-rate.md).
> Three corrections, and the identification comes out stronger, not weaker.**
>
> 1. **The index is 4, not 0.** The near-radical vector for the smallest *even*
>    eigenvalue is Connes–Consani's $\phi_2=\psi_2\psi_0(0)-\psi_0\psi_2(0)$
>    (`Spectraltriples.tex:744`), and their $\psi_2=\mathit{PS}_{4,0}$. Index 4
>    is forced by $\mathcal E$'s domain $f(0)=\widehat f(0)=0$ together with the
>    finite-Fourier phase — mg-aedf's mode-4 selection, in the prolate rather
>    than the Hermite limit. Measured: $s/(1-\Lambda_0)$ runs $5\times10^8$ to
>    $2.8\times10^{10}$ and *grows* by a factor $56$; $s/(1-\chi_2)$, with
>    $\chi_2=\sqrt{\Lambda_4}$, runs $7.6$ to $13.0$.
> 2. **"No rate is given there or anywhere else in the paper" is true of
>    arXiv:2106.01715 and false of the survey.** Connes, `rhready.tex:1149`
>    (Feb 2026), states $1-\chi_2\sim\frac{2^{14}\sqrt2\,\pi^5}{3}\mu^{9/2}
>    e^{-4\pi\mu}$ from Fuchs Thm 1, and reports a "striking similarity" between
>    $\epsilon(\lambda)$ and $1-\chi_2$ — as a figure, with no constant. The
>    rate, the $9/2$ and the constant are his; the quantitative confrontation
>    with $s(\mu)$ is ours.
> 3. **The rate cannot discriminate.** Fuchs' factor $e^{-2c}$ does not depend
>    on the index, so *every* prolate index passes the $0.12\sigma$ test. What
>    discriminates is the power $n+\tfrac12$ and the constant — and at index 4
>    all three fitted parameters land within $1\sigma$, with none of them free.
>
> One anchor correction while here: `:184` above should be `:191`. The prolate
> identification $\psi_{m,\lambda}=\mathit{PS}_{2m,0}(2\pi\lambda^2,x/\lambda)$
> is at `Spectraltriples.tex:191`, re-read on this pass; `:189` in §6 is right.

### 5.1 Their one published number

At $\mu=11$ the smallest positive eigenvalue is $2.389\times10^{-48}$
(`:178`, read in the source). N-convergence here, at 100 digits:

| $N$ | $s(11)$ | $\log_{10}$ |
|---|---|---|
| $50$ | $2.389468\times10^{-48}$ | $-47.6217$ |
| $80$ | $1.370549\times10^{-48}$ | $-47.8631$ |
| $100$ | $1.225866\times10^{-48}$ | $-47.9116$ |
| $120$ | $1.120712\times10^{-48}$ | $-47.9505$ |

(the $N=100$ row is §4.1's, at $120$ digits; the others are check 5's, at $100$)

The **exponent** is settled at $-48$ and reproduces their number. The
**mantissa** is not converged — it is still falling at $N=120$ — so this is not a
verification of $2.389$.

Note what $N=50$ does: it lands on $2.3894\ldots$, their four printed digits.
Either that is their truncation level or it is a coincidence. **The paper never
says which $N$ they used** — `:210` says only that the eigenvalues are computed
for "indices $n$ and $m$ whose absolute values are $\le N$" — so this cannot be
settled from the paper, and it is recorded here as unresolved rather than claimed
either way. It is also worth noting that on their own log-scale figures the
entire $N=50\to120$ drift is a change of $0.33$ against an ordinate of $-48$: it
is invisible, which is consistent with their remark at `:210` that increasing $N$
"does not alter substantially the lower part of the spectrum" without that remark
being evidence that the mantissa has converged.

---

## 6. What a semilocal theorem would have to prove

This is the sharpening the README asks for, and it is the point of the note.

Combining §4 and §5: a proof of $QW_\lambda\ge0$ for the semilocal form must
establish that, on the near-radical direction,
$$\sigma^{\mathrm{arch}}(v_\mu)\;=\;\Big(\sum_pW_p\Big)(v_\mu)\;+\;s(\mu),
\qquad \sigma^{\mathrm{arch}}(v_\mu)\approx0.025\log\mu,\qquad
s(\mu)\approx10^{6.6}\,\mu^{5.3}\,e^{-4\pi\mu},$$
with $s>0$. In words: **two computable quantities of size $\approx0.025\log\mu$,
one archimedean and one a finite sum over $p^m<\mu$, agree to about $5.2$ decimal
digits per unit of $\mu$ over the computed range — at a rate consistent with
$4\pi/\log10=5.4575$ — and the sign of the discrepancy is always the same one.**

Three consequences, and each of them is a constraint on method, not a
restatement of difficulty.

1. **No fixed-relative-error argument can work.** Any bound on either side that
   is accurate to a fixed relative error $\varepsilon$, or to a fixed power
   $\mu^{-k}$, loses at $\mu\gtrsim(k\log\mu+\log(1/\varepsilon))/(4\pi/\log10)$.
   The required relative accuracy is $e^{-4\pi\mu}/(0.025\log\mu)$ — it is not a
   constant, and it is not polynomial.
2. **No prime can be dropped and no tail estimated.** §4.3: each $p^m<\mu$
   individually carries $0.10$–$0.84$, fifty-three orders above the residue, and
   the cost is not ordered by the size of the prime. The sum is not dominated by
   its head, and the standard move of controlling $\sum_{p>P}$ crudely is
   unavailable at every $P<\mu$.
3. **The difficulty is not magnitude but cancellation, and §2 is what makes that
   precise.** The deficit is bounded by $5.3722$ for all $\mu$ — a fixed, small,
   explicit constant. Nothing on the archimedean side diverges. What has to be
   proved is an exact-to-$e^{-4\pi\mu}$ agreement between two bounded quantities,
   which is a statement about the arithmetic of the primes and not about the size
   of anything.

That is also, read the other way, an explanation of *why* Connes–Consani's
near-radical construction is the right conceptual object: the near-radical is
exactly the subspace on which the two sides are forced into this agreement, and
its dimension $1+\nu(\mu)\sim2\mu$ (`:189`) is the number of independent such
agreements $\mu$ demands at once.

---

## 7. The house rule, applied to this note

> **Is any statement in this note false for $-W_\lambda$?**

Taking each bottom-line item under $\sigma\mapsto-\sigma$:

| item | under $-W_\lambda$ | verdict |
|---|---|---|
| 1. $\lambda_{\min}(\sigma^{\mathrm{arch}})\ge2\vartheta'(0)$ | becomes $\lambda_{\max}(\sigma^{\mathrm{arch}})\le-2\vartheta'(0)=5.372$. Measured here: $\lambda_{\max}=5.4855$ at $\mu=2$, $N=160$, and $11.139$ at $\mu=100$, $N=80$ — and it increases without bound in $N$, since their form takes values in $(-\infty,+\infty]$ (`:289`) | **FALSE for $-W$**, and not marginally. Sign-sensitive |
| 2. $R(\mu)>D(\mu)$ | the primes would have to *reduce* an archimedean excess and instead increase it | **FALSE for $-W$** |
| 3. $\sigma^{\mathrm{arch}}(v_\mu)>0$, $-\sum W_p(v_\mu)<0$, sum $>0$ | all three signs flip; the sum is $-s(\mu)<0$ | **FALSE for $-W$** |
| 4. the rate $4\pi$ | $|s|$ is unchanged | **sign-blind.** It is a statement about magnitude only, and is admissible only as the quantitative half of item 3 |
| 5. the digit count | likewise magnitude | **sign-blind**, same caveat |
| 6. every prime power load-bearing | "the form goes negative" flips to "goes positive" | **FALSE for $-W$** |

Four of the six are false under $W\mapsto-W$, and the two that are not are
explicitly the magnitudes attached to item 3 rather than free-standing claims.
This note is not a dictionary. The mechanism it turns on — a quadratic form,
its bottom eigenvector, and the sign of a Rayleigh quotient there — is the one
the house rule was written to demand.

**One warning to myself, in the same spirit as `semilocal-gap.md` §3.2's.** The
sentence "the two halves agree to $5.46\mu$ digits" is by itself invariant under
$W\mapsto-W$. It is only sign-bearing as part of "…and the archimedean half is
the positive one". Do not quote the digit count on its own as if it said
something about the direction of the inequality.

---

## 8. Provenance

To the standard of `citation-audit.md` §9.

**Read as primary source**, from arXiv LaTeX downloaded on 2026-08-12 from
`arxiv.org/e-print/2106.01715`, file `Spectraltriples.tex`:

- `:160`–`:215` in full — the introduction's statement of $QW_\lambda$, the
  $2.389\times10^{-48}$ at `:178`, the description of the near-radical and the
  prolate vectors at `:184`–`:190`, and the matrix/truncation description at
  `:210`;
- Proposition `Hilbert` and its proof, `:289`–`:300`;
- `§sectsmall`, `:644`–`:695` — the "exponential behavior" sentence at `:645`,
  the small-eigenvalue figures, and the eigenvector figures;
- the section opening of `riemweilexpl`, `:696`–`:702`.

Lines `:385`, `:392`, `:414`, `:532`, `:542`–`:600` are used as
`verify_arch_positivity.py` (mg-555b) uses them and were re-checked at statement
level on this pass; I did not re-read the surrounding proofs.

**Derived here, not taken from any source** — each marked *ours* at the point of
use: the closed form for $h_{nm}$ (§1.1); the uniform bound
$D(\mu)<-2\vartheta'(0)$ and the monotonicity of $\vartheta'$ that it needs
(§2.1); the saturation table (§2.2); the over-repair on $v_{\rm arch}$ (§3); the
sign reversal on the near-radical direction (§4.2); the numerical
load-bearing-ness of each prime power (§4.3); the rate $4\pi$ (§5); the
obstruction statement (§6).

**The claim in this note that would do the most damage if wrong** is §2.1's
bound, because it is the only one stated as a proof and everything in §6 item 3
leans on it. Its exposure is the normalisation of Proposition `Hilbert` — a
factor of $2$ there doubles the constant. That is exactly why check 1 of the
script exists and why it is a check on the *matrix this script builds*, not on
the formula as printed. Its second exposure is that Proposition `Hilbert` is
taken on trust from their paper; I did not verify its proof.

**Rests on secondary reading:** the Slepian/Fuchs asymptotic
$1-\Lambda_0(c)\sim4\sqrt{\pi c}\,e^{-2c}$ used in §5 is quoted from the standard
prolate literature as recorded in `s3-reduction-audit.md`, not re-derived and not
checked against Slepian's papers on this pass. It enters only the *interpretation*
of the fitted constant $A$, never its measurement, and §5 marks the
identification as indicated rather than proved.

> **mg-fcb8: and it is quoted at the wrong index.** Fuchs at index $n$ is
> $4\sqrt\pi\,8^nc^{n+1/2}e^{-2c}/n!$, and the index that governs $s$ is $n=4$.
> The general-$n$ form is now checked against an arbitrary-precision computation
> of $\Lambda_0,\Lambda_2,\Lambda_4$ — `verify_prolate_rate.py` check 1 — and
> against Connes' independently printed constant, which is exactly $\tfrac12$
> Fuchs at $n=4$, $c=2\pi\mu$. Fuchs' paper itself is still not read.

---

## 9. Open, and left open deliberately

| # | item | why it is open |
|---|---|---|
| **T1** | Is $D(\mu)\to-2\vartheta'(0)$ exactly, or to something strictly smaller? | The saturation is numerical to $\mu=10^{20}$ and the gap is still $0.089$. The limit argument (concentrate $\widehat f$ at $t=0$ while killing the boundary term with an $O(e^{-L/4})$ correction near $\pm L/2$) is sketched and not written out. It would make §2 a clean two-sided theorem |
| **T2** | ~~Prove the rate $4\pi$~~ — **SPLIT by mg-fcb8** | The route named here was right: `prolate-rate.md` §6 evaluates $QW_\lambda$ on the prolate vector and gets an *identity*, $QW_\lambda(g)=\sum_Z\lvert\mathcal F_\mu r\rvert^2$ with $r$ the part of $\mathcal E\phi$ falling outside $[\lambda^{-1},\lambda]$. But the goal is unreachable as stated. A rate is two-sided, and its lower half is a positive lower bound on $\lambda_{\min}(QW_\lambda)$ for every $\lambda$ — which **is equivalent to RH** (`rhready.tex:1145`). What remains open is **T2a**: the mean-value bound over the zeros that gives the upper half |
| **T3** | ~~The $B=5.32$ in the fit~~ — **CLOSED by mg-fcb8** | Neither horn. The prediction was never $\tfrac12$: at the forced index the Slepian prefactor is $n+\tfrac12=9/2$, stated independently by Connes at `rhready.tex:1149`, and the fit is $0.86\sigma$ from it. This row was the index-0 hypothesis leaving its one visible mark |
| **T4** | The odd sector | Everything here is $\sigma^+$, as Connes–Consani's sensitivity sections are. They report the odd matrix behaves similarly with one fewer small eigenvalue (`:664`). Not checked here |
| **T5** | Is the sign reversal of §4.2 stable in $\mu$? | Verified for $5\le\mu\le12$. It is the load-bearing structural claim of the note and the range is short |

`semilocal-gap.md` §8's open list is untouched by this note except that **S2 is
now quantified rather than merely settled**: the failure of archimedean-only
positivity past $\mu=2.2710$ is bounded in size for all $\mu$ (§2), which is more
than "it fails".
