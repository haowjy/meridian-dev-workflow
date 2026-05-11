# Changelog

Caveman style. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [SemVer](https://semver.org/). Versions before 0.0.14 in git history only.

## [Unreleased]

### Changed
- `@qa-lead`: gpt-5.4 (Codex) → sonnet (Claude). Orchestrators need native blocking spawn-wait, not Codex poll loops. Sonnet handles test design decisions fine.

## [0.5.10] - 2026-05-11

### Changed
- `dev-principles`: added Testing section — coders verify by running the program, fix broken tests, leave new test design to dedicated testers. Stops coders from padding changes with hundreds of lines of unit tests.
- `@coder`: "verify proportionally to blast radius" → "verify by running the code, not by writing tests."

## [0.5.9] - 2026-05-11

## [0.5.8] - 2026-05-10

### Added
- `@qa-design-lead`: analysis-only agent spawned by @qa-lead when the test suite has structural problems. Reads test files and explorer report, produces `design/test-strategy.md`. No sub-spawning — pure analysis and doc writing. Covers tier audit, diff analysis of coder-touched tests, anti-pattern inventory, conftest map, decomposition plan.

### Changed
- `@qa-lead`: full loop driver — explores first (spawns @explorer), decides whether to spawn @qa-design-lead for heavy redesign or proceed inline, runs one @reviewer pass, then hands off to `@coder --skills unit-test` or `@coder --skills integration-test`. Adds Edit tool for `# qa-validated: <work-item>` markers. Drops direct use of @unit-tester and @integration-tester in favor of `@coder` + skill routing.

## [0.5.7] - 2026-05-10

### Changed
- `@kb-lead`: loads `qi-layer` — placement rules inform routing decisions (what goes to @code-mirror vs @kb-writer).

## [0.5.6] - 2026-05-10

## [0.5.5] - 2026-05-10

### Changed
- `@code-mirror`: loads `qi-layer` skill, body trimmed — placement rules now in skill, body focuses on writing craft.

## [0.5.4] - 2026-05-10

### Changed
- `@kb-lead`: step 5 (structural health) explains why it's sequenced after writers — new pages create orphan nodes and break cross-references.

## [0.5.3] - 2026-05-10

### Added
- `@code-mirror` agent: focused writer for .context/CONTEXT.md and AGENTS.md — inline knowledge colocated with source code. Sonnet model, workspace-write sandbox.
- `@kb-lead` agent: post-implementation knowledge capture coordinator. Routes to @code-mirror (.context/), @kb-writer (KB), @tech-writer (docs/). Replaces product-lead's parallel kb-writer + tech-writer + kb-maintainer spawns.

### Changed
- `@product-lead`: post-implementation routing simplified — spawns @qa-lead + @kb-lead instead of three parallel doc agents + sequential kb-maintainer. Passes work directory context (`-f $(meridian work current)`) to kb-lead. `<delegate>` tag uses behavioral framing instead of role identity.
- `@tech-lead`: replaced contradictory "every action is a spawn" absolute with scoped behavioral guidance. `<delegate>` tag uses behavioral framing.
- `@planner`: replaced brittle verb-inference routing rule with spawn-identity check. "Parallelize aggressively" → "parallelize when independence is proven."
- `@investigator`: replaced recursive self-spawning with @explorer/@smoke-tester delegation for narrow probes.
- `@tech-writer`: fixed wrong-agent routing — @explorer for reading, @smoke-tester for runtime verification. "Important information first" → lead with user action/command/behavior.
- `@alignment-reviewer`: replaced contrastive definition with positive framing.
- `@ux-lead`: `<delegate>` tag uses behavioral routing instead of role identity.
- `@unit-tester`, `@integration-tester`: descriptions reframed positively instead of "not the right fit for."
- `agent-staffing`: "delegation is mandatory" → "delegation is the default" with coordination-artifact exception.
- `agent-staffing/reviewers`: over-absolute skip rule replaced with decision-log rationale.
- `agent-staffing/testers`: "only verification that matters" → "mandatory behavioral lane."
- `agent-staffing/builders`: empty superlative replaced with specific @web-researcher staffing guidance.
- `issues`: over-absolute filing rule replaced with durable-tracking test. Silent `gh` failure → explicit reporting.
- `unit-test`, `integration-test`: descriptions reframed positively.

## [0.5.2] - 2026-05-10

## [0.5.1] - 2026-05-09

### Changed
- `/dev-principles`: separation of concerns now explains the LLM-agent cost — smaller files mean less context consumed per read.

## [0.5.0] - 2026-05-09

### Changed
- `/dev-principles`: rewritten from SOLID-based to simplicity-centered — entanglement reduction, separation of concerns (Dijkstra), rhetorical questions over rules. Replaces `design-principles` and `refactoring-principles`.
- `@coder`: broadened to include structural refactors (absorbed `@refactor-coder`). Description and body updated.
- `@reviewer`: structural health added as a focus lane (absorbed `@refactor-reviewer`). Description updated.
- `@tech-lead`: references updated — `@coder` for refactors, `@reviewer` with structural focus. Worktree section now uses `/meridian-work-coordination` instead of `/feature-worktree`.
- `@design-lead`: design methodology folded into agent body (was in deleted `design-principles` skill). Skills list updated.
- `@alignment-reviewer`: simplified reviewer references.
- `@product-lead`: simplified reviewer references.
- `agent-staffing`: removed `@refactor-reviewer` from catalogs, updated structural review routing.
- `execution-model`: removed `@refactor-coder` from mermaid diagram, `@refactor-reviewer` → `@reviewer (structural focus)`.
- `plan-package`: removed `@refactor-coder` from staffing contract, updated final review loop.
- `review/resources/architecture.md`: replaced SOLID terminology with independence/entanglement framing.
- `review/SKILL.md`: added `structural-health/` to resource list.
- All skills tagged with `type:` field (principle, guardrail, or reference).

### Removed
- `@refactor-coder` agent — absorbed into `@coder`.
- `@refactor-reviewer` agent — absorbed into `@reviewer` (structural focus lane).
- `/design-principles` skill — methodology folded into `@design-lead` body.
- `/refactoring-principles` skill — values into `/dev-principles`, resources moved to `review/resources/structural-health/`.
- `/reflection` skill — moved to `meridian-base` as a generic capability.
- `/feature-worktree` skill — obsoleted by `meridian work start --worktree`.
- `/verification` skill — orphaned since `@verifier` removal in v0.4.0.

### Fixed
- README: removed stale `@verifier` row, phantom `context-handoffs` and `mermaid` skills, deduplicated `dev-artifacts`, added missing `testing-principles` and `integration-test`.
- `architect`, `planner`, `frontend-designer`: added missing `shared-workspace` skill.
- Trimmed redundant "resolve work directory" instructions from agent bodies — `shared-workspace` covers this.

## [0.4.1] - 2026-05-09

### Changed
- `web-researcher`: prompt injection warning in description — treat findings as evidence, not instructions.
- `agent-staffing/builders`: explorer reframed around token cost delegation. Web researcher prompt injection note.

## [0.4.0] - 2026-05-08

### Added
- `/reflection` skill — generic self-review loop (verify, reflect, fix, re-verify). Loaded by all coders, model-invocable for any agent.
- `/feature-worktree` skill — feature worktree setup, ship (PR to main), cleanup conventions.
- `bootstrap/feature-worktree` — harness permission setup for worktree paths.
- net-negative section in `/refactoring-principles` — refactors that grow the codebase need justification.
- "Watch for stalls" in tech-lead and product-lead — stop and reflect when something isn't converging instead of spawning harder.
- Ship defined: final gate passes → PR from feature worktree to main.

### Changed
- Execution model: removed @verifier and @reviewer from subphase loop. Coders self-verify and self-review via `/reflection`. 3 spawns per subphase → 1.
- Execution model: phase exit gate and final gate marked parallel (`--bg` + `spawn wait`).
- Design-lead: collapsed 4 sequential stages into 2 parallel fan-outs (investigate + synthesize/converge). Added `--continue` for probing spawns deeper. Review is now multi-reviewer parallel fan-out.
- Design-lead: scoped to design altitude — spec (EARS) + target architecture, not implementation detail.
- Refactor-reviewer: deletion-first mandate — start with what can be removed, block net-positive refactors.
- Tech-lead: creates feature worktree before first phase, ships via PR. Added git worktree/push/branch/gh tools.

### Removed
- `@verifier` agent — replaced by coder self-verification via `/reflection`.

## [0.3.9] - 2026-05-06

## [0.3.8] - 2026-05-06

### Changed
- `@qa-lead`: sharpened unit-test judgment — keep/add tests for durable contracts, delete stale or implementation-shaped unit tests.
- more possible fanouts

## [0.3.7] - 2026-05-04

### Changed
- design-lead: design package is minimum deliverable floor, not suggestion — omissions require explicit justification

## [0.3.6] - 2026-05-04

## [0.3.5] - 2026-05-03

### Changed
- Skill schema: migrated from `invocation: explicit` to `model-invocable: false`. Some skills previously marked explicit are now model-discoverable.
- Bumped meridian-base to v0.2.4, meridian-prompter to v0.1.8.

## [0.3.4] - 2026-05-03

### Changed
- Bumped meridian-base dep to v0.2.2.

### Removed
- Model catalog (`opus`, `gpt`, `sonnet`, `codex`, `gptmini`, `gpt55`, `opus47`) — now lives in meridian-base.

## [0.3.3] - 2026-05-03

## [0.3.2] - 2026-05-03

## [0.3.1] - 2026-05-02

### Changed
- Agent profiles: migrated 6 agents from deprecated `models:` to `fanout:` + `model-policies:` (browser, browser-tester, coder, frontend-coder, mockup-gen, refactor-reviewer).
- Skill frontmatter: migrated all 17 skills from legacy `disable-model-invocation`/`allow_implicit_invocation` to canonical `invocation: explicit`.

### Added
- `bootstrap/imagegen-setup/BOOTSTRAP.md`: documents Codex `[features] image_generation = true` config requirement for imagegen agent.

## [0.3.0] - 2026-05-02

### Changed
- `@product-manager` → `@product-lead`. Role name reflects leadership over product direction, not middle-management.

#### LLM writing cleanup and skill propagation
- `@tech-writer`: added `intent-modeling` — mines conversation history for what to document.
- `@architect`: re-added `tech-docs` skill (was removed prematurely, before recognizing tech-docs is design doc methodology).
- `@design-writer`: added `tech-docs` skill. Body trimmed — inlined mermaid/link-checker guidance replaced with skill references.
- `@imagegen`: added `intent-modeling`. Description now tells callers to specify visual intent before spawning. Body addresses underspecified prompts. Removed prescribed work directory output.
- `@smoke-tester`: description rewritten to cover both probing and verification modes equally.
- `@investigator`: split `@explorer` reference into `@explorer` (codebase) + `@session-explorer` (sessions). Trimmed contrastive filler.
- `@web-researcher`: updated routing for explorer/session-explorer split.
- `@refactor-coder`: positive opener (was "not to add features; it is to improve"). Cut orchestrator-scoping "good units" list. Trimmed skill restatement in Refactoring Posture. Compressed Behavior Preservation.
- `@refactor-reviewer`: compressed "What to Look For" — references skill instead of duplicating 8-bullet list.
- `@alignment-reviewer`: scope discipline flipped from negative list to positive routing.
- `@unit-tester`: trimmed "safety net" metaphor.
- `@verifier`: trimmed "clearing mechanical noise" restatement.
- `@frontend-coder`: trimmed "separate polished UI from functional-but-flat" filler.
- `@mockup-gen`: trimmed redundant "not production code" from body opener (description already routes on this).
- `refactoring-principles` skill: "not tidiness for its own sake" → "the goal is making the next change smaller."
- `architecture` skill: reshaped from process prescription (frame → explore → compare → stress-test) to shared vocabulary (boundaries, dependencies, tradeoff dimensions, structural risk). All three consumers benefit now, not just architect.
- `unit-test` skill: cut "What Unit Tests Are For" section — testing-principles covers tier definition, agent knows what unit tests are.
- `tech-docs` skill: scoped as design document methodology. Removed obsolete `scripts/` (check-md-links replaced by `meridian kg check`). Removed "Writing for Agent Consumers" — readability principles apply to all readers.
- `smoke-test` skill: rewritten for equal probing/verification coverage. Killed contrastive "ARE and ARE NOT" section.
- `agent-staffing/builders.md`: added `@session-explorer` entry with routing guidance.
- `agent-staffing/maintainers.md`: updated `@kb-writer` entry for `@session-explorer` delegation.
- `@product-lead`: prescriptive requirements gathering (7 bullet points with examples) compressed to principles. Added `intent-modeling` skill — handles hypothesis-vs-spec reasoning that was hand-rolled in the body.
- `@tech-lead`: trimmed 211→105 lines. Cut execution loop duplication with `planning/resources/execution-model.md` (was restating the entire subphase/gate/final-gate loop). Cut prescriptive "Before Any Final Report" checklist — replaced with two report shapes. Added `intent-modeling` — launch prompt interpretation and redesign-brief judgment are intent calls. `@product-manager` refs → `@product-lead`.
- `@design-lead`: trimmed 184→105 lines. Cut 40-line "Design Artifact Hygiene" section (detailed kb-maintainer instructions) to one sentence. Cut "Refactoring Awareness" section that restated `refactoring-principles` skill. Fixed stale `meridian spawn -a architect-lead` in description. Added `llm-writing`.
- `@planner`: trimmed 131→95 lines. Cut prescriptive thoroughness checklist into prose principles. `@product-manager` refs → `@product-lead`. Added `llm-writing`.
- `@qa-lead`: trimmed 136→75 lines. Collapsed step-by-step "Strategy Before Tests" into principle-level guidance. Collapsed "Produce Tests" prescriptive sections.
- `@tech-writer`: trimmed 100→60 lines. Cut "Writing Principles" section (generic writing advice now covered by `llm-writing`). Compressed Diátaxis to bullets. Added `llm-writing`.
- `@design-writer`: trimmed 67→45 lines. Cut "Quality Bar" checklist. Added `llm-writing`.
- `@architect`: added `llm-writing`.
- `@frontend-designer`: added `llm-writing`.
- `@reviewer`: `models:` fan-out field → `fanout:` (new schema).
- `@design-lead`, `@qa-lead`, `@ux-lead`: added `intent-modeling`. All orchestrators interpret caller intent and make escalation/routing judgments.
- `@ux-lead`: `@product-manager` refs → `@product-lead`.
- `review` skill: trimmed 76→50 lines. Cut "What wastes everyone's time" (negative framing). Cut "How to Conduct the Review" prescriptive steps. Description trigger-first.
- All skill descriptions: trigger-first ("Load when..." / "Use when...") instead of content-first. Fixed: `agent-management`, `design-principles`, `dev-principles`, `planning`, `refactoring-principles`, `testing-principles`, `browser-test`, `ears-parsing`, `issues`.
- `issues` skill: trimmed 114→38 lines. Cut prescriptive examples, negative framing ("When NOT to Create"), verbose workflow integration. Opening now leads with "agents systematically under-file" to counter the actual failure mode.
- `@product-lead`, `@design-lead`, `@tech-lead`, `@qa-lead`: added `issues` skill — leads triage reviewer findings and should file non-blocking issues rather than losing them.
- `@coder`, `@smoke-tester`: added `issues` skill — discover file-worthy problems during implementation and testing.
- All `@product-manager` and `@architect-lead` references updated across agents and skill resources.

## [0.2.3] - 2026-05-02

### Changed
- `@architect-lead` → `@design-lead`. Name reflects what the agent does (orchestrate the design process) not what it delegates to (`@architect`). People were already used to `design-orchestrator`.
- `@design-lead` completion: caller-agnostic, report summarizes design package and key decisions. Removed orphaned "work-item tier" jargon and `@product-manager` special-case.
- `@architect`: uses `WebSearch`/`WebFetch` directly instead of spawning `@web-researcher`. One fewer spawn depth level.
- `@frontend-designer`: removed mockup section — mockups are `@mockup-gen`'s job. Boundary is now specs vs demos.

## [0.2.2] - 2026-05-01

### Changed
- `@product-manager`: `<delegate_writing>` → generic `<delegate>` block. Covers all work types (investigation, diagnosis, implementation, writing) not just file writes. Bright-line test: "if you're reading source files, reproducing errors, or running non-git commands, you've crossed into work that belongs to a spawn." Same exceptions (requirements.md, prompt files, explicit user request).

## [0.2.1] - 2026-05-01

### Removed
- `meridian-cli` from cross-source dependencies in README (skill deleted from meridian-base).

## [0.2.0] - 2026-04-30

### Added
- `@alignment-reviewer` agent: coverage verification — checks whether one artifact delivers what another promised (plan vs design, impl vs spec, code vs architecture). Takes source of truth via `-f`, optional conversation context via `--from`. Reports items as Covered/Gap/Partial/Drift. Model: gpt55, read-only.
- `@frontend-dev` agent: primary visual/UX entry point — the visual counterpart to @dev-orchestrator. Works directly with user to iterate on design through rapid mockup cycles. Opus model, `harness: claude`, `approval: yolo`. Spawns @mockup-gen, @browser, @frontend-designer, @frontend-coder, @browser-tester, @imagegen.
- `@mockup-gen` agent: fast throwaway visual mockups using the project's real frontend components and design system. Speed over polish — hardcode data, skip edge cases, get something visual in front of the user fast. Model: gpt55.
- `@imagegen` agent: native image generation. UI concept mockups, visual explorations, icons, reference imagery. Usually spawned on explicit user request. Model: gpt55.
- `@browser` agent: general-purpose browser interaction via `playwright-cli`. Scraping, data extraction, screenshots, interactive annotation, design research — the prompt defines the purpose. Model: gpt55.
- `playwright-cli` dependency: Microsoft's `@playwright/cli` skill for harness-agnostic browser automation via Bash. Replaces Playwright MCP plugin.

- `dev-artifacts`: path discovery updated — context dirs available as `$MERIDIAN_CONTEXT_*_DIR` env vars alongside CLI commands.

### Changed
- **Role renames**: `dev-orchestrator` → `product-manager`, `design-orchestrator` → `architect-lead`, `impl-orchestrator` → `tech-lead`, `test-orchestrator` → `qa-lead`, `frontend-dev` → `ux-lead`. Real-world titles prime for delegation over micromanagement.
- **Skill rename**: `orchestrate` → `agent-management`. Body vocabulary updated to manager/lead.
- **Skill list rebuild**: 56→39 loads across coordinators. Each role loads only what it actually needs.
- **New `design-principles` skill**: split from dev-principles — spec-driven development, treat requirements as hypotheses, edge-case thinking, probe before committing. ~400w.
- `dev-principles`: slimmed 1001→457w after design-principles extraction.
- `browser-test`: trimmed 478→164w. Methodology only, mechanics in `/playwright-cli`.
- `decisions.md` decoupled — no longer mandatory file path. Decisions belong in relevant design docs.
- All skills get explicit invocation-control flags. `issues` explicitly flipped as safety net.
- `agent-staffing`: vocabulary → manager/lead. Cross-references updated throughout resources.
- `AGENTS.md`: updated with `mars version` release guidance.
- `mars.toml`: removed `caveman` dependency.
- `@design-orchestrator`: new "Design Artifact Hygiene" gate before returning design-ready. Spawns `@kb-maintainer` in explicit target-tree mode (`-f design/`) — splits mixed-purpose docs, resolves contradictions, extracts rejected approaches to `design/alternatives.md`, enforces `design/index.md` as reading-order entry point. Deletion tightened: only when content is explicitly duplicated or clearly superseded by cited replacement; unindexed docs get relinked or flagged before deletion. `feasibility.md` scoped to probes/evidence/constraints, decisions go in `decisions.md`. Gate runs after review loops converge, before terminal report.
- `@design-orchestrator`: Completion now caller-agnostic — returns design-ready to whoever spawned it. @planner spawn only when caller explicitly delegated autonomous planning. When caller is @dev-orchestrator, it owns user approval gate and planner handoff. Technical feasibility pushback also routes to caller, not hardcoded @dev-orchestrator. Enforced via `<do_not_spawn_planner>` constraint block.
- `@dev-orchestrator`: frontmatter no longer forces generic `effort: high`; model alias policy now owns effort default.
- `@dev-orchestrator`: checkpoints now explicitly pass behavioral spec (`-f design/spec/`) to planner and impl-orchestrator when present — EARS traceability mandatory when EARS exist. Fixed stale `@prompt-writer` → `@prompter-orchestrator` reference. Routing table clarifies coder vs frontend-coder: functional (logic, state, routing, data flow) vs visual (design fidelity, aesthetics, UI polish).
- `@impl-orchestrator`: scope clarified — functionality, logic, structure, and design alignment. Can touch frontend code for functional concerns; visual/UX iteration belongs to @frontend-dev. Phase exit gate gains @alignment-reviewer lane for EARS verification + @browser-tester for functional frontend verification. Can respawn @planner mid-flight when EARS gaps found at phase gates. Final gate uses @alignment-reviewer with full design package for holistic design-intent check.
- `@planner`: "or lighter context" removed — requires design package with requirements, no escape hatch. Can be spawned by @impl-orchestrator for mid-flight plan adjustment. Two new thoroughness checks: every requirement in `requirements.md` maps to a delivering subphase, every EARS statement maps to a subphase whose blueprint actually scopes the work (table assignment alone is not delivery).
- `@coder`: description reframed from file-type restriction to intent-based routing. Now full-stack: backend, frontend logic, CLI, infrastructure, data flow, build systems. "Do not use for React, TSX, CSS" restriction removed. Description adds spawn/prompt guidance (subphase, EARS statements, integration boundaries).
- `@frontend-coder`: model `claude-opus-4-6` → `gpt55` (clear specs don't need Opus aesthetic judgment — GPT executes faithfully against design targets). Fan-out updated `opus`/`opus47` → `gpt55`/`codex`. Description reframed: pick when visual quality and design fidelity are the primary concern, not just because file is frontend code. Body shifted from autonomous aesthetic judgment ("generic UI is a failure") to faithful spec execution ("match the visual target"). Adds mockup/screenshot guidance.
- `@refactor-coder`: dropped "scoped" filler from description. Added prompt guidance: state structural move and behavior-preservation constraints.
- `@browser-tester`: model `claude-opus-4-6` → `gpt55` (GPT excels at computer use). MCP Playwright plugin → `playwright-cli` skill (harness-agnostic CLI). Sandbox → `danger-full-access` (browser automation needs it). Description adds spawn/prompt guidance.
- `browser-test` skill: refactored to methodology-only — references `/playwright-cli` for browser mechanics instead of teaching Playwright usage.
- `agent-staffing/builders.md`: coder catalog entries updated — @coder is full-stack, @frontend-coder is visual design fidelity. Added @mockup-gen, @imagegen, @browser entries.
- `agent-staffing/testers.md`: @browser-tester entry updated for `playwright-cli` usage and `--annotate` for interactive browser sessions.
- `agent-staffing/reviewers.md`: added @alignment-reviewer entry with usage at plan verification and impl final gate.
- `@dev-orchestrator`: `@code-documenter` → `@kb-writer` in routing and post-impl. Post-impl now spawns `@kb-maintainer` after kb-writer completes for structural health.
- `@impl-orchestrator`: `@code-documenter` → `@kb-writer`, `@kb-maintainer`, `@tech-writer`.
- `@test-orchestrator`: description updated — runs parallel with `@kb-writer` not `@code-documenter`.
- `agent-staffing/maintainers.md`: `@code-documenter` → `@kb-writer` + `@kb-maintainer` entries.
- `dev-artifacts/ownership.md`: KB ownership updated to @kb-writer/@kb-maintainer. Documentation layers reframed — KB is persistent knowledge base, not code mirror. Points to `/kb-conventions`.
- `dev-principles` skill: added "Diagram First" section — default to mermaid diagrams for structural communication.
- README: topology, agent table, lifecycle, and cross-source deps updated for KB agents and explorer move.

### Removed
- `@code-documenter` agent: replaced by `@kb-writer` + `@kb-maintainer` in meridian-base.
- `@explorer` agent: moved to meridian-base — generic cheap reader, not dev-workflow-specific.
- `decision-log` skill: moved to meridian-base for broader reuse.
- `session-mining` skill: moved to meridian-base for broader reuse.

## [0.1.7] - 2026-04-25

### Changed
- `agent-staffing`: model catalog guidance now `meridian mars models list`. Old `meridian models list` path gone.

## [0.1.6] - 2026-04-25

### Changed
- `@planner`: source writes fenced to active work `plan/` artifacts only. Imperative prompts now re-scoped to planning. Terminal report no longer replaces plan package.

## [0.1.5] - 2026-04-24

### Changed
- mars.toml: model alias overhaul. Removed version-specific pinned aliases (`gpt54`, `opus45`, `opus46`) — agents now use explicit model IDs (`gpt-5.4`, `claude-opus-4-6`, `claude-opus-4-5`). Kept `gpt55` and `opus47` as opt-in pinned aliases for specific model behavior. `gpt` auto-resolve pinned to `gpt-5.4` (strongest generalist), `opus` pinned to `claude-opus-4-6` (best instruction-following Opus). Hybrid `model+match` on auto-resolve aliases — pinned winner for resolution, match patterns for `--all` discovery only.
- mars.toml: alias descriptions rewritten. Pinned aliases describe version-specific characteristics (strengths, weaknesses, cost). Auto-resolve aliases describe the role/category. No more duplication between layers.
- mars.toml: `default_effort` on all aliases. `autocompact: 30` on `opus` alias (1M context degrades past ~300k).
- 14 agents: model refs changed from deleted aliases to explicit model IDs. `gpt54` → `gpt-5.4` (10 agents), `opus46` → `claude-opus-4-6` (3 agents), `opus45` → `claude-opus-4-5` (1 agent).
- `@reviewer`, `@refactor-reviewer`: `models:` fan-out entries updated from `gpt54`/`opus46` to `gpt`/`opus` aliases.
- `@frontend-coder`: `models:` fan-out entries updated from `opus46` to `opus`.
- Git denylist hardened across all agents: `Bash(git checkout:*)` (was `Bash(git checkout --:*)`), added `Bash(git switch:*)` and `Bash(git stash:*)`.

### Added
- `models:` field on `@coder`, `@frontend-coder`, `@reviewer`, `@refactor-reviewer` — per-model effort/autocompact overrides for fan-out spawns.
- `gpt55` pinned alias: GPT-5.5 opt-in for action-oriented fast work, `default_effort: low`.
- `opus47` pinned alias: Opus 4.7 opt-in, `default_effort: medium`. Description notes: strongest benchmarks but literal instruction-following breaks complex prompts, long-context degrades above 100k, 35% tokenizer cost increase.

## [0.1.3] - 2026-04-24

### Added
- `md-validation` skill added to `@architect`, `@code-documenter`, `@tech-writer`, `@reviewer`, `@design-writer`, `@planner`, `@frontend-designer`.
- "Prefer mermaid diagrams and tree structures" instructions in `@architect`, `@code-documenter`, `@tech-writer`, `@design-writer`.

### Changed
- `@impl-orchestrator`: frontend/UI routing explicit. React, TSX, CSS, Storybook, components, visual states → `@frontend-coder`. UI phases need browser verification, not just typecheck/build.
- `@impl-orchestrator`: broad Bash removed from profile tools. Orchestrator more spawn-only, less self-implementation path.
- `@frontend-coder`: now default for all frontend/UI implementation, not only when aesthetic matters.
- `@coder`: now excludes React, TSX, CSS, Storybook, and user-facing component work.

### Removed
- `mermaid` skill — replaced by `md-validation` from meridian-base.

## [0.1.2] - 2026-04-21

### Changed
- Context backend migration: `.meridian/fs/` → kb (`meridian context kb`), `.meridian/work/<id>/` → work dir (`meridian work current`). All agents and skills use query commands instead of path construction or env vars.
- Agents updated: architect, code-documenter, design-orchestrator, design-writer, dev-orchestrator, frontend-designer — removed path reconstruction, `meridian context --json`, hardcoded `.meridian/fs/` and `.meridian/work/` paths.
- Skills updated: dev-artifacts (layout + ownership), agent-staffing/maintainers, context-handoffs — new `-f folder/` + `-f file` pattern in examples.

### Added
- `@design-writer` agent: lightweight design doc writer for updates, post-review edits, scope adjustments. Sonnet model. Spawned by dev-orchestrator for settled changes — design-orchestrator still writes initial design.
- `@test-orchestrator` agent: designs + produces permanent test suite after impl ships. Risk-based strategy before writing. Adversarial testing phase to counter LLM "verify what works" bias. Iterative refinement loop. Runs parallel with doc agents post-impl.
- `dev-principles`: two new sections at top — "Spec-Driven Development" (requirements → EARS spec → architecture → verified impl, spec is the contract) and "Treat Requirements as Hypotheses" (XY Problem, JTBD framing, solution-free problem statements).

### Changed
- `@impl-orchestrator`: through-execution contract. Phase gates = checkpoints, not stops. Three named early exits (redesign brief, escalated blocker, caller-scoped subset w/ explicit stop language). Final report split: completion-shape vs early-exit-shape. Phase def: "stopping point" → "checkpoint". `<delegate_writing>` block: `>>` and `sed -i` allowed, destructive rewrites banned. "adjust scope" removed from adapt clause.
- `@dev-orchestrator`: post-impl spawn uses `--from $MERIDIAN_CHAT_ID` (was ambiguous "your session ID").
- `orchestrate` skill: new "Match prompt scope to agent scope" clause. Cadence instructions ≠ completion scope.
- `planning` skill: phase def aligned with impl-orchestrator ("stopping point" → "checkpoint").
- `context-handoffs` skill: `--from` covers `<spawn-id>` and `$MERIDIAN_CHAT_ID` (top-level primary at any depth). Worked example added.
- `session-mining` skill: `$MERIDIAN_CHAT_ID` semantics corrected — top-level primary, not parent. Heading, body, frontmatter all fixed.
- `@dev-orchestrator`: reframed as "primary developer / translator between user and technical teams." New requirements gathering section — XY Problem awareness, JTBD-style questioning, first-principles challenge, solution-free gating before routing to design. Specialist routing table expanded: design-writer, smoke-tester for probing, investigator for diagnosis. Post-impl routing: test-orchestrator + code-documenter + tech-writer in parallel with `--from` session context. Planner terminal state handling (probe-request → smoke-tester, structural-blocking → design-orchestrator). Writing constraint: delegate via specialists, exceptions for requirements.md and prompts.
- `@design-orchestrator`: reframed as technical design owner, not problem discovery. Sonnet 1M model, autocompact 30. Explores technical options (not first-principle problems — that's dev-orchestrator). Challenges technical feasibility. Expanded refactoring awareness — "clean codebase is prerequisite, design time is cheapest fix." Spawns explorer, refactor-reviewer, reviewer. Uses smoke-tester for probes not coder.
- `@impl-orchestrator`: broke coder-centrism. New definitions section (phase, subphase, probe, diagnosis — each with right agent). Subphase loop: probe-first step, light reviewer per subphase, route issues by type (impl → coder, behavioral → smoke-tester, root-cause → investigator). Phase gate: one general reviewer (save fan-out for final gate), temp unit/integration tests deleted after. Final gate: reviewer fan-out by focus area, duplicate higher-level with opus, refactor-reviewer on full change set. Judgment/escalation discipline — recognize non-converging cycles, escalate redesign briefs.
- `@planner`: methodology moved from planning skill into agent body (inputs, thoroughness, priorities, output contract, terminal shapes). Parallelism-first. Route by work type — probe/diagnosis lanes before coding.
- `planning` skill: stripped to shared definitions only (phase, subphase, verification levels, probe/diagnosis lanes, fix-cycle routing). Both planner and impl-orchestrator load it without overlap.
- `execution-model.md`: full rewrite. Mermaid diagram matches updated impl-orchestrator — probe step, light reviewer, issue-type routing, refactor-reviewer final-gate only, temp gate tests.
- `plan-package.md`: staffing contract updated — implementer variants, probe/diagnosis steps, routing by finding type.
- `testing-principles` skill: added risk-based testing, testing trophy model (integration-heavy), test behavior not implementation, hermetic by default, DAMP over DRY, LLM-generated test caveats.
- `@tech-writer`: Diátaxis framework (tutorials, how-tos, reference, explanation). Gather context first via explorers + --from. Spawns own reviewer for accuracy. Audience-flexible — adapts to technical level.
- `@code-documenter`: agent-facing format guidance (bullet/key-value over prose, include security/performance/failure modes). Spawns own reviewer for accuracy.
- `@docs-orchestrator`: deleted. Replaced by direct spawns of code-documenter + tech-writer from dev-orchestrator.
- `@coder`: clarified that unclear runtime behavior at integration boundaries → report back to orchestrator for smoke-tester.
- 7 worker agents: added "Your final message is your report — no file needed." (reviewer, refactor-reviewer, explorer, verifier, smoke-tester, investigator, web-researcher)

### Renamed
- `@internet-researcher` → `@web-researcher`. Updated all references across agents and skills.

### Removed
- `@docs-orchestrator` agent: replaced by direct code-documenter + tech-writer spawns with --from context.

## [0.0.31] - 2026-04-19

### Added
- `refactoring-principles` skill: structural-improvement guidance for design, impl, and review. Core judgments: refactor early while context fresh, small behavior-preserving moves over big redesigns, duplication beats wrong abstraction but must be discoverable. Structural risk signals catalog. Smell families: `smells/bloaters.md`, `smells/change-preventers.md`, `smells/couplers.md`, `smells/dispensables.md`, `smells/oo-abusers.md`. Refactoring moves: `moves/composing-methods.md`, `moves/moving-features.md`, `moves/organizing-data.md`, `moves/simplifying-conditionals.md`, `moves/dealing-with-generalization.md`. Detection and review-translation resources.
- `@refactor-coder` agent: executes behavior-preserving structural refactors. Spawned when primary objective is structural improvement (naming, locality, legacy isolation, extensibility) not feature shipping. Loads `refactoring-principles`. Model: codex, effort: high. Task-containment rules: one coherent unit per spawn — naming unification, boundary extraction, compatibility isolation, branching consolidation, or obsolete-path cleanup. Reports residual risk and scope misalignment.

### Changed
- `@refactor-reviewer`: full rewrite. Now loads `refactoring-principles`. Structured around smell detection and severity judgment. Body expanded with concrete what-to-look-for list (scattered edits, mixed responsibilities, misleading names, frozen wrong axis, repeated branching, legacy smear, dead structure, cost-free indirection), severity rubric (broad coordinated edits > wrong-place agent edits > weak names > legacy clutter), and selective skill-reference routing table (change-preventers for scattered fan-out, bloaters for oversized classes, couplers for weak locality, dispensables + deprecation-and-legacy for dead structure, moves/ for unclear remedy).
- `@design-orchestrator`: loads `refactoring-principles` skill.
- `dev-principles` skill: trimmed and reorganized.
- `context-handoffs` skill: trimmed.

## [0.0.30] - 2026-04-19

### Added
- `testing-principles` skill: research-backed testing foundation. Kent Beck's Test Desiderata, Gary Bernhardt's Functional Core / Imperative Shell, tier selection (unit vs integration vs smoke), common mistakes catalog.
- `integration-test` skill: middle tier between unit and smoke. Fakes at external boundaries, no real I/O, tests component composition.
- `orchestrate` skill: shared orchestration patterns. Convergence loops, escalation/redesign briefs, delegation discipline, artifact-as-state. All orchestrators load it.
- `@integration-tester` agent: executes integration tests per the new skill.
- `planning/resources/execution-model.md`: phase/subphase loop mermaid diagram. impl-orch and planner point here instead of restating.
- `dev-artifacts/resources/plan-package.md`: phase file structure, artifact contracts. Offloaded from skill body.
- `dev-artifacts/resources/ownership.md`: writer/reader rules, doc layers. Offloaded from skill body.

### Changed
- `smoke-test` skill: dual context — probing mode (research phase, understand behavior) vs verification mode (impl phase, prove correctness). Same tools, different intent.
- `unit-test` skill: references `testing-principles`, language-agnostic, functional-core focus.
- `planning` skill: subphase concept added. Subphases get light verification (build + existing tests), phases get full exit gates (testers + reviewer fan-out). Body trimmed, detail offloaded to resources.
- `dev-artifacts` skill: body trimmed ~55%, detail offloaded to new resources.
- `@impl-orchestrator`: flexible input — works with formal plan, or spawns @planner when no plan exists. Body trimmed ~65% since /orchestrate carries shared patterns.
- `@planner`: can be spawned by @dev-orchestrator or @impl-orchestrator. Description updated. Body trimmed.
- `@design-orchestrator`: loads `refactoring-principles`. Body trimmed ~45%, refactoring awareness section added.
- `@dev-orchestrator`: body trimmed ~50%. Routing rules compressed.
- `@docs-orchestrator`: body trimmed ~40%.
- All orchestrators: `orchestrate` added to skills list, shared delegation/convergence/escalation patterns extracted.

## [0.0.29] - 2026-04-17

### Changed
- `shared-workspace` skill moved to `meridian-base` — base agents (orchestrator, subagent) need it, dev-workflow imports it via dependency.
- `@architect`, `@docs-orchestrator`: spawn syntax teaching condensed to single line referencing `/meridian-spawn` skill.
- `@planner`: `model: gpt-5.4` → `model: gpt`. Use symbolic name, let mars resolve to current best.

## [0.0.28] - 2026-04-17

### Changed
- All agents: comprehensive `disallowed-tools` hardening. Block `ScheduleWakeup` (use `run_in_background` instead), `Cron*`, `PushNotification`, `RemoteTrigger`, `EnterPlanMode`, `ExitPlanMode`, `EnterWorktree`, `ExitWorktree`, `NotebookEdit`. Keep `LSP` and `Monitor` available (code intelligence, background process streaming). Orchestrators keep `Task*` (work tracking). `@dev-orchestrator` keeps `AskUserQuestion` (user clarification). Root cause: p2084 impl-orch used `ScheduleWakeup` to "wait" for child spawn instead of `run_in_background` notification — tool was available despite profile teaching the correct pattern.
- `@impl-orchestrator`: Explore phase removed — verification responsibility stays with `@dev-orchestrator` and `@design-orchestrator` where design decisions are made. Phase Loop simplified: testers + quick `@reviewer` (fast model) run in parallel during each phase, catch obvious issues before final fan-out. Final Review findings route back through Phase Loop, not just coder fixes.

## [0.0.27] - 2026-04-16

### Changed
- All four orchestrators (`@dev-orchestrator`, `@design-orchestrator`, `@impl-orchestrator`, `@docs-orchestrator`): added reiteration line — "Always pass `run_in_background: true` to the Bash tool when invoking `meridian spawn`. The harness returns a task ID immediately and delivers a notification when the spawn terminates, so you stay responsive and can run multiple spawns concurrently." Skill-level teaching already exists in `meridian-spawn` but profile-level reiteration needed to reliably steer models. Root cause: p47 impl-orch spawned planner in background and ended its turn with report "Waiting for planner spawn to complete" — background mode treated as handoff instead of a notification-delivery convenience.
- `@design-orchestrator` and `@impl-orchestrator`: `model: opus` → `model: claude-opus-4-5-20251101`. Version-pinned for autonomous-run stability; pattern-match passthrough in `meridian-cli`'s model resolver routes the raw ID to the Claude harness.

## [0.0.26] - 2026-04-16

### Added
- `@impl-orchestrator` gains explicit **Explore** phase before Plan. Verifies design against code reality — every structural claim in `design/refactors.md` or the architecture tree gets a file:line pointer confirming current code supports it; falsified claims trigger a Redesign Brief *before* any planning burn. Root-caused from R06 workspace-config-design cycle where design narrative ("move composition into factory") didn't match code shape (factory input DTO already carried pre-resolved outputs — the "move" was structurally impossible). Explore is a gate: `plan/pre-planning-notes.md` must exist + be populated before `@planner` spawns. Required fields: verified claims, falsified claims, latent risks not in design, probe gaps, leaf-distribution hypothesis. Previous prompt treated pre-planning notes as a preamble, which made skipping them invisible.
- `@impl-orchestrator` Redesign Brief section lists explore-falsified as the cheapest trigger — costs only the explore phase, no planning or coding wasted. Plan and build triggers cost more. Explore exists to maximize the first and minimize the rest.
- `agent-staffing` skill: new **@reviewer as Architectural Drift Gate** section under "When Reviewers Apply". Names the anti-pattern of rg-count / grep-count CI invariants for architectural enforcement — gameable via rename-and-shim (coder optimizing to green CI can stub the "correct" site and keep real composition at the old site, count stays clean, ship drift). Prescribes `@reviewer` with a declared-invariant prompt (lives at `.meridian/invariants/<surface>-invariant.md` or similar), CI spawns reviewer on PRs touching protected surface, blocks merge on `fail`. Pair with deterministic behavioral tests as backstop — reviewer is probabilistic, tests pin down specific invariants. Distinct @reviewer use from design review and final implementation review.

### Changed
- `agent-staffing` skill: new **Terminology: Fan-Out vs Parallel Lanes** section near the top. Names the distinction between same-prompt-different-models (fan-out, reserved for critical decisions) and different-prompts-different-focus-areas (parallel lanes, default review posture). Previous language conflated them in several places — "testers fan out in parallel" read as same-prompt-different-models to careful readers, but the intent was parallel lanes. Clarified the "testers fan out in parallel" and "final review loop fan-out" language in the Parallelism section to use the right terms.

## [0.0.25] - 2026-04-16

### Changed
- `@impl-orchestrator` full prompt rewrite. Old prompt framed delegation as a constraint ("never write code") and scattered spawn triggers across 6 sections. New prompt mirrors `@design-orchestrator` structure: positive role identity ("you drive it to shipped code"), inline WHY for the delegation rule, explicit "`meridian spawn` is a shell command you invoke through the Bash tool" teaching with a concrete `Bash("meridian spawn -a coder ...")` example, and a centralized Delegation Strategy section listing every agent's spawn trigger. Root-caused from p1900 where opus used Edit 6× and Write 12× despite `disallowed-tools: [Edit, Write, NotebookEdit]` — prompt-steering, not YAML enforcement, is the primary guardrail.
- `@impl-orchestrator`: `effort: medium` → `effort: high`. Multi-hour autonomous orchestration runs need the thinking budget for instruction compliance under pressure.
- `@docs-orchestrator`: `effort: medium` → `effort: high`. Same autonomous-run reasoning. Opening rewritten for positive framing. Removed defensive "don't work around this through Bash file writes" hedge — hedges plant the workaround idea before forbidding it. Added `meridian spawn` Bash-tool teaching with concrete example.
- `@dev-orchestrator`: added `meridian spawn` Bash-tool teaching with concrete example and `/meridian-cli` skill reference.
- `@design-orchestrator`: merged duplicate `disallowed-tools` keys into one. YAML last-key-wins meant the destructive-git restrictions were silently dropped — only `[Agent]` was enforced.
- All four orchestrators: `tools: [Bash]` → `tools: [Bash, Bash(meridian spawn *)]`. Generic `Bash` remains for reading and verification commands; the explicit `Bash(meridian spawn *)` entry signals to readers and future stricter allowlist enforcement that `meridian spawn` is the primary action tool.

## [0.0.22] - 2026-04-14

### Changed
- `shared-workspace` skill scope tightened. Removed from agents that don't mutate repo state: `@explorer`, `@reviewer`, `@refactor-reviewer`, `@architect`, `@planner`, `@frontend-designer`, `@internet-researcher`. Orientation (`meridian work` / `git status` at session start) and the safety rules (no destructive git, no `git add -A`, don't delete unfamiliar untracked files) don't apply to read-only agents or agents that only write to `$MERIDIAN_WORK_DIR/` — their caller already holds repo orientation. Retained on all four orchestrators, code-editing agents (`@coder`, `@frontend-coder`, `@verifier`, `@investigator`, `@code-documenter`, `@tech-writer`, `@unit-tester`), and broad-permission testers (`@browser-tester`, `@smoke-tester`) where the safety rules are real guardrails.
- `@dev-orchestrator`: `effort: medium` → `effort: high`. User-facing orchestrator handling intent gathering, design review, and redesign routing across design/impl orchestrators was under-resourced at medium.
- `dev-principles` skill: new "Depend Deliberately" section — the pair to "Delete Often". A well-maintained library is a pre-validated abstraction; it has already survived the Rule of Three in the wild. Dependency earns its place when it deletes more code than it adds and collapses subsystems rather than swapping primitives. Simplicity measured by total ownership (code + cognitive load + failure modes + test matrix), not import count. Rejects the reflexive "stdlib-only is cleaner" frame.
- `dev-principles` skill: new "Probe Your Options Before You Commit" section — deduction from reading code is cheap but wrong often enough to cost rework cycles. Match probe investment to decision reversibility: cheap experiments for one-way-door decisions, skip for reversible ones. Treat "we'll find out during implementation" as a risk flag, not a plan. When you catch yourself deducing instead of probing ("this looks like phantom complexity"), stop and design the probe.
- `dev-principles` skill: new "Name the Constraint Before Deleting" subsection under integration-boundary probing — reading code tells you what it does, not why it exists. `git log -S <symbol>`, targeted tests, decision logs before removal. "Looks excessive to a fresh reader" is not the same as "is excessive" — code defending an invariant under concurrent load or preserving interactive fidelity will always look excessive on a calm read.
- `dev-principles` skill: new structural-health signal — platform-specific imports (`fcntl`, `msvcrt`, `termios`, `winreg`, `pwd`, `select.kqueue`) or OS-conditional branches appearing in more than one module. Mechanism is leaking into policy; collapse to one adapter.

### Added
- `disallowed-tools` entries for destructive git commands (`git revert:*`, `git checkout --:*`, `git restore:*`, `git reset --hard:*`, `git clean:*`) on agents with `Bash` tool access. Hard guard alongside the `shared-workspace` safety rules — prevents accidental destruction of other actors' uncommitted work even if the skill guidance is ignored.

## [0.0.19] - 2026-04-11

### Changed
- Spec-driven workflow restructure. Design package splits into `design/spec/` (EARS-notation behavioral contract with stable IDs) + `design/architecture/` (technical realization) + `design/refactors.md` (rearrangement agenda) + `design/feasibility.md` (probe evidence). Plan gains `plan/leaf-ownership.md` (exclusive EARS-statement-to-phase ownership), `plan/pre-planning-notes.md` (planning impl-orch runtime observations), `plan/preservation-hint.md` (dev-orch carry-over on redesign cycles). Replaces the `scenarios/` folder convention — verification keys on claimed EARS statement IDs, not scenario files.
- `@impl-orchestrator` two-role contract: planning role (consumes design, calls `@planner`, terminates plan-ready) and execution role (consumes plan from disk, drives phase loops, terminates converged). Each role runs in its own spawn. Planning caps `K_fail=3`, `K_probe=2`. Execution adds preserved-phase re-verification and spec-drift escape hatch. All escape hatches emit a `Redesign Brief` section in the terminal report.
- `@planner` three terminal shapes: `plan-ready`, `probe-request`, `structural-blocking`. Distinguishes knowledge gaps from structural properties — structural-blocking is a redesign signal, not a retry case. Ownership at EARS-statement granularity. Parallelism-first; refactor agenda mandatory.
- `@design-orchestrator` spec-first ordering, active gap-finding (probe real systems while designing), four-lens convergence (behavioral correctness, structural soundness, spec/arch alignment, refactor impact).
- `@dev-orchestrator` v3 routing with plan acceptance criteria keyed to EARS ownership and refactor accounting. Autonomous redesign loop: `design-problem` → design-orch + preservation hint + counter advance; `scope-problem` → fresh planning impl-orch. `K=2` design-problem cap. Trivial path names `@frontend-coder` / `@code-documenter` / `@tech-writer` alongside `@coder`.
- `@docs-orchestrator` tightened: drops inline spawn examples (→ `/meridian-spawn`), adds `decisions.md` and `design/spec/` + `design/architecture/` as mining/authority sources, adds explicit "never write docs directly" standing principle, collapses prescriptive phase steps into behavioral write/review/fix description.
- `@coder` loads `dev-principles`, bound to claimed EARS statement IDs as verification contract.
- `@reviewer` loads `dev-principles`, validates EARS alignment. Principle violations are ordinary findings.
- `planning` skill rewritten for v3: required files, overview.md contract, leaf-ownership.md contract, staffing as mandatory output, terminal shapes.
- `dev-artifacts` skill rewritten as canonical v3 layout reference.
- `smoke-test`, `unit-test`, `verification` skills: scenarios/ acceptance → claimed-EARS-statement acceptance. Load `/ears-parsing` for per-pattern parse and per-ID reporting (`verified` / `falsified` / `unparseable` / `blocked`).
- 29 agent + skill descriptions rewritten from WHAT-lead to WHEN-lead ("Use when ___" / "Spawn when ___" / "Spawned by ___"). Fixes widespread WHAT-in-frontmatter pattern — descriptions serve callers deciding whether to spawn/load, not runners. Worst offenders fixed: `dev-principles` now has a real trigger, `mermaid` is no longer a fragment. Load-bearing sibling discriminators preserved.

### Added
- `ears-parsing` skill: mechanical EARS verification contract for testers. Pattern table (u/s/e/w/c → trigger/fixture/assertion), per-ID reporting format, escape valve for non-parseable statements. Loaded by `smoke-test`, `unit-test`, `verification`.

### Removed
- `scenarios/` folder convention. Replaced by `design/spec/` EARS leaves + `plan/leaf-ownership.md` ledger.

## [0.0.18] - 2026-04-10

### Added
- `dev-principles` skill: new "Keep Docs Current" section. Two bullets — update docs in the same change as the behavior they describe (drift compounds silently), and treat reference material for external tools as a snapshot that must be re-verified when versions change. Companion lesson to the v0.0.17 "Configuration is integration too" bullet: v0.0.17 covered the consumer side (don't trust docs blindly), v0.0.18 covers the producer side (don't let your own docs drift).

## [0.0.17] - 2026-04-10

### Changed
- `dev-principles` skill: extend "Probe Before You Build at Integration Boundaries" with a new bullet — "Configuration is integration too. When you add a field to an external tool's config based on docs, verify the installed tool honors it end-to-end — parser acceptance isn't behavior, and docs often describe features the installed version doesn't implement." Lesson from the `v0.0.16` caveman exclude misadventure.

### Removed
- `exclude = ["skill:caveman-commit", "skill:caveman-review"]` from the `caveman` dep block in `mars.toml`. Dead code — `FilterConfig::to_mode()` in mars makes filter modes mutually exclusive (`skills.is_some()` fires before `exclude.is_some()`), so the field was silently dropped on every read. Shipped in `v0.0.16` based on a misread of `mars-toml-reference.md` without verifying the installed mars version honored it. The dead-weight `caveman-commit` and `caveman-review` skills in `.agents/skills/` are caused by a separate bug — transitive filter drop in mars `0.0.9`, already fixed upstream in mars-agents commit `b540032` (included in mars `0.0.13`). They will clean up automatically once meridian's bundled mars is upgraded.

## [0.0.16] - 2026-04-10

### Fixed
- `@internet-researcher` frontmatter: bare colon in description ("Reads the internet, not the codebase: library docs...") broke YAML parse — `mars check` flagged `mapping values are not allowed here`. Converted description to folded block style (`description: >`), matching `@architect` convention. Shipped broken in `v0.0.14`; this is the first release where `@internet-researcher` actually loads.
- `caveman` dep filter: `skills = ["caveman"]` did prefix-match, not exact-match, in mars sync — pulled `caveman-commit` and `caveman-review` into `.agents/skills/` alongside `caveman`. Added `exclude = ["skill:caveman-commit", "skill:caveman-review"]` so next sync drops them as orphans. No agent referenced them, so effect is cleanup only.

### Changed
- `CHANGELOG.md` rewritten in caveman style. Prior entries (`0.0.14`, `0.0.15`) ported, substance preserved. Convention documented in `meridian-channel/AGENTS.md`.

## [0.0.15] - 2026-04-10

### Added
- `caveman` skill (dep on [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)) loaded into intermediary orchestrators: `@design-orchestrator`, `@impl-orchestrator`, `@docs-orchestrator`. Compresses coordination chatter (delegation prompts, decision logs, phase status). Each runs `caveman full` mode with agent-specific extension: decision logs, phase status, `scenarios/` seeds still record *why* in caveman style so resumed work rehydrates reasoning. Sub-agent profiles (`@architect`, `@coder`, `@code-documenter`, `@tech-writer`, etc.) stay non-caveman — design docs, code, `fs/` mirrors, user docs untouched.
- `caveman` dep declared in `mars.toml`. Pins to `v0.0.15` pick it up transitively. Pins to `v0.0.14` skip caveman entirely.

## [0.0.14] - 2026-04-10

### Added
- `@investigator`: delegation capability. Spawns `@smoke-tester`, `@explorer`, `@unit-tester`, `@internet-researcher`, or narrower `@investigator` recursively. Sandbox → `danger-full-access` for `gh`/`curl`/web tools.
- `@impl-orchestrator`: "External knowledge gaps" escalation paragraph. `@coder` stuck on lib/API behavior? Spawn `@internet-researcher`, don't burn `@coder` cycles guessing from training-data assumptions.
- `CHANGELOG.md` introduced. Keep a Changelog format (later caveman-ified, see `[Unreleased]`).

### Changed
- `@researcher` → `@internet-researcher`. New name advertises external-knowledge role, pairs with `@explorer` (internal counterpart). Body refreshed: "internet vs codebase" split explicit, no overlap with `@explorer`.
- `@investigator` refocused around diagnose → triage. Three outcomes: scoped fix, filed GH issue, documented non-issue. Dropped dual-primary reactive/backlog-sweep split. GH issue filing = first-class, not fallback.
- `@architect` "External research" section rewritten. Frames external research as grounding design in ecosystem knowledge, not training-data guessing. Calls out `@internet-researcher` vs `@explorer`.
- `@design-orchestrator` "Research what you don't know": names `@internet-researcher` as "single most-forgotten delegation in design loop." Urges heavy use.
- `agent-staffing` `builders.md`: `@internet-researcher` headlines with same framing. `@explorer` reframed as "internal counterpart."
- `README` prose + agent table updated for rename.

### Removed
- `@researcher` profile. Replaced by `@internet-researcher`.
