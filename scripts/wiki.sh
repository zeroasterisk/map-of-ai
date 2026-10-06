#!/usr/bin/env bash
# Fetch plain-text extract of a Wikipedia article (for fact checking).
# Usage: scripts/wiki.sh "Dartmouth_workshop" [chars]
#
# P0-T1: survives parallel agents. Behaviour:
#   - on-disk cache under .cache/wiki/<title>.json (repo-relative); a cache
#     hit never touches the network. Set WIKI_NOCACHE=1 to bypass.
#   - retry with exponential back-off (plus Retry-After when Wikipedia sends
#     it) on HTTP 429 and 5xx, up to WIKI_RETRIES (default 6) attempts.
#   - a polite fixed pause WIKI_PAUSE (default 0.5 s) after every network
#     fetch so a tight loop stays under Wikipedia's rate ceiling.
#   - descriptive User-Agent with contact URL, as Wikimedia's policy asks.
# Exit code 0 on success (extract printed), 1 if every attempt failed.
set -u
title="$1"; n="${2:-3000}"
here=$(cd "$(dirname "$0")" && pwd)
cache_dir="${WIKI_CACHE_DIR:-$here/../.cache/wiki}"
retries="${WIKI_RETRIES:-6}"
pause="${WIKI_PAUSE:-0.5}"
ua='map-of-ai research bot (https://github.com/zeroasterisk/map-of-ai)'
url="https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&redirects=1&titles=${title}"

mkdir -p "$cache_dir"
key=$(printf '%s' "$title" | tr -c 'A-Za-z0-9._-' '_')
cache="$cache_dir/$key.json"

print_extract() {
  python3 -c "import sys,json; p=json.load(open(sys.argv[1]))['query']['pages']; print(list(p.values())[0].get('extract','(no page)')[:$n])" "$1"
}

if [ -z "${WIKI_NOCACHE:-}" ] && [ -s "$cache" ] && print_extract "$cache" >/dev/null 2>&1; then
  print_extract "$cache"; exit 0
fi

tmp=$(mktemp); hdr=$(mktemp)
trap 'rm -f "$tmp" "$hdr"' EXIT
attempt=0; delay=2
while [ "$attempt" -lt "$retries" ]; do
  attempt=$((attempt+1))
  code=$(curl -s -A "$ua" -D "$hdr" -o "$tmp" -w '%{http_code}' --max-time 30 "$url" 2>/dev/null || echo 000)
  sleep "$pause"
  if [ "$code" = "200" ] && print_extract "$tmp" >/dev/null 2>&1; then
    cp "$tmp" "$cache"; print_extract "$cache"; exit 0
  fi
  ra=$(grep -i '^retry-after:' "$hdr" | tr -dc '0-9' | head -c 4)
  wait_s=$delay
  if [ -n "$ra" ] && [ "$ra" -gt "$wait_s" ] 2>/dev/null; then wait_s=$ra; fi
  echo "wiki.sh: HTTP $code for '$title' (attempt $attempt/$retries); retrying in ${wait_s}s" >&2
  sleep "$wait_s"
  delay=$((delay*2)); [ "$delay" -gt 60 ] && delay=60
done
echo "wiki.sh: giving up on '$title' after $retries attempts (last HTTP $code)" >&2
exit 1
