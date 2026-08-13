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

## Three runs, three instances

| run | what it found |
|---|---|
| mg-a087 | Lemma 5.1's hypothesis "$\Phi$ analytic at $x=1$" was doing two independent jobs; the note's weakening — "boundedness near $x=1$ would do" — named one of them. |
| mg-7fc6 | `cor:upper` was printed without $\mu^{-1}\log(1-\chi_2)\to-4\pi$, the hypothesis that carries the $4\pi$ — which revealed that the unconditional chain rests on **two** imports where the ledger said one. |
| mg-57a2 | [`dilate-sum.md`](dilate-sum.md) Lemma 3.1's Liouville potential was **false**: printed $(c^2-\chi+1)/(x^2-1)$, true $(c^2-\chi)/(x^2-1)+1/(x^2-1)^2$. It had propagated to [`band-edge-connection.md`](band-edge-connection.md), [`h1-mean-value.md`](h1-mean-value.md) and [`verify_q2.py`](verify_q2.py)'s CHECK 1 banner. |

All three are recorded in full where they were found — [`lean/README.md`](../lean/README.md)
§"What formalising changed in the informal statements", items 1, 4 and 7 — and this note
does not re-audit them.

Three runs, three defects in what a statement says, and no run has yet found a conclusion
that was wrong. (Item 7 there records mg-57a2's as
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

*The house rule applied to this note:* there is no mathematical statement here for
$-W_\lambda$ to act on. It is method, and it is sign-blind in the only sense available to
it — nothing above becomes false, or true, if the sign of $W_\lambda$ is reversed.
