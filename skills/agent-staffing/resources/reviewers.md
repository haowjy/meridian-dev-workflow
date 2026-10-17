# Reviewers

Spawn `@reviewer` with skills matched to the change's risks.

## Lanes a Change Needs

Review and probe the system as it stands, so each lane sees how the change
fits the code around it and what it left without a caller. Brief each lane
with where the change landed, the risks to check, and the earlier review
reports on the same code, so it can tell a recurring concern from a new one. Put
each reviewer on a model family other than every model that wrote the work.

- `@reviewer` for correctness, regressions, and behavior.
- `@reviewer` with `/thermo-nuclear-review` when the change adds or
  restructures code. Code drifts from `/dev-principles` even when its
  writer loaded them; a reviewer focused there catches what a general pass
  skims.
- One more `@reviewer` for each risk the change carries, from the picker
  below.
- `@prober` when the change alters what the running system does
  (`testers.md`).

Spawn the lanes together. Confirm the stack the prober runs was built from
the code under review, and tell each lane to use its own test data
(accounts, records, fixtures, browser session) and not to reset or restart
shared services; run lanes one after the other when they would share state
you can't separate.

## Skill Picker

| Review kind | Spawn | When |
|-------------|-------|------|
| Default review | `@reviewer` | Correctness, maintainability, efficiency, security |
| Strict maintainability | `@reviewer --skills thermo-nuclear-review` | Changes that add or restructure code, beside the default reviewer; spaghetti growth |
| Efficiency | `@reviewer` with the efficiency lane named in the prompt | Runtime paths, polling, persistence, scans, startup |
| Architecture / boundaries | `@reviewer --skills thermo-nuclear-review,architecture` | Cross-module boundary changes, dependency direction; repeat findings on one concern (Synthesizing Findings) |
| Test structure | `@reviewer --skills test-architecture` | Test suite changes |
| Design alignment | `@reviewer --skills review-alignment` | Cross-artifact fidelity vs design/requirements |
| Frontend structural | `@reviewer --skills react-architecture` | React component boundaries, state, tokens |
| Doc structure | `@reviewer --skills tech-docs,llm-writing,md-validation` | Doc-heavy changes |

## Model Selection

An architecture review triggered by repeat findings runs on Fable, even
when the coder or lead is a Claude model: it judges the system's shape across
rounds, where depth of judgment matters more than a second family's eye.
That makes it a supplement. Before acting on its remedy, have a reviewer on
a family other than the coder's check it; the default reviewer still runs
beside it.

DeepSeek and Luna are options for quick, low-risk checks, not automatic
fallbacks.

## Synthesizing Findings

Fix valid findings; record reasons for deferrals with the work item's
decisions. Resolve conflicting findings using the design and evidence. Read
findings by concern, the code behind one responsibility, not by symptom or
file.

Count rounds per review target: each gate in phased work, otherwise the
change. A round is one review and the fixes it calls for. At each limit,
stop sending rounds:
- **A concern that would need a third round of fixes:** trace the root
  cause, yourself or with `@investigator`, then have the system reviewed as
  a whole (`@reviewer --skills thermo-nuclear-review,architecture`) with
  every earlier report. Ask whether the findings share a cause, and for
  either the move that ends it or a frame-rot verdict. The cause often sits
  where two parts own one invariant.
- **A concern that would need a second redesign:** bring the impasse to
  your caller. A failed redesign usually means the problem sits in scope or
  requirements.
- **A target that would need a fourth review round**, whatever the
  concerns: investigate the design rather than cycling reviewers.
