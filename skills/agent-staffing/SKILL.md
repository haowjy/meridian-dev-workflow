---
name: agent-staffing
type: reference
description: Use when composing a team — which agents, how many, parallel vs sequential, effort scaling.
model-invocable: true
---

# Agent Staffing

If no team composition was provided by your caller, compose one yourself
using the agent catalogs below.

## Fan-Out vs Parallel Lanes

- **Fan-out**: same prompt, same files, different models. Convergent signal
  on a high-stakes call. Reserved for critical decisions.
- **Parallel lanes**: different prompts (different focus areas), usually
  default model each. Most review staffing uses parallel lanes.

Fan out reviewers across models for perspective diversity. Run
`meridian mars models list` for configured families and strengths.

## Agent Catalogs

- `resources/reviewers.md`: @reviewer, @alignment-reviewer, @simplify-reviewer
- `resources/testers.md`: @prober, @browser-prober, testing skills
- `resources/builders.md`: @coders, @architects, @web-researchers, @explorers
- `resources/maintainers.md`: @kb-lead, @kb-maintainer, @investigator
