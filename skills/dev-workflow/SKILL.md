---
name: dev-workflow
description: Development lifecycle orchestration — sequencing design, review, planning, and implementation phases with multi-agent coordination. Use this whenever you're working on a feature, refactor, or bug fix that involves more than one step. Activate for any task that benefits from phased execution, subagent delegation, or structured review — even if the user doesn't explicitly ask for a "workflow."
---
# Dev Workflow
You orchestrate lifecycle phases, delegate execution/review, and keep state visible so future agents can resume cleanly.
This skill defines phase order and gates. Use `architecture-design` and `plan-implementation` for phase-specific craft.
This skill assumes `__meridian-work-coordination` owns work setup, status semantics, and artifact placement. Use `$MERIDIAN_WORK_DIR` for work-scoped tracking.
All command examples live in `resources/workflow-examples.md`.

## The Lifecycle
Set status with `meridian work update --status <status>`:
```
designing -> reviewing -> planning -> implementing -> done
```
Not every task needs every phase. Scale ceremony to complexity.

### Status vocabulary
| Status | Meaning |
|--------|---------|
| `designing` | Explore the problem and write design artifacts |
| `reviewing` | Stress-test the design with reviewers |
| `planning` | Decompose approved design into phases |
| `implementing` | Execute phases against the plan |
| `done` | Phases complete, tests pass, shippable |

## Routing by Complexity
Assess scope first. Over-coordination on simple work creates noise.

**Trivial** — typo, config change, one-liner  
Do it yourself or spawn one coder. No reviewers, no tester.

**Small** — scoped bug fix, simple feature, <5 files  
Skip design/review and go to `implementing`. Coder -> tester (verify mode) -> one reviewer (best-fit lens). Usually one phase, no plan files.

**Medium** — multi-file feature, moderate refactor, new module  
Light design (`overview.md`), no adversarial design review. Plan 2-4 phases. Coder -> tester (verify mode) -> two reviewers per phase.

**Complex** — architecture change, subsystem, cross-cutting refactor  
Use full lifecycle: design doc, adversarial review, detailed planning, phased implementation with full review gates.

**Exploratory** — unclear scope before committing  
Research the landscape yourself (or spawn a researcher for external best practices), then choose the actual tier.

Keep status visible, decisions durable, and verification enforced (scaled by tier).

## Phase Transitions
Use `resources/workflow-examples.md` for all transition commands.

### Entering design (`designing`)
Read `architecture-design` for method. Before designing, run `meridian work list`. If another work item touches the same area, run `meridian work show <name>` to understand what it's doing, then design with awareness so the efforts do not conflict. If overlap is significant, surface it to the user and decide whether to coordinate, wait, or define an explicit boundary. Log coordination decisions in `implementation-log.md` (`coordination` category).

### Entering review (`reviewing`)
Fan out 2-3 reviewers with different lenses. Synthesize by severity:
- **CRITICAL**: must fix before proceeding.
- **HIGH**: fix or explicitly accept with rationale.
- **MEDIUM/LOW**: log and continue.
When reviewers disagree, decide and record in `decision-log.md`. Escalate if uncertain. If design changes substantially, run at most one extra review round (max two rounds total).
Exit review when CRITICAL items are resolved and HIGH items are fixed or explicitly accepted.

### Entering planning (`planning`)
Read `plan-implementation` for phase decomposition, dependencies, and staffing.

### Entering implementation (`implementing`)
Start `implementation-log.md` at entry. Append bugs, unexpected behaviors, deferred findings, and backlog candidates. Use `resources/artifacts.md` formats.

### Marking done
Before `done`:
- All phases implemented and reviewed.
- Full-suite tests pass.
- No unresolved CRITICAL `implementation-log.md` items.
- Deferred items tracked locally or as GH issues (via investigator).

## The Implementation Loop
Repeat per phase. Use `resources/workflow-examples.md` for all loop commands.

For each phase, spawn a coder with full context: design docs, phase spec, relevant code, and explicit boundaries. Read the coder report for drift and surprises, and keep the phase moving when tangential issues appear by spawning an investigator in parallel.

Next, run a tester in verify mode (tests, type checks, lint). The tester handles mechanical breakage and reports substantive issues so reviewers can focus on higher-value review work. Then fan out 2-3 reviewers with distinct lenses and synthesize findings by severity.

| Severity | Action |
|----------|--------|
| CRITICAL | Fix now, then re-review |
| HIGH | Fix now or defer with rationale |
| MEDIUM | Investigator decides quick-fix vs GH issue |
| LOW | Log if useful and move on |

If fixes are needed, spawn targeted coder fixes and re-review until the phase converges. Cap this loop at three cycles; if it is still unstable after that, escalate to the user because the issue is likely structural.

Before moving to the next phase, confirm tests pass, changes are committed with clear messages, plan status is updated, and deferred items are logged in `implementation-log.md`. If plan assumptions changed, update phase files and record decision updates.

## The Investigator Pattern
Coders/reviewers will surface out-of-scope findings (adjacent bugs, surprises, improvements). Do not derail the active phase.
Spawn an `investigator` to handle findings in parallel. Investigator quick-fixes trivial safe items or files GH issues with evidence.
You do not need `issue-tracking` directly here; the investigator carries it. Your role is triage and orchestration.

## Cross-Workspace Coordination
When multiple work items are active, run `meridian work list` before design, use `meridian work sessions <name>` to see which sessions have touched each item, and read overlapping design docs. During implementation, log overlap in `implementation-log.md` with `coordination` category. Use separate git worktrees to isolate parallel efforts (see `resources/workflow-examples.md`). Each worktree is file-isolated, and coordination remains visible via `meridian work list` and `meridian work show`.

## Tracking Artifacts
All tracking artifacts live in `$MERIDIAN_WORK_DIR/`:
```
$MERIDIAN_WORK_DIR/
  overview.md              # Design: problem, approach, architecture
  decision-log.md          # Append-only decisions (D-1, D-2, ...)
  implementation-log.md    # Append-only findings (IL-1, IL-2, ...)
  plan/
    phase-1-slug.md        # Per-phase implementation specs
    phase-2-slug.md
    ...
```
Use `resources/artifacts.md` formats for `decision-log.md` and `implementation-log.md`.
