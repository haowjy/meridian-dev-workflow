---
name: agent-staffing
type: reference
description: Load when composing a team for a work item. Which agents to spawn, how many, model selection.
model-invocable: true
---

# Agent Staffing

If no team composition was provided by your caller, compose one yourself using the catalogs below.

## Fan-Out vs Parallel Lanes

- **Fan-out**: same prompt, same files, different models. Convergent signal on a high-stakes call.
- **Parallel lanes**: different prompts (different focus areas), default model each.

Fan out reviewers across models for perspective diversity. `meridian mars models list` shows configured families and strengths.

## Agent Catalogs

- `resources/reviewers.md`: which `--skills` to pass @reviewer by change risk
- `resources/testers.md`: @prober modes, runtime verification, browser, POC
- `resources/builders.md`: @coder, @architect, @web-researcher, @explorer, @session-miner
- `resources/maintainers.md`: @kb-lead, @kb-maintainer, @investigator
