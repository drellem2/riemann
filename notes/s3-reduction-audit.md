# Where the $S^3$ geometry could reduce a Connes gap — audit of item (iii) and a ranked shortlist

Work item mg-aedf. Companion script: [`verify_prolate_claims.py`](verify_prolate_claims.py)
(needs numpy; all numbers quoted below are its output).

Nothing in `start.tex` or `s3.tex` was edited. References are by line.

**Citations checked (added 2026-08-12).** [`citation-audit.md`](citation-audit.md)
(mg-3a9c) verified this note's attributions against the sources: **B1–B4 hold as
stated**, and the references are recorded at the four sites below. Three items remain
**open**, and are marked open rather than dropped — **U3** (the uniform-error form of
the Hermite limit, §2), **U4** (Fuchs' exact constant, §2), **U6** (the prolate-index
ambiguity, §0). One substantive narrowing, at §3: the finite-Fourier phase fact **is**
in Connes–Consani; the mode-4 *selection* built on it is not. Annotated in place, not
rewritten — what this note concluded on its own evidence is part of the record.

---

## Bottom line

**No candidate examined is a reduction of a Connes gap.** Item (iii) is true and
provable, but it is a statement about prolate spheroidal functions containing no
arithmetic; it gives the size of a quantity that is not itself an obstruction.
The two candidates that would touch the actual gap — identifying $C_\lambda$
geometrically (`start.tex:373-377`) and the uniform gap on the orthogonal
complement (`start.tex:379-383`) — each replace the open problem with a strictly
harder one.

What the audit did produce is three provable sharpenings and one correction, all
of which turn out to be **classical Slepian theory rather than $S^3$ geometry**:

1. **The choice of mode 4 is forced, and the reason is not geometric.** It is the
   finite-Fourier phase $i^n$. Mode 0 and mode 4 have $\mu_n>0$; mode 2 has
   $\mu_2<0$. Imposing $\widehat h_\lambda(0)=0$ makes the two endpoint values
   *cancel* for $\{0,4\}$ and *reinforce* for $\{0,2\}$. This contradicts
   `s3.tex:82-83`, which credits mode selection to the $S^3$ geometry.
2. **Items (i) and (ii) are one fact, not two.** (ii) is the one-line consequence
   of imposing (i), via the Slepian–Pollak finite-Fourier eigenrelation. `start.tex:191-195`
   presents "exceptional sector $= 0 + O(1-\chi_4)$" as two independent controls;
   it is one control with one free parameter spent.
3. **Item (ii) can be upgraded to an exact leading term with a sign**, and (iii)
   to an exact rational constant. The documents state both as $O$/$\asymp$ only.
4. **The implied constant in $h_\lambda(0)=O(1-\chi_4)$ is not uniform in $\lambda$** —
   it grows like $c^{1/4}$.

---

## 0. Reconstruction of the setup, and its falsifier

