#!/usr/bin/env python3
"""The positive control for the exit-code contract of `verdict.py` (mg-5995).

    cd notes && python test_exit_codes.py            # ~2 minutes
    cd notes && python test_exit_codes.py verify_q1.py    # one script

A test that has never been observed failing is not known to work.  Every
`verify_*.py` script now decides something and exits 1 when the decision comes
out negative -- so for each of the eighteen this runs the script with

    VERIFY_SELFTEST_FORCE_FAIL=1

which forces the FIRST decision it reaches to come out negative, and requires
that the process exit non-zero and name the forced check on stderr.  Two things
that would silently defeat the contract are caught by that:

  * a script that imports `verdict` but never calls `check`/`word` reaches no
    forced decision at all, runs to the end and exits 0 -- reported as a
    failure here, not as a pass;
  * a script that records failures but never calls `VD.finish()` exits 0 too.

The forced run stops at the first decision, so this costs seconds even for the
scripts whose full grid runs for twenty minutes.  It therefore proves the wiring
of the first decision in each script, and the machinery those decisions all
share; it does not re-derive every later call site.  `VERIFY_SELFTEST_FORCE_FAIL
=all` forces every decision in a script and runs to the end, which does exercise
all of them, and is what to reach for when changing a script's checks.

The negative control is the other half: the three fastest scripts are also run
unforced and must exit 0.  Without it a contract that failed everything would
pass every test above.

A third, STATIC control runs before either, and it is the one that replaced CI's
output grep (mg-a682).  Both forced controls above stop at the FIRST decision, so
neither says anything about a verdict word printed by a later one -- and the old
`grep -E 'Traceback|REFUTED|MISMATCH' run.log` in `.github/workflows/verifiers.yml`
was what covered that case.  That grep could not tell a verdict from prose about
one, because they are the same bytes: `verify_sonin_margin.py` documents two
readings mg-0b7a refuted, printed those three sentences, and turned `main` red
while exiting 0.  So the distinction is drawn where it is structural instead --
in the SOURCE, not in the output:

  * a verdict is the word ALONE, as a value: `VD.word(ok, "ok", "REFUTED", ...)`;
  * prose about a verdict is the word inside a sentence, and a sentence is never
    equal to the word.

`wiring_failures` requires every string literal equal to a verdict word to be an
argument of a `.word(...)` call, so prose may contain `REFUTED` freely and a bare
`print("REFUTED")` -- the mg-5995 defect, a cell that reports a refutation and
exits 0 -- is a failure here.  It also requires each script to END in
`VD.finish()`, since a script that records a later failure and never reaches
`finish()` exits 0 and neither forced control would notice.

Being static it needs no imports, so it runs before the environment check and its
verdict is about the source rather than about this machine.

A script that never ran is not a script whose contract is broken, and the two
must not be reported the same way.  On a machine without `mpmath` installed
every one of the eighteen dies at import and exits 1, which looks exactly like
eighteen broken contracts unless something says otherwise -- and that reading is
worse than the truth, because the fix is one `pip install`.  So the imports the
selected scripts need are checked BEFORE anything is run, and any child that
dies of `ModuleNotFoundError` anyway (a sibling import this scan did not follow,
a module installed but broken) is reported as an environment failure rather than
as a contract failure.  A module that is present but too old is the same case
wearing different clothes and is checked the same way -- see `FLOORS`.

Exit status: 0 if every script passed all three controls, 1 if any contract
failed, 2 if the environment is missing something and the RUN controls were
therefore not tested.  A 2 is not a result about the contract; it means the runs
did not happen.  The static control has run by then either way.
"""

import ast
import importlib.util
import os
import subprocess
import sys
import time
import warnings

HERE = os.path.dirname(os.path.abspath(__file__))

# what `pip install` line to point at when an import is missing; this is the one
# README.md gives under "Reproducing the same checks locally".
PIP_LINE = 'pip install "numpy>=2.0" "mpmath>=1.3"'

# the third-party modules any of these scripts import.  Everything else they
# import is either the standard library or a sibling in this directory.
THIRD_PARTY = ("numpy", "mpmath")

