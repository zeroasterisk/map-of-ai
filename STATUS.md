# STATUS — end of session 2026-09-06

## What exists in the repo

| File | State | Notes |
|---|---|---|
| `BRIEF.md` | Alan's verbatim intent | unchanged |
| `PROJECT_PLAN.md` | draft for review | goal restatement, 5 phases, 8 milestones, 7 open decisions, risks |
| `AXES.md` | proposal for decision | X origin + non-linear scale; 5 Y candidates compared; recommendation |
| `ALTITUDES.md` | proposal for decision | 4 zoom levels with entity types, counts, worked examples, data-model sketch |
| `SOURCING.md` | draft; endpoints probed | 3 source tiers with live curl status, monthly cadence, filters, triangulation, aging rules |
| `research/01`–`08` | **verified** (links) / first-draft (coverage) | 8 era files, ~1,250 lines, 10–30 timeline rows each, numbered sources |
| `research/09-cross-cutting-threads.md` | verified (links) | 8 threads (RL, robotics, safety, compute, open/closed, NLP, vision, games) with dated milestones |
| `research/TEMPLATE.md` | stable | template every era file follows |
| `scripts/check_links.sh` | working | 737 URLs checked across repo; 0 failures outside the documented allowlist |
| `scripts/wiki.sh` | working | Wikipedia plaintext fetch for fact-checking (no retry; API 429s after ~25 rapid calls) |
| `scripts/link_allowlist.txt` | | URLs known to block bots (openai.com HTML) or template/API URLs |

Commits are incremental on `main`; nothing is uncommitted.

## What "verified" means here, honestly

- **Verified:** every URL in the file resolves (HTTP < 400) and the writing
  agent cross-checked each date/name against the fetched Wikipedia extract or
  primary paper (Crossref/arXiv) before writing it. Several draft claims were
  corrected in the process (e.g. SAIL founding year, Alvey dates, FGCS end).
- **Not yet verified:** *coverage*. Nobody has yet asked "what important thing
  is missing from this era?" That review is the next content task and should
  be done by a different model or a human, not by the authors.
- **Provisional:** `research/08` has an explicit "Needs verification (recent,
  mid-2025 → Sept 2026)" section. Those items are single-sourced from
  Wikipedia extracts and must go through the `SOURCING.md` triangulation
  before they get map positions. Everything east of ~mid-2025 should be
  treated as frontier haze.
- The research files were written by three parallel model runs against a
  shared template. Voice and density vary by file (01–03 lean academic;
  06–08 lean dense). A copy-edit pass for a single voice is Phase 3 work.

## Decisions Alan needs to make

1. **Y axis.** Recommended: reasoning ↔ embodiment in five bands (Candidate E),
   with symbolic ↔ learned as terrain biome and open ↔ closed as an eastern
   overlay. Fallback: symbolic ↔ connectionist (Candidate A) with the
   mitigations in `AXES.md` §4. The argument that decides it: A is
   time-correlated and leaves the 2012–present half of the map with no
   vertical structure; E populates every era top to bottom and agrees with A
   on the west half anyway.
2. **X origin.** Recommended: mainland coast at 1943 (McCulloch–Pitts), with
   1936 Turing / Gödel / Boole / Leibniz as an off-shore archipelago.
3. **X scale.** Piecewise (widths per year growing eastward) vs. density-
   weighted. Rendering decision; principle (non-linear, with a visible year
   graticule) proposed now.
4. **Altitudes.** Ship A1–A3 everywhere, A4 only for 2017+ initially.
5. **Naming.** Evocative region names ("The Statistical Isthmus") with neutral
   subtitles, or neutral only.
6. **Scope edge.** Include OR / control theory / computational neuroscience /
   HCI as coastal territories, or leave them as sea?
7. **Frontier review.** Who signs off the monthly intake.

## Recommended next steps (in order)

1. Alan reads `AXES.md` §3 and decides 1–2 above. Everything downstream
   depends on it. Suggested validation before committing: sketch four vertical
   slices (1965, 1990, 2015, 2025) on paper under the chosen axis and check
   that neighbours feel right.
2. Coverage review of `research/01`–`09` by a second model with a different
   training cut, prompt: "list ten things a historian of AI would expect in
   this era that are absent". Add, source, re-run `check_links.sh`.
3. Fix the `data/` schema (`ALTITUDES.md` §7) and author A1 + A2 entities for
   all nine continents (~60 countries). This converts prose into positions and
   is the first point where the map can be drawn at all.
4. Run one frontier intake for 2026-08 end-to-end per `SOURCING.md` to test
   the cadence and produce `research/frontier/2026-08.md`. Get a Semantic
   Scholar API key; write a scraper or manual checklist for Anthropic / Meta /
   xAI which have no bot-readable feed.
5. Author A3 cities (~400) with band + biome + parent.
6. Phase 4 spike in parallel with 5: one continent (Deep Learning Basin is
   densest and best-sourced) rendered at three altitudes.

## How the visual map would eventually be built (plan only, not started)

- **Content → data.** Markdown research stays the human-readable source of
  truth; a `data/` directory of YAML entities (one per A1–A4 item) carries
  positions, band, biome, parent, sources, status. A build script validates
  that every entity has sources and a parent, and that no A3 point sits
  outside its A2 polygon.
- **Layout.** A1/A2 polygons are hand-drawn by the curator (SVG/GeoJSON in a
  vector editor or a small in-browser tool). A3/A4 points are placed inside
  their parent by the curator; an automated local relaxation step only
  removes overlaps. Algorithms nudge; humans decide neighbourhood. This is the
  mapofmetal approach and the reason it looks curated rather than generated.
- **Terrain.** Biome polygons plus noise, hillshade and coastline treatment
  rendered offline into a raster tile pyramid (Python/PIL or Blender or a
  hand-painted layer in Procreate/Photoshop for the "loved" look), one
  pyramid per altitude range.
- **Engine.** MapLibre GL JS with a custom style: raster terrain underneath,
  vector layers for borders, rivers/roads (cross-cutting threads), labels
  with proper collision handling and zoom-dependent visibility. Fallback:
  Leaflet + image pyramid if we decide vector labels are more trouble than
  they're worth for a first release.
- **Interaction.** Click region → side panel with the mapofmetal-style
  write-up and a "notable places" list; click city → card with summary,
  dates, sources; search box; year slider that highlights a vertical band;
  toggles for threads and the open/closed overlay; "frontier haze" style for
  provisional items.
- **Delivery.** Static build to GitHub Pages; monthly `frontier:` commits
  trigger a rebuild.

## Known issues / tooling notes

- `scripts/wiki.sh` has no back-off; parallel agents hit Wikipedia 429s. Add
  a sleep/retry or move to a cached fetcher before the coverage review.
- Publisher DOI landing pages (ACM, OUP, MIT Press, Science, AAAI) return 403
  to curl. The files cite the DOI as text and link an open mirror or
  Wikipedia; this is fine but worth knowing when adding sources.
- One subagent run crashed after writing `research/04` (file is complete and
  passes checks) — no content lost, noted for transparency.
- OpenReview API is 403 to bots; ICLR proceedings need a browser or a key.
