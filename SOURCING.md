# SOURCING — keeping the east edge of the map current

> Status: proposal. Endpoint availability below was probed with curl on
> 2026-09-06 from this environment (status codes noted). Re-probe before
> automating; feeds move.

## 0. The problem

West of ~12 months ago, Wikipedia plus primary papers are reliable and the
compendium in `research/` uses them. East of that, Wikipedia lags, lab blogs
are press releases, and social media is fast but wrong. The map updates
monthly, so we need a repeatable intake that (a) doesn't miss the things that
will matter in two years and (b) doesn't fill the coastline with things that
won't.

Guiding rule: **the map records what changed the field, not what was
announced.** A monthly intake should produce very few A3 cities and a
moderate number of provisional A4 streets, most of which will be pruned.

## 1. Source tiers

### Tier 1 — Primary (what happened, from the people who did it)

| Source | Access | Probe | Use |
|---|---|---|---|
| arXiv new listings cs.AI, cs.LG, cs.CL, cs.CV, cs.RO | RSS `https://rss.arxiv.org/rss/cs.AI+cs.LG+cs.CL`; API `https://export.arxiv.org/api/query?search_query=cat:cs.LG&...` | 200 | volume is ~1,000+/day; only useful with a filter (see §3) |
| arXiv listing page | `https://arxiv.org/list/cs.AI/new` | 200 | manual skim |
| OpenAI news | RSS `https://openai.com/news/rss.xml` (HTML pages 403 to bots) | 200 | model/product releases |
| Google DeepMind blog | RSS `https://deepmind.google/blog/rss.xml` | 200 | model/research releases |
| Google Research blog | RSS `https://research.google/blog/rss/`; `https://blog.google/technology/ai/rss/` | 200 | |
| Anthropic news | HTML `https://www.anthropic.com/news` (no RSS found) | 200 | scrape or manual |
| Meta AI blog | HTML `https://ai.meta.com/blog/` (RSS path 404) | 200 | Llama releases |
| Mistral | HTML `https://mistral.ai/news` | 200 | |
| Qwen (Alibaba) | `https://qwenlm.github.io/blog/` | 200 | |
| DeepSeek | GitHub org + arXiv (no blog feed) | | technical reports land on arXiv |
| xAI | HTML `https://x.ai/news` | 403 to curl | manual |
| Microsoft Research | feed 403 to curl | 403 | manual |
| Hugging Face Daily Papers | API `https://huggingface.co/api/daily_papers?limit=N` | 200 | community-curated arXiv shortlist; best single high-signal feed for papers |
| Conference proceedings | `https://papers.nips.cc/`, `https://neurips.cc/virtual/<year>/papers.html`, `https://icml.cc/virtual/<year>/papers.html`, ICLR via OpenReview (API 403 to curl; browser works) | 200/403 | award papers and orals only; the map does not track accepted-paper volume |
| Model/system cards, technical reports | linked from the above | | authoritative for capabilities and dates |
| GitHub | `https://api.github.com/search/repositories?...` | 200 | star velocity for tools/frameworks/agents |

### Tier 2 — Curated secondary (what mattered, in the judgement of people who read everything)

| Source | Access | Probe | Notes |
|---|---|---|---|
| Import AI (Jack Clark) | `https://importai.substack.com/feed`, `https://jack-clark.net/feed/` | 200 | weekly, policy + research, since 2016 |
| The Batch (deeplearning.ai) | `https://www.deeplearning.ai/the-batch/` | 200 | weekly, mainstream |
| Interconnects (Nathan Lambert) | `https://www.interconnects.ai/feed` | 200 | open models, RLHF, post-training |
| Simon Willison | `https://simonwillison.net/atom/everything/` | 200 | tooling, agents, practical LLM use |
| AI News (Latent Space / smol.ai) | `https://news.smol.ai/` | | daily digest of Discord/X/Reddit |
| Language Models & Co (Jay Alammar) | `https://newsletter.languagemodels.co/feed` | 200 | |
| LessWrong / Alignment Forum | `https://www.lesswrong.com/feed.xml` | 200 | safety/alignment discourse |
| Hacker News | `https://hn.algolia.com/api/v1/search?query=...&tags=story` | 200 | attention signal, not authority |
| Epoch AI notable models DB | `https://epoch.ai/data/notable-ai-models` | 200 | compute, params, dates for major models; downloadable CSV |
| LMArena leaderboard | `https://lmarena.ai/leaderboard` | 200 | human-preference ranking; useful for "did this model matter" |
| Papers with Code | status uncertain in 2026; check before relying on it | | historically SOTA tables |
| Semantic Scholar API | `https://api.semanticscholar.org/graph/v1/paper/arXiv:<id>?fields=citationCount` | 429 without key; get a free API key | citation velocity for 3–12-month-old papers |
| OpenAlex | `https://api.openalex.org/works?...` | 200, no key | citation counts, author/institution metadata; open |
| Crossref | `https://api.crossref.org/works/<doi>` | 200 | DOI → title/venue/date verification |

### Tier 3 — Annual retrospectives (what still mattered a year later)

| Source | Cadence | Use |
|---|---|---|
| State of AI Report (Benaich/Hogarth) `https://www.stateof.ai/` | Oct | promote/prune decisions |
| Stanford AI Index `https://aiindex.stanford.edu/report/` | Apr | numbers, adoption, policy |
| NeurIPS/ICML/ICLR test-of-time and best-paper awards | with each conference | strongest signal for A3 promotion |
| Wikipedia "20XX in artificial intelligence" and model articles | continuous | when Wikipedia has a stable article, the item is out of the frontier zone |

