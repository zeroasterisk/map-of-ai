#!/usr/bin/env bash
# Run scripts/validate.py against every fixture and compare with EXPECTED.txt.
# Usage: scripts/fixtures/run.sh            # compare, exit 1 on diff
#        scripts/fixtures/run.sh --update   # rewrite EXPECTED.txt
#
# Layout: fixtures/valid/ is a complete mini data root that must validate
# clean; fixtures/invalid/<rule>/ is a copy of it with exactly one violation
# of <rule>. A file FLAGS in a case dir adds validator flags for that case
# (V-32 needs --require-children). Every case except V-20 runs --offline;
# V-20 is the only network rule, so its case runs online (skipped when
# FIXTURE_OFFLINE=1 is set).
set -u
here=$(cd "$(dirname "$0")" && pwd)
repo=$(cd "$here/../.." && pwd)
val="$repo/scripts/validate.py"
out=$(mktemp); trap 'rm -f "$out"' EXIT

{
  echo "## valid"
  (cd "$repo" && "$val" --offline scripts/fixtures/valid; echo "exit=$?")
  for d in "$here"/invalid/*/; do
    rule=$(basename "$d")
    flags="--offline"
    [ "$rule" = "V-20" ] && flags=""
    [ -f "$d/FLAGS" ] && flags="$flags $(cat "$d/FLAGS")"
    if [ "$rule" = "V-20" ] && [ -n "${FIXTURE_OFFLINE:-}" ]; then
      echo "## $rule (skipped: FIXTURE_OFFLINE)"; continue
    fi
    echo "## $rule"
    # shellcheck disable=SC2086
    (cd "$repo" && "$val" $flags "scripts/fixtures/invalid/$rule" | grep -E '^FAIL' | sed 's#scripts/fixtures/invalid/##'; echo "exit=${PIPESTATUS[0]}")
  done
} > "$out"

if [ "${1:-}" = "--update" ]; then
  cp "$out" "$here/EXPECTED.txt"; echo "EXPECTED.txt updated"; exit 0
fi
if diff -u "$here/EXPECTED.txt" "$out"; then
  echo "fixtures: OK ($(grep -c '^## V-' "$out") invalid cases + valid set match EXPECTED.txt)"
else
  echo "fixtures: MISMATCH"; exit 1
fi
