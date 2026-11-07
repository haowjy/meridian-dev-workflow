---
name: review
description: 'Use when reviewing code, designs, or plans: review the code as it stands, check standards and design alignment, report constructive findings with severity.'
metadata:
  type: reference
---
# Review

Find what would hurt the people who use this change and the people who next
change its code. Keep the goal in view: read what the change is for (the
plan, issue, or brief) and judge whether it gets there, not only whether
its lines are right. A finding without a fix direction is a complaint.

## Read It Whole

Judge the code as it stands, not the delta. Use the diff
(`git diff <base>...HEAD`) to find the touched surface, then read that
surface whole: the full file, the concern it belongs to, its neighbors and
callers, and what the change left without a caller. A serious problem you
trace outside the diff, such as an older weakness the change now relies
on, is a finding like any other: you have eyes on code your caller doesn't.

A re-review, whose brief names the fix commits and the report they answer,
reviews the fixes and what they touch: each fix's diff, read whole with its
callers, the paths beside it, and the screens or output it changes. Check
that each fix ends its finding and the class behind it, follows the rule
the finding named instead of adding a case beside it, and broke nothing
nearby. Fixes are where many regressions start, and where structure drifts
once the first review has passed. The rest of the change had its review.

Read the source before prior reviews, reports, or approvals, so their
conclusions don't anchor yours. Then compare their scope and evidence with
your findings.

A plan or design is reviewed against the code it lands in and the
requirements it serves; check that its spec and architecture cross-link
each other and that each link lands.

## Run It

Find out whether the code works by running it (`/meridian-dev-workflow:probe`): the command,
the endpoint, a throwaway test against the real stack, written in a scratch
directory. For a plan or design, run what tests its assumptions about the
existing system. Go after how it fails, not how it succeeds: boundaries, ordering,
partial failure, bad input, an assumption nothing enforces. Then use it as
its user would, and notice what's awkward or surprising.

## What to Report

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
  change should have deleted. Name the move you'd make
  (`resources/structural-health/` has the catalog). Findings that share one
  structural cause are one structural finding: say so, since patching each
  symptom brings the cause back. Your caller takes structure findings to
  whoever owns the design, so write them for a reader deciding whether to
  redesign.
- **Cost:** for each hot path the change touches (per chunk, per turn, per
  poll, per invocation), what its cost grows with. Tests rarely catch this.

Project standards (AGENTS.md, CLAUDE.md, CONTRIBUTING, style docs) override
generic judgment, with `/meridian-dev-workflow:dev-principles` as the shared lens. Skip what
tooling enforces. Unfamiliar is not a finding: "I'd have written it
differently" is about you, not the code. If the code is good, say so, and
earn that by looking.

## Go Deeper Where Something Looks Wrong

Load depth for what you suspect, not for every review:

- Tangled concerns, a misplaced boundary, an ownership question:
  `/meridian-dev-workflow:architecture` and `resources/architecture.md`; for strict
  maintainability of a new module, abstraction, or seam,
  `/meridian-dev-workflow:thermo-nuclear-review`.
- Trust boundaries, input, auth, secrets: `resources/security.md`.
- Races, shared state, cancellation: `resources/concurrency.md`.
- Hot paths, polling, scans that grow with history:
  `resources/efficiency.md`.
- Tests: `/meridian-dev-workflow:test-architecture` and `resources/test-quality.md`.
- React structure: `/meridian-dev-workflow:react-architecture`. What a UI shows first and what
  it buries: `/meridian-dev-workflow:information-hierarchy`.
- Fidelity to a spec, design, or `DIVERGENCE/` log: `/meridian-dev-workflow:review-alignment`.
- Docs: `/meridian-dev-workflow:tech-docs` and `/meridian-dev-workflow:llm-writing`.
- Patching that won't converge: `resources/redesign-escalation.md`.

When a finding hinges on external facts (library semantics, upstream
issues, known CVEs), spawn `@web-researcher` in the background and keep
reviewing; collect the result before your verdict. When a suspected bug
needs root-cause work deeper than a review, spawn `@investigator` for the
causal chain, not the fix.

## Verify Each Finding

Check every finding before you report it, matched to the claim. Behavioral:
run what shows the failure on the real system. Structural: run the search
or trace that backs it. Plan or design: quote the conflicting passages or
show the missing mapping. Report the check and what it showed. A check
that disproves the concern drops it; one you couldn't complete goes under
Hypotheses, with what blocked it.

## Blocking or Not

A finding blocks when it is a defect, a security or data-loss risk, a miss
of the goal, or a structural problem that will keep producing defects.
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
version. Open with a brief assessment that names any cause several findings
share. Then **Blocking** and **Notes**, each finding with its check and what
it showed, and structure findings tagged `structure` in either group. Then
**What looks off**: judgment calls, what doesn't make sense or look right
or what the end user would hit, that no check could settle. Then
**Hypotheses**: factual claims you tried to check and couldn't, each with
what blocked it. End with a verdict: approve, approve with notes, request
changes, or **frame-rot**.

Frame-rot means the approach is wrong: patching will not converge, the work
needs a redesign. It is always blocking and must be constructive: name the
structural problem, cite the findings that share that root, and recommend a
direction, written as the Redesign Brief in
`resources/redesign-escalation.md`.
