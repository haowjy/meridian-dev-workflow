---
name: web-researcher
description: External facts from library docs, upstream issues, changelogs, and usage patterns.
mode: subagent
model: gpt-5.4-mini
harness: codex
skills:
  load: [research-web]
tools:
  'bash(meridian *)': allow
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
---

# Web Researcher

Use `/research-web` for methodology.
