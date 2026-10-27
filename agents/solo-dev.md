---
name: solo-dev
description: "Launch for a change one agent implements and verifies itself, without a team of implementers. Pass target behavior, relevant context, constraints, acceptance criteria, and verification expectations."
mode: primary
model: astra
subagents: [reviewer, prober, explorer, investigator, kb-lead, cold-reader, subagent]
effort: high
model-policies:
  - match: {alias: astra}
    override: {effort: high}
  - match: {alias: opus}
    override: {effort: medium}
  - match: {alias: sol}
    override: {effort: high}
  - match: {alias: deepseekpro}
    override: {effort: high}
skills:
  load: [solo-dev, dev-principles, work-artifacts, qi-maintenance, explore-and-engage, intent-modeling, agent-staffing]
  available: [shared-dao, pre-dev, testing, dev-workflow, review, post-dev, issues, architecture, qi-layer, knowledge-layers, probe]
tools:
  bash: allow
  write: allow
  edit: allow
  'bash(git push *)': allow
  'bash(gh pr *)': allow
  'skill(deep-research)': deny
  'skill(init)': deny
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

# Solo Dev

Implement the change yourself and verify it yourself, following
`/solo-dev`.
