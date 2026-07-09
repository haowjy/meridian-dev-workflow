---
name: review
type: reference
description: "Use when reviewing code, designs, or plans: review the code as it stands, check standards and design alignment, report constructive findings with severity."
model-invocable: true
---
# Review

Find the risks the implementer can't see. A finding without a fix direction
is a complaint.

## Scope the Review

Judge the code as it stands now, not the delta. A branch or diff tells you
*where* to look — pin it (`git diff <base>...HEAD`) to locate the touched
surface — but then read that surface whole: the full file, the seam it lives
in, how it composes with its neighbors. A change can be clean line by line
and still leave the component incoherent.

With no diff given, review the assigned surface; if none assigned,
prioritize highest-risk surfaces. Go deep on the assigned lane, but flag
serious issues outside it — you have eyes on the code that the orchestrator
doesn't.

## Two Axes

**Standards.** Check against the repo's own conventions wherever they live —
AGENTS.md, CLAUDE.md, CONTRIBUTING, style docs — with `/dev-principles` as
the shared lens. Repo standards override generic judgment. Skip anything
tooling already enforces.

**Design.** Check the change against what it was supposed to build:
requirements, design docs, `DIVERGENCE/` in the work directory. For systematic
coverage and drift checking, load `/review-alignment`.

Attached skills deepen a lane: `/thermo-nuclear-review`,
`/test-architecture`, `/react-architecture`.

## The Quality Bar

Judge quality as ease of change. The objective test is entanglement: are
concerns braided together that could be independent? A quality finding
points at the interleaving, and the fix direction is the disentangling
move. `/architecture` carries the full test.

Unfamiliar is not a finding. "I'd have written it differently" is relative
to the reviewer; entanglement is in the code.

## What Makes a Good Finding

- **Specific.** File, line, function.
- **Reasoned.** The failure mode, not just the pattern name.
- **Constructive.** A concrete fix direction the implementer can act on.
- **Non-obvious.** Linters catch formatting; you're here for context, intent,
  and interaction between components.

Probe how the code fails, not how it succeeds: boundary conditions, ordering
assumptions, partial failure, unenforced assumptions. If the code is
genuinely good, say so — but earn that by looking.

**Suggest refactors.** When structure is the problem, propose the move
(`resources/structural-health/` has the catalog). Code is cheapest to change
now, before more work lands on top of it.

## Your Report

Brief overall assessment, findings grouped by severity — lead with real
damage: bugs, security holes, data loss, broken invariants — then verdict:
approve, approve with notes, request changes, or **frame-rot**.

Frame-rot means the approach is wrong: patching will not converge, the work
needs a redesign. It is always blocking — and it must be constructive: name
the structural problem, cite the findings that share that root, and
recommend a direction (load `/architecture` for the structural vocabulary a
redesign needs). See `resources/redesign-escalation.md` for the signals and
the escalation shape.

## Resources

- [`resources/redesign-escalation.md`](resources/redesign-escalation.md): signals that patching won't converge, how to write the escalation
- [`resources/security.md`](resources/security.md): trust boundaries, input validation, auth, secrets
- [`resources/concurrency.md`](resources/concurrency.md): races, deadlocks, shared state, cancellation
- [`resources/architecture.md`](resources/architecture.md): independence, boundaries, module structure, design alignment
- [`resources/structural-health/`](resources/structural-health/): code smells, refactoring moves, deprecation patterns (use when focus is structural)
- [`resources/test-quality.md`](resources/test-quality.md): edge cases over happy paths, tautological assertions, tier placement, test effectiveness (use when focus is test quality)
