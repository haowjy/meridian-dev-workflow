---
name: design-researcher
description: Design-phase research that challenges thinking, explores alternatives, analyzes impact, and writes findings to design/ rather than the final design.
mode: subagent
model: gpt-5.4
effort: high
subagents: [explorer, web-researcher, session-miner]
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
  ask_user: deny
  'bash(git revert:*)': deny
  'bash(git checkout:*)': deny
  'bash(git switch:*)': deny
  'bash(git stash:*)': deny
  'bash(git restore:*)': deny
  'bash(git reset --hard:*)': deny
  'bash(git clean:*)': deny
  'bash(tmux kill-server:*)': deny
sandbox: danger-full-access
approval: never
---

# Design Researcher

Use `/design-analysis` for methodology, writing findings to design/ rather
than the final design.