# the oldest version of each that these scripts are run against, as (major,
# minor); README.md, "The versions these scripts are run on", is the statement
# of record.  An installed-but-too-old module is checked here for the same
# reason a missing one is: on numpy 1.x every script that calls `np.trapezoid`
# dies of an `AttributeError` -- not an `ImportError`, so `import_error` below
# does not see it -- and gets counted as a broken contract.  It is not one.  It
# is this machine, and the fix is the `pip install` line above.
FLOORS = {"numpy": (2, 0), "mpmath": (1, 3)}

# script -> the arguments/environment CI uses, so the forced run reaches its
# first decision on the same grid the workflow runs.
SCRIPTS = [
    ("verify_arch_positivity.py", [], {}),
    ("verify_citation_u8.py", [], {}),
    ("verify_deficit_repair.py", ["--quick"], {}),
    ("verify_dunster.py", [], {}),
    ("verify_h0.py", [], {"QUICK": "1"}),
    ("verify_h1.py", [], {}),
    ("verify_independent_recheck.py", [], {}),
    ("verify_index_convention.py", [], {}),
    ("verify_prolate_claims.py", [], {}),
    ("verify_prolate_rate.py", ["--quick"], {}),
    ("verify_q1.py", ["--quick"], {}),
    ("verify_q2.py", ["--quick"], {}),
    ("verify_q3.py", [], {}),
    ("verify_semilocal_gap.py", [], {}),
    ("verify_sign_claims.py", [], {}),
    ("verify_sonin_trace.py", [], {}),
    ("verify_sonin_margin.py", ["--quick"], {}),
    ("verify_sonin_ceiling.py", ["--quick"], {}),
]

# the negative control: fast enough to run in full inside a test.
CLEAN = ["verify_semilocal_gap.py", "verify_sign_claims.py", "verify_prolate_claims.py"]

# the verdict words that a script prints INSTEAD OF a passing word, i.e. the ones
# whose appearance in a table cell is the script saying the check came out wrong.
# `(FAILS)` and `NO` are deliberately absent, for the same reason they are absent
# from the exit-code contract itself: both mark cells that are EXPECTED to fail
# and that README.md documents as such.  Adding a word here is a claim that no
# passing run may ever print it as a cell.
#
# Note that the line below would fail this file's own check, and the paragraphs
# above it would not -- which is the check working, and is why only `SCRIPTS` is
# scanned.  The remedy is an artefact of the same kind as the defect: what is
# NOT caught is a verdict word assembled rather than written (`"REFUT" + "ED"`,
# an f-string), because then no literal equals the word.  Nothing in the corpus
# does that, and a script that did would be reaching for it.
BAD_WORDS = ("REFUTED", "MISMATCH")


def _is_main_guard(node):
    """True for `if __name__ == "__main__":`."""
    if not isinstance(node, ast.If) or not isinstance(node.test, ast.Compare):
        return False
    t = node.test
    return (isinstance(t.left, ast.Name) and t.left.id == "__name__"
            and len(t.comparators) == 1
            and isinstance(t.comparators[0], ast.Constant)
            and t.comparators[0].value == "__main__")


def _calls(node, attr):
    """True if `node` is a call to something named `.attr(...)`."""
    return (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
            and node.func.attr == attr)


def wiring_failures(scripts):
    """The static control.  A list of what is wrong in the source; [] if nothing.

    Two things, both of which would let a script report a wrong result and exit 0:

      * a verdict word standing alone as a value anywhere other than inside a
        `.word(...)` call -- `print("REFUTED")` decides nothing and exits 0.
        A string that merely CONTAINS the word is prose and is not touched: that
        is the whole distinction the old CI grep could not draw.
      * a script that does not END in `VD.finish()`.  Both forced controls below
        stop at the first decision -- `verdict.py` calls `finish` itself there --
        so a missing `finish()` is invisible to them; a failure recorded by any
        later decision would be dropped on the floor and the script would exit 0.
    """
    out = []
    for script, _, _ in scripts:
        path = os.path.join(HERE, script)
        with open(path) as fh:
            source = fh.read()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", SyntaxWarning)
            tree = ast.parse(source, filename=path)

        wired = set()
        for node in ast.walk(tree):
            if _calls(node, "word"):
                for arg in list(node.args) + [kw.value for kw in node.keywords]:
                    wired.add(id(arg))
        for node in ast.walk(tree):
            if (isinstance(node, ast.Constant) and isinstance(node.value, str)
                    and node.value.strip() in BAD_WORDS and id(node) not in wired):
                out.append("%s:%d: %r stands alone as a value but is not an "
                           "argument of a `.word(...)` call, so printing it "
                           "would not fail the run"
                           % (script, node.lineno, node.value))

        # Two shapes are in use and both are fine: a `__main__` guard whose last
        # statement is `VD.finish()`, and `verify_prolate_claims.py` /
        # `verify_sign_claims.py`, which have no guard and run at module level
        # ending in a top-level `VD.finish()`.  What is checked is the last thing
        # the script executes, whichever shape it is.  (This distinction was
        # measured, not assumed: requiring the guard flagged those two on the
        # first run of this control.)
        mains = [n for n in tree.body if _is_main_guard(n)]
        if len(mains) > 1:
            out.append("%s: %d `if __name__ == \"__main__\":` blocks, expected "
                       "at most 1" % (script, len(mains)))
            continue
        where, body = ("`__main__`", mains[0].body) if mains else ("the module", tree.body)
        last = body[-1]
        if not (isinstance(last, ast.Expr) and _calls(last.value, "finish")):
            out.append("%s:%d: %s does not end in a `.finish()` call, so a "
                       "failure recorded after the first decision would exit 0"
                       % (script, last.lineno, where))
    return out


