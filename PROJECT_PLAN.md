# PROJECT PLAN — Map of AI

> Source of intent: `BRIEF.md` (Alan Blount, verbatim). This document is the
> plan derived from it. Design decisions live in `AXES.md`, `ALTITUDES.md`,
> `SOURCING.md`; content lives in `research/`; current state in `STATUS.md`.

## 1. Goal, restated

Build a map, in the literal cartographic sense, of the history and present of
AI research. Time runs west to east from the field's origins to the current
month; the north–south position and the terrain encode *what kind* of AI work
something is, so that related schools of thought sit next to each other and a
viewer can navigate by neighbourhood as well as by date. Like a physical map it
has zoom levels: continents (eras/paradigms), countries (schools of thought),
cities (labs, landmark systems and papers), streets (people, individual
papers, models). It is updated monthly at the eastern edge.

The reference is mapofmetal.com: a Google-Maps-style, drag-and-zoom map of
music genres where position encodes lineage and affinity, each region has a
name and a write-up, and the whole thing is obviously made with care. The bar
is the same care in both the cartography and the curation.

Two things make this harder than a timeline, and they are the actual work:

1. **The Y axis and terrain must make intellectual neighbours into geographic
   neighbours in every era**, not just the era that inspired the axis.
2. **The content must be right.** Every date, name and paper is checkable;
   the last twelve months need a sourcing discipline because Wikipedia lags.

## 2. Non-goals (for now)

- Not an exhaustive bibliography. A3 cities are things a well-read
  practitioner recognises; A4 streets are open-ended but curated.
- Not a leaderboard or news site. Monthly updates add what changed the field.
- Not a graph visualisation. Position is authored by curators against fixed
  axes, not computed by a layout algorithm (see Phase 4 for where algorithms
  help without owning the layout).

## 3. Phases

### Phase 1 — Axis design  (this session: proposal delivered)

Deliverables:
- `AXES.md`: X origin and scale; 3–5 Y candidates evaluated; recommendation.
- Decision from Alan on Y axis and X origin.

Status: proposal complete. Recommendation: X mainland starts 1943 with a
pre-1943 archipelago; non-linear X scale; Y = reasoning ↔ embodiment in five
bands; symbolic ↔ learned rendered as terrain biome; open ↔ closed as an
eastern overlay.

### Phase 2 — Altitude / zoom design  (this session: proposal delivered)

Deliverables:
- `ALTITUDES.md`: entity types per altitude, counts, examples, non-positional
  layers, data model sketch.
- Decision from Alan on 3 vs 4 shipped altitudes and label style.

Status: proposal complete.

### Phase 3 — Content compendium  (this session: first pass delivered; ongoing)

Deliverables:
- `research/0N-*.md`, one per era, each with timeline, people, papers,
  sub-clusters with borders, map notes, numbered verified sources. **Done:
  nine files, 1,500+ lines, ~600 URLs link-checked.**
- `research/09-cross-cutting-threads.md` for rivers/roads. **Done.**
- `SOURCING.md` for the frontier. **Done.**
- Next: convert prose into structured entities (`data/*.yaml` per
  `ALTITUDES.md` §7) with band/biome/parent assigned; ~60 A2 countries,
  ~400 A3 cities to start. This is the bulk of remaining curation.
- Next: first `research/frontier/2026-09.md` produced by running the
  `SOURCING.md` cadence once, to test it.
- Next: second-opinion review of each era file by a different model or a
  human, focused on omissions (what's missing matters more than what's wrong;
  what's there is sourced).
- Next: regional write-ups, the mapofmetal-style paragraph a visitor reads when
  they click a country. The research files have the material; the prose needs
  a consistent voice.

### Phase 4 — Visual design and build  (not started)

Deliverables:
- Style tiles: biome palette, typography, label hierarchy, icon set, water
  and terrain textures. Two or three visual directions before committing.
- Layout: authored positions for A1/A2 polygons; A3 points placed within their
  A2 parent by curator, with a force-directed *local* relaxation only to
  resolve overlaps (algorithm may nudge, never decide neighbourhood).
- Renderer. Candidate stack, to be decided in Phase 4 with a spike:
  - Data: YAML/JSON entities → build step → vector tiles (tippecanoe) or a
    single GeoJSON per altitude.
  - Map engine: MapLibre GL JS (open-source, vector tiles, custom styles,
    smooth zoom, label collision handled) or Leaflet with an image pyramid
    (simpler, how mapofmetal-era sites work, less flexible). MapLibre is the
    default assumption.
  - Terrain: pre-rendered raster layer (generated from biome polygons with
    noise/hillshade, e.g. in a Python/Blender/Inkscape pipeline) beneath vector
    labels and markers. This is where the "lovingly crafted" look comes from.
  - Site: static, GitHub Pages; cards and region write-ups from markdown.
- Monthly update pipeline: `SOURCING.md` cadence → new entities → rebuild →
  deploy.

### Phase 5 — Publish and maintain  (not started)

- Public URL, about page crediting sources and mapofmetal.com as inspiration.
- Monthly frontier commits.
- Annual re-curation using Tier-3 retrospectives (`SOURCING.md` §1).

## 4. Milestones

| # | Milestone | Depends on |
|---|---|---|
| M1 | Alan decides Y axis, X origin, altitude count | this session's docs |
| M2 | `data/` schema fixed; A1 + A2 entities authored for all eras | M1 |
| M3 | A3 entities authored for all eras (~400) with positions | M2 |
| M4 | Visual direction chosen from 2–3 style tiles | M1 |
| M5 | Renderer spike: one continent, three altitudes, real data | M2, M4 |
| M6 | Full map v0 (A1–A3), private URL | M3, M5 |
| M7 | First monthly frontier update run end-to-end | M6, SOURCING.md |
| M8 | Public launch | M6, M7, write-ups |

## 5. Open decisions (need Alan)

1. Y axis: Candidate E (recommended) or Candidate A. See `AXES.md` §3–4.
2. X origin: 1943 mainland + pre-1943 archipelago (recommended), or 1936, or 1950.
3. Ship A1–A3 first, A4 only for 2017+ (recommended) or all four everywhere.
4. Evocative region names with neutral subtitles (recommended) or neutral only.
5. Map engine: MapLibre GL (recommended) vs Leaflet image pyramid. Decide
   after the Phase 4 spike, not before.
6. Who reviews the frontier intake monthly: Alan, a second model, or both.
7. Scope of "AI": include adjacent fields (operations research, control
   theory, computational neuroscience, HCI) as coastal territories or leave
   them as off-map sea? Current research files include them only where AI
   people cite them.

## 6. Risks

- **Axis regret.** Changing Y after A3 positions are authored means
  re-placing hundreds of entities. Mitigation: decide Y on the two-axis
  argument in `AXES.md`, then validate with a paper sketch of 1965, 1990,
  2015 and 2025 vertical slices before authoring positions.
- **Recency bloat.** The east edge will attract ten times the entities per
  year of the west. Mitigation: non-linear X scale, A4-first intake, aging
  and pruning rules in `SOURCING.md`.
- **Factual drift.** Mitigation: every entity carries sources; `scripts/check_links.sh`
  in CI; `status` field on every entity.
- **Aesthetic mediocrity.** A default MapLibre style looks like a road map,
  not like mapofmetal. Mitigation: style tiles before renderer; budget real
  design time; consider a designer for the terrain layer.
