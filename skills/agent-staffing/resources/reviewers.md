# Reviewers

Spawn `@reviewer` with `--skills` matched to the change's risk areas.
Different focuses and different models give you breadth, not redundant
coverage of the same concern.

## Skill Picker

| Review kind | Spawn | When |
|-------------|-------|------|
| Default static review | `@reviewer` | Always for code changes: correctness, contracts, security |
| Strict maintainability | `@reviewer --skills thermo-nuclear-review` | Structure/branching changes, spaghetti growth |
| Architecture / seams | `@reviewer --skills thermo-nuclear-review` | Cross-module boundary changes, dependency direction |
| Test structure | `@reviewer --skills test-architecture` | Test suite changes |
| Design alignment | `@reviewer --skills review-alignment` | Cross-artifact fidelity vs design/requirements |
| Frontend structural | `@reviewer --skills react-architecture` | React component boundaries, state, tokens |
| Doc structure | `@reviewer --skills tech-docs,llm-writing,md-validation` | Doc-heavy changes |

Stack multiple: `@reviewer --skills review,thermo-nuclear-review`.
The change itself tells you which perspectives matter.

## Fan-Out Models

Fan out reviewers across models for perspective diversity. Use `-m` to override the default:

- `sol`: thorough, finds subtle issues
- `opus`: best long-context judgment

Three reviewers with different models on the same prompt surface more than three of the same model.

## When to Review

Use reviewer fan-out at three points: design review, major implementation
convergence after a coherent batch, and the final end-to-end review. Tiny
intermediate fixes are tester-driven; reviewers are escalation-only there.

## Between Convergence Points

Involve reviewers between convergence points only when testers surface
a concrete issue the coder cannot resolve:

- One reviewer on the specific unresolved concern.
- A second only if the issue spans multiple risk dimensions.
- Feed findings back into coder + tester loops, then continue.

## Synthesizing Findings

Fix valid findings by default. Defer only with explicit rationale in the
decision log. When reviewers disagree, you make the call;
you have the full design and prior context they don't.

If reviews aren't converging after multiple iterations, that's usually a
signal the design has a structural problem; investigate or escalate.
