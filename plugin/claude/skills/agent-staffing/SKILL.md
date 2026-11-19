---
name: agent-staffing
description: 'Load before you spawn a worker or a reviewer: how a change is reviewed and probed, and when a model change is justified.'
metadata:
  type: reference
---

# Agent Staffing

## Review

Staff every review per `resources/reviewers.md`: when it runs, who reviews,
and the one round of fixes that ends it.

## Model Selection

Honor explicit user model instructions. Otherwise launch each role on the
model its configuration gives it, rather than selecting a model for
anticipated difficulty. Brief
the configured worker on concurrency hazards and other known risks, what
must keep working, and how to verify them. This applies to reviewers
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
worker. Model changes do not reset the review round in `resources/reviewers.md`.

## Probing

Brief `prober` per `resources/testers.md`, which also says when it runs.
