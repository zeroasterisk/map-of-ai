# Coverage review brief (PLAN.md P1-T1…P1-T9) — instructions for the reviewing agent

You are a *reviewer who did not write this file*. Repo: /home/node/map-of-ai (already cloned; do NOT run git commit/push/pull/stash — the orchestrator commits). Work only in the files named in your task. Do not edit scripts/link_allowlist.txt; if a needed source host blocks curl, say so in your final summary with the exact URL and reason.

## Read first
1. research/TEMPLATE.md (section order and rules)
2. SPEC.md §4.1 (R-01…R-07) and §4.5 (A-R1…A-R5), §2.9 (adjacent-field scope rule: control theory, cybernetics-as-engineering, OR, cog-sci, neuroscience, HCI, statistics, pure theory of computation get NO territory of their own; a specific item from them is in only if it directly fed an AI milestone — then note what it fed)
3. Your research file, top to bottom.

## Tools
- scripts/wiki.sh "Article_Title" [chars] — cached, rate-limited Wikipedia plain-text extract. Use it for fact-checking every date/name you add. Prefer it over raw curl.
- scripts/check_links.sh research/0N-*.md — must end with failed=0.
- scripts/check_research.py research/0N-*.md — prints PASS/FAIL for R-01…R-07 (R-07 needs your report under data/reviews/).
- curl for primary sources (arXiv abs pages, DOIs, lab blogs) when confirming.

## Procedure
1. Candidate generation. Answer, in writing, the prompt: "List at least ten things a historian of AI would expect in <this era> that are absent from this file; for each, cite one authoritative source." Aim for 12–15 candidates so ≥10 survive. Think across: systems, papers, people, institutions/labs, datasets/benchmarks, events/conferences, funding/policy events, controversies, non-US work (UK, France, Germany, USSR, Japan, China), hardware/compute, and the file's own "Schools of thought" borders. Check each candidate really is absent (grep the file for the name AND obvious variants).
2. Verify each candidate you intend to add: fetch the Wikipedia article via wiki.sh and/or the primary source; confirm the year and the claim. No date or name goes in without a source you actually fetched.
3. Disposition each candidate exactly one of:
   - added — you add it to the file (timeline row and/or key-people/key-paper bullet and/or school bullet), with a NEW numbered source appended to ## Sources in the format `[n] Title — URL (accessed 2026-09-06)`. Continue the file's numbering; never renumber existing sources.
   - folded — it belongs inside an existing row/bullet: edit that row/bullet to mention it (and add a source if a new claim is introduced).
   - rejected — out of scope (SPEC §2.9), belongs to another era file (say which), or too minor for A1–A3; one-line reason.
   Every disposition needs a one-line reason.
4. Also fix anything mechanical the checker flags (R-04 unreferenced sources: cite them somewhere sensible or remove them if truly unused; R-06 bullets lacking `borders:`: add a borders clause).
5. Set the frontmatter line to `> **Status:** reviewed`.
6. Write the review report at data/reviews/2026-09-06-research-0N.md with EXACTLY this structure:

```
# Review: research/0N-<name>.md (coverage, PLAN.md P1-Tn)

- Scope: research/0N-<name>.md
- Reviewer: <your model name as you know it; if unsure write "Hermes subagent (reviewer role), model per session config"> — reviewer role only; the file's git author is "Hermes Agent <agent@hermes.local>" (writing role, earlier session)
- Date: 2026-09-06
- Commit reviewed: <output of `git rev-parse HEAD` at the moment you started>

## Criteria (SPEC.md §4.1)

| ID | Result | Evidence |
|---|---|---|
| R-01 | PASS/FAIL | one line |
| R-02 | PASS/FAIL | one line |
| R-03 | PASS/FAIL | paste the check_links.sh summary line |
| R-04 | PASS/FAIL | one line |
| R-05 | PASS/FAIL | one line |
| R-06 | PASS/FAIL | one line (bullet count) |
| R-07 | PASS/FAIL | "N candidates: a added, f folded, r rejected" |

## Candidate omissions (≥ 10)

| # | Candidate | Source checked | Disposition | Reason / where it went |
|---|---|---|---|---|
| 1 | ... | URL | added | timeline row 19xx + source [nn] |
...

## Other edits
- bullet list of mechanical fixes (R-04/R-06 etc.)

## Notes for continent/country authoring
- 2–5 bullets: anything the reviewer noticed about the "Map notes" placement that Phase 2 should know (wrong school boundary, an item that should be a city, etc.)
```

Results after your edits must be: `scripts/check_research.py research/0N-*.md` → every criterion PASS (R-03 included: run it with links on), and `scripts/check_links.sh research/0N-*.md` → failed=0.

## Quality bar (Alan's explicit priority: "get the history correct")
- Accuracy over speed. If you cannot verify a date, do not add the item; reject it with reason "could not verify".
- Do not pad with trivia; each added item must plausibly be a city (A3) or affect a country (A2) on a map of AI.
- Keep the file's voice: terse, factual, "why it matters" column filled.
- Never invent URLs. Only cite URLs you fetched (200) in this session.

## Final summary to return (keep under 40 lines)
- Path of the report; counts added/folded/rejected
- The list of added items (year — item — source number)
- Output of scripts/check_research.py for the file (all lines)
- Any URL that needs allowlisting and why
- Anything you were unsure about
