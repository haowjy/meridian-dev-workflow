# Reviewers

Spawn `@reviewer` with skills matched to the change's risks. Use
`/agent-staffing`'s Model Selection policy for routing and escalation.

## Lanes a Change Needs

Review and probe the system as it stands, so each lane sees how the change
fits the code around it and what it left without a caller. Brief each lane
with where the change landed, the risks to check, and the earlier review
reports on the same code, so it can tell a recurring concern from a new one.

- `@reviewer` for correctness, regressions, and behavior.
- `@reviewer` with `/thermo-nuclear-review` when the change adds a module,
  abstraction, or seam, moves responsibility between them, or grows
  existing code beyond a local edit. Code drifts from `/dev-principles`
  even when its writer loaded them; a reviewer focused there catches what
  a general pass skims.
- `@explorer` when the change deletes or replaces code, and before the
  thermo lane: it lists what the change and its fixes left without a
  caller, given the change's base. Delete what is clearly dead, and pass
  the rest to the reviewers.
- One more `@reviewer` for each risk the change carries, from the picker
  below.
- `@prober` when the change alters what the running system does
  (`testers.md`).

Spawn the other lanes together, and the thermo lane after their fixes land,
so it folds those patches into the code's structure. Confirm the stack the prober runs was built from
the code under review, and tell each lane to use its own test data
(accounts, records, fixtures, browser session) and not to reset or restart
shared services; run lanes one after the other when they would share state
you can't separate.

## Skill Picker

| Review kind | Spawn | When |
|-------------|-------|------|
| Default review | `@reviewer` | Correctness, maintainability, efficiency, security |
| Strict maintainability | `@reviewer`; attach `/thermo-nuclear-review` | New modules, abstractions, or seams; moved responsibility; growth beyond a local edit |
| Efficiency | `@reviewer` with the efficiency lane named in the prompt | Runtime paths, polling, persistence, scans, startup |
| Architecture / boundaries | `@reviewer`; attach `/thermo-nuclear-review` and `/architecture` | Cross-module boundary changes, dependency direction; repeat findings on one concern (Synthesizing Findings) |
| Test structure | `@reviewer`; attach `/test-architecture` | Test suite changes |
| Design alignment | `@reviewer`; attach `/review-alignment` | Cross-artifact fidelity vs design/requirements |
| Frontend structural | `@reviewer`; attach `/react-architecture` | React component boundaries, state, tokens |
| Doc structure | `@reviewer`; attach `/tech-docs`, `/llm-writing`, and `/md-validation` | Doc-heavy changes |

## Synthesizing Findings

Fix valid findings; record reasons for deferrals with the work item's
decisions. Commit a fix that restructures code or changes behavior, rerun
the suite, and rerun the lanes whose verdicts it could change; read smaller
fixes yourself.

Resolve conflicting findings using the design and evidence. Read
findings by concern, the code behind one responsibility, not by symptom or
file.

Count rounds per review target: each gate in phased work, otherwise the
change. A round is one review and the fixes it calls for. At each limit,
stop sending rounds:
- **A concern that would need a third round of fixes:** trace the root
  cause, yourself or with `@investigator`, then have the system reviewed as
  a whole (`@reviewer`; attach `/thermo-nuclear-review` and `/architecture`) with
  every earlier report. Ask whether the findings share a cause, and for
  either the move that ends it or a frame-rot verdict. The cause often sits
  where two parts own one invariant.
- **A concern that would need a second redesign:** bring the impasse to
  your caller. A failed redesign usually means the problem sits in scope or
  requirements.
- **A target that would need a fourth review round**, whatever the
  concerns: investigate the design rather than cycling reviewers.
