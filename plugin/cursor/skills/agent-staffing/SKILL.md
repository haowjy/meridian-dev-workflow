---
name: agent-staffing
description: 'Load before you spawn a worker or a reviewer: which agent for which work, the review lanes a change needs, and when a model change is justified.'
metadata:
  type: reference
alwaysApply: false
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
- `@kb-lead`: knowledge capture when a change settles, from `/meridian-dev-workflow:post-dev`

## Model Selection

Honor explicit user model instructions. Otherwise launch each role through
its configured routing, including user overrides and automatic fallback
policy, rather than selecting a model for anticipated difficulty. Brief
the configured worker on concurrency hazards and other known risks, the
invariants to preserve, and how to verify them. This applies to reviewers
as well as implementers.

Escalate only after independent review verifies a substantial pattern of
defects in that agent's work. Attribute the findings to the role whose work
failed: defects a reviewer finds in code are not a reason to upgrade the
reviewer. Task complexity, a worker saying it is stuck, and launch or
availability failures are not that evidence; fix the brief or runtime
problem instead of buying a stronger model.

Choose the least-cost upgrade whose strengths in the current model catalog
address the demonstrated failure. Try suitable intermediate options before
the premium tier; move higher only when review of the attempted fix still
shows substantial defects. Pass the findings and prior work to the next
worker. Model changes do not reset the review and redesign limits in
`resources/reviewers.md`.

## Parallel Work and Review

Use parallel lanes for independent tasks. Run reviews in a session of their own,
apart from the writer's.

## Agent Catalogs

- `resources/reviewers.md`: the lanes a change needs, the skills for each reviewer, and when review-fix loops stop. Open it before staffing any review.
- `resources/testers.md`: @prober modes, runtime verification, browser, POC
- `resources/builders.md`: @coder, @frontend-coder, @mockup-dev, and design exploration (@architect, @web-researcher, @browser, @design-researcher, @source-researcher, @explorer, @session-miner)
- `resources/maintainers.md`: @kb-lead, @kb-maintainer, @investigator
