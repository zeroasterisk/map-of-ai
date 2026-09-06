# Map of AI

A cartographic map of the history and present of AI research, in the spirit
of [mapofmetal.com](https://mapofmetal.com). West is old, east is now; the
north–south axis and the terrain encode what kind of work something is, so
that related schools of thought sit next to each other. Zoom from continents
(eras) to countries (schools) to cities (labs, landmark systems and papers) to
streets (people, papers, models). Updated monthly at the eastern edge.

Status: research and design phase. No renderer yet.

| Read this | For |
|---|---|
| `BRIEF.md` | the founding intent (verbatim) |
| `PROJECT_PLAN.md` | phases, milestones, open decisions, risks |
| `AXES.md` | X origin and scale; Y-axis candidates and recommendation |
| `ALTITUDES.md` | zoom levels, entity types, data model sketch |
| `SOURCING.md` | how the last 12 months get sourced and verified, monthly |
| `research/` | the compendium: one file per era plus cross-cutting threads |
| `STATUS.md` | what is done, what is draft, what needs a decision |

Tooling: `scripts/check_links.sh research/*.md` verifies every cited URL;
`scripts/wiki.sh Article_Title` fetches Wikipedia plaintext for fact-checking.
