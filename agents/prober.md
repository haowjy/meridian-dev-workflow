---
name: prober
description: "Spawn when you need runtime evidence: exercise workflows, reproduce bugs, stress boundaries, build throwaway POCs. Pass entrypoints, expected behavior, constraints, evidence needed, and any numbers to record. It names what it creates with its spawn id; after a failed or cancelled run, remove what it left under that id. Skills: probe, poc, agent-browser."
mode: subagent
model: luna
effort: high
model-policies:
  - match: {alias: luna}
    override: {effort: high}
  - match: {alias: deepseek}
    override: {effort: high}
  - match: {alias: sonnet}
    override: {effort: high}
  - match: {alias: sol}
    override: {effort: high}
skills:
  load: [probe]
  available: [poc, agent-browser, issues]
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

# Prober

Use `/probe`.

Check project-specific testing instructions (README, AGENTS.md) before
starting.
