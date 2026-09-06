#!/usr/bin/env bash
# Verify every http(s) URL in the given files resolves (HTTP < 400).
# Usage: scripts/check_links.sh research/*.md data/**/*.yaml
#   .md   : every http(s) URL in the text is checked.
#   .yaml : only `url:` values are checked (SPEC.md V-20 — sources[].url);
#           quoted or unquoted, block or flow style.
# URLs are de-duplicated across all given files, so `checked=N` is the number
# of distinct URLs. Exit code 1 if any link fails. Prints FAIL lines and a
# summary. Known bot-blocked or template URLs live in scripts/link_allowlist.txt
# (one exact URL per line; lines starting with # are comments).
set -u
here=$(cd "$(dirname "$0")" && pwd)
allow="$here/link_allowlist.txt"
fail=0; total=0; allowed=0
declare -A seen
for f in "$@"; do
  case "$f" in
    *.yaml|*.yml)
      # url: value   |  - url: value  |  {url: value, ...}
      urls=$(grep -oE '(^|[{ ,-])url:[[:space:]]*["'"'"']?https?://[^][ <>"'"'"'`)},]+' "$f" \
             | sed -E 's/^.*url:[[:space:]]*["'"'"']?//' | sed -E 's/[.,;:]+$//' | sort -u)
      ;;
    *)
      # ']' first in the negated class so it is literal; strip trailing punctuation
      urls=$(grep -oE 'https?://[^][ <>"'"'"'`)]+' "$f" | sed -E 's/[.,;:]+$//' | sort -u)
      ;;
  esac
  for u in $urls; do
    [ -n "${seen[$u]:-}" ] && continue
    seen[$u]=1
    total=$((total+1))
    code=$(curl -sL -o /dev/null -w '%{http_code}' --max-time 25 \
      -A 'Mozilla/5.0 (map-of-ai link checker)' "$u" 2>/dev/null) || code=000
    # a timeout mid-redirect leaves curl's partial code (e.g. 302) with rc!=0;
    # treat any non-2xx/3xx-final as failure by requiring rc==0 above.
    [[ "$code" =~ ^[0-9]{3}$ ]] || code=000
    if [ "$code" -ge 400 ] || [ "$code" -eq 0 ]; then
      if [ -f "$allow" ] && grep -v '^#' "$allow" | grep -qxF "$u"; then
        allowed=$((allowed+1)); continue
      fi
      echo "FAIL $code $f $u"
      fail=$((fail+1))
    fi
  done
done
echo "checked=$total failed=$fail allowlisted=$allowed"
[ "$fail" -eq 0 ]
