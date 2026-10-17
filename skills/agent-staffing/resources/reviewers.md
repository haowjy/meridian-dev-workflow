# Reviewers

Spawn `@reviewer` with skills matched to the change's risks.

## Skill Picker

| Review kind | Spawn | When |
|-------------|-------|------|
| Default review | `@reviewer` | Every review gate: correctness, maintainability, efficiency, security |
| Strict maintainability | `@reviewer --skills thermo-nuclear-review` | Every phase gate and final gate, beside the default reviewer; structure/branching changes, spaghetti growth |
| Efficiency | `@reviewer` with the efficiency lane named in the prompt | Runtime paths, polling, persistence, scans, startup |
| Architecture / boundaries | `@reviewer --skills thermo-nuclear-review,architecture` | Cross-module boundary changes, dependency direction. Repeat findings: one concern (the code behind one responsibility) would need a third round of fixes; after the investigator's root cause, review the system as a whole with every earlier report, and report whether the findings share a cause, and either the move that ends it or frame-rot |
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
at every gate.

DeepSeek and Luna are options for quick, low-risk checks, not automatic
fallbacks.

## Synthesizing Findings

Fix valid findings; record reasons for deferrals with the work item's
decisions. Resolve conflicting findings using the design and evidence. A
concern that would need a third round of fixes calls for root-cause
investigation and an architecture review of the system as a whole, not
another reviewer on the next delta. When a change would need a fourth
review round, whatever the concerns, investigate the design or escalate
rather than cycling reviewers.
