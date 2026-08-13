# The defect this corpus keeps producing: the printed statement does not match the argument beneath it

Work item mg-83d1. **Methodology, not mathematics.** Nothing here changes a statement, a
proof, a constant or a number; every finding it refers to is closed and its repair has
landed. It exists because the class below is the one thing three formalisation runs have
found, and it is invisible to every instrument this repository owns.

Read this alongside the house rule (*is the statement false for $-W_\lambda$?*, stated in
the paper's §`sec:houserule` and applied in the closing "house rule, applied to this note"
section every note here carries). Those are the project's **two standing checks**: the
house rule asks whether a true statement can carry the content claimed for it; this one
asks whether the statement printed is the statement proved.

---

## The class, in one sentence

> **The printed statement does not match the argument beneath it.**

The argument is sound and its consequences are true; the sentence, formula or hypothesis
list standing above it says something else — weaker, or different, or false. A reader
checking the prose against itself cannot see this, because the prose is coherent. A reader
checking the consequences cannot see it either, because the consequences are right.

**It is not "missing hypotheses."** That narrower reading fits the first two samples, and
it was circulated as the finding before the third arrived and refuted it — the third was a
displayed formula that was simply false. The narrow version is recorded here only so that a
reader who met it earlier replaces it: a missing hypothesis is one way for a statement to
disagree with its argument, not the class.

## Four instances: three formalisation runs, and one re-derivation

| run | what it found |
|---|---|
| mg-a087 | Lemma 5.1's hypothesis "$\Phi$ analytic at $x=1$" was doing two independent jobs; the note's weakening — "boundedness near $x=1$ would do" — named one of them. |
| mg-7fc6 | `cor:upper` was printed without $\mu^{-1}\log(1-\chi_2)\to-4\pi$, the hypothesis that carries the $4\pi$ — which revealed that the unconditional chain rests on **two** imports where the ledger said one. |
| mg-57a2 | [`dilate-sum.md`](dilate-sum.md) Lemma 3.1's Liouville potential was **false**: printed $(c^2-\chi+1)/(x^2-1)$, true $(c^2-\chi)/(x^2-1)+1/(x^2-1)^2$. It had propagated to [`band-edge-connection.md`](band-edge-connection.md), [`h1-mean-value.md`](h1-mean-value.md) and [`verify_q2.py`](verify_q2.py)'s CHECK 1 banner. |
| mg-d03b | `verify_sonin_trace.conditions()` printed the name $\hat g(i/2)$ over a row that was the integral over $[-L,L]$, twice the support — an antiderivative evaluated at the wrong endpoint. See below: this one was **not** found by a formalisation run, and its consequence was not nothing. |

The first three are recorded in full where they were found —
[`lean/README.md`](../lean/README.md) §"What formalising changed in the informal
statements", items 1, 4 and 7 — and this note does not re-audit them; the fourth is in
[`sonin-margin.md`](sonin-margin.md).

Four defects in what a statement says. **No *formalisation* run has yet found a
conclusion that was wrong; the fourth instance found one, and it was not a formalisation
run** — see below. (Item 7 there records mg-57a2's as
an incorrect *proof*, which it also is — the note's derivation drops a power. Both readings
are of the same event; what this note is about is where the damage sat, and it sat in the
printed line, not in anything drawn from it.)

## Why nothing catches it

**Nothing downstream goes red.** In all three cases everything *derived* from the bad
statement was correct, so no check failed, no number moved, and nothing complained.

That is not luck, it is the shape of the class. A statement gets into the corpus by being
used; if what was used were wrong, something would already have broken. What survives is
exactly the discrepancy that the downstream use does not exercise — a hypothesis nobody
needed to name, a formula consumed only through a bound that both versions satisfy.

mg-57a2's formula had been read and copied four times before a machine saw it, including
into a `CHECK` banner: **an instrument quoting the wrong statement while correctly testing
the right one.** A numerical script that tests conclusions is not evidence about the line it
prints above them.

So: this class has no natural detector, and it will not announce itself. It is found only by
re-deriving a printed statement from scratch, and that has to be done on purpose.

---

## The fourth instance, which arrived from somewhere else (mg-d03b)

The fourth was not found by formalising. It was found by re-deriving a printed number
from scratch because a work item said to, and it differs from the first three in the one
way that matters: **its consequence was not nothing.**

