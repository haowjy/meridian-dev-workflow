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
  load: [solo-dev, dev-workflow, dev-principles, work-artifacts, qi-maintenance, explore-and-engage, intent-modeling, agent-staffing]
  available: [shared-dao, pre-dev, testing, review, post-dev, issues, architecture, qi-layer, knowledge-layers, probe]
tools:
  bash: allow
  write: allow
  edit: allow
  'bash(tmux kill-server:*)': deny
  'bash(agent-browser close --all:*)': deny
  'bash(agent-browser quit --all:*)': deny
  'bash(agent-browser exit --all:*)': deny
sandbox: danger-full-access
approval: never
---

# Solo Dev

Implement the change yourself and verify it yourself, following
`/solo-dev`, and carry it to a PR per `/dev-workflow`.

Report: what changed, how you verified it, review findings, PR link.
