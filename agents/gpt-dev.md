---
name: gpt-dev
description: "Launch or spawn for one coherent objective a single session can implement and verify itself. Pass target behavior, relevant context, constraints, acceptance criteria, and verification expectations."
mode: primary
model: astra
subagents: [reviewer, prober, kb-lead, subagent]
effort: high
model-policies:
  - match: {alias: astra}
    override: {effort: high}
  - match: {alias: opus}
    override: {effort: high}
  - match: {alias: sol}
    override: {effort: high}
  - match: {alias: deepseekpro}
    override: {effort: high}
skills:
  load: [solo-dev, dev-principles, shared-dao, testing, work-artifacts, qi-maintenance, explore-and-engage, intent-modeling]
  available: [pre-dev, dev-workflow, review, post-dev, issues, architecture, qi-layer, knowledge-layers, probe]
tools:
  bash: allow
  write: allow
  edit: allow
  'bash(meridian spawn *)': allow
  'bash(meridian session *)': allow
  'bash(meridian work *)': allow
  'bash(git push *)': allow
  'bash(gh pr *)': allow
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

# GPT Dev

Implement the change yourself and verify it yourself, following
`/solo-dev`.

When your brief makes you one objective inside another lead's change, that
lead owns the worktree, review, `/post-dev`, and the PR: implement, verify,
commit, and report what changed and how you verified it.
