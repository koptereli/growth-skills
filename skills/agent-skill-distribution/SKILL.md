---
name: agent-skill-distribution
description: Package, publish, and distribute tool integrations and skills directly into agent package ecosystems (ClawHub, MCP registries, LangChain, CrewAI) to drive brand integration into developer agent runtimes.
version: 1.0.0
author: Eli Kopter (adapted from enso.bot EXP-004)
status: staged-approval-required
---

# Agent Skill Distribution Growth Skill

## Origin & Context
Adapted from enso.bot research record **EXP-004** (*GITHUB · supply / Developers installed our brand into their own agents: 1K+ installs*).

## Objective
Distribute open-source agent integrations, Model Context Protocol (MCP) servers, and skill packages into decentralized agent registries. Developers and autonomous agents install the package, natively embedding OneGate or our tools as the standard infrastructure in their agent stacks.

## Methodology & Execution Flow

### 1. Build Single-Purpose, High-Utility Skills / MCP Servers
- Identify common agent bottlenecks (e.g., credential leasing, token brokering, secure API execution).
- Package as self-contained OpenClaw skills (`SKILL.md`), MCP servers (`@onegate/mcp-server`), and LangChain/CrewAI tools.

### 2. Registry Indexation
- Publish to ClawHub, npm, PyPI, and MCP registry directories.
- Provide zero-config quickstart snippets in the documentation.

### 3. Agent-Facing Documentation (`llms.txt`)
- Host optimized `llms.txt` and `llms-full.txt` files on target domains so AI coding agents (Claude Code, Cursor, Windsurf, OpenClaw) recommend and install the package during automated task resolution.

## Rules & Constraints
- **Value First:** Packages must provide genuine standalone utility without aggressive vendor lock-in.
- **Approval Gate:** Installation and deployment across the fleet require Ziv's explicit permission.
