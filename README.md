# Map of AI: The 2036 Textbook Atlas

**Live interactive atlas:** [mapofai.dev](https://mapofai.dev) (mirror: [zeroasterisk.github.io/map-of-ai](https://zeroasterisk.github.io/map-of-ai/))  
**A2A Cartographer Agent:** [`https://agent.mapofai.dev`](https://agent.mapofai.dev) · **Agent Card:** [`https://agent.mapofai.dev/.well-known/agent-card.json`](https://agent.mapofai.dev/.well-known/agent-card.json) · **AI Catalog (ARD):** [`https://mapofai.dev/.well-known/ai-catalog.json`](https://mapofai.dev/.well-known/ai-catalog.json)

An interactive, antique-cartographic map of the history of artificial intelligence research (1666 to 2026), inspired by [mapofmetal.com](https://mapofmetal.com) and 19th-century Swiss topographic relief plates (Eduard Imhof hillshading and Lehmann slope hachures).

- West is old, East is now (`AXES.md` §1), spanning the Antecedent Isles (1666-1942) through the Transformer Plateau (2017-2022) and the Generative Coast (2022-present).
- North to South encodes research approach (`AXES.md` §3), placing formal and symbolic work in the north (`N1`/`N2`), language and agentic synthesis along the central band (`C`), and statistical, connectionist, and embodied schools in the south (`S1`/`S2`).
- Five semantic zoom altitudes (`Alt 0` through `Alt 4`, `z0` through `z4`) reveal detail progressively from World (`Alt 0`) to Regions (`Alt 1`), Provinces (`Alt 2`), Syllabus Milestones (`Alt 3`), and Archival Citations (`Alt 4`).

---

## Want a change made? Have your agent ask my agent

Manual GitHub Issues, Pull Requests, and Discussions are disabled on this repository. If you want to add a historical milestone, fix a citation or date, or suggest a lineage road, **have your AI agent ask the Map of AI Cartographer Agent for it** over the [Agent2Agent (A2A) protocol](https://a2a-protocol.org):

- **A2A Agent Host:** [`https://agent.mapofai.dev`](https://agent.mapofai.dev)
- **A2A Discovery Card:** [`https://agent.mapofai.dev/.well-known/agent-card.json`](https://agent.mapofai.dev/.well-known/agent-card.json)
- **AI Catalog & ARD Discovery (`v1.0` / `v0.5`):** [`https://mapofai.dev/.well-known/ai-catalog.json`](https://mapofai.dev/.well-known/ai-catalog.json) & [`https://agent.mapofai.dev/.well-known/ai-catalog.json`](https://agent.mapofai.dev/.well-known/ai-catalog.json)
- **A2A JSON-RPC Endpoint:** `https://agent.mapofai.dev/a2a` (supports both A2A `1.0` and `0.3`)
- **Authentication Scheme (`github_bearer`):** Agent Card (`/.well-known/agent-card.json`) and AI Catalog (`/.well-known/ai-catalog.json`) discovery are public. **All `POST /a2a` JSON-RPC calls** (catalog search, proposal staging, and `CONFIRM`) require a consistent upfront `Authorization: Bearer ghp_<REDACTED_GITHUB_TOKEN>` header with read-only `read:user` scope (GitHub account age `>= 30` days, max `3` PRs / 24h; zero repository write scopes required).

### Happy-Path Authentication Walkthrough (Consistent Upfront Auth)

Pass a single read-only GitHub token (`read:user` scope, e.g. `export GITHUB_TOKEN="ghp_<REDACTED_GITHUB_TOKEN>"` or `$(gh auth token)`) on all `POST /a2a` requests from Turn 1 through confirmation.

#### Option A: Using the Official [`a2a-cli`](https://github.com/a2aproject/a2a-cli)

```bash
# 1. Inspect the public Agent Card (unauthenticated discovery)
a2a card get https://agent.mapofai.dev

# 2. Configure a read-only `read:user` GitHub token (e.g. `$(gh auth token)`)
export GITHUB_TOKEN="ghp_<REDACTED_GITHUB_TOKEN>"

# 3. Turn 1: Propose and stage a milestone with a primary citation
#    Returns a Task in TASK_STATE_INPUT_REQUIRED (substate: proposal_staged_awaiting_confirmation)
a2a send -a https://agent.mapofai.dev -o json \
  --auth "Bearer ${GITHUB_TOKEN}" \
  'Propose adding "Direct Preference Optimization (DPO)" (2023) to alignment-safety with citation https://arxiv.org/abs/2305.18290'

# 4. Turn 2: Confirm the staged proposal to open a Pull Request on zeroasterisk/map-of-ai
a2a send -a https://agent.mapofai.dev \
  --task-id "<TASK_ID_FROM_TURN_1>" \
  --context-id "<CONTEXT_ID_FROM_TURN_1>" \
  --auth "Bearer ${GITHUB_TOKEN}" \
  "CONFIRM"
```

#### Option B: Using `curl` (A2A v1.0 JSON-RPC `SendMessage`)

```bash
export GITHUB_TOKEN="ghp_<REDACTED_GITHUB_TOKEN>"

# Turn 1: Stage the proposal and capture taskId + contextId
TURN1_JSON=$(curl -sS -X POST https://agent.mapofai.dev/a2a \
  -H "Content-Type: application/json" \
  -H "A2A-Version: 1.0" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  -d '{
    "jsonrpc": "2.0",
    "id": "turn-1",
    "method": "SendMessage",
    "params": {
      "message": {
        "messageId": "msg-turn-1",
        "role": "ROLE_USER",
        "parts": [
          {
            "text": "Propose adding \"Direct Preference Optimization (DPO)\" (2023) to alignment-safety with citation https://arxiv.org/abs/2305.18290"
          }
        ]
      }
    }
  }')

TASK_ID=$(echo "${TURN1_JSON}" | jq -r '.result.task.id')
CONTEXT_ID=$(echo "${TURN1_JSON}" | jq -r '.result.task.contextId')
echo "Staged task=${TASK_ID} context=${CONTEXT_ID}"

# Turn 2: Send CONFIRM to open the GitHub Pull Request
curl -sS -X POST https://agent.mapofai.dev/a2a \
  -H "Content-Type: application/json" \
  -H "A2A-Version: 1.0" \
  -H "Authorization: Bearer ${GITHUB_TOKEN}" \
  -d "{
    \"jsonrpc\": \"2.0\",
    \"id\": \"turn-2\",
    \"method\": \"SendMessage\",
    \"params\": {
      \"message\": {
        \"messageId\": \"msg-turn-2\",
        \"taskId\": \"${TASK_ID}\",
        \"contextId\": \"${CONTEXT_ID}\",
        \"role\": \"ROLE_USER\",
        \"parts\": [{\"text\": \"CONFIRM\"}]
      }
    }
  }" | jq .
```

#### Option C: Using the Python [`a2a-sdk`](https://github.com/a2aproject/a2a-python) (`httpx` + JSON-RPC)

```python
import asyncio
import uuid
import httpx

A2A_ENDPOINT = "https://agent.mapofai.dev/a2a"
GITHUB_TOKEN = "ghp_<REDACTED_GITHUB_TOKEN>"  # Only `read:user` scope required


async def propose_and_confirm() -> None:
    headers = {
        "A2A-Version": "1.0",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
    }
    async with httpx.AsyncClient(timeout=30.0, headers=headers) as client:
        # Turn 1: Stage candidate milestone proposal
        turn1 = await client.post(
            A2A_ENDPOINT,
            json={
                "jsonrpc": "2.0",
                "id": str(uuid.uuid4()),
                "method": "SendMessage",
                "params": {
                    "message": {
                        "messageId": str(uuid.uuid4()),
                        "role": "ROLE_USER",
                        "parts": [
                            {
                                "text": (
                                    'Propose adding "Direct Preference Optimization (DPO)" '
                                    "(2023) to alignment-safety with citation "
                                    "https://arxiv.org/abs/2305.18290"
                                )
                            }
                        ],
                    }
                },
            },
        )
        task = turn1.json()["result"]["task"]
        task_id, context_id = task["id"], task["contextId"]
        print(f"Turn 1 state: {task['status']['state']} (task_id={task_id})")

        # Turn 2: Confirm staged proposal to open the Pull Request
        turn2 = await client.post(
            A2A_ENDPOINT,
            json={
                "jsonrpc": "2.0",
                "id": str(uuid.uuid4()),
                "method": "SendMessage",
                "params": {
                    "message": {
                        "messageId": str(uuid.uuid4()),
                        "taskId": task_id,
                        "contextId": context_id,
                        "role": "ROLE_USER",
                        "parts": [{"text": "CONFIRM"}],
                    }
                },
            },
        )
        print("Turn 2 result:", turn2.json()["result"]["task"]["metadata"])


if __name__ == "__main__":
    asyncio.run(propose_and_confirm())
```

### Official A2A CLI & SDK Repositories

Build or connect your own agent using the official [Agent2Agent (A2A)](https://github.com/a2aproject/A2A) tools and SDKs:

- **A2A Protocol Specification:** [`a2aproject/A2A`](https://github.com/a2aproject/A2A) ([a2a-protocol.org](https://a2a-protocol.org))
- **A2A CLI (`a2a`):** [`a2aproject/a2a-cli`](https://github.com/a2aproject/a2a-cli) — Official command-line client (`card get`, `send`, `task get`, `task subscribe`)
- **A2A Inspector:** [`a2aproject/a2a-inspector`](https://github.com/a2aproject/a2a-inspector) — Interactive web inspector and validator for A2A agents
- **Official Language SDKs:**
  - **Python SDK (`a2a-sdk`):** [`a2aproject/a2a-python`](https://github.com/a2aproject/a2a-python)
  - **JavaScript / TypeScript SDK (`@a2a-js/sdk`):** [`a2aproject/a2a-js`](https://github.com/a2aproject/a2a-js)
  - **Go SDK (`a2a-go`):** [`a2aproject/a2a-go`](https://github.com/a2aproject/a2a-go)
  - **Java SDK (`a2a-java`):** [`a2aproject/a2a-java`](https://github.com/a2aproject/a2a-java)
  - **.NET / C# SDK (`a2a-dotnet`):** [`a2aproject/a2a-dotnet`](https://github.com/a2aproject/a2a-dotnet)
  - **Rust SDK (`a2a-rs`):** [`a2aproject/a2a-rs`](https://github.com/a2aproject/a2a-rs)
- **Agent Frameworks & Samples:** [Google Agent Development Kit (`google/adk-python`)](https://github.com/google/adk-python) · [`a2aproject/a2a-samples`](https://github.com/a2aproject/a2a-samples)

---

## How it works

### 1. The 2036 textbook dataset (10 continents, 49 provinces, 10 outlying islands, 517 landmarks)
Every major era from Leibniz's *De Arte Combinatoria* (1666) to modern open agentic protocols (`MCP`, `A2A`, `A2UI`, `AP2`, `AAIF`, `SKILL.md`, `UCP`, `Agent Plugins`, `AX`, `ARD`) and frontier models (`DeepSeek-R1`, `Gemini 2.5`, `Gemini 3`, `Gemini 4 Argon`, `Claude 4`, `Claude Opus 5.5`, `o3`, `GPT-5`, `OpenAI 6`, `Gemma 1-4`) is mapped with verified dates, authors, institutional hubs, 15 hardware summits along the Silicon Range, 27 alternative-paradigm landmarks across 10 outlying islands, and primary citations (`site/atlas_data.js`, `data/continents/REGISTRY.md`, `research/`).

### 2. Open Knowledge Format (OKF v0.2) LLM Wiki & 79 Lineage Post Roads
All 475 historical milestone nodes, 47 spatial provinces, and 79 West-to-East lineage roads (`10` primary trunks, `14` cross-province branches, and `55` thematic/lab spurs = `492` directed causal edges) are maintained as a self-contained **601-file Open Knowledge Format (OKF) v0.2 knowledge graph** in [`wiki/`](wiki/index.md) and compiled into the plate via [`scripts/compile_okf_roads.py`](scripts/compile_okf_roads.py). Every road is audited for historical, institutional, and causal accuracy so competing labs are never conflated. Hovering or clicking any milestone highlights its connected West/East lineage paths and lets you walk step-by-step along the road in the Citation Inspector.

### 3. 2D topographic elevation model and multi-scale copperplate micro-cartography
Instead of 2.5D cartoon mountain stamps, a Python Digital Elevation Model (`scripts/build_dem.py` and `drawThreads` in `site/atlas.html`) synthesizes an `1800x1050` float32 heightfield along the Silicon Range, producing 315-degree northwest Lambertian hillshading (`site/assets/textures/hillshade.png`), 5-band marching-squares hypsometric elevation contours (`site/data/contours.geojson`), and gradient-aligned Lehmann slope hachures (`site/data/hachures.geojson`). At higher zoom levels (`z=3` and `z=4`), raster biome textures give way to fine vector copperplate detail: woodcut trees, marsh reeds, alpine crags, engraved town rosettes, and star-citadel fortifications.

### 4. Subpixel cursor-locked zoom and world-anchored vector labels
To make zooming feel like Google Maps, `site/index.html` patches Leaflet 1.9.4's integer pixel rounding (`_getNewPixelOrigin`, `latLngToLayerPoint`, `_setZoomTransform`, and `_reset`) to preserve floating-point subpixel precision and replaces discrete wheel snapping with a continuous velocity-proportional wheel controller + post-zoom bounds helper. Scroll speed maps directly to zoom speed, stops on the exact frame you stop scrolling (`0 ms` coasting), and keeps the plate coordinate under your cursor locked across `z=-1.0..5.0`. All continent banners, province headers, outlying islands, and milestone pins live in world coordinates inside `.leaflet-labels-pane` so the GPU scales labels and terrain tiles together without lag.

---

## Run locally and verify

### Serve the map locally
No build step or external API keys are required:

```bash
python3 -m http.server -d site 8765
# Open http://localhost:8765/
```

### Run verification checks

Run the 100-frame mobile viewport density and collision test (`412x892` @ DPR 2 across `z0` through `z3`):

```bash
python3 tests/sample_frames.py
```

Run the OKF v0.2 knowledge graph compiler, registry, YAML schema, and SVG plate layout checks:

```bash
python3 scripts/compile_okf_roads.py
python3 scripts/check_registry.py
python3 scripts/validate.py --offline --summary
python3 site/check_layout.py
```

---

## Repository structure

| Path | Purpose |
|---|---|
| `site/index.html` | Self-contained interactive atlas (`Leaflet` continuous subpixel zoom + world-locked vector label engine + interactive road highlighting) |
| `site/atlas.html` | Master planimetric SVG plate renderer (shorelines, copperplate micro-cartography, 3-tier lineage post roads, 2D topographic DEM) |
| `wiki/` | 601-file **Open Knowledge Format (OKF) v0.2 LLM Wiki** (`wiki/index.md`, `wiki/roads/`, `wiki/provinces/`, `wiki/milestones/`) |
| `scripts/compile_okf_roads.py` | Compiles and validates the 79 OKF v0.2 lineage roads (`492` causal edges across `475` milestones) into `wiki/` and `site/atlas.html` |
| `scripts/refresh.py` | Monthly milestone refresh CLI (`--status`, `--add`, `--build`) with deterministic `(year, province, y_Hint)` placement |
| `site/atlas_data.js` | Complete compiled 2036 Textbook dataset (10 continents, 49 provinces, 10 outlying islands, 517 landmarks, 79 lineage roads) |
| `site/tiles/{0..4}/{x}/{y}.png` | 7,599 multi-scale pure-terrain & copperplate raster tiles (`z=0..4`: `40 / 135 / 493 / 1,881 / 5,050`, zero baked text) |
| `scripts/build_dem.py` | Synthesizes the `1800x1050` float32 DEM, hillshade, marching-squares contours, and Lehmann hachures |
| `site/build_tiles.py` | Renders the multi-scale pure-terrain tile pyramid from `site/atlas.html` and bundles `site/atlas_data.js` |
| `site/CNAME` | Custom domain configuration (`mapofai.dev`) for GitHub Pages |
| `tests/sample_frames.py` | Mobile viewport (`412x892` @ DPR 2) density, clipping, and overlap gate (`100/100` pass) |
| `docs/density/baseline.json` | Latest verified 100-frame sampler report (`100.0%` pass rate) |
| `docs/GTM_NARRATIVE_GEMINI4_ARGON.md` | Engineering field notes: how Gemini 4 Argon rescued the repo (`0% -> 100%`) plus post-review polish (OKF LLM Wiki, causal roads, tile cleanup) |
| `research/` | 9-part historical research compendium (1666 to 2026) with verified primary citations |
| `SPEC.md` / `AXES.md` / `ALTITUDES.md` | Cartographic specification, coordinate axes, and semantic zoom taxonomy |