## 2. Monthly cadence

Run in the first week of each month for the previous calendar month.

1. **Collect** (automatable, ~1 hour compute): pull Tier 1 RSS/API feeds for
   the month; pull HF Daily Papers; pull Tier 2 newsletters; dump to
   `intake/YYYY-MM/raw.jsonl`.
2. **Filter** (§3) to a candidate list of 30–80 items.
3. **Triangulate** (§4) each candidate; drop anything with fewer than two
   independent sources.
4. **Classify** each survivor: entity type (model / paper / tool / event /
   lab), Y band, biome, A2 parent, thread(s). Write to
   `research/frontier/YYYY-MM.md` using the template in §6 and, once the data
   model exists, to `data/` entries with `status: provisional`.
5. **Review** by Alan (or a second model pass with a different model): 15
   minutes, veto/add.
6. **Age the frontier**: revisit items from 6 and 12 months ago. Promote to A3
   (`status: verified`) if they pass §5, otherwise leave at A4 or prune.
7. **Commit** with message `frontier: YYYY-MM`. Move the east edge.

Automation note: steps 1–2 and the triangulation lookups in 3 are a good fit
for a scheduled agent job; steps 4–6 need judgement and should stay a
human-in-the-loop model pass.

## 3. Filters (what earns a look)

An item enters the candidate list if it hits at least one:

- Appears in ≥2 Tier-2 curators in the same month.
- HF Daily Papers with ≥ ~50 upvotes, or Semantic Scholar/OpenAlex citation
  count in the top 1% for its age.
- A Tier-1 lab release with a technical report or model card (not a pricing or
  feature announcement).
- A best-paper/oral at NeurIPS/ICML/ICLR/ACL/CVPR/ICRA.
- Top-10 on LMArena or a comparable benchmark leaderboard at any point in the
  month.
- A tool/framework/protocol crossing a GitHub-star or adoption threshold
  (e.g. 10k stars in <90 days) or adopted by ≥2 major labs (the MCP pattern).
- A policy/governance event with primary text (act, executive order, summit
  declaration, major lawsuit ruling).

Explicitly excluded: funding rounds, valuations, hires and departures,
pricing changes, minor version bumps, benchmark claims without a report,
demos without weights or API access.

## 4. Triangulation before writing anything

For each candidate record:

| Field | Requirement |
|---|---|
| Date | primary source (arXiv v1 date, blog post date, release notes). Never a tweet. |
| Who | authors/org from the primary artifact, not from coverage |
| Claim | one sentence of what it did, in the primary source's own words; benchmark numbers only from the report or an independent evaluation |
| Independent confirmation | ≥1 Tier-2 source or an independent eval (LMArena, Epoch, an academic replication) |
| Wikipedia status | `none` / `stub` / `stable` — recorded so aging (§5) is mechanical |
| Confidence | `high` (primary + independent + Wikipedia stable), `medium` (primary + independent), `low` (primary only) |

Items with `low` confidence render with frontier haze and no permanent label.

## 5. Promotion from provisional to verified (aging)

At 6 and 12 months, an item is promoted from A4 provisional to A3 verified if
it meets two of:

- Wikipedia article exists and is stable (not flagged, >6 months old).
- Cited ≥100 times (OpenAlex or Semantic Scholar) or referenced by ≥3
  subsequent Tier-1 releases.
- Appears in State of AI / AI Index / a conference retrospective.
- Still in production use or still on a top leaderboard.

Otherwise it stays A4 (visible only at street zoom) or is pruned if it has no
remaining independent coverage. Pruned items are kept in
`research/frontier/pruned.md` with the reason, so the same thing isn't
re-evaluated next year.

## 6. Frontier file template

`research/frontier/YYYY-MM.md`:

```
# Frontier intake — YYYY-MM
Collected: <date>   Reviewed by: <name/model>   Sources pulled: <list>

## Promoted to A3 this month (rare)
- ...

## New provisional A4 entries
| Date | Item | Type | Band | A2 parent | Threads | Primary | Independent | Confidence |
|------|------|------|------|-----------|---------|---------|-------------|------------|

## Aging review (items from YYYY-MM minus 6 / minus 12)
| Item | Decision | Reason |

## Pruned
| Item | Reason |

## Notes / things to watch
```

## 7. What Wikipedia is still good for at the frontier

- Its "20XX in artificial intelligence" and per-model articles are usually
  created within days of a major release; they are a decent *index* even when
  the prose is thin. Track article *existence and stability* as a signal
  (§4), not as a source of facts.
- Its talk pages surface disputes about dates and claims early.

## 8. Known gaps

- Chinese-language sources (WeChat posts from Chinese labs, Zhihu) are
  under-covered by the feeds above; Qwen/DeepSeek/Moonshot/Zhipu releases
  often appear on arXiv and GitHub first, which is covered, but commentary is
  not. Candidate: add a Chinese-ecosystem newsletter (ChinAI) to Tier 2.
- Robotics and embodied AI move through ICRA/CoRL/RSS and company blogs
  (Boston Dynamics, Figure, Physical Intelligence, 1X) rather than the LLM
  feeds; add `cs.RO` and CoRL proceedings explicitly.
- Anthropic, Meta, xAI, Microsoft have no working RSS for bots; these need a
  scraper or a manual check.
