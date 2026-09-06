# Map of AI

A cartographic map of the history and present of AI research, in the spirit
of [mapofmetal.com](https://mapofmetal.com). West is old, east is now; the
north–south axis and the terrain encode what kind of work something is, so
that related schools of thought sit next to each other. Zoom from continents
(eras) to countries (schools) to cities (labs, landmark systems, papers,
events and major people). Updated monthly at the eastern edge.

Status: framework decided, spec and plan written, awaiting go-ahead to
execute. No `data/` entities and no renderer yet.

| Read this | For |
|---|---|
| `BRIEF.md` | the founding intent (verbatim) |
| `SPEC.md` | **normative**: entity schema, validation rules, acceptance criteria, definition of done |
| `PLAN.md` | decomposed units of work with IDs, inputs, outputs, checks, dependencies |
| `AXES.md` | X origin and scale; Y axis (decided) and why |
| `ALTITUDES.md` | the three zoom levels and their entity types (decided) |
| `SOURCING.md` | how the last 12 months get sourced and verified, monthly |
| `research/` | the compendium: one file per era plus cross-cutting threads |
| `STATUS.md` | what is done, what is decided, what happens next |
| `PROJECT_PLAN.md` | original plan; goal/risks still valid, task list superseded by `PLAN.md` |

Tooling: `scripts/check_links.sh research/*.md` verifies every cited URL;
`scripts/wiki.sh Article_Title` fetches Wikipedia plaintext for fact-checking.
