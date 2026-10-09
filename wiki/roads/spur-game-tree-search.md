---
type: Lineage Road
title: The Chess, Checkers & Monte Carlo Tree Search Spur
description: Traces game-tree search from Claude Shannon's minimax chess paper (1950), Strachey & Prinz's Ferranti draughts/chess
  programs (1951), and Arthur Samuel's IBM 701/704 checkers learning programs (1952–1959) through alpha-beta pruning (1961),
  Greenblatt's Mac Hack VI (1967), CMU's Deep Thought (1988), Jonathan Schaeffer's Chinook checkers (1992), and IBM Deep Blue
  defeating Kasparov (1997) to Kocsis & Szepesvári's UCT Monte Carlo Tree Search (2006) and DeepMind's AlphaGo defeating Fan
  Hui (2015).
road_id: spur-game-tree-search
road_tier: spur
stop_count: 11
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://vision.unipv.it/IA1/ProgrammingaComputerforPlayingChess.pdf
  title: Shannon 1950 [23]
- resource: https://en.wikipedia.org/wiki/Mac_Hack
  title: Greenblatt 1967 [24]
- resource: https://www.nature.com/articles/nature16961
  title: Silver et al., Nature 529 [46]
---

# The Chess, Checkers & Monte Carlo Tree Search Spur

**Road ID**: `spur-game-tree-search` · **Hierarchy Class**: `spur` · **Stops**: `11` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces game-tree search from Claude Shannon's minimax chess paper (1950), Strachey & Prinz's Ferranti draughts/chess programs (1951), and Arthur Samuel's IBM 701/704 checkers learning programs (1952–1959) through alpha-beta pruning (1961), Greenblatt's Mac Hack VI (1967), CMU's Deep Thought (1988), Jonathan Schaeffer's Chinook checkers (1992), and IBM Deep Blue defeating Kasparov (1997) to Kocsis & Szepesvári's UCT Monte Carlo Tree Search (2006) and DeepMind's AlphaGo defeating Fan Hui (2015).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Historical game-playing AI milestones with clear academic/published citations.
- **Reddit Test**: Shows how classical minimax/alpha-beta (`Shannon -> Samuel -> Deep Thought -> Chinook -> Deep Blue`) evolved into UCT MCTS (`uct-mcts-2006`), which directly combined with deep neural networks in AlphaGo (`fan-hui-2015`).
- **Individuals Involved Test**: Claude Shannon, Arthur Samuel, Feng-hsiung Hsu, Murray Campbell, Jonathan Schaeffer, Levente Kocsis, Csaba Szepesvári, and David Silver are linked in exact historical sequence.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `1950.2` | [Shannon Chess Minimax](/milestones/shannon-chess-minimax-1950.md) | [The Imitation Game & Game-Search Headland](/provinces/turing-test-headland.md) | Claude Shannon formulates minimax tree search and static evaluation for chess |
| 2 | `1951.7` | [Ferranti Mark 1 Games](/milestones/ferranti-draughts-chess-1951.md) | [The Imitation Game & Game-Search Headland](/provinces/turing-test-headland.md) | Strachey's draughts and Prinz's chess run on Manchester's Ferranti Mark 1 |
| 3 | `1952.8` | [Samuel IBM 701 Checkers](/milestones/samuel-ibm701-checkers-1952.md) | [The Imitation Game & Game-Search Headland](/provinces/turing-test-headland.md) | Arthur Samuel builds the first self-learning checkers program on the IBM 701 |
| 4 | `1959.5` | [Samuel Checkers](/milestones/samuel-checkers-1959.md) | [The Heuristic Search Highlands](/provinces/heuristic-search-highlands.md) | Arthur Samuel coins machine learning with self-playing checkers program |
| 5 | `1961.8` | [Alpha–Beta Pruning](/milestones/alpha-beta-pruning-1961.md) | [The Heuristic Search Highlands](/provinces/heuristic-search-highlands.md) | McCarthy, Brudno and Edwards formalize alpha–beta minimax game-tree pruning |
| 6 | `1967.3` | [Mac Hack VI](/milestones/mac-hack-chess-1967.md) | [The Heuristic Search Highlands](/provinces/heuristic-search-highlands.md) | Richard Greenblatt chess program becomes first to beat tournament humans |
| 7 | `1988.7` | [Deep Thought & HiTech](/milestones/deep-thought-chess-1988.md) | [The Cyc Ontology & Deep Thought Highlands](/provinces/fifth-generation-and-cyc-highlands.md) | CMU's HiTech and Deep Thought chess machines defeat grandmasters in tournament play |
| 8 | `1992.7` | [Chinook Checkers Match](/milestones/chinook-checkers-1992.md) | [The Cyc Ontology & Deep Thought Highlands](/provinces/fifth-generation-and-cyc-highlands.md) | Jonathan Schaeffer's Chinook challenges Marion Tinsley for the world checkers championship |
| 9 | `1997.36` | [Deep Blue vs. Kasparov](/milestones/deep-blue-kasparov-1997.md) | [The Statistical Corpus Basin](/provinces/statistical-corpus-basin.md) | IBM's Deep Blue defeats World Chess Champion Garry Kasparov 3.5–2.5 |
| 10 | `2006.4` | [UCT Monte Carlo Tree Search](/milestones/uct-mcts-2006.md) | [The Support Vector Escarpment](/provinces/support-vector-escarpment.md) | Kocsis and Szepesvári formulate UCT bandit tree search, transforming computer Go |
| 11 | `2015.8` | [Fan Hui 5–0](/milestones/fan-hui-2015.md) | [The AlphaGo Delta](/provinces/deep-rl-delta.md) | AlphaGo beats the European champion (Oct 2015; Nature, Jan 2016) |

