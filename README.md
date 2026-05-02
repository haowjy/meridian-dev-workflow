# meridian-dev-workflow

An opinionated multi-agent dev team for structured software development,
built on [Meridian](https://github.com/meridian-flow/meridian-cli)'s coordination
primitives. Install this and your orchestrator gets a full squad — architects,
coders, reviewers, testers, web-researchers, and documenters — plus workflow
skills that teach it how to run a structured development lifecycle.

Built on [meridian-base](https://github.com/meridian-flow/meridian-base). Both must
be installed.

## Orchestrator Topology

The dev lifecycle splits across orchestrators with distinct ownership:

**product-manager** (interactive) — the primary developer. Translates between
user and technical teams. Requirements gathering, scope sizing, design/plan
approval, redesign routing. Spawns everything downstream.

**design-lead** (autonomous) — owns the technical design. Challenges
feasibility, explores structural options, produces behavioral spec + architecture.

**planner** (autonomous) — decomposes design into executable phases with
parallelism posture, EARS ownership, and staffing.

**tech-lead** (autonomous) — drives phase-by-phase execution. Probes
before coding, routes findings by type, runs verification gates.

**qa-lead** (autonomous) — designs and produces the permanent test
suite after implementation ships. Risk-based strategy, adversarial testing.

**kb-writer** + **kb-maintainer** + **tech-writer** (autonomous, parallel) —
capture decisions and domain knowledge into KB, maintain KB structural health,
and update user-facing docs respectively after implementation.

```bash
# Full lifecycle:
# product-manager → design-lead → planner → tech-lead
#   → qa-lead + kb-writer + kb-maintainer + tech-writer (parallel)
meridian spawn -a product-manager -p 'Build JWT token validation'
```

## Agents

**Orchestrators:**

| Agent | Model | Role |
|---|---|---|
| `product-manager` | (harness default) | Primary developer — requirements gathering, routing, design/plan approval, redesign routing |
| `design-lead` | sonnet 1M | Technical design — challenges feasibility, explores options, produces spec + architecture |
| `tech-lead` | opus | Phase-by-phase execution — probe/code/verify loops, gates, final review |
| `qa-lead` | gpt | Permanent test suite — risk-based strategy, tier design, adversarial testing |

**Design & Planning:**

| Agent | Model | Role |
|---|---|---|
| `architect` | gpt | Explores tradeoffs and produces hierarchical design docs with spec/architecture trees |
| `planner` | gpt | Decomposes design packages into executable phases with EARS-statement ownership and parallelism posture |
| `design-writer` | sonnet | Lightweight design doc writer — post-review updates, scope adjustments, settled design edits |
| `frontend-designer` | opus | UI/UX design specs — layout, hierarchy, motion, aesthetic direction for frontend-coder |

**Implementation:**

| Agent | Model | Role |
|---|---|---|
| `coder` | codex | Production code writer — implements scoped tasks from phase blueprints |
| `frontend-coder` | opus | Production frontend code with distinctive design quality via the frontend-design skill |
| `refactor-reviewer` | gpt | Reduces codebase entropy — structural cleanup, SOLID fixes, dependency untangling |

**Testing & Verification:**

| Agent | Model | Role |
|---|---|---|
| `verifier` | gpt | Runs tests, type checks, and linters — fixes mechanical breakage, reports real issues |
| `unit-tester` | gpt | Writes and runs targeted unit tests for edge cases and regression guards |
| `smoke-tester` | gpt-5.4 | End-to-end testing from the user's perspective — CLI flows, HTTP requests, race probes |
| `browser-tester` | opus | Browser-based QA via Playwright — visual verification, user flows, console errors |

**Review & Analysis:**

| Agent | Model | Role |
|---|---|---|
| `reviewer` | gpt | Deep code review — specify a focus area (security, SOLID, correctness) or leave broad |
| `investigator` | gpt | Brief triage of flagged issues — quick-fixes trivial items, files GH issues for the rest |

**Research & Documentation:**

| Agent | Model | Role |
|---|---|---|
| `web-researcher` | codex | Best practices, library comparisons, and architecture patterns via web search — the external counterpart to `explorer` |
| `explorer` | gpt-5.4-mini | Fast, cheap codebase explorer — reads files, searches code, mines past sessions |
| `kb-writer` | sonnet | Writes and updates the project's knowledge base — decisions, domain knowledge, architecture, synthesized research |
| `kb-maintainer` | gpt | Structural health of the KB — splits, merges, cross-references, staleness, conflict resolution |
| `tech-writer` | sonnet | Writes and maintains user-facing docs — getting started guides, API reference, CLI usage, and tutorials |

## Skills

**Workflow orchestration:**

| Skill | What it teaches |
|---|---|
| `decision-log` | Decision capture — reasoning, alternatives, constraints |
| `dev-artifacts` | Shared artifact convention between orchestrators |
| `context-handoffs` | Context scoping for agent spawns |
| `session-mining` | Session-mining workflow patterns — recover parent-session decisions and delegate bulk transcript reads |
| `architecture` | Problem framing, tradeoff analysis, approach evaluation |
| `planning` | Decomposing design packages into executable phases — EARS ownership, parallelism posture, staffing |
| `agent-staffing` | Team composition — which agents to spawn, how many, what runs in parallel |
| `dev-principles` | Engineering principles LLM agents systematically violate — refactoring, abstraction, deletion, edge cases |
| `dev-artifacts` | Shared artifact convention between orchestrators — v3 layout with spec/architecture trees |

**Agent methodology:**

| Skill | What it teaches |
|---|---|
| `review` | Adversarial code review — severity thinking, structured reporting |
| `issues` | GitHub Issues integration — labels, work-item linking, `gh` CLI patterns |
| `browser-test` | Browser QA methodology — visual verification, accessibility, console errors |
| `smoke-test` | End-to-end testing — CLI, HTTP, race probes, interruption recovery |
| `unit-test` | Focused test writing — edge cases, regression guards, tricky logic |
| `verification` | Build verification — getting tests, types, and lint green |
| `ears-parsing` | Mechanical EARS verification contract for testers — per-pattern parse and per-ID reporting |
| `tech-docs` | Technical writing craft — hierarchical docs, linking strategy, and progressive disclosure |
| `frontend-design` | Distinctive, production-grade frontend interfaces — anti-generic-AI aesthetics |
| `mermaid` | Mermaid diagram syntax rules and validation |

## Cross-Source Dependencies

Several agents load skills from both this repo and `meridian-base`:

- `meridian-spawn` (base) — how to spawn and coordinate agents
- `meridian-work-coordination` (base) — how to manage work items
- `session-mining` (base) — workflow patterns for mining decisions from session history
- `kb-conventions` (base) — KB structure, navigation, writing standards, flag protocol

The install engine warns about cross-source deps but doesn't fail — these
resolve from the base source. Both sources must be installed.

## Install

```bash
meridian mars add meridian-flow/meridian-base
meridian mars add meridian-flow/meridian-dev-workflow
meridian config set primary.agent product-manager
```

## Layout

```
agents/*.md              # Agent profiles (YAML frontmatter + markdown)
skills/*/SKILL.md        # Skills (with optional resources/ subdirectory)
```

## See Also

- [meridian-cli](https://github.com/meridian-flow/meridian-cli) — the Meridian coordination engine
- [meridian-base](https://github.com/meridian-flow/meridian-base) — core coordination layer this builds on
