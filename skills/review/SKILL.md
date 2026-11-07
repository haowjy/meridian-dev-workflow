---
name: review
description: "Use when reviewing code, designs, or plans: review the code as it stands, check standards and design alignment, report constructive findings with severity."
model-invocable: true
metadata:
  type: reference
---
# Review

Find what would hurt the people who use this change and the people who next
change its code. Keep the goal in view: read what the change is for (the
plan, issue, or brief) and judge whether it gets there, not only whether
its lines are right. Give each finding a fix direction at the level it
needs: a different approach, a structural move, or the shape the code
should take. Leave the patch to whoever fixes it.

## Read It Whole

Judge the code as it stands, not the delta. Use the diff
(`git diff <base>...HEAD`) to find the touched surface, then read that
surface whole: the full file, the concern it belongs to, its neighbors and
callers, and what the change left without a caller. A serious problem you
trace outside the diff is a finding like any other: you have eyes on code
your caller doesn't.

Read the change and the code around it yourself: your judgment rests on
that reading. Hand the sweeps past it to one `@explorer` with all your
questions: what the change left without a caller, every other place a
finding's pattern recurs, how the rest of the codebase already does what
the change does. Read the code behind what comes back before it becomes a
finding.

A re-review, whose brief names the fix commits and the report they answer,
reviews the fixes and what they touch: each fix's diff, read whole with its
callers, the paths beside it, and the screens or output it changes. Check
that each fix ends its finding and the class behind it, follows the rule
the finding named instead of adding a case beside it, and broke nothing
nearby: fixes are where many regressions start. The rest of the change had
its review.

Read the source before prior reviews, reports, or approvals, so their
conclusions don't anchor yours. Then compare their scope and evidence with
your findings.

Review a plan or design against the code it lands in and the requirements
it serves.

## Run It

Find out whether the code works by running it (`/probe`): the command,
the endpoint, a throwaway test against the real stack, written in a scratch
directory; for a plan, what tests its assumptions about the existing
system. Go after how it fails, not how it succeeds: boundaries, ordering,
partial failure, bad input, an assumption nothing enforces. Then use it as
its user would.

## What to Look For

- **Defects:** what breaks, regresses, loses data, opens a security hole,
  or misses the goal.
- **What doesn't make sense:** a name that says something other than what
  the code does, a step whose reason you can't find, a rule enforced in one
  place and skipped in the next.
- **What doesn't look right:** code that works but that you'd stop on, such
  as a special case beside the rule it should follow, or a state nothing
  can leave.
- **What the end user would hit:** what the person using it sees, waits
  for, or loses when it goes wrong: the error text, a stuck or blank screen,
  an edit gone after reload, a command that succeeds and does nothing.
- **Bad structure:** concerns braided together, a responsibility in the
  wrong place, a new path beside the old one it should replace, code the
  change should have deleted. Suggest the move, or the structure you'd aim
  for when one move won't get there (`resources/structural-health/` has the
  catalog of moves; `/architecture` the vocabulary). Your caller takes
  structure findings to whoever owns the design, so write them for a
  reader deciding whether to redesign.
- **Cost:** a hot path (per turn, per poll, per invocation) whose cost
  grows with something it shouldn't (`resources/efficiency.md`). Tests
  rarely catch this.

Project standards (AGENTS.md, CLAUDE.md, CONTRIBUTING, style docs) override
generic judgment, with `/dev-principles` as the shared lens. Skip what
tooling enforces. Unfamiliar is not a finding: "I'd have written it
differently" is about you, not the code. If the code is good, say so, and
earn that by looking.

## Go Deeper Where Something Looks Wrong

Load depth for what you suspect, not for every review:

- Tangled concerns, a misplaced boundary, an ownership question:
  `/architecture` and `resources/architecture.md`; for strict
  maintainability of a new module, abstraction, or seam,
  `/thermo-nuclear-review`.
- Trust boundaries, input, auth, secrets: `resources/security.md`.
- Races, shared state, cancellation: `resources/concurrency.md`.
- Tests: `/test-architecture` and `resources/test-quality.md`.
- React structure: `/react-architecture`. What a UI shows first and what
  it buries: `/information-hierarchy`.
- Fidelity to a spec, design, or `DIVERGENCE/` log: `/review-alignment`.
- Docs: `/tech-docs` and `/llm-writing`.
- Patching that won't converge: `resources/redesign-escalation.md`.

Check what the code assumes and what you recommend against the real
thing: a library's docs or its installed source, the platform's behavior,
upstream issues and CVEs, and whether a built-in or an established pattern
already does what the change hand-rolls. Spawn `@web-researcher` in the
background for what needs the web, and collect it before your verdict. For
a bug that needs deeper root-cause work, spawn `@investigator` for the
causal chain.

## Verify Each Finding

Check every finding before you report it, matched to the claim. Behavioral:
run what shows the failure on the real system. Structural: run the search
or trace that backs it. Plan or design: quote the conflicting passages or
show the missing mapping. Report the check and what it showed. A check
that disproves the concern drops it; for one you couldn't complete, say
what blocked it.

## Blocking or Not

A finding blocks when it is a defect, a miss of the goal, or a structural
problem that will keep producing defects.
Everything else is a note: the caller fixes it now or doesn't, and it never
earns another review round. For each blocking finding, say whether it is a
one-off or one instance of a class, and for a class, the fix that ends it
rather than the patch for this instance: the caller gets one round of
fixes. Earlier review reports, when your brief passes them, are evidence:
cite each earlier finding that lands on the same concern as one of yours,
and say whether it recurs because a fix fell short or because the
structure keeps producing it.

## Your Report

Name what you reviewed: the commit and base, or the artifact's path and
version. Lead with what blocks and any cause several findings share, then
the rest, shaped to what you found. Keep what you verified apart from what
you only judged or couldn't check, so your caller knows what rests on
evidence, and mark structure findings as such. End with a verdict: approve,
approve with notes, request changes, or **frame-rot**.

Frame-rot means the approach is wrong and patching won't converge. It
always blocks; write it as the Redesign Brief in
`resources/redesign-escalation.md`.
