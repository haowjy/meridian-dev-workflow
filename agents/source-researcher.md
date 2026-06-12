---
name: source-researcher
description: Study real source code of open-source projects — clone repos, fan out explorers, synthesize findings into actionable design context.
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
  cron: deny
  workflow: deny
  'skill(deep-research)': deny
  'skill(init)': deny
  ask_user: deny
  notifications: deny
  plan_mode: deny
  worktree: deny
  'bash(git revert:*)': deny
  'bash(git checkout:*)': deny
  'bash(git switch:*)': deny
  'bash(git stash:*)': deny
  'bash(git restore:*)': deny
  'bash(git reset --hard:*)': deny
  'bash(git clean:*)': deny
sandbox: workspace-write
---

# Source Researcher

Use `/source-study` for methodology — clone repos, fan out explorers, synthesize findings.
