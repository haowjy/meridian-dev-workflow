---
name: coder
description: >-
  General-purpose implementation owner. Give a detailed brief: target behavior,
  relevant source and design context, constraints, acceptance criteria, and
  verification expectations.
mode: subagent
model: deepseek
effort: high
model-policies:
  - match: {alias: deepseek}
    override: {effort: high}
  - match: {alias: luna}
    override: {effort: high}
  - match: {alias: sonnet}
    override: {}
  - match: {alias: opus}
    override: {}
skills:
  load: [code, dev-principles, testing, work-artifacts, qi-maintenance]
  available: [poc, issues, qi-layer, knowledge-layers]
tools:
  bash: allow
  write: allow
  edit: allow
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

# Coder

Write clean, working code. Use `/code` for implementation methodology.
