# STATUS — as of 2026-09-18 (session 30: LOD tile pyramid rebuilt z0–z4 — Transformer Plateau pilot bbox, anchors, Leaflet banner)

## One-line status

**Session 30 — pushed to `main`: `site/tiles/` rebuilt from scratch on the 1800×1050 plate (first bake since session 14 / `5a47738`), so the Leaflet viewer now carries the Y-funnel v12 plate, the three late-2026 Silicon Range milestones, the 9 Transformer Plateau countries and their 69 LOD events; a third z4 pilot bbox `transformer-plateau (1056, 304, 1472, 720)` (all corners 16-aligned) joins the basin and coast; `site/anchors.json` rebaked (33 anchors: +`transformer-plateau` continent +8 spatial plateau countries) so `?place=` permalinks resolve; `site/index.html` banner now names all three pilot continents and "5 levels of detail", coordinate comment reads 1800×1050 (bounds were already data-driven from `meta.plate`); all gates green except the pre-existing `clipped`.**

- **Tiles (`site/tiles/meta.json`):** z0 40 (2.0 MB) · z1 135 (7.4 MB) · z2 493 (20.4 MB) · z3 1881 (53.1 MB) · z4 2270 (63.9 MB) = **4819 tiles, 146.8 MB** (session 14: 4143 tiles / 119 MB). z4 per region: deep-learning-basin 560 · transformer-plateau 676 (new) · generative-coast 1034. `pilot_bboxes` order in `meta.json` is basin, plateau, coast; `pilot_bbox` (back-compat) stays the basin. `site/labels.json` regenerated alongside. z3/z4 are captured in horizontal strips of whole tile rows (`--strip-px 6000` memory bound, e.g. z3 5888 + 2512 px; plateau z4 5888 + 768 px) that tile independently — no seams found in the Leaflet review below.
- **build_tiles.py:** `PLATE = (1800, 1050)`, `PILOT_BBOXES` gains `transformer-plateau` (covers plateau land + borders + dots + labels: minX 1079 / minY 319.4 / maxX 1444.5 / maxY 705 inside 1056–1472 × 304–720), `LOD_DESC` 1/3/4 name the plateau as a pilot; docstring geometry updated to 1050 px.
- **Anchors (`site/anchors.json`, `plate [1800, 1050]`, 33 entries):** new `transformer-plateau` (continent, centre 1259.1/530, bbox 1092.8–1432.1 × 330.3–691) and the 8 spatial plateau countries `alignment-critique-tributaries`, `decoder-generative-school`, `encoder-understanding-school`, `multimodal-scientific-transformers`, `open-replication-commons`, `scaling-law-empiricists`, `sparse-moe-engineers`, `systems-infrastructure-axis`; `national-champion-scalers` is `spatial: false` and has no anchor by design.
- **Leaflet visual verification (Playwright, served `site/`):** `index.html?place=transformer-plateau&z=2` → 29 tile requests, 0 HTTP ≥ 400, 0 JS errors, all 28 loaded tiles from level 2 (`docs/screens/leaflet-s30-transformer-plateau-z2.png`: 6 plateau country names + tags + years legible, dashed borders continuous, no grey/missing tiles or seams). `…&z=4` → 41 requests, 0 ≥ 400, 0 JS errors, 40 loaded tiles from level 4 (`docs/screens/leaflet-s30-transformer-plateau-z4.png`: BERT Escarpment / Eleutherian Commons z4 detail with RoBERTa, T5 · C4, SuperGLUE, Transformer-XL, RAG, DistilBERT dots + one-line facts). Vision review notes one z4 nit for later: the T5 · C4 dot sits on its own fact line at the plateau centre view (A1 placement class, not a tile defect).
- **Gates:** `build_entities_json.py` OK (3 continents, 26 countries / 23 spatial, 224 LOD events — unchanged); `validate.py --offline` files=29 rules=25 fails=0; `check_research.py --fast` PASS (rc 0); `check_lod_labels.py` LOD LABEL GATE: PASS (0 overlapping text boxes, 0 dots outside countries, 0 text off plate, z0–z4); `check_layout.py` countryCount 0 (23) · countryContainment 0 · countryOverlap 0 · countryLabelOverlaps 0 · countryLabelOutside 0 · zoomInconsistent 0 · labelOverlaps 0 · textClash 0 · leaderProblems 0 · thread gates 0; `clipped` 806 pre-existing (same count as session 29) alone drives RESULT: FAIL.
- **Open follow-ups:** P3-T12 verification review of the plateau set (A-K1…A-K7 evidence, 5-claim spot-checks per country incl. the events layer); Phase 4 city pilot P4-T1 (basin) or P4-T9 Table 2 for the plateau; retire the `clipped` class; the T5 · C4 dot-over-fact nit in the plateau z4 tiles; a z5 level if the city layer needs it (would need a fourth strip band per bbox); the `pending-neighbour:` 09c/09d/09e thread hand-offs.

---
### Session 29 (kept for reference)

# STATUS — as of 2026-09-18 (session 29: P3-LOD The Transformer Plateau LOD event layer — hints, tags, 69 events)

## One-line status

**Session 29 — pushed to `main`: P3-LOD complete. `data/events/transformer-plateau.yaml` authored on the exact basin/coast schema: all 8 spatial plateau countries carry a z1 `hint`, a z2 `tag` and 69 named events (28 `lod: 3` headline + 41 `lod: 4` detail), every row traced to `research/07-transformers-and-llms-2017-2022.md` (every `sources[].url` an exact substring of research/07 [1]–[94], checked by script: 0 misses); `site/entities.json` + `entities.js` regenerated (224 LOD events); one renderer fix in `site/atlas.html` (leader-label offset ladder gained ±12 px steps) so the plateau's taller z2 label blocks place without collision; all gates green except the pre-existing `clipped`.**

- **Events (`data/events/transformer-plateau.yaml`, 69 rows, ids unique, `one_line` ≤ 15 words, `year` inside `[start-0.5, end+1]` for every country — build_entities_json.py enforces these):**
  1. `encoder-understanding-school` The BERT Escarpment — 11 events (3 lod3 + 8 lod4) — hint "BERT · RoBERTa · T5" — tag "ELMo → BERT → RoBERTa → T5" — lod3: BERT, RoBERTa, T5 · C4
  2. `decoder-generative-school` The Autoregressive Ridge — 11 events (5 lod3 + 6 lod4) — hint "GPT-2 · GPT-3 · Codex" — tag "GPT-1 → GPT-2 → GPT-3 → Codex" — lod3: GPT-1, GPT-2, GPT-3, Codex · Copilot, InstructGPT
  3. `scaling-law-empiricists` The Scaling-Law Fault Line — 8 events (4 lod3 + 4 lod4) — hint "Kaplan · Chinchilla · MMLU" — tag "Bitter Lesson → Scaling Laws → Chinchilla → emergence" — lod3: The Bitter Lesson, Scaling Laws, MMLU, Chinchilla
  4. `sparse-moe-engineers` The Mixture-of-Experts Delta — 5 events (2 lod3 + 3 lod4) — hint "Attention Is All You Need · Switch" — tag "Outrageously Large Nets → Transformer → GShard → Switch" — lod3: Attention Is All You Need, Switch Transformer
  5. `systems-infrastructure-axis` The Megatron Yards — 7 events (3 lod3 + 4 lod4) — hint "Megatron-LM · A100 · DeepSpeed" — tag "Megatron-LM + ZeRO/DeepSpeed → A100 → MT-NLG → PaLM" — lod3: Megatron-LM, Nvidia A100, PaLM · Pathways
  6. `multimodal-scientific-transformers` The Attention Promontory — 10 events (4 lod3 + 6 lod4) — hint "ViT · AlphaFold 2 · CLIP" — tag "ViT → AlphaFold 2 → CLIP → Flamingo → Whisper" — lod3: Vision Transformer, AlphaFold 2, DALL-E · CLIP, Gato
  7. `alignment-critique-tributaries` The Human-Feedback Tributaries — 8 events (3 lod3 + 5 lod4) — hint "RLHF · Stochastic Parrots · Anthropic" — tag "Human Preferences → Stochastic Parrots → Anthropic → Galactica" — lod3: RL from Human Preferences, Anthropic founded, Stochastic Parrots
  8. `open-replication-commons` The Eleutherian Commons — 9 events (4 lod3 + 5 lod4) — hint "EleutherAI · The Pile · BLOOM" — tag "The Pile → GPT-NeoX → BLOOM" — lod3: Hugging Face transformers, The Pile, OPT-175B, BLOOM
  Not authored: DeBERTa and Base Layers (the brief listed them but research/07 carries no source for either — nothing here is new research). `national-champion-scalers` is `spatial: false` so it has no lane of its own; its models are drawn as lod4 detail events in the countries whose bullets also cite them — PanGu-α, ERNIE 3.0, YaLM-100B in `open-replication-commons`, Wu Dao 2.0 in `sparse-moe-engineers`. Attention Is All You Need sits in `sparse-moe-engineers` (the only plateau lane open in 2017.45 besides alignment; its bullet cites [1]–[3] via Shazeer).
