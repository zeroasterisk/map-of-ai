# Density sampler — v2 (MapLibre) — 2026-09-23 00:44 UTC

Renderer `site/v2/index.html`, 412×892 CSS px @ DPR 2, 100 fixture frames (88 land frames with sea_ratio ≤ 0.6), 256.5 s.

Hard gates (clipped==0, overlaps==0, font caps, no HTML markers): **7/100 frames pass**.
External (non-localhost) requests: 0. Console errors: 0.

| level | MapLibre z | frames | land | pass | soft-fail | HARD-fail | pass rate (land) | p50 labels / landmarks / facts / clipped | top failure reasons |
|---|---|---|---|---|---|---|---|---|---|
| z0 | 3.0 | 25 | 25 | 0 | 0 | 25 | 0% | 7 / 1 / 0 / 3 | clipped×25, labels×25, continents×25 |
| z1 | 4.5 | 25 | 25 | 0 | 0 | 25 | 0% | 11 / 0 / 3 / 5 | clipped×25, landmarks×25, countries×17, labels×6 |
| z2 | 6.0 | 25 | 20 | 0 | 0 | 25 | 0% | 21 / 9 / 5 / 9 | clipped×25, landmarks×14, labels×2 |
| z3 | 7.5 | 25 | 18 | 0 | 2 | 18 | 0% | 6 / 2 / 3 / 3 | labels×18, landmarks×18, clipped×18, facts×14 |

## Worst 10 frames

| frame | level | labels | landmarks | facts | clip | ovl | sea | reasons | link |
|---|---|---|---|---|---|---|---|---|---|
| z3-022 | z3 | 1 | 1 | 0 | 1 | 0 | 0.45 | clipped=1; labels=1 < 24; landmarks=1 < 18; facts=0 < 6; countries=0 < 1 | [`?z=7.5&x=571.9&y=702.0`](v2/index.html?z=7.5&x=571.9&y=702.0) |
| z3-010 | z3 | 2 | 1 | 1 | 1 | 0 | 0.16 | clipped=1; labels=2 < 24; landmarks=1 < 18; facts=1 < 6; countries=0 < 1 | [`?z=7.5&x=568.6&y=457.4`](v2/index.html?z=7.5&x=568.6&y=457.4) |
| z3-017 | z3 | 4 | 1 | 3 | 4 | 0 | 0.19 | clipped=4; labels=4 < 24; landmarks=1 < 18; facts=3 < 6; countries=0 < 1 | [`?z=7.5&x=876.8&y=515.9`](v2/index.html?z=7.5&x=876.8&y=515.9) |
| z3-018 | z3 | 4 | 2 | 2 | 2 | 0 | 0.22 | clipped=2; labels=4 < 24; landmarks=2 < 18; facts=2 < 6; countries=0 < 1 | [`?z=7.5&x=250.0&y=507.6`](v2/index.html?z=7.5&x=250.0&y=507.6) |
| z3-009 | z3 | 8 | 5 | 3 | 4 | 0 | 0.02 | clipped=4; labels=8 < 24; landmarks=5 < 18; facts=3 < 6; countries=0 < 1 | [`?z=7.5&x=695.4&y=627.7`](v2/index.html?z=7.5&x=695.4&y=627.7) |
| z3-014 | z3 | 8 | 4 | 4 | 5 | 0 | 0.02 | clipped=5; labels=8 < 24; landmarks=4 < 18; facts=4 < 6; countries=0 < 1 | [`?z=7.5&x=929.4&y=573.7`](v2/index.html?z=7.5&x=929.4&y=573.7) |
| z3-011 | z3 | 13 | 9 | 4 | 6 | 0 | 0.00 | clipped=6; labels=13 < 24; landmarks=9 < 18; facts=4 < 6; countries=0 < 1 | [`?z=7.5&x=1367.9&y=621.4`](v2/index.html?z=7.5&x=1367.9&y=621.4) |
| z3-008 | z3 | 6 | 2 | 3 | 5 | 0 | 0.15 | clipped=5; labels=6 < 24; landmarks=2 < 18; facts=3 < 6 | [`?z=7.5&x=1567.6&y=282.6`](v2/index.html?z=7.5&x=1567.6&y=282.6) |
| z1-009 | z1 | 7 | 0 | 1 | 4 | 0 | 0.89 | clipped=4; labels=7 < 8; landmarks=0 < 4; countries=1 < 3 | [`?z=4.5&x=275.1&y=632.7`](v2/index.html?z=4.5&x=275.1&y=632.7) |
| z1-011 | z1 | 7 | 0 | 1 | 4 | 0 | 0.93 | clipped=4; labels=7 < 8; landmarks=0 < 4; countries=1 < 3 | [`?z=4.5&x=220.7&y=662.4`](v2/index.html?z=4.5&x=220.7&y=662.4) |

## Measurement notes

- `labels`/`landmarks`/`facts` = symbols MapLibre actually placed (`queryRenderedFeatures` over the symbol layers, deduped by layer+feature id).
- `overlaps`/`clipped` use MapLibre's own committed collision boxes (exact placed extents, text-padding removed).
- `clipped` counts every placed label whose box crosses the viewport edge by > 2 CSS px. MapLibre places symbols inside a fixed 100 px band
  outside the viewport and has no option to suppress edge-straddling labels, so on a continuous-pan map this count is structurally > 0 whenever
  labels exist near the frame edge (`clipped_major` in the JSON = those with < 50 % of the box visible). The §2.3 premise that MapLibre hides
  edge labels does not hold; the gate is reported as specified, and the definition is flagged for the planner in ORCHESTRATOR_LOG.md.
- z0/z1 frames on a portrait phone can never reach sea_ratio ≤ 0.6 (the land band is ≈560 units tall vs a 1385–3920-unit frame), so their
  density floors are applied to every frame; z2/z3 floors apply to land frames only.
