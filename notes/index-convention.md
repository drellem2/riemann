# What $h_{4,\lambda}$ means — settling audit item U6

Work item mg-9433. Companion script:
[`verify_index_convention.py`](verify_index_convention.py) (needs `mpmath`; no numpy).
Answers `citation-audit.md` §7 item U6, and closes the falsifier of
`s3-reduction-audit.md:64-75`.

Nothing in `start.tex` or `s3.tex` was edited. References are by line.

---

## Bottom line

**The corpus's $h_{4,\lambda}$ is prolate index 4.** mg-aedf's numerics used the right
object and **every constant in `s3-reduction-audit.md` stands** — $8/11$, $3/11$,
$\sqrt{3/8}$, $\pi^{-1/4}$, $3/512\,c^{-4}$, and the signed formula at `:274-278`.
No correction is required.

But the route by which that was established is **not** the one this work item
proposed, and the difference matters enough to lead with:

> **`start.tex:180-181` cannot settle U6, and no amount of precision changes that.**
> The identity holds *exactly* — to full working precision, at every band-limit and
> every precision tested — for **every** partner mode $m\equiv0\pmod 4$, and fails by
> four to twenty orders of magnitude for **every** $m\equiv2\pmod 4$. It carries
> exactly one bit of information, the finite-Fourier phase, and both candidate
> readings (prolate index 4 and prolate index 8) sit on the same side of it.

So the work item's premise — "there is an artifact that discriminates" — is false, and
the honest report of the numerics alone would have been *neither settled nor refuted*.
What settles U6 is documentary: the corpus's vector is **Connes–Consani–Moscovici's**
$\psi^+_\ell$ at $\ell=1$ (arXiv:2310.18423, quoted verbatim in §4 below), which is
built from **Hermite** functions $h_{4\ell}$ and $h_0$ in the full index. The corpus's
letters, both subscripts, and its phrase "the CCM choice of
coefficients" (`start.tex:147`) are that formula, transcribed. The halved index
$\psi_{m,\lambda}:=\mathrm{PS}_{2m,0}$ that raised the alarm is Connes–Consani's
labelling in a *different* paper, and the corpus is not using it.

Both papers denote the **same object**. U6 was a collision of two labels for
$\mathrm{PS}_{4,0}$, not a mathematical ambiguity, and the corpus follows the label
under which that object is called "4".

---

## 1. What was asked, and what the artifact can actually do

`citation-audit.md` §7 U6: Connes–Consani define $\psi_{m,\lambda}:=\mathrm{PS}_{2m,0}$,
so their $m$ is **half** the prolate index. mg-aedf's scripts used prolate index 4,
i.e. their $m=2$. If `start.tex:138-145` means *their* $m=4$, it is prolate index 8 and
every constant in that note changes.

Two readings, then:

| | reading A | reading B |
|---|---|---|
| $h_{4,\lambda}$ is | $\mathrm{PS}_{4,0}$ (prolate index 4) | $\mathrm{PS}_{8,0}$ (prolate index 8) |
| in Connes–Consani's labels | $\psi_{2,\lambda}$ | $\psi_{4,\lambda}$ |
| assumed by | `s3-reduction-audit.md` (mg-aedf) | nobody yet |

The proposed discriminator is `start.tex:180-181`: for the combination
$h_\lambda=\alpha h_{0,\lambda}+\beta h_{4,\lambda}$ subject to
$\widehat h_\lambda(0)=0$ (`start.tex:171`),

$$h_\lambda(0)=\alpha\,h_{0,\lambda}(0)\,\frac{\chi_4-\chi_0}{\chi_4}.$$

### Setup and arithmetic

Reconstruction as in `s3-reduction-audit.md:55-57`: band-limit $c$ (the documents'
$\lambda$), interval $[-1,1]$, concentration eigenvalues $\Lambda_n$, and the
documents' $\chi_n=\sqrt{\Lambda_n}$.