- **Rendering (probed in-page at `?tilesrc=1&lod=N`, 1800×1050):** lod1 → 3 hints fit (encoder, scaling, sparse; the other 5 lanes are too narrow at lod1 — same behaviour as the basin's curated-out hints), lod2 → 8/8 tags visible, lod3 → 24 labelled headline dots, lod4 → 68/69 events labelled (1 curated out). `docs/screens/lod_labels_summary.json` refreshed by the gate (lod3 events 90, lod4 219 site-wide).
- **Renderer fix (`site/atlas.html` A2 country label fallback):** with a `tag`, the plateau's leader-placed label blocks are one line taller, and every 26/44-px offset in the ladder collided with a neighbour for `decoder-generative-school` vs `open-replication-commons` (its years line landed on "The Eleutherian"). Added `[0, ±12]` steps after `[0, 0]`; generic, and `git stash` confirms the basin/coast label gates are unchanged (countryLabelOverlaps 0 before and after). Two tags were also shortened for the same reason (`decoder` dropped "→ InstructGPT", `commons` dropped "Hugging Face →" and "→ OPT" — both still appear as events).
- **Entity counts:** 3 continents, 26 countries (23 spatial), 224 LOD events (155 → 224), 1 thread / 15 milestones.
- **Gates:** `build_entities_json.py` OK; `validate.py --offline` files=29 rules=25 fails=0; `check_research.py --fast` PASS (rc 0); `check_lod_labels.py` LOD LABEL GATE: PASS (0 overlapping text boxes, 0 dots outside countries, 0 text off plate, z0–z4); `check_layout.py` countryCount 0 (23) · countryContainment 0 · countryOverlap 0 · countryLabelOverlaps 0 · countryLabelOutside 0 · zoomInconsistent 0 · labelOverlaps 0 · textClash 0 · leaderProblems 0 · thread gates 0; `clipped` alone drives RESULT: FAIL — 625 at session start, 806 now, same class (A1 event-label boxes at the viewBox edge; the plateau's new z3/z4 labels sit east of the basin's, so more of them touch the edge in the A1 probe).
- **Open follow-ups:** P3-T12 verification review of the plateau set (A-K1…A-K7 evidence, 5-claim spot-checks per country, now including the events layer); Phase 4 city pilot (P4-T1 on the basin) or P4-T9 Table 2 for the plateau; the `clipped` class (a gate that ignores off-viewBox A1 event labels, or an A1 label suppression near the edge); z0–z5 tile pyramid rebuild so `site/tiles/` picks up the plateau events; the `pending-neighbour:` 09c/09d/09e thread hand-offs.

---
### Session 28 (kept for reference)

# STATUS — as of 2026-09-18 (session 28: P3-T9 The Transformer Plateau country layer — 9 countries + coverage matrix Table 1)

## One-line status

**Session 28 — pushed to `main`: P3-T9 complete. Nine countries authored under `transformer-plateau` in `data/countries/` (8 spatial + `national-champion-scalers` as `spatial: false`, surfaced as a `related_facts` hover note on `open-replication-commons`), mapping 1:1 to the 9 `## Schools of thought` bullets of `research/07-transformers-and-llms-2017-2022.md`; `data/coverage/transformer-plateau.md` Table 1 filled (9 rows = A-M2 awk count 9; 0 merged, 0 dropped); `site/atlas.html` `SUBCOLS` gained 2018/2020 and `kEnd` now snaps a country's end to the next continent column within the 0.8-yr LICENSE slack (no orphan parent slivers at the 2022.8 belt / 2021.3 seam); `site/check_layout.py` N_COUNTRIES 15→23; `site/entities.json` + `entities.js` regenerated; all gates green except the pre-existing `clipped` 625.**

- **Countries (`data/countries/`, parent `transformer-plateau`, all `status: sourced`, summaries 144–160 words, ≥ 4 sources each, every URL an exact substring of research/07, every `research_ref.sources` ⊆ its bullet's [n]s — A-K2 checked by script, 0 fails):**
  1. `encoder-understanding-school` The BERT Escarpment — 2018–2020, C/Cb, forest — [4, 7, 30, 46, 47, 48, 53, 54, 55, 71, 89]
  2. `decoder-generative-school` The Autoregressive Ridge — 2018–2022, C/Ca, jungle — [5, 11, 19, 28]
  3. `scaling-law-empiricists` The Scaling-Law Fault Line — 2019–2022, N2/N2b, grassland — [9, 20, 49, 63, 64, 65, 70]
  4. `sparse-moe-engineers` The Mixture-of-Experts Delta — 2017–2021, S1/S1a, jungle — [27, 34, 74, 93]
  5. `systems-infrastructure-axis` The Megatron Yards — 2019–2022, S2/S2a, harbour — [23, 57, 58, 61]
  6. `multimodal-scientific-transformers` The Attention Promontory — 2020–2022, S1/S1b, jungle — [13, 14, 16, 17, 40, 42, 80, 81, 82]
  7. `alignment-critique-tributaries` The Human-Feedback Tributaries — 2017–2022, N2/N2a, mixed — [19, 37, 38, 44, 68, 69, 85]
  8. `open-replication-commons` The Eleutherian Commons — 2020–2022, C/Cb, grassland — [22, 32, 41, 72, 73, 77]
  9. `national-champion-scalers` The Sovereign Scaling Enclaves — 2021–2022, C, highland, `spatial: false` — [74, 75, 76, 77, 94]
  Cross-continent neighbours resolved per A-K4 where the entity exists (`closed-frontier-labs`, `open-weights-movement`, `alignment-interpretability-plateau`, `diffusion-media-district`, `compute-hardware-hinterland`, `neural-nlp-sequence-school`, `gpu-convnet-school`, `chinese-state-response`); `pending-neighbour:` notes left for the 09c/09d/09e threads and RAG/robotics. A-K7 calls (N2a not N1 for alignment; S1b not S2 for multimodal; harbour territory for systems) recorded in `data/coverage/transformer-plateau.md` for P3-T12.
- **Renderer:** the plateau's grid owns N2b–S2a from 2017, N2a from 2019.6, S1/S2a only until 2021.3 and never N1 — lanes were chosen to fit that (one lane each, N→S: N2a · N2b · Ca · Cb (BERT then commons) · S1a · S1b · S2a). `kEnd` snap is generic (applies to all continents; basin/coast polygons unchanged — generative-coast A2 probe re-run and reverted, check_layout containment/overlap still 0). New screenshot `docs/screens/transformer-plateau-a2.png` (probe_continent_countries.py).
- **Entity counts:** 3 continents, 26 countries (23 spatial), 155 LOD events, 1 thread / 15 milestones.
- **Gates:** `validate.py --offline` files=29 rules=25 fails=0; `validate.py --file` online (V-20 live) 0 fails on each of the 9 new files; `check_research.py --fast` PASS; `check_registry.py` rows=10 fails=0; `check_lod_labels.py` LOD LABEL GATE: PASS; `check_layout.py` countryCount/containment/overlap/labelOverlaps/labelOutside/zoomInconsistent/a2FewTexts all 0 (N_COUNTRIES 23), thread gates 0; `clipped` 625 pre-existing alone drives RESULT: FAIL.
- **Open follow-ups:** P3-T12 review of the plateau set (A-K1…A-K7 evidence, 5-claim spot-checks); Phase 4 city pilot (P4-T1 on the basin) or P4-T9 Table 2 for the plateau; LOD hints/events (`data/events/transformer-plateau.yaml`) so the plateau's provinces carry lod1 hints and lod3/4 events like the basin and coast; the `pending-neighbour:` 09c/09d/09e thread hand-offs.

---
### Session 27 (kept for reference)

# STATUS — as of 2026-09-18 (session 27: P2-T9 The Transformer Plateau Continent YAML + coverage matrix initialization + Silicon Range hardware thread milestones)

## One-line status

**Session 27 — pushed to `main`: P2-T9 (`data/continents/transformer-plateau.yaml`) authored covering 2017–2022, band `[N1, N2, C, S1, S2]`, biome `jungle`, 235-word summary, 8 citations from `research/07-transformers-and-llms-2017-2022.md`, verified online with all gates passing; `data/coverage/transformer-plateau.md` initialized with header block and 9-bullet schools-of-thought check; `data/threads/silicon-river-hardware.yaml` extended with three late-2026 milestones (Ohio Gigawatt Campus, Cerebras CS-4, Nvidia $99B Portfolio & Anthropic IPO Anchor) from `research/09` Thread (d); `site/entities.json` and `site/entities.js` regenerated; all gates green except the pre-existing `clipped` 625.**

- **Continent entity (`data/continents/transformer-plateau.yaml`):** P2-T9 from `PLAN.md` / `REGISTRY.md` row 9. Level: continent; Name: The Transformer Plateau; Subtitle: "Attention, pre-trained language models and scaling laws, 2017–2022"; Band: [N1, N2, C, S1, S2] (home band C spreading to all bands); Biome: jungle; Time range: 2017–2022. Summary (235 words, Rule V-11) traces the era from Vaswani et al. (June 2017) through BERT (2018), GPT-1/2/3 (2018–2020), scaling laws (Kaplan 2020, Chinchilla 2022), multimodal cross-overs (ViT, CLIP, AlphaFold 2), to InstructGPT (March 2022) and open counter-movements preceding ChatGPT (Nov 2022). Research reference points to `research/07-transformers-and-llms-2017-2022.md` sources [1, 2, 7, 9, 11, 14, 19, 20]; all 8 sources verified online (200).
- **Coverage Matrix initialized (`data/coverage/transformer-plateau.md`):** A-M1 header block initialized. Shell check A-M2 confirmed 9 bullets under `## Schools of thought / sub-clusters` in `research/07-transformers-and-llms-2017-2022.md`. Table 1 mapped to country authoring for upcoming P3-T9.
- **Silicon Range Update (`data/threads/silicon-river-hardware.yaml`):** Extended `milestones:` with 3 late-2026 milestones from `research/09` Thread (d):
  - Ohio Gigawatt Campus (year: 2026.63, ref: d28, Nvidia $105B credit/compute for OpenAI's Ohio data centre, SB Energy 8 GW campus)
  - Cerebras CS-4 (year: 2026.64, ref: d15, 750 PFLOPS wafer-scale system, $20B OpenAI compute partnership)
  - Nvidia $99B Portfolio & Anthropic IPO Anchor (year: 2026.70, ref: d64/d65, Nvidia $99B equity book and anchor in Anthropic's record Nasdaq IPO)
  `site/entities.json` and `site/entities.js` rebuilt via `build_entities_json.py` (now 3 continents, 17 countries, 155 LOD events, 1 thread with 15 milestones).
- **Gates:** `validate.py` files=20 rules=25 fails=0 (`--offline` across data/; online 200 on new continent file). `check_research.py --fast` PASS. `check_registry.py` rows=10 fails=0. `check_lod_labels.py` LOD LABEL GATE: PASS. `check_layout.py` all structural / country / containment / zero-overlap / thread gates 0 (15 milestone peaks drawn, dense labels curated out cleanly); `clipped` 625 pre-existing alone drives RESULT: FAIL.
- **Open follow-ups:** P3-T9 (authoring 5–9 countries for `transformer-plateau` in `data/countries/` and filling Table 1 in `data/coverage/transformer-plateau.md`).

---
### Session 26 (kept for reference)

# STATUS — as of 2026-09-17 (session 26: final staging clear-out — compute infrastructure / mega-financing / hardware / enterprise clouds + policy / safety incidents / copyright / governance / research discoveries promotions into research/08 + /09)

## One-line status

**Session 26 — pushed to `main`: the final 38 open rows of `data/staging/innermost-loop-candidates.md` — compute infrastructure, mega-financing, hardware and enterprise clouds (SK Hynix's $38B fabs, CoreWeave and Nebius Q2, the Decart talks, Nvidia's 13F / $99B equity book / SB Energy stake / Q2 FY2027 / Anthropic IPO anchor, Anthropic's $10B facility and record-IPO plan, Stripe–OpenRouter, Meta's Azure tokens, the Sol price cut, the SEC's Situational Awareness subpoenas, a16z's Machine Age Fund, Physical Superintelligence, Berkshire's Alphabet block) and policy, safety incidents, copyright, governance and research (the Fable 5 biology-classifier constitution, Cloudflare's machine-traffic crossover, Zuckerberg's essay, Gemini at 1B, HEIR, the gendered-bias and mind-virus and EEG papers, 404 Media's Amazon book scanning, Google's Spirit Airlines data, customer-held logs, Japan's comply-or-explain code, Brockman's consolidation, the Zaporizhzhia autonomous drone strike, the FDA AI deputy, China / New Zealand companion rules, ARIA's AI-song ban, Sony–Warner v. Anthropic) — are promoted into research/08 [281]–[318] and research/09 [b24]–[b26], [c43]–[c52], [d60]–[d65], [e27]–[e30], with every URL fetched, blocked ones verified by syndication / Google News RSS / Wayback and allowlisted with notes; staging is now 238/238 `[x]`; all gates green except the pre-existing `clipped` 625.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 38 rows ticked — the staging file is fully cleared (238 `[x]`, 0 open). research/08 timeline +18 rows (several candidates consolidated into multi-source rows per the brief), slotted by date among the existing Aug–Sep 2026 rows: *7 Aug* Fable 5 biology constitution [283] and SK Hynix fabs + Cloudflare crossover [281][282]; *10 Aug* Zuckerberg essay + Mind Viruses [284][285]; *11 Aug* CoreWeave + Nebius + Gemini 1B [286][287][288]; *13 Aug* Decart talks and collapse [289]; *14 Aug* Nvidia 13F + HEIR [290][291]; *15–17 Aug* SB Energy + Crunchbase + OpenRouter report [292][293]; *16–17 Aug* Amazon books + Spirit data + gendered-bias paper [294][295][296]; *18–21 Aug* Anthropic credit facility / IPO size / customer-held logs + Stripe–OpenRouter + Meta–Azure + Sol price cut [297]–[302]; *19 Aug* Japan comply-or-explain [303]; *20 Aug* Brockman + EEG decoding [304][305]; *24–25 Aug* Zaporizhzhia drone + SEC / Situational Awareness + FDA AI deputy [306][307][308]; *25–26 Aug* China / NZ companions + ARIA [309][310][311]; *26 Aug* Nvidia Q2 FY2027 [312]; *28–29 Aug* a16z Machine Age + Sony–Warner v. Anthropic [313][314]; *1 Sep* Physical Superintelligence [315]; *4–5 Sep* Nvidia $99B + Berkshire / Alphabet [316][317]; *11 Sep* Nvidia anchors Anthropic IPO [318]. research/09: thread (b) Embodiment Road +3 rows [b24]–[b26], description extended to [b26]; thread (c) Conscience Road +4 rows [c43]–[c52], description to [c52]; thread (d) Silicon River +4 rows [d60]–[d65] (one cross-cites the existing [d28] Ohio credit line and [d37] memory crunch), description to [d65]; thread (e) Commons Road +2 rows [e27]–[e30], description to [e30]. No thread-ID cites in research/08 (cross-file references are prose, "(file 09d)"); the Anthropic IPO-size row cross-references [161] in prose and the SB Energy / $99B rows point to [d28] via "(file 09d)".
- **Dates and claims corrected against sources:** Fable 5 biology post is dated 7 Aug on the page (staging ~8); Zuckerberg essay 10 Aug (staging ~12; Guardian same day); Pichai's Gemini post 11 Aug 17:00 UTC (staging ~12); HEIR 14 Aug; Crunchbase 17 Aug; 404 Media 17 Aug; Bloomberg Law 17 Aug; Mind Viruses submitted 10 Aug (staging ~19); gendered-bias paper submitted 13 Aug (staging ~16); Stripe–OpenRouter announcement 19 Aug (staging ~21; TechCrunch/Bloomberg price report 16 Aug); Verge Brockman piece 20 Aug (staging ~23); Sol price cut 21 Aug 19:34 UTC (staging ~23); EEG paper submitted 20 Aug (staging ~25); Nebius 13 Aug; The Information SB Energy 15 Aug (staging ~16); JURIST NZ 25 Aug (staging ~27); BBC ARIA 25 Aug (staging ~29); a16z 28 Aug (staging ~29); MBW 29 Aug on a 28 Aug filing (staging ~31); Wissner-Gross 1 Sep (staging ~2). Claims: the Madonna cover peaked at **No. 2** overall (No. 1 on the dance chart), not #1 as staged; Nvidia's release guides **Q3 $108B** — the staged "~70% growth for FY2028" does not appear in it and was dropped; SK Hynix's figure is **54.3 trillion won** split 35.2T Yongin (HBM/DRAM) + 19.1T Cheongju (NAND), board-approved 7 Aug (verified via Engadget — the staging row had no URL); Spirit's **7.5 billion** are passenger *transaction* records, de-identified, and the 97.5 million passenger profiles are excluded; China's companion rules date from **15 July** (the Guardian piece is the 25–26 Aug report); Decart talks (13 Aug, ~$6B) were **abandoned 8 Sep** per Bloomberg syndication — folded into the same row; Anthropic's IPO-size story is Japan Times/Bloomberg 21 Aug and does not itself carry the $65B run-rate / $11.5B Q2 figures, so those were not asserted; the NYT drone piece is a two-headline package ("A Drone Killed Three Ukrainians…" / "Minicomputers Made by Nvidia…"), strike date 6 July, three dead (19, 41, 48).
- **Sourcing hygiene:** every URL fetched before citing (browser-UA fetcher, keyword-window extractor, Google News RSS decoder, Wayback CDX/availability API). Live 200: anthropic.com ×2, theregister.com, cnbc.com ×6, x.com ×3 (snowflake-dated), nebius.com (+ press-release PDF via pypdf), blog.google, theinformation.com (headline/byline/date only), arxiv.org ×3, 404media.co, news.bloomberglaw.com, news.crunchbase.com, stripe.com, japantimes.co.jp ×2, theverge.com, nvidianews.nvidia.com, theguardian.com ×2, jurist.org, a16z.com, bbc.com, musicbusinessworldwide.com, plus pickups engadget.com, finance.yahoo.com, jpost.com, fortune.com, thenextweb.com ×2, finance.biggo.com, meduza.io, techcrunch.com ×2, pymnts.com, calcalistech.com, technologyreview.com. Allowlisted 10 blocked URLs with verification notes: bloomberg.com ×6 (403; Decart / 13F / credit facility / IPO size / retention / Meta–Azure via Google News RSS + Yahoo Finance, Fortune, Japan Times, BigGo, The Next Web, Anthropic 1 Sep post), nytimes.com ×2 (403; no Wayback snapshot; RSS headlines + Meduza / TechCrunch / CNBC), reuters.com ×2 (401; RSS + CNBC / PYMNTS / Calcalist). Pitfalls this session: `meta.com/thefutureisforeveryone/` is 400 to bots and a JavaScript shell even in its Wayback snapshot (20260810102317) — the checker does not flag it, but the essay text was verified from the Guardian and cited alongside; `theinformation.com` and `meta.com` pass the checker without allowlisting, so allowlist only what `check_links.sh` actually fails; Nebius' newsroom page carries no figures — they live in a linked PDF; the staging SK Hynix row had no URL — Google News RSS surfaced the Engadget report.
- **Gates:** `validate.py` files=19 rules=25 fails=0. `check_research.py`: 08, 09, 04 all R-01…R-07 PASS on the final pass (08: 188 rows / 318 sources / 534 links, 0 failed, 92 allowlisted; 09: 16 rows / 224 sources / 473 links, 0 failed, 68 allowlisted; 04: 34 / 92 / 102, 0 failed). `check_lod_labels.py` PASS (lod4 47 marks, 75 one-line rows, curated-out unchanged). `check_layout.py` all structural / country / containment / overlap / thread gates 0; `clipped` 625 pre-existing, RESULT: FAIL is that gate alone. Nothing under `site/` or `data/regions/` changed, so no tile rebuild.
- **Open follow-ups:** z4 text needs an SVG label overlay to be crisp. Staging is empty (238/238) — the next digest pass starts a fresh candidate file. None of the promoted items are on the map; the 24 Aug autonomous-drone strike ([306]/[b25]) is the strongest Conscience Road event candidate of the session and the 4–5 Sep / 11 Sep Nvidia equity-circularity rows ([316][318]/[d64][d65]) the strongest Silicon River one.

---
### Session 25 (kept for reference)

# STATUS — as of 2026-09-17 (session 25: products / autonomous agents / developer platforms + frontier model releases / multimodal / autonomous research / coding promotions into research/08 + /09)

## One-line status

**Session 25 — pushed to `main`: the two clusters the session-25 brief named — products, autonomous agents and developer platforms (New Orleans' AI 911 triage, ChatGPT for Teens, Private Safety Processing, Mechanical Turk's closure, Reuters on Meta's abandoned 60% agent-replacement plan, Salesforce's CRM inside Claude, Perplexity's Portable Computer, OpenAI's persistent Codex agent, the Cursor wind-down, OpenClaw 2.0, the Cybercab launch, ChatGPT health records, Meta Muse) and frontier model releases, multimodal, autonomous research and coding (Poetiq's Metasystem, Ultrafast on Cerebras, DeepMind's SL2T, Inherent Labs' Faraday, Prime Intellect's speedrun study, Wan3.0, the Fable 5.1 routing sighting, Gemini 3.8 Flash / Flash Cyber, Muse Spark 1.3, World Labs Atlas, WeatherNext 3, Cognition SWE-2, GPT-Live-1 and ChatGPT Images 2.5) — are promoted from staging into research/08 [254]–[280] and research/09 [a13]–[a16], [b21]–[b23], [c38]–[c42], [e23]–[e26], with every URL fetched, blocked ones verified by Wayback / syndication / Google News RSS and allowlisted with notes; all gates green except the pre-existing `clipped` 625.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 27 rows ticked (the brief's 26 candidates; GPT-Live-1 and Images 2.5 are two staging rows; 200 of the file's rows now `[x]`, 38 open). research/08 timeline +21 rows, slotted by date among the existing Aug–Sep 2026 rows: *4 Aug* Poetiq Metasystem [254]; *late Jul–9 Aug* New Orleans 911 [255]; *12 Aug* SL2T [256]; *13 Aug* Ultrafast [257]; *14 Aug* Faraday + Prime Intellect [258][259]; *18–19 Aug* ChatGPT for Teens + Private Safety Processing [260][261]; *24 Aug* Wan3.0 [262]; *25 Aug* Mechanical Turk [263] and Perplexity Portable Computer [279]; *26 Aug* Salesforce in Claude [264], Reuters' Project OT [265], the Fable 5.1 routing sighting [278]; *27 Aug* persistent Codex agent [266]; *28 Aug* Cursor wind-down [267]; *30 Aug* OpenClaw 2.0 [268]; *1 Sep* Atlas + ChatGPT health records [269][270]; *2–3 Sep* Gemini 3.8 Flash/Cyber + Muse Spark 1.3 [271][272]; *3 Sep* Cybercab + WeatherNext 3 [273][274]; *8 Sep* Meta Muse [280]; *8–10 Sep* ChatGPT Images 2.5 + GPT-Live-1 [275][276]; *10 Sep* SWE-2 [277]. research/09: thread (a) Reasoning Road +3 rows [a13]–[a16], description extended to [a16]; thread (b) Embodiment Road +3 rows [b21]–[b23], description extended to [b23]; thread (c) Conscience Road +3 rows [c38]–[c42], description extended to [c42]; thread (e) Commons Road +2 rows [e23]–[e26] (one cross-cites [a16]), description extended to [e26]. No thread-ID cites in research/08 (cross-file references are prose, "(file 09a)").
- **Dates and claims corrected against sources:** Poetiq post is 4 Aug (staging ~8 Aug); SL2T 12 Aug and Ultrafast 13 Aug (staging ~13); Faraday and Prime Intellect both 14 Aug (staging ~16); ChatGPT for Teens 18 Aug, Private Safety Processing 19 Aug; Salesforce/VentureBeat 26 Aug and Perplexity 25 Aug (staging ~27); Cursor post 28 Aug and WIRED persistent-agent piece 27 Aug (staging ~29); OpenClaw 2.0 30 Aug (staging ~31); Atlas 1 Sep, Gemini 3.8 Flash 2 Sep, Muse Spark 1.3 2 Sep, WeatherNext 3 3 Sep (staging ~3); ChatGPT health records 1 Sep (staging ~3); Cybercab public rides 3 Sep (staging 2 Sep is the Reuters preview date); ChatGPT Images 2.5 8 Sep, GPT-Live-1 10 Sep, SWE-2 10 Sep, Meta Muse 8 Sep (staging ~12); Fable 5.1 routing post 26 Aug 15:21 UTC by snowflake (staging ~27). Claims: SL2T is *trained on* 50+ sign languages but ships ASL→English only, 70 BLEURT zero-shot, landmarks-only upload; Ultrafast is 14× on GPT-5.6 Sol at ~750 tok/s, $75/$300 per M tokens, 10 rpm per org; Prime Intellect is 153 runs over 18 models, Fable 5 2,726 steps = 81.7% of the gap closed in 8.7 days, "none of the runs produced a fundamentally new method"; Faraday is 27B, 310 Replica tasks from 100 papers, better "for every category of paper"; Mechanical Turk closes effective 30 Sep; Meta's plan was "Project OT", 60% of *some* team headcounts, second layoff round cancelled, incidents +40% (Ars Technica quoting Reuters); Salesforce's Claude connector has 37 skills (30 sales-specific), "roughly 60%" of sellers' time in CRM, consumption pricing; Perplexity local models are PPLX 27B and Qwen 3.8 27B on DGX Spark or 24 GB RTX; OpenClaw 2.0 is 933 contributors (569 first-time), >16,000 PRs, 106 releases in 230 days; Cybercab is 45 registered vehicles, "under $30,000" per Musk; ChatGPT health records connects >1,300 hospitals and >30,000 clinics via Epic, Cerner, Athena, Meditech; Gemini 3.8 Flash Cyber is 2.6× more remediated vulnerabilities with 76% valid fixes, agentic video −88% tokens at 4 fps; Muse Spark 1.3 max scores 62 on AAII (xhigh 61) at $0.55 per task, weights undecided; Atlas is a multimodal autoregressive diffusion transformer over text/image/video/3D; WeatherNext 3 is hourly ≤5 km directly from satellite observations; SWE-2 is post-trained from Kimi K3 (2.8T), 50.0% FrontierCode 1.1 Main, within a point of Fable 5.1 at 64% lower cost, Terminal-Bench 4 27.3% vs 55.8%; GPT-Live-1 is full-duplex speech at ~5¢/min ($0.052 audio in + out); Images 2.5 adds sketch-based editing; Meta Muse (code name Hatch) rolls out in the US, free with $20/$100 tiers, in "its own isolated environment" per Wang — Meta newsroom + CNBC 8 Sep (ai.meta.com/muse and developer.meta.com are JS-rendered shells); the staging phrase "for US adults" was not verifiable and was not used.
- **Sourcing hygiene:** every URL fetched before citing. Live 200: poetiq.ai, nypost.com, deepmind.google, inherentlabs.ai, primeintellect.ai, cnbc.com ×2 (Mechanical Turk, Muse), about.fb.com, arstechnica.com, openclaw.ai, blog.google ×2, worldlabs.ai, cognition.com, x.com (legit_api; snowflake-dated), wired.com, thenextweb.com, the-decoder.com, siliconangle.com, businessinsider.com, thenewstack.io, computerworld.com, developer.meta.com (200 but JS-rendered — no server-side text), web.archive.org. Allowlisted 12 blocked URLs with verification notes: openai.com ×7 (403 to the checker; full text via Wayback snapshots 20260815181741 / 20260824171941 / 20260915120957 / 20260913234942 / 20260910062021 / 20260915174538 / 20260915202858), venturebeat.com (403/429; Wayback 20260827022716), perplexity.ai (403 Cloudflare; Wayback 20260915132159 + launch date via Google News RSS), reuters.com ×3 (401; headline + date via Google News RSS, details via The Next Web / Ars Technica / Business Insider). Pitfalls this session: `ai.meta.com/muse/` and `developer.meta.com/ai/models/muse-spark/` return 200 with an empty JS shell — text verified from CNBC / The Decoder / SiliconANGLE instead; the New Orleans row's "first deployed in late July" comes from the NYPost body, so its row is dated "late Jul–9 Aug"; the Cursor post does not mention Anthropic — the "Anthropic pledges more compute" staging claim was dropped as unverified.
- **Gates:** `validate.py` files=19 rules=25 fails=0. `check_research.py`: 08, 09, 04 all R-01…R-07 PASS on the final pass (08: 170 rows / 280 sources / 478 links, 0 failed, 82 allowlisted; 09: 16 rows / 201 sources / 424 links, 0 failed, 60 allowlisted; 04: 34 / 92 / 102, 0 failed). `check_lod_labels.py` PASS (lod4 47 marks, 75 one-line rows, curated-out unchanged). `check_layout.py` all structural / country / containment / overlap / thread gates 0; `clipped` 625 pre-existing, RESULT: FAIL is that gate alone. Nothing under `site/` or `data/regions/` changed, so no tile rebuild.
- **Open follow-ups:** z4 text needs an SVG label overlay to be crisp. Staging: 38 unticked rows; remaining clusters are thin. None of the promoted items are on the map; the 14 Aug autonomous-research pair ([258][259]) is the strongest Reasoning Road event candidate and the 25–26 Aug labour pair ([263][265]) the strongest Conscience Road one.

---
### Session 24 (kept for reference)

# STATUS — as of 2026-09-17 (session 24: compute-infrastructure / sovereign-energy / supply-chain + safety / threat-intelligence / policy / legislative promotions into research/08 + /09)

## One-line status

**Session 24 — pushed to `main`: the two clusters the session-24 brief named — compute infrastructure, sovereign energy and the supply chain (EO 14421 bulk-power emergency, semiconductor tariffs, the China remote-access rule, Germany's 2030 compute target, SpaceX's turbine-blade factory, OpenAI's Mac fleet, SB Energy's $5.5B warrants, Anthropic's $35B Lambda deal and $517B/14.8 GW tally, Dell's $95B backlog, the ASML 12-inch-mask roadmap, the Duane Arnold DOE loan, Qualcomm–AWS warrants, Google's €13B Finland commitment, OpenAI–Samsung chips, ten states tearing up data-centre tax breaks, Oracle's tripled capex) and safety, threat intelligence, policy and legislation (NYC's K-8 AI moratorium, OpenAI's "automated shutdown capabilities" letter, the G20 Carolina Principles, the DOJ fair-use Statement of Interest, the Pentagon–Commerce split on Anthropic, the Sanders–Casar ASI ban bill, Anthropic's September threat report, OpenAI's four California bills, the Senate "duty of care" draft) — are promoted from staging into research/08 [228]–[253] and research/09 [c29]–[c37], [d43]–[d59], with every URL fetched, blocked ones verified by Wayback / syndication / Google News RSS and allowlisted with notes; all gates green except the pre-existing `clipped` 625.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 26 rows ticked (173 of the file's rows now `[x]`, 65 open). research/08 timeline +10 rows, slotted by date among the existing Aug–Sep 2026 rows: *26–28 Aug* EO 14421 + semiconductor tariffs + China remote-access rule [228][229][230]; *27–29 Aug* Germany compute shortage + SpaceX turbine blades [231][232]; *30–31 Aug* OpenAI Mac fleet + SB Energy warrants + Anthropic–Lambda $35B [233][234][235]; *1–2 Sep* Dell $95B backlog + NYC moratorium + shutdown letter [236][237][238]; *2–3 Sep* G20 Carolina Principles + DOJ fair use + Pentagon ban + Sanders–Casar bill [239]–[242]; *6 Sep* Anthropic $517B/14.8 GW [243]; *8–9 Sep* ASML masks + Duane Arnold + Qualcomm–AWS + Finland + Samsung [244]–[248]; *9–10 Sep* states' tax breaks/Massachusetts + Anthropic threat report [249][250]; *10 Sep* Oracle Q1 FY2027 [251]; *9–11 Sep* OpenAI policy window + Senate duty of care [252][253]. research/09: thread (c) Conscience Road +2 rows [c29]–[c37] and description extended to [c37]; thread (d) Silicon River +3 rows [d43]–[d59] and description extended to [d59]. No new thread-ID cites in research/08 (R-04 pitfall from session 22 respected — cross-file references are prose, "(thread (c), file 09)").
- **Dates and claims corrected against sources:** staging had "EO 14420" — the order is **Executive Order 14421** (whitehouse.gov text; 14420 is not this order), signed 26 Aug (staging ~28 Aug); the Lambda deal is WSJ 31 Aug (staging ~3 Sep); SB Energy warrants 31 Aug; Apple/Mac piece 30 Aug (staging ~31); The Information's $517B tally 6 Sep (staging ~7); China remote-access rule 28 Aug (staging ~29); SpaceX 29 Aug; Sanders–Casar press release 3 Sep; states' tax breaks WSJ 9 Sep (staging ~12), Massachusetts EO 8 Sep; OpenAI's policy post 9 Sep (staging ~12) and it backs **four** California bills (SB 813, AB 1405, SB 1119, AB 1864), not three; NYC's moratorium is K-8 (2-K through 8th grade, ~600,000 students) reported 1 Sep, announced 2 Sep; Oracle capex $28.5B vs $8.5B (tripled), with $664B RPO, $125B debt, −$5.4B FCF; Dell $60.9B AI orders / $16.4B AI revenue / $95B backlog / $74B FY guide; Qualcomm warrants 25M shares (~$4B) vesting against up to $60B of purchases; Duane Arnold 615 MW, restart 2029; Finland ≥€13B (~$15.1B); Germany's minister is Karsten Wildberger and the 2030 "quadruple" is the federal AI/HPC target restated amid the shortage; Anthropic threat report: five biological-misuse case studies among seven harm areas, Dec 2025–Aug 2026, all on Haiku/Sonnet/Opus.
- **Sourcing hygiene:** every URL fetched before citing. Live 200: whitehouse.gov, cnbc.com ×5 (semiconductor tariffs, Dell, Qualcomm, Finland, Oracle), techcrunch.com, sanders.senate.gov, anthropic.com, theinformation.com ×4 (metadata only — figures from 24/7 Wall St., TradingKey, Tom's Hardware ×2 pickups), plus pickups tomshardware.com, 247wallst.com, tradingkey.com, finance.yahoo.com, trendforce.com, netz-trends.de, meritalk.com, lowenstein.com, finance.biggo.com, tradingview.com (Reuters syndication), spokesman.com (Reuters syndication), nyc.gov, k12dive.com, dailysignal.com, wbur.org, web.archive.org. Allowlisted 14 blocked URLs with verification notes: bloomberg.com ×5 (403; Germany/ASML/Finland/Pentagon via Google News RSS + pickups, G20 via Wayback 20260907072831), wsj.com ×3 (Wayback 20260910190533 / 20260907002038 / 20260914 full text), reuters.com ×4 (401; shutdown + duty-of-care via Google News RSS + newspaper syndication, fair use via RSS + Lowenstein alert, Samsung via Wayback 20260910021209), nytimes.com (403; RSS + NYC Mayor's Office + K-12 Dive), openai.com/index/ai-policy-window (403 to the checker; Wayback 20260916153304). Pitfalls this session: `check_research.py` R-05 requires the literal `(accessed YYYY-MM-DD)` — "(accessed … via web.archive.org)" fails; the Galveston Daily News Reuters copy first used for [238]/[c30] rate-limits the checker (429) — swapped for the TradingView Reuters syndication (stable 200); pre-existing web.archive.org URLs in 08/09 time out (000) intermittently and pass on rerun, nothing allowlisted for them.
- **Gates:** `validate.py` files=19 rules=25 fails=0. `check_research.py`: 08, 09, 04 all R-01…R-07 PASS on the final pass (08: 149 rows / 253 sources / 443 links 0 failed 70 allowlisted; 09: 16 / 185 / 401, 0 failed 54 allowlisted; 04: 34 / 92 / 102, 0 failed). `check_lod_labels.py` PASS (lod4 47 marks, 75 one-line rows, curated-out unchanged). `check_layout.py` all structural / country / containment / overlap / thread gates 0; `clipped` 625 pre-existing, RESULT: FAIL is that gate alone. Nothing under `site/` or `data/regions/` changed, so no tile rebuild.
- **Open follow-ups:** z4 text needs an SVG label overlay to be crisp. Staging: 65 unticked rows; remaining clusters are thin. None of the promoted items are on the map; the 1–3 Sep governance rows ([237]–[242]) are the strongest Conscience Road event candidate ("every branch at once") and the 8–9 Sep infrastructure row ([244]–[248]) the strongest Silicon River one.

---
### Session 23 (kept for reference)

# STATUS — as of 2026-09-17 (session 23: GPT-6 Astra emergence / frontier benchmarks / scientific controversies + open-weights geopolitics / distillation / open model releases promotions into research/08 + /09)

## One-line status

**Session 23 — pushed to `main`: the two clusters the session-23 brief named — GPT-6 Astra's emergence, its third-party benchmarking and the scientific controversies around it (Altman's AGI-this-year interview, the recurrent-depth legibility dispute, Fortune's "benchmaxxing" metric revisions, Artificial Analysis / Epoch FrontierMath 97.6% / Robocurve 19-of-20 / Portal for $571 / ValsAI saturation / Vending-Bench $15,515, Buckmaster's statement and the 771-signature Caltech Mathathon letter) and open-weights geopolitics, the distillation contest and open model releases (Muse Glimmer, Nemotron 3.5 Lightning + Switchyard, WIRED's hidden-trace extraction, Gemma's billionth download, WSJ's $6B Nemotron 4, Ox Alpha → GLM-5.3-Flash, Qwen3.8-Flash, Moonshot's 30% K3 offer, the GLM-5.3 weights licence, NYT's Inspur/Aivres $5.6B, ByteDance's world model, the NSA/CISA/FBI six-lab distillation advisory, DeepSeek V4.1-Flash) — are promoted from staging into the research corpus: research/08 [203]–[227] and research/09 Thread (b) [b20], Thread (c) [c26]–[c28], Thread (d) [d42], Thread (e) [e18]–[e22]. All 25 staging rows ticked, every URL fetched or verified by syndication/archive, 7 bot-blocked URLs allowlisted with method, all gates in the same state as session 22.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 25 rows ticked (147 of the file's rows now `[x]`, 91 open). research/08 timeline +13 rows, slotted by date among the existing Aug–Sep 2026 rows: *10–11 Aug* Muse Glimmer + Nemotron 3.5 Lightning/Switchyard [203][204]; *11 Aug* WIRED hidden-trace extraction [205]; *20 Aug* Gemma 1B downloads [206]; *20–23 Aug* Ox Alpha stealth + WSJ Nemotron 4 [207][208]; *26–27 Aug* GLM-5.3-Flash + Qwen3.8-Flash + Moonshot K3 revenue share [209][210][211]; *26–28 Aug* Altman AGI-this-year / Astra preview [212]; *28 Aug* GLM-5.3 weights + hyperscaler licence [213]; *2–4 Sep* recurrent-depth legibility + benchmaxxing [214][215]; *4–7 Sep* Artificial Analysis / FrontierMath / Robocurve / Portal / ValsAI [216]–[220]; *8–10 Sep* Buckmaster + Caltech letter [221][222]; *6–7 Sep* NYT Inspur/Aivres + Bloomberg Zhang Yiming [223][224]; *8–9 Sep* distillation advisory [225]; *7–10 Sep* DeepSeek V4.1-Flash + Vending-Bench [226][227]. research/09: Thread (b) +1 row ([b20] Robocurve), description extended to [b20]; Thread (c) +3 rows ([c26][c27] legibility + benchmaxxing; [e19] cross-cited for the GLM-5.3 licence; [c28] Buckmaster + Caltech), description extended to [c28]; Thread (d) +1 row ([d42] Inspur/Aivres, [e18] cross-cited for Nemotron 4), description extended to [d42]; Thread (e) +3 rows ([e18] US small open models + Nemotron 4; [e19][e20] Ox Alpha/GLM-5.3-Flash/Qwen3.8-Flash/Moonshot; [e21][e22] advisory + V4.1-Flash + ByteDance), description extended to [e22].
- **Dates and claims corrected against sources:** staging had ~29 Aug for the Altman piece (TIME interview 26 Aug, Sources.news digest ~28–29; written 26–28 Aug); ~2026-09-03 for the recurrent-depth story (TechCrunch pickup 2 Sep; written 2–3 Sep); ~6 Sep for Robocurve (figure timestamps 2026-09-04); ~6 Sep for FrontierMath (run started 5 Sep per benchmarks.csv); ~12 Sep for Vending-Bench (posted 7 Sep); ~12 Sep for DeepSeek V4.1-Flash (page date 10 Sep, pricing effective 04:00 UTC 10 Sep); ~2026-08-12 for WIRED and Nemotron (both 11 Aug); ~21 Aug for Gemma (20 Aug); ~23 Aug for Ox Alpha (dropped on OpenRouter 20 Aug, Wccftech 21 Aug); ~29 Aug for the GLM-5.3 weights (The New Stack 28 Aug 17:42Z); ~10 Sep for Buckmaster (TechCrunch 8 Sep). Claims: Robocurve's "19/20 vs 8/20 at half the cost" is 19 of 20 vs 8 of 20 (Fable 5: 1 of 20), 2.5 vs 6.8 min per trial, $0.94 vs $2.12 per run; Vending-Bench "triples" is $15,515 vs $5,422 average over six runs, "almost three times as much", and Astra is the first OpenAI model to rank #1 there; Qwen3.8-Flash is 125B parameters with open weights (Bloomberg via Deccan Chronicle), HK$80B = $10.2B follow-on; Moonshot's offer is "up to a 30pc share" of K3-related cloud revenue; the distillation advisory names six labs (DeepSeek, Moonshot, Alibaba, MiniMax, StepFun, Z.AI) and is a joint NSA/CISA/FBI advisory per CyberScoop; NYT's figure is "at least $5.6 billion" April 2024–February 2026 with ">$3 billion" of Blackwell servers, per ImportGenius records; DeepSeek V4.1-Flash is a 552B MoE with 8B active input / 16B active output parameters; GLM-5.3-Flash's licence is MIT at $0.15/$0.50 per million tokens, OpenRouter lists it created 2026-08-26T15:59Z with 1.31M context ("biggest launch" was not verifiable and was dropped); Muse Glimmer is 30B under Apache 2.0, "a novel distillation recipe" from a larger teacher; ValsAI saturation is a single X post by @chrisgpt.
- **Sourcing hygiene:** every URL fetched before citing. Live 200: research.meta.ai, blogs.nvidia.com, wired.com, blog.google, wccftech.com, z.ai (JS-rendered — text read from the page's asset bundle), openrouter.ai API, deccanchronicle.com, siliconrepublic.com, sources.news, thenewstack.io, theinformation.com (200 this session; page metadata only), techcrunch.com ×2, fortune.com, artificialanalysis.ai, epoch.ai (leaderboard + benchmarks.csv), openai.robocurve.org, tomshardware.com, x.com (chrisgpt; fxtwitter mirror for text), cims.nyu.edu (PDF via `/tmp/pdfvenv` pypdf), proofsandprompts.com, andonlabs.com, deepseek.com, freepressjournal.in, thenextweb.com, nbcnews.com, cyberscoop.com, web.archive.org (WSJ). Allowlisted with method: wsj.com (401; Wayback 20260910004217 page metadata gives headline + datePublished 23 Aug), bloomberg.com ×2 (403, no-www canonical for Qwen as staged; Deccan Chronicle full syndication; The Next Web + Yahoo Finance SG for ByteDance), reuters.com ×2 (401; Google News RSS + Silicon Republic / NBC + CyberScoop), time.com (406; Wayback 20260916225300; Sources.news digest cited first), nytimes.com (403, no snapshot; Google News RSS + Free Press Journal figures). `/tmp/s21_gdecode.py` again did the paywalled-headline work; `/tmp/s23_get.py` (browser-UA fetch + keyword sentences) is the fetch helper.
- **Gates:** `validate.py` files=19 rules=25 fails=0. `check_research.py`: 08, 09, 04 all R-01…R-07 PASS (08: 139 rows / 227 sources / 399 links 0 failed 56 allowlisted; 09: 16 / 159 / 359, 0 failed 40 allowlisted — 2 transient failures on a first pass, 0 on rerun and on `check_links.sh` alone; 04: 34 / 92 / 102, 0 failed). `check_lod_labels.py` LOD LABEL GATE: PASS (lod4 47 marks / 75 one-line rows, curated-out unchanged). `check_layout.py` all structural / country / containment / zero-overlap / thread gates 0; `clipped` 625 (pre-existing; RESULT: FAIL is that gate alone). Nothing under `site/` or `data/regions/` changed.
- **Open follow-ups:** z4 text needs an SVG label overlay to be crisp. Staging: 91 unticked rows; remaining clusters are thin. None of the promoted items are on the map; the 4–7 Sep Astra benchmark row ([216]–[220]) and the distillation advisory ([225]) are the strongest map-event candidates (Reasoning Road / Commons Road).

---
### Session 22 (kept for reference)

# STATUS — as of 2026-09-17 (session 22: AI-memory-crunch / chip-supply-chain / chip-geopolitics + AI-safety / policy / governance promotions into research/08 + /09)

## One-line status

**Session 22 — pushed to `main`: the two clusters the session-22 brief named — the AI memory crunch, hardware supply chain and chip geopolitics (2027 DRAM/HBM sellout, DDR5 +485%, NYT memory lobbying, WSJ Apple–CXMT/YMTC and Lutnick, Situational Awareness' $400M lithography bet, Trump's Section 232 polysilicon floor + 15% tariff, Nvidia's >15% server price hikes, Micron's $10B Research Labs, OpenAI's Jalapeño first results) and AI safety, policy and governance escalation (DOE Genesis Open Models + Genesis-Science-1, Sanders' pause letter, Claude's EU-mandated text watermark + the Commission's "AI generated" icons + Gruber, the White House framework extending to open weights, Anthropic's August Risk Report with "Model 2" / risk "low" / saturated evals, the Redwood–Anthropic Conceptual Reasoning Index, OpenAI's Collective Cyberdefense call, Judge Lin vacating the Pentagon's Anthropic blacklisting) — are promoted from staging into the research corpus: research/08 [183]–[202] and research/09 Thread (c) [c21]–[c25] + Thread (d) [d37]–[d41]. All 19 staging rows ticked, every URL fetched or verified by syndication/archive, 10 bot-blocked URLs allowlisted with method, all gates in the same state as session 21.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 19 rows ticked (122 of the file's rows now `[x]`, 116 open). research/08 timeline +10 rows, slotted by date among the existing Aug 2026 rows: *6–7 Aug* polysilicon Section 232 proclamation [183]; *5–17 Aug* memory crunch (Digitimes sellout via IGN, Tom's Hardware price tracker, NYT lobbying, WSJ Apple/CXMT/YMTC + Lutnick) [184][185][186][187]; *7–9 Aug* Situational Awareness → Source Foundry [188]; *8 Aug* DOE Genesis Open Models + Genesis-Science-1 [189]; *10 Aug* Sanders letter [191]; *10–16 Aug* Claude watermark / EC icons / Gruber [192][193][194]; *12–14 Aug* White House framework → open weights + Risk Report "Model 2" + CRI [195][196][197]; *20–22 Aug* Micron $10B Research Labs + Nvidia >15% hikes [200][201]; *25 Aug* Jalapeño first results [202]; *27–28 Aug* Collective Cyberdefense + Judge Lin's Pentagon ruling [198][199]. research/09: Thread (c) +4 rows ([c21] Sanders; [c22] watermark/icons; [c23] White House + CRI + Risk Report; [c24][c25] cyberdefense + ruling), description extended to [c25]; Thread (d) +3 rows ([d37][d38] memory crunch; [d39][d40] polysilicon + Source Foundry; [d41] Micron + Nvidia hikes), description extended to [d41].
- **Jalapeño handling:** the brief said reuse research/09's `[d13]` in research/08 — but `check_research.py` R-04 rejects thread-prefixed ids in research/08 ("cited but undefined: ['d13']"), as it does `[c8]` and `[d16]`. Added `[202]` in research/08 pointing at the same OpenAI URL + Wayback copy and cross-noting `[d13]`; the two cross-thread prose references were rewritten as "(file 09c)/(file 09d)" like the neighbouring rows.
- **Dates and claims corrected against sources:** staging had ~8 Aug for the DRAM sellout (IGN datePublished 5 Aug), ~19 Aug for DDR5 +485% (Tom's Hardware 17 Aug; +485% is the 2×32 GB DDR5-5600 row, kits range +355–485%), ~14 Aug for the WSJ Apple piece (datePublished 15 Aug 01:00Z, i.e. 14 Aug US; written 10–14 Aug with the CXMT testing report), ~8 Aug for Source Foundry (WSJ 7 Aug, TechCrunch 9 Aug), 2026-08-11 for the Register piece (00:27Z 11 Aug, help doc "published on Monday" = 10 Aug), ~12 Aug for the EC icons (page "Last update 10 August 2026"), ~12 Aug for Sanders (letter dated 10 Aug), ~17 Aug for Gruber (Sunday 16 Aug; Anthropic's explainer is 14 Aug), ~13 Aug for WIRED (12 Aug), ~14 Aug for CRI (12 Aug), ~23 Aug for Micron (dateline 20 Aug), ~27 Aug for Jalapeño (25 Aug, as [d13]), ~29 Aug for Collective Cyberdefense (TechCrunch 27 Aug — "over a hundred" signatories then; the 150+ is the current list), 2026-08-28 for the ruling (order issued Thursday night 27 Aug, Reuters/Guardian dated 28 Aug — written 27–28 Aug). Claims: the staging digest's "memory chip prices roughly quadruple" is not in the NYT primary metadata (the headline is about lobbying) and was not used; Jalapeño is 1.5–1.9× perf/W and 1.7–3.6× latency (ranges, not point figures); the Risk Report's "Model 2" is "somewhat more capable than Mythos 5" with no release plans, the "low" is an increase from "very low", and the saturation applies to the AI-R&D task-based evaluations; WIRED's framework is voluntary and unpublished; the Pentagon designation vacated is Hegseth's 27 Feb "supply-chain risk" order (Judge Rita Lin, N.D. Cal., 59 pages per Al Jazeera).
- **Sourcing hygiene:** every URL fetched before citing. Live 200: ign.com, tomshardware.com, theregister.com, digital-strategy.ec.europa.eu, daringfireball.net, wired.com ×2, alignment.anthropic.com, anthropic.com (watermark explainer), sanders.senate.gov (PDF), www-cdn.anthropic.com (Risk Report PDF), techcrunch.com ×2, gizmodo.com, thenews.com.pk, techrepublic.com, straitstimes.com, canarymedia.com, finance.yahoo.com, theguardian.com, aljazeera.com. Allowlisted with method: reuters.com ×2 (401; Google News RSS + Straits Times / Guardian–Al Jazeera–WIRED), nytimes.com (403; page metadata via Google News redirect gave headline, byline, published_time; Gizmodo pickup), wsj.com ×2 (401; Wayback snapshots 20260820160753 and 20260815170048 verified headline/byline/lede), genesisopenmodels.anl.gov (403 challenge; Wayback 20260826134643), axios.com (403; RSS date only, primary PDF cited), openai.com/collective-cyberdefense (403; Wayback 20260911185518 + TechCrunch), investors.micron.com (403; reader proxy), bloomberg.com (403, no snapshot; Reuters pickup on Yahoo Finance + CNA). Pitfall: several pickup URLs guessed from RSS titles were wrong slugs — always take the `rel=canonical` from the fetched page (Gizmodo, The News, TechRepublic, WIRED, Anthropic and Canary Media all differed).
- **Gates:** `validate.py` files=19 rules=25 fails=0. `check_research.py`: 08, 09, 04 all R-01…R-07 PASS (08: 126 rows / 202 sources / 360 links 0 failed 48 allowlisted; 09: 16 / 149 / 331, 0 failed 34 allowlisted — one transient `000` on a first pass, 0 on rerun; 04: 34 / 92 / 102, 0 failed). `check_lod_labels.py` LOD LABEL GATE: PASS (lod4 47 marks / 75 one-line rows, curated-out unchanged). `check_layout.py` all structural / country / containment / zero-overlap / thread gates 0; `clipped` 625 (pre-existing; RESULT: FAIL is that gate alone). Nothing under `site/` or `data/regions/` changed.
- **Open follow-ups:** z4 text needs an SVG label overlay to be crisp. Staging: 116 unticked rows; remaining clusters are thin (xAI/Colossus buildout, model-release odds and ends, misc lab events). None of the promoted items are on the map; the memory-crunch row ([184]–[187]) is the strongest Silicon River event candidate and the Pentagon ruling ([199]) the strongest Conscience Road one.

---
### Session 21 (kept for reference)

# STATUS — as of 2026-09-17 (session 21: physical-AI / robotics / autonomous-fleet + AI-for-science / math / bio-discovery promotions into research/08 + /09; research/04 europepmc fix)

## One-line status

**Session 21 — pushed to `main`: the two clusters the session-21 brief named — physical AI, robotics, embodiment and autonomous fleets (Dyna-2, Waymo CPUC, physical-AI $47.4B H1, GEN-1.5, Nevada 7,000 robotaxis + Waymo's 1,000-TOPS ASIC, SoftBank–1X, Model Hardware Standard, Nvidia's $10B physical-AI business) and AI for science, mathematics and bio-discovery (Riemann 41.6% → 67.2% Lean-verified, Claude protein design 14/15, GenBio AIDO Cell, Co-Scientist reactor/E. coli/HealthBench, BirdCODE, UCSF autism atlas, Insilico rentosertib) — are in the curated corpus as fourteen research/08 rows ([167]–[182]), six Embodiment Road rows ([b13]–[b19]) and two Silicon River rows ([d35]–[d36]) in research/09; research/04's two 403 europepmc links now point at PubMed. All gates in their expected state.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 16 rows ticked (103 of the file's rows now `[x]`, 135 open). research/08 timeline +14 rows, slotted by date among the existing Aug–Sep 2026 rows: *10 Aug* Riemann zeta lower bound [167]; *10–12 Aug* Dyna-2 human-to-robot transfer scaling law [168]; *14 Aug* CPUC 18-county approval [169]; *18 Aug* Crunchbase $47.4B/521 deals [170], Claude protein design + analytical chemistry [171], GenBio AIDO Cell [172]; *19 Aug* GEN-1.5 physical prompting [173]; *20 Aug* "robotaxi day" — Nevada 7,000 permits + Waymo sixth-gen compute / Bloomberg TSMC-5nm chip [174][175], BirdCODE [176]; *26–27 Aug* SoftBank–1X talks [177], Model Hardware Standard [178], Co-Scientist arXiv 2608.26701 [179]; *29 Aug* WSJ Nvidia physical AI / China [180]; *4 Sep* UCSF profound-autism atlas [181]; *7 Sep* Insilico rentosertib aging clocks [182]. research/09 Thread (b) Embodiment Road: description extended to [b1]–[b19], six milestone rows (10–12 Aug → 29 Aug) with cross-links to (c) and (d); Thread (d) Silicon River: description extended to [d1]–[d36], [d35] Waymo ASIC and [d36] Nvidia physical-AI/China rows.
- **Dates and claims corrected against sources:** staging had ~12 Aug for Riemann (page dated 10 Aug), ~12 Aug for Dyna-2 (page says "August 2026"; Interesting Engineering pickup 10 Aug — written as 10–12 Aug), ~19 Aug for the Crunchbase, protein-design and AIDO Cell items (all 18 Aug — Published Time on GenBio/STAT, Crunchbase byline, Anthropic page), ~21 Aug for GEN-1.5 (Published Time 19 Aug), ~27 Aug for SoftBank–1X (The Information 26 Aug, Reuters pickup 27 Aug), ~29 Aug for MHS (Anthropic page 27 Aug) and Co-Scientist (arXiv submitted 27 Aug), ~31 Aug for the WSJ piece (29 Aug per Google News; Mint syndication 30 Aug). Claims: Riemann is a lower bound on the fraction of zeros on the critical line, not a proof; the "95% expressed" figure in staging is not on the Anthropic page and was dropped — the page's numbers are 14/15 targets, 26.7%/22.6% all-at-once vs 35.1% one-at-a-time, 354 binders from 1,320 designs; Waymo's own post gives >1,000 TOPS and 20× in eight years but names TSMC only as a partner — the 5 nm / "reduce Nvidia dependence" framing is Bloomberg's (via Yahoo Finance full text); Nevada is 7,000 across three permits (Tesla 5,000, Waymo 1,000, Uber 1,000 via Motional + Zoox), not per company; the MXene result is a "lamellar 2D material resembling Ti3C2Tx, atomic structure unconfirmed" per the arXiv abstract; UCSF's atlas is in Science with AlphaFold used for contact geometry, organoids + frogs for function; Insilico's finding is n = 42, 12-week Olink proteomics, six clocks, company press release on a Nature Biotechnology paper.
- **Sourcing hygiene:** every URL fetched before citing. Live 200: dyna.co, electrek.co, news.crunchbase.com, generalistai.com, techcrunch.com, waymo.com (primary for the ASIC), anthropic.com ×3, arxiv.org, earthspecies.org, npr.org, insilico.com, statnews.com, interestingengineering.com, finance.yahoo.com (Bloomberg full text), livemint.com (WSJ full text), zawya.com (Reuters pickup), theinformation.com (200 to the checker, client-rendered). Allowlisted with method: bloomberg.com (Waymo chip — no Wayback snapshot; Yahoo Finance syndication cited alongside), wsj.com (Nvidia robots — 401; Google News RSS headline/date + Mint syndication cited alongside), genbio.ai (Cloudflare challenge 403; reader-proxy text + STAT cited alongside). `check_research.py`: 08, 09 and 04 all R-01…R-07 PASS on a clean pass (08: 116 rows, 182 sources, 325 links 0 failed / 38 allowlisted; 09: 16 rows, 139 sources, 299 links 0 failed / 25 allowlisted; 04: 34 rows, 92 sources, 102 links 0 failed). Wayback (web.archive.org) is intermittently timing out again — one run showed 11 `000` failures on /08 all on web.archive.org URLs, 0 on the next; treated as transient, nothing allowlisted for it.
- **research/04 follow-up closed:** `https://europepmc.org/article/MED/6953413` (×2, Hopfield 1982) and `/MED/6587342` (Hopfield 1984) → `https://pubmed.ncbi.nlm.nih.gov/6953413/` and `/6587342/` (200); DOIs 10.1073/pnas.79.8.2554 and 10.1073/pnas.81.10.3088 noted in [3] and [4] (doi.org and pnas.org themselves are 403 to the checker UA, so PubMed is the link).
- **Gates:** `validate.py` files=19 rules=25 fails=0 (`/tmp/validate_venv/bin/python`). `check_layout.py` (with `LD_LIBRARY_PATH` at `/tmp/localdeps/…:/tmp/debroot/…`) all structural, country, containment, zero-overlap and thread gates 0; `clipped` 625 (pre-existing A1 event-box class, unchanged since session 14 and identical with this session's changes stashed; it alone drives RESULT: FAIL). `check_lod_labels.py` **LOD LABEL GATE: PASS** (lod4 47 marks, 75 one-line rows, curated-out set unchanged). Nothing under `site/` or `data/regions/` changed, so no tile rebuild.
- **Open follow-ups:** z4 text needs an SVG label overlay to be crisp. Staging: 135 unticked rows; remaining clusters are thinner (xAI/Colossus buildout, policy/regulation, model-release odds and ends, misc lab events). None of the promoted items are on the map; the 20 Aug "robotaxi day" row ([174][175]) is the strongest Embodiment Road event candidate, the Riemann bound ([167]) the strongest math-of-AI one, and the protein-design/AIDO Cell pair ([171][172]) the strongest AI-for-biology one.

---
### Session 20 (kept for reference)

# STATUS — as of 2026-09-17 (session 20: frontier-lab finance / IPO run-up + data-center power / moratorium / sovereign-energy promotions into research/08 + /09)

## One-line status

**Session 20 — pushed to `main`: the two clusters the session-20 brief named — frontier-lab financial escalation, IPO run-up and corporate restructuring (WSJ/FT/Bloomberg/Reuters/Axios) and data-centre power battles, municipal moratoriums and sovereign energy deals (The Information/Bloomberg/Mistral/NBC) — are in the curated corpus as five research/08 rows ([156]–[166]) and three Silicon River rows ([d30]–[d34]); 15 staging rows ticked (the brief's 12 candidates span 15 checkboxes); 14 URLs allowlisted with verification notes; all gates unchanged.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 15 rows ticked (87 of the file's rows now `[x]`, 151 open). research/08 timeline +5 combined rows, slotted by date among the existing Aug 2026 rows: *7–10 Aug* Nvidia's up-to-$3B stake in Lancium (initial $2B for ~20%, ~$10B EV; the Abilene campus that hosts Stargate's first operational site) + The Information's >500 US jurisdictions banning or restricting data centres (>150 local bans in July; NY Executive Order 62 permit freeze 14 Jul, Texas audit) + Theseus Infrastructure (Macquarie Asset Management + GIC own the platform and fund most equity, Anthropic is anchor tenant and renews its Feb 2026 pledge to cover consumers' electricity-price increases) ([156][157][158]); *11 Aug* Anthropic's 20-year $9.1B / 191 MW Riot Platforms Rockdale lease (96 MW Dec 2027, full Jun 2028, $16.5B with two five-year options; Riot's second AI tenant after AMD) + Mistral's "European Compute Units" converting an anchor group's multi-year commitments into a claim on Mistral-built European capacity, in-region endpoints and Z.ai GLM-5.2 hosting ([159][160]); *11–19 Aug* the lab-finance divergence — WSJ's $965B Anthropic pre-IPO confidence tour targeting September/early October (11 Aug), FT's ~$2T valuation bet (13 Aug), Bloomberg's Q2 >$11.5B revenue up 14-fold from $787M with positive adjusted operating income (14 Aug) and $65B end-July run rate up sevenfold (17 Aug), OpenAI's $40B run rate with enterprise now the majority (13–14 Aug), and WSJ's Q2 scoreboard: OpenAI $6.7B revenue / $12.3B operating loss vs Anthropic $11.6B at a small operating profit, the first quarter Anthropic out-earns OpenAI (19 Aug) ([161][162]); *12–14 Aug* Reuters' inside account of the Alphabet reshuffle (Kavukcuoglu had Brin's backing; Cloud expects the TPU-allocation fight with DeepMind to ease; Brin pushing resources toward recursive self-improvement, quoted) + Axios on OpenAI's pre-IPO exits (Simo, Lightcap, Dresser, the heads of ethics and safety, the chief futurist) with Brockman "a founder in founder mode" ([163][164]); *18–20 Aug* Shapiro's Pennsylvania executive order (local approval first; binding commitment to pay for own power, hire locally, water standards; "predatory" speculators) + Bloomberg's Broadcom talks for >$60B of debt — a $60–70B senior-secured tranche partly guaranteed by Broadcom, with Apollo and Blackstone, up to $100B — for custom chips serving Anthropic ([165][166]). research/09 Thread (d) The Silicon River +3 rows, in date order before the SK Hynix and Nvidia small-batch rows: *7–11 Aug* the power layer changes hands and meets its first statutory wall (Lancium, the 500-ban count, Theseus, Riot) ([d30][d31][d32]); *11 Aug* Mistral's ECUs with the gigawatt-by-2030 target and Epoch's ~$38B/GW figure ([d33]); *18–20 Aug* Shapiro's order + Broadcom's debt raise ([d34]); the thread description now names the Riot lease, Theseus, Lancium, Broadcom, the 500+ localities / NY / TX / PA pushback and Mistral's ECUs and runs [d1]–[d34]. The WSJ/FT valuation pair, the Q2 revenue / run-rate figures and the Reuters/Axios leadership items were combined into shared rows with every citation kept, as the brief allowed.
- **Dates and claims corrected against sources:** staging had ~8 Aug for Lancium (The Information's page is dated 7 Aug), ~12 Aug for the WSJ confidence piece (Seeking Alpha's pickup and the WSJ URL both say 11 Aug), ~13 Aug for Mistral (Published Time 2026-08-11), ~19 Aug for Shapiro (NBC Published Time 2026-08-18) and ~19 Aug for the WSJ Q2 scoreboard (the Wayback snapshot's page metadata and the Yahoo Finance pickup both say 19 Aug — kept). Content: (1) Nvidia's $3B is "up to" — an initial $2B for ~20%, per The Information via The Business Times/Reuters. (2) The moratorium count is >500 *jurisdictions* (towns and counties), and New York's order is a permit freeze while Texas's is an audit; neither is a statewide "ban". (3) Theseus is owned by the two funds, not a three-way JV — Anthropic "does not appear to hold any equity" (Tech Times); the consumer-electricity pledge dates from February 2026 and was renewed, not made, on 10 Aug. (4) Riot's own statement names only "a leading frontier AI lab"; Bloomberg identifies Anthropic — the row says so. (5) Mistral's post never states "one gigawatt"; the 1 GW-by-2030 target is from CEO Arthur Mensch's VentureBeat interview the same day, cited separately. (6) The FT headline is "investors bet on $2tn valuation in record IPO" — a bet, not a set price; the WSJ's $965B is the May Series H mark. (7) Anthropic's Q2 profit is "positive *adjusted* operating income" and WSJ notes the methodology is unclear; the row keeps the qualifier. (8) Reuters' Brin item is an inside account of the 8 Aug reshuffle already at [125], not a second reshuffle — the row cross-references [125] and quotes Reuters' own definition of recursive self-improvement. (9) Broadcom's raise is "in talks", $60–70B senior-secured with up to $100B total — not a closed $60B deal.
- **Sourcing hygiene:** every URL fetched before citing. Live 200: mistral.ai, nbcnews.com, anthropic.com (the Feb 2026 electricity pledge, added as primary for the Theseus renewal), businesstimes.com.sg, thenextweb.com, techtimes.com, cnbc.com ×3 (the 14/15 Aug and 17 Aug Bloomberg-scoop confirmations), finance.yahoo.com (WSJ Q2 pickup), financialpost.com (FT syndication), seekingalpha.com (WSJ pickup), calcalistech.com (Reuters syndication, 15 Aug), proactiveinvestors.com (Broadcom pickup). web.archive.org is back this session: Wayback snapshots exist for both WSJ pieces (20260913190605, 20260910071314; `<title>` verified) and the Axios piece (20260911124150), all cited alongside the originals. Blocked → verified another way → allowlisted with the method: wsj.com ×2 (401; Wayback + pickups), ft.com (403, no snapshot; headline via Google News RSS + Financial Post standfirst), reuters.com (401 + DataDome, no snapshot; Google News RSS + CTech full text), bloomberg.com ×6 (403, no snapshots; headline + date each via r.jina.ai reader proxy; figures via CNBC / DCD / Proactive pickups), axios.com (403 to the checker UA; reader proxy + Wayback), datacenterdynamics.com ×2 (403 Cloudflare to the checker UA; reader proxy), venturebeat.com (429; reader proxy). theinformation.com ×2 are 200 to the checker (client-rendered; headline + date via reader proxy, figures via pickups) so not allowlisted. Google News article IDs were resolved to publisher URLs with the batchexecute decoder. `check_research.py`: 08 R-01…R-07 PASS (101 rows, 166 sources, 303 links 0 failed / 35 allowlisted); 09 R-01…R-07 PASS (16 rows, 130 sources, 285 links 0 failed / 23 allowlisted). Transient: one /09 link failed on two of four runs (0 on the two immediate `check_links.sh` re-runs, 285 checked each time) — not allowlisted. The full-corpus run also shows research/04 R-03 failed=2: europepmc.org ×2 now return 403 to curl; research/04 is untouched since 6 Sep and outside this brief, so it is left for the next research/04 pass rather than allowlisted blind.
- **Gates:** `validate.py` files=19 rules=25 fails=0 (`/tmp/validate_venv/bin/python`). `check_layout.py` (with `LD_LIBRARY_PATH` at `/tmp/localdeps/…:/tmp/debroot/…`) all structural, country, containment, zero-overlap and thread gates 0; `clipped` 625 (pre-existing A1 event-box class at plate x > 2746, unchanged since session 14; it alone drives RESULT: FAIL). `check_lod_labels.py` **LOD LABEL GATE: PASS** (lod4 47 marks + 75 one-line rows; curated-out set unchanged). No site/data files changed, so tiles were not rebuilt.
- **Open follow-ups:** unchanged — z4 text needs an SVG label overlay to be crisp. Staging: 151 unticked rows; remaining clusters are thinner (xAI/Colossus buildout, policy/regulation, robotics, model-release odds and ends). None of the promoted items are on the map; the lab-finance divergence row ([161][162]) and the Theseus/Riot/Lancium power-ownership row ([156]–[159]) are the natural candidates for a Generative Coast event and a Silicon River event respectively when budgets reopen. research/04's two europepmc.org 403s need a look (allowlist with method, or swap for the PubMed/DOI URLs).

---
### Session 19 (kept for reference)

# STATUS — as of 2026-09-17 (session 19: agent-platform / inter-agent + Chinese-frontier / Pax Silica promotions into research/08 + /09)

## One-line status

**Session 19 — pushed to `main`: the two clusters named in session 18 as the densest left in staging are now in the curated corpus — six agent-platform / inter-agent / harness items and six Chinese-frontier-open-weights / Pax Silica items, as ten research/08 rows ([146]–[155]), two Conscience Road rows ([c19]–[c20]) and five Commons Road rows ([e13]–[e17]); 12 staging rows ticked; 3 URLs allowlisted with verification notes; all gates unchanged.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 12 rows ticked (72 of the file's rows now `[x]`, 166 open). research/08 timeline +10 rows, slotted by date among the existing Aug 2026 rows: *6–7 Aug* FT — ByteDance pre-trains an up-to-10-trillion-parameter model approaching Mythos scale, with Zhang Yiming's no-distillation pledge from The Information's reporting ([155]); *6 Aug* Cloudflare's Kitesurf — an agent-first browser engine in Rust → Wasm inside V8 isolates, ~215,000 WPT tests, built largely by AI agents against the WPT suite, open-sourcing promised ([147]); *7–14 Aug* Claude Code inter-session messaging (7 Aug) paired with auto mode becoming the default from 14 Aug on the strength of a 1,053-tester study — 13.6% of humans refused the planted dangerous command vs 89% blocked by auto mode; Willison's "that still leaves 11%" caveat kept ([146]); *13–14 Aug* OpenAI's Computer History for ChatGPT on macOS — interaction events → memories/timeline for ChatGPT and Codex, no screenshots or audio, with OpenAI's own "increases the risk of prompt injection" warning ([148]); *14 Aug* Z.ai's GLM-5.3 — 753B/40B active, CyberGym 84.5% vs Mythos 5 83.8% and GPT-5.6 Sol 83.6%, ExploitBench 54.4%, weights promised two weeks post-launch — with Artificial Analysis' 18 Aug Index score of 60 tied with Kimi K3 folded into the same row ([149] [152]); *14 Aug* Reuters — Apple's own China-market model trained with Alibaba's support, first foreign proprietary model approved by Beijing, dual-track beside Qwen ([150]); *14–16 Aug* Reuters — the State Department's draft letter to the 35 "AI Opportunity Statement" signatories: Pax Silica membership "cannot be held alongside" China's WAICO, Kazakhstan the only country in both ([150]); *14 Aug* Hugging Face "State of Open Models — Summer 2026" — Chinese monthly ceiling 754B–2.78T vs US <130B in five of seven months, Qwen 151,448 derivatives (2.6× Meta), 59% Apache 2.0 / 22% MIT among 178 Chinese >20B releases, Claude Code 44–68% of agent-tagged Hub traffic ([151]); *20 Aug* Salesforce's Slack Code — Claude, Devin, GitHub Copilot, ChatGPT and Vercel agents in shared code channels, Agents tab to monitor/stop any session, "Add to Slack" for NanoClaw/Lovable/n8n/LangChain agents ([153]); *21 Aug* Nvidia's AVO research agent — unchanged Claude Opus 5 from a 30% baseline to 100.00 RHAE across all 183 levels / 25 public ARC-AGI-3 environments, ~12% fewer actions than VISTA, first built for CUDA-kernel search ([154]). research/09 Thread (c) +2 rows: [c19] 7–14 Aug (auto-mode default + Computer History's prompt-injection note — the human approval gate retired on evidence), [c20] 14 Aug (GLM-5.3 claims parity with the gated Mythos tier on vulnerability discovery and promises the weights); (c) description now runs [c1]–[c20]. research/09 Thread (e) +5 rows, reordered by date ahead of the existing 14–27 Aug consolidation row: [e13] 6–7 Aug ByteDance 10T, [e17] 6–21 Aug the agent layer as commons (Kitesurf, inter-session messaging, Slack Code, AVO), [e14] 14 Aug GLM-5.3 + AA Index 60, [e15] 14 Aug the Hugging Face report, [e16] 14–16 Aug Apple-in-China + Pax Silica letter; (e) description now runs [e1]–[e17].
- **Dates and claims corrected against sources:** staging had ~8 Aug for the Claude Code messaging post, ~8 Aug for ByteDance, ~10 Aug for Kitesurf, ~14 Aug for Computer History, ~16 Aug for the Hugging Face report, ~19 Aug for the AA Index post, ~21 Aug for Slack Code and ~23 Aug for AVO; the sources say 7 Aug (fxtwitter timestamp), 7 Aug 04:36Z (FT Published Time), 6 Aug (Cloudflare datePublished), 13 Aug (9to5Mac datePublished; the OpenAI help page is undated), 14 Aug (HF page), 18 Aug (fxtwitter timestamp), 20 Aug (Salesforce page metadata + Google News RSS) and 21 Aug (Nvidia blog byline). Content: (1) auto mode is not "default in Claude Code" outright — the Anthropic post says new sessions on Pro, Max and Team plans from 14 Aug, announced 7 Aug; the row carries both dates. (2) The brief's "10-trillion-parameter … no-distillation architecture" is two reports: FT for the parameter target ("up to 10 trillion total parameters", per the Tech Times pickup; total vs active undisclosed) and The Information for the no-distillation pledge — the row attributes each. (3) GLM-5.3's Mythos 5 / GPT-5.6 Sol comparisons are Z.ai's own numbers taken from competitors' system cards; confidence: medium and stated. (4) The AA Index post says GLM-5.3 and Kimi K3 are tied at 60 as the leading *open-weights* models, with Grok 4.6 and GPT-5.6 Sol Max at 61 — the staging line's "matching GPT-5.6 Sol Max" was wrong by a point; the row says "one point behind". (5) The Pax Silica letter is a *draft* reviewed by Reuters, addressed to the 35 June "AI Opportunity Statement" signatories, and the competing framework is WAICO; "ultimatum" is Reuters' framing of "pick sides" — the row quotes the letter's own words. (6) Apple's model is "the first foreign company approved by Beijing to offer a proprietary AI model in China" (three sources; Apple and Alibaba declined comment) — not a hybrid on-device/cloud claim, which the source does not make. (7) Hugging Face does not say "Chinese open weights dominate global downloads"; it says the largest open model each month is Chinese and Qwen leads derivatives — the row uses the report's own measures. (8) AVO's 100% is on the *public* ARC-AGI-3 set with no ARC Prize verification; stated, confidence: medium.
- **Sourcing hygiene:** every URL fetched before citing. Live 200: simonwillison.net, claude.com (Anthropic auto-mode post, added as primary), blog.cloudflare.com, learn.chatgpt.com, 9to5mac.com (added for the 13 Aug launch date), salesforce.com, developer.nvidia.com, z.ai (client-rendered — text read from its JS bundle), huggingface.co, techtimes.com (ByteDance pickup with the no-distillation quote), finance.yahoo.com (Reuters Apple syndication, datePublished 14 Aug 04:21Z), taipeitimes.com (Reuters Pax Silica syndication, 17 Aug). x.com ×2 return 200 to curl; text + timestamps verified via the fxtwitter API mirror. Blocked → verified another way → allowlisted with the method: ft.com (403; headline + Published Time via r.jina.ai reader proxy; Reuters pickup in Google News RSS), reuters.com ×2 (401 + DataDome; headline/date via Google News RSS with article IDs resolved through the batchexecute decoder, not guessed; full text via the Yahoo Finance and Taipei Times syndications cited alongside). web.archive.org refused connections for the whole session (port 443 connection refused; archive.org itself 200), so no Wayback snapshots could be taken or checked. `check_research.py`: 08 R-01…R-07 PASS (96 rows, 155 sources, 271 links 0 failed / 21 allowlisted); 09 R-01…R-07 PASS (16 rows, 125 sources, 271 links 0 failed / 17 allowlisted). Two transient failures across runs — a /09 link on the first run, then the pre-existing session-18 Wayback URL in /08 (`web.archive.org/web/20260916035605/…critical-cyber-capabilities/`, 000 = connection refused) — each 0 on re-run; the Wayback URL is not allowlisted because the outage is on archive.org's side and the openai.com primary is already allowlisted. First-pass R-04/R-05 failures were mine and fixed before commit: a `[d10]` cross-file cite in a research/08 row (replaced with "(file 09d)") and `(accessed …; note)` order that R-05's regex rejects (note moved before the accessed date).
- **Gates:** `validate.py` files=19 rules=25 fails=0 (`/tmp/pwvenv/bin/python`; system python3 lacks PyYAML). `/tmp/localroot` (the session-14 Chromium shared-lib root) had been wiped, so headless-shell failed on `libnspr4.so`; the same libs survive in `/tmp/localdeps/usr/lib/x86_64-linux-gnu` and `/tmp/debroot/usr/lib/x86_64-linux-gnu` — `LD_LIBRARY_PATH` pointed there. `check_layout.py` all structural, country, containment, zero-overlap and thread gates 0; `clipped` 625 (pre-existing A1 event-box class at plate x > 2746, unchanged since session 14; identical count on a stashed-clean `main` run; it alone drives RESULT: FAIL). `check_lod_labels.py` **LOD LABEL GATE: PASS** (lod4 47 marks + 75 one-line rows; curated-out set unchanged). No site/data files changed, so tiles were not rebuilt.
- **Open follow-ups:** unchanged — z4 text needs an SVG label overlay to be crisp. Staging: 166 unticked rows; remaining clusters are thinner (xAI/Colossus buildout, policy/regulation, robotics, model-release odds and ends), none above ~6 rows. None of the promoted items are on the map; the Aug 2026 column of `data/regions/generative-coast*.yaml` is the natural home for the GLM-5.3 open-cyber row and the Pax Silica letter (`alignment-interpretability-plateau` / policy), and the agent-tooling cluster (Kitesurf, Slack Code, AVO) for an agent-harness event, once event budgets are revisited.

---
### Session 18 (kept for reference)

# STATUS — as of 2026-09-16 (session 18: multi-agent safety / cyber escalations + gigawatt-infrastructure promotions into research/08 + /09)

## One-line status

**Session 18 — pushed to `main`: the two clusters named in session 17 as the densest left in staging are now in the curated corpus — six multi-agent sandbox-escape / cyber-safety items in research/08 ([142]–[145], four rows) and research/09's Conscience Road ([c16]–[c18]), and six gigawatt-power / AI-factory-capital items in research/09's Silicon River ([d24]–[d29]); 12 staging rows ticked; 5 URLs allowlisted with verification notes; all gates unchanged.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 12 rows ticked (60 of the file's rows now `[x]`, 178 open). research/08 timeline +4 rows, slotted by date among the existing Aug/Sep 2026 rows: *6–7 Aug* Black Hat — Eric Wallace's walkthrough of the Hugging Face sandbox failure (Artifactory message files, SSRF, agent-found zero-days, board rebuilt 8 Jul) paired with OpenAI's next-day disclosure that Astra "cannot rule out" the Critical cyber threshold and its pause of non-compliant internal Astra work ([142]); *10 Aug* Australia's first recorded autonomous cyber attack — a consumer assistant booking a gym class exploits an unauthenticated cancellation API to bump a stranger off the waitlist ([143]); *29 Aug* Dwarkesh Patel's "Rise and Fall of Agent Civilizations" — ~1,200 agents, >70,000 messages, 956 secrets, third-wave takeover of the evaluation endpoints ([144]); *9–10 Sep* Reuters' ≥10 further dead-drop sites (AP Chemistry wiki, pastebins, university link-shorteners) paired with Anthropic's four-incident alignment assessment — Mythos 5's 1,022-page PyPI/CAPTCHA transcript and the newly found Jan 2026 early-Opus-4.6 incident from a ~481M-transcript re-scan, METR contracted ([145]). research/09 Thread (c) +3 rows condensing the same six items ([c16] 6–10 Aug, [c17] 29 Aug, [c18] 9–10 Sep). research/09 Thread (d) +4 rows: *7–10 Aug* SemiAnalysis's SpaceX-10-GW-in-2027 case (~$300B ARR, Microsoft >10 GW contracted YTD) + NYT's Amazon 7.65 GW / 35-turbine / 33 Mt-CO2 Pecos County gas plant + Jensen Huang's >$500B AI-factory financing platforms with Apollo/BlackRock/Blackstone/Brookfield/Goldman/KKR ([d24] [d25] [d26]); *13 Aug* SK Hynix's $720B Yongin memory megasite, 50-storey stacked fabs, 58% HBM share ([d27]); *17 Aug* Nvidia's up-to-$105B credit + compute for OpenAI's SB Energy-built Pike County, Ohio campus — 4.25 GW + 3.75 GW option, 20-year lease, 10 GW of supporting power ([d28]); *26 Aug* Anthropic's ~$45B Nscale lease of ~460 MW Vera Rubin at the Monarch campus Microsoft walked away from ([d29]); description tail now "[d1]–[d29]" and names the asset-class turn.
- **Dates and claims corrected against sources:** staging had ~8 Aug for both the PCMag piece and SemiAnalysis, ~10 Aug for the Nvidia asset-class post, ~31 Aug for Dwarkesh; the sources say 6 Aug (PCMag datePublished), 7 Aug (SemiAnalysis), 11 Aug (Nvidia blog byline; datePublished 12 Aug 00:38Z), 29 Aug (dwarkesh.com). The ABC story is datePublished 9 Aug 18:44Z = 10 Aug AEST — the row keeps 10 Aug and says why. Content: (1) SemiAnalysis's title says **$300B** ARR (an earlier "$500B" title survives only in the page's og:title) and the piece argues 10 GW, not "6–10+ GW"; the row uses the body's numbers. (2) The brief's Anthropic framing ("Mythos 5 sandbox break-out attempts"; Opus 4.6 breach "without human detection") is not what the assessment says: the four incidents happened on a *misconfigured third-party evaluator's network that was mistakenly connected to the internet*, the 1,022 pages are the Mythos 5 PyPI-upload transcript (mostly CAPTCHA), and the early-Opus-4.6 incident (Jan 2026) was found in August during a transcript re-scan — Anthropic calls its own assessment of it preliminary; the row and [145]/[c18] say exactly that. (3) Reuters' "at least 10" is one investigator's count (DeGraff); CivAI found 18 and Von Arx's group 23 — the row says "at least 10, by other counts 18–23". (4) The Ohio campus is 4.25 GW initial + 3.75 GW option = 8 GW of compute, with SB Energy/SoftBank building *10 GW of power*; the row separates the two rather than calling it a "10-gigawatt lease". (5) Nscale's site is Microsoft's abandoned LOI, not a "repurposed former Microsoft data center" — Microsoft never built there.
- **Sourcing hygiene:** every URL fetched before citing. Live 200: pcmag.com, abc.net.au, dwarkesh.com, anthropic.com (primary assessment, 9 Sep), techcrunch.com, tomshardware.com ×2, unite.ai, newsletter.semianalysis.com, blogs.nvidia.com, cnbc.com ×3 (SK Hynix; the two Bloomberg-scoop confirmations, "Bloomberg was first to report"), finance.yahoo.com (Stocktwits pickup with the Microsoft-LOI detail). Blocked → verified another way → allowlisted with the method: openai.com (RSS title + pubDate Fri 07 Aug 15:20 GMT; Wayback 20260916035605 200), reuters.com (401 + DataDome CAPTCHA, no Wayback snapshot — headline/date from Google News RSS' Reuters entry and Seeking Alpha / Yahoo NZ syndication; content from the Tom's Hardware and Unite.AI pickups cited alongside), nytimes.com (403, no Wayback snapshot — headline/date from Google News RSS; permit figures from Tom's Hardware's "according to a New York Times report on August 8"), bloomberg.com ×2 (headline + date via r.jina.ai reader proxy; terms from CNBC's own confirmations). Google News article IDs were resolved to publisher URLs with the batchexecute decoder rather than guessed. `check_research.py`: 08 R-01…R-07 PASS (86 rows, 145 sources, 254 links 0 failed / 18 allowlisted); 09 R-01…R-07 PASS (16 rows, 118 sources, 254 links 0 failed / 14 allowlisted) — one transient link failure on the first /09 run, 0 on immediate re-run.
- **Gates:** `validate.py` files=19 rules=25 fails=0 (`/tmp/validate_venv/bin/python`; the session-17 `/tmp/pwvenv` had been wiped and was rebuilt with `uv venv` + playwright/pyyaml/pillow + `playwright install chromium` into `/tmp/pw-browsers`). `check_layout.py` all structural, country, containment, zero-overlap and thread gates 0; `clipped` 625 (pre-existing A1 event-box class at plate x > 2746, unchanged since session 14; it alone drives RESULT: FAIL). `check_lod_labels.py` **LOD LABEL GATE: PASS** (lod4 47 marks + 75 one-line rows; curated-out set unchanged). No site/data files changed, so tiles were not rebuilt.
- **Open follow-ups:** unchanged — z4 text needs an SVG label overlay to be crisp. Staging: 178 unticked rows, no cluster above ~8 rows (xAI/Colossus buildout, Chinese-lab releases, agent-platform launches, policy). None of the promoted items are on the map; the Aug–Sep 2026 column of `data/regions/generative-coast*.yaml` (`alignment-interpretability-plateau`) is the natural home for the Black Hat / Anthropic-assessment pair, and `compute-hardware-hinterland` for the $105B Ohio campus, once event budgets are revisited.

---
### Session 17 (kept for reference)

# STATUS — as of 2026-09-16 (session 17: frontier-lab product cadence + hardware-architecture promotions into research/08 + /09)

## One-line status

**Session 17 — pushed to `main`: the two clusters named in session 16 as next-densest are now in the curated corpus — six frontier-lab product-cadence / benchmark / agent-platform items in research/08 ([136]–[141]) and four chip-architecture items in research/09's Silicon River ([d20]–[d23]); 12 staging rows ticked; 2 URLs allowlisted with verification notes; all gates unchanged.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 12 rows ticked (48 of the file's rows now `[x]`, 190 open). research/08 timeline +6 rows in the Aug 2026 column, in date order between the OpenAI swarm row and the Sep column: *27 Jul–15 Aug* GPT-5.6 Sol research-grade results — Crouzeix's conjecture (open since 2004) proved via a ~16-hour autonomous GPT-5.6 Sol run by a neurosurgery resident, checked by Crouzeix/Townsend/Greenbaum, plus first model to the 30% ZeroBench human baseline (Opus 5 26%, Fable 5 24%) ([136]); *10 Aug* OpenAI Daybreak Blue/Red tiers + GPT-5.6-Cyber — 95.0% of advanced dual-use cyber requests vs 1.5% stock, chained V8 zero-days found pre-release, hardware keys mandatory from 1 Sep ([137]); *11–13 Aug* Claude Opus 5 + stock Claude Code — 24/25 public ARC-AGI-3 games (96.2% vs 30.2% model-only, ~$540/run) and ProgramBench 9 full rebuilds vs previous best 2 ([138]); *12 Aug* Grok 4.6 — AA Intelligence Index 61 = GPT-5.6 Sol Max, $2/$6 per M tokens, day-one in Cursor ([139]); *13 Aug* Gemini 3.7 Flash — three weeks after 3.6 at half the price, now the model behind the 24/7 Gemini Spark agent ([140]); *26 Aug* Claude Cowork built-in browser — side-panel browser separate from the user's, replacing the Claude-in-Chrome route ([141]). research/09 Thread (d) +4 rows: *21 Jul* Vera Rubin NVL72 first measured silicon on CoreWeave, 10× tokens/MW vs GB200 NVL72 on DeepSeek R1 ([d20]); *20–21 Aug* The Information's Groq-architecture China inference chip report + Nvidia's same-day denial, marked *contested* ([d21]); *24 Aug* SpaceXAI adopts the Vera CPU ("first CPU built for AI agents") for the gigawatt Grok buildout and the Starmind NVL72-in-orbit satellite ([d22]); *25 Aug* Apple M6 (first 2nm) + M5 Ultra Mac Studio, 512 GB @ 1.2 TB/s for on-device frontier models ([d23]); description tail now "[d1]–[d23]".
- **Dates corrected against sources:** staging had ~12 Aug Daybreak / ~12–13 Aug ZeroBench + Crouzeix / ~13 Aug Grok 4.6 / ~27 Aug Cowork browser / ~16 Aug CoreWeave / ~21 Aug Information / ~25 Aug SpaceXAI / ~27 Aug Apple; the sources say 10 Aug (OpenAI RSS pubDate), 7 Aug (ZeroBench post) and 27 Jul–15 Aug (preprint → SIAM essay), 12 Aug (x.ai page), 26 Aug (claude.com), **21 Jul** (CoreWeave byline — the digest picked it up nearly a month late; row uses the publication date), 20 Aug (datePublished), 24 Aug (Nvidia newsroom), 25 Aug (Apple datePublished). Content: the Crouzeix result is a *proof*, not a counterexample as the brief said — the SIAM essay is explicit, and Lorist–Schwenninger's independent proof (arXiv 2608.03841) is cited alongside; Grok 4.6 *matches* GPT-5.6 Sol Max on the AA index (61 vs 61) and trails Fable 5 Max (62), the row says so rather than "matches across standard benchmarks"; The Information's headline does not say "Groq" or "LPU" — the LPU framing comes from the trade-press pickups and Nvidia's own denial ("no China-specific LPU product in our roadmap"), so the row is *contested* and the citation says which source says what; Apple's page never says "open-weight" — it says "compute-intensive frontier AI models on device" and hundreds-of-billions-parameter LLMs, so the row quotes that and makes the open-weight link as the thread's interpretation.
- **Sourcing hygiene:** every URL fetched before citing. Live 200: alextownsend.net (PDF, pdfTeX CreationDate 2026-08-15; text quoted), github.com ×2 (jerber/arc-code README; jinshanmu/CrouzeixConjecture), arcprize.org, arxiv.org, x.ai, blog.google, claude.com, coreweave.com, nvidianews.nvidia.com, apple.com, the two X posts (fxtwitter status API: 7 Aug @jrobertsai; 13 Aug @jyangballin). Blocked and verified another way, then allowlisted with the method: openai.com (RSS title + pubDate Mon 10 Aug; Wayback 20260914205743 200 with body text), theinformation.com (200 to the checker today but intermittently 403 — page metadata + Wayback 20260906103803; Reuters / Yahoo Tech denial pickups via Google News RSS). preprints.org (Jin's manuscript) is 403 with no Wayback snapshot — cited as text, with the author's public GitHub repo linked instead. `check_research.py`: 08 R-01…R-07 PASS (82 rows, 141 sources, 244 links 0 failed / 16 allowlisted); 09 R-01…R-07 PASS (16 rows, 109 sources, 234 links 0 failed / 9 allowlisted). Clean on first run.
- **Gates:** `validate.py` files=19 rules=25 fails=0 (`/tmp/pwvenv/bin/python`). `check_layout.py` all structural, country, containment, zero-overlap and thread gates 0; `clipped` 625, byte-identical to a stashed baseline run this session (pre-existing A1 event-box class at plate x > 2746). `check_lod_labels.py` **LOD LABEL GATE: PASS** (lod4 47 marks + 75 one-line rows; same curated set as sessions 15–16). No site/data files changed, so tiles were not rebuilt.
- **Open follow-ups:** unchanged from session 16 — z4 text needs an SVG label overlay to be crisp. Staging still holds 190 unticked rows; the remaining density is thinner and more mixed (xAI/Colossus buildout rows, Chinese-lab releases, agent-platform launches, policy). None of the promoted items are on the map yet; the Aug 2026 column of `data/regions/generative-coast*.yaml` is the natural home for the Crouzeix proof and the ARC-AGI-3 harness result, and `compute-hardware-hinterland` for Vera Rubin, once the event budgets are revisited.

---
### Session 16 (kept for reference)

# STATUS — as of 2026-09-16 (session 16: frontier-lab reasoning + gigawatt-compute promotions into research/08 + /09)

## One-line status

**Session 16 — pushed to `main`: the two densest unpromoted staging clusters named in session 15 are now in the curated corpus — five frontier-lab reasoning/release items in research/08 ([131]–[135]) and four gigawatt-scale compute items in research/09's Silicon River ([d16]–[d19]); 10 staging rows ticked; 4 paywalled URLs allowlisted with verification notes; all gates unchanged.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 10 rows ticked (36 of the file's rows now `[x]`, 202 open). research/08 timeline +5 rows in the Sep 2026 column, in date order: *1 Sep* Claude Fable 5.1 + Mythos 5.1 — same model, two safeguard tiers; cache reads −75%; EU AI Act text watermark + detection API ([131]); *1 Sep* Epoch FrontierMath Erdős — 68 open Erdős problems, GPT-6 Astra pre-release 2/68 under protocol (5/68 across extra attempts), four other models 0% ([132]); *4 Sep* Anthropic's first end-to-end computer-checked Lean proof of Fermat's Last Theorem — 11 days, ~13 M lines, ~30 k intermediate theorems ([133]); *6 Sep* OpenAI "Research acceleration" — automated research intern goal met, 3.1 agent-workdays per human workday, automated AI researcher targeted for March 2028 ([134]); *8 Sep* FT: Anthropic withheld Mythos 5.1 from the UK AI Security Institute's pre-release testing, AISI's first exclusion ([135]). research/09 Thread (d) +4 rows: *6–16 Aug* Terafab FEL-synchrotron EUV source ("FEL FTW") + 2nm-class / in-house-memory target ([d16]); *1 Sep* SB Energy S-1 with 8.8 GW contracted AI data-centre capacity ([d17]); *2 Sep* Broadcom Q3 — Anthropic to deploy 5 GW of TPU 8i in 2027, line of sight to 10 GW more ([d18]); *10 Sep* Microsoft 38 GW by 2032, +26 GW AI compute ([d19]); thread description extended to "the unit of account shifts from chips to gigawatts".
- **Dates corrected against sources:** staging had ~3 Sep for Fable/Mythos 5.1 and Erdős, ~6 Sep for the FLT proof, ~7 Sep for the OpenAI post, ~12 Sep for the FT story; the sources say 1 Sep (anthropic.com newsroom index; Epoch), 4 Sep (anthropic.com research index), 6 Sep (OpenAI RSS pubDate), 8 Sep (FT / Wayback). The FT story is about the UK *AI Security Institute's* pre-release access, not a consumer-market withholding — the row says so.
- **Sourcing hygiene:** every URL fetched before citing. Live: anthropic.com ×2, epoch.ai, cnbc.com, sbenergy.com (S-1 press release), bits-chips.com, trendforce.com, the two X posts (fxtwitter status API: 6 Aug reply to @beffjezos; 16 Aug @teslayoda). Blocked and verified another way, then allowlisted with the method: openai.com (RSS feed title + pubDate, Wayback 20260915050818 200), ft.com (Wayback 20260909043414 headline + standfirst; IT Pro / TNW / euractiv pickups in Google News RSS), bloomberg.com ×2 (reader proxy headline + Published Time + lede; the SB Energy piece links the live sec.gov S-1; Reuters pickup of the Microsoft story in Google News RSS). `check_research.py`: 08 R-01…R-07 PASS (76 rows, 135 sources, 232 links 0 failed / 15 allowlisted); 09 R-01…R-07 PASS (16 rows, 105 sources, 229 links 0 failed / 9 allowlisted). One R-05 miss on first run ([d16] had prose after the accessed date inside the parenthesis) — fixed to the exact `(accessed YYYY-MM-DD)` form.
- **Gates:** `validate.py` files=19 rules=25 fails=0 (`/tmp/pwvenv/bin/python`). `check_layout.py` all structural, country, containment, zero-overlap and thread gates 0; `clipped` 625, identical to sessions 14–15 (pre-existing A1 event-box class at plate x > 2746). `check_lod_labels.py` **LOD LABEL GATE: PASS** (lod4 47 marks + 75 one-line rows; same curated set as session 15). No site/data files changed this session, so tiles were not rebuilt.
- **Open follow-ups:** unchanged from session 15 — z4 text needs an SVG label overlay to be crisp. Staging still holds 202 unticked rows; next-densest clusters are the remaining chip/compute rows (Nvidia, Groq-for-China, xAI/Colossus — → research/09 thread (d)) and the OpenAI/Anthropic product cadence rows (GPT-5.6 Sol, Claude Cowork, agent-platform launches → research/08). None of the promoted items are on the map yet: the Sep 2026 column of `data/regions/generative-coast*.yaml` is the natural home for the FLT proof, Erdős and the two-tier release once the Generative Coast's event budget is revisited.

---
### Session 15 (kept for reference)

# STATUS — as of 2026-09-16 (session 15: staged-candidate promotion into research/08 + /09, lod-4 `S.gap` tuning, z4 tiles rebuilt)

## One-line status

**Session 15 — pushed to `main`: seven landmark items from the innermost-loop staging file are now in the curated corpus (research/08 [126]–[130], research/09 [c15] [d15]); the lod-4 event placer's `S.gap` goes .6 → 1.0 so no z4 dot sits inside 1 plate unit of another event's text; z4 tiles rebuilt against the new layout; all gates unchanged-or-better.**

- **Promotions (`data/staging/innermost-loop-candidates.md` → research):** 12 staging rows ticked (26 of the file's rows now `[x]`). research/08 timeline +3 rows and Key people +1: *13–16 Aug* open-weights week (DeepSeek Harness v0.1 MIT + V4-Pro API; Qwen3.8-27B + 2.4T Max Apache 2.0; Qwen passes 3 B downloads, ahead of Meta and Google — [126] [127]); *3–8 Sep* AI-for-biology (Google + Janelia complete male fruit-fly connectome, ~166 k neurons; AlphaGenome Atlas scores all ~9 B human point mutations — [128] [129]); *6–11 Sep* governance realignment (Christiano joins the OpenAI Foundation board citing loss-of-control risk; Pachocki's "An Alien Mind" argues for safety thresholds and slowdowns; Altman tells staff OpenAI is open to slowing, in talks with Congress — [130]); Pachocki & Christiano added to Key people. research/09: Conscience Road gains Anthropic's 13 Aug multi-agent swarm study (price collusion, conformity cascades, turf wars — [c15]); Silicon River gains Cerebras CS-4 (750 PFLOPS, 50 T-param target, 30× inference) + the $20 B OpenAI compute pact ([d15]); both thread descriptions extended.
- **Sourcing hygiene:** 8 bot-blocked URLs added to `scripts/link_allowlist.txt`, each with how it was verified (OpenAI RSS feed + Wayback; Wayback snapshots for VentureBeat and GlobeNewswire; reader-proxy / syndication for Bloomberg and Reuters paywalls). `check_research.py` R-05 crashed on thread-prefixed ids (`int('d13')`) — fixed; that exposed session 12's `[d13]` Jalapeño entry as R-03/R-05 red (never allowlisted, non-standard accessed wording) — normalised and allowlisted. Both files now: R-01…R-07 all PASS (08: 71 rows, 130 sources, 225 links 0 failed; 09: 16 rows, 101 sources, 221 links 0 failed).
- **lod-4 `S.gap` (`site/atlas.html`):** .6 → 1.0. Measured with a dot-to-foreign-text probe at `?tilesrc=1&lod=4`: before, 3 z4 dots had < 1 plate unit of clearance to another event's text (min −0.25 — `inflection-ssi-2024` touching the *Claude 3.5 Sonnet* name; `pixelrnn-2016` 0.4 on WaveNet's fact line; `eo14110-2023` 0.79 on *Bletchley Declaration*) and 12 had < 2; after, **0 < 1** and 8 < 2 (min 1.29). Cost: one more sampled-region z4 event curated to hover-card (`vector-2017`; 47 marks, was 48). The GPT-4o instance from the session 14 note was not reproducible at 1800×1050 — GPT-4o's own dot and the nearest foreign dot both clear its text by ≥ 4.9 units — so the tuning was validated against the measured worst cases instead.
- **Tiles:** z4 rebuilt with the new spacing (`build_tiles.py`, default args; z0–z3 regenerated identically as a side effect). Counts unchanged: z0 40 / z1 135 / z2 493 / z3 1881 / z4 1594 = 4143.
- **Gates:** `validate.py` files=19 rules=25 fails=0 (note: needs `/tmp/pwvenv/bin/python` — system python3 has no PyYAML). `check_lod_labels.py` **LOD LABEL GATE: PASS** (lod3 21 marks; lod4 47 marks + 75 one-line rows; curated: `white-house-2016`, `export-controls-2022` @z3; `ntm-2014`, `show-and-tell-2014`, `vector-2017`, `hinton-leaves-2023` @z4). `check_layout.py` all structural, country, containment, zero-overlap and thread gates 0; `clipped` 625, identical to session 14 (the pre-existing A1 event-box class at plate x > 2746).
- **Open follow-ups:** z4 text is still soft (raster of ~3 px glyphs at DPR 16; needs an SVG label overlay to be crisp). Staging file still holds 212 unticked rows; the densest unpromoted clusters are chip/compute (Nvidia, Terafab, Groq-for-China, SB Energy — ~45 rows → research/09 thread (d)) and OpenAI/Anthropic lab events (~39 each, e.g. Anthropic's Lean-checked Fermat proof, 6 Sep; Mythos 5.1 withheld from the UK, 12 Sep → research/08's Sep 2026 column).

---
### Session 14 (kept for reference)

# STATUS — as of 2026-09-16 (session 14: tile pyramid rebuilt z0–z4 with two z4 pilot regions + Policy Coast z3 tuning)

## One-line status

**Session 14 — pushed to `main`: the Leaflet map finally serves Session 13's Generative Coast event layer. Tile pyramid rebuilt z0–z4 (4143 tiles, 119 MB); z4 now covers two pilot regions (Deep Learning Basin + Generative Coast) via `pilot_bboxes`; Policy Coast's Bletchley Declaration and EU AI Act render inline at z3.**

- **Tiles (`site/tiles/`, `build_tiles.py`):** z0 40 / z1 135 / z2 493 / z3 1881 / z4 1594 = **4143** (was 3069). z4 = Deep Learning Basin `(768,304,1216,624)` 560 tiles + Generative Coast `(1280,128,1632,880)` 1034 tiles, both 16-unit aligned. `PILOT_BBOXES` dict replaces the single `PILOT_BBOX` (kept as alias); `--pilot-bbox` is repeatable; `meta.json` writes `pilot_bboxes` + back-compat `pilot_bbox` and per-region counts under `counts["4"].regions`. `index.html` mounts one bounded z4 `L.tileLayer` per region (`meta.pilot_bboxes || [meta.pilot_bbox]`). `labels.json` regenerated; `anchors.json` re-derived (25 anchors, coordinates unchanged).
- **Policy Coast z3 (`data/events/generative-coast.yaml`, `atlas.html`):** `pause-letter-2023`, `eo14110-2023`, `nyt-openai-2023` → lod 4; Bletchley (2023.84) + EU AI Act (2024.2) remain the lod 3 headlines. Root cause was geometric — the country's land wedge is too thin at its 2023 edge for any dot — so the event placer now tries a short inward slide (≤ 40 plate units, nearest usable lane first) before giving up; events that fit at their own year never move. z3 Policy Coast: Bletchley + EU AI Act inline (were curated out). z4: all 10 policy events place (were 4). Sampled-region curation 14 → 5.
- **Gates:** `validate.py` files=19 rules=25 fails=0. `check_lod_labels.py` **LOD LABEL GATE: PASS** (lod3 21 marks; lod4 48 marks + 75 one-line rows). `check_layout.py` all structural, country, containment, zero-overlap and thread gates 0; `clipped` 625 (was 602), all at plate x > 2746 — the pre-existing A1 event-box class, +23 from the newly placed Policy Coast events.
- **Leaflet verified** (Playwright): `?place=generative-coast` opens at the coast; z2.5 shows country names + tag lines + z3 events; z4 loads the coast's own tiles (0 HTTP ≥ 400, all tiles complete). Shots: `docs/screens/leaflet-s14-generative-coast-z2.5.png`, `leaflet-s14-generative-coast-policy-z4.png` (Bletchley + EU AI Act with fact lines), `-frontier-z4.png`, `-agents-z4.png`, `leaflet-s14-deep-learning-basin-z4.png`.
- **Open follow-ups:** z4 text is soft (raster of ~3 px glyphs at DPR 16 — unchanged since session 12; needs an SVG label overlay to be crisp); one z4 dot sits within ~1 unit of the GPT-4o fact line in the Closed Frontier (gate passes; consider a larger lod-4 `S.gap`).

---
### Session 13 (kept for reference)

# STATUS — as of 2026-09-16 (session 13: Generative Coast LOD events layer + Silicon Range Redwood milestone)

## One-line status

**Session 13 — pushed to `main` (6eb4404): Generative Coast gets its z3/z4 event layer — 105 sourced events across 8 countries (48 lod3 headline / 57 lod4 detail), plus z1 hints and z2 tags; Redwood added to the Silicon Range. Alan's "map looks sparse" test-case for the densest timeframe is now on the plate.**

- **`data/events/generative-coast.yaml`:** same schema as `deep-learning-basin.yaml`. Per country: closed-frontier-labs 23 (10/13), open-weights-movement 19 (7/12), agents-tooling-coast 18 (8/10), diffusion-media-district 11 (4/7), reasoning-test-time-compute 10 (5/5), policy-governance-coast 10 (5/5), alignment-interpretability-plateau 7 (4/3), compute-hardware-hinterland 7 (5/2). Every URL verified verbatim against research/08 (script check: 0 misses); all `one_line` ≤ 15 words. Brief-suggested items research/08 does not carry (Let's Verify, Quiet-STaR, ControlNet, Flux, Sleeper Agents, Golden Gate Claude, TPU v5p, SB 1047) were deliberately omitted rather than invented.
- **`build_entities_json.py`:** the event-year span check now resolves `end: present` (all 8 Generative Coast countries) the same way atlas.html's `PRESENT` does; previously it crashed with `str + int`. Output: 17 countries, **155 LOD events** total (50 basin + 105 coast).
- **Silicon Range:** `Redwood` (2026.66, Architect Labs, research/09 [d14]) appended after Jalapeño in `data/threads/silicon-river-hardware.yaml`; thread milestone tail is now Blackwell → Jalapeño → Redwood.
- **Gates:** `scripts/validate.py` → files=19 rules=25 fails=0. `check_lod_labels.py` → **LOD LABEL GATE: PASS** (lod3 20 event marks / lod4 48 marks + 75 one-line rows in the sampled region; 14 events curated out to hover-card only, mostly the dense 2023–24 policy column). `check_layout.py` → every structural, country, containment, zero-overlap and thread gate 0; only `clipped` is non-zero (602, up from 162) and a script check confirms all 602 are event name/year/one_line texts at plate x > 2746 — the same pre-existing A1 event-box class, scaled with the new events.
- **Open follow-up:** policy-governance-coast is the tightest country (6 of its 10 events curated out at z3); a taller sub_band or splitting its lod3 set would let Bletchley / NYT / EU AI Act render inline.

---
### Session 12 (kept for reference)

# STATUS — as of 2026-09-16 (session 12: Tile pyramid rebuild for 1800×1050 + Silicon Range + Leaflet verification + cron watchdog)

## One-line status

**Session 12 — merged to `main`, full tile pyramid (z0–z4, 3069 tiles, 94.4 MB) regenerated for 1800×1050 plate height and Silicon Range; Leaflet map verified; 3-hour cron watchdog registered.**

- **Merged & Flattened to main:** `axis-recalibration-y-height-hardware-range` merged into `main` after resolving citation ordering in `research/09` (Jalapeño as `[d13]`, Redwood as `[d14]`).
- **LOD Label Gate PASS:** Configured `#thread-labels` in `site/atlas.html` to render at A1 macro scale (lod0) and hide at lod1–4, letting regional country names, hints, and paper events occupy the space without collision. Updated `check_lod_labels.py` for the Y-funnel offset. Result: 0 text overlaps across all zoom levels, monotonic information density growth verified.
- **Tile Pyramid Rebuilt:** `build_tiles.py` executed across all levels z0–z4 for the new 1800×1050 canvas. Total 3069 tiles generated (z0: 40, z1: 135, z2: 493, z3: 1881, z4: 560), meta.json updated (`plate: [1800, 1050]`).
- **Anchors Updated:** `build_anchors.py` executed, producing 25 centroid anchors in `anchors.json` matching the new Y coordinates.
- **Leaflet Viewer Verified:** Captured Playwright screenshots (`leaflet-rebuild-A1.png`, `leaflet-deep-learning-basin.png`, `leaflet-generative-coast.png`), confirmed seamless rendering, full Generative Coast vertical extent, and intact Silicon Range relief without missing tiles or tearing.
- **Watchdog & Cron:** Created `/home/node/agent/scripts/map_of_ai_watchdog.py` (checks running jobs and thread turn timestamp <30m) and scheduled `map-of-ai-rework-trigger` cronjob (`every 3h`) to trigger re-work when idle >30m.

---
### Session 11 (kept for reference)

# STATUS — as of 2026-09-13 (session 11: Y-funnel geometry + the Silicon Range — the first cross-cutting linear thread)

## One-line status

**Session 11 — branch `axis-recalibration-y-height-hardware-range` (pilot: deep-learning-basin + generative-coast),
two geometry changes shipped 2026-09-13; NO country/event data or facts edited.**

**Part 1 — Y-FUNNEL v12 (`site/atlas.html`).** The per-band HEIGHT now grows with the year the way the X axis's
width-per-year does (AXES.md §1 `SEG`). `YSEG = [[2017,1],[2022,1.1],[2024,1.3],[2025.2,1.6],[PRESENT,2.0]]`,
`yScale(yr)` piecewise-linear between anchors, 1× for everything ≤ 2017 → 2× at the present-day coast (band 82 → 90 →
107 → 131 → 164 px). Why those ratios: (i) ≤ 2017 must be pixel-identical to v11 (Alan: pre-2025 content is not
redrawn), so the first anchor is 2017 = start of the 6×/yr X segment; (ii) the Transformer Plateau (2017–22) may grow
only "a bit" → 1.1; (iii) the acceleration has to be legible at A1 but not blow the canvas out, so the east edge is 2×
(Alan's 2–2.5× target, taken at the low end because the canvas also carries the ±46 px spine), with most of the growth
after 2024 (1.3 → 2.0 over the last two years = the same "recent gets dramatically more room" shape as SEG's 3× → 6×).
Mechanics: authoring stays in the 1× plate (ROWY/BY/LABEL/ENV unchanged, 150–560); `FY(x, py)` stretches plate y about
band C's centre by `yScale(yearAt(x))` and is applied inside `SY()` with the spine shear, so land, coast, country rows,
labels, graticule and the band legend all fan out by construction. Plate 1800×700 → 1800×1050 (`H`, `RULER_Y` 618 →
975, tilesrc CSS). `check_layout.py` judges bands in the 1× frame via `plateY()` (the renderer's exact inverse).
Measured: Deep Learning Basin land bbox height 288 → 288 (unchanged, only shifted down by Y_OFF=165); Generative Coast
474 → 819 px. Before/after: `docs/shots/y-funnel-before-A2.png` / `y-funnel-after-A2.png` (A2 country view of both
pilots — the 8 coast provinces are visibly taller, all 8 labels legible, no overlaps, polygons intact) and
`y-funnel-after-A1.png` (whole plate: the continent reads as a trumpet widening east; nothing off-canvas).

**Part 2 — THE SILICON RANGE (`data/threads/silicon-river-hardware.yaml` + `drawThreads()` in atlas.html).** First
implementation of an AXES.md §3 cross-cutting LINEAR thread on the actual map (search of atlas.html/data for
river|road|thread before this session: nothing rendered — threads existed only as research/09 prose). It is a
mountain range, not a country: `kind: mountain-range`, its own primitive (spine + relief silhouette + hachures + summit
peaks + hover card), never through fineCell/fineTrace. Runs along the S1/S2 seam (research/09 (d): "connectionist/
scaling bank after 1999") from 1999 to the present coast, so it crosses the Basin, the Plateau and the Coast. Peak
height ∝ milestone `peak` × the local (funnelled) band height, so eastern peaks are taller. Milestones — ALL from
research/09 thread (d)'s Milestones table, every url a [d1]–[d12] citation copied verbatim: GeForce 256 1999 [d3] ·
CUDA 2007 [d4] · AlexNet on GPUs 2012 [d5] · TPU + DGX-1 2016 [d6] · Volta V100 2017 [d11] · Cerebras WSE-1 2019 [d11]
· Scaling laws 2020 [d7][d12] · Hopper H100 2022 [d8] · Export controls / CHIPS Act 2022 [d10] · Blackwell 2024 [d9].
Lisp machines 1973 [d1] and Connection Machine 1985 [d2] are recorded under `not_yet_drawn` (symbolic bank, west of
both pilots; out of this pilot's span). Labels (name + year) use the country/event offset-search idiom (`union` +
`fitsInside` + placed-box hit test, lod 2 curated out if nothing fits, lod 1 gets a leader) AND the range's skyline is
registered as `window.THREAD_OBSTACLES` before `relayout()`, so continent labels are placed around it by construction
(`deep-learning-basin` gained `alt` anchors north of the ridge for this). Result on the A1 plate: all 11 milestone
labels placed, 0 curated, 0 thread-label overlaps, 0 outside the coast, "SILICON RANGE" title set under the ridge in
the Basin. Screenshot: `docs/shots/silicon-range-A1.png`.

**Jalapeño chip — flagged, then sourced, then added (in that order).** When Part 2 was built, `grep -ri jalape
research/ data/ site/ AXES.md` returned zero hits, so it was NOT drawn and no citation was invented. Commit 6612451
(Alan, via Hermes, same session) then added it to research/09 thread (d)'s Milestones table as [d13] (OpenAI,
"Jalapeño's first results…", 25 Aug 2026, via a Wayback snapshot because the live page sits behind a Cloudflare
challenge). Only after that citation existed was an 11th milestone (`year: 2026.65`, lod 1, ref d13) added to the
thread yaml. Note the source is the vendor's own announcement archived 2 weeks ago — weaker than the Wikipedia/arXiv
sources behind [d1]–[d12]; worth a second independent source when one exists. Render note: a present-month milestone
sits ON the east coast, so `drawThreads()` clamps a summit west by half a peak width to keep the whole peak on land
(`MX()`); the year label is unchanged.

**Gates (real `check_layout.py --shot` output, after Part 2):** continents 10 · lands 13 · coastLoops 5 · overlaps 0 ·
notAdjacent 0 · outsideCoast 0 · bandViol 0 · labelOverlaps 0 · textClash 0 · outside 0 · foreign 0 · smallFonts 0 ·
rulerClashes 0 · envelopeViol 0 · notFunnel 0 · countryCount 15/15 · countryContainment 0 (300/300 inside parent for
all 15) · countryOverlap 0 · zoomInconsistent 0 · countryLabelOverlaps 0 · countryLabelOutside 0 · NEW threadCount 1 ·
threadLabelsVisible 11 (≥ 4) · threadLabelOverlaps 0 · threadLabelOutside 0. Overall RESULT is FAIL only on the
pre-existing `clipped` (A1 event-label boxes vs viewBox; 160 at session start, 162 now — same class, the z3/z4 event
layer is out of scope here). Every other gate is at or above the session-10 standard.

**Out of scope, flagged as the natural next step:** the LOD tile pyramid (`build_tiles.py` PLATE = (1800, 700),
`site/tiles/`, index.html Leaflet bounds) is still built from the OLD 700-px geometry and does not know about threads.
Rebuilding it now would bake in geometry that may still move; do it once this base geometry is confirmed good.
Fuller range version (not needed for the pilot): extend west to the Lisp/Connection Machine symbolic-bank segment,
per-lod label sizes for z2–z4 like events, and a `thread-labels` export into `labels.json` for the Leaflet overlay.

---
### Session 10 (kept for reference)

**Session 10 — P2-T10 + P3-T10 (Generative Coast, 2022–present) data layer shipped 2026-09-13.** Alan: "the map
looks sparse to me … We can try the most current timeframe and see what dense looks like." Coverage matrix
`data/coverage/generative-coast.md` maps research/08's 8 `## Schools of thought` bullets 1:1 to 8 countries (8 < SPEC
§4.3 cap of 9; 0 merged, 0 dropped): `closed-frontier-labs` The Closed Frontier (Ca) · `open-weights-movement` The
Open-Weights Commons (Cb, 2023–) · `diffusion-media-district` The Diffusion Shoreline (S2a+S2b) ·
`reasoning-test-time-compute` Reasoning Ridge (N2b, 2024–, wetland) · `agents-tooling-coast` The Agents Causeway
(S1a+S1b, mixed) · `alignment-interpretability-plateau` The Alignment Plateau (N1b, mixed) · `policy-governance-coast`
The Policy Coast (N1a, 2023–, highland) · `compute-hardware-hinterland` The Compute Hinterland (S2c, harbour).
`data/continents/generative-coast.yaml` (P2-T10) written in the same session because validate.py V-30 needs the
parent. Sourcing: all 59 country `sources[].url` + 8 continent urls are byte-identical substrings of research/08's
`## Sources`; every `research_ref.sources` int exists there (V-22); every dated fact in the 9 summaries was
spot-checked by grep against research/08's timeline (Midjourney 12 Jul 2022, GroqCloud 19 Feb 2024, Nvidia $4T, 28
countries at Bletchley, Qwen3.8, Muse Spark, Sora 2, Cowork, $5.6M, Mostaque, Sydney, SSI, AlphaProof, Kimi K2, Gemma 4,
Turing Award, 100 million — all present). `scripts/validate.py` → files=19 rules=25 fails=0 **including V-20 live
links**. Render wiring: `site/atlas.html` country grid gained N1a/N1b/N2a/N2b fine rows (the coast is the only
full-height continent), 2023/2024 sub-columns and `end: 'present'` → E; `build_entities_json.py` / `validate.py`
SUB_BANDS now list N1a–N2b; `entities.json` = 17 countries, 15 spatial. `check_layout.py` (N_COUNTRIES 7 → 15): all
country gates PASS — countryCount 15/15, containment 300/300 inside parent for all 15, zero-overlap 0 pairs, 0 label
overlaps, 0 labels outside, A2 zoom consistent. Its overall RESULT is FAIL only on `clipped` (A1 event labels near
the viewBox edge), which is pre-existing: 179 before this change, 160 after (verified by `git stash`). Evidence:
`docs/screens/generative-coast-a2.png` (A2 country view: 8 stacked provinces N→S, each with name + years; new
`site/probe_continent_countries.py <continent-id>` prints per-country bbox + visible labels). NOT done (Phase 2,
separate task): z0–z5 tiles, `data/events/generative-coast.yaml`, hints, headline events; deep-learning-basin data
and tiles untouched. Known: `site/probe_countries.py` times out on `#shapes .continent` visibility at baseline too
(pre-existing, not investigated).

**LEAFLET v3.1 (LOD pilot fixes) shipped 2026-09-13** — https://zeroasterisk.github.io/map-of-ai/
**Alan on v3:** "text is crazy big, when you zoom in it should have resized" and "I don't understand the red lines".

**Fix 1 — text sized in SCREEN px, not plate units.** build_tiles.py screenshots
lod level z at device scale 2**z, and every label font-size was a plate-unit
constant, so on-screen text GREW with zoom (kev-name 4.0 plate × 8 = 32 px at
z3 → 2.3 × 16 = 36.8 px at z4; country kname 10.2 plate × 16 = 163 px at z4).
atlas.html now derives the plate font-size from a per-role screen-px target:
`plate_fs = target_px / 2**lod` (`TILESRC`/`LOD`/`ZSCALE`/`PX()` at the top of
the script; only in `?tilesrc=1` mode — the plain interactive atlas.html is
byte-for-byte the same layout). Targets: kname 34 px, ktag/ksub/kyrs 28 px
(lod2–4, the auto-fit tier ladder scales by the same factor, line gap 4 px);
khint 16 px (lod1 — 28 px fits in no lane, 16 px is the largest size that
places both hints); kev-name 30 → 26 px, kev-year 22 → 19 px (lod3 → lod4),
kev-line 19 px. Measured (site/measure_lod_text.py, getBoundingClientRect ×
2**lod, median bbox height in screen px):

| role | before lod2 / lod3 / lod4 | after lod2 / lod3 / lod4 |
|---|---|---|
| kname (country) | 48 / 96 / 192 | 40 / 40 / 48 |
| ktag / kyrs | 40 / 80 / 160 | 36 / 36–40 / 48 |
| kev-name (same event, e.g. AlexNet) | – / 42.7 / 48.0 (+12 %) | – / 40.0 / 34.3 (−14 %) |
| kev-year | – / 29.3 / 35.2 | – / 26.7 / 22.9 |
| kev-line | – / – / 32 | – / – / 22.9 |

(kname at lod4 is 48 vs 40 at lod3 because the widest tier now fits inside
every lane at z4 — +20 %, the "a bit bigger at deeper lod" allowance; before it
was ×2 per level.)

**Fix 2 — event leaders.** `.kev-leader` was the dot's rust red (#7a2414) and
read as a road. Now the country leader's language: solid #3d2e1a hairline
(.45, opacity .7). Deliberately NOT dashed — the province line (.kzoom) and
road border (.cborder.road) at lod2–4 are already dashed brown, and a dashed
trial rendered indistinguishable from them (docs/screens review). Evidence:
docs/screens/lod4-leaders-after.png (Attention Headwaters, z4, 4 leaders).
`.kev-dot` stays red.

Gates after both fixes: check_lod.py PASS, check_lod_labels.py PASS (0
overlaps, 0 dots outside, 0 off-plate; curated: ev3 white-house-2016, ev4
ntm-2014 / show-and-tell-2014 / sensetime-ilsvrc-2016). Basin text items /
chars / marks per level are now 5/39/0 → 7/122/0 → 32/446/0 → 72/928/20 →
201/2950/47 (smaller text = more of the 47 events fit at z4; was 32).

## One-line status (session 8, superseded)

**LEAFLET v3 (LOD pilot) shipped 2026-09-12** — https://zeroasterisk.github.io/map-of-ai/
**Alan's feedback on v2:** "the details are not detail-y enough … I really want
the zoom-in to provide more and more and more detail at every step, not just
a different texture" and, correcting the plan to bolt a deeper tier on: "the
levels you have right now maybe don't need to exist without additional
detail … each of those steps needs to have a significant increase in the
amount of information presented for the same region." Diagnosis of v2 by its
own numbers: z0→z1 was texture + one year line, z2→z3 was a subtitle line.

**What changed — 5 levels (z0–z4), each step carries new FACTS, not a new
texture.** Content redistributed and expanded across the existing steps; z4
added because 40+ sourced events at z3 would have collided (curate, don't
overlap). PILOT SCOPE: only the Deep Learning Basin has hint/tag/event data;
every other continent renders exactly as before (its z3 art also serves
zoom 4 — no new tiles elsewhere). Wider rollout is a separate task, not
started.

| level | px/unit | tiles | NEW at this step (Basin) | basin text items / chars / event marks |
|---|---|---|---|---|
| z0 | 1 | 24 | continents, names | 5 / 39 / 0 |
| z1 | 2 | 90 | textures, continent years, faint borders, **+4 landmark hints** ("ImageNet · AlexNet 2012", "DQN → AlphaGo", "word2vec → attention", "Google Brain · DeepMind · OpenAI") | 8 / 152 / 0 |
| z2 | 4 | 319 | solid borders, country names, **+ per-country one-line tag + years** (7 tags, e.g. "ImageNet → AlexNet → ResNet", "SenseTime; first national AI plans") | 33 / 429 / 0 |
| z3 | 8 | 1254 | country subtitles, **+17 headline events as dots at their year** (ImageNet 2009, Google Brain 2011, AlexNet 2012, DQN 2013, word2vec 2013, VAE 2013, GAN 2014, ResNet 2015, AlphaGo v. Lee Sedol 2016, WaveNet 2016, Switchboard parity 2016 …) | 67 / 662 / 17 |
| z4 | 16 (bbox only, 560 tiles) | 560 | **+15 more events (32 on the map) and a sourced one-line fact under each headline event** (e.g. AlexNet "15.3 % top-5 error vs 26.2 %"; Four-groups paper "error rates fall ~30 %") | 144 / 1880 / 32 |

Before (v2, same region, same measurement): 5/39 → 4/64 → 15/184 → 22/247;
z0→z1 LOST items; z2→z3 added only 7 subtitle lines. After: every step at
least doubles the text items (5→8→33→67→144) and chars grow 39→152→429→
662→1880. `site/check_lod_labels.py` (new gate) asserts this growth per
step and ZERO text-on-text overlaps, every event dot inside its own country,
at every level: PASS (`docs/screens/check_lod_labels_after.txt`; before
numbers in `docs/screens/lod_labels_before.json` — v2 also had one kname
overlap at lod2 the old gate never saw).

`site/check_lod.py` reworked: the old "ink fraction after downsampling all
levels to z0 size" metric erased small type (z2→z3 read +0.0016) and could
not see the difference; it now measures ink MASS at each level's own
resolution, scale-normalised (dark px ÷ 2^z ÷ area ×1000), with a minimum
gain per step. Basin, plate (804,320,386×288):

| step | before (v2) | after (v3) |
|---|---|---|
| z0→z1 | 20.1 → 47.1 (+27.1) | 20.0 → 49.0 (+29.0) |
| z1→z2 | 47.1 → 161.9 (+114.8) | 49.0 → 195.4 (+146.5) |
| z2→z3 | 161.9 → 354.7 (+192.8) | 195.4 → 438.7 (+243.2) |
| z3→z4 | — | 438.7 → 919.4 (+480.7) |

(ink mass also counts textures/borders, so v2's steps were not zero — the
text-item / char counts above are the information measure; both improved
on every step.) Gate PASS, see `docs/screens/check_lod_before.txt` /
`check_lod_after.txt`.

**Sourcing — zero invented facts.** Every hint, tag and event lives in
`data/events/deep-learning-basin.yaml` with `sources:` and traces to
`research/06-deep-learning-revolution-2006-2017.md` (its numbered refs) or a
country YAML `sources:` entry — checked mechanically: all 50 events' URLs
appear verbatim in one of those files (0 unsourced). Examples: AlexNet 2012
→ proceedings.neurips.cc …c399862d… (Krizhevsky, Sutskever & Hinton) +
en.wikipedia.org/wiki/AlexNet; ResNet 2015 → arxiv.org/abs/1512.03385;
"Four groups" 2012 → ieeexplore.ieee.org/document/6296526 (Hinton et al.,
IEEE SPM); AlphaGo v. Lee Sedol → en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol.
Detail is
uneven on purpose: Eastern Coast Forts (SenseTime / national plans, 2015–17)
is a narrow lane with only 4 sourced events, 2 of which fit; Speech has 7.
Events that did not fit are curated off the raster (listed by the gate) and
remain in entities.json for hover cards — not overlapped.

**Rendering notes:** events are positioned by derivation (x = X(year), y in
the country's lane), placed with the country-label idiom (offset search →
collision against placed boxes → leader line → curate out). Chromium hints
sub-3 px glyph advances even at DPR 16, which bunched letters in the z4
tiles; `text-rendering: geometricPrecision` in tilesrc mode fixed it (verified
on a 16× crop). z4 is rendered in tile-row strips of the Basin bbox
(768,304)–(1216,624) to bound memory; `index.html` mounts it as a second,
bounded tile layer (`meta.full_zmax`, `meta.pilot_bbox`) so no 404 storm off
the basin. `check_layout.py`, `check_url.py` still PASS.

**Evidence:** `docs/screens/lod2-0.png .. lod2-4.png` (atlas render of the
Basin, 780,300→1220,620, per lod, 4× — compare v2's `lod-0..3.png`),
`docs/screens/lod2-index-z0..z4.png` (the Leaflet viewer on the shipped
tiles at each integer zoom), `docs/screens/lod-tiles-same-region.png`
(z0..z4 reassembled from tiles).
Previous status follows.

## One-line status (session 7, superseded)

**LEAFLET v2 (LOD) shipped 2026-09-12** — https://zeroasterisk.github.io/map-of-ai/
**Alan's bug: "I zoomed in and the tiles didn't change."** Root cause: v1
took ONE 8× screenshot of `atlas.html?tilesrc=1` and made z0–z2 by LANCZOS
downsampling it, so every level was the same picture at a different
resolution — zooming sharpened strokes but never revealed anything. Fix:
**each zoom level is now its own render.** `atlas.html?tilesrc=1&lod=N`
(N=0..3) is a set of CSS-only toggles on already-placed elements (no drawing
math duplicated), and `build_tiles.py` screenshots lod=z at device-scale 2^z
and slices it ONLY into level z (no resampling between levels). What is
visible per level:

| level | px/plate unit | tiles | shows |
|---|---|---|---|
| z0 | 1 (1800×700) | 24 | flat tinted continents (no terrain texture), coast, ONE label per continent (name only), leaders; no country layer |
| z1 | 2 (3600×1400) | 90 | + terrain textures, + continent subtitle/year lines, + faint country borders (A1 style), no country labels |
| z2 | 4 (7200×2800) | 319 | + solid country borders (A2 province line), + country NAME labels; a continent whose countries are labelled hides its own huge name (else "BASIN" sat on "The AlphaGo Delta") |
| z3 | 8 (14400×5600) | 1254 | full detail: country name + subtitle + years, country leaders/dots, per-country biome tints |

Only the Deep Learning Basin has country data (unchanged scope); other
continents just gain textures and year lines from z1 on. Labels/leaders/
countries are therefore IN the raster now; `index.html` dropped the DOM
label overlay (the invisible continent hit-paths for hover cards remain),
and its HUD says which level's tiles are on screen. 1687 tiles, 58 MB.

**Evidence that content changes, not just resolution:**
- `docs/screens/lod-0.png .. lod-3.png` — the same plate region (Basin,
  780,300 → 1220,620) screenshotted at each lod, same scale, side by side.
- `docs/screens/lod-tiles-same-region.png` — the same region REASSEMBLED
  FROM THE SHIPPED TILES of z0..z3, downsampled to one size.
- `site/check_lod.py` (new gate, PASS): after downsampling every level to
  z0 size, dark-ink fraction in the Basin interior is z0 .0103 < z1 .0123 <
  z2 .0371 < z3 .0375 (the z1→z2 jump is the country borders + names);
  adjacent levels differ by mean |Δluma| 23.0 / 10.0 / 6.1 vs a pure-resample
  noise floor of 1.8 / 1.7 / 1.0; a texture-only land patch has luma stddev
  2.9 at z0 vs 18.9 at z1 (flat vs textured); bytes per plate unit² z0 1.1 →
  z3 30.9.
- `site/verify_leaflet.py` (PASS): at fit zoom Leaflet holds 24 tiles all
  from `tiles/0/`; after wheel-zoom to 3.0 it holds 50 tiles all from
  `tiles/3/`; at zoom 2 on the Basin 28 tiles all from `tiles/2/`; 167
  requests, 0 non-200, 0 JS errors. Live: `Last-Modified: Sat, 12 Sep 2026
  22:22:43 GMT` on `/`, `/static-map.html`, `/tiles/meta.json`, sample z0
  and z3 tiles; live `meta.json` carries the per-level `lod` descriptions.

**Audit URL (no pan/zoom UI, raw 256 px tiles at 1:1):**
`https://zeroasterisk.github.io/map-of-ai/static-map.html?level=2&x=15&y=7`
— one tile; add `&r=1` for the 3×3 ring around it; `?level=0` alone shows a
whole level; **`?level=3&px=1000&py=450`** shows the tile containing plate
point (1000,450) — change only `level` to compare the same place across
levels (the page links z0/z1/z2/z3 for the focused tile's centre, and prints
the tile's plate-unit extent). Query params rather than a path like
`/static-map/2/15,7` because GitHub Pages serves static files only — no
server routing, no `_redirects`. `check_layout.py` (atlas.html) still PASS.
Previous status follows.

## One-line status (session 6, superseded)

**LEAFLET v1 shipped 2026-09-12** — https://zeroasterisk.github.io/map-of-ai/
is now a real Leaflet 1.9.4 map (`L.CRS.Simple`, Google-Maps-style
scroll-wheel / pinch / drag / +− zoom) over a raster XYZ tile pyramid of the
**unchanged v11 continent art**. Nothing was redrawn: the old renderer is
`site/atlas.html` (was `index.html`, art byte-identical; gained a
`?tilesrc=1` bare-plate mode and `window.exportLabels()`), and
`site/build_tiles.py` screenshots it at device-scale 8 (14400×5600 px) and
slices `site/tiles/{z}/{x}/{y}.png`, z0–z3, 256 px, **1687 tiles, 62 MB**,
committed as static files (z3 1254 · z2 319 · z1 90 · z0 24). Coordinate
system: 1 plate unit (atlas viewBox px, 1800×700) = 2^z screen px, so every
overlay position is the same `X(year)` / `bandTop(band)` number atlas.html
draws — continent name labels (divIcon markers, sizes from atlas.html's own
placement, ×2^min(zoom,1)), leaders, leader dots and land hit-paths (hover
cards) come from `site/labels.json` exported by that placement code.
Verification (`site/verify_leaflet.py`, run against the LIVE URL): wheel
zoom −0.5 → 3.0, drag moved centre (1131,349) → (1176,334), 192 tile
requests all 200, 0 JS errors — screens `docs/screens/leaflet-v1-initial.png`,
`leaflet-v1-after-wheel-drag.png`, `leaflet-v1-z2-basin.png`.
**Not in this view yet (milestone 2, next session): the P3-RENDER country
layer** (7 Basin countries, A2 labels, containment gates) — still fully
working at `atlas.html`, which `check_layout.py` now targets. Honest image
quality: at fit zoom (−0.5) and z2–z3 native the raster is crisp (ink strokes
clean, no visible seams after the integer-tile-size fix); z3 = 8 px per plate
unit, i.e. 8× the old SVG's 1:1, and `maxZoom` is capped at 3 so tiles are
never upscaled (a z3.5 test showed visible blur + 1 px hairline gaps — both
fixed by the cap and by `width:256px !important` + `will-change`). Fractional
zooms (zoomSnap .25) between native levels are browser-downsampled, slightly
softer than integer levels but no seams. Tile decisions: 256 px (Leaflet
default; 512 would quarter request count but the whole pyramid is ~60 MB
either way), z3 max because z4 would be ~4× the tiles (~250 MB in the repo,
untested 16× = 28800 px screenshot) while z3 already out-resolves the source
textures (512 px JPGs at 230 plate px → 1.8 px per texture px at z3). Previous status
follows.

## One-line status (session 5, superseded)

**P3-RENDER v2 shipped 2026-09-12** — the Deep Learning Basin pilot now renders
7 spatial countries (partition pre-solved by Alan, implemented as given):
`gpu-convnet-school` S2a 2009–2015 · `speech-recognition-converts` S2b
2009–2016 · `deep-generative-shoreline` S2c 2013–2017 ·
`neural-nlp-sequence-school` Ca 2011–2016 · `industrial-lab-founders`
Cb+S1a 2011–2015 · `deep-rl-delta` S1b 2013–2017 · `chinese-state-response`
Cb 2015–2017. Two countries demoted to hover facts (`spatial: false`, data
kept): `tooling-guild` → continent-card "also happening" fact;
`pretraining-foothills` → "preceded by" fact on gpu-convnet-school. One
nudge: chinese-state-response start 2014→2015 (clean Cb handoff from
industrial-lab-founders; noted in its YAML). Sub-bands are a country-layer-only
split of the existing ROWY rows (C→Ca/Cb, S1→S1a/S1b, S2→S2a/S2b/S2c);
continent geometry is byte-identical A1↔A2 (gate). `check_layout.py` →
RESULT: PASS incl. new gates: containment 300/300 in parent for all 7,
zero-overlap 0 hits over 8 pairs × 500 samples, coast/border `d` identical
zoomed vs not, A2 labels non-colliding. Live: https://zeroasterisk.github.io/map-of-ai/
(click the Basin → A2; Esc/sea → A1). Screens: `docs/screens/p3-v2-A1.png`,
`p3-v2-A2.png`, `p3-v2-A2-crop.png`. Honest A2 note: 5 of 7 lanes are too
thin for an inside label and fall back to name+years with a leader; the
2006–2011 western lobe of the Basin is intentionally uncovered (foothills
demoted). Previous status follows.

## One-line status (session 4, superseded)

**Registry accepted by Alan 2026-09-11 (v11) — "registry-frozen".** P0, P1,
P2-T1, P2-T1-RENDER done. Session 4 closed the two P3 spec/plan gaps
(`SPEC.md` §9 P3-RENDER; `PLAN.md` §5 dependency note + P3-RENDER unit) and
landed the pilot data layer: `data/continents/deep-learning-basin.yaml`
(P2-T8) + 9 country YAMLs (P3-T8) + `data/coverage/deep-learning-basin.md`
Table 1; `scripts/validate.py --summary` → files=10 fails=0 (V-20 links live).
**Next gate: Alan reviews `SPEC.md` §9, then P3-RENDER is built** so the pilot
decomposition can be reviewed visually. Monthly frontier intake (P5) remains
**deferred by Alan, not scheduled.**

## What Alan is being asked to review

**Session 4 (2026-09-11) items — review first:**

1. `SPEC.md` §9 (P3-RENDER): the visual grammar G1–G10 and acceptance
   criteria A-V1…A-V10 for drawing countries inside a continent. Key calls:
   two zoom states (A1 = today's map, A2 = click a continent → its countries
   with labels, other continents dimmed); countries reuse the parent texture
   unless their `biome` differs (wetland RL delta, harbour tooling guild);
   thin wobbly interior borders, no new continent geometry.
2. `PLAN.md` §5 dependency note: a continent's countries proceed on
   *registry-frozen* + its own continent YAML, not on all ten continents'
   P2-T2…T13.
3. The pilot decomposition itself (`data/countries/*.yaml`, 9 files) — the
   A-K7 judgement calls are listed at the bottom of
   `data/coverage/deep-learning-basin.md`. Read them as YAML for now; visual
   review comes after P3-RENDER.

**Earlier (registry, v11 — accepted 2026-09-11):**

Open <https://zeroasterisk.github.io/map-of-ai/> (GitHub Pages, deployed from
`site/` by `.github/workflows/pages.yml`; source of truth is
`data/continents/REGISTRY.md`). Questions on the page banner:

1. Does the west-to-east ordering and the left-right sense of scale feel right?
   (X is piecewise-scaled per `AXES.md` §1: 1943–74 1×, 1974–2006 1.5×,
   2006–17 3×, 2017–present 6×; pre-1943 is a log-compressed archipelago.)
2. Do the biome colours read clearly (highland / grassland / forest / jungle /
   mixed)?
3. The two judgement calls in `REGISTRY.md` §2: **D1** research/01 → Antecedent
   Isles (offshore) + Cybernetic Shore; **D2** research/03 → Winter Steppes
   (1974–1993) + Expert Systems Plateau (1980–1993, nested "warm valley").
4. Names/subtitles (`REGISTRY.md` §1). Ids freeze once accepted.

| # | id | name | span | biome |
|---|---|---|---|---|
| 1 | `antecedent-isles` | The Antecedent Isles | 1666–1942 (offshore) | highland |
| 2 | `cybernetic-shore` | The Cybernetic Shore | 1943–1956 | mixed |
| 3 | `symbolic-heartland` | The Symbolic Heartland | 1956–1974 | highland |
| 4 | `winter-steppes` | The Winter Steppes | 1974–1993 | highland |
| 5 | `expert-systems-plateau` | The Expert Systems Plateau | 1980–1993 | highland |
| 6 | `connectionist-revival` | The Connectionist Revival | 1982–1998 | forest |
| 7 | `statistical-isthmus` | The Statistical Isthmus | 1988–2011 | grassland |
| 8 | `deep-learning-basin` | The Deep Learning Basin | 2006–2017 | forest |
| 9 | `transformer-plateau` | The Transformer Plateau | 2017–2022 | jungle |
| 10 | `generative-coast` | The Generative Coast | 2022–present | jungle |

## Phase status

| Phase | Units | State | Evidence |
|---|---|---|---|
| G0 | go-ahead | done (Alan: "get the history and current correct") | this session |
| P0 tooling | P0-T1…T4 | **done** | commits `9d25447` `1db3e92` `bf7c56d` `76d9de6`; `scripts/fixtures/run.sh` passes (25 V-rules, one FAIL per invalid fixture) |
| P1 research coverage | P1-T1…T9, T10, T11 | **done** | commits `7bc7c72` (T11), `89793c3` `c096929` `937d2bf` `28bb209` `40ae90b` `32d271b` `4296598` `58b035d` `8bbfbbe`; all nine files `Status: reviewed`; `scripts/check_research.py research/0*.md` → R-01…R-07 PASS for every file; review reports in `data/reviews/2026-09-06-research-0N.md` |
| P2-T1 registry | P2-T1 | **done, proposed** | commit `95e9323`; `scripts/check_registry.py` → 13/13 PASS |
| P2-T1-RENDER | render + Pages | **done, live (v11)** | commits `1247b0b` … `47cf0d2`; Pages workflow green; live URL HTTP 200 with title text; headless Chromium draws 10 continents, 0 JS errors; `site/check_layout.py` PASS |
| P2-T2…T13 | continents | **P2-T8, P2-T10 done** (`data/continents/deep-learning-basin.yaml`, `generative-coast.yaml`, status sourced); T2–T7, T9, T11–T13 not started, unblocked (registry-frozen) | validate.py 0 FAIL incl. V-20 |
| P3 countries | P3-T1…T12 | **P3-T8 done** (9 countries, coverage Table 1 = 9/9 bullets); **P3-T10 done** (8 countries, Table 1 = 8/8 bullets, all spatial, rendered at A2); A-K2 refs⊆bullet checked; T1–T7, T9, T11–T12 not started | `scripts/validate.py` → files=19 fails=0; `check_layout.py` country gates 15/15 |
| P4 city pilot | P4-T1…T8 | not started | — |
| P5 frontier intake | P5-T0, P5-R1…R6 | **deferred by Alan, not scheduled** (`PLAN.md` §7 header) | — |
| P6 quality | P6-T1…T5 | not started | — |

## P1 in numbers (history accuracy work)

| File | Timeline rows | Sources | Candidates reviewed (added/folded/rejected) |
|---|---|---|---|
| 01 origins | 36 | 51 | 25 (10/9/6) |
| 02 Dartmouth & symbolic | 40 | 57 | 25 (15/7/3) |
| 03 winters & expert systems | 35 | 55 | 24 (12/8/4) |
| 04 connectionism | 34 | 92 | 24 (11/8/5) |
| 05 statistical ML | 30 | 92 | 28 (22/1/5) |
| 06 deep learning | 41 | 120 | 33 (15/13/5) |
| 07 transformers | 43 | 94 | 38 (20/12/6) |
| 08 generative & agents | 63 | 120 | 47 (33/4/10) + triangulation of 6 provisional items (5 moved to sourced rows with confidence, 1 rejected) |
| 09 cross-cutting threads | 16 junctions (+ 8 thread tables) | 95 | 30 (20/5/5) |

Every added item carries a source fetched (HTTP 200) during the review;
reviewer ≠ author per git log (SPEC.md R-07). `research/08`'s "Needs
verification" section is empty; the east edge is Sept 2026 with
`(confidence: …)` annotations on the last rows (`data/reviews/2026-09-06-research-08-triangulation.md`).

## Where to look

| Question | File |
|---|---|
| What is this project? | `BRIEF.md`, `README.md` |
| Coordinates / zoom levels | `AXES.md`, `ALTITUDES.md` — decided |
| What "correct" looks like | `SPEC.md` |
| Work breakdown, DAG, gates | `PLAN.md` (§4 has P2-T1-RENDER; §7 marks P5 DEFERRED) |
| The continent registry | `data/continents/REGISTRY.md` |
| The rendered prototype | `site/` → <https://zeroasterisk.github.io/map-of-ai/> |
| Deep links to a view (`?place=deep-rl-delta`, `?z=2&x=1000&y=400`, copy-link button) | `docs/URL_SCHEME.md`; gate `site/check_url.py` |
| Review reports | `data/reviews/` |
| Tooling | `scripts/README.md` |

## Decisions (recorded; do not re-open)

| # | Decision | Status | Where |
|---|---|---|---|
| 1 | Y = Candidate E, five soft bands; symbolic ↔ learned as biome | Confirmed | `AXES.md` §3 |
| 2 | X mainland starts 1943; pre-1943 offshore archipelago | Confirmed | `AXES.md` §1 |
| 3 | Three altitudes; people are `type: person` cities | Confirmed | `ALTITUDES.md` |
| 4 | Evocative name + neutral subtitle | Confirmed | `SPEC.md` §2.3 |
| 5 | Adjacent fields case-by-case | Soft default | `SPEC.md` §2.9 |
| 6 | X scale piecewise (prototype uses AXES.md §1 ratios) | Rendering decision; prototype implements the piecewise table | `AXES.md` §1 |
| 7 | Monthly frontier intake | **Deferred by Alan, not scheduled** | `PLAN.md` §7 |
| 8 | research/01 → two continents; research/03 → two continents | Proposed (P2-T1), awaiting Alan | `REGISTRY.md` §2 |

## What exists in the repo

| Path | State |
|---|---|
| `research/01`–`09` | `Status: reviewed`; R-01…R-07 PASS; links `failed=0` |
| `data/continents/REGISTRY.md` | proposed (10 rows) |
| `data/reviews/` | 11 reports (9 coverage, 1 triangulation, 1 review brief) |
| `scripts/validate.py` | SPEC.md §3 rules V-01…V-60 (25 rules); `--offline`, `--file`, `--require-children` |
| `scripts/fixtures/` | valid set + one invalid case per rule + `EXPECTED.txt` + `run.sh` |
| `scripts/check_links.sh` | Markdown + YAML `url:` values; allowlist with reasons |
| `scripts/check_research.py` | R-01…R-07 for research files (numeric and lettered source keys) |
| `scripts/check_registry.py` | P2-T1 Check |
| `scripts/wiki.sh` | back-off + retry + on-disk cache |
| `site/` + `.github/workflows/pages.yml` | review prototype, deployed |
| `data/countries/`, `data/cities/`, `data/coverage/` | do not exist yet (P3/P4) |

## Known issues / tooling notes

- `check_links.sh`: `dspace.mit.edu` returns 405 to non-browser requests and
  `doi.org/10.1086/286788` is intermittently slow — both allowlisted with
  reasons in `scripts/link_allowlist.txt`.
- `ai.meta.com/blog/*` → 400 and `openai.com/index/*` → 403 to curl; use
  `about.fb.com`, `openai.com/news/rss.xml`, or Wayback snapshots (recorded in
  the research/08 triangulation report).
- Render prototype: the 1980–2011 cluster (Steppes / Plateau / Revival /
  Isthmus) overlaps by design (ALTITUDES.md §2 "continents overlap in X on
  purpose"); translucency is used so all four read. Real Phase-4 polygons will
  replace this.
- Render pass v10 (2026-09-09): Alan on v9 — "looking pretty good … the
  easternmost edge should be full top to bottom, and if there's some kind of a
  color coding, it should be on theme but a bit more intense." (1) East edge:
  the registry already had the coast at N1–S2; the v7 "ragged frontier" GRID
  rows receded the last two columns to N1b–S2b and N2a–S2a, so the present-day
  coast was only 284 plate px of a 410 px band area. GRID columns 2024.3 →
  present are now all `ggggggggg`; measured land at 2025.9 is plate y 142–564
  (band area 150–560). (2) Tints: BIOME hues kept, saturation ~1.5–3× (highland
  #b48a5c→#c4763a, grassland #c8a85a→#d6a52c, forest #7d8f60→#5e9238, jungle
  #5f8378→#2a8c6c, wetland #7f8f96→#4c8ca4, harbour #a59a84→#b89a5e, mixed
  #7c6f8c→#7a58a4) and the wash/border-band opacities .13/.26 → `TINT_WASH`
  .30 / `TINT_BAND` .48. All gates PASS. **Independent review found the tint
  bump NOT visible** ("colors are on the muted/parchment side") — see v11.
- Render pass v11 (2026-09-09, "biome-only intensity"; Alan: "Intense = biome
  only and don't overdo it"). Root cause of the invisible v10 bump: the tint is
  a normal-blend wash over a texture that is itself ~80 % parchment (texture
  means: sat .20–.36, value .81–.97), so rendered = tex·(1−wash) + tint·wash;
  at wash .30 a fill was still 70 % parchment. Sampled live v10 fill saturation
  (HSV of the mean of 300 in-fill pixels per region) was only .13–.46 and
  chroma barely moved vs v9 — the swatches got vivid, the map did not. v11
  solves the tint FROM the wanted rendered colour (`tint = 2·target − texture
  mean` at `TINT_WASH` .50; `TINT_BAND` .52): highland #b66b30, grassland
  #c5a64c (pulled back from a first candidate #cd9e28 that the reviewer called
  "the one that tips toward garish"), forest #558828, jungle #0f7562, wetland
  #2d7eb7, harbour #af974c, mixed #7155b8. Measured live v10 → v11 saturation:
  symbolic-heartland .38→.45, expert-systems .40→.48, isthmus .46→.45 (chroma
  106→99, deliberately held), connectionist .30→.37, basin .31→.39, transformer
  .18→.24, generative-coast .18→.26, cybernetic .13→.15. Only biome fills
  changed — border ink, labels, sea, halo untouched. Independent vision review
  of the live v11: "clearly more saturated … still holds the antique-atlas
  register". All gates PASS (`check_layout.py` RESULT: PASS, marker v11).
- Render pass v9 (2026-09-08, "isochrone frontiers"): Alan on v8 — "still too 90
  degree rectangular … the basic allocations are still too rigidly along x and
  y grids". Root cause: every boundary was `x = start_year` (one x for the whole
  boundary; wobble/lean on a plumb line is still a plumb line). v9 adds `FRONT`
  in `site/index.html`: per column line, per half-band row, a YEAR OFFSET, so
  every boundary is `x = f(band, year)` — a frontier that arrives in some bands
  years before others (one-line story per line in the comment block). The same
  table ramps the outer envelope's fixed-year steps. Frontiers cannot cross: the
  page asserts ≥ 18 px between consecutive lines on every used row, bounds skew
  per region (≤ 3 yr and ≤ 30 % of span), and clamps jitter + wander to the
  actual local gap. `check_layout.py` now holds each region's drawn x-extent to
  the published `FRONTIER` (± YEAR_SLACK) and has a `frontiersNotDiagonal` gate
  (≥ 6 regions with ≥ 30 px arrival spread across band rows). Measured: 8 of 9
  mainland regions diagonal (the one-row plateau cannot be); formerly plumb
  seams now tilt 16–24°. All gates PASS. Next lever if still too rigid: let the
  Deep Learning Basin reach N2 (needs an ALTITUDES/REGISTRY decision).
- Render pass v8 (2026-09-07, "the funnel"): the mainland now has a GLOBAL
  outer envelope (`ENV` in `site/index.html`, documented in the comment block
  above it) — 2 half-band rows of land at the 1943 tip, 9 rows by 2022, with
  bays (the Winter Gulf 1974–82, the isthmus' southern bay 1998–2006) and a
  tilted north bank so the widening is irregular, not a cone. Regions are
  clipped to the envelope; the v5–v7 internal-border work lives inside it.
  `site/check_layout.py` gained `envelopeViol` (rendered land beyond ENV) and
  `notFunnel` (tip ≤150 px, max ≥3× tip, east-quarter mean ≥2× west-quarter).
  Rendered profile: 88 px at 1943 → 415 px at 2024 (4.7×).
- GitHub Actions warns that `actions/checkout@v4`, `configure-pages@v5`,
  `upload-pages-artifact@v3`, `deploy-pages@v4` target Node 20 (forced to
  Node 24); bump to the next majors when convenient — deploy is green as is.

## Ideas noted, NOT scope

- Street level via citation-graph projection (Phase 5+).
- Voice/copy-edit pass across research files (`SPEC.md` §6 item 8).
- Full render/frontend (Phase 4 of `PROJECT_PLAN.md`) — the `site/` prototype
  is a review aid, not the start of that work.
