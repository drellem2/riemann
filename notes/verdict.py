"""The exit-code contract shared by the `notes/verify_*.py` scripts (mg-5995).

WHY THIS EXISTS

Those scripts are reports.  They print a table and the verdict lives in a cell:
`verify_q1.py` prints `REFUTED`, `verify_independent_recheck.py` prints
`MISMATCH`, `verify_semilocal_gap.py` prints `NO`.  Until mg-5995 every one of
them returned 0 whatever the cell said, so

    python verify_q1.py; echo $?

printed 0 whether the check passed or refuted itself.  `README.md` invites a
stranger to run exactly that command, which made it a reproduction command that
could not fail.  CI worked around it by grepping the captured output for
`Traceback|REFUTED|MISMATCH`; that grep stays, as a second line of defence, but
it is not the contract.  This module is.

WHAT IT DOES NOT DO

It does not change what any script prints.  On a passing run this module writes
nothing to stdout or stderr and exits 0, so the tables the corpus cites by line
are byte-identical to what they were.  On a failing run it exits 1 and writes
the list of failed checks to STDERR, leaving stdout alone.

USAGE

    from verdict import Verdict
    V = Verdict()

    # (a) a verdict word that is already printed into a table cell: the word and
    #     the exit code are then computed from the same boolean, and cannot
    #     drift apart.
    ok = V.word(worst <= E_proved(c), "ok", "REFUTED",
                "CHECK 2: E_obs <= E(c) proved (c=%s, n=%d)" % (c, n))
    print(... ok)

    # (b) a claim the script states in its own prose but prints only as numbers.
    V.check(r1 <= 1, "CHECK 2: sup x|W| <= B_1 |Phi(1)| (c=%s, n=%d)" % (c, n))

    ...
    V.finish()          # last line of __main__: exits 1 if anything failed

WHAT TO WIRE, AND WHAT NOT TO

Wire a check only where the script itself decides something: a printed verdict
word, an explicit "X refutes the lemma" in its own prose, or a residual it says
must vanish.  Do NOT invent a threshold for a quantity a script explicitly
reports rather than bounds, and do NOT wire a cell that is documented as allowed
to fail -- `(FAILS)` in `verify_q1.py` CHECK 5 (chi_8 >= c^2 at small c) and the
`(not geometric)` cells of `verify_prolate_rate.py` CHECK 3 are both expected,
and `README.md` records them as such.  A check nobody can fail is the defect
this module exists to fix; a check that fires on a documented exception is the
same defect with the sign flipped.

PROVING THE CONTRACT CAN FAIL

A test that has never been observed failing is not known to work.  Set

    VERIFY_SELFTEST_FORCE_FAIL=1        # force the 1st decision negative, exit 1 at once
    VERIFY_SELFTEST_FORCE_FAIL=7        # force the 7th
    VERIFY_SELFTEST_FORCE_FAIL=all      # force every decision, run to the end, exit 1

The integer form exits as soon as the forced decision is reached, so it is a
per-script positive control that costs seconds even for the scripts whose full
grid runs for twenty minutes.  `test_exit_codes.py` runs it for every script.
"""

import os
import sys

ENV = "VERIFY_SELFTEST_FORCE_FAIL"


class Verdict(object):
    """Records the decisions a verify script makes, and exits accordingly."""

    def __init__(self, script=None):
        self.script = script or os.path.basename(sys.argv[0]) or "verify"
        self.decisions = 0
        self.failures = []
        raw = os.environ.get(ENV, "").strip().lower()
        self.force_all = raw == "all"
        self.force_at = None
        if raw and not self.force_all:
            try:
                self.force_at = int(raw)
            except ValueError:
                raise SystemExit("%s must be a positive integer or 'all', not %r"
                                 % (ENV, raw))
            if self.force_at < 1:
                raise SystemExit("%s must be >= 1, not %d" % (ENV, self.force_at))

    # --- recording ------------------------------------------------------------

    def _record(self, ok, what):
        self.decisions += 1
        forced = self.force_all or self.decisions == self.force_at
        if forced:
            ok = False
            what = "%s   [FORCED NEGATIVE by %s]" % (what, ENV)
        if not ok:
            self.failures.append("#%d  %s" % (self.decisions, what))
        if forced and not self.force_all:
            # positive control: stop at the forced decision rather than running
            # the remaining hours of grid.
            self.finish()
        return ok

    def check(self, ok, what):
        """Record a claim the script makes.  Returns the boolean, unchanged."""
        return self._record(bool(ok), what)

    def word(self, ok, good, bad, what=None):
        """Record a claim and return the word to print for it."""
        return good if self._record(bool(ok), what or bad) else bad

    # --- the exit code --------------------------------------------------------

    def finish(self):
        """Exit 1 if any recorded decision came out negative, 0 otherwise."""
        if not self.failures:
            sys.exit(0)
        sys.stdout.flush()
        sys.stderr.write("\n%s: %d of %d checks FAILED\n"
                         % (self.script, len(self.failures), self.decisions))
        for f in self.failures:
            sys.stderr.write("    %s\n" % f)
        sys.stderr.flush()
        sys.exit(1)