**Everything below is `mpmath` at a stated working precision.** The prolates are built
from the prolate *differential* operator in the orthonormal Legendre (Bouwkamp) basis —
the route `s3-reduction-audit.md:340-345` recommends — with Sturm-sequence bisection for
eigenvalues and inverse iteration for eigenvectors. The finite-Fourier eigenvalue is
obtained in closed form, $\mu_n=\sqrt2\,d_0/\psi_n(0)$, from Slepian–Pollak at $x=0$;
no quadrature enters anywhere.

**Pipeline verification** (script §0). $\mu_n$ is also evaluated at $x=0.7$ and $x=1$
via $\int_{-1}^{1}P_k(t)e^{izt}dt=2i^kj_k(z)$, which uses the *whole* eigenvector and
spherical Bessel functions rather than the single coefficient $d_0$. At $c=10$,
$\mathrm{dps}=40$, the three evaluations agree to all 20 digits printed, for
$n=0,2,4,6,8$; eigenpair residuals are $\sim10^{-38}$. So the eigenvectors, not merely
the eigenvalues, are verified. The signs come out $\mu_0>0$, $\mu_2<0$, $\mu_4>0$,
$\mu_6<0$, $\mu_8>0$ — the $i^n$ phase of `s3-reduction-audit.md:227-238`.

---

## 2. The measurement: the identity does not discriminate

Ratio LHS/RHS of `start.tex:180-181`, at $c=30$, working precision 80 digits, for every
even partner mode up to 20:

| $m$ | $m \bmod 4$ | $\operatorname{sign}\mu_m$ | $\Lambda_m$ | $\lvert\text{ratio}-1\rvert$ | |
|---|---|---|---|---|---|
| 2 | 2 | $-$ | 1.0 | $4.5\times10^{+20}$ | |
| **4** | **0** | $+$ | 1.0 | $1.3\times10^{-65}$ | **reading A** |
| 6 | 2 | $-$ | 1.0 | $8.1\times10^{+13}$ | |
| **8** | **0** | $+$ | 1.0 | $1.9\times10^{-70}$ | **reading B** |
| 10 | 2 | $-$ | 1.0 | $3.6\times10^{+8}$ | |
| 12 | 0 | $+$ | 0.999998 | $8.1\times10^{-76}$ | |
| 14 | 2 | $-$ | 0.999759 | $1.7\times10^{+4}$ | |
| 16 | 0 | $+$ | 0.985645 | $1.4\times10^{-79}$ | |
| 18 | 2 | $-$ | 0.706923 | $1.3\times10^{+1}$ | |
| 20 | 0 | $+$ | 0.106277 | $0$ | |

**The test has power and it is not vacuous** — it rejects every $m\equiv2\pmod4$, by up
to twenty orders of magnitude, including modes whose concentration eigenvalue is
numerically indistinguishable from those of the accepted modes. It simply has no
resolving power *inside* the accepted class.

### Precision stability

Required by the work item, and the point on which a claim like this stands or falls.
$\lvert\text{ratio}-1\rvert$ as the working precision is increased:

| $c$ | $m$ | dps 30 | dps 50 | dps 80 | dps 120 | dps 200 |
|---|---|---|---|---|---|---|
| 12 | 4 | 1.6e-28 | 1.0e-48 | 1.3e-78 | 3.1e-118 | 2.6e-199 |
| 12 | 8 | 2.0e-31 | 2.7e-51 | 2.1e-81 | 1.9e-121 | 1.6e-201 |
| 20 | 4 | 4.4e-23 | 6.7e-43 | 2.5e-73 | 8.8e-114 | 6.3e-194 |
| 20 | 8 | 2.8e-28 | 2.5e-48 | 3.2e-78 | 3.6e-118 | 3.1e-198 |
| 30 | 4 | 7.9e-15 | 7.0e-35 | 2.9e-65 | 4.4e-105 | 5.1e-185 |
| 30 | 8 | 4.2e-21 | 2.1e-41 | 1.1e-70 | 4.2e-111 | 2.9e-191 |
| 40 | 4 | 8.8e-7  | 8.0e-27 | 4.5e-59 | 5.0e-97  | 3.1e-177 |
| 40 | 8 | 1.3e-13 | 3.8e-33 | 1.6e-63 | 1.3e-103 | 1.2e-184 |
| 60 | 4 | 0.278   | 6.9e-11 | 1.8e-41 | 2.5e-80  | 2.1e-160 |
| 60 | 8 | 0.118   | 4.3e-18 | 7.1e-49 | 1.7e-88  | 8.6e-168 |

