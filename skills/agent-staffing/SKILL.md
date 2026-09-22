---
name: agent-staffing
type: reference
description: Load when composing a team for a work item. Which agents to spawn, how many, model selection.
model-invocable: true
---

# Agent Staffing

If no team composition was provided by your caller, compose one yourself using the catalogs below.

## Model Selection

Keep explicit caller choices and role-specific policies. Otherwise, prefer
capable, inexpensive workers for implementation and execution; larger models
must earn their cost through technical depth, decision quality, or writing.
Read `resources/model-selection.md` when choosing a model or departing from a
profile default. It covers the general preference order, local-model options,
writing-heavy work, and capability checks.

## Fan-Out vs Parallel Lanes

- **Fan-out**: same prompt, same files, different models. Convergent signal on a high-stakes call.
- **Parallel lanes**: different prompts (different focus areas), default model each.

Prefer a reviewer model different from the model that actually implemented the
change, including after fallback. Fan out across models when the risk warrants
multiple perspectives; a different model still needs an independent review
context.

## Agent Catalogs

- `resources/reviewers.md`: which `--skills` to pass @reviewer by change risk
- `resources/testers.md`: @prober modes, runtime verification, browser, POC
- `resources/builders.md`: @coder, @architect, @web-researcher, @explorer, @session-miner
- `resources/maintainers.md`: @kb-lead, @kb-maintainer, @investigator
