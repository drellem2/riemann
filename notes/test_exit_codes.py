#!/usr/bin/env python3
"""The positive control for the exit-code contract of `verdict.py` (mg-5995).

    cd notes && python test_exit_codes.py            # ~2 minutes
    cd notes && python test_exit_codes.py verify_q1.py    # one script

A test that has never been observed failing is not known to work.  Every
`verify_*.py` script now decides something and exits 1 when the decision comes
out negative -- so for each of the fifteen this runs the script with

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

Exit status: 0 if every script passed both controls, 1 otherwise.
"""

import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))

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
]

# the negative control: fast enough to run in full inside a test.
CLEAN = ["verify_semilocal_gap.py", "verify_sign_claims.py", "verify_prolate_claims.py"]


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
    bad = []

    print("POSITIVE CONTROL -- the first decision forced negative, per script")
    print("%-34s %8s %6s  %s" % ("script", "exit", "s", "the check it stopped on"))
    for script, args, env_extra in scripts:
        p, dt = run(script, args, env_extra, forced=True)
        err = p.stderr.decode("utf-8", "replace")
        named = [ln.strip() for ln in err.splitlines() if "FORCED NEGATIVE" in ln]
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
        if p.returncode != 0:
            bad.append("%s: unforced run exited %d" % (script, p.returncode))
            sys.stderr.write(p.stderr.decode("utf-8", "replace"))
        print("%-34s %8d %6.1f" % (script, p.returncode, dt))

    print()
    if bad:
        print("FAILED:")
        for b in bad:
            print("    %s" % b)
        return 1
    print("every script tested has a reachable failing exit path, and the "
          "unforced runs exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
