---
name: planning
description: Use after a design package exists and before coders are spawned — decomposing a design into executable phases and subphases, writing blueprints, mapping dependencies, sequencing refactors, and figuring out parallelism posture. Not the right fit when the design itself is unresolved (escalate back to design instead).
---

# Plan Implementation

Design describes target state. Plan describes execution delta.

The plan is a delta, not a restatement of the full system. The point is to translate design intent into phase-by-phase executable work with explicit ownership and verification.

Planner output must be executable by @impl-orchestrator without hidden assumptions.

See `resources/execution-model.md` for the phase/subphase execution diagram the plan drives.

## Inputs You Must Consume

- `design/spec/` tree
- `design/architecture/` tree
- `design/refactors.md`
- `design/feasibility.md`
- `plan/pre-planning-notes.md`
- `plan/preservation-hint.md` (when present)
- `requirements.md`
- relevant decision/audit artifacts in the work directory

## Thoroughness Is Mandatory

Shallow planning causes shallow implementation, and shallow implementation ships bugs that design and probes already warned about.

Before declaring plan-ready, walk every decision entry, edge case, and audit finding into a concrete phase contract. No input gets to evaporate between your read and the coder's blueprint.

Thoroughness checks:

- Every numbered decision points to an exact phase and artifact owner.
- Every spec edge case points to exact verification evidence ownership.
- Every audit or probe gap points to the phase that closes it.

If any of those checks produce "none," planning is incomplete.

Thorough planning is expensive. Do it anyway. Re-implementing on a thin plan costs more.

## Planning Priorities

- Parallelism-first decomposition with explicit round constraints.
- Structural refactors early when they unlock parallel feature work.
- Complete and exclusive ownership of EARS statements.
- Clear tester lanes and evidence expectations per phase.

## Phase Decomposition

Break work into phases. A phase is substantial enough to deserve its own exit gate — a full verification sweep and reviewer fan-out.

A good phase is:

- **Independently testable** (most important): completion can be verified without waiting on later phases.
- **Bounded to specific files/modules**: ownership is clear and cross-phase collision risk stays low.
- **Right-sized**: substantial enough to matter, small enough for a phase exit gate to be meaningful.

## Subphases

Within a phase, break work into subphases when the phase is large enough that intermediate checkpoints would catch drift earlier than the phase exit gate would.

A subphase is:

- **Smaller than a phase, larger than a commit.**
- **Independently verifiable at a light level** — compiles, existing tests still pass, contract of the subphase holds.
- **Allowed to break things temporarily within the phase** — the phase exit gate catches problems the light verification missed. This is why phases still get the full gate.

Phases can be flat when they are already small. Subphases are explicit when they add checkpoint value.

### Verification Levels

- **Between subphases — light verification.** `@verifier` confirming the build and existing test suite stay green. Quick feedback to keep momentum. Not the place for reviewer fan-out or smoke tests.
- **Phase exit gate — full verification.** `@verifier` (full), `@smoke-tester`, `@unit-tester` or `@integration-tester` as applicable, `@reviewer` fan-out across focus areas, `@refactor-reviewer` for structural health.

Keep blueprints self-contained. Include only context that changes implementation decisions.

## Output Contract

Produce the standard `plan/` package defined by `/dev-artifacts`.
Include staffing concrete enough that `@impl-orchestrator` can execute directly.

## Non-Negotiable Rules

- Sequence the refactor agenda exactly as declared in `design/refactors.md`, including foundational prep entries when present.
- If runtime context is missing, emit a probe-request with specific questions.
- If design preserves structural coupling that blocks decomposition, emit structural-blocking.

## Terminal Shapes

- `plan-ready`
- `probe-request`
- `structural-blocking`
