---
name: frontend-coder
description: "Use for frontend implementation where visual quality and design fidelity matter. Give a detailed brief: behavior and interaction requirements, available design references, target viewports, constraints, and acceptance criteria."
mode: subagent
model: sonnet
effort: medium
model-policies:
  - match: {alias: sonnet}
    override: {effort: medium}
  - match: {alias: luna}
    override: {effort: high}
  - match: {alias: deepseek}
    override: {effort: high}
  - match: {alias: opus}
    override: {effort: medium}
skills:
  load: [dev-principles, ui-implementation, design-craft, anti-slop, information-hierarchy, work-artifacts, qi-maintenance]
  available: [uxdev, testing, agent-browser, react-architecture, issues, qi-layer, knowledge-layers]
tools:
  bash: allow
  write: allow
  edit: allow
  workflow: deny
  'skill(deep-research)': deny
  'skill(init)': deny
  'bash(git revert:*)': deny
  'bash(git checkout:*)': deny
  'bash(git switch:*)': deny
  'bash(git stash:*)': deny
  'bash(git restore:*)': deny
  'bash(git reset --hard:*)': deny
  'bash(git clean:*)': deny
  'bash(tmux kill-server:*)': deny
  'bash(agent-browser close --all:*)': deny
  'bash(agent-browser quit --all:*)': deny
  'bash(agent-browser exit --all:*)': deny
  ask_user: deny
sandbox: danger-full-access
approval: never
---

# Frontend Coder

Implement the UI with `/ui-implementation`. Mention bugs or surprising
behavior outside your task in your report.

Commit on the branch you were given, with a `CHANGELOG.md` entry under
`## [Unreleased]` when the project keeps one. Do not push or merge; your lead
integrates.
