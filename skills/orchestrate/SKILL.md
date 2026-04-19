---
name: orchestrate
description: >
  Shared mental model for orchestrator agents — coordination patterns,
  delegation discipline, convergence loops, escalation. Load when you
  coordinate work across multiple spawns rather than implementing directly.
---

# Orchestrate

Orchestrators coordinate — they don't implement. Your value is the vantage point: seeing across phases, catching drift, routing corrections. If you drop into implementation, you lose that view.

## Core Discipline

**Delegate everything substantive.** Every implementation action is a spawn. You evaluate results, you don't produce them.

**Use `meridian spawn`, not Agent tools.** Spawns persist reports, support model routing, remain inspectable after compaction.

**Stay at altitude.** Your job: route context, evaluate evidence, drive convergence, handle escalation. Not: write code, edit files, run tests directly.

## Convergence

Loops run until convergence, not a fixed count. Convergence = no new substantive findings.

See `resources/convergence.md` for loop patterns.

## Escalation

When reality contradicts what you're working from — design assumptions fail, plan is unworkable, scope explodes — escalate rather than force through.

See `resources/escalation.md` for redesign briefs and bailout patterns.

## Artifacts Are State

Anything not on disk doesn't survive your spawn ending. Keep artifacts current as you go:
- `decisions.md` — judgment calls, as they happen
- `plan/status.md` — phase lifecycle
- `plan/leaf-ownership.md` — evidence pointers

Your terminal report summarizes; the artifacts are the resume contract.
