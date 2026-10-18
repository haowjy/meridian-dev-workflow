---
name: agent-staffing
type: reference
description: Load when composing a team or choosing review and verification coverage.
model-invocable: true
---

# Agent Staffing

## Standard Team

Most changes are staffed from these; the catalogs below cover the rest.

- `@explorer`: reads across files and history, so your context stays on
  decisions
- `@coder`: for general coding; `@frontend-coder` for frontend coding
- `@reviewer`: finds risks in code, designs, or requirements before they're
  acted on, with skills matched to what it reviews (`resources/reviewers.md`)
- `@prober`: runtime evidence from the real system: workflows, bug
  reproductions, boundaries
- `@investigator`: root cause when behavior is unclear
- `@kb-lead`: knowledge capture when a change settles, from `/post-dev`

## Model Selection

Choose the least expensive model whose description
(`meridian mars models aliases`) fits the work. Escalate on evidence, not a
guess at difficulty: when a worker runs out of depth, retry on a stronger
model with its report, so the retry builds on what it learned. Start
stronger for concerns known to be hard: concurrency, data integrity,
ownership across modules.

## Parallel Work and Review

Use parallel lanes for independent tasks. Use cross-model fan-out when the
decision needs independent model perspectives. Run reviews in a session of their own,
apart from the writer's.

## Agent Catalogs

- `resources/reviewers.md`: the lanes a change needs, the skills for each reviewer, and when review-fix loops stop. Open it before staffing any review.
- `resources/testers.md`: @prober modes, runtime verification, browser, POC
- `resources/builders.md`: @coder, @architect, @web-researcher, @explorer, @session-miner
- `resources/maintainers.md`: @kb-lead, @kb-maintainer, @investigator
