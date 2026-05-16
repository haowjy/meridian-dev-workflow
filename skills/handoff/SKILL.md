---
name: handoff
type: reference
description: >
  Load when writing a handoff prompt for a subagent spawn — after you've
  decided which agent to use and what they need to do. Prompt craft for
  handoffs: context matching, boundary setting, exit criteria.
model-invocable: true
---

# Handoff Prompt Craft

A handoff prompt is exactly what the subagent needs to produce a verifiable
output. Every sentence costs the subagent's attention — give them only what
helps them do the job.

## What to Give the Subagent

**What** — concrete task, specific deliverable. "Produce design/architecture/
high-level.md with three structural options, each enumerating tradeoffs" tells
an architect what to produce. "Produce a plan" describes a job, not a task.

**Why** — purpose and outcome in one sentence. Enough for the subagent to make
decisions that serve the right goal.

**How to verify** — exit criteria. What does "done" look like? Tell the
subagent to self-check before reporting. "After producing, verify every design
option addresses the stated constraints."

**Constraints** — scope boundaries. "Modify only src/auth/." Specific,
testable limits.

## Match Context to Job

Give the subagent what its role needs, not everything you know.

A **coder** needs WHAT to build + WHICH files to touch. Give the design
conclusion, not the design deliberation.

An **architect** needs the DESIGN QUESTION + constraints. Give the problem,
not the codebase layout.

A **reviewer** needs the artifact + focus area. Give the output to review,
not how it was produced.

Ask: does this sentence help the subagent produce better output?

## With --from: Point, Don't Restate

When you spawn with `--from <chat-id>`, the subagent has access to the
session. Tell it what to mine: "The session covers the requirements. Mine
it for decisions and constraints." The prompt carries the task, exit
criteria, and scope boundaries.

Without `--from`, keep the prompt tight — pass artifacts via `-f` instead
of inlining them. Artifacts travel as files and folders, using absolute
paths. The prompt carries task and constraints; design documents, specs,
and code travel as `-f` references.

## Write the Conclusion, Not the Path

The subagent opens your prompt in isolation — it has no access to your
planning conversation.

**Write for the reader.** "The user and I discussed" references a conversation
the subagent wasn't in. Write the outcome: "The user needs X because Y."

**Front-load.** Purpose first, specifics second, references last. The
subagent should know what it's doing by line 3.

**Be concrete.** "Find where auth logic is duplicated across
src/api/handlers/" not "explore the codebase."

**One verification sentence.** "Verify by running `pytest tests/auth/`."
A multi-point review checklist belongs to you, the orchestrator — the
subagent cannot review itself.

## Keep It Tight

A handoff fits in one screen. Read it back: keep only what helps the subagent
produce better output. Give them room for the actual work.
