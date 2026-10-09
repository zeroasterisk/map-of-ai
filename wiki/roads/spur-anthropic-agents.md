---
type: Lineage Road
title: The Anthropic Claude Code & Cowork Agent Spur
description: Traces Anthropic's agentic product and open standard contributions from Claude 3.5 Computer Use (Oct 2024) and
  Model Context Protocol (MCP, Nov 2024) through Claude Code (Feb 2025), Agent Skills / SKILL.md (Dec 2025), Claude Cowork
  (Jan 2026), and Agent Plugins (Mar 2026).
road_id: spur-anthropic-agents
road_tier: spur
stop_count: 6
status: active
generated:
  by: gemini-4-argon/1.0
  at: '2026-10-08T20:15:00Z'
verified:
- by: human:zeroasterisk
  at: '2026-10-08T20:15:00Z'
sources:
- resource: https://www.anthropic.com/news/3-5-models-and-computer-use
  title: Anthropic, Introducing computer use, 22 Oct 2024 [15]
- resource: https://agentskills.io
  title: Agent Skills Specification (agentskills.io) [97]
- resource: https://github.com/google/agent-plugins
  title: Agent Plugins Specification (github.com/google/agent-plugins) [97]
---

# The Anthropic Claude Code & Cowork Agent Spur

**Road ID**: `spur-anthropic-agents` · **Hierarchy Class**: `spur` · **Stops**: `6` · [Back to Roads Index](/roads/index.md)

## Historical & Architectural Rationale

Traces Anthropic's agentic product and open standard contributions from Claude 3.5 Computer Use (Oct 2024) and Model Context Protocol (MCP, Nov 2024) through Claude Code (Feb 2025), Agent Skills / SKILL.md (Dec 2025), Claude Cowork (Jan 2026), and Agent Plugins (Mar 2026).

## 3-Test Knowledge Graph Audit

- **Lawyer Test**: Pure Anthropic agentic product & open-spec lineage; never routes through Google ADK/Gemini CLI or OpenAI Operator.
- **Reddit Test**: Matches how developers actually experienced Anthropic's agentic stack: `Computer Use -> MCP -> Claude Code -> SKILL.md -> Cowork -> Plugins`.
- **Individuals Involved Test**: Anthropic's Claude Code, MCP, and Cowork engineering teams are linked along their own releases.

## Ordered Milestone Stops (West → East)

| # | Year | Milestone | Province | One-Line Summary |
|---|------|-----------|----------|------------------|
| 1 | `2024.81` | [computer use](/milestones/computer-use-2024.md) | [The Agents Causeway](/provinces/agents-tooling-coast.md) | Anthropic's Claude 3.5 Sonnet drives a desktop via screenshots and clicks (22 Oct 2024) |
| 2 | `2024.9` | [MCP](/milestones/mcp-2024.md) | [The Agents Causeway](/provinces/agents-tooling-coast.md) | Anthropic open-sources the Model Context Protocol (25 Nov 2024): standard plumbing for tool-using agents |
| 3 | `2025.12` | [Claude Code](/milestones/claude-code-2025.md) | [The Agents Causeway](/provinces/agents-tooling-coast.md) | Anthropic's terminal coding agent (Feb 2025); Karpathy coins "vibe coding" |
| 4 | `2025.97` | [Agent Skills (SKILL.md)](/milestones/agent-skills-2025.md) | [The Agents Causeway](/provinces/agents-tooling-coast.md) | Agent Skills specification standardizes portable SKILL.md procedural knowledge packages across agents |
| 5 | `2026.03` | [Claude Cowork](/milestones/cowork-2026.md) | [The Agents Causeway](/provinces/agents-tooling-coast.md) | Claude Cowork (12 Jan 2026): Claude Code's agent loop for non-coding knowledge work |
| 6 | `2026.18` | [Agent Plugins](/milestones/agent-plugins-2026.md) | [The Agents Causeway](/provinces/agents-tooling-coast.md) | Agent Plugins v1.0 bundles skills, MCP servers, subagents, and hooks into portable manifests |

## Directed Road Segments

- [computer use](/milestones/computer-use-2024.md) (`2024.81`) → [MCP](/milestones/mcp-2024.md) (`2024.9`)
- [MCP](/milestones/mcp-2024.md) (`2024.9`) → [Claude Code](/milestones/claude-code-2025.md) (`2025.12`)
- [Claude Code](/milestones/claude-code-2025.md) (`2025.12`) → [Agent Skills (SKILL.md)](/milestones/agent-skills-2025.md) (`2025.97`)
- [Agent Skills (SKILL.md)](/milestones/agent-skills-2025.md) (`2025.97`) → [Claude Cowork](/milestones/cowork-2026.md) (`2026.03`)
- [Claude Cowork](/milestones/cowork-2026.md) (`2026.03`) → [Agent Plugins](/milestones/agent-plugins-2026.md) (`2026.18`)
