#!/usr/bin/env bash
# Fetch plain-text extract of a Wikipedia article (for fact checking).
# Usage: scripts/wiki.sh "Dartmouth_workshop" [chars]
title="$1"; n="${2:-3000}"
curl -s -A 'map-of-ai research bot' \
  "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&redirects=1&titles=${title}" \
  | python3 -c "import sys,json; p=json.load(sys.stdin)['query']['pages']; print(list(p.values())[0].get('extract','(no page)')[:$n])"