## Directed Road Segments

- [Shannon Chess Minimax](/milestones/shannon-chess-minimax-1950.md) (`1950.2`) → [Ferranti Mark 1 Games](/milestones/ferranti-draughts-chess-1951.md) (`1951.7`)
- [Ferranti Mark 1 Games](/milestones/ferranti-draughts-chess-1951.md) (`1951.7`) → [Samuel IBM 701 Checkers](/milestones/samuel-ibm701-checkers-1952.md) (`1952.8`)
- [Samuel IBM 701 Checkers](/milestones/samuel-ibm701-checkers-1952.md) (`1952.8`) → [Samuel Checkers](/milestones/samuel-checkers-1959.md) (`1959.5`)
- [Samuel Checkers](/milestones/samuel-checkers-1959.md) (`1959.5`) → [Alpha–Beta Pruning](/milestones/alpha-beta-pruning-1961.md) (`1961.8`)
- [Alpha–Beta Pruning](/milestones/alpha-beta-pruning-1961.md) (`1961.8`) → [Mac Hack VI](/milestones/mac-hack-chess-1967.md) (`1967.3`)
- [Mac Hack VI](/milestones/mac-hack-chess-1967.md) (`1967.3`) → [Deep Thought & HiTech](/milestones/deep-thought-chess-1988.md) (`1988.7`)
- [Deep Thought & HiTech](/milestones/deep-thought-chess-1988.md) (`1988.7`) → [Chinook Checkers Match](/milestones/chinook-checkers-1992.md) (`1992.7`)
- [Chinook Checkers Match](/milestones/chinook-checkers-1992.md) (`1992.7`) → [Deep Blue vs. Kasparov](/milestones/deep-blue-kasparov-1997.md) (`1997.36`)
- [Deep Blue vs. Kasparov](/milestones/deep-blue-kasparov-1997.md) (`1997.36`) → [UCT Monte Carlo Tree Search](/milestones/uct-mcts-2006.md) (`2006.4`)
- [UCT Monte Carlo Tree Search](/milestones/uct-mcts-2006.md) (`2006.4`) → [Fan Hui 5–0](/milestones/fan-hui-2015.md) (`2015.8`)
