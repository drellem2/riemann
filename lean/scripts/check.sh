#!/usr/bin/env bash
# Build the Lean development and verify that nothing depends on `sorryAx`.
#
# Usage:  lean/scripts/check.sh
#
# Exits non-zero if the build fails, if any `sorry` appears in the sources, or
# if any listed result depends on `sorryAx`.
set -euo pipefail

cd "$(dirname "$0")/.."

if ! command -v lake >/dev/null 2>&1; then
  if [ -x "$HOME/.elan/bin/lake" ]; then
    export PATH="$HOME/.elan/bin:$PATH"
  else
    echo "check.sh: lake not found; install elan (https://github.com/leanprover/elan)" >&2
    exit 127
  fi
fi

echo "== toolchain =="
cat lean-toolchain
echo "mathlib rev: $(git -C .lake/packages/mathlib rev-parse HEAD 2>/dev/null || echo '(not fetched)')"

echo
echo "== grep for sorry in sources =="
# `Axioms.lean` mentions `sorryAx` in its comments; exclude comment lines by
# looking only for the tactic/term `sorry` as a standalone token.
if grep -rnE '(^|[^A-Za-z_])sorry([^A-Za-z_]|$)' Riemann Riemann.lean; then
  echo "check.sh: found 'sorry' in sources" >&2
  exit 1
fi
echo "none"

echo
echo "== build =="
# Capped thread count: this is a shared host.
LEAN_NUM_THREADS="${LEAN_NUM_THREADS:-4}" lake build

echo
echo "== axiom audit =="
out=$(LEAN_NUM_THREADS="${LEAN_NUM_THREADS:-4}" lake env lean Riemann/Axioms.lean)
echo "$out"
if echo "$out" | grep -q sorryAx; then
  echo "check.sh: a result depends on sorryAx" >&2
  exit 1
fi
n=$(echo "$out" | grep -c 'depends on axioms')
echo
echo "check.sh: OK — $n results, none depending on sorryAx"