def imported_names(path):
    """The top-level module names `path` imports, parsed rather than grepped.

    Parsed because a grep for `import mpmath` also matches the prose in
    `verify_dunster.py`'s docstring, and an import this file only imagines is
    exactly the false environment failure it exists to prevent.
    """
    with open(path) as fh:
        source = fh.read()
    with warnings.catch_warnings():
        # several scripts quote LaTeX in a docstring, and `\l` is a SyntaxWarning
        # under 3.12+.  Running them is not this file's business; parsing them is.
        warnings.simplefilter("ignore", SyntaxWarning)
        tree = ast.parse(source, filename=path)
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            names.add(node.module.split(".")[0])
    return names


def requirements(script, _seen=None):
    """The third-party modules `script` needs, following sibling imports.

    Today every script that needs mpmath or numpy imports it directly, so the
    recursion changes no answer.  It is here because eleven of the eighteen import
    another verifier by bare module name: the first one to take a dependency only
    through a sibling would otherwise be cleared to run on a machine that cannot
    run it, and would then be reported as a broken contract, which is the exact
    confusion this file exists to end.
    """
    seen = set() if _seen is None else _seen
    if script in seen:
        return set()
    seen.add(script)
    need = set()
    for name in imported_names(os.path.join(HERE, script)):
        if name in THIRD_PARTY:
            need.add(name)
        elif os.path.exists(os.path.join(HERE, name + ".py")):
            need |= requirements(name + ".py", seen)
    return need


def version_of(mod):
    """(major, minor) of an installed module, or None if it will not be read.

    Only the first two components, and only when both are plain integers: a
    development suffix is not worth a parser here, and a version this cannot
    read is reported as no answer rather than as a failure.
    """
    try:
        parts = __import__(mod).__version__.split(".")
        return (int(parts[0]), int(parts[1]))
    except Exception:
        return None


def check_environment(scripts):
    """Report an unusable environment before running anything; [] if it will do.

    Returns a list of (module, [scripts that need it], what is wrong) for every
    module that is not importable by the interpreter the children will run under
    -- which is this one, since `run` invokes `sys.executable` -- or that is
    importable but older than the floor in `FLOORS`.
    """
    needed = {}
    for script, _, _ in scripts:
        for mod in requirements(script):
            needed.setdefault(mod, []).append(script)
    missing = []
    for mod in sorted(needed):
        try:
            found = importlib.util.find_spec(mod) is not None
        except (ImportError, ValueError):
            found = False
        if not found:
            missing.append((mod, needed[mod], "missing"))
            continue
        floor = FLOORS.get(mod)
        have = version_of(mod) if floor else None
        if floor is not None and have is not None and have < floor:
            missing.append((mod, needed[mod],
                            "%s installed, needs >= %d.%d"
                            % (__import__(mod).__version__, floor[0], floor[1])))
    return missing


def import_error(stderr):
    """The `ModuleNotFoundError`/`ImportError` line in `stderr`, or None.

    The backstop for what `check_environment` cannot see: a module that is
    installed but raises on import, a sibling import added since, a module
    imported inside a function.  A child that died here never reached a decision,
    so it says nothing either way about the exit-code contract.
    """
    for line in reversed(stderr.splitlines()):
        line = line.strip()
        if line.startswith(("ModuleNotFoundError:", "ImportError:")):
            return line
    return None


