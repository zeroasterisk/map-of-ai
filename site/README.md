# site/ — review prototype (P2-T1-RENDER)

Single static page rendering `data/continents/REGISTRY.md` as a horizontal map strip
(X = time, piecewise-scaled per AXES.md §1; Y = the five AXES.md §3 bands as faint
latitudes; colour = biome). Deployed to GitHub Pages by `.github/workflows/pages.yml`.

- `index.html` — all HTML/CSS/JS inline; no build step.
- `build_registry_json.py` — parses REGISTRY.md (via `scripts/check_registry.py`'s
  parser) into `registry.json`; run it after editing the registry. The Pages workflow
  runs it on every deploy, so the committed `registry.json` is only for local preview.
- Local preview: `python3 -m http.server -d site 8765` → http://localhost:8765/

Render-only layout hints (`INSET` in index.html) nest the Expert Systems Plateau
inside the Winter Steppes band; they are not registry data.
