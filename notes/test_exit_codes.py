#!/usr/bin/env python3
"""The positive control for the exit-code contract of `verdict.py` (mg-5995).

    cd notes && python test_exit_codes.py            # ~2 minutes
    cd notes && python test_exit_codes.py verify_q1.py    # one script

A test that has never been observed failing is not known to work.  Every
`verify_*.py` script now decides something and exits 1 when the decision comes
out negative -- so for each of the seventeen this runs the script with

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

A script that never ran is not a script whose contract is broken, and the two
must not be reported the same way.  On a machine without `mpmath` installed
every one of the seventeen dies at import and exits 1, which looks exactly like
seventeen broken contracts unless something says otherwise -- and that reading is
worse than the truth, because the fix is one `pip install`.  So the imports the
selected scripts need are checked BEFORE anything is run, and any child that
dies of `ModuleNotFoundError` anyway (a sibling import this scan did not follow,
a module installed but broken) is reported as an environment failure rather than
as a contract failure.  A module that is present but too old is the same case
wearing different clothes and is checked the same way -- see `FLOORS`.

Exit status: 0 if every script passed both controls, 1 if any contract failed,
2 if the environment is missing something and the contract was therefore not
tested.  A 2 is not a result about the contract; it means the run did not happen.
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
]

# the negative control: fast enough to run in full inside a test.
CLEAN = ["verify_semilocal_gap.py", "verify_sign_claims.py", "verify_prolate_claims.py"]


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
    recursion changes no answer.  It is here because nine of the seventeen import
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
    print("every script tested has a reachable failing exit path, and the "
          "unforced runs exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
