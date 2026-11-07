# Reviewers

Spawn `@reviewer` for a change's review. Use `/meridian-dev-workflow:agent-staffing`'s Model
Selection policy for routing and escalation.

## When Review Runs

A feature gets two reviews: its plan, before code is written, and its code,
once all of it is built. A plan review is the cheapest catch: a better
structure found in the plan costs an edit, and found in code, a rewrite. A
feature built in phases, moves, or part PRs still gets one code review, of
everything it changed since its base. Each extra gate repeats the review,
its fixes, and the runtime check.

## Lanes a Change Needs

- One `@reviewer` for the code. It reviews everything about the change and
  loads the skills its findings call for. Brief it with what the feature is
  for, where the change landed, the risks you see, and the earlier review
  reports on the same code, so it can tell a recurring concern from a new
  one. One reviewer sees one cause behind several symptoms, where split
  lanes each report their own.
- `@prober` once, on the final code, when the change alters what the
  running system does (`testers.md`). Confirm the stack it runs was built
  from the final code, and tell it to use its own test data and browser
  session and not to reset or restart shared services.

## After the Review

One round per feature, in this order: the review, its fixes, one
re-review of those fixes, the prober's run, and one re-check of what the
probe's fixes change. Nothing in it repeats. Fix valid blocking findings; notes are yours to take or leave. Record
reasons for deferrals with the work item's decisions, and resolve
conflicting findings using the design and evidence.

Read the findings by concern, the code behind one responsibility, before
fixing any. Blocking structure findings, findings that share a cause, and a
frame-rot verdict go to `@design-lead` (the user, when you can't spawn
one) as a Redesign Brief (`/meridian-dev-workflow:review`
`resources/redesign-escalation.md`) with the report, not to a patch:
symptoms patched one at a time bring the cause back in the re-review. A
question about what the feature should do goes to the user.

Each fix is committed, the suite rerun, and the fix checked on the real
system, on what it changes and the screens or commands next to it. Read
small fixes yourself. Send fixes that restructure code or change behavior
to one re-review, all fixes from the report together: a `@reviewer` briefed
with the fix commits, the report they answer, and what each fix was meant
to end. It reviews the fixes and what they touch, not the whole change
again.

Defects the prober finds go back to the coder, who fixes and checks them;
read the fix diffs yourself, then send the prober back once, only to what
those fixes change.

A re-review or probe re-check that still finds blocking problems ends the
round. Take them to `@design-lead`, or to the user when they turn on what
the feature should do, rather than starting another round. A failed redesign goes to your
caller: the problem usually sits in scope or requirements.

## Reviewing Requirements or a Design

Requirements and designs are review targets like code: a `@reviewer` can
challenge the requirements or the framing, not only an implementation. For
a converged design, have one `@reviewer` challenge its correctness, edge
cases, and requirement coverage, and a `@prober` check what it assumes of
the real system. Substantive findings mean another round; minor
refinements mean converged. Substantive findings after a second round go to
your caller as the open question.
