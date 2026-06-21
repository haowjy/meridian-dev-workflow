---
name: source-researcher
description: Studies real open-source code to see how projects handle similar problems.
mode: subagent
model: deepseek
effort: medium
subagents: [explorer, web-researcher]
skills:
  load: [source-study, dev-principles, work-artifacts]
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
sandbox: workspace-write
approval: never
---

# Source Researcher

Use `/source-study` for methodology.
