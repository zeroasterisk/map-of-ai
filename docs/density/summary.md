# Density sampler — v2 (MapLibre) — 2026-09-23 01:36 UTC

Renderer `site/v2/index.html`, 412×892 CSS px @ DPR 2, 100 fixture frames (88 land frames with sea_ratio ≤ 0.6), 238.8 s.

Hard gates (clipped_major==0, overlaps==0, font caps, no HTML markers): **8/100 frames pass**.
External (non-localhost) requests: 0. Console errors: 0.

| level | MapLibre z | frames | land | pass | soft-fail | HARD-fail | pass rate (land) | p50 labels / landmarks / facts / clipped / clipped_major | top failure reasons |
|---|---|---|---|---|---|---|---|---|---|
| z0 | 3.0 | 25 | 25 | 0 | 4 | 21 | 0% | 7 / 1 / 0 / 2 / 1 | labels×24, continents×24, clipped_major×21 |
| z1 | 4.5 | 25 | 25 | 2 | 0 | 23 | 8% | 13 / 7 / 1 / 5 / 2 | clipped_major×23 |
| z2 | 6.0 | 25 | 20 | 0 | 0 | 25 | 0% | 25 / 10 / 5 / 11 / 6 | clipped_major×25, landmarks×5 |
| z3 | 7.5 | 25 | 18 | 0 | 0 | 23 | 0% | 14 / 7 / 5 / 6 / 2 | clipped_major×23, landmarks×18, labels×16, facts×10 |

## Worst 10 frames

| frame | level | labels | landmarks | facts | clip/major | ovl | sea | reasons | link |
|---|---|---|---|---|---|---|---|---|---|
| z3-022 | z3 | 1 | 1 | 0 | 1/1 | 0 | 0.45 | clipped_major=1; labels=1 < 24; landmarks=1 < 18; facts=0 < 6; countries=0 < 1 | [`?z=7.5&x=571.9&y=702.0`](v2/index.html?z=7.5&x=571.9&y=702.0) |
| z3-014 | z3 | 10 | 5 | 5 | 7/1 | 0 | 0.02 | clipped_major=1; labels=10 < 24; landmarks=5 < 18; facts=5 < 6; countries=0 < 1 | [`?z=7.5&x=929.4&y=573.7`](v2/index.html?z=7.5&x=929.4&y=573.7) |
| z3-011 | z3 | 13 | 9 | 4 | 6/2 | 0 | 0.00 | clipped_major=2; labels=13 < 24; landmarks=9 < 18; facts=4 < 6; countries=0 < 1 | [`?z=7.5&x=1367.9&y=621.4`](v2/index.html?z=7.5&x=1367.9&y=621.4) |
| z3-008 | z3 | 6 | 2 | 3 | 5/4 | 0 | 0.15 | clipped_major=4; labels=6 < 24; landmarks=2 < 18; facts=3 < 6 | [`?z=7.5&x=1567.6&y=282.6`](v2/index.html?z=7.5&x=1567.6&y=282.6) |
| z3-017 | z3 | 8 | 2 | 5 | 6/6 | 0 | 0.19 | clipped_major=6; labels=8 < 24; landmarks=2 < 18; facts=5 < 6 | [`?z=7.5&x=876.8&y=515.9`](v2/index.html?z=7.5&x=876.8&y=515.9) |
| z3-013 | z3 | 11 | 5 | 5 | 4/2 | 0 | 0.48 | clipped_major=2; labels=11 < 24; landmarks=5 < 18; facts=5 < 6 | [`?z=7.5&x=1465.6&y=249.9`](v2/index.html?z=7.5&x=1465.6&y=249.9) |
| z3-003 | z3 | 14 | 7 | 5 | 8/2 | 0 | 0.29 | clipped_major=2; labels=14 < 24; landmarks=7 < 18; facts=5 < 6 | [`?z=7.5&x=1123.4&y=703.6`](v2/index.html?z=7.5&x=1123.4&y=703.6) |
| z3-012 | z3 | 17 | 9 | 5 | 9/2 | 0 | 0.37 | clipped_major=2; labels=17 < 24; landmarks=9 < 18; facts=5 < 6 | [`?z=7.5&x=606.8&y=420.8`](v2/index.html?z=7.5&x=606.8&y=420.8) |
| z3-020 | z3 | 19 | 11 | 5 | 6/4 | 0 | 0.30 | clipped_major=4; labels=19 < 24; landmarks=11 < 18; facts=5 < 6 | [`?z=7.5&x=408.4&y=577.9`](v2/index.html?z=7.5&x=408.4&y=577.9) |
| z0-004 | z0 | 6 | 1 | 0 | 2/1 | 0 | 0.97 | clipped_major=1; labels=6 < 9; continents=5 < 8 | [`?z=3.0&x=221.3&y=458.0`](v2/index.html?z=3.0&x=221.3&y=458.0) |

## Measurement notes

- `labels`/`landmarks`/`facts` = symbols MapLibre actually placed (`queryRenderedFeatures` over the symbol layers, deduped by layer+feature id).
- `overlaps`/`clipped` use MapLibre's own committed collision boxes (exact placed extents, text-padding removed).
- `clipped` counts every placed label whose box crosses the viewport edge by > 2 CSS px. MapLibre places symbols inside a fixed 100 px band
  outside the viewport and has no option to suppress edge-straddling labels, so on a continuous-pan map this count is structurally > 0 whenever
  labels exist near the frame edge. Planner decision (Phase 4b): the HARD gate is `clipped_major == 0` (a placed label with < 50 % of its
  box visible — the half-cut banner); raw `clipped` is reported, not gated.
- z0/z1 frames on a portrait phone can never reach sea_ratio ≤ 0.6 (the land band is ≈560 units tall vs a 1385–3920-unit frame), so their
  density floors are applied to every frame; z2/z3 floors apply to land frames only.
- z1 `landmarks` = landmark-class symbols (lod 1–2 events, lod ≤ 1 summits) + country names (Phase 4b task D); `landmarks_symbols` in the JSON
  is the symbol-only count.
