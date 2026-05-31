---
name: post-impl-capture
type: mode-shift
description: Use after implementation ships — coordinates knowledge capture across .context/, KB, and docs layers.
model-invocable: true
---

# Post-Implementation Capture

After implementation ships, durable knowledge is scattered: decisions and
rejected alternatives in the session transcript, intent in the design
artifacts, and what actually shipped in the code. Capture it before the
transcript compacts and the reasoning evaporates.

This is your capture loop aimed at a shipped change. The base loop still holds —
fan out read-only investigators, write every layer inline, hand structure to
@kb-maintainer — with these implementation-specific moves.

## Mine the implementation session

Spawn @session-miner over the implementation session(s) for decisions, rejected
alternatives, and constraints that never reached the code or the artifacts.
Point them at the session(s) the caller identified.

## Diff intent against outcome

Read the work item's design artifacts (`requirements.md`, `design/`) for what was
*intended*, and the changed files for what was *built*. The delta is where
undocumented decisions hide — a dropped requirement, an added workaround, a
renamed boundary. When intent and outcome disagree, the human's decisions in the
session are canonical.

## Write every affected layer inline

Route each piece to where it belongs:

- modules with contract changes → `.context/CONTEXT.md` and `AGENTS.md`
- cross-cutting decisions, patterns, project-wide rationale → the KB
- user-visible behavior changes → `docs/`

Replace superseded claims instead of layering new text over stale.

## Check coverage before reporting

- Every module with a significant contract change documented?
- Cross-cutting decisions and rejected alternatives captured in the KB?
- User-visible changes reflected in `docs/`?

A gap that changes one of these targets earns another investigator wave — within
the base loop's three-wave cap. Past the cap, report the uncovered gap instead
of spawning more.

## Hand structure to @kb-maintainer

When the capture leaves a tree lopsided — oversized docs, walls of text, stale
cross-references — spawn one @kb-maintainer per writable tree you touched (one
target tree per spawn; other paths are read-only context) to rebalance the
hierarchy and fix references.
