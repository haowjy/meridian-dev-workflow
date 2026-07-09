---
name: design-researcher
description: Researches design and architectural options, writing analysis for the team.
mode: subagent
model: sol
effort: medium
model-policies:
  - match: {alias: sol}
    override: {effort: medium}
  - match: {alias: terra}
    override: {}
  - match: {alias: opus46}
    override: {}
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
