---
name: agent-staffing
type: reference
description: Load when composing a team or choosing review and verification coverage.
model-invocable: true
---

# Agent Staffing

## Model Selection

Read `resources/model-selection.md` when choosing models or checking visual,
writing, or data-use requirements.

## Parallel Work and Review

Use parallel lanes for independent tasks. Use cross-model fan-out when the
decision needs independent model perspectives. Reviews need a fresh context,
not necessarily a different model.

## Agent Catalogs

- `resources/reviewers.md`: which `--skills` to pass @reviewer by change risk
- `resources/testers.md`: @prober modes, runtime verification, browser, POC
- `resources/builders.md`: @coder, @architect, @web-researcher, @explorer, @session-miner
- `resources/maintainers.md`: @kb-lead, @kb-maintainer, @investigator
