#!/usr/bin/env bash
# Verify every http(s) URL in the given markdown files resolves (HTTP < 400).
# Usage: scripts/check_links.sh research/*.md
# Exit code 1 if any link fails. Prints FAIL lines and a summary.
# Known: openai.com returns 403 to curl; such URLs are listed in scripts/link_allowlist.txt
set -u
here=$(cd "$(dirname "$0")" && pwd)
allow="$here/link_allowlist.txt"
fail=0; total=0; allowed=0
for f in "$@"; do
  # ']' first in the negated class so it is literal; strip trailing punctuation
  urls=$(grep -oE 'https?://[^][ <>"'"'"'`)]+' "$f" | sed -E 's/[.,;:]+$//' | sort -u)
  for u in $urls; do
    total=$((total+1))
    code=$(curl -sL -o /dev/null -w '%{http_code}' --max-time 25 \
      -A 'Mozilla/5.0 (map-of-ai link checker)' "$u" 2>/dev/null || echo 000)
    if [ "$code" -ge 400 ] || [ "$code" -eq 0 ]; then
      if [ -f "$allow" ] && grep -qxF "$u" "$allow"; then
        allowed=$((allowed+1)); continue
      fi
      echo "FAIL $code $f $u"
      fail=$((fail+1))
    fi
  done
done
echo "checked=$total failed=$fail allowlisted=$allowed"
[ "$fail" -eq 0 ]