- The *statement-shaped* half is the class exactly. `verify_sonin_trace.conditions()`
  returned a row named $\hat g(i/2)$ that was the integral over $[-L,L]$ rather than the
  support $[-L/2,L/2]$ — `np.exp(q)` where `np.exp(q/2)` was meant. Nothing went red;
  the script's output before and after the fix is **byte-identical**, because the column
  it fed does not depend on which two conditions are imposed.
- The *number-shaped* half is new here and worth naming separately. `sonin-trace.md`
  printed $8.7\times10^{-5}$ as "the margin Theorem 1 buys". It is
  $\epsilon'(1^+)L^2/2\pi^2N^2$ — a closed form in the truncation order $N$, which goes
  to zero as $N$ grows. The prose above the table said what the table was *about*, and
  the table was about something else. [`sonin-margin.md`](sonin-margin.md).

Two additions to the practices below, both cheap and both would have caught it.

**Vary the parameter that is supposed not to matter.** A truncation order, a grid step,
a quadrature node count. If a headline number moves like $N^{-2}$, it is a statement
about $N$. mg-5210 varied $N$ once, for a *sign* (CHECK 2 at $N=40$ and $80$), and never
for a *value*. One extra column would have ended it.

**Look for a monotonicity the answer must satisfy, and check the table against it.**
$-E$, $\lVert g\rVert^2$ and both vanishing conditions are independent of the support
length, and a test function admissible at $\mu_1$ is admissible at every $\mu_2>\mu_1$
by extension by zero. So the true minimum is *non-increasing* in $\mu$ — and the printed
column increases in $\mu$ by a factor of 36. That is a one-line argument, needs no code,
and contradicts the table on its face. **The cheapest independent instrument is a
theorem about the shape of the answer, not a second computation.**

---

## Two practices, which is what a reader should take from this

### 1. Run a cheap independent instrument before the expensive one

Before committing to the expensive check — a formalisation, a long proof, a rewrite — spend
minutes on an independent one that could disagree with it. Independent means it does not
consume the statement under test: evaluate both sides numerically at a separating instance,
take a degenerate limit where the answer is known, check a dimension or an order of
magnitude by hand.

mg-57a2 caught the false potential **numerically, before writing a line of Lean**: its own
candidate formula matched the true value to 1e-13 where the note's matched to two
significant figures. Minutes of arithmetic told it that the expensive instrument was about
to be pointed at the wrong statement.

This is not a Lean rule. The value is not that the cheap check is a proof — it is not — but
that it is *pointed at the statement itself* rather than at the statement's consequences,
which is the only place this class is visible. Two significant figures is a failed check,
not a passed one; when the agreement is that bad, stop and find out why.

### 2. Machine-check the claim that nothing downstream moves; do not argue it

When a correction lands, the tempting sentence is "and nothing else changes". Prove it.

mg-57a2 did: the corrected $\epsilon$ still yields Lemma 3.2's (3.3) with the same constant
$6c$, hence the same $B_1$, $B_2$, $K_P(c)$ — machine-checked, not asserted. Concretely,
find every point at which the corrected object is consumed, and check the consuming
statement against the corrected object rather than against the argument that nothing about
it moved.

The reason this matters: **a no-op claim is exactly the shape a reviewer waves through.** It
carries no visible risk, it makes no new assertion, and it arrives attached to a repair that
is manifestly an improvement. Nobody argues with it, so nothing tests it — the same blind
spot that let the defect in, now applied to the fix. *The claims most worth proving are the
ones nobody would challenge.*

---

## The two standing checks, together

| check | question | when |
|---|---|---|
| the house rule | *Is the statement false for $-W_\lambda$?* If not, it is sign-blind, and it is not evidence about the direction of an inequality however sharp it is. | every load-bearing statement; each note's closing house-rule section |
| this one | *Does the printed statement say what the argument beneath it proves?* Cheap instrument first; then machine-check the no-op. | before formalising, and whenever a correction lands |

They fail in opposite directions and neither substitutes for the other: the house rule
catches a true statement being read for more than it says, this one catches a statement
that was never what its argument gave.

*The house rule applied to this note:* the fourth instance is the one place where it
bites. Its damage landed in a statement that is **not** sign-blind — Theorem 1's
inequality — and it got there through machinery that is entirely sign-blind. There is
otherwise no mathematical statement here for
$-W_\lambda$ to act on. It is method, and it is sign-blind in the only sense available to
it — nothing above becomes false, or true, if the sign of $W_\lambda$ is reversed.
