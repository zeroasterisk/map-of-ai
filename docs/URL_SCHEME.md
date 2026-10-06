# Deep-link URL scheme — the live Leaflet map (`site/index.html`)

Every view of the map has a URL. Pan or zoom and the address bar updates in place; the **copy link** button
(bottom-right of the map) puts that URL on the clipboard. Paste it to point someone (or the agent) at exactly
what you are looking at.

Base: `https://zeroasterisk.github.io/map-of-ai/`

## 1. Precise form (canonical — this is what the map writes)

```
?z=<zoom>&x=<plate_x>&y=<plate_y>
```

* `x`, `y` — the view center in **plate units**: the atlas.html coordinate system, 1800 × 700, origin top-left,
  y grows downward. 1 plate unit = 1 px at zoom 0 (the same numbers `static-map.html?px=&py=` uses).
* `z` — Leaflet zoom, `-1 … 3` in steps of 0.25 (`2^z` px per plate unit; tiles come from level `round(z)`).
* Written on every settled pan/zoom via `history.replaceState` (150 ms debounce, no history entries), rounded to
  0.1 plate unit / 0.1 zoom.

Example — the north-west corner of the Deep Learning Basin at country-name detail:
`https://zeroasterisk.github.io/map-of-ai/?z=2&x=1000&y=400`

## 2. Named anchor (convenience)

```
?place=<continent-id | country-id>[&z=<zoom>]
```

* Ids are the registry ids (`data/continents/*.yaml`, `site/entities.json`). The target point is the entity's
  **label anchor**: the fill centroid of its polygon, the same rule atlas.html uses to place labels, baked once
  into `site/anchors.json` by `site/build_anchors.py` (re-run after any geometry change — it also lists ids that
  exist in entities.json but are not drawn, e.g. `tooling-guild`, `pretraining-foothills`, which have no anchor).
* Default zoom: **continent 0.5** (whole continent with its neighbours, level-0/1 tiles), **country 2.5**
  (level-2/3 tiles, where country names are in the raster).
* Unknown id → `console.warn`, default whole-plate view; nothing breaks.
* As soon as the map settles, the URL is rewritten to the precise form, so what you *share back* is always
  coordinates — the named form is an entry point, not a state.

Examples:

* continent — `https://zeroasterisk.github.io/map-of-ai/?place=deep-learning-basin`
  (→ `?z=0.5&x=989.3&y=483.5`)
* country — `https://zeroasterisk.github.io/map-of-ai/?place=deep-rl-delta`
  (→ `?z=2.5&x=1084.2&y=472.2`)
* country, zoomed out to see its parent — `?place=deep-rl-delta&z=1`

Available ids: continents `antecedent-isles cybernetic-shore symbolic-heartland winter-steppes
expert-systems-plateau connectionist-revival statistical-isthmus deep-learning-basin transformer-plateau
generative-coast`; countries `chinese-state-response deep-generative-shoreline deep-rl-delta gpu-convnet-school
industrial-lab-founders neural-nlp-sequence-school speech-recognition-converts`.

## 3. Precedence

1. `place` (if found) sets center **and** zoom.
2. Any explicit `z`, `x`, `y` then overrides that one field. So `?place=deep-rl-delta&z=1` keeps the country's
   center at zoom 1; `?place=deep-rl-delta&x=1000` moves only the x center.
3. Nothing given, or only an unknown `place` → default `fitBounds` view of the whole plate.

## 4. Related

* `static-map.html?level=2&px=1000&py=450&r=1` — raw tile audit for the same plate point (no map UI, separate tool).
* Gate: `site/check_url.py` (Playwright) — asserts load-by-place, load-by-coords, URL follows pan/zoom,
  clipboard == `location.href`.

## 5. Live evidence (check_url.py run against the deployed site)

`docs/screens/url-live/` — `a_place_continent.png` (`?place=deep-learning-basin` → z 0.5, 989.3/483.5),
`a_place_country.png` (`?place=deep-rl-delta` → z 2.5, 1084.2/472.2, "The AlphaGo Delta" centered),
`b_precise.png` (`?z=2&x=1000&y=400`), `c_after_pan_zoom.png` (URL rewritten to `?z=3&x=1075&y=430`),
`d_copied.png` (clipboard == `location.href`).
