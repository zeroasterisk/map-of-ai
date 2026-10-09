---
type: Lineage Road
title: The Situation Calculus, QA3 & Planner/Actor Formalisms Spur
description: Traces logical action formalisms and procedural deduction from Robinson's Resolution Principle (1965) to Cordell
  Green's QA3 resolution theorem-proving planner (1969), McCarthy & Hayes's Situation Calculus (1969), Colmerauer's Prolog
  (1972), and Carl Hewitt's Planner & Actor model of concurrent computation (1973).
road_id: spur-situation-calculus-actors
road_tier: spur
stop_count: 5
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://doi.org/10.1145/321250.321253
  title: Robinson 1965 [16]
- resource: http://www-formal.stanford.edu/jmc/mcchay69.pdf
  title: McCarthy & Hayes 1969 [27]
- resource: https://www.ijcai.org/Proceedings/73/Papers/027B.pdf
  title: Hewitt, Bishop & Steiger, IJCAI 1973 [32]
---

# The Situation Calculus, QA3 & Planner/Actor Formalisms Spur

**Road ID**: `spur-situation-calculus-actors` · **Hierarchy Class**: `spur` · **Stops**: `5` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces logical action formalisms and procedural deduction from Robinson's Resolution Principle (1965) to Cordell Green's QA3 resolution theorem-proving planner (1969), McCarthy & Hayes's Situation Calculus (1969), Colmerauer's Prolog (1972), and Carl Hewitt's Planner & Actor model of concurrent computation (1973).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Academic Stanford, SRI, Marseille, and MIT publications.
- **Reddit Test**: Captures the classic Stanford/SRI declarative theorem-proving (`Resolution -> QA3 -> Situation Calculus -> Prolog`) vs MIT procedural (`Planner/Actors`) debate.
- **Individuals Involved Test**: Alan Robinson, Cordell Green, John McCarthy, Pat Hayes, Alain Colmerauer, and Carl Hewitt are linked across the exact papers that debated declarative vs procedural deduction.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `1965.1` | [Resolution Principle](/milestones/resolution-principle-1965.md) | [The Logic & Representation Plateau](/provinces/logic-representation-plateau.md) | J. Alan Robinson discovers single refutation-complete rule for predicate logic |
| 2 | `1969.4` | [QA3 Question Answering](/milestones/qa3-deduction-1969.md) | [The Logic & Representation Plateau](/provinces/logic-representation-plateau.md) | Bertram Raphael and Cordell Green demonstrate first-order deductive retrieval |
| 3 | `1969.8` | [Situation Calculus](/milestones/mccarthy-situations-fluents-1969.md) | [The Logic & Representation Plateau](/provinces/logic-representation-plateau.md) | McCarthy and Hayes introduce the Situation Calculus and formulate the Frame Problem |
| 4 | `1972.4` | [Prolog Created](/milestones/prolog-creation-1972.md) | [The Logic & Representation Plateau](/provinces/logic-representation-plateau.md) | Colmerauer & Roussel create Prolog with Kowalski Horn-clause logic |
| 5 | `1973.6` | [Actor Model](/milestones/hewitt-planner-actors-1973.md) | [The Logic & Representation Plateau](/provinces/logic-representation-plateau.md) | Carl Hewitt introduces the Actor Model of concurrent distributed artificial intelligence |

## Directed Road Segments

- [Resolution Principle](/milestones/resolution-principle-1965.md) (`1965.1`) → [QA3 Question Answering](/milestones/qa3-deduction-1969.md) (`1969.4`)
- [QA3 Question Answering](/milestones/qa3-deduction-1969.md) (`1969.4`) → [Situation Calculus](/milestones/mccarthy-situations-fluents-1969.md) (`1969.8`)
- [Situation Calculus](/milestones/mccarthy-situations-fluents-1969.md) (`1969.8`) → [Prolog Created](/milestones/prolog-creation-1972.md) (`1972.4`)
- [Prolog Created](/milestones/prolog-creation-1972.md) (`1972.4`) → [Actor Model](/milestones/hewitt-planner-actors-1973.md) (`1973.6`)
