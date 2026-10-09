# Monthly Refresh Guide (`map-of-ai`)

The **Map of AI — The 2036 Textbook Atlas** is architected so that monthly catalog updates (new frontier models, agent protocols, hardware summits, or archival citations) require **zero manual coordinate math**.

Every milestone's world position `(x, y)` is automatically derived at build time from:
1. Its **province (`country_id`)** and **decimal year (`year`)** inside `data/events/<continent>.yaml`.
2. The deterministic Voronoi-treemap province polygon and multi-scale collision solver in `site/atlas.html` (`placeLod()`).

---

## 1. Quick Status Check

To inspect current catalog totals and the 25 most recent milestones on the Eastern Frontier (`2025.0–Present`):

```bash
python3 scripts/refresh.py --status
```

---

## 2. Adding a New Milestone

### Option A: Via `scripts/refresh.py --add` (Recommended)

Run `scripts/refresh.py --add` with the target province ID, decimal year (`YYYY + (month - 1)/12`), LOD (`3` for Syllabus headline, `4` for Archive detail), a `<= 15`-word `one_line` summary, and a primary source citation:

```bash
python3 scripts/refresh.py --add \
  --country generative-ai-continent-transformers-foundation-models \
  --id gemini-4-5-ultra \
  --name "Gemini 4.5 Ultra" \
  --year 2026.9 \
  --lod 3 \
  --one-line "Native multi-hour autonomous verification and world-model synthesis" \
  --source-url "https://blog.google/technology/ai/" \
  --source-title "Google DeepMind 2026 — Gemini 4.5 Technical Report"
```

Common Eastern Frontier target provinces (`--country`):
- **Foundation Models & Frontier Launches**: `generative-ai-continent-transformers-foundation-models` (`data/events/generative-ai-continent.yaml`)
- **Alignment, Reasoning & Constitutional AI**: `generative-ai-continent-alignment-watershed` (`data/events/generative-ai-continent.yaml`)
- **Agentic Protocols, Coding Agents & Orchestration (`MCP`, `A2A`, `A2UI`, `AP2`, `UCP`, `ARD`, `Skills`, `Plugins`, `AX + Substrate`, `AAIF`)**: `generative-ai-continent-agentic-territories` (`data/events/generative-ai-continent.yaml`)
- **Diffusion, Flow & Video Generation**: `generative-ai-continent-diffusion-flow-highlands` (`data/events/generative-ai-continent.yaml`)
- **State-Space & Hybrid Sequence Models**: `generative-ai-continent-state-space-archipelago` (`data/events/generative-ai-continent.yaml`)
- **Frontier Open-Weight Releases (`Gemma`, `Llama`, `DeepSeek`)**: `deep-learning-mainland-representation-pretraining` (`data/events/deep-learning-mainland.yaml`)

### Option B: Direct YAML Edit

Edit the corresponding `data/events/<continent>.yaml` file directly. Every event entry follows this schema:

```yaml
      - id: gemini-4-argon
        name: Gemini 4 Argon
        year: 2026.3
        lod: 3
        one_line: Frontier reasoning and long-horizon autonomous coding architecture
        sources:
          - url: https://blog.google/technology/ai/
            title: Google DeepMind 2026 — Gemini 4 Argon Technical Release
```

**Schema Rules (`scripts/validate.py`)**:
1. `year` must fall within the parent province's `time_range.start` and `time_range.end` (provinces with `end: present` automatically accept dates up to `current_year + 1`).
2. `one_line` must be **15 words or fewer**.
3. `sources` must contain at least one `{url, title}` citation.

---

## 3. Rebuilding Tiles & Running All Verification Gates

After adding or updating entries, run the full build and verification pipeline:

```bash
uv run --with pillow --with playwright --with pyyaml python3 scripts/refresh.py --build
```

This executes four deterministic steps:
1. **`site/build_entities_json.py`**: Compiles `data/continents/*.yaml`, `data/countries/*.yaml`, `data/events/*.yaml`, and `data/threads/*.yaml` into `site/entities.json` and `site/entities.js`.
2. **`scripts/validate.py --offline --summary`**: Validates all 25 schema, temporal span, word-count, and citation rules (`0` failures required).
3. **`site/build_tiles.py`**: Launches headless Chromium on `site/atlas.html`, exports `site/labels.json` and `site/atlas_data.js`, and renders the 5-level multi-scale raster pyramid (`site/tiles/0..4`, including `8x` Syllabus tiles and `16x` Archive full-map tiles with finer terrain grain, topographic contours, town planimetry, and vellum readability wash).
4. **`site/check_layout.py` & `tests/sample_frames.py`**: Verifies all 30 cartographic layout invariants and all 100 mobile viewport density frames (`100/100` pass rate required).
