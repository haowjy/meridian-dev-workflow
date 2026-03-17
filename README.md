# meridian-dev-orchestration

Opinionated software development lifecycle methodology for Meridian. A complete dev team — coder, reviewers, testers, investigator, researcher, documenter — plus structured workflow skills for design → plan → implement → review → test → document.

Requires [meridian-base](https://github.com/haowjy/meridian-base) to be installed (the `dev-orchestrator` agent references base skills via cross-source dependencies).

## Layout

- `agents/*.md` — installable agent profiles
- `skills/*/SKILL.md` — installable skills (with optional `resources/`)

## Contents

### Agents (8)

| Agent | Model | Purpose |
|---|---|---|
| `dev-orchestrator` | opus | Full SDLC orchestrator (loads base + dev skills) |
| `coder` | codex | Production code writer — implements scoped tasks |
| `reviewer` | gpt | General code reviewer — orchestrator sets lens via prompt |
| `tester` | sonnet | Versatile QA — verifies builds, writes tests, runs smoke/browser tests |
| `investigator` | gpt | Bug investigation — brief triage, quick-fix or file GH issue |
| `researcher` | codex | External researcher — best practices, alternatives, web search |
| `documenter` | opus | Technical documentation orchestrator — synthesizes codebase mirror in $MERIDIAN_FS_DIR via explorer subagents |
| `explorer` | codex-spark | Fast codebase explorer — reads files, searches code, mines past conversations |

### Skills (7)

| Skill | Purpose |
|---|---|
| `dev-orchestration` | Development lifecycle orchestration — phase loop, agent staffing, complexity routing |
| `architecture-design` | Architecture design methodology — problem framing, tradeoff analysis, Mermaid diagrams |
| `mermaid` | Mermaid diagram syntax rules and validation script |
| `plan-implementation` | Breaking designs into executable phases — dependency mapping, agent headcount |
| `reviewing` | Adversarial code review methodology — review lenses, severity framework |
| `issue-tracking` | GitHub Issues integration — severity labels, work-item linking, `gh` CLI patterns |
| `tech-docs` | Technical documentation — compressed codebase mirror in $MERIDIAN_FS_DIR with architecture, features, and decision rationale |

## Cross-Source Dependencies

The `dev-orchestrator` agent references skills from `meridian-base`:

- `__meridian-orchestrate`
- `__meridian-spawn-agent`
- `__meridian-work-coordination`

The install engine's dependency resolver warns about cross-source deps but does not fail — these skills resolve from the separately-installed base source. Both sources must be installed for `dev-orchestrator` to work.

## Install

```bash
# Install everything
meridian install @haowjy/meridian-dev-orchestration

# Or selectively
meridian install @haowjy/meridian-dev-orchestration --agents coder,reviewer
```

Requires `meridian-base` to be installed first:

```bash
meridian install @haowjy/meridian-base
meridian install @haowjy/meridian-dev-orchestration
```

## The Lifecycle

```
designing → reviewing → planning → implementing → done
```

Each phase has associated agents and artifacts. The `dev-orchestration` skill orchestrates the full loop; phase-specific skills (`architecture-design`, `plan-implementation`, `reviewing`) teach the craft for each phase.

## See Also

- [meridian-channel](https://github.com/haowjy/meridian-channel) — the Meridian coordination engine
- [meridian-base](https://github.com/haowjy/meridian-base) — core coordination layer this builds on
