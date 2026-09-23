# Density sampler — v2 (MapLibre) — 2026-09-23 03:02 UTC

Renderer `site/v2/index.html`, 412×892 CSS px @ DPR 2, 100 fixture frames (88 land frames with sea_ratio ≤ 0.6), 233.6 s.

Hard gates (clipped_major_anchored==0, overlaps==0, font caps, no HTML markers): **75/100 frames pass**.
External (non-localhost) requests: 0. Console errors: 0.

| level | MapLibre z | frames | land | pass | soft-fail | HARD-fail | pass rate (land) | p50 labels / landmarks / facts / clipped / clipped_major / major_anchored | p50 sea | top failure reasons |
|---|---|---|---|---|---|---|---|---|---|---|
| z0 | 3.0 | 25 | 25 | 0 | 25 | 0 | 0% | 3 / 1 / 0 / 1 / 1 / 0 | 0.95 | labels×25, continents×25 |
| z1 | 4.5 | 25 | 25 | 9 | 12 | 4 | 36% | 15 / 3 / 7 / 6 / 2 / 0 | 0.82 | landmarks×15, countries×15, clipped_major_anchored×4 |
| z2 | 6.0 | 25 | 20 | 8 | 4 | 10 | 40% | 23 / 13 / 2 / 10 / 4 / 0 | 0.45 | clipped_major_anchored×10, facts×8 |
| z3 | 7.5 | 25 | 18 | 0 | 7 | 11 | 0% | 12 / 7 / 3 / 5 / 3 / 0 | 0.29 | landmarks×18, labels×17, facts×15, clipped_major_anchored×11 |

## Worst 10 frames

| frame | level | labels | landmarks | facts | clip/major/anchored | ovl | sea | reasons | link |
|---|---|---|---|---|---|---|---|---|---|
| z3-014 | z3 | 10 | 5 | 5 | 7/2/1 | 0 | 0.01 | clipped_major_anchored=1; labels=10 < 24; landmarks=5 < 18; facts=5 < 6; countries=0 < 1 | [`?z=7.5&x=929.4&y=573.7`](v2/index.html?z=7.5&x=929.4&y=573.7) |
| z3-011 | z3 | 15 | 10 | 5 | 9/4/1 | 0 | 0.00 | clipped_major_anchored=1; labels=15 < 24; landmarks=10 < 18; facts=5 < 6; countries=0 < 1 | [`?z=7.5&x=1367.9&y=621.4`](v2/index.html?z=7.5&x=1367.9&y=621.4) |
| z3-013 | z3 | 11 | 5 | 5 | 4/2/1 | 0 | 0.48 | clipped_major_anchored=1; labels=11 < 24; landmarks=5 < 18; facts=5 < 6 | [`?z=7.5&x=1465.6&y=249.9`](v2/index.html?z=7.5&x=1465.6&y=249.9) |
| z3-009 | z3 | 12 | 6 | 5 | 5/2/1 | 0 | 0.00 | clipped_major_anchored=1; labels=12 < 24; landmarks=6 < 18; facts=5 < 6 | [`?z=7.5&x=695.4&y=627.7`](v2/index.html?z=7.5&x=695.4&y=627.7) |
| z3-003 | z3 | 16 | 9 | 5 | 7/4/1 | 0 | 0.29 | clipped_major_anchored=1; labels=16 < 24; landmarks=9 < 18; facts=5 < 6 | [`?z=7.5&x=1123.4&y=703.6`](v2/index.html?z=7.5&x=1123.4&y=703.6) |
| z3-000 | z3 | 20 | 11 | 3 | 11/5/1 | 0 | 0.26 | clipped_major_anchored=1; labels=20 < 24; landmarks=11 < 18; facts=3 < 6 | [`?z=7.5&x=534.5&y=478.4`](v2/index.html?z=7.5&x=534.5&y=478.4) |
| z3-010 | z3 | 20 | 13 | 3 | 6/2/1 | 0 | 0.15 | clipped_major_anchored=1; labels=20 < 24; landmarks=13 < 18; facts=3 < 6 | [`?z=7.5&x=568.6&y=457.4`](v2/index.html?z=7.5&x=568.6&y=457.4) |
| z3-021 | z3 | 15 | 7 | 6 | 8/5/1 | 0 | 0.00 | clipped_major_anchored=1; labels=15 < 24; landmarks=7 < 18 | [`?z=7.5&x=681.2&y=546.2`](v2/index.html?z=7.5&x=681.2&y=546.2) |
| z1-001 | z1 | 16 | 3 | 9 | 8/5/3 | 0 | 0.83 | clipped_major_anchored=3; landmarks=3 < 4; countries=2 < 3 | [`?z=4.5&x=530.0&y=694.9`](v2/index.html?z=4.5&x=530.0&y=694.9) |
| z1-021 | z1 | 16 | 3 | 9 | 8/5/3 | 0 | 0.83 | clipped_major_anchored=3; landmarks=3 < 4; countries=2 < 3 | [`?z=4.5&x=532.6&y=650.6`](v2/index.html?z=4.5&x=532.6&y=650.6) |

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
