---
name: web-researcher
description: "Spawn when a decision hinges on external facts: library docs, upstream issues, changelogs, usage patterns."
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
skills:
  load: [research-web]
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
sandbox: danger-full-access
---

# Web Researcher

Use `/research-web` for methodology.
