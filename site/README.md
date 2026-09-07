# site/ — review prototype (P2-T1-RENDER)

Single static page rendering `data/continents/REGISTRY.md` as an atlas-style map
(X = time, piecewise-scaled per AXES.md §1; Y = the five AXES.md §3 bands as faint
latitudes; colour = biome). Deployed to GitHub Pages by `.github/workflows/pages.yml`.

- `index.html` — all HTML/CSS/JS inline; no build step. Fonts: Cinzel (names) + Lora
  (body) via Google Fonts, with Georgia fallback.
- `build_registry_json.py` — parses REGISTRY.md (via `scripts/check_registry.py`'s
  parser) into `registry.json`; run it after editing the registry. The Pages workflow
  runs it on every deploy, so the committed `registry.json` is only for local preview.
- `check_layout.py` — headless-Chromium (Playwright) review gate: asserts zero pixel-level
  overlap between distinct landmass fills (with a sea gap), zero label-bbox overlaps, and
  every mainland label inside its own landmass; writes a screenshot. Run:
  `python3 site/check_layout.py` (needs `pip install playwright` + a Chromium).
- Local preview: `python3 -m http.server -d site 8765` → http://localhost:8765/

## Placement model (render-only; not registry data)

Each mainland continent has a `CELL` (a polygon in (year, band-fraction) space that no other
cell touches) and a `COAST` (a smooth Catmull-Rom/Bézier coastline through a handful of
control points, clipped to the cell). Disjoint cells ⇒ landmasses can never overlap, however
the coastlines are drawn. The 1974–2011 cluster (REGISTRY.md D2/D4 overlaps) is resolved as:

- winter-steppes — N1 + upper N2;
- expert-systems-plateau — lower N2 + a sliver of C, nested directly under the steppe
  (the "warm valley", D2);
- connectionist-revival — S1–S2 with a cape reaching into C before 1988;
- statistical-isthmus — a thin neck in band C between plateau and revival from 1988 (Pearl),
  widening to N2–S1 once the steppe/plateau (1993) and revival (1998) end;
- deep-learning-basin — S1–S2 until the isthmus ends (2011), then the full C–S2 span.

Registry `band span` values are unchanged; these are the pixel realisations of them.
