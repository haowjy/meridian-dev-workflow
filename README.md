# meridian-dev-workflow

An opinionated multi-agent dev team for structured software development,
built on [Meridian](https://github.com/haowjy/meridian-cli)'s coordination
primitives. Install this and your orchestrator gets a full squad: architects,
coders, reviewers, testers, web-researchers, and documenters: plus workflow
skills that teach it how to run a structured development lifecycle.

Built on [meridian-base](https://github.com/haowjy/meridian-base). Both must
be installed.


## Orchestrator Topology

The dev lifecycle splits across leads with distinct ownership:

**product-lead** (interactive): settles product direction with the user:
intent, requirements, decisions. Gathers evidence through cheap research
spawns, then hands off to the next lead as a new session the user launches.
It does not spawn builders.

**gpt-dev** (interactive): one session that implements and verifies a single
objective itself, spawning a reviewer and prober only at the end (`/solo-dev`).

**ux-lead** (interactive): the same single-session shape for UI work. Converges
on visual direction with the user, then implements and checks the rendering
itself, spawning coders only for big frontend refactors. Hands non-frontend
work to gpt-dev or tech-lead.

**design-lead** (autonomous): owns the technical design. Explores structural
options, produces high-level structure, key interfaces, boundaries, patterns,
and tradeoffs.

**tech-lead** (primary): leads technical work end to end. Makes the
technical decisions, runs a team of agents through long-running work, keeps
several tasks moving at once, and makes small changes itself.

**kb-lead** (autonomous, conditional): coordinates knowledge capture across
.context/, KB, and docs/ layers. Runs once per change from `/post-dev`,
reading the work directory's decision and divergence logs first.

```bash
# Default lifecycle:
# product-lead --handoff--> design-lead --handoff--> tech-lead | gpt-dev
# ux-lead (one session: mockup-dev variants -> ui-implementation)
# kb-lead runs once per change, from /post-dev
meridian -a product-lead
```

## Agents

Models below are profile defaults; ordered alternatives live in each agent's
`model-policies`. See `skills/agent-staffing/` for task-based selection.

**Leads:**

| Agent | Model | Role |
|---|---|---|
| `product-lead` | opus | Product direction: intent, requirements, decisions, handoff |
| `ux-lead` | opus | Visual direction and UI implementation in one session |
| `design-lead` | opus | Technical design: structural options, interfaces, boundaries, tradeoffs |
| `tech-lead` | fable | Technical lead: decisions, an agent team, several concurrent tasks, hands-on fixes |

**Design:**

| Agent | Model | Role |
|---|---|---|
| `architect` | astra | Explores tradeoffs and produces hierarchical design docs with spec/architecture trees |
| `design-researcher` | sol | Researches structural options and writes analysis for the design team |

**Implementation:**

| Agent | Model | Role |
|---|---|---|
| `coder` | deepseek | Production code writer: implements scoped tasks and behavior-preserving refactors |
| `frontend-coder` | deepseek | Production frontend code with visual self-verification via agent-browser |
| `gpt-dev` | astra | Direct implementation lead for well-scoped work |
| `mockup-dev` | luna | Fast frontend mockups and throwaway POCs |

**Testing & Verification:**

| Agent | Model | Role |
|---|---|---|
| `prober` | deepseek | Runtime verifier. Skills: probe, poc, agent-browser |
| `reviewer` | astra | Code reviewer: static and runtime. Skills: review, probe, thermo-nuclear-review, test-architecture, review-alignment |

**Review & Analysis:**

| Agent | Model | Role |
|---|---|---|
| `investigator` | luna | Root-cause diagnosis for broken or suspicious behavior |

**Research & Documentation:**

| Agent | Model | Role |
|---|---|---|
| `web-researcher` | luna | External evidence: library docs, upstream issues, architecture patterns via web search |
| `explorer` | luna | Fast, cheap codebase explorer: reads files, searches code, traces git history |
| `source-researcher` | luna | Studies real open-source implementations for relevant patterns |
| `kb-lead` | opus | Captures durable knowledge: mines the work, writes .context/, KB, and docs/ inline, fans out @explorer/@session-miner to read |

**Visual:**

| Agent | Model | Role |
|---|---|---|
| `browser` | muse-contributor | Browser interaction: scraping, navigation, screenshots. Training-eligible endpoint; select an approved alternative for sensitive context. |
| `imagegen` | sol | Image generation: UI concept mockups, visual explorations, icons |

## Skills

**Workflow orchestration:**

| Skill | What it teaches |
|---|---|
| `session-mining` | Session-mining workflow patterns: recover parent-session decisions and delegate bulk transcript reads |
| `architecture` | Problem framing, tradeoff analysis, approach evaluation |
| `agent-staffing` | Team composition: which agents to spawn, how many, what runs in parallel |
| `parallel-execution` | Coordinate parallel spawns so edit lanes do not collide; fan in before dependent edits |
| `dev-principles` | Simplicity, separation of concerns, structural judgment: the operating lens for code decisions |
| `testing` | Restraint-first testing discipline: tier selection, when NOT to write tests, functional core patterns. Resources cover unit and integration patterns. |
| `probe` | Runtime verification mode-shift: run real commands, exercise real workflows, report what breaks. Two modes: probing (exploratory) and verification (confirmatory). |
| `poc` | Throwaway code that answers a feasibility question: logic spikes or UI exploration. Always deleted. |

**Agent methodology:**

| Skill | What it teaches |
|---|---|
| `review` | Constructive code review: judge the code as it stands, standards and design axes, quality as ease of change, redesign escalation |
| `review-alignment` | Alignment verification: does one artifact faithfully represent another? |
| `divergence` | Track plan divergence during multi-phase work in a `DIVERGENCE/` folder |
| `issues` | GitHub Issues integration: labels, work-item linking, `gh` CLI patterns |
| `react-architecture` | React-specific structural lens: tokens, state, composition, imports, component API consistency |
| `tech-docs` | Technical writing craft: hierarchical docs, linking strategy, and progressive disclosure |
| `unravel-codebase` | Human-invoked guided walkthrough of unfamiliar code: reads alongside you, explains how it works, and doubles as a KB/vocab cleanup pass |
| `ui-implementation` | Production UI follow-through after visual direction is settled |
| `thermo-nuclear-review` | Extremely strict maintainability review: abstraction quality, code judo moves |
| `test-architecture` | Strict test structure audit: fixture sprawl, implementation-pinned tests, deletion targets, test file boundaries |

## Cross-Source Dependencies

Several agents load skills from both this repo and `meridian-base`:

- `meridian-work-coordination` (base): how to manage work items
- `session-mining` (base): workflow patterns for mining decisions from session history
- `knowledge-layers` (base): where knowledge lives: AGENTS.md, .context/, KB, docs/, work directories

The install engine warns about cross-source deps but doesn't fail: these
resolve from the base source. Both sources must be installed.

## Install

```bash
meridian mars add meridian-flow/meridian-base
meridian mars add meridian-flow/meridian-dev-workflow
meridian config set primary.agent product-lead
```

## Layout

```
agents/*.md              # Agent profiles (YAML frontmatter + markdown)
skills/*/SKILL.md        # Skills (with optional resources/ subdirectory)
```

## See Also

- [meridian-cli](https://github.com/meridian-flow/meridian-cli): the Meridian coordination engine
- [meridian-base](https://github.com/meridian-flow/meridian-base): core coordination layer this builds on
