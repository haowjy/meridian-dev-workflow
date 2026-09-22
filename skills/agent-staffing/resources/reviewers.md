# Reviewers

Spawn `@reviewer` with skills matched to the change's risks.

## Skill Picker

| Review kind | Spawn | When |
|-------------|-------|------|
| Default static review | `@reviewer` | Code review gates: correctness, contracts, security |
| Strict maintainability | `@reviewer --skills thermo-nuclear-review` | Structure/branching changes, spaghetti growth |
| Architecture / seams | `@reviewer --skills thermo-nuclear-review` | Cross-module boundary changes, dependency direction |
| Test structure | `@reviewer --skills test-architecture` | Test suite changes |
| Design alignment | `@reviewer --skills review-alignment` | Cross-artifact fidelity vs design/requirements |
| Frontend structural | `@reviewer --skills react-architecture` | React component boundaries, state, tokens |
| Doc structure | `@reviewer --skills tech-docs,llm-writing,md-validation` | Doc-heavy changes |

## Model Selection

DeepSeek and Luna are options for quick, low-risk checks, not automatic
fallbacks.

## When to Review

Review designs, coherent implementation batches, and final end-to-end behavior.
Use multiple reviewers only when the risk warrants it.

## Between Convergence Points

For small intermediate fixes, escalate to a reviewer only when verification
finds an issue the coder cannot resolve. Scope the review to that issue; add
another reviewer only for a separate risk.

## Synthesizing Findings

Fix valid findings; record reasons for deferrals in the decision log. Resolve
conflicting findings using the design and evidence. If reviews repeatedly fail
to converge, investigate the design or escalate rather than cycling reviewers.
