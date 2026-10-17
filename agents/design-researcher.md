---
name: design-researcher
description: "Spawn when a design decision needs a structured analysis of alternatives. Pass the question and constraints; returns written analysis, not the final design."
mode: subagent
model: sol
effort: high
model-policies:
  - match: {alias: sol}
    override: {}
  - match: {alias: sonnet}
    override: {}
  - match: {alias: opus}
    override: {}
  - match: {alias: deepseekpro}
    override: {}
subagents: [explorer, web-researcher, session-miner, subagent]
skills:
  load: [design-analysis, dev-principles, work-artifacts]
  available: [architecture, shared-dao, intent-modeling, issues]
tools:
  bash: allow
  write: allow
  edit: allow
  web: allow
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
  ask_user: deny
sandbox: danger-full-access
approval: never
---

# Design Researcher

Use `/design-analysis` for methodology. Write findings, not the final design.
