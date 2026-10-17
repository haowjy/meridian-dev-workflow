---
name: source-researcher
description: "Spawn to see how real open-source projects handle a similar problem. Pass the problem and any candidate projects."
mode: subagent
model: luna
effort: high
model-policies:
  - match: {alias: luna}
    override: {effort: high}
  - match: {alias: deepseek}
    override: {effort: high}
  - match: {alias: sol}
    override: {effort: medium}
  - match: {alias: sonnet}
    override: {}
subagents: [explorer, web-researcher, subagent]
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

# Source Researcher

Use `/source-study` for methodology.