def run(script, args, env_extra, forced):
    env = dict(os.environ)
    env.update(env_extra)
    if forced:
        env["VERIFY_SELFTEST_FORCE_FAIL"] = "1"
    else:
        env.pop("VERIFY_SELFTEST_FORCE_FAIL", None)
    t0 = time.time()
    p = subprocess.run([sys.executable, script] + args, cwd=HERE, env=env,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p, time.time() - t0


def main(argv):
    wanted = [a for a in argv if not a.startswith("-")]
    scripts = [s for s in SCRIPTS if not wanted or s[0] in wanted]
    if not scripts:
        print("no such script: %s" % ", ".join(wanted))
        return 1

    # The static control first: it needs no imports, so its verdict is about the
    # source and holds on a machine that cannot run anything below.
    print("STATIC CONTROL -- every verdict word is wired, every __main__ ends in finish()")
    wiring = wiring_failures(scripts)
    for w in wiring:
        print("    %s" % w)
    if wiring:
        print()
        print("FAILED -- %d of the %d scripts selected can report a wrong result "
              "and exit 0." % (len({w.split(":")[0] for w in wiring}), len(scripts)))
        return 1
    print("%d scripts: no unwired %s, all end in finish()."
          % (len(scripts), "/".join(BAD_WORDS)))
    print()

    missing = check_environment(scripts)
    if missing:
        print("NOT RUN -- this environment does not have what the scripts need.")
        print()
        for mod, users, why in missing:
            print("    %-8s %s, needed by %d of the %d scripts selected (%s)"
                  % (mod, why, len(users), len(scripts),
                     ", ".join(users) if len(users) <= 3 else
                     ", ".join(users[:3]) + ", ..."))
        print()
        print("    %s" % PIP_LINE)
        print()
        print("Nothing was run, so this says nothing about the exit-code "
              "contract; it is a statement about this machine.")
        return 2

    bad = []
    never_ran = []

    print("POSITIVE CONTROL -- the first decision forced negative, per script")
    print("%-34s %8s %6s  %s" % ("script", "exit", "s", "the check it stopped on"))
    for script, args, env_extra in scripts:
        p, dt = run(script, args, env_extra, forced=True)
        err = p.stderr.decode("utf-8", "replace")
        oops = import_error(err)
        named = [ln.strip() for ln in err.splitlines() if "FORCED NEGATIVE" in ln]
        if oops:
            never_ran.append("%s: %s" % (script, oops))
            what = "(not run -- %s)" % oops
        else:
            ok = p.returncode != 0 and named
            if not ok:
                bad.append("%s: forced run exited %d%s" % (
                    script, p.returncode,
                    "" if named else " and named no forced check on stderr"))
            what = named[0][:90] if named else "(none -- no decision was reached)"
        print("%-34s %8d %6.1f  %s" % (script, p.returncode, dt, what))

    print()
    print("NEGATIVE CONTROL -- the same scripts, unforced, must exit 0")
    for script in CLEAN:
        if wanted and script not in wanted:
            continue
        args, env_extra = [(a, e) for s, a, e in SCRIPTS if s == script][0]
        p, dt = run(script, args, env_extra, forced=False)
        err = p.stderr.decode("utf-8", "replace")
        oops = import_error(err)
        if oops:
            never_ran.append("%s: unforced run: %s" % (script, oops))
        elif p.returncode != 0:
            bad.append("%s: unforced run exited %d" % (script, p.returncode))
            sys.stderr.write(err)
        print("%-34s %8d %6.1f%s"
              % (script, p.returncode, dt, "  (not run -- %s)" % oops if oops else ""))

    print()
    if never_ran:
        print("NOT RUN -- these died before reaching any decision, which is a "
              "fact about this machine and not about the contract:")
        for n in never_ran:
            print("    %s" % n)
        print()
        print("    %s" % PIP_LINE)
        print()
    if bad:
        print("FAILED -- these ran and their contract came out wrong:")
        for b in bad:
            print("    %s" % b)
        return 1
    if never_ran:
        return 2
    print("every script tested has a reachable failing exit path, its verdict "
          "words are wired to it, and the unforced runs exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
