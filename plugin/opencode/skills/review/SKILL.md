---
name: review
description: 'Use when reviewing code, designs, or plans: review the code as it stands, check standards and design alignment, report constructive findings with severity.'
metadata:
  type: reference
---
# Review

Find the risks the implementer can't see. A finding without a fix direction
is a complaint.

## Scope the Review

Judge the code as it stands now, not the delta. A branch or diff tells you
*where* to look — pin it (`git diff <base>...HEAD`) to locate the touched
surface — but then read that surface whole: the full file, the concern it belongs
to, how it composes with its neighbors. A change can be clean line by line
and still leave the component incoherent.

With no diff given, review the assigned surface; if none assigned,
prioritize highest-risk surfaces. Go deep on the assigned lane. A serious
issue outside the lane or the diff, including a cause you trace there such
as an older weakness the change now relies on, is a finding like any other,
with severity and a fix direction, not a side note: you have eyes on the
code that your caller doesn't.

Read the source before prior reviews, reports, or approvals, so their
conclusions don't anchor yours. Then compare their scope and evidence with
your findings.

## Two Axes

**Standards.** Check against the project's own conventions wherever they live —
AGENTS.md, CLAUDE.md, CONTRIBUTING, style docs — with `/meridian-dev-workflow:dev-principles` as
the shared lens. Project standards override generic judgment. Skip anything
tooling already enforces.

**Design.** Check the change against what it was supposed to build:
requirements, design docs, `DIVERGENCE/` in the work directory. For systematic
coverage and drift checking, load `/meridian-dev-workflow:review-alignment`.

Attached skills deepen a lane: `/meridian-dev-workflow:thermo-nuclear-review`,
`/meridian-dev-workflow:test-architecture`, `/meridian-dev-workflow:react-architecture`.

## Maintainability

Judge quality as ease of change: how few concepts a reader must hold to
change the code safely. Check both on every review:

- **Entanglement.** Concerns braided together that could be independent. The
  finding points at the interleaving; the fix direction is the disentangling
  move. `/meridian-dev-workflow:architecture` carries the full test.
- **Deletion.** LLM-written code keeps what it should delete. Name what the
  change could delete or simplify: dead paths, a mechanism it duplicates
  instead of replacing, wrappers, branches a simpler structure would remove. A
  new path beside an old one it should replace is a finding. A diff hides
  what the change left without a caller: search for remaining references to
  what it removed.

Unfamiliar is not a finding. "I'd have written it differently" is relative
to the reviewer; entanglement is in the code.

## Efficiency by Construction

Tests rarely catch large efficiency problems. On every review, name the hot
paths the change touches (per chunk, per turn, per poll, per invocation) and
what their cost scales with, against `/meridian-dev-workflow:dev-principles`' efficiency principle. Load `resources/efficiency.md`
when the change touches a hot path. Skip micro-optimizations.

## What Makes a Good Finding

- **Specific.** File, line, function.
- **Reasoned.** The failure mode, not just the pattern name.
- **Constructive.** A concrete fix direction the implementer can act on.
- **Non-obvious.** Linters catch formatting; you're here for context, intent,
  and interaction between components.
- **Verified.** Check every finding before you report it, and match the check
  to the claim. Behavioral: run the command, failing test, or script that
  shows the failure. Structural: run the search or trace that backs it
  (callers, remaining references). Design or plan: quote the conflicting
  passages or show the missing mapping. Report the check and the observation
  that settled it. A check that disproves the concern drops the finding; a
  check you could not complete goes under Hypotheses in the report, with what
  blocked it.

Probe how the code fails, not how it succeeds: boundary conditions, ordering
assumptions, partial failure, unenforced assumptions. If the code is
genuinely good, say so — but earn that by looking.

**Suggest refactors.** When structure is the problem, propose the move
(`resources/structural-health/` has the catalog). Code is cheapest to change
now, before more work lands on top of it.

## Look Past This Round

A blocking finding is a one-off or one instance of a class; say which. For
a class, name the move that would end it, and whether your fix direction
makes that move or patches this instance. Earlier review reports on the
same surface, when your brief passes them, are your evidence: cite each
earlier finding that lands on the same concern as one of yours. Recurrence across rounds is evidence for the
signals in `resources/redesign-escalation.md`.

## Your Report

Name the commit and base you reviewed. Then a brief overall assessment,
findings grouped by severity — lead with real damage: bugs, security holes,
data loss, broken invariants — then verdict: approve, approve with notes,
request changes, or **frame-rot**. Every finding in the severity groups is
verified, with its check and what it showed. A closing **Hypotheses** section
lists what you could not check, each with what blocked it.

Frame-rot means the approach is wrong: patching will not converge, the work
needs a redesign. It is always blocking — and it must be constructive: name
the structural problem, cite the findings that share that root, and
recommend a direction (load `/meridian-dev-workflow:architecture` for the structural vocabulary a
redesign needs). See `resources/redesign-escalation.md` for the signals and
the escalation shape.

## Resources

- [`resources/redesign-escalation.md`](resources/redesign-escalation.md): signals that patching won't converge, how to write the escalation
- [`resources/security.md`](resources/security.md): trust boundaries, input validation, auth, secrets
- [`resources/concurrency.md`](resources/concurrency.md): races, deadlocks, shared state, cancellation
- [`resources/efficiency.md`](resources/efficiency.md): hot paths, write amplification, polling, scans that grow with history, eager startup, contention
- [`resources/architecture.md`](resources/architecture.md): independence, boundaries, module structure, design alignment
- [`resources/structural-health/`](resources/structural-health/): code smells, refactoring moves, deprecation patterns (use when focus is structural)
- [`resources/test-quality.md`](resources/test-quality.md): edge cases over happy paths, tautological assertions, tier placement, test effectiveness (use when focus is test quality)
