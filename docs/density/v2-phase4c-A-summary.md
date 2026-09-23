# Density sampler — v2 (MapLibre) — 2026-09-23 02:48 UTC

Renderer `site/v2/index.html`, 412×892 CSS px @ DPR 2, 100 fixture frames (88 land frames with sea_ratio ≤ 0.6), 242.0 s.

Hard gates (clipped_major_anchored==0, overlaps==0, font caps, no HTML markers): **58/100 frames pass**.
External (non-localhost) requests: 0. Console errors: 0.

| level | MapLibre z | frames | land | pass | soft-fail | HARD-fail | pass rate (land) | p50 labels / landmarks / facts / clipped / clipped_major / major_anchored | p50 sea | top failure reasons |
|---|---|---|---|---|---|---|---|---|---|---|
| z0 | 3.0 | 25 | 25 | 3 | 18 | 4 | 12% | 8 / 1 / 0 / 2 / 1 / 0 | 0.95 | labels×21, continents×21, clipped_major_anchored×4 |
| z1 | 4.5 | 25 | 25 | 16 | 0 | 9 | 64% | 13 / 7 / 1 / 5 / 2 / 0 | 0.82 | clipped_major_anchored×9 |
| z2 | 6.0 | 25 | 20 | 4 | 2 | 19 | 20% | 25 / 10 / 5 / 11 / 6 / 1 | 0.46 | clipped_major_anchored×19, landmarks×5 |
| z3 | 7.5 | 25 | 18 | 0 | 9 | 10 | 0% | 14 / 7 / 5 / 6 / 2 / 0 | 0.29 | landmarks×17, labels×16, clipped_major_anchored×10, facts×9 |

## Worst 10 frames

| frame | level | labels | landmarks | facts | clip/major/anchored | ovl | sea | reasons | link |
|---|---|---|---|---|---|---|---|---|---|
| z3-013 | z3 | 11 | 5 | 5 | 4/2/1 | 0 | 0.48 | clipped_major_anchored=1; labels=11 < 24; landmarks=5 < 18; facts=5 < 6 | [`?z=7.5&x=1465.6&y=249.9`](v2/index.html?z=7.5&x=1465.6&y=249.9) |
| z3-020 | z3 | 19 | 11 | 5 | 6/4/1 | 0 | 0.30 | clipped_major_anchored=1; labels=19 < 24; landmarks=11 < 18; facts=5 < 6 | [`?z=7.5&x=408.4&y=577.9`](v2/index.html?z=7.5&x=408.4&y=577.9) |
| z0-012 | z0 | 7 | 1 | 0 | 2/2/1 | 0 | 0.95 | clipped_major_anchored=1; labels=7 < 9; continents=6 < 8 | [`?z=3.0&x=1329.4&y=487.2`](v2/index.html?z=3.0&x=1329.4&y=487.2) |
| z0-024 | z0 | 7 | 1 | 0 | 2/2/1 | 0 | 0.94 | clipped_major_anchored=1; labels=7 < 9; continents=6 < 8 | [`?z=3.0&x=1353.2&y=514.6`](v2/index.html?z=3.0&x=1353.2&y=514.6) |
| z0-022 | z0 | 8 | 1 | 0 | 3/2/1 | 0 | 0.94 | clipped_major_anchored=1; labels=8 < 9; continents=7 < 8 | [`?z=3.0&x=1190.9&y=535.0`](v2/index.html?z=3.0&x=1190.9&y=535.0) |
| z3-009 | z3 | 13 | 6 | 6 | 6/2/1 | 0 | 0.02 | clipped_major_anchored=1; labels=13 < 24; landmarks=6 < 18 | [`?z=7.5&x=695.4&y=627.7`](v2/index.html?z=7.5&x=695.4&y=627.7) |
| z3-016 | z3 | 16 | 5 | 8 | 8/6/2 | 0 | 0.46 | clipped_major_anchored=2; labels=16 < 24; landmarks=5 < 18 | [`?z=7.5&x=1022.5&y=511.1`](v2/index.html?z=7.5&x=1022.5&y=511.1) |
| z3-019 | z3 | 18 | 7 | 8 | 5/2/1 | 0 | 0.00 | clipped_major_anchored=1; labels=18 < 24; landmarks=7 < 18 | [`?z=7.5&x=612.3&y=601.3`](v2/index.html?z=7.5&x=612.3&y=601.3) |
| z3-005 | z3 | 20 | 11 | 7 | 11/6/1 | 0 | 0.27 | clipped_major_anchored=1; labels=20 < 24; landmarks=11 < 18 | [`?z=7.5&x=429.2&y=517.8`](v2/index.html?z=7.5&x=429.2&y=517.8) |
| z3-015 | z3 | 22 | 9 | 9 | 11/4/1 | 0 | 0.26 | clipped_major_anchored=1; labels=22 < 24; landmarks=9 < 18 | [`?z=7.5&x=785.5&y=645.7`](v2/index.html?z=7.5&x=785.5&y=645.7) |

## Measurement notes

- `labels`/`landmarks`/`facts` = symbols MapLibre actually placed (`queryRenderedFeatures` over the symbol layers, deduped by layer+feature id).
- `overlaps`/`clipped` use MapLibre's own committed collision boxes (exact placed extents, text-padding removed).
- `clipped` counts every placed label whose box crosses the viewport edge by > 2 CSS px. MapLibre places symbols inside a fixed 100 px band
  outside the viewport and has no option to suppress edge-straddling labels, so on a continuous-pan map this count is structurally > 0 whenever
  labels exist near the frame edge. Planner decision (Phase 4c, supersedes 4b): the HARD gate is `clipped_major_anchored == 0` — a placed
  label whose anchor point is inside the viewport but < 50 % of its box is visible (the half-cut banner of an on-screen subject). Raw
  `clipped` and `clipped_major` (which includes labels of off-screen anchors in MapLibre's padding band) are reported, not gated.
- z0/z1 frames on a portrait phone can never reach sea_ratio ≤ 0.6 (the land band is ≈560 units tall vs a 1385–3920-unit frame), so their
  density floors are applied to every frame; z2/z3 floors apply to land frames only.
- z1 `landmarks` = landmark-class symbols (lod 1–2 events, lod ≤ 1 summits) + country names (Phase 4b task D); `landmarks_symbols` in the JSON
  is the symbol-only count.
