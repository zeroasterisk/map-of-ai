# Density sampler — v2 (MapLibre) — 2026-09-23 03:45 UTC

Renderer `site/v2/index.html`, 412×892 CSS px @ DPR 2, 100 fixture frames (90 land frames with sea_ratio ≤ 0.6), 264.8 s.

Hard gates (clipped_any_anchored==0, clipped_major_anchored==0, overlaps==0, font caps, no HTML markers): **15/100 frames pass**.
External (non-localhost) requests: 0. Console errors: 0.

| level | MapLibre z | frames | land | pass | soft-fail | HARD-fail | pass rate (land) | p50 labels / landmarks / facts / clipped / clipped_major / major_anchored / any_anchored | p50 sea | p50 blank | top failure reasons |
|---|---|---|---|---|---|---|---|---|---|---|---|
| z0 | 3.0 | 25 | 25 | 0 | 7 | 18 | 0% | 5 / 1 / 0 / 2 / 1 / 0 / 1 | 0.92 | 0.82 | labels×25, continents×25, clipped_any_anchored×18 |
| z1 | 4.5 | 25 | 25 | 0 | 0 | 25 | 0% | 21 / 10 / 7 / 8 / 4 / 0 / 3 | 0.67 | 0.54 | clipped_any_anchored×25, blank_ratio×22, clipped_major_anchored×6, labels×1 |
| z2 | 6.0 | 25 | 22 | 0 | 0 | 25 | 0% | 27 / 20 / 1 / 11 / 5 / 1 / 5 | 0.34 | 0.40 | clipped_any_anchored×25, clipped_major_anchored×17, facts×13, blank_ratio×7 |
| z3 | 7.5 | 25 | 18 | 0 | 8 | 17 | 0% | 10 / 4 / 3 / 4 / 2 / 0 / 2 | 0.21 | 0.67 | blank_ratio×21, clipped_any_anchored×17, landmarks×17, facts×17 |

## Worst 10 frames

| frame | level | labels | landmarks | facts | clip/major/anchored/any | ovl | sea | blank | reasons | link |
|---|---|---|---|---|---|---|---|---|---|---|
| z3-009 | z3 | 11 | 6 | 5 | 6/2/1/4 | 0 | 0.00 | 0.67 | clipped_major_anchored=1; clipped_any_anchored=4; blank_ratio=0.67 > 0.5; labels=11 < 24;  | [`?z=7.5&x=695.4&y=627.7`](v2/index.html?z=7.5&x=695.4&y=627.7) |
| z3-021 | z3 | 11 | 6 | 5 | 4/1/1/4 | 0 | 0.00 | 0.59 | clipped_major_anchored=1; clipped_any_anchored=4; blank_ratio=0.59 > 0.5; labels=11 < 24;  | [`?z=7.5&x=681.2&y=546.2`](v2/index.html?z=7.5&x=681.2&y=546.2) |
| z3-010 | z3 | 16 | 10 | 3 | 6/3/1/3 | 0 | 0.00 | 0.51 | clipped_major_anchored=1; clipped_any_anchored=3; blank_ratio=0.51 > 0.5; labels=16 < 24;  | [`?z=7.5&x=568.6&y=457.4`](v2/index.html?z=7.5&x=568.6&y=457.4) |
| z2-006 | z2 | 14 | 10 | 1 | 5/2/1/4 | 0 | 0.53 | 0.62 | clipped_major_anchored=1; clipped_any_anchored=4; blank_ratio=0.62 > 0.5; facts=1 < 2 | [`?z=6.0&x=842.7&y=444.7`](v2/index.html?z=6.0&x=842.7&y=444.7) |
| z2-023 | z2 | 23 | 16 | 1 | 11/8/4/7 | 0 | 0.56 | 0.56 | clipped_major_anchored=4; clipped_any_anchored=7; blank_ratio=0.56 > 0.5; facts=1 < 2 | [`?z=6.0&x=482.0&y=382.4`](v2/index.html?z=6.0&x=482.0&y=382.4) |
| z1-017 | z1 | 21 | 8 | 9 | 9/4/1/5 | 0 | 0.82 | 0.62 | clipped_major_anchored=1; clipped_any_anchored=5; blank_ratio=0.62 > 0.5 | [`?z=4.5&x=301.8&y=565.0`](v2/index.html?z=4.5&x=301.8&y=565.0) |
| z1-006 | z1 | 22 | 8 | 9 | 11/2/1/9 | 0 | 0.79 | 0.61 | clipped_major_anchored=1; clipped_any_anchored=9; blank_ratio=0.61 > 0.5 | [`?z=4.5&x=333.1&y=558.9`](v2/index.html?z=4.5&x=333.1&y=558.9) |
| z2-018 | z2 | 22 | 14 | 1 | 8/3/2/7 | 0 | 0.44 | 0.49 | clipped_major_anchored=2; clipped_any_anchored=7; facts=1 < 2 | [`?z=6.0&x=672.3&y=691.6`](v2/index.html?z=6.0&x=672.3&y=691.6) |
| z1-010 | z1 | 23 | 14 | 6 | 13/8/1/5 | 0 | 0.63 | 0.54 | clipped_major_anchored=1; clipped_any_anchored=5; blank_ratio=0.54 > 0.5 | [`?z=4.5&x=951.5&y=549.0`](v2/index.html?z=4.5&x=951.5&y=549.0) |
| z2-004 | z2 | 23 | 15 | 1 | 14/9/1/5 | 0 | 0.34 | 0.50 | clipped_major_anchored=1; clipped_any_anchored=5; facts=1 < 2 | [`?z=6.0&x=917.8&y=716.6`](v2/index.html?z=6.0&x=917.8&y=716.6) |

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
- Phase 4d task A: `clipped_any_anchored` (HARD, == 0) = a placed label whose anchor is on-screen and ANY part of whose box is off-screen by
  > 2 CSS px; sea labels (symbol-ocean) are exempt because they may be hidden entirely instead. `blank_ratio` (soft, ≤ 0.5 at z1–z3) = share of
  a 16×16 grid over the canvas screenshot whose luminance std-dev < 6 grey levels (no text, icon, terrain, sea texture or border ink).
- z1 `landmarks` = landmark-class symbols (lod 1–2 events, lod ≤ 1 summits) + country names (Phase 4b task D); `landmarks_symbols` in the JSON
  is the symbol-only count.