Every entry tracks the working precision one-for-one. **The residual is roundoff and
the agreement is exact** — the answer does not move when digits are added, it only gets
more digits. Practical rule for later work: $\mathrm{dps}\gtrsim 0.9c+(\text{digits
wanted})$; the loss is the cancellation in $\chi_m-\chi_0\sim1-\Lambda_0\sim e^{-2c}$.

Truncation is not the limiting error either: at $c=30$, $m=8$, $\mathrm{dps}=80$, the
residual is flat at $\sim10^{-71}$ for Legendre bases of size $N=60,90,120,160,220$.

### The $c$ range, and why small-$c$ agreement is not what is happening here

Tested $c\in\{8,10,12,14,16,20,24,28,30,40,60\}$ for the identity, up to $c=400$ for the
asymptotic constants. The work item warned that agreement at small $c$, "where both
conventions nearly coincide", proves nothing. **The two conventions never coincide at
any $c$ tested.** They are different functions with different concentration eigenvalues
throughout:

| $c$ | $\Lambda_4$ | $\Lambda_8$ |
|---|---|---|
| 8 | 0.74790284 | 0.00041825206 |
| 10 | 0.97445778 | 0.014920175 |
| 14 | 0.99993948 | 0.66365081 |
| 16 | 0.99999776 | 0.94900699 |
| 20 | 1.0 | 0.99975345 |

At $c=8$ the two candidate modes differ by three orders of magnitude in leakage, and the
identity holds for both to 40+ digits. This is not a near-degeneracy being resolved
badly; it is an identity that does not depend on the quantity in question.

---

## 3. Why both pass — the identity carries exactly one bit

With $\widehat h_\lambda(0)=0$ and the Slepian–Pollak eigenrelation
$\widehat\psi_n(0)=\mu_n\psi_n(0)$, $\mu_n=i^n\sqrt{2\pi\Lambda_n/c}$:

$$\beta\psi_m(0)=-\alpha\frac{\mu_0}{\mu_m}\psi_0(0),\qquad
h_\lambda(0)=\alpha\psi_0(0)\Bigl(1-\frac{\mu_0}{\mu_m}\Bigr),\qquad
\frac{\mu_0}{\mu_m}=\frac{\chi_0}{\chi_m\,i^{\,m}} .$$

So

$$\boxed{\;\texttt{start.tex:180-181}\ \text{holds}\iff i^{\,m}=+1\iff m\equiv0\!\!\pmod 4.\;}$$

That is the whole content of the identity. It is a statement about the **phase class**
of $h_{4,\lambda}$ and about nothing else — in particular it is silent on which member
of that class is meant, and $4$ and $8$ are both members. The measurement in §2 is the
verification of this algebra, not an independent probe.

**What the identity does establish, and it is not nothing:** $h_{4,\lambda}$ is a
*single even prolate mode* whose finite-Fourier eigenvalue is positive. That kills
`s3-reduction-audit.md:73`'s third falsifier branch ("the 4th eigenvector of
$W_\lambda$") unless that object happens to be such a prolate, and it independently
confirms the mode-selection mechanism of `s3-reduction-audit.md:227-238` from the
corpus's own asserted identity rather than from Slepian theory alone.

---

## 4. What does settle it — the primary sources, read as source

Since the numerics cannot decide, the decision has to come from the documents. This was
recorded as open by `citation-audit.md` §7, which read the papers as rendered HTML. I
read them as **LaTeX source**, downloaded from `arxiv.org/e-print/`, and quote verbatim.

### 4.1 The alarm is real: Connes–Consani do halve the index

