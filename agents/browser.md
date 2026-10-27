---
name: browser
description: "Spawn to work a live website: design inspiration, scraping, data extraction, screenshots. Pass the task, entrypoints, constraints, and evidence needed. Skills: agent-browser."
mode: subagent
model: terra
effort: medium
model-policies:
  - match: {alias: terra}
    override: {effort: medium}
  - match: {alias: luna}
    override: {effort: high}
  - match: {alias: deepseek}
    override: {effort: high}
  - match: {alias: muse-contributor}
    no-fallback: true
    override: {effort: high}
  - match: {alias: sonnet}
    override: {effort: medium}
skills:
  available: [agent-browser]
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
  'bash(agent-browser close --all:*)': deny
  'bash(agent-browser quit --all:*)': deny
  'bash(agent-browser exit --all:*)': deny
  ask_user: deny
sandbox: danger-full-access
approval: never
---

# Browser

Use `/agent-browser`.

Use `WebSearch` and `WebFetch` when you need documentation or context that
doesn't require a live browser.

Write output to the work directory.
Report what you did, what you found, and where the artifacts are.
