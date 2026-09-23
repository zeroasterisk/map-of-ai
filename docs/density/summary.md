# Density sampler — v2 (MapLibre) — 2026-09-23 03:27 UTC

Renderer `site/v2/index.html`, 412×892 CSS px @ DPR 2, 100 fixture frames (90 land frames with sea_ratio ≤ 0.6), 245.1 s.

Hard gates (clipped_major_anchored==0, overlaps==0, font caps, no HTML markers): **73/100 frames pass**.
External (non-localhost) requests: 0. Console errors: 0.

| level | MapLibre z | frames | land | pass | soft-fail | HARD-fail | pass rate (land) | p50 labels / landmarks / facts / clipped / clipped_major / major_anchored | p50 sea | top failure reasons |
|---|---|---|---|---|---|---|---|---|---|---|
| z0 | 3.0 | 25 | 25 | 0 | 25 | 0 | 0% | 5 / 1 / 0 / 2 / 1 / 0 | 0.92 | labels×25, continents×25 |
| z1 | 4.5 | 25 | 25 | 18 | 1 | 6 | 72% | 22 / 10 / 8 / 8 / 4 / 0 | 0.67 | clipped_major_anchored×6, labels×1 |
| z2 | 6.0 | 25 | 22 | 2 | 6 | 15 | 9% | 24 / 16 / 1 / 9 / 4 / 1 | 0.34 | clipped_major_anchored×15, facts×14, landmarks×2, labels×1 |
| z3 | 7.5 | 25 | 18 | 0 | 14 | 6 | 0% | 8 / 4 / 3 / 4 / 2 / 0 | 0.21 | landmarks×18, labels×17, facts×17, clipped_major_anchored×6 |

## Worst 10 frames

| frame | level | labels | landmarks | facts | clip/major/anchored | ovl | sea | reasons | link |
|---|---|---|---|---|---|---|---|---|---|
| z3-009 | z3 | 8 | 4 | 4 | 4/3/1 | 0 | 0.00 | clipped_major_anchored=1; labels=8 < 24; landmarks=4 < 18; facts=4 < 6; countries=0 < 1 | [`?z=7.5&x=695.4&y=627.7`](v2/index.html?z=7.5&x=695.4&y=627.7) |
| z3-021 | z3 | 8 | 4 | 4 | 3/1/1 | 0 | 0.00 | clipped_major_anchored=1; labels=8 < 24; landmarks=4 < 18; facts=4 < 6; countries=0 < 1 | [`?z=7.5&x=681.2&y=546.2`](v2/index.html?z=7.5&x=681.2&y=546.2) |
| z2-006 | z2 | 12 | 8 | 1 | 5/2/1 | 0 | 0.53 | clipped_major_anchored=1; labels=12 < 14; landmarks=8 < 10; facts=1 < 2 | [`?z=6.0&x=842.7&y=444.7`](v2/index.html?z=6.0&x=842.7&y=444.7) |
| z3-000 | z3 | 19 | 11 | 3 | 9/5/1 | 0 | 0.13 | clipped_major_anchored=1; labels=19 < 24; landmarks=11 < 18; facts=3 < 6 | [`?z=7.5&x=534.5&y=478.4`](v2/index.html?z=7.5&x=534.5&y=478.4) |
| z3-015 | z3 | 15 | 6 | 6 | 11/5/1 | 0 | 0.13 | clipped_major_anchored=1; labels=15 < 24; landmarks=6 < 18 | [`?z=7.5&x=785.5&y=645.7`](v2/index.html?z=7.5&x=785.5&y=645.7) |
| z2-018 | z2 | 17 | 9 | 1 | 6/1/1 | 0 | 0.44 | clipped_major_anchored=1; landmarks=9 < 10; facts=1 < 2 | [`?z=6.0&x=672.3&y=691.6`](v2/index.html?z=6.0&x=672.3&y=691.6) |
| z2-023 | z2 | 18 | 11 | 1 | 7/5/1 | 0 | 0.56 | clipped_major_anchored=1; facts=1 < 2 | [`?z=6.0&x=482.0&y=382.4`](v2/index.html?z=6.0&x=482.0&y=382.4) |
| z2-024 | z2 | 25 | 17 | 1 | 6/3/1 | 0 | 0.30 | clipped_major_anchored=1; facts=1 < 2 | [`?z=6.0&x=600.3&y=482.3`](v2/index.html?z=6.0&x=600.3&y=482.3) |
| z2-012 | z2 | 26 | 20 | 0 | 5/2/1 | 0 | 0.35 | clipped_major_anchored=1; facts=0 < 2 | [`?z=6.0&x=1096.5&y=699.5`](v2/index.html?z=6.0&x=1096.5&y=699.5) |
| z2-015 | z2 | 32 | 25 | 0 | 14/6/3 | 0 | 0.15 | clipped_major_anchored=3; facts=0 < 2 | [`?z=6.0&x=1409.6&y=430.5`](v2/index.html?z=6.0&x=1409.6&y=430.5) |

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