`arXiv:2106.01715` (*Spectral triples and $\zeta$-cycles*), source file
`Spectraltriples.tex` line 191 and again 719:

> `\psi_{m,\lambda}(x):=\text{\textit{PS}}_{2m,0}\left(2 \pi \lambda^2,\frac{x}{\lambda}\right), \ \ m\leq \nu(\lambda^2)\sim 2 \lambda^2.`

and line 193:

> "Its Fourier transform $\fourier_{e_\R}(\psi_{m,\lambda})$ restricted to the interval
> $[-\lambda,\lambda]$, is equal to $\chi_m\psi_{m,\lambda}$ where the scalar $\chi_m$ is
> very close to $(-1)^m$ provided that $m$ is less than $\nu(\lambda^2)\sim 2\lambda^2$."

Confirmed, verbatim. **U6's premise is correct**: in *that* paper $m$ is half the
prolate index, and $(-1)^m=i^{2m}$ is the same phase rule seen through the halving.

Their own two-mode combinations, line 744, "which vanish at $0$ and are given, for
$n>0$, by":

> `\phi_{2n}(x):=\psi_{2n}(x)\psi_{0}(0)-\psi_{0}(x)\psi_{2n}(0), \ \ \phi_{2n+1}(x):=\psi_{2n+1}(x)\psi_{1}(0)-\psi_{1}(x)\psi_{2n+1}(0).`

Note this pairs *even with even, odd with odd* in their index — which is exactly
"$\equiv0\bmod4$ with $\equiv0\bmod4$" in prolate index. Their smallest even member is
$\phi_2$, pairing $\psi_{0,\lambda}$ with $\psi_{2,\lambda}=\mathrm{PS}_{4,0}$.

### 4.2 But the corpus is quoting the *other* paper, and that one does not halve

`start.tex:136` heads its section "The distinguished **CCM** vector", and `:147` says
"with the **CCM** choice of coefficients". The three-author paper is
Connes–Consani–Moscovici, `arXiv:2310.18423`, source `mainc2m24fine.tex`. Lines 616–627,
verbatim:

> **616:** "For $\lambda\to\infty$ the eigenfunctions for positive eigenvalues of
> ${\bf W}_{\lambda}$ are approximated by the eigenfunctions of the operator
> ${\bf H}=-\partial^2+(2\pi q)^2$. The latter eigenfunctions are the Hermite functions
> $\{h_{2n}\}$."
>
> **618:** "Let $\cS(\R)_0^{\rm ev}$ be the subspace of the even part of the Schwartz
> space $\cS(\R)$ obtained by imposing the two conditions $f(0)=\widehat f(0)=0$."
>
> **622:** "The Fourier transform $\fourier_{e_\R}(h_{2m})$ is $(-1)^m h_{2m}$ and thus
> the two conditions $f(0)=\widehat f(0)=0$ are fulfilled by the two families of
> functions"
>
> **624:** `\psi^+_\ell:=h_{4\ell}-\frac{h_{4\ell}(0)}{h_0(0)}h_0, \ \ \psi^-_\ell:=-h_{4\ell+2}+\frac{h_{4\ell+2}(0)}{h_2(0)} h_2`
>
> **627:** `h_{2n}(0)=(-1)^n \frac{ 2^{\frac{1}{4}-n} \sqrt{(2 n)!}}{n!}`

Four independent alignments with `start.tex:138-149`, and no strain in any of them:

1. **The letter.** CCM write $h$; Connes–Consani write $\psi$. The corpus writes $h$.
2. **Both subscripts.** CCM's $\psi^+_\ell$ at $\ell=1$ is a combination of $h_0$ and
   $h_4$ — the corpus's $h_{0,\lambda}$ and $h_{4,\lambda}$, exactly, and $\ell=1$ is
   the first member of the family. Connes–Consani's even family is
   $(\psi_0,\psi_{2n})_{n>0}$, so a pair $(\psi_0,\psi_4)$ does exist there — but as the
   *second* member, used collectively with the rest for $\Pi(\lambda,k)$ rather than
   singled out. Their first member is $(\psi_0,\psi_2)=(\mathrm{PS}_{0,0},\mathrm{PS}_{4,0})$.
   The corpus singles out one partner and calls it 4; only CCM's indexing makes the
   first member "4".
