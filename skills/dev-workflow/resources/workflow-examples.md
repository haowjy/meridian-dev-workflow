# Workflow Command Examples

Use these examples with the `dev-workflow` skill. Adjust model, files, and prompts to the specific work item.

## Entering Design

```bash
meridian work start "descriptive name"
meridian work update $MERIDIAN_WORK_ID --status designing
```

## Entering Review

```bash
meridian work update $MERIDIAN_WORK_ID --status reviewing
```

### Design review fanout

```bash
meridian spawn -a reviewer -p "Review this design with solid lens: correctness, maintainability, SRP, abstractions" \
  -f $MERIDIAN_WORK_DIR/overview.md -f $MERIDIAN_WORK_DIR/decision-log.md

meridian spawn -a reviewer -p "Review this design with planning lens: architectural fit, phase sequencing, dependency graph" \
  -f $MERIDIAN_WORK_DIR/overview.md -f [relevant codebase files]
```

## Entering Planning

```bash
meridian work update $MERIDIAN_WORK_ID --status planning
```

## Entering Implementation

```bash
meridian work update $MERIDIAN_WORK_ID --status implementing
```

## Marking Done

```bash
meridian work update $MERIDIAN_WORK_ID --status done
# or: meridian work done $MERIDIAN_WORK_ID
```

## Implementation Loop

### Spawn coder

```bash
meridian spawn -a coder -m codex \
  -p "Phase N: [clear description of what to implement]" \
  -f $MERIDIAN_WORK_DIR/overview.md \
  -f $MERIDIAN_WORK_DIR/plan/phase-N-slug.md \
  -f [relevant source files]
```

### Verify with tester

```bash
meridian spawn -a tester -p "Verify Phase N: run tests, type check, lint. Fix what's mechanical, report what's real." \
  -f [changed files]
```

### Fan out reviewers

```bash
meridian spawn -a reviewer -p "Review Phase N with solid lens: SRP, abstractions, code quality" -f [changed files]
meridian spawn -a reviewer -p "Review Phase N with concurrency lens: races, deadlocks, shared state" -f [changed files]
meridian spawn wait $SPAWN_ID_1 $SPAWN_ID_2
```

### Fix findings

```bash
meridian spawn -a coder -m codex \
  -p "Fix these review findings in Phase N: [specific findings]" \
  -f [review reports] -f [affected files]
```

## Investigator Pattern

```bash
meridian spawn -a investigator -p "Investigate: [what was flagged]" -f [relevant files]
```

## Cross-Workspace Worktree

```bash
git worktree add ../project-feature-name feature-branch
```
