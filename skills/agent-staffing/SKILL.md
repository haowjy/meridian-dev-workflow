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

At high-stakes gates, fan out reviewers across models on the same frozen head; model diversity yields disjoint finding classes, not just redundancy. Pair every static review lane with a prober lane because code reading and runtime probing catch different physics. `meridian mars models list` shows configured families and strengths.

## Agent Catalogs

- `resources/reviewers.md`: which `--skills` to pass @reviewer by change risk
- `resources/testers.md`: @prober modes, runtime verification, browser, POC
- `resources/builders.md`: @coder, @architect, @web-researcher, @explorer, @session-miner
- `resources/maintainers.md`: @kb-lead, @kb-maintainer, @investigator

## Model Budget

Model routing is constrained by provider credit budgets only the user sees.
Default to each agent's configured model. Treat in-session routing directives
from the user ("X for complicated, Y for mechanical", "out of Z credits") as
binding for the rest of the session; record them in the work item so spawned
leads inherit them. When a provider dies mid-session (credit exhaustion,
harness timeout), reroute remaining lanes to surviving families and note the
change in the work ledger — don't retry the dead provider.
