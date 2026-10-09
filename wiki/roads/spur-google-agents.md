---
type: Lineage Road
title: The Google ADK, Gemini CLI & A2UI Agent Spur
description: Traces Google's agentic developer platform from Gemini 2.0 Flash (Dec 2024) to the Agent2Agent (A2A) protocol
  and Agent Development Kit (ADK) at Cloud Next (Apr 2025), Gemini CLI (Jun 2025), and A2UI generative UI protocol (Oct 2025).
road_id: spur-google-agents
road_tier: spur
stop_count: 4
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/
  title: Google DeepMind, Introducing Gemini 2.0, 11 Dec 2024 [45]
- resource: https://github.com/google/adk-python
  title: Google ADK (GitHub) [96]
- resource: https://github.com/google-gemini/gemini-cli
  title: Google Gemini CLI (GitHub) [96]
- resource: https://a2ui.org
  title: A2UI Protocol Specification (a2ui.org) [96]
- resource: https://github.com/a2ui-project/a2ui
  title: a2ui-project/a2ui (GitHub) [96]
---

# The Google ADK, Gemini CLI & A2UI Agent Spur

**Road ID**: `spur-google-agents` · **Hierarchy Class**: `spur` · **Stops**: `4` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces Google's agentic developer platform from Gemini 2.0 Flash (Dec 2024) to the Agent2Agent (A2A) protocol and Agent Development Kit (ADK) at Cloud Next (Apr 2025), Gemini CLI (Jun 2025), and A2UI generative UI protocol (Oct 2025).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: 100% Google Cloud / Google DeepMind agentic platform lineage.
- **Reddit Test**: Connects `gemini20-flash -> a2a-protocol -> adk-gemini-cli -> a2ui-protocol` without crossing into Anthropic's Claude Code.
- **Individuals Involved Test**: Google Cloud and Gemini CLI/ADK engineers are connected exclusively to Google's agentic stack.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2024.94` | [Gemini 2.0 Flash](/milestones/gemini20-flash-2024.md) | [The Closed Frontier](/provinces/closed-frontier-labs.md) | Google ships Gemini 2.0 Flash (11 Dec 2024) built for the agentic era |
| 2 | `2025.27` | [A2A Protocol](/milestones/a2a-protocol-2025.md) | [The Agents Causeway](/provinces/agents-tooling-coast.md) | Google Cloud and 50+ partners launch Agent2Agent (A2A) protocol (9 Apr 2025) for agent interop |
| 3 | `2025.48` | [ADK · Gemini CLI](/milestones/adk-gemini-cli-2025.md) | [The Agents Causeway](/provinces/agents-tooling-coast.md) | Google open-sources Agent Development Kit (Apr 2025) and Gemini CLI (25 Jun 2025) |
| 4 | `2025.82` | [A2UI Protocol](/milestones/a2ui-protocol-2025.md) | [The Agents Causeway](/provinces/agents-tooling-coast.md) | Agent-to-UI (A2UI) protocol decouples agent component trees from live client data models |

## Directed Road Segments

- [Gemini 2.0 Flash](/milestones/gemini20-flash-2024.md) (`2024.94`) → [A2A Protocol](/milestones/a2a-protocol-2025.md) (`2025.27`)
- [A2A Protocol](/milestones/a2a-protocol-2025.md) (`2025.27`) → [ADK · Gemini CLI](/milestones/adk-gemini-cli-2025.md) (`2025.48`)
- [ADK · Gemini CLI](/milestones/adk-gemini-cli-2025.md) (`2025.48`) → [A2UI Protocol](/milestones/a2ui-protocol-2025.md) (`2025.82`)
