---
name: coder
description: General purpose implementation of code.
mode: subagent
model: sol
effort: medium
model-policies:
  - match: {alias: sol}
    override: {effort: medium}
  - match: {alias: composer}
    override: {}
  - match: {alias: sonnet}
    override: {}
  - match: {alias: deepseek}
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
