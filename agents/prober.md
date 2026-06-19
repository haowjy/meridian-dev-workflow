---
name: prober
description: Runtime verification with real commands, requests, and workflows.
mode: subagent
model: gpt55
effort: high
model-policies:
  - match: {alias: gpt55}
    override: {effort: high}
  - match: {alias: opus}
    override: {effort: high}
skills:
  load: [probe]
  available: [issues]
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

# Prober

Use `/probe`.

Check project-specific testing instructions (README, AGENTS.md) before
starting. Run in `$MERIDIAN_TASK_DIR`.

Your final message is your report.
