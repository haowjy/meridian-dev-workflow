# meridian-dev-workflow

Opinionated software development lifecycle methodology for Meridian. A complete dev team — coder, reviewers, testers, investigator, researcher, documenter — plus structured workflow skills for design, planning, implementation, review, testing, and documentation.

Requires [meridian-base](https://github.com/haowjy/meridian-base) to be installed (the `dev-orchestrator` agent references base skills via cross-source dependencies).

## Layout

- `agents/*.md` — installable agent profiles
- `skills/*/SKILL.md` — installable skills (with optional `resources/`)

## Contents

### Agents (11)

| Agent | Model | Purpose |
|---|---|---|
| `dev-orchestrator` | (default) | Full dev lifecycle orchestrator — plans, delegates, drives work to completion |
| `coder` | codex | Production code writer — implements scoped tasks from design docs and plans |
| `reviewer` | gpt | General code reviewer — broad review across all quality dimensions |
| `investigator` | gpt | Bug investigator — brief triage, quick-fix or file GH issue |
| `researcher` | codex | External researcher — best practices, alternatives, web search |
| `documenter` | opus | Technical documentation — synthesizes codebase mirror in `$MERIDIAN_FS_DIR` |
| `explorer` | gpt-5.3-codex-spark | Fast codebase explorer — reads files, searches code, mines past conversations |
| `browser-tester` | opus | Browser-based QA — visual verification, user flows, form testing |
| `smoke-tester` | codex | End-to-end QA tester — testing from the user's perspective |
| `unit-tester` | gpt | Focused test writer — writes and runs targeted unit tests |
| `verification-tester` | gpt | Build verification — runs tests, type checks, and linters |

### Skills (12)

| Skill | Purpose |
|---|---|
| `dev-orchestration` | Development lifecycle orchestration — phase sequencing, agent staffing, complexity routing |
| `architecture-design` | Architecture design methodology — problem framing, tradeoff analysis, Mermaid diagrams |
| `plan-implementation` | Phase decomposition — focused blueprints, dependency mapping, agent staffing |
| `review` | Code review methodology — adversarial mindset, severity thinking, structured reporting |
| `review-orchestration` | Directing reviewers — choosing focus areas, model selection, synthesizing findings |
| `issue-tracking` | GitHub Issues integration — labels, work-item linking, `gh` CLI patterns |
| `browser-testing` | Browser-based QA — visual verification, user flows, accessibility, console errors |
| `smoke-testing` | End-to-end testing from the user's perspective — CLI, HTTP, race probes |
| `unit-testing` | Focused unit test writing — edge cases, regression guards, tricky logic |
| `verification-testing` | Build verification — tests, type checks, linters, mechanical breakage |
| `tech-docs` | Technical documentation — compressed codebase mirror with architecture and decision rationale |
| `mermaid` | Mermaid diagram syntax rules and validation |

## Cross-Source Dependencies

The `dev-orchestrator` agent references skills from `meridian-base`:

- `__meridian-spawn-agent`
- `__meridian-session-context`
- `__meridian-work-coordination`

The install engine's dependency resolver warns about cross-source deps but does not fail — these skills resolve from the separately-installed base source. Both sources must be installed for `dev-orchestrator` to work.

## Install

```bash
# Install everything
meridian sources add @haowjy/meridian-base
meridian sources add @haowjy/meridian-dev-workflow
meridian sources install
```

Requires `meridian-base` to be installed first.

## See Also

- [meridian-channel](https://github.com/haowjy/meridian-channel) — the Meridian coordination engine
- [meridian-base](https://github.com/haowjy/meridian-base) — core coordination layer this builds on