3. **The coefficients.** "The CCM choice of coefficients" (`start.tex:147`) is
   $\beta/\alpha=-h_0(0)/h_4(0)$, i.e. CCM's line 624 verbatim. Connes–Consani's
   $\varphi_4$ has the *analogous* coefficients in their labels, so this alignment is
   not decisive on its own — it is decisive in combination with (1) and (2), since
   only CCM supply that formula under the letter $h$ with the subscript $4$.
4. **The index is the full index.** CCM's $\fourier(h_{2m})=(-1)^mh_{2m}$ means the
   subscript of $h$ is the ordinary Hermite index, and their split into $4\ell$ /
   $4\ell+2$ is the mod-4 phase rule stated in that index. So $h_4$ is Hermite index 4.

Line 616 is the transport: CCM's $h_{2n}$ are the $\lambda\to\infty$ limits of the
prolate operator's eigenfunctions, **at fixed index**. So $h_{4,\lambda}$ is the
finite-$\lambda$ prolate whose limit is $h_4$ — that is $\mathrm{PS}_{4,0}$.
`start.tex:148-149` ("let $\chi_0,\chi_4$ be their concentration eigenvalues") is the
corpus doing that transport explicitly: concentration eigenvalues are a prolate notion,
not a Hermite one.

### 4.3 An arithmetic corroboration that is not a notation argument

CCM's closed form at line 627 gives

$$\frac{h_4(0)}{h_0(0)}=\frac{2^{1/4-2}\sqrt{4!}}{2!}\cdot 2^{-1/4}=\frac{\sqrt{6}}{4}=\sqrt{\tfrac38}.$$

That is `s3-reduction-audit.md:147`'s $\sqrt{3/8}$, on the nose. mg-aedf derived it
independently from the fixed-index Hermite limit and never saw this formula. Two
derivations, one number: the object mg-aedf computed with and the object CCM define are
the same object. Under reading B the corresponding number would be
$h_8(0)/h_0(0)=\sqrt{35/128}$, which appears nowhere.

### 4.4 So the collision is a collision of labels, not of objects

$\mathrm{PS}_{4,0}$ is called $\psi_{2,\lambda}$ by Connes–Consani and $h_4$ (in the
Hermite limit) by Connes–Consani–Moscovici. The corpus writes $4$. Under CCM's label
that is $\mathrm{PS}_{4,0}$; under CC's it would be $\mathrm{PS}_{8,0}$. The corpus's
letter, its pair, its coefficients and its section heading are all CCM's. **Reading A.**

Worth stating separately, because it is the one part of this that does not depend on
whose notation the corpus copied: **both papers' first even two-mode combination is
$(\mathrm{PS}_{0,0},\mathrm{PS}_{4,0})$** — Connes–Consani's $\varphi_2$ and CCM's
$\psi^+_1$ are the same pair of prolate indices. Reading A is what the literature's
minimal object is under either labelling; reading B would require the corpus to have
skipped it.

A refinement to `citation-audit.md` §4.2 row 8, which maps `start.tex:138-145` to
Connes–Consani's $\varphi_{2n}$ and calls it "same construction, mirrored endpoint".
That verdict is right about the *construction* — §6.2 below makes the mirroring
precise — but the corpus's **labelling** comes from CCM's line 624, not from
$\varphi_{2n}$. The right-hand entry of that row should be
$\psi^+_\ell:=h_{4\ell}-\frac{h_{4\ell}(0)}{h_0(0)}h_0$ (arXiv:2310.18423), with
$\varphi_{2n}$ as the Connes–Consani analogue. That distinction is the whole of U6.

