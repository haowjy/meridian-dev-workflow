---
name: prober
description: >-
  Spawn when you need runtime evidence: exercise workflows, reproduce bugs,
  stress boundaries, build throwaway POCs. Skills: probe, poc, agent-browser.
mode: subagent
model: sol
effort: high
model-policies:
  - match: {alias: sol}
    override: {effort: high}
  - match: {alias: sonnet}
    override: {effort: high}
skills:
  load: [probe]
  available: [diagnose, poc, agent-browser, issues]
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