Neither document fixes normalizations, so the objects were reconstructed from
classical Slepian theory: band-limit $c$ (the documents' $\lambda$), interval
$[-1,1]$, concentration operator with eigenvalues $\Lambda_0>\Lambda_1>\dots$
and orthonormal eigenfunctions $\psi_n$.

The documents' $\chi_n$ is $\sqrt{\Lambda_n}$. Two independent reasons:
`s3.tex:64-66` writes the leakage as $1-\chi_n^2$ where the true leakage is
$1-\Lambda_n$; and `start.tex:180-181` reproduces *only* under $\chi_n=\sqrt{\Lambda_n}$.

**Evidence the reconstruction is right:** derived independently, it reproduces
`start.tex:180-181` — $h_\lambda(0)=\alpha h_{0,\lambda}(0)(\chi_4-\chi_0)/\chi_4$ —
to **8 significant figures** at $c=4,6,8,10,12$ (script, column `C: ratio`
$=1.00000000$). A formula that specific is not matched by coincidence.

**Falsifier:** if CCM's $h_4$ is not the 4th prolate of order zero, §3's
mode-selection result changes. The phase-matching condition is $n\equiv0\pmod 4$
(§3), so:

- *Full prolate indexing* ($h_4=\psi_4$): phase-matches **and** is the minimal such
  partner of $\psi_0$ — i.e. the choice that minimises leakage subject to the
  cancellation. That the reading makes the CCM choice optimal is further evidence for it.
- *Even-only indexing* ($h_4=\psi_8$): still phase-matches, but is not minimal —
  $\psi_4$ would do strictly better. The mechanism survives; the optimality claim does not.
- *"4th eigenvector of $W_\lambda$"*: §3 does not survive this reading at all.

Daniel's forthcoming examples should state the indexing explicitly.

> **Still open — audit U6 (`citation-audit.md` §7).** The citation audit sharpened this
> falsifier without settling it, and it is recorded here as open rather than dropped.
> Connes–Consani index their two-mode combinations by
> $\psi_{m,\lambda}:=\mathrm{PS}_{2m,0}$, so **their $m$ is half the prolate index**.
> The script here uses prolate index 4, i.e. their $m=2$. If `start.tex:138-145` means
> *their* $m=4$, it is prolate index 8 and every constant in this note changes. What
> survives either reading is §3's phase rule, since both candidate indices are
> $\equiv0\pmod4$; what does not survive is the $8/11$ of §2. So the falsifier above is
> not hypothetical — there is a live second reading in the published source, and only
> Daniel can close it.

---

## 1. What item (iii) reduces, and to what

`s3.tex:55-78` asserts two things, and they have very different status.

### (a) The Pythagoras identity (`s3.tex:62-67`) — true, and free

$\|(1-\widehat P)h_\lambda\|^2 = |a_\lambda|^2(1-\chi_0^2)+|b_\lambda|^2(1-\chi_4^2)$.

This is exactly the **double orthogonality** of the prolates. With $\psi_n$ supported
in the interval and $DBD\psi_n=\Lambda_n\psi_n$:

$$\langle(1-B)\psi_0,(1-B)\psi_4\rangle=\langle\psi_0,\psi_4\rangle-\langle B\psi_0,\psi_4\rangle=0-\Lambda_0\langle\psi_0,\psi_4\rangle=0 .$$

It requires no hypothesis about which modes occur and **no $S^3$ input whatsoever**.
`s3.tex:80-82` describes it as something the $S^3$ geometry supplies ("The $S^3$
geometry identifies which modes occur"); the identity holds for any two prolates.

A consequence worth recording: since $\Lambda_0>\Lambda_4$ and $|a|^2+|b|^2=1$,

$$\|(1-\widehat P)h_\lambda\|^2 \;\le\; 1-\Lambda_4 ,$$

so **the upper half of the $\asymp$ at `s3.tex:75-77` is free.** Only the lower
bound carries content.

### (b) The conclusion $\asymp 1-\chi_4$ — needs the lower bound only

So item (iii)'s real content is the *lower* bound, and it reduces

> "the CCM near-null direction is small for some unexplained reason"

to

> "$|b_\lambda|$ is bounded below as $\lambda\to\infty$."

That is a genuine reduction *of a prolate question to a prolate question*. It does
not reduce anything on the Connes side: $\|(1-\widehat P)h_\lambda\|^2$ is not an
obstruction in Weil positivity. It is the leakage of the test vector, and the
arithmetic operator $E$ sits between it and $QW_\lambda(Eh_\lambda)$. There is no
implication leakage-scale $\Rightarrow$ Weil-form scale anywhere in either document.

---

## 2. The two unproved uniformity claims — verdicts

| # | Claim | As stated | Verdict |
|---|---|---|---|
| U1 | $b_\lambda\ne0$, uniformly (`s3.tex:68`) | pointwise only | **Provable; known.** $\lvert b_\lambda\rvert^2\to 8/11$ |
| U2 | lower-mode leakage negligible (`s3.tex:83-84`) | asserted as obvious | **Already known.** Fuchs/Slepian; ratio $\asymp c^{-4}$ |

### U1 — "$b_\lambda\neq0$" is stated pointwise; the $\asymp$ needs it uniformly

**Verdict: plausibly provable, and in fact it follows from known asymptotics.**

$\widehat h_\lambda(0)=0$ forces $\beta/\alpha=-(\chi_0/\chi_4)\,\psi_0(0)/\psi_4(0)$. As
$c\to\infty$ the prolates of fixed index converge (after rescaling $x\mapsto\sqrt{c}\,x$)
to Hermite functions, so

$$\frac{\psi_4(0)}{\psi_0(0)}\longrightarrow\frac{\psi_4^{H}(0)}{\psi_0^{H}(0)}=\sqrt{\tbinom{4}{2}/4^{2}}=\sqrt{3/8},$$

giving $|\beta/\alpha|\to\sqrt{8/3}$ and $|b_\lambda|^2=|\beta|^2\to 8/11$.

Verified: $|\beta|^2 = 0.783,\,0.745,\,0.734,\,0.730,\,0.729,\,0.728$ at
$c=10,20,50,100,200,400$ against $8/11=0.7273$. So U1 is not merely true — the
limit is an explicit rational.

The inputs are the fixed-index large-$c$ Hermite limit for prolates, which has
rigorous uniform-error versions in the literature (Slepian 1965 for the asymptotic;
Bonami–Karoui and Osipov–Rokhlin–Xiao for rigorous bounds — *citations to be checked,
this audit was run offline*). **This is not the difficulty in disguise. It is
bookkeeping over a known asymptotic.**

> **Checked, 2026-08-12 — B2, B3 hold (`citation-audit.md` §3).** The sources are
> right, and are: D. Slepian, *Some asymptotic expansions for prolate spheroidal wave
> functions*, J. Math. and Phys. **44** (1965) 99–140 (**B2**); A. Bonami, A. Karoui,
> *Uniform approximation and explicit estimates for the prolate spheroidal wave
> functions*, Constr. Approx. **43** (2016), and A. Osipov, V. Rokhlin, H. Xiao,
> *Prolate Spheroidal Wave Functions of Order Zero*, Applied Math. Sciences **187**,
> Springer 2013 (**B3**) — the latter being reference [16] of Connes–Consani–Moscovici
> arXiv:2310.18423, i.e. the same source the principals use.
> **Still open — audit U3.** The *uniform-error* statement this paragraph attributes to
> Slepian 1965 was not checked against the paper (paywalled). So "has rigorous
> uniform-error versions in the literature" is an attribution to a confirmed source, not
> a verification of the statement, and the verdict that U1 is "bookkeeping over a known
> asymptotic" rests on it.

### U2 — "leakage associated to lower modes is smaller"

**Verdict: already known, with an explicit rate — and the rate is only polynomial.**

Fuchs/Slepian: $1-\Lambda_n(c)\sim \dfrac{4\sqrt\pi\,8^n c^{n+1/2}e^{-2c}}{n!}$, hence

$$\frac{1-\Lambda_0}{1-\Lambda_4}\sim\frac{4!}{8^4}\,c^{-4}=\frac{3}{512}c^{-4}.$$

Verified: measured ratio vs. predicted, $c=8\to14$: $8.4\text{e-}6/1.4\text{e-}6$,
$1.7\text{e-}6/5.9\text{e-}7$, $6.3\text{e-}7/2.8\text{e-}7$, $2.9\text{e-}7/1.5\text{e-}7$ —
the $c^{-4}$ rate is right and the constant is converging (slow, as Fuchs asymptotics are).

> **Checked, 2026-08-12 — B4 (`citation-audit.md` §3).** Source confirmed: W.H.J.
> Fuchs, *On the eigenvalues of an integral equation arising in the theory of
> band-limited signals*, J. Math. Anal. Appl. **9** (1964) 317–330.
> **Still open — audit U4.** The exact constant $4\sqrt\pi\,8^nc^{n+1/2}e^{-2c}/n!$ was
> not checked against the paper. The numerical evidence just above is *consistent with*
> it and no more: a slowly converging ratio is not a check of the formula, and the
> $3/512$ derived from it inherits that status.

The quantitative consequence matters and is not stated in either document: because the
suppression is only **polynomial** ($c^{-4}$), not exponential, U2 is not free — it is a
real constraint, namely $|b_\lambda|^2\gg c^{-4}$. U1 supplies that with room to spare.

**Neither uniformity claim is the whole difficulty in disguise.** Both are consequences
of classical prolate asymptotics. Item (iii) is therefore *true and provable* — and
correspondingly *contains no arithmetic*.

### Sharpened form of item (iii)

Combining, with $\|h_\lambda\|_2=1$:

$$\boxed{\;\|(1-\widehat P)h_\lambda\|_2^2=\tfrac{8}{11}\,(1-\Lambda_4)\bigl(1+O(c^{-4})\bigr)\;}$$

Verified: `leak/(1-lam_4)` equals $|\beta|^2$ to 6 digits at every $c$ tested —
the mode-0 term is invisible, exactly as the $c^{-4}$ rate predicts.

This is strictly stronger than `s3.tex:75-77` ($\asymp$) and is a hard consistency
check on any future trace-formula computation.

---

## 3. Why mode 4 — the one structural finding

`s3.tex:83` credits the $S^3$ geometry with forcing the $h_4$ component. It is forced,
but by Slepian–Pollak: the prolates are eigenfunctions of the finite Fourier transform,

$$\int_{-1}^{1}\psi_n(t)e^{icxt}\,dt=\mu_n\psi_n(x),\qquad \mu_n=i^{\,n}\sqrt{2\pi\Lambda_n/c}.$$

At $x=0$ this reads $\widehat\psi_n(0)=\mu_n\psi_n(0)$. Imposing $\widehat h_\lambda(0)=0$
on $h_\lambda=\alpha\psi_0+\beta\psi_m$ then gives

$$m\equiv0\ (4):\quad h_\lambda(0)=\alpha\psi_0(0)\frac{\chi_m-\chi_0}{\chi_m}\sim-\alpha\psi_0(0)(1-\chi_m)\quad\textbf{[cancels]}$$
$$m\equiv2\ (4):\quad h_\lambda(0)=\alpha\psi_0(0)\frac{\chi_m+\chi_0}{\chi_m}\sim\ \ 2\alpha\psi_0(0)\qquad\qquad\textbf{[reinforces]}$$

**Mode 4 is the least-leaky even prolate whose finite-Fourier phase matches mode 0.**
Mode 2 is closer and would leak far less, but its phase is wrong and it destroys the
endpoint cancellation entirely.

Verified two ways. Convention-free: $r_n:=\widehat\psi_n(0)/\psi_n(0)=\mu_n$ is independent
of eigenvector sign choices, and the script finds $r_0,r_4>0$, $r_2<0$, all with
$|r_n|=\sqrt{2\pi/c}$ to 6 digits at $c=10\dots400$. Directly: imposing the *same*
constraint on $\{0,2\}$ and $\{0,4\}$ at $c=8\dots16$ gives $|h(0)|\approx1.37\to1.69$
(i.e. $O(1)$, growing) for $\{0,2\}$ versus $7.8\text{e-}2\to9.2\text{e-}7$ for $\{0,4\}$.

**This subtracts from the $S^3$ case rather than adding to it.** The mode selection —
the one place `s3.tex` claims the geometry does structural work — is a parity rule in
Slepian theory. Any $S^3$ derivation of "4" will at best reproduce it.

> **Narrowed by the citation audit — B1 and its note (`citation-audit.md` §3).** The
> eigenrelation holds and the source is right (D. Slepian, H.O. Pollak, Bell System
> Tech. J. **40** (1961) 43–63). What the audit adds is that the two halves of this
> section have different status, where the heading above calls the whole of it "the one
> structural finding":
>
> - **The phase fact is not ours.** Connes–Consani state the same relation themselves,
>   as $\widetilde{\mathcal F}(\psi_{m,\lambda})=\chi_m\psi_{m,\lambda}$ with $\chi_m$
>   "very close to $(-1)^m$ provided $m<2\lambda^2$" (arXiv:2106.01715 §3). Their $m$ is
>   half the prolate index, so $(-1)^m=i^{2m}=i^{\,n}$ — **the same statement** — and
>   they use it, to split the even and odd matrices.
> - **The mode-4 *selection* is ours.** Choosing 4 as the least-leaky even prolate whose
>   phase matches mode 0, and the $\{0,2\}$-versus-$\{0,4\}$ comparison above, are not in
>   Connes–Consani; they never select a mode this way.
>
> So the conclusion of this section **stands and is reinforced**: the mode selection is
> a parity rule in classical Slepian theory — and, more sharply, one already in the
> corpus's own base paper — so it subtracts from the $S^3$ case, and any $S^3$
> derivation of "4" at best reproduces it. What does not stand is reading this section
> as a *new* fact about the phase.

---

## 4. Items (i) and (ii) are one fact; and (ii) has a sign

The relation above shows $\widehat h_\lambda(0)=0$ is not a cancellation *discovered* in
the $S^3$ mode decomposition (`s3.tex:17-23`) — it is the **constraint that defines**
$\beta/\alpha$. Item (ii) is then its one-line consequence. `start.tex:191-195` boxes
"exceptional sector $=0+O(1-\chi_4)$" as two controls; it is one.

Because $\chi_0>\chi_4$ always, $(\chi_4-\chi_0)/\chi_4<0$, and $\psi_0(0)\sim(c/\pi)^{1/4}$
(verified: $\psi_0(0)/c^{1/4}=0.7509$ at $c=400$ vs $\pi^{-1/4}=0.7511$). So with
$\alpha\to\sqrt{3/11}$:

$$\boxed{\;h_\lambda(0)=-\sqrt{\tfrac{3}{11}}\Bigl(\tfrac{c}{\pi}\Bigr)^{1/4}(1-\chi_4)\bigl(1+O(c^{-4})\bigr)\;}$$

Two things follow that the documents do not state:

- **The sign is determined** (negative under $\alpha,\psi_0(0)>0$). Every other
  conclusion in `s3.tex` is $O/\Theta/\asymp$ and therefore sign-blind; this one is not.
- **The constant is not uniform.** `start.tex:186` and `s3.tex:35` write $h_\lambda(0)=O(1-\chi_4)$,
  which reads as an $O(1)$ constant. Under $\|h_\lambda\|_2=1$ it grows like $c^{1/4}$.
  Harmless for an $\asymp$ statement; **not** harmless for the comparison of constants
  that the sign question actually requires.

---

## 5. Ranked shortlist of candidate reductions

"Reduction" is used strictly: does it replace the open problem with a *strictly easier* one?

| # | Gap | Proposed $S^3$ reduction | What must be proved | Is it a reduction? |
|---|---|---|---|---|
| 1 | Why this test vector / why mode 4 (`s3.tex:82-83`) | geometry forces the $h_4$ component | *nothing* — it is Slepian–Pollak $\mu_n=i^n\sqrt{2\pi\Lambda_n/c}$ plus $\Lambda_n\downarrow$ | **Dissolved, not reduced.** Proved here, without $S^3$. Removes an $S^3$ claim. |
| 2 | What exactly does $Q$ remove? (`start.tex:44`, `:209-210`) | — | a *definition*, not a theorem | **Blocking and cheap.** See below. |
| 3 | Sign of the endpoint contribution | item (ii) | fixed-index Hermite limit + Fuchs/Slepian (both known) | **Partial and real.** Settles one of two unknown signs; see §4. Proved here modulo cited asymptotics. |
| 4 | Scale of the CCM near-null direction | item (iii) | U1, U2 — both known (§2) | **True, provable, arithmetically empty.** No $\zeta$, no primes, no Weil form. |
| 5 | Can $\mathrm{sign}(C_\lambda)$ be computed numerically? | — | extended-precision prolates | **Operational blocker, measured here.** See below. |
| 6 | Turning the prime sum into a boundary term | commutator localization (`start.tex:264-273`) | explicit kernel for the multiplicative-translation matrix elements of $[L_c,P]$, then a coefficient computation | **No — a change of coordinates.** Real content, but it is Slepian not $S^3$, and `start.tex:297-300` already concedes it gives neither sign nor size. |
| 7 | Value of $C_\lambda$ | identify it as an $S^3$ boundary/intersection quantity (`start.tex:373-377`) | an *intertwiner* between the $S^3$ model and the arithmetic side | **No — strictly harder.** `start.tex:98` calls the dictionary "schematic rather than an asserted literal equivalence". Nothing in the $S^3$ model knows about primes. Replaces "compute an arithmetic constant" with "construct a geometry-to-arithmetic intertwiner". |
| 8 | Uniform gap on the orthogonal complement (`start.tex:379-383`) | — | $\langle W_\lambda f,f\rangle\ge c\|f\|^2$ for all $f$ off a 3-dimensional space, uniformly in $\lambda$ | **No — this is RH.** Weil positivity on a codimension-3 space. `start.tex:391` already flags it as the critical logical point. No $S^3$ material addresses it. |

Nothing in the audit touches item (iv) / $(*)$ — `s3.tex:210`, `start.tex:212-217`.
That gap is exactly where both documents leave it.

### On #2 — a blocking ambiguity that is cheap to resolve

`start.tex:44` says $Q$ "removes the expected low-dimensional exceptional sector."
If $Q$ removes the $h(0)$ and $\widehat h(0)$ directions, then items (i) and (ii)
**do not enter $QW_\lambda(Eh_\lambda)$ at all** — their role is only to show $h_\lambda$
nearly lies in the domain of the Weil criterion, and they contribute nothing to the
sign. If $Q$ does not remove them, they contribute explicitly, and §4's signed formula
feeds straight into $C_\lambda$.

The documents do not say which, and the two readings give materially different programs.
This is a definition to write down, not a theorem to prove, and it gates the value of
everything in §§2–4. **It is the cheapest high-value item on this list.**

### On #5 — the numerical sign computation has a narrow window

mg-8888's recommended next target was to compute $\mathrm{sign}(C_\lambda)$ numerically.
The audit measured the feasibility, and it is tighter than it looks:

- Mode 4 is inside the concentrated plateau only for $2c/\pi>5$, i.e. $c>7.9$.
- In double precision the identity of `start.tex:180-181` reproduces to 8 digits for
  $c\le12$, drifts by $\sim10^{-4}$ at $c=14$, is $\sim10\%$ wrong at $c=16$, and is
  **meaningless at $c=20$** — $1-\Lambda_0\sim e^{-2c}$ underflows relative to $\Lambda_0\approx1$.
- Worse, the sinc-kernel eigenproblem degenerates: once $\sim2c/\pi$ eigenvalues equal
  $1$ to machine precision, `eigh` returns an arbitrary rotation inside that cluster, so
  the **eigenvectors are junk too**, not merely the eigenvalues. (At $c=30$ it reports
  $\psi_4(0)/\psi_0(0)=7.88$; at $c=120$, $39.7$. Both meaningless.)

So the usable double-precision window is roughly $10\le c\le14$ — about one decade of
$1-\Lambda_4$, which is thin for fitting an exponent, and thinner still for a sign that
may only settle asymptotically.

**Recommended fix, and it is not exotic:** work with the prolate differential operator
$L_c$ in the normalized-Legendre (Bouwkamp) basis rather than the concentration kernel.
$L_c$ has well-separated eigenvalues $\chi_n\sim n^2$, so its eigenvectors are stable at
any $c$; the script uses this route to reach $c=400$ cleanly. Composed with `mpmath`
for the $1-\Lambda_n$ subtractions, this removes the ceiling entirely. Note this is the
same $L_c$ whose commutator identity $[L_c,P]=0$ is invoked at `start.tex:264-273`.

---

## 6. What would make the $S^3$ material more than a dictionary

Stated as a target rather than a complaint. Every $S^3$ statement in the corpus turned
out, on inspection, to be a restatement of a Slepian statement. That will remain true
until the geometry supplies one of:

- **(a) An action, not an analogy.** A unitary representation of a compact group on the
  CCM test space commuting with $W_\lambda$ up to controlled error. Positivity could then
  come from group averaging (Bochner/Godement) rather than from an estimate — which
  *would* be a genuine reduction, because it would replace an asymptotic by a symmetry.
  There is no evidence in the corpus that such an action exists, and $W_\lambda$ carries
  the primes, which no compact group acts on. Naming it is still worthwhile: it is what
  "the $S^3$ geometry reduces a Connes gap" would have to *mean*.
- **(b) An exact intertwiner** carrying the prolate concentration operator to a geometric
  operator on $S^3$ with computable spectrum. Then #7 above becomes available.
- **(c) Any $S^3$ statement that is not sign-blind.** This is the sharpest test and the
  cheapest to apply.

### What Daniel's forthcoming examples would need to show

To change the verdict above, an example must do at least one of:

1. **Fix the indexing** (§0 falsifier): state whether $h_4$ is the 4th prolate of order
   zero. Everything in §3 is conditional on this.
2. **Derive the mode selection from $S^3$ by a route that is not the $i^n$ phase.** If
   $S^3$ reproduces "4" via the phase, that is consistency, not new content. If it predicts
   a *different* selection rule that also holds, that is new content and would move the
   geometry from dictionary to tool.
3. **Produce one signed $S^3$ conclusion.** A single statement of the form "this quantity
   is positive because of the geometry" would be worth more than any number of further
   $\asymp$ statements — the sign is the entire content of what remains (`s3.tex:183`).
4. **Exhibit the action or intertwiner of (a)/(b)**, even in a special case.
5. **Give one nontrivial numerical agreement** between an $S^3$-computed quantity and a
   prolate/arithmetic one that is not forced by construction.

An example that adds a sixth row to the dictionary table at `start.tex:100-127` would
not change anything in this report.

---

## 7. Relation to the existing next target

This does not displace "compute $\mathrm{sign}(C_\lambda)$ and the true exponent"
(mg-8888), and does not contradict it. It bears on it in three places:

- §4 determines the **sign and exact constant of the endpoint term**, removing one of the
  unknowns from that computation — *conditional on #2*, the $Q$ question.
- §2 supplies the **exact constants** $8/11$, $3/11$, $\sqrt{3/8}$, $\pi^{-1/4}$ and the
  $c^{-4}$ error rate, which any candidate asymptotic must reproduce. These are cheap
  falsification checks.
- §5 says the computation **cannot be done in double precision** as it stands, and gives
  the route that works.

`s3.tex:183` remains accurate: what is left is the sign and the leading arithmetic
coefficient. Nothing found here supplies either.