The one thing this does *not* settle is whether Daniel was aware there were two labels.
The corpus is internally consistent under reading A; it does not follow that the
ambiguity was noticed. That is worth telling him, and it is the reason
`s3-reduction-audit.md:371-372` ("state whether $h_4$ is the 4th prolate of order zero")
should stay on the list for his examples even though the audit item is now closed.

---

## 5. Consequence for `s3-reduction-audit.md`: nothing changes

Reading A is what that note assumed. Every constant stands:

| quantity | `s3-reduction-audit.md` | status |
|---|---|---|
| $\lvert b_\lambda\rvert^2\to$ | $8/11$ (`:136`, `:149`) | **stands** |
| $\alpha\to$ | $\sqrt{3/11}$ (`:276`) | **stands** |
| $\psi_4(0)/\psi_0(0)\to$ | $\sqrt{3/8}$ (`:147`) | **stands**, and now has a closed-form source (§4.3) |
| $(1-\Lambda_0)/(1-\Lambda_4)\sim$ | $\tfrac{3}{512}c^{-4}$ (`:181`) | **stands** |
| sharpened item (iii) | $\tfrac{8}{11}(1-\Lambda_4)(1+O(c^{-4}))$ (`:207`) | **stands** |
| signed endpoint formula | $-\sqrt{\tfrac3{11}}(c/\pi)^{1/4}(1-\chi_4)(1+O(c^{-4}))$ (`:278`) | **stands** |
| $\psi_0(0)\sim(c/\pi)^{1/4}$ | (`:274-275`) | **stands**, and is index-independent anyway |
| mode 4 is the *minimal* phase-matching partner | (`:69-70`) | **stands** |

### The counterfactual, recorded so the falsifier is closed rather than deleted

Had reading B held, these are the values it would have taken. They are computed, not
asserted, so that `s3-reduction-audit.md:64-75`'s falsifier is answered with a number
rather than retired quietly:

| quantity | reading A (correct) | reading B (rejected) |
|---|---|---|
| $\lvert b_\lambda\rvert^2\to$ | $8/11=0.727273$ | $128/163=0.785276$ |
| $\alpha^2\to$ | $3/11$ | $35/163$ |
| $\psi_m(0)/\psi_0(0)\to$ | $\sqrt{3/8}$ | $\sqrt{35/128}$ |
| $(1-\Lambda_0)/(1-\Lambda_m)\sim$ | $\tfrac3{512}c^{-4}$ | $\tfrac{315}{131072}c^{-8}$ |
| endpoint constant | $-\sqrt{3/11}=-0.522233$ | $-\sqrt{35/163}=-0.463383$ |
| mode is minimal phase-matching partner | yes | **no** — $\mathrm{PS}_{4,0}$ would leak less |

Verified numerically (script §4): $\lvert b_\lambda\rvert^2$ measured at
$c=20,40,100,200,400$ is $0.745298,\,0.735385,\,0.730348,\,0.728785,\,0.728023$ for
$m=4$ and $0.823513,\,0.800127,\,0.790638,\,0.787878,\,0.786559$ for $m=8$. Richardson
extrapolation from $c=200,400$ assuming $O(1/c)$: $0.7272604$ against $8/11=0.7272727$,
and $0.7852390$ against $128/163=0.7852761$. Both rationals confirmed to $\sim10^{-5}$.

The Fuchs exponents are consistent with $c^{-4}$ and $c^{-8}$ respectively, with the
same slow constant convergence mg-aedf reported — so this inherits U4's status
(*consistent with*, not *a check of*, the Fuchs constant), not a stronger one.

---

## 6. Two side findings

### 6.1 `s3-reduction-audit.md:322-346`'s double-precision ceiling is a property of the implementation, not of the identity

That section reports the identity "$\sim10\%$ wrong at $c=16$" and "meaningless at
$c=20$" in double precision, measured on the sinc concentration kernel, whose top
eigenvalues cluster at 1 and whose eigenvectors then degenerate. On the
differential-operator route **the same section recommends** (`:340-345`), double
precision does considerably better:

| $c$ | $\lvert\text{ratio}-1\rvert$, $m=4$ | $m=8$ |
|---|---|---|
| 12 | 3.3e-15 | 2.8e-17 |
| 16 | 4.9e-12 | 1.9e-16 |
| 20 | 7.7e-10 | 1.0e-13 |
| 24 | 1.7e-5 | 5.8e-11 |
| 28 | 1.1e-2 | 3.1e-8 |

So mg-aedf's own recommended fix works, and its measured window ($10\le c\le14$) was a
measurement of the tool. The residual cancellation is real and unavoidable —
$\chi_m-\chi_0\sim1-\Lambda_0\sim e^{-2c}$ — so arbitrary precision is still required
above $c\approx24$, and mg-aedf's headline warning ("the sign computation cannot be done
in double precision") survives for any computation that must reach large $c$. What does
not survive is the specific claim that $c=16$ is already 10% wrong.

This does not weaken the vision document's drift-mode 5 (*precision theatre*). It
sharpens it: the ceiling to quote is the one for the arithmetic you are actually using,
and quoting a ceiling measured on a different algorithm is its own version of the same
mistake.

### 6.2 The corpus's construction is the Fourier mirror of CCM's, and that is what `start.tex`'s "New reductions" section is

CCM's $\psi^+_\ell$ lies in $\{f(0)=\widehat f(0)=0\}$ **exactly** — because
$h_{4\ell}$ and $h_0$ are both $+1$-eigenvectors of the Fourier transform, so the two
conditions coincide, and one linear condition buys both. This is `start.tex:80-82`'s
codimension-two space, and it is why CCM get the pair for free.

At finite $\lambda$ that collapse fails: $\mathrm{PS}_{n,0}$ is only an *approximate*
Fourier eigenvector, $\chi_n=\sqrt{\Lambda_n}<1$. The two conditions separate, one
coefficient can only buy one of them, and the residual in the other is exactly

$$h_\lambda(0)=\alpha\,h_{0,\lambda}(0)\,\frac{\chi_4-\chi_0}{\chi_4}$$

— `start.tex:180-181`. Connes–Consani impose the $x$-side condition and carry the
residual on the Fourier side ($\phi_n(0)=0$, line 744); the corpus imposes the Fourier
side (`start.tex:171`) and carries it at the endpoint. Same construction, mirrored,
as `citation-audit.md` §4.2 row 8 already suspected.

The consequence for how `start.tex:198` should be read: "the main new structural result"
is the *finite-$\lambda$ correction term* to a cancellation that is exact in CCM's
$\lambda\to\infty$ picture. That is a real thing to have computed, and it is a smaller
thing than the sentence claims — which is the direction `citation-audit.md` §8 already
flagged for `:198`, now with the specific reason.

---

## 6.3 Two by-products, from having the sources on disk — reported, not acted on

Neither is this work item's business; both are recorded because the check cost one grep
each and both bear on items the project is currently blocked on. Nothing was edited on
their account.

**`citation-audit.md` §4.3 is confirmed from the primary source** — the claim its own §9
names as "the claim in this note that would do the most damage if wrong". In
`Spectraltriples.tex`:

- **line 169:** "By semi-local Weil quadratic form we mean the restriction $QW_\lambda$
  of the sesquilinear form …" — $QW_\lambda$ is a single symbol for the Weil quadratic
  form, defined as such. No operator $Q$ is introduced anywhere.
- **line 713 / 717:** `({\bf W}_{\lambda}\psi)(q) = -\partial((\lambda^2-q^2)\partial)\ldots`
  and "The operator ${\bf W}_{\lambda}$ … is selfadjoint and positive and its
  eigenfunctions are the prolate spheroidal wave functions."

Both halves hold. Counting confirms the trap: `W_\lambda` occurs 41 times in that file
and **every occurrence is inside `QW_\lambda`**; the prolate operator appears 4 times
and only as **bold** `{\bf W}_{\lambda}`. The two objects are distinguished by a font
and a leading letter, in the same section. That is a sufficient explanation for how
`start.tex:41-44` came to split the symbol, and it means the split cannot be repaired by
choosing a reading — under the published notation there is no $Q$ to remove anything.
Gate 2, on the published side, is answered; whether `start.tex` should follow the
published side is still Daniel's.

**Gate 1's published-reading answer is confirmed verbatim, not inferred.** The vision
document's amendment §3 read *finitely many primes* off Connes–Consani's Figures 7–17.
Line 169 states it in words: $QW_\lambda$ "only involves primes less than, say,
$\lambda^2$". That is `signed-geometry-proposals.md:388-389`'s middle branch — the one
on which C2 predicts the sign and supplies a route to it — and it upgrades the
"partial answer from the literature" recorded at `:399-404`, which reads the same
conclusion off Figures 7–17, to a verbatim statement in the text. It remains Daniel's to confirm
that this is what `start.tex` means; the *published* reading is no longer in doubt.

---

## 7. The house rule

> Is any statement in this note false for $-W_\lambda$?

**No. This note is sign-blind, entirely.** Not one statement in it mentions $W_\lambda$,
$\zeta$, $E$, or a prime. It is a statement about which prolate function a subscript
denotes, and about the constants attached to it, and every one of those survives
$W_\lambda\mapsto-W_\lambda$ untouched.

That is expected for a convention-settling note and is not a defect in it, but the
consequence should be stated plainly rather than left implicit: **settling U6 does not
advance the sign question by one step.** What it does is protect constants that were
themselves sign-blind. The single exception in the vicinity —
`s3-reduction-audit.md:278`'s $h_\lambda(0)<0$ — is a sign attached to the *test
vector*, not to the form, and `s3-sign-blindness.md:83` already records it as such.

The value delivered here is defensive: a threat to a result the project was treating as
established has been removed, and the specific way it was removed (documentary, not
numerical) is now on the record so nobody repeats the numerical attempt.

---

## 8. This note, audited by its own rule

A note that settles a citation question is subject to citation error, and a note whose
headline is a numerical non-result is subject to having measured the wrong thing.

**What I read as primary source.** The LaTeX sources of arXiv:2310.18423
(`mainc2m24fine.tex`, 99,875 bytes, dated 2024-05-04) and arXiv:2106.01715
(`Spectraltriples.tex`), downloaded from `arxiv.org/e-print/` and read directly. Every
quotation in §4 is from those files, with the line number in that file given. This is a
stronger provenance than `citation-audit.md` had for the same passages, which is why an
item it recorded as open can be closed here. It is *not* the published journal text
(Enseign. Math. **69** (2023) 93–148 for the second); arXiv source and published version
could in principle differ, though not plausibly in a definition.

**What is inference, not quotation.** That the corpus is quoting CCM's line 624 rather
than coincidentally arriving at the same pair. The four alignments of §4.2 plus the
arithmetic corroboration of §4.3 make this very strong, but the corpus contains no
citation — `citation-audit.md` §8's first finding — so the identification is
reconstructed rather than declared. If Daniel says he meant Connes–Consani's
$\psi_{4,\lambda}$, he is describing a different vector from the one his own
coefficients define, and that is a correction to `start.tex` rather than a refutation
of this note.

**What the numerics do and do not show.** They show the identity is exact for every
$m\equiv0\pmod4$ and false for every $m\equiv2\pmod4$, at 30–200 digits and
$c=8\ldots60$, stably in precision and in truncation. They do **not** show reading A;
nothing numerical can, and §3 proves why. Anyone re-running the script and finding
"$m=4$ passes" has not confirmed reading A — $m=8$ passes identically.

**The residual open item.** `s3-reduction-audit.md:73`'s third falsifier branch —
$h_{4,\lambda}$ as "the 4th eigenvector of $W_\lambda$" — is now heavily constrained
(§3: it must be a single even prolate with positive finite-Fourier eigenvalue) but is
not formally excluded, since the corpus never defines $W_\lambda$. Under
`citation-audit.md` §4.3 there may be no operator $W_\lambda$ in the corpus's sense at
all, in which case the branch is empty. That is Gate 2, and it is Daniel's.
