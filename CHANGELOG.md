# Changelog

Caveman style. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [SemVer](https://semver.org/). Versions before 0.0.14 in git history only.

## [Unreleased]

## [0.16.3] - 2026-10-28

### Changed
- Plugin bundles meridian-base 0.13.6: `md-validation` keeps the neutral method and Mermaid authoring rules; Meridian's validator details now come from meridian-cli's bundled `md-validation__meridian`.

## [0.16.2] - 2026-10-28

### Changed
- Skills stop stating Meridian mechanics as fact: `/agent-staffing` drops "automatic fallback policy", `/pre-dev` makes the worktree the task's default checkout instead of pointing "the work item's source checkout" at it, `/post-dev` closes the work item once its agents finish instead of archiving it, `/post-dev`'s commit-pinned evidence links no longer cite work-directory pruning, and `ship.md` and `probe/resources/measurement.md` lose Meridian-only wording and examples.

## [0.16.1] - 2026-10-27

### Changed
- Requires meridian-base >=0.13.1, which ships `llm-writing/resources/cold-read.md` and the capture loop `/post-dev` points at.
- Agent bodies keep the job, boundaries, engagement, and report; method moved into the skills each agent loads, so each rule has one owner.
- `/dev-workflow` is the shared lifecycle, loaded by tech-lead, solo-dev, and ux-lead: keep going and the stop conditions, verify and failing-test triage, review staffing, the merge hand-off to `@coder` with `/merge-prep`, early `@kb-lead`, commits, PR, branch cleanup. `/solo-dev` is the do-it-yourself mode (solo-dev, ux-lead); `/parallel-execution` the delegated mode (tech-lead).
- Review rounds stop after two completed rounds per target, not three. A design under challenge is a review target: `reviewers.md` gains Reviewing Requirements or a Design, and design-lead's own cycle cap is gone.
- `/architecture` gains Settling a Design (requirements as hypotheses, alternatives, prior art, built variants); `/tech-docs` gains Revising a Design and the draw-or-outline rule; `/review` names `/probe` and the `@web-researcher` and `@investigator` hand-offs, and `/information-hierarchy` for UI reviews; `/review-alignment` checks spec–architecture links; `/probe` reads the project's testing instructions first; `/uxdev` runs `/grill-with-docs` before hardening against a documented decision; `builders.md` lists `@design-researcher` and `@source-researcher`.
- architect loads `/architecture` and `/tech-docs` and can load `/source-study`; design-lead loads `/architecture`; tech-lead lists `/dev-principles` as available instead of loading it; coder, frontend-coder and investigator can load `/llm-writing`.
- PR and branch-cleanup mechanics moved to `dev-workflow/resources/ship.md`; worktree mechanics and long-running lanes to `parallel-execution/resources/worktrees.md`. Each SKILL.md keeps the step and points there.
- `agent-staffing` and `architecture` descriptions open with the moment to load them.

## [0.16.0] - 2026-10-27

### Changed
- Requires meridian-base >=0.13.0 (schema 1).
- Agent and skill definitions use Mars schema 1; requires Mars >=0.20.0 and Meridian >=0.15.0 (meridian-cli on Mars 0.20).
- Ships as a plugin built by `mars build plugin` (committed `plugin/`, marketplace `meridian-dev-workflow`): Claude Code and Cursor load agents and skills, Codex and OpenCode load skills. Includes meridian-base's workers and skills.

## [0.15.17] - 2026-10-27

### Changed
- dev-workflow, post-dev, coder, frontend-coder, README: the changelog rule defers to the project's own convention instead of naming `CHANGELOG.md` `## [Unreleased]`. Where the convention puts the entry in the PR body, the coder writes the proposed entry in its report for the lead to place.

## [0.15.16] - 2026-10-27

### Changed
- Prober defaults to `terra` (GPT-6.1 Terra), not `luna`. Head-to-head replay of three past probes: Terra won two of three on blind grading, more accurate claims, 1.6–18x faster.
- Leads (design, product, solo-dev, tech, ux) may `git revert`; still deny checkout, switch, stash, restore, reset --hard, clean, since leads share one checkout. Product, tech, ux leads no longer deny `deep-research`/`init` skills; ux-lead may run workflows.

## [0.15.15] - 2026-10-25

### Changed
- Requires Meridian >=0.14.5 and accepts meridian-base 0.12, which moved Meridian's own skills into Meridian.
- Agent profiles rely on runtime-supplied capabilities to notify the human and
  read past sessions. Leads keep `/handoff` available for transition-brief
  judgment while the runtime supplies primary-session launch mechanics;
  work-item cleanup names the lifecycle action instead of a package skill.
- Agent descriptions and workflow guidance name portable capabilities such as source checkouts, work directories, skill attachment, past sessions, and diagram validation instead of Meridian commands, flags, and environment variables.
- Delegation wording now uses attach skills and pass files consistently; probing names artifacts with the caller-known run ID, and source study reuses the shared reference cache.
- Agent descriptions restore their routing-specific Spawn and Launch wording.

## [0.15.14] - 2026-10-25

### Changed
- Requires Meridian >=0.14.0 and Mars >=0.18.0 for portable network policies.
- `@architect` and `@web-researcher` return to workspace sandboxes with explicit shell network access; `@imagegen` also declares the network it needs.

## [0.15.13] - 2026-10-25

### Changed
- Requires Meridian >=0.13.0 for platform-owned Meridian command permissions.
- tech-lead, solo-dev, product-lead, ux-lead, and design-lead drop redundant scoped Meridian allows; plain Bash and their `subagents` declarations already grant the commands.

## [0.15.12] - 2026-10-24

### Changed
- design-craft Copy: cut taglines; text explaining how the screen works → name outcome on control, rewrite title, or fix layout. Keep what the screen can't show (format, consequence, recovery).
- ui-implementation: write on-screen text by design-craft Copy; report lists hint/subtitle/helper text kept on changed screens and what each tells the user, or none.
- frontend-coder: loads design-craft.

## [0.15.11] - 2026-10-24

### Changed
- agent-browser: drop `close --all` from the command list; name a session per agent and close only it.
- prober, browser, mockup-dev, ux-lead, frontend-coder: deny `agent-browser close|quit|exit --all`, which ends other agents' browsers.

## [0.15.10] - 2026-10-23

### Changed
- dev-principles: Defensive Code section (moved from solo-dev, now reaches coder/reviewer).

## [0.15.9] - 2026-10-23

### Changed
- post-dev and agent-staffing brief `@kb-lead` as its description asks, instead of keeping their own lists of what to pass.

## [0.15.8] - 2026-10-23

### Changed
- pre-dev plan review and the thermo lane fire on new modules, abstractions, or seams, moved responsibility, or growth beyond a local edit, not on any added code. The dead-code scan runs before the thermo lane or when a change deletes or replaces code.

## [0.15.7] - 2026-10-23

### Changed
- architect, web-researcher: `sandbox: danger-full-access` until Meridian grants sandboxed spawns network and its own state paths. Under `workspace-write`, Claude (since meridian 0.12.0) and Codex cut their shell off from the internet, host services and child spawns.

## [0.15.6] - 2026-10-22

### Changed
- Staffing preserves configured model routing. Escalation requires substantial verified review findings and tries suitable lower-cost upgrades before premium models; task complexity and launch failures no longer justify overrides.
- Tech-lead, ux-lead, reviewer staffing, and prober routing defer to the shared model-selection policy; hard merges no longer get preemptive upgrades.
- Spawn-capable profiles load agent-staffing from the start; known concurrency risks go in worker briefs, not preemptive model upgrades.

## [0.15.5] - 2026-10-21

### Changed
- reviewer can write repro scripts and throwaway tests (`edit`/`write` denies removed); keeps the reviewed source and artifacts untouched, writing repros to a scratch directory.
- review skill: every finding is verified before it is reported (run it, trace it, or quote the conflicting passages); disproved concerns are dropped; unchecked ones go under a closing Hypotheses section.
- tech-lead hands merges and rebases to `@coder --skills merge-prep`, skimming the PRs being merged in and briefing what matters from both sides; hard merges get a stronger model.
- parallel-execution: one coder takes a whole convergence and merges the branches in sequence; the lead's own integration-check step is gone.
- merge-prep: a spawned merger reports what the sources don't settle instead of asking; new "Check the Result" section (build and run focused checks before calling the merge done).
- coder: "Do not push"; merges when its brief assigns one.

## [0.15.4] - 2026-10-21

## [0.15.3] - 2026-10-18

### Changed
- Reviewer lanes run on the model whose description (`meridian mars models aliases`) names what the lane judges. Staffing guidance names no models; strengths live in the catalog descriptions. `resources/model-selection.md` deleted: its pointer and escalation rule moved into agent-staffing's body; the rest repeated the descriptions or Meridian's subagent-prompting guidance.
- tech-lead, product-lead and ux-lead never fall back to Fable (`no-fallback: true`); Fable is escalation only.

## [0.15.2] - 2026-10-18

### Changed
- `reviewer` and `architect` can spawn `@explorer` for cheap code exploration.
- `/probe` records the numbers a task makes useful, plus any the brief names (choosing from time, resources, user effort such as steps or clicks, volume), each with unit, conditions and method; reports carry them. prober's description asks callers to name the numbers they want.
- No agent defaults to Fable: tech-lead and product-lead default to Opus, the repeat-findings architecture review runs on Opus, and model-selection no longer recommends Fable. Fable stays in profiles as a fallback.
- Reviewers need a session of their own; every model-family rule for reviewers dropped (agent-staffing, reviewers.md, final gate, design-lead, solo-dev, architecture-review cross-check).
- Thermo-nuclear review before code exists: `/pre-dev` has a lead implementing a change that adds or restructures code get its plan, and the design doc when there is one, thermo-reviewed against the code it lands in; enabling refactors go first in the plan. tech-lead and solo-dev plan before running `/pre-dev`, so the review has a plan to read; solo-dev can spawn `@explorer` for the dead-code step. The skill gains a design-or-plan section: whether each added mechanism is needed at all, an enabling refactor in existing code, a simpler structure that absorbs the design's special cases, a new path beside one it should replace; line counts, dead code and type escapes wait for the code.
- Dead-code search goes to `@explorer` once review fixes land: given the change's base, it lists what the change and its fixes left without a caller; the lead deletes what is clearly dead and passes the uncertain cases to the thermo lane.
- Implementation review runs the thermo lane once the other lanes' fixes land, so it folds the patches into the code instead of leaving them bolted on. A fix that restructures code or changes behavior is committed, reruns the suite and the lanes whose verdicts it could change; the rule lives in `reviewers.md`, and solo-dev and parallel-execution point there.

## [0.15.1] - 2026-10-17

### Changed
- Leaner loaded context. tech-lead loads `testing` and `shared-dao` only on demand; solo-dev `shared-dao`. `dev-principles` drops what models already do (core-belief preambles, separate Consistency and Separation of Concerns sections) and keeps the steering. solo-dev and tech-lead no longer repeat the no-new-tests rule or the record-each-decision rule that their loaded skills carry. Tech-lead spawn prompt -33%, solo-dev -30%, coder -33%.
- Primary profiles (tech-lead, solo-dev, ux-lead, product-lead, design-lead) load `/notify`. `pre-dev` finds the work directory with `meridian work current`.
- `/diagnose`: rank competing explanations instead of a fixed 3-5 hypotheses; with no loop possible, work from a captured artifact and report the cause unconfirmed, instead of stopping.

## [0.15.0] - 2026-10-17

### Added
- `/agent-browser` ships a Linux wrapper that runs Chrome in its own memory-capped systemd scope, with direct-exec fallback when the user manager is unavailable.

### Changed
- Convergence limits live once in `agent-staffing/resources/reviewers.md`: rounds counted per review target (a gate, else the change); a concern needing a third round of fixes gets a root cause and a whole-system review; a second redesign goes to the caller; a fourth review round means investigating the design. tech-lead, solo-dev and parallel-execution point there. Lane briefs carry earlier review reports.
- tech-lead restores the Redesign Brief pointer and counts fixes, not coders. solo-dev and ux-lead can spawn `@investigator` and `@cold-reader`; tech-lead `@cold-reader`; post-dev has the PR body cold-read.
- Subagent profiles deny `ask_user` again.
- Review no longer required on every change: tech-lead, solo-dev and `reviewers.md` staff the lanes a change needs, so a lead can ship a small fix unreviewed. Pointers to `reviewers.md` say to open it before staffing a review.
- Fixed names and repo conventions out: product-lead records requirements and vocabulary where the project's conventions keep them, not in fixed `requirements.md`/`vocab.md`; no `design/` path, no one-decision-per-file or one-file-per-divergence rule; post-dev and dev-workflow follow the project's release conventions instead of `release:patch` and 70-char titles, CHANGELOG only where kept; react-architecture states import direction without one layout; ux-lead retries on a better model.
- Fewer always-run steps: pre-dev makes a worktree when the work belongs on one and a PR body when the work ends in a PR; source-study spawns an explorer per area worth studying and synthesizes itself; visualize-codebase splits pages only for more than one level.
- Skills and reviewer say "your caller" instead of "the orchestrator". `@coder` and tech-lead descriptions say what comes back.
- Cut text that changed nothing: browser's copy of `/agent-browser`, dev-principles' Get It Right the First Time, source-study's When list, test-naming advice, divergence's Downstream, review-alignment's duplicate traceability check, pep talk and restated reasons in thermo-nuclear, research-web, code, post-dev, model-selection, prober, product-lead.
- Scope fences out. `review-alignment`: drops the line handing code quality and tests to other lanes; `/review`'s out-of-lane findings rule applies. `research-web`: say which source is current or authoritative, and how strong each approach's evidence is. design-lead: investigation scales to uncertainty; challenge with every check the design's risks call for, not one. ux-lead: no longer routes work outside the frontend to other leads. `/agent-staffing`: reviewer covers code, designs, requirements.
- Knowledge capture: one `@kb-lead` run per change stays the default, stated once in `/post-dev` with its reason (cost; decision records make late capture cheap). Other sites point there. tech-lead regains early capture when a decision settled and work pauses across sessions.
- Review lanes a change needs live once, in `/agent-staffing` `resources/reviewers.md`; `/solo-dev` and `/parallel-execution` point there (solo-dev and ux-lead can now load `agent-staffing`). Thermo-nuclear reviewer when code is added or restructured, not every gate.
- `/parallel-execution` available to tech-lead, not loaded every run. Phase gate only where later phases build on the phase; review-fix loops stop at the `reviewers.md` limits.
- **Breaking:** `@gpt-dev` renamed `@solo-dev`; `meridian -a gpt-dev` stops working. Out of tech-lead's subagents; a session you launch, not a worker.
- tech-lead defined by its decisions, one task or several; one work item can hold several tasks; no delegate-everything rule; `/parallel-execution` when work splits into parallel lanes or dependent phases. Briefing guidance moved to meridian's spawn prompting (needs meridian-cli with it).
- Non-convergence: reviewers get earlier reports; findings grouped by concern (code behind one responsibility), not symptom. Third round of coders on one concern → step back: `@investigator` first, then review of the whole system. Second redesign or fourth review round → caller or design. design-lead: third cycle → caller.
- `/review`: serious issue outside lane or diff is a finding, not a side note. New "Look Past This Round": one-off or class, class-ending move, earlier findings cited.
- Tests: keep none unless the user asked (directly or through a brief); delete tests written to check work. Across `/testing`, `/code`, `/dev-principles`, `/solo-dev`, `@coder`, testers, `/post-dev`, `/diagnose`.
- `/solo-dev` review scales with change: cross-family reviewer, thermo-nuclear when code added or restructured, one per risk, prober when runtime behavior changes. After structural fixes, rerun only lanes the fix could change (also `/parallel-execution`).
- `/agent-staffing`: Standard Team list, loaded by tech-lead. Architecture / boundaries row covers repeat findings on Fable, beside the cross-family default review.
- "Seam" for an area becomes "concern"; seam means a boundary.
- `@reviewer`, `@coder` descriptions carry briefing rules (changes and risks, not a commit range; tests only on request).
- `@web-researcher`, `@architect`: full bash (for shell search tools on harnesses without built-in web tools), workspace sandbox; Codex uses its built-in search. `@source-researcher`: full access, since `git clone` needs the network. `/research-web` prefers the harness's built-in web tools. Prior art: web-researcher finds and saves docs, source-researcher studies source; `/source-study` starts from the caller's prior art.
- Retry after running out of depth goes to "a better model", per model selection. Decision records can span files.

## [0.14.14] - 2026-10-16

### Changed
- Fewer tests. Default verification: list failure modes, check each on running system, run existing tests covering touched code. New test only for case `/testing` admits (pure core, named regression, external contract); delegated workers write only tests brief names.
- `/testing` no longer loaded by `@coder`, `@frontend-coder`, `@gpt-dev`; available instead. Test-count/suite-time baseline growth needs brief or human approval.
- `/diagnose`: repro via CLI/HTTP first; repro command goes in commit message; loop kept as test only when brief names one.
- Review test-quality: missing test not a finding; report unverified failure mode. Testing resources no longer demand per-requirement tests.

## [0.14.13] - 2026-10-16

### Changed
- `/solo-dev`, `/parallel-execution`: gate wording states what lanes do; drops negated contrasts.

## [0.14.12] - 2026-10-16

### Changed
- `/thermo-nuclear-review`: reviews the system as it stands from the brief's focus; no diff framing.

## [0.14.11] - 2026-10-16

### Changed
- `/parallel-execution` gates, `/solo-dev` review: lanes review and probe the system as it stands, briefed with focus areas (what changed, seams touched, risks), not a commit's diff. A phase can span many commits; the gate runs once its work merges.

## [0.14.10] - 2026-10-16

### Changed
- `/parallel-execution`: every phase ends with a phase gate: default `@reviewer`, thermo-nuclear `@reviewer` focused on structure, `@prober`. Next phase waits for it. Final gate fans out wider: those three on the whole change, one reviewer per risk (tests, alignment, React, efficiency), end-to-end probe, full suite. Re-run the whole gate when fixes restructure code or change behavior.

## [0.14.9] - 2026-10-16

### Changed
- `/thermo-nuclear-review`: holds the code to `/dev-principles` and enforces them strictly.

## [0.14.8] - 2026-10-16

### Changed
- `/solo-dev`, `/parallel-execution`: thermo-nuclear reviewer is focused on structure, not limited to it; it still flags serious issues outside its lane, per `/review`.

## [0.14.7] - 2026-10-16

### Changed
- `/solo-dev`: review fans out on the commit: a default `@reviewer`, a separate `@reviewer` with `/thermo-nuclear-review` on structure alone, one more per risk (tests, design alignment, React, efficiency), plus `@prober`. Replaces attaching thermo-nuclear to the single reviewer.
- `/parallel-execution`: final whole-change review runs a default reviewer and a separate thermo-nuclear reviewer. `/agent-staffing` reviewer picker matches.
- `/thermo-nuclear-review`: thin-module blocker uses `/dev-principles`' term, shallow modules.

## [0.14.6] - 2026-10-16

### Changed
- `/solo-dev`: the review spawn attaches `/thermo-nuclear-review`, matching the final whole-change review in `/parallel-execution`.

## [0.14.5] - 2026-10-16

### Changed
- `/review`: Deletion check searches references to what the change removed; the diff hides code it orphaned.

## [0.14.4] - 2026-10-16

### Changed
- `/thermo-nuclear-review`: dead code is a presumptive blocker: unreachable, unreferenced, or result unused, including what the change orphaned (search references; the diff hides it). Wrapper blocker covers modules too thin to stand apart from their caller.

## [0.14.3] - 2026-10-16

### Changed
- `/probe`: spawn-id naming covers names the probe chooses (project tooling names dev stacks); the raw-captures rule sits beside the screenshot rule. `/post-dev`: the commit-link reason covers pruning as well as the archive move.

## [0.14.2] - 2026-10-16

### Changed
- `/post-dev`: evidence images in the PR body link to the commit that last touched them, not `main`; archiving a work item moves it and breaks `main` links.

## [0.14.1] - 2026-10-15

### Changed
- `/probe`: share the host. Reuse the stack and browser serving the task dir; name what you create with your spawn id; stop and delete it before reporting, keeping cited evidence; keep raw captures out of the work dir. `@prober` description: callers remove a failed run's leftovers by its id. `/post-dev`: stop dev stacks, browsers, scratch worktrees, and temp dirs before the PR.

## [0.14.0] - 2026-10-15

### Changed
- Requires meridian-base 0.11 (`/correct`, the corrections register, generic base wording).
- Second review round: the whole-change review runs on a family other than every phase's implementers (split by surface when none is free of all). `@prober` no longer loads `/diagnose` (`@investigator` owns diagnosis), and `/diagnose` removes its instrumentation at whatever phase it stops. Measurement vetting covers performance comparisons; a single timing reports unit, conditions, and run count.
- Review fixes: reviews run on a model family other than every model that wrote the change, stated at each gate (`/solo-dev`, `/parallel-execution`). `/solo-dev` confirms the stack was built from the reviewed commit and runs review and probe one after the other when they would share state. `@gpt-dev` spawned for one objective inside another lead's change reports back; that lead reviews and ships. `/diagnose` stops at root cause unless the brief assigns the fix. `/post-dev` review sign-off names which later changes it covers. Measurement vetting applies to performance numbers, not every count. `@ux-lead` and `@design-lead` can spawn `@session-miner`. Positive-framing fixes: `/design-analysis` keeps its no-implementation line; tests consolidate equivalent coverage rather than one tier per path; `/diagnose` doesn't wait on the user.
- Interactive leads (`@tech-lead`, `@gpt-dev`, `@ux-lead`, `@design-lead`) load `explore-and-engage` and `intent-modeling`, so the evidence and fix-the-class rules reach them when they talk to the human.
- `/parallel-execution` runs wide mechanical changes as expand, migrate, contract: new form beside the old, callers migrated in parallel batches, old form deleted as the last phase.
- `/correct` moved to meridian-base; its code levels are a resource there.
- Positive framing pass: ~40 soft negations rewritten as the behavior to do, or deleted where the positive sentence already carried it (agents, `/code`, `/solo-dev`, `/testing`, `/design-craft`, `/design-analysis`, `/review` structural-health, and others). Bright-line prohibitions (push/merge, `main`, test-only logic) stay.
- `/dev-principles` has a comment rule: comment only what the code can't show; design rationale goes in `.context/`, change history in the commit message, structure in names rather than banners.
- Measured numbers get vetted before they're reported or acted on: `/probe`'s new `resources/measurement.md` (limiter, production settings, errors, alternating repeat runs, end-to-end share, did the work happen), adapted from pstack's benchmark checklist. `/dev-principles` and `/diagnose` point to it.
- Reviews run on a model family other than the one that wrote the work (`/agent-staffing`, `/solo-dev`, `@design-lead`).
- `/ui-implementation` carries the production-UI method for any implementer: read the design first, build every state, check rendering in a browser. `@frontend-coder` loads it and defaults to Sonnet, separate from `@coder`'s Luna.
- `@reviewer` and `@tech-lead` keep Grok as an explicit option but never fall back to it.
- `@tech-lead` is the default primary (README install). It owns technical decisions, runs an agent team through long-running work, keeps several tasks moving as separate work items, and makes small fixes itself with `/code`. Effort xhigh → high.
- `@product-lead` settles product direction only: evidence, requirements, decisions, then a `/handoff` to the lead you launch. It no longer spawns builders, design leads, or `@kb-lead`.
- New `/solo-dev`: a lead implements and verifies in one session, then runs `@reviewer` and `@prober` on the finished commit, and again only when fixes restructured code or changed behavior. `@gpt-dev` reduces to it.
- `@ux-lead` loads `/solo-dev` plus UI specifics: incremental changes and most refactors itself, two or three parallel `@mockup-dev` variants to compare directions, `@frontend-coder`/`@coder` only for a big frontend refactor. `/ui-implementation` and `/uxdev` match.
- `@design-lead` runs one challenge after converging, and builds a browsable artifact itself, only when asked.
- Fewer reviews: `/parallel-execution` reviews once per phase, never per branch, and finishes each phase's review before the next phase builds on it. The last phase's review covers the whole change with `thermo-nuclear-review`.
- `/review` checks maintainability (entanglement, what the change could delete) and hot-path efficiency on every review, with new `resources/efficiency.md`. It reads source before prior approvals and names the commit and base reviewed.
- `/thermo-nuclear-review` rewritten, 193 → ~70 lines: finds the code-judo move that deletes groups of edge cases, checks documented architecture against code, finds copy-pasted siblings, one blocker list.
- `@reviewer` settles behavioral findings on the real system with `/probe`, not the test suite.
- `/dev-principles`: look for the model with no special case before adding a branch or flag; delete the replaced path instead of keeping it as a fallback; efficiency by construction.
- `/probe` screenshots visual results, looks at them before reporting, and reports anything abnormal as a likely UX bug.
- Focused checks per change; the full suite runs once at the merge or ship gate (`/code`, `/solo-dev`, `/parallel-execution`). Reviewer and prober share one dev stack, each with its own test data.
- Escalation: a worker that ran out of depth retries once on Opus with its report (`agent-staffing/resources/model-selection.md`); a bad brief gets a better brief. A second same-class finding on one seam stops patching. A spawn that fails before doing work gets its cause fixed or its model changed.
- `@investigator` stops at the root cause unless the brief assigns the fix.
- `@reviewer` keeps DeepSeek and Luna as explicit options for low-risk checks but never falls back to them.
- Knowledge capture runs once per change from `/post-dev`, reading the decision file and `DIVERGENCE/` first.
- `@tech-lead` and `/solo-dev` run `/pre-dev` before the first source edit, so a directly launched lead still captures before-state evidence. `/pre-dev` checks a reused worktree belongs to the work item, and builds generated artifacts per worktree. `/post-dev` checks the final commit's review passed.
- `@coder`/`@frontend-coder` commit on their branch with a changelog entry and never push or merge.
- `/parallel-execution` gives each change to shared code one owner. `/source-study` runs one or two explorers per source. `/diagnose` is model-invocable.
- Agent and skill descriptions say when and why to use them; the README tables say what each agent does.
- README describes the current system: the leads, the lifecycle of a change, review coverage, and every agent and skill with its actual default model.
- `@browser` and the staffing guide no longer call Muse Contributor a default or fallback; it is an explicit option. The investigator brief says whether to fix or stop at the cause.

## [0.13.13] - 2026-10-01

### Changed
- Dev workflow: trimmed restated filler (intro line, a no-op loop step, a duplicate Do-Not bullet, tripled timing phrasing in Branch Cleanup); added a pointer to check for a manual verification guide when the cleanup tool can't verify eligibility on its own.

## [0.13.12] - 2026-10-01

### Changed
- Dev workflow: widen the new cleanup rule from "prune the worktree" to "clean up everything the branch claimed" (worktree, branch, databases, dev processes, ports), per user feedback.

## [0.13.11] - 2026-10-01

### Changed
- Dev workflow: prune a worktree as soon as its branch merges, not after — squash-merging the integration branch later erases both the PR-match and ancestry proof the cleanup tool needs.

## [0.13.10] - 2026-09-26

## [0.13.9] - 2026-09-25

## [0.13.8] - 2026-09-24

### Changed
- UX Lead: direct small UI tweaks; explore major directions with the human before implementation.
- UX skills: preserve established visual systems, record major design direction, and let briefs override aesthetic defaults.
- Dev workflow: focus checks on change risk; run full gates at ship readiness. Structural review follows risk and repo policy.

## [0.13.7] - 2026-09-22

### Changed
- Staffing catalogs: shorter role briefs; review fan-out follows risk, not phase gates. Fresh review context no longer requires a different model.

## [0.13.6] - 2026-09-22

### Changed
- Investigator: Luna default; DeepSeek, Sol, Sonnet, Opus fallbacks.
- Design researcher: Sol default; Sonnet, Opus, DeepSeek Pro fallbacks.
- Source researcher: Luna default; DeepSeek, Sol, Sonnet fallbacks.
- Removed Composer fallbacks from coder, frontend-coder, and mockup-dev; dropped stale Composer/Cursor staffing guidance. Base alias retained for a later release.
- Mockup dev: Luna default; DeepSeek, Sonnet, Sol fallbacks at medium effort. Description asks for a detailed visual brief.
- Staffing: cheap-first implementation, task-specific larger-model selection, separate writing judgment, detailed briefs, and reviewer-model independence. Model-selection depth lives in a dedicated resource.
- Coder and frontend-coder default to DeepSeek, followed by Luna and Sonnet; final alternatives are Opus46 and generic Opus respectively. Caller descriptions request detailed briefs.
- Prober defaults to DeepSeek; browser defaults to training-eligible Muse Contributor, with caller-side data-use checks and no implicit Contributor fallback after a primary override.
- Reviewer policy: Astra, Sol, Grok, Opus. DeepSeek/Luna are explicit quick-review choices, not automatic fallbacks.
- GPT Dev: Astra, Opus, Sol, DeepSeek Pro. Web researcher: Luna, DeepSeek, Sonnet; removed its fixed harness to allow model-specific routing.
- Probe reports incidental confusing user-visible behavior, separating defects from usability concerns and uncertain observations.
- Reconciled README defaults and staffing guidance with the updated profiles.
- Requires Mars >=0.14.0 for explicit-only `no-fallback` policy entries.
- Requires meridian-base >=0.10.11 for Muse aliases and refreshed base staffing.

## [0.13.5] - 2026-09-16

### Changed
- DeepSeek policy aliases: `deepseek` → `deepseekpro`, `deepseekflash` → `deepseek`.

## [0.13.4] - 2026-09-16

## [0.13.3] - 2026-09-16

### Changed
- `@gpt-dev` verifies itself (project checks + self-probe); independent review at objective-complete, not per commit. Dropped smallest-diff instruction that fought `/dev-principles`.

## [0.13.2] - 2026-09-14

### Changed
- `@architect` defaults to `gpt` at `medium`; `sol` at `high` is the first fallback.
- `@design-lead` and `@gpt-dev` default to `gpt`.
- `@frontend-coder` defaults to `fable` at `medium`; `astra` at `high` and `opus` are fallbacks.
- `@reviewer` defaults to `gpt`; `fable` replaces Opus 4.6 as a fallback.
- `@source-researcher` defaults to `sol`; DeepSeek remains a fallback.
- `@tech-lead` defaults to Opus 4.6.
- `@ux-lead` defaults to `astra`; `fable` at `high` is an added fallback.

## [0.13.1] - 2026-09-07

### Changed
- Updated only model policies: product, technical, UX, architectural, and design
  agents now select generic `gpt` instead of specialized GPT-family aliases.
  Their default `model` fields are unchanged.

## [0.13.0] - 2026-07-25

### Added
- `/pre-dev`: PR body draft check — copy the repo PR template into the work
  dir as `pr-body-<slug>.md` before code changes and capture before-state
  evidence into it while "before" still exists.

### Changed
- `/dev-workflow`: push step passes the pre-dev draft as `--body-file`, runs
  a repo body checker when one exists, and falls back to the raw template
  when the draft is missing.
- `/post-dev`: PR readiness tops up the pre-dev draft instead of filling the
  raw template from scratch.
- **Breaking:** requires `meridian-base >=0.10.0, <0.11.0`, which authors hooks
  as per-target native fragments and needs mars-agents >= 0.12.0. The previous
  constraint (`<0.9.0`) resolved a meridian-base that mars 0.12.0 rejects
  outright, so `mars sync` failed with exit 2 on any project using this package.

## [0.12.8] - 2026-07-17

## [0.12.7] - 2026-07-17

## [0.12.6] - 2026-07-17

### Fixed
- `/post-dev`: after-merge cleanup names the exact command to close the work item (`meridian work done <slug>`) instead of a vague pointer, so merged PRs stop leaving work items open indefinitely.

## [0.12.5] - 2026-07-15

### Added
- `/merge-prep` skill: comprehension checkpoint before merging or rebasing a branch. Reads PR, linked conversations, commits, and target patterns before conflict resolution.

## [0.12.4] - 2026-07-14

### Changed
- Durable source editors and leads with explicit direct-edit exceptions always load `/qi-maintenance`; `/qi-layer` and `/knowledge-layers` stay available for substantial edits without consuming every run's context.
- `/dev-workflow`, `/issues`, and `/post-dev`: deferred work routes by scope to `.context/TODO`, `.context/FUTURE`, or GitHub; post-dev requires a completed final-path `@kb-lead` reconciliation and same-branch colocated truth while cross-cutting KB capture may land independently.
- Require `meridian-base >=0.8.7` for `/qi-maintenance`.

## [0.12.3] - 2026-07-11

## [0.12.2] - 2026-07-09

### Changed
- `@browser` and `@architect` now default to `sol`, preserving their existing effort and fallback policies.
- `@coder` now defaults to `sol` at `medium` effort, with Composer retained as a fallback.
- `@design-lead` retains Opus 4.6 as its default and replaces the GPT-5.5 fallback with `sol` at `xhigh` effort.
- `@design-researcher` now defaults to `sol` at `medium` effort, with `terra` and Opus 4.6 as fallbacks.
- `@frontend-coder` and `@gpt-dev` now default to `sol` at `xhigh` effort.
- `@imagegen` now defaults to `sol` at `xhigh` effort, with only `terra` as fallback.
- `@investigator` now defaults to `sol` at `xhigh`, with `terra` at `xhigh` and Opus 4.6 as fallbacks; duplicate-effort Sol fallbacks are unsupported.
- `@mockup-dev` now defaults to `terra` at `xhigh`, with Composer, Sonnet, and `sol` at `medium` as ordered fallbacks.
- `@prober` now defaults to `sol` at `xhigh`, retaining Sonnet as fallback.
- `@reviewer` now defaults to `sol` at `xhigh` effort.
- Product Lead, Tech Lead, and UX Lead retain their Opus defaults and replace GPT-5.5 fallbacks with `sol` at `xhigh`.
- `@source-researcher` retains DeepSeek as its default and adds `terra` at `medium` as the first fallback, before Sonnet.

## [0.12.1] - 2026-07-09

### Changed
- Bump meridian-base dependency to `>=0.8.0, <0.9.0` (DIVERGENCE convention, layer-wide current-truth rule).

## [0.12.0] - 2026-07-09

### Added
- `/divergence` skill: `DIVERGENCE/` folder protocol for tracking plan shifts during multi-phase work (one file per entry; reviewers and knowledge capture consume it).
- `/review` `resources/redesign-escalation.md`: non-convergence signals and the canonical four-part Redesign Brief (classification, structural problem, evidence, direction, what survives) used by both reviewer frame-rot verdicts and implementation-lead step-back escalation.

### Changed
- `/review` rewritten constructive: judge code as it stands now (a diff only locates), standards + design axes, quality as ease of change with entanglement as the objective test (canonical in `/architecture`), findings must carry a fix direction, frame-rot verdict is always blocking and always constructive.
- Escalation topology: tech-lead escalates redesign directly to `@design-lead` and surfaces non-converging cycles to its caller; product-lead remains sole HITL and dispatches self-classifying Redesign Briefs; fixed K=2 cycle count replaced with convergence judgment; `/handoff` reserved for human session boundaries (programmed through omission).
- Harness-agnostic sweep per new `/prompt-principles` section: agent bodies state intent; CLI mechanics (`--from`, `--continue`, `--task-dir`, wait commands) defer to the environment. `@agent` references and `--skills` attachment remain as composition vocabulary.
- `reviewer`: body slimmed against loaded `/review`; gains `@web-researcher` (background fact-checking) and `@investigator` (diagnosis only — causal chain, not fixes) subagents.
- `/architecture` leads with entanglement as the quality test; `/testing` opens with tests-as-guardrails; `/review-alignment` is model-invocable, treats logged divergence as plan, and defers the verdict boundary to `/review`.
- `kb`-capture guidance in leads: capture after settled phases with conversation, changed files, and work directory as context.
- Agent roster updates: new and retuned subagent profiles (architect, browser, design-researcher, imagegen, mockup-dev, prober, source-researcher, web-researcher, investigator, frontend-coder, gpt-dev).
- `ui-implementation` is model-invocable so ux-lead can self-load it as instructed.
- README refreshed: constructive review row, divergence/review-alignment listed, ghost skill rows removed, agent roles and models corrected.

## [0.11.44] - 2026-07-05

### Changed
- `/dev-principles`: rewrite Core Beliefs as explicit principle/why/action chains; add system-level simplicity as the fourth belief. Tighten Simplicity section to call out over-engineering as adding moving parts.

## [0.11.43] - 2026-07-05

### Changed
- Replaced `gpt54` with `gpt55`.

## [0.11.42] - 2026-07-04

### Changed
- Remove em dashes across all skills and agents. Fix model aliases: architect/design-researcher to gpt54, web-researcher to gptmini.

## [0.11.41] - 2026-07-04

### Changed
- `@design-lead`: overhaul. Load information-hierarchy and explore-and-engage. Route all subagents in body (architect, design-researcher, explorer, web-researcher, reviewer, kb-maintainer, prober, browser, source-researcher, mockup-dev). Add prototype phase, structured-artifact via spawned subagent, audience-aware output.
- `@tech-lead`: tighten body, collapse decomposition/verification into compact agent routing.
- `@reviewer`: fix model alias to gpt54, add fable to model-policies.
- `@investigator`: fix model alias to gpt54.
- `@prober`: add diagnose to available skills.
- `@browser`: description updated for design/behavior inspiration.
- `@frontend-coder`: model changed to opus48, add fable and glm to model-policies.
- `@mockup-dev`: fix model alias to opus46.
- `/parallel-execution`: remove "default to parallel", add judgment-based parallelism, add final whole-change convergence gate.
- `/agent-staffing` reviewers.md: add fan-out models section, remove @reviewer --skills probe row.
- `/diagnose`: simplify description.

## [0.11.40] - 2026-07-04

### Changed
- `/visualize-codebase` now loads `/information-hierarchy` and `/structured-artifact` (renamed from `/interactive-artifact` in meridian-base).
- `/parallel-execution`: rewritten around worktree isolation and DAG planning. Absorbed `execution-model.md` from agent-staffing (tech-lead pipeline, convergence gates, fix-cycle routing). Gates clarified as convergence loops. Added "Adapt the Plan" section.
- `/agent-staffing`: removed execution-model (moved to parallel-execution). Now purely team composition.
- `/react-architecture`: body tightened (133 to 36 lines). Stack-specific smell catalogs moved to `resources/smells.md`.
- `/test-architecture`: body tightened (235 to 30 lines). Smell catalogs moved to `resources/smells.md`.
- `/source-study`: body tightened (83 to 22 lines). Clone mechanics and example prompts moved to `resources/method.md`.
- `/dev-principles`: tightened (61 to 42 lines). Cut rhetoric, merged overlapping sections.
- `/tech-docs`: tightened (60 to 30 lines). Removed directory tree example.
- `/architecture`: tightened (53 to 30 lines). Collapsed boundary types.
- `/testing`: tightened (118 to 56 lines). Merged duplicate tier sections. Resources: em dash cleanup across all 4 resource files.
- `/code`: simplified description and body.
- `/poc`: body tightened. Description: "Proof of concept. Throwaway code that answers a feasibility question. Always deleted."
- `/diagnose`: em dash cleanup.
- `/uxdev`: em dash cleanup, description simplified.
- `@coder`: body simplified to "Write clean, working code."
- `@prober`: description rewritten with when-to-load signal.
- `@reviewer`: description lists available skills including `information-hierarchy`. Body adds guidance to load `/information-hierarchy` for UI/frontend reviews. `information-hierarchy` added to available skills.
- `@gpt-dev`: removed `parallel-execution` from available (not needed for single-objective work). Review section simplified.
- `@frontend-coder`: `information-hierarchy` added to always-load.
- `@mockup-dev`: `information-hierarchy` added to always-load.
- `@design-lead`: removed `alignment-reviewer` from subagents, replaced with `@reviewer --skills review-alignment`.
- `@tech-lead`: removed `test-reviewer` and `alignment-reviewer` from subagents.
- `@product-lead`: removed `alignment-reviewer` from subagents.
- `@browser`: em dash cleanup.
- Em dashes replaced with proper punctuation across all touched agents, skills, and resources.

### Removed
- `@alignment-reviewer`: replaced by `@reviewer --skills review-alignment`.
- `@test-reviewer`: replaced by `@reviewer --skills test-architecture,testing`.
- `/improve-codebase-architecture`: subsumed by `/thermo-nuclear-review` + `/dev-principles`.
- `/prototype`: replaced by `/poc`.

## [0.11.39] - 2026-06-27

### Changed
- `/dev-workflow`: when a feature branch is complete and passes the full gate, push and open/update its PR without asking.

## [0.11.38] - 2026-06-27

### Changed
- `/dev-workflow` clarifies that direct integration into protected branches like `main` or `staging` is PR/human-owned while leaving normal feature-branch merges available.

## [0.11.37] - 2026-06-22

### Changed
- Browser tooling swapped `playwright-cli` → `agent-browser` across `@browser`, `@browser-prober`, `@frontend-coder`, `@mockup-dev`. New self-authored `agent-browser` mechanism skill: stable core surface inline, `agent-browser skills get` as escape hatch for depth. Leaner always-loaded footprint, plus `console`/`errors`, React introspection (`react`, `vitals`), and the live observability dashboard.

### Removed
- `playwright-cli` dependency dropped from `mars.toml`. `show --annotate` (bidirectional draw-on-page review) has no agent-browser equivalent — handled out-of-band (Cursor); `agent-browser dashboard start`, optionally `tailscale serve 4848`, covers watch-live.

## [0.11.36] - 2026-06-21

### Changed
- 7 agent descriptions rewritten as when/why selection signals instead of body summaries: `@product-lead`, `@tech-lead`, `@gpt-dev`, `@design-lead`, `@design-researcher`, `@source-researcher`, `@mockup-dev`.

## [0.11.35] - 2026-06-19

### Fixed
- All agents: deny `bash(tmux kill-server:*)` at the tool-policy layer to prevent global tmux server teardown.

## [0.11.34] - 2026-06-19

### Changed
- All 21 agent bodies trimmed: filler removal, em-dash → colon, natural sentence rewording. Net −400 lines.
- All agents: dropped `reflection` from `skills.load` (12 agents). Verification stays with loaded methodology skills and external gates.
- Primary leads (`@product-lead`, `@design-lead`, `@tech-lead`): exploration discipline condensed, routing lists tightened.
- `@investigator`: thinned to wrapper; added `thermo-nuclear-review` to available for structural observations post-diagnosis.
- `@prober`, `@browser-prober`: thinned to wrappers pointing at `/probe`.
- `@simplify-reviewer`: fixed load list (`reflection` → `improve-codebase-architecture`).
- `@product-lead`: post-impl spawn uses plain `@kb-lead` (was `--skills post-impl-capture`).
- `@tech-lead`: removed `planning` from available.
- `agent-staffing` skill: gutted from 67 to 23 lines (redundant principles already in lead bodies).
- `testing` skill: removed stale `/reflection` reference.
- `visualize-codebase`: fixed stale description.

### Removed
- `planning` skill deleted. Execution-model diagram moved to `agent-staffing/resources/`.
- `post-impl-capture` skill deleted. Unique content absorbed into `@kb-lead` Orient step (meridian-base).
- `@design-writer` agent deleted. Orphan; `@design-lead` + `@architect` cover design docs.
- Stale README rows: `design-writer`, `post-impl-capture`, `planning`.

## [0.11.33] - 2026-06-18

## [0.11.32] - 2026-06-17

### Added
- `/visualize-codebase` skill (renamed from `codebase-walkthrough`): user-invocable, builds an interactive artifact mapping a codebase's structure, behavior, relationships, and health. Loads `/interactive-artifact` for rendering mechanism.
- `visualize-codebase/resources/db-schema.md`: DB schema introspection pipeline — `mermerd` for live database → Mermaid ER (subset with `--selectedTables`), plus layered data-flow annotations from code analysis.
- `visualize-codebase/resources/db-schema-alternatives.md`: fallbacks (`pg-mermaid`, raw SQL) when `mermerd` isn't available.

### Changed
- `unravel-codebase`: removed pointer to `/visualize-codebase` — reference is one-way only (visualize-codebase knows about unravel, not the other way around).
- `visualize-codebase/SKILL.md`: `/llm-writing` pass — cut redundant dimension restatement, collapsed "Teach Progressively" into intro, added "Splitting the Artifact" guidance for progressive mobile-friendly consumption.

### Removed
- `html-artifact` skill (directory deleted) — replaced by `/interactive-artifact` in meridian-base (generic mechanism) and `/visualize-codebase` (codebase methodology).
- `codebase-walkthrough` skill — renamed to `visualize-codebase`.
- Dropped `meridian-spawn` from `available:` across all agents that listed it (`@tech-lead`, `@product-lead`, `@design-lead`, `@gpt-dev`, `@investigator`, `@ux-lead`) and from the README cross-source dependency list. Spawn doctrine now lives in meridian — injected spawn contract + discovery pointers in the system prompt, with `meridian spawn -h` as the on-demand reference. Skill deleted in meridian-base.

## [0.11.31] - 2026-06-15

## [0.11.30] - 2026-06-14

### Changed
- `unravel-codebase` and `post-impl-capture` load `/qi-layer`; `unravel-codebase` references `/knowledge-layers`.
- README cross-source dependency list updated: `kb-conventions` → `knowledge-layers`.
- `@design-lead`, `@product-lead`: default model `opus46` → `opus48`.
- `@tech-lead`: removed `opus46` fallback policy.
- Lead agents (`@product-lead`, `@tech-lead`, `@design-lead`) plus `@investigator`, `@ux-lead`, and `@kb-lead` now explicitly mandate spawning `@explorer` for codebase exploration instead of reading files themselves.

## [0.11.29] - 2026-06-14

## [0.11.28] - 2026-06-13

### Fixed
- All agents: remove invalid `tools:` deny rules (`cron`, `notifications`, `plan_mode`, `worktree`) — no matching tools in harness.
- `@prober`: drop stale body reference to `worktree: deny`.

## [0.11.27] - 2026-06-13

## [0.11.26] - 2026-06-13

## [0.11.25] - 2026-06-12

### Changed
- product-lead, design-lead, tech-lead: add quality ownership sections — leads form their own judgment on spawn output rather than delegating quality verdicts
- dev-principles: add comprehensibility principle — abstractions should clarify, not obscure

## [0.11.24] - 2026-06-12

### Fixed
- Add missing `approval: never` to 6 agent profiles with `sandbox: danger-full-access` (browser, browser-prober, coder, frontend-coder, investigator, mockup-dev). Headless spawns on harnesses like Cursor rejected all shell/git commands without an explicit approval mode.

## [0.11.23] - 2026-06-12

### Added
- `@source-researcher`: study open-source project source code — clones repos, fans out explorers, synthesizes findings.
- `/uxdev`: mode-shift for visual design thinking — learn the design language, iterate with taste, verify what renders.
- `/design-craft`: frontend craft methodology — color (OKLCH, contrast, strategy), typography, layout, motion, copy.
- `/anti-slop`: guardrail against AI UI tells — cream bg, gradient text, glassmorphism, card grids, eyebrow kickers, copy patterns.
- `/code`: mode-shift for implementation — read, edit, verify, report methodology extracted from `@coder`.
- `/diagnose`: 6-phase bug diagnosis loop — feedback loop, reproduce, hypothesise, instrument, fix, regression-test. Adapted from mattpocock/skills (Apache 2.0).
- `/research-web`: external evidence gathering — library docs, upstream issues, production patterns. Compile and report only.
- `/design-analysis`: design synthesis — challenge assumptions, frame options, analyze impact, recommend.
- `/review-alignment`: alignment verification — coverage, drift, gap classification. "Does this artifact deliver what that artifact promised?"
- `/source-study`: renamed from `/source-context`. Build context by studying real source code.

### Changed
- `impeccable`: deleted. Replaced by `/uxdev` + `/design-craft` + `/anti-slop`.
- `ui-craft-basics`: deleted. Content merged into `/anti-slop`.
- `/source-context`: renamed to `/source-study`.
- `@coder`: body thinned — methodology moved to `/code`. Loads `/code`.
- `@ux-lead`: body thinned, loads `/uxdev` + `/design-craft` + `/anti-slop`, added `@frontend-coder` to subagents.
- `@web-researcher`: body thinned — methodology moved to `/research-web`.
- `@design-researcher`: body thinned — methodology moved to `/design-analysis`.
- `@alignment-reviewer`: body thinned — methodology moved to `/review-alignment`.
- `@investigator`: body thinned — methodology moved to `/diagnose`, removed `ask_user: deny`, restored coordination rules.
- `@tech-lead`: added `write: allow`, `edit: allow`, added `@alignment-reviewer` to subagents, `/uxdev` and `/code` to available.
- `@product-lead`: added `@alignment-reviewer`, `@source-researcher` to subagents, `/uxdev` and `/code` to available, `/source-study` replaces `/source-context`.
- `@design-lead`: added `@source-researcher` to subagents, `/uxdev` to available, `/source-study` replaces `/source-context`.
- `@frontend-coder`: `/uxdev` added to available, `/anti-slop` replaces `ui-craft-basics`.
- `@mockup-dev`: loads `/uxdev` + `/design-craft` + `/anti-slop`.
- `/code`: test guidance rephrased to positive framing, defers to `/testing`.
- `/review-alignment`: added review procedure (source-of-truth-first, checklist), fixed Partial+Drift overlap rule, fixed `/review` contrast.
- `/design-craft`: CSS/API implementation mechanics removed, kept design principles.
- `/research-web`: scope tightened to gather+report only. `/research-design` renamed to `/design-analysis`.
- `model-invocable`: set to `false` for load-only skills (`research-web`, `design-analysis`, `review-alignment`, `diagnose`).

## [0.11.22] - 2026-06-12

## [0.11.21] - 2026-06-09

## [0.11.20] - 2026-06-09

### Changed
- `thermo-nuclear-review`: replace PR/diff/branch-specific language with target-agnostic "the change" — skill now works correctly when loaded via `--skills`, not just in PR review context.

## [0.11.19] - 2026-06-07

## [0.11.18] - 2026-06-06

## [0.11.17] - 2026-06-06

## [0.11.16] - 2026-06-06

### Changed
- `@browser-prober`: explicit prohibition against running test suites; removed "check for existing E2E tests" escape hatch that pointed agents toward test harnesses instead of live browser interaction.

## [0.11.15] - 2026-06-06

## [0.11.14] - 2026-06-06

### Changed
- `@prober` and `/probe`: explicit prohibition against running test suites — prober exercises the built artifact (CLI, API, UI), not the development toolchain.

## [0.11.13] - 2026-06-06

### Changed
- All 21 agents: deny `Workflow`, `Skill(deep-research)`, and `Skill(init)` tools to prevent runaway multi-agent fan-out and accidental CLAUDE.md initialization.
- All 20 agents that had `notebook: deny`: removed the denial — notebook editing is now allowed.

## [0.11.12] - 2026-06-06

### Added
- `/probe`: mode-shift skill for runtime verification — generic methodology (two modes: probing vs verification) that any agent can load. Extracted from `testing/resources/manual-testing.md` and `testing/resources/browser-testing.md`.
- `/unravel-codebase`: human-invoked guided walkthrough of an unfamiliar codebase. Reads alongside the user, explains how it works today, and doubles as a cleanup pass on KB/vocab drift — fixes what's clear, flags what isn't. Not model-invocable.
- `/test-architecture`: strict test structure audit — hunts implementation-pinned tests, mock cascades, fixture sprawl, deletion targets, and file-size boundary violations. Loaded as an available skill by `reviewer` and `tech-lead`.
- `@test-reviewer`: dedicated test structure auditor. Loads `test-architecture` and `testing`, read-only sandbox, reports findings without executing changes.

### Changed
- `@probe` → `@prober`, `@browser-probe` → `@browser-prober`: agents renamed to free the skill namespace. Both now load `/probe` instead of `/testing`. `@prober` no longer has `subagents: [coder]` — verifiers verify, they don't fix.
- `/testing`: removed `resources/manual-testing.md` and `resources/browser-testing.md` (content moved to `/probe` skill and `@browser-prober` body). "When Each Tester Applies" restructured as tier-labeled list pointing to resources, `/probe` skill, and renamed agents.
- `/test-architecture`: trimmed from 320 to 235 lines — merged vapid tests into deletion targets, removed flaky test remediation (coder's job), removed redundant review questions, removed fixture writing advice, reworked approval bar from hard rules to behavioral heuristics.
- `@test-reviewer`: removed `shared-dao` from available, removed `bash(rg/ls)` permission cargo, removed competing priority ordering from body.
- `/unravel-codebase`: explicit `@explorer` spawn reference, added exit condition.
- `/pre-dev`, `/post-dev`: removed `user-invocable: false` (unnecessary, model-invocable is sufficient).

## [0.11.11] - 2026-06-05

## [0.11.10] - 2026-06-03

### Changed
- `/source-context`: full clone by default instead of `--depth 1`. Added progressive deepening commands for large repos.

## [0.11.9] - 2026-06-02

### Added
- `@mockup-dev`: fast Cursor/composer frontend mockups for visual iteration before production work hardens.
- `/impeccable`: Mars-compatible mirror of pbakaus/impeccable from the `.claude` skill, adapted to source `skills/impeccable` paths and kept human-invoked/non-model-invocable.
- `/ui-craft-basics`: lightweight model-invocable UI craft guardrails for mockups and production frontend work.
- `/ui-implementation`: explicit user-invocable production UI mode for settled visual direction. Not model-invocable.

### Changed
- `@ux-lead`: default model `opus46` → `opus47`; prompt trimmed around interactive user taste, design-system discovery, mockup iteration, and handoff to `/ui-implementation`.
- `@mockup-dev`, `@frontend-coder`: load `/ui-craft-basics`; Impeccable stays human-invoked and not ambient.
- Removed the `frontend-design` dependency and agent skill references.

## [0.11.7] - 2026-06-02

### Removed
- Primary lead profiles no longer explicitly allow harness-native `agent` tools; delegation stays on Meridian spawn.

### Changed
- `@frontend-coder`: default model `opus48` → `opus47`; drop `opus48` from model-policies (visual implementation tier).

## [0.11.5] - 2026-05-31

### Added
- `source-context` skill: clone open source repos into `~/.meridian/ref/`, spawn parallel `@explorer` agents to study source code, synthesize findings. Builds richer decision context before planning or designing.

### Changed
- `@product-lead`, `@design-lead`: `source-context` added to available skills.

## [0.11.4] - 2026-05-31
### Changed
- `post-impl-capture`: rewritten to the inline model — mine the impl session, diff intent (design artifacts) vs built (changed files), write every layer inline, hand structure to `@kb-maintainer`. No longer spawns `@code-mirror`/`@kb-writer`/`@tech-writer`. Retyped `reference` → `mode-shift` (it shifts `@kb-lead`'s capture mode, not plain reference material). Coverage-gap rescans inherit the base loop's three-wave cap instead of spawning open-endedly. `@kb-maintainer` handoff is now one-per-tree (one target per spawn).
- `agent-staffing`: maintainers catalog now lists `@kb-lead` + `@kb-maintainer`; dropped `@kb-writer`/`@tech-writer`.
- `@tech-lead`, `@gpt-dev`: destructive-git denylist trimmed to the house default — dropped `merge`/`rebase`/`worktree add`/`branch -d/-D/-m/-M` denies. Those are non-destructive forward/additive ops; the denylist now gates only branch-switching (`checkout`/`switch`) and uncommitted-work destruction (`reset --hard`/`restore`/`clean`/`stash`/`revert`).

### Removed
- `@kb-lead` moved to meridian-base — now a generic capture agent that writes `.context/`/KB/`docs/` inline. Dev callers pass dev specializations via `--skills`: `post-impl-capture`, `tech-docs`, `issues`.
- `@code-mirror` and `@tech-writer` agents — folded into `@kb-lead`'s inline writing.

### Changed
- `testing`: manual probes now require `meridian -C "$MERIDIAN_TASK_DIR" ...` for Meridian commands inside inherited sessions.

## [0.11.2] - 2026-05-30

- `@product-lead`: default dev handoff -> `@gpt-dev`

## [0.11.1] - 2026-05-30

## [0.11.0] - 2026-05-30

### Changed
- Lead agents (product-lead, tech-lead, design-lead, ux-lead): `agent: deny` -> `agent: allow` for native subagent dispatch.

## [0.10.0] - 2026-05-30

### Added
- `@gpt-dev`: direct implementation lead for gpt55/codex — codes itself, spawns reviewers to verify. No coder delegation, minimal orchestration overhead.
- `@probe`: runtime behavior verification agent.
- `@browser-probe`: browser-based verification (renamed from browser-tester).
- `/dev-workflow`, `/pre-dev`, `/post-dev`, `/prototype` skills.

### Changed
- All skill descriptions trimmed to one-line "when + what" format. Removed `detail` field from all skills.
- `@tech-lead`: upgraded `mode: subagent` → `mode: primary`. Added `thermo-nuclear-review` to skills.available. Removed `bash(sed *)` allow (undermined `edit: deny` delegation). Model-policies: alias-based (`opus46`, `opus48`), not raw model IDs.
- `@design-lead`: upgraded `mode: subagent` → `mode: primary`. Cold-start orientation. Removed stale model aliases, added gpt55/opus48. Removed `/dev-artifacts` references.
- `@product-lead`: replaced hardcoded tech-lead handoff with `/handoff` skill and implementation lead routing. Removed lifecycle peers from `subagents:`. Model-policies: dropped harness overrides, added opus48. Added `agent-staffing`, `prototype` to available.
- `@ux-lead`: pinned default model to opus46 (interactive primary). Removed `harness: claude` (auto-resolves). Model-policies: opus46/47/48 + gpt55. Added `prototype` to available.
- `@frontend-coder`: moved `frontend-design` from available to load. Model-policies: opus47/48/composer/deepseek/gpt55, removed stale `codex`. Added `react-architecture` to available.
- `@coder`: model-policies cleaned — removed stale `codex`, added deepseek.
- `@gpt-dev`: removed nonexistent `explorer` from subagents.
- `@architect`, `@design-writer`: removed `/dev-artifacts` references.
- `@reviewer`: added `read`, `rg`, `ls` tools for uncommitted file inspection. Added `improve-codebase-architecture`, `tech-docs`, `llm-writing` to available (leads invoke these via `--skills`). Added `react-architecture` to available.
- `@kb-lead`: added `post-impl-capture` to available.
- `dev-principles`: added "Get it right the first time" — AI code is cheap to write, expensive to untangle. `model-invocable: false` (loaded on 12 agents, never available).
- `agent-staffing`: model selection section — profile defaults handle most roles, reviews fan out across models for perspective diversity. Placed on product-lead, design-lead, tech-lead available lists.
- `tech-docs`: replaced inline validation commands with `/md-validation` reference.
- `planning`: fixed malformed nested backtick formatting in verification levels.
- All agents: `decision-logging` → `decision-log` (skill merged upstream).
- All agents: `decision-log`, `knowledge-capture` removed from available lists (folded into `work-artifacts` upstream).
- All agents: removed `delegation` from skills (merged into `clear-mind` upstream).
- All agents with work-item responsibilities: load `work-artifacts` (new upstream skill).
- Fixed corrupted body content in `issues` (stale `detail:` line leaked into body text).

### Removed
- `dev-artifacts` skill — ownership table duplicated what each agent body already says; stale references to removed `plan/status.md`.
- `@browser-tester` — renamed to `@browser-probe`.
- `@qa-lead`, `@smoke-tester`, `@unit-tester` — consolidated into testing skill resources.
- `browser-test`, `smoke-test`, `unit-test`, `integration-test` skills — consolidated into `/testing` with resources.

## [0.9.0] - 2026-05-29

### Added
- `@design-researcher`: pure research/challenge specialist — adversarial analysis, alternatives, tradeoff matrices. Fans out to explorers and web-researchers.

### Changed
- All agent descriptions papered to one-liners — no spawn syntax, portable.
- Orchestrator skill lists: heavy reference skills replaced with thin principle shims (`delegation`, `decision-logging`, `work-tracking`, `knowledge-capture`). Reference skills remain on-demand via `/skill-name`.
- 17 reference skills flipped to `model-invocable: true` — agents can discover them globally.
- `@design-lead` subagents: added `design-researcher`.

## [0.8.1] - 2026-05-29

## [0.8.0] - 2026-05-29

### Changed
- All agents: add `mode` field (primary or subagent) for progressive loading
- Orchestrators: add `subagents` list for inventory filtering
- 5 agents: `approval: yolo` → `approval: never`
- 17 skills: add `detail` field for inventory summaries

## [0.7.27] - 2026-05-29

update models

## [0.7.26] - 2026-05-28

## [0.7.25] - 2026-05-28

### Changed
- `@product-lead`: post-impl kb-lead spawn uses `--skills post-impl-capture` by default. Covers all documentation layers (inline, KB, docs), not just KB.

## [0.7.24] - 2026-05-27

### Added
- `@frontend-coder`: `playwright-cli` and `browser-test` skills, `danger-full-access` sandbox. Visually verifies its own output as it builds — opens browser, snapshots, adjusts.
- `react-architecture` skill: React-specific structural lens — token discipline, state architecture, component composition, import boundaries, component API consistency. Complements `dev-principles` with what generic structural skills don't cover about React codebases. Loaded on demand via `--skills react-architecture`.

### Changed
- `@product-lead`, `@tech-lead`, `@ux-lead`: nudge leads to update `.context/CONTEXT.md` and `AGENTS.md` when they discover structural understanding while working.
- Tester skills (`smoke-test`, `unit-test`, `integration-test`) now verify against requirements docs instead of EARS statement IDs. Acceptance contracts read `requirements.md` / `visual-requirements.md` / design specs.
- `@alignment-reviewer`: EARS traceability → requirements traceability.
- `@reviewer`: validate against stated requirements, not EARS/phase blueprints.
- `@tech-lead`: verify requirements delivery at step boundaries.
- `@ux-lead`: added visual requirements gathering (probe → `visual-requirements.md` gate), shared visual vocabulary section that orients against existing KB/codebase terms with `grill-with-docs`, oneshot default path through `@frontend-coder`, exploration exception for genuinely ambiguous visual intent. Skills added: `shared-dao`, `dev-artifacts`, `shared-workspace`, `session-mining`, `grill-with-docs`. Model pinned to `opus` with `model-policies` cascade.
### Removed
- `@mockup-gen`: deleted. Throwaway visual iteration runs through `@frontend-coder` with a fast model when needed.
- `@frontend-designer`: deleted. Visual spec formation is ux-lead's job (via `visual-requirements.md`); implementation routes directly to `@frontend-coder`.
- `@planner`: deleted. Planning is deprecated; tech-lead decomposes work inline from the design package.
- `ears-parsing` skill: deleted. Testers verify against requirements, not EARS.
- `dev-artifacts/resources/plan-package.md`: deleted. Plan ceremony (phases, EARS claims, leaf-ownership) replaced by lightweight requirements-driven flow.
- `README.md`: full refresh — all agents and skills now accurate with current models, roles, and deprecation status.

## [0.7.23] - 2026-05-27

### Changed
- `@coder`: effort `none` → `medium` (top-level and composer override). Unblocks `meridian mars check` on mars 0.7.3, which rejects `none`. For composer, cursor probe treats `medium` and `none` as the same default tier — no behavior change. gpt55 and codex overrides unchanged.
- `@tech-lead`: "Worktree and Ship" → "Task Dir and Ship". Source-code work targets `$MERIDIAN_TASK_DIR` (set by @product-lead on the work item). Dropped `--worktree` mid-run ensure path, managed-worktree set-worktree references, and `worktree-management` skill pointer. Ship section opens PR from the branch in `$MERIDIAN_TASK_DIR` instead of from a managed worktree branch.
- `@product-lead`: tech-lead handoff isolation guidance now uses plain `git worktree add` + `meridian work task-dir <path>` (or `work start --task-dir`). Cross-repo work sets `task_dir` to the sibling checkout instead of passing `--repo`. Recovery uses `meridian work task-dir <path>` instead of `set-worktree`. Calls out that meridian does not own the `task_dir` directory.
- `@probe`: workspace placement guidance now references `$MERIDIAN_TASK_DIR` directly — runs in the task dir (project root, plain worktree, or sibling checkout) with `cd`/`git -C` for ops there. `worktree: deny` still pins placement to the caller.
- `/smoke-test`: execution section reworded around `$MERIDIAN_TASK_DIR`. Drops "managed worktree" framing; testers `cd` / `git -C` into the task dir and still do not create or switch worktrees.
- `agent-staffing/testers`: `@probe` lane reworded around `$MERIDIAN_TASK_DIR`. Drops "managed worktree" framing.

### Removed
- `/worktree-management` skill — orphaned by the task-dir redesign. Every command it taught (`meridian work worktree --ensure`, `spawn --worktree`, `meridian work set-worktree`, `meridian work clear-worktree`, managed temporary worktrees) is gone, and no agent referenced it. Worktree decisions are owned by `@product-lead`; `task_dir` is the binding.
- `bootstrap/feature-worktree` — taught managed-worktree harness permissions and incorrectly told users to grant `Bash(git worktree *)` to `@tech-lead`. Tech-lead is denied that tool surface in the task-dir model; `@product-lead` (or the human) owns worktree creation outside the prompt package.

## [0.7.22] - 2026-05-26

### Added
- `worktree-management` skill: shared reference for managed worktree commands — provisioning, inspection, spawning, cross-repo targeting, rebinding (`set-worktree`), cleanup (`clear-worktree`), temporary worktrees.

### Changed
- `@product-lead`, `@tech-lead`: extracted worktree mechanism knowledge into `worktree-management` skill. Agents keep ownership/decision guidance, skill holds the command surface.
- `@coder`: default model switched to `composer`, effort to `none`.
- `@frontend-designer`: model switched to `opus` alias, added `claude-opus-4-7` policy.
- `@mockup-gen`: model switched to `opus46`, removed codex policy.
- `agent-staffing`: `models list` references now document `--live` flag.

## [0.7.21] - 2026-05-25

### Changed
- `@product-lead`: past-session lookup now treats bare `session log` as safe recent entries and reserves `--full`/`--no-truncate` for deliberate expansion.
- `@product-lead`: past-session lookup now calls out entry `0` as the selected segment prologue/handoff slot.
- `@product-lead`: session log guidance aligned with finalized CLI — segment-local default, `--segment previous|N`, `--global` as explicit opt-in only, and `meridian session search` recommended with the printed `Open:` command for known text.

## [0.7.20] - 2026-05-24

### Changed
- `@tech-lead`, `@product-lead`: worktree wording corrected to match shipped `spawn --worktree` behavior — requires a selected work item, will not target the temporary managed worktree from `meridian work worktree --ensure` (no active work item). Temp worktree is now described as a caller-facing isolation tool; tech-lead escalates to start a work item when sub-spawn isolation is needed.
- `@product-lead`: tech-lead handoff example now uses `meridian work start --worktree "<name>"` as the canonical create+start path so the managed worktree exists in one step.
- `@product-lead`, `@tech-lead`: worktree guidance now treats isolation as warranted for larger/risky work, not small direct coder slices; implementation owners use Meridian managed worktree ensure instead of manual `git worktree add` paths.
- `@product-lead` tech-lead handoff: dropped redundant `work worktree --ensure` preflight in the common path — `spawn --worktree` ensures the managed worktree itself. Examples now use `<work-id>` consistently with `--work` and worktree commands. Adds temporary worktree path (`meridian work worktree --ensure` with no active work item) for isolation without a work item.
- `@tech-lead` worktree section: operational specifics for mid-run ensure — session stays in its launch directory, subsequent specialist spawns run inside the managed worktree via `--worktree`, and a re-launch in the worktree is what tech-lead reports rather than attempting to relocate the current session. Adds temporary worktree mode for isolation without a work item.
- `@product-lead`, `@tech-lead`: cross-repo implementation guidance — pass `--repo <path-or-alias>` when coordination runs in one repo (e.g. `meridian-cli`) but implementation belongs in another (`mars-agents`, `meridian-web`, prompt packages). Target repo determines canonical worktree path; ambiguous target fails clearly instead of provisioning in the wrong repo.
- `@product-lead`, `@tech-lead`, `@probe`, `/smoke-test`, `agent-staffing`: finalized workspace/worktree wording — tester guidance now uses caller-selected workspace, managed worktree metadata is authoritative on ensure/recovery, and tech-lead shipping text no longer hardcodes worktree-only PR wording.

## [0.7.19] - 2026-05-23

### Changed
- `@coder`: shifted from narrow patch executor to scoped implementation owner. Defers structural doctrine to `/dev-principles`, allows clean local restructuring, fixes frontend-coder routing text.
- `agent-staffing`, `@tech-lead`: coder staffing now splits by objective and ownership, not arbitrary 2-4 file limits.
- `@tech-lead`: reframed around objective framing and convergence judgment; coders own code-level structure inside assigned objectives.
- Dev workflow verification language now separates manual smoke checks from automated tests/checks in reports.
- QA timing aligned as post-convergence, pre-shipping audit across `@tech-lead`, `@`, staffing, and plan-package guidance.
- `@product-lead`: standard QA audit now routes through `@tech-lead`; direct `@` spawn reserved for standalone audit of converged implementation.
- `@`, testing guidance: pruning language now puts burden of proof on keeping tests, requires named durable behavior/contract/risk for retained coverage, and sends uncertain coverage to manual smoke guide improvements before automated tests.

## [0.7.18] - 2026-05-23

### Changed
- `@product-lead`: shared-language setup now calls for focused explorer fanout and explicit term conflict/gap reports before writing `vocab.md`.

## [0.7.17] - 2026-05-22

### Added
- `thermo-nuclear-review` skill — extremely strict maintainability review for abstraction quality, file-size growth, and spaghetti detection. Adapted from [cursor/plugins](https://github.com/cursor/plugins). Not model-invocable; load explicitly when you want the harshest lens.

## [0.7.16] - 2026-05-22

## [0.7.15] - 2026-05-22

### Changed
- `/dev-principles`, `@tech-lead`: softened the new testing and LOC-growth guidance from procedural wording to judgment-oriented heuristics while keeping the smoke-first, lower-tier-tests-when-justified posture.
- `@kb-lead`: coverage review now pushes KB cleanup toward current, consolidated pages instead of additive layering.
- `@code-mirror`: now carries `/shared-dao` so inline code-colocated docs use the same term-discipline as KB work.

## [0.7.14] - 2026-05-22

### Changed
- `/dev-principles`: testing guidance now favors durable boundary coverage over routine test addition. Added end-of-change LOC reflection so code growth needs a concrete justification and a re-check against shallow wrappers, duplicated logic, and weak boundaries.
- `@tech-lead`: verification defaults to smoke testing and review. Lower-tier tests are now conditional on durable boundary, composition, or narrow logic risk. Final structural review now checks net LOC growth before stopping.
- `planning`, `plan-package`: phase exit gates and staffing now treat unit/integration test lanes as justified exceptions instead of default lanes.
- README: removed stale `@` testing row.

## [0.7.13] - 2026-05-22

## [0.7.12] - 2026-05-19

## [0.7.11] - 2026-05-19

### Changed
- `@`: simplified from 4-phase orchestrator to hands-on agent — gathers context via explorer/session-miner, makes deletion/addition judgments directly, reviewer pass on the diff. Most QA passes should be net-negative in test lines.
- `@kb-lead`: reframed from post-implementation capture coordinator to general documentation coordinator — any doc goal (cleanup, restructuring, term changes, coverage audits, post-impl capture). Added `@kb-maintainer` to layer table with conditional sequencing.

### Added
- `post-impl-capture` skill: extracted kb-lead's implementation-specific coordination sequence. Callers pass `--skills post-impl-capture` when spawning kb-lead after implementation ships.

### Removed
- `@qa-designer`: orphaned by  simplification —  now makes tier/deletion judgments directly.

## [0.7.10] - 2026-05-17

### Changed
- `@product-lead`, `@ux-lead`: route by installed agent descriptions and ownership instead of fixed specialist lists; make evidence-gathering spawns active and lifecycle leads reactive.
- `@ux-lead`: run exploration and user critique as parallel visual-design tracks; verify spawn reports produced the expected visual artifact.
- `@mockup-gen`: auto approval enabled.
- `AGENTS.md`: clarify source-only prompt editing and generated `.mars/` sync boundary.

## [0.7.9] - 2026-05-17

### Changed
- `@`, `@qa-designer`: resolve test strategy output before spawning designer; prefer active work directory and fall back to `/tmp` for ephemeral QA handoff.

## [0.7.8] - 2026-05-16

### Changed
- `@design-lead`: loads `/tech-docs`, adds mandatory documentation-structure review lane for non-trivial design packages, and routes large doc-structure cleanup findings to `@kb-maintainer --skills tech-docs,llm-writing` before final report.

## [0.7.7] - 2026-05-16

## [0.7.6] - 2026-05-16

### Changed
- `@kb-lead`, `@product-lead`, `@design-lead`, `@tech-lead`, `@design-writer`, `@reviewer`: carry `shared-dao`
- `@product-lead`: renamed `glossary.md` to `vocab.md`
- `@`: final report must show add audit, delete audit, no-op rationale, and validation. Explicitly explains why tests were added, deleted, kept, moved, or left unchanged.

## [0.7.5] - 2026-05-16

## [0.7.4] - 2026-05-16

## [0.7.3] - 2026-05-16

## [0.7.2] - 2026-05-16

### Added
- `@simplify-reviewer` agent: structural friction hunter. Finds shallow modules, fragmentation, deletion targets, and deep-module opportunities. Spawned by @design-lead (investigation) and @tech-lead (final structural review). Read-only, outputs concrete simplification moves with leverage priority. Model: gpt.
- `/improve-codebase-architecture` skill: methodology for hunting structural friction — shallow modules, fragmented concerns, deletion targets, inline targets, deep-module opportunities. Resources reference the structural-health catalog under `/review`.
- `@product-lead` shared language: mines KB and codebase for existing terminology via @explorer, grills user for convergence, produces canonical-only `glossary.md` alongside `requirements.md`. Unresolved terminology discrepancies logged separately.
- `/handoff` skill: prompt craft for subagent handoffs — context matching, boundary setting, exit criteria. Teaches orchestrators to give subagents exactly what they need for verifiable output. Pass artifacts via `-f` instead of inlining. When spawning with `--from`, teaches pointing to session content instead of restating it. Loaded by @product-lead, @design-lead, @tech-lead.

### Changed
- `/dev-principles`: "Good software is software that is easy to change" as opening. Added deep modules over shallow modules section. Added anti-festering — tech debt compounds at agent speed. Added tests at interfaces not internals to enable safe simplification. Coders write tests freely;  does cleanup audit.
- `@coder`: pre-edit XML `<boundary_rule>` gate — new files, classes, and abstractions require independent-concern justification. Shallow modules explicitly called out as structural debt to avoid. Dropped prose repetition.
- `@tech-lead`: final structural review adds `@simplify-reviewer` lane. `@reviewer (structural focus)` narrowed — deep-module territory owned by `@simplify-reviewer`. QA Escalation → QA Audit: standard post-impl step, not escalation.
- `@design-lead`: investigation fan-out adds `@simplify-reviewer` (replaces `@reviewer (structural focus)` overlap). Investigation findings must be written into design documents immediately, not left in conversation context. Design decisions are live, not accumulated — drop what the latest direction invalidates. Reviewer handoffs pass current direction only, not abandoned decisions.
- `@`: repositioned from emergency responder to standard post-impl test audit — adds boundary tests for interfaces and edge cases, deletes tests that don't protect real behavior. Spawned by @product-lead and @tech-lead as a standard phase. Model changed from sonnet to gpt55. Execute section now has explicit Delete lane via `edit`.
- `@qa-designer` (was `@qa-design-lead`): renamed and reframed — independently audits test suite and designs correct shape (tier placement, coverage gaps, delete targets). Standard spawn by @, not emergency-only. Model changed from claude-opus-4-6 to gpt55.
- `agent-staffing`: reviewers catalog updated with @simplify-reviewer entry and spawning guidance.
- `@design-writer`, `@tech-writer`, `@code-mirror`: model changed from sonnet to deepseek (DeepSeek V4 Pro) with sonnet as fallback candidate.
- `@reviewer`: opus fallback replaced with deepseek candidate.
- `@tech-lead`: model changed from claude-opus-4-6 to gpt55 with claude-opus-4-6 as fallback.
- `@web-researcher`: model changed from codex to gpt-5.4-mini (harness: codex).

## [0.7.1] - 2026-05-15

### Changed
- `@probe`: worktree-native default. Caller owns worktree placement. Temp envs only for destructive probes or clean-baseline comparisons.
- `smoke-test`: execution guidance worktree-first, disposable envs as exception. Shared-workspace safety lives in skill, not duplicated in agent.
- `agent-staffing/resources/testers.md`: @probe lane now active-worktree by default.

## [0.7.0] - 2026-05-14

### Changed
- Workflow: default path is now design-lead → tech-lead. Planner removed entirely from active lifecycle.
- `@product-lead`: routing simplified — design → user approval → tech-lead. Planner checkpoint removed. Post-impl spawns @kb-lead; @ spawned only on explicit need or tech-lead escalation. Redesign loop routes design-lead → tech-lead directly.
- `@design-lead`: lighter output — high-level structure, key interfaces, boundaries, patterns, tradeoffs, risks. Removed "minimum deliverable" heavyweight spec language. Removed @planner auto-spawn. Description reframed from "heavy design" to "design guidance."
- `@tech-lead`: owns work decomposition directly from design, functional verification, targeted boundary tests, safe restructuring, and final structural review. Planner escalation removed. Integration testing uses `@coder --skills integration-test` instead of `@integration-tester`.
- `@`: repositioned from mandatory post-impl phase to specialist escalation. Description reframed — spawned for significant structural test-suite work, not routine post-impl.
- `@kb-lead`: description softened — "when implementation knowledge needs capturing" instead of "after implementation ships." Timing left intentionally flexible.
- `agent-staffing/resources/testers.md`: permanent test suite note updated — @tech-lead owns with @ as specialist escalation. `@integration-tester` replaced with `@coder --skills integration-test`.
- `dev-artifacts/resources/ownership.md`: plan/ writer changed from @planner to @tech-lead. @planner removed from all artifact readers.
- `planning/SKILL.md`: description updated — used by @tech-lead, not @planner.
- `agent-staffing/resources/reviewers.md`: @alignment-reviewer usage updated — planner verification point replaced with design verification.
- README: lifecycle updated to design-lead → tech-lead default. Planner removed from topology and agent table.  marked as specialist.

- `@tech-lead` Implementation: coder spawns scoped to one subphase, 2-4 files. Parallel `--bg` when file sets are disjoint, sequential when they overlap.
- `@tech-lead` Verification: test-quality reviewer spawned after test-writing at phase gates.
- All callers: `@` → `@coder --skills unit-test,testing-principles`. `@coder --skills integration-test` → `@coder --skills integration-test,testing-principles`. Updated in tech-lead, , investigator, planning, agent-staffing, dev-artifacts.
- `testing-principles`: description notes to always include when spawning coder for testing. "When Each Tester Applies" section uses `@coder --skills` patterns.
- `dev-principles` Deletion: rewrote from hedging questions to direct mandates — delete dead code, collapse duplication, fix structural rot immediately, escalate deep rot.
- `agent-staffing/resources/builders.md`: coder entry reframed around small spawn scope and parallel-when-disjoint.
- `agent-staffing/resources/reviewers.md`: test quality added as review focus area.

### Added
- `review/resources/test-quality.md`: review focus area for test effectiveness — edge cases over happy paths, tautological assertions, mock-dominated tests, tier placement.

### Deprecated
- `@planner`: marked deprecated with `model-invocable: false`. Retained as legacy artifact; no lead or orchestrator routes to it. Default workflow is design-lead → tech-lead.
- `@integration-tester`: marked deprecated with `model-invocable: false`. Use `@coder --skills integration-test` instead. The skill carries the methodology; @coder provides execution.
- `@`: marked deprecated with `model-invocable: false`. Use `@coder --skills unit-test,testing-principles` instead.

## [0.6.2] - 2026-05-11

## [0.6.1] - 2026-05-11

## [0.6.0] - 2026-05-11

## [0.5.11] - 2026-05-11

### Changed
- `@`: gpt-5.4 (Codex) → sonnet (Claude). Orchestrators need native blocking spawn-wait, not Codex poll loops. Sonnet handles test design decisions fine.

## [0.5.10] - 2026-05-11

### Changed
- `dev-principles`: added Testing section — coders verify by running the program, fix broken tests, leave new test design to dedicated testers. Stops coders from padding changes with hundreds of lines of unit tests.
- `@coder`: "verify proportionally to blast radius" → "verify by running the code, not by writing tests."

## [0.5.9] - 2026-05-11

## [0.5.8] - 2026-05-10

### Added
- `@qa-design-lead`: analysis-only agent spawned by @ when the test suite has structural problems. Reads test files and explorer report, produces `design/test-strategy.md`. No sub-spawning — pure analysis and doc writing. Covers tier audit, diff analysis of coder-touched tests, anti-pattern inventory, conftest map, decomposition plan.

### Changed
- `@`: full loop driver — explores first (spawns @explorer), decides whether to spawn @qa-design-lead for heavy redesign or proceed inline, runs one @reviewer pass, then hands off to `@coder --skills unit-test` or `@coder --skills integration-test`. Adds Edit tool for `# qa-validated: <work-item>` markers. Drops direct use of @ and @integration-tester in favor of `@coder` + skill routing.

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
- `@product-lead`: post-implementation routing simplified — spawns @ + @kb-lead instead of three parallel doc agents + sequential kb-maintainer. Passes work directory context (`-f $(meridian work current)`) to kb-lead. `<delegate>` tag uses behavioral framing instead of role identity.
- `@tech-lead`: replaced contradictory "every action is a spawn" absolute with scoped behavioral guidance. `<delegate>` tag uses behavioral framing.
- `@planner`: replaced brittle verb-inference routing rule with spawn-identity check. "Parallelize aggressively" → "parallelize when independence is proven."
- `@investigator`: replaced recursive self-spawning with @explorer/@probe delegation for narrow probes.
- `@tech-writer`: fixed wrong-agent routing — @explorer for reading, @probe for runtime verification. "Important information first" → lead with user action/command/behavior.
- `@alignment-reviewer`: replaced contrastive definition with positive framing.
- `@ux-lead`: `<delegate>` tag uses behavioral routing instead of role identity.
- `@`, `@integration-tester`: descriptions reframed positively instead of "not the right fit for."
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
- `@`: sharpened unit-test judgment — keep/add tests for durable contracts, delete stale or implementation-shaped unit tests.
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
- Agent profiles: migrated 6 agents from deprecated `models:` to `fanout:` + `model-policies:` (browser, browser-probe, coder, frontend-coder, mockup-gen, refactor-reviewer).
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
- `@probe`: description rewritten to cover both probing and verification modes equally.
- `@investigator`: split `@explorer` reference into `@explorer` (codebase) + `@session-miner` (sessions). Trimmed contrastive filler.
- `@web-researcher`: updated routing for explorer/session-miner split.
- `@refactor-coder`: positive opener (was "not to add features; it is to improve"). Cut orchestrator-scoping "good units" list. Trimmed skill restatement in Refactoring Posture. Compressed Behavior Preservation.
- `@refactor-reviewer`: compressed "What to Look For" — references skill instead of duplicating 8-bullet list.
- `@alignment-reviewer`: scope discipline flipped from negative list to positive routing.
- `@`: trimmed "safety net" metaphor.
- `@verifier`: trimmed "clearing mechanical noise" restatement.
- `@frontend-coder`: trimmed "separate polished UI from functional-but-flat" filler.
- `@mockup-gen`: trimmed redundant "not production code" from body opener (description already routes on this).
- `refactoring-principles` skill: "not tidiness for its own sake" → "the goal is making the next change smaller."
- `architecture` skill: reshaped from process prescription (frame → explore → compare → stress-test) to shared vocabulary (boundaries, dependencies, tradeoff dimensions, structural risk). All three consumers benefit now, not just architect.
- `unit-test` skill: cut "What Unit Tests Are For" section — testing-principles covers tier definition, agent knows what unit tests are.
- `tech-docs` skill: scoped as design document methodology. Removed obsolete `scripts/` (check-md-links replaced by `meridian kg check`). Removed "Writing for Agent Consumers" — readability principles apply to all readers.
- `smoke-test` skill: rewritten for equal probing/verification coverage. Killed contrastive "ARE and ARE NOT" section.
- `agent-staffing/builders.md`: added `@session-miner` entry with routing guidance.
- `agent-staffing/maintainers.md`: updated `@kb-writer` entry for `@session-miner` delegation.
- `@product-lead`: prescriptive requirements gathering (7 bullet points with examples) compressed to principles. Added `intent-modeling` skill — handles hypothesis-vs-spec reasoning that was hand-rolled in the body.
- `@tech-lead`: trimmed 211→105 lines. Cut execution loop duplication with `planning/resources/execution-model.md` (was restating the entire subphase/gate/final-gate loop). Cut prescriptive "Before Any Final Report" checklist — replaced with two report shapes. Added `intent-modeling` — launch prompt interpretation and redesign-brief judgment are intent calls. `@product-manager` refs → `@product-lead`.
- `@design-lead`: trimmed 184→105 lines. Cut 40-line "Design Artifact Hygiene" section (detailed kb-maintainer instructions) to one sentence. Cut "Refactoring Awareness" section that restated `refactoring-principles` skill. Fixed stale `meridian spawn -a architect-lead` in description. Added `llm-writing`.
- `@planner`: trimmed 131→95 lines. Cut prescriptive thoroughness checklist into prose principles. `@product-manager` refs → `@product-lead`. Added `llm-writing`.
- `@`: trimmed 136→75 lines. Collapsed step-by-step "Strategy Before Tests" into principle-level guidance. Collapsed "Produce Tests" prescriptive sections.
- `@tech-writer`: trimmed 100→60 lines. Cut "Writing Principles" section (generic writing advice now covered by `llm-writing`). Compressed Diátaxis to bullets. Added `llm-writing`.
- `@design-writer`: trimmed 67→45 lines. Cut "Quality Bar" checklist. Added `llm-writing`.
- `@architect`: added `llm-writing`.
- `@frontend-designer`: added `llm-writing`.
- `@reviewer`: `models:` fan-out field → `fanout:` (new schema).
- `@design-lead`, `@`, `@ux-lead`: added `intent-modeling`. All orchestrators interpret caller intent and make escalation/routing judgments.
- `@ux-lead`: `@product-manager` refs → `@product-lead`.
- `review` skill: trimmed 76→50 lines. Cut "What wastes everyone's time" (negative framing). Cut "How to Conduct the Review" prescriptive steps. Description trigger-first.
- All skill descriptions: trigger-first ("Load when..." / "Use when...") instead of content-first. Fixed: `agent-management`, `design-principles`, `dev-principles`, `planning`, `refactoring-principles`, `testing-principles`, `browser-test`, `ears-parsing`, `issues`.
- `issues` skill: trimmed 114→38 lines. Cut prescriptive examples, negative framing ("When NOT to Create"), verbose workflow integration. Opening now leads with "agents systematically under-file" to counter the actual failure mode.
- `@product-lead`, `@design-lead`, `@tech-lead`, `@`: added `issues` skill — leads triage reviewer findings and should file non-blocking issues rather than losing them.
- `@coder`, `@probe`: added `issues` skill — discover file-worthy problems during implementation and testing.
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
- `@frontend-dev` agent: primary visual/UX entry point — the visual counterpart to @dev-orchestrator. Works directly with user to iterate on design through rapid mockup cycles. Opus model, `harness: claude`, `approval: yolo`. Spawns @mockup-gen, @browser, @frontend-designer, @frontend-coder, @browser-probe, @imagegen.
- `@mockup-gen` agent: fast throwaway visual mockups using the project's real frontend components and design system. Speed over polish — hardcode data, skip edge cases, get something visual in front of the user fast. Model: gpt55.
- `@imagegen` agent: native image generation. UI concept mockups, visual explorations, icons, reference imagery. Usually spawned on explicit user request. Model: gpt55.
- `@browser` agent: general-purpose browser interaction via `playwright-cli`. Scraping, data extraction, screenshots, interactive annotation, design research — the prompt defines the purpose. Model: gpt55.
- `playwright-cli` dependency: Microsoft's `@playwright/cli` skill for harness-agnostic browser automation via Bash. Replaces Playwright MCP plugin.

- `dev-artifacts`: path discovery updated — context dirs available as `$MERIDIAN_CONTEXT_*_DIR` env vars alongside CLI commands.

### Changed
- **Role renames**: `dev-orchestrator` → `product-manager`, `design-orchestrator` → `architect-lead`, `impl-orchestrator` → `tech-lead`, `test-orchestrator` → ``, `frontend-dev` → `ux-lead`. Real-world titles prime for delegation over micromanagement.
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
- `@impl-orchestrator`: scope clarified — functionality, logic, structure, and design alignment. Can touch frontend code for functional concerns; visual/UX iteration belongs to @frontend-dev. Phase exit gate gains @alignment-reviewer lane for EARS verification + @browser-probe for functional frontend verification. Can respawn @planner mid-flight when EARS gaps found at phase gates. Final gate uses @alignment-reviewer with full design package for holistic design-intent check.
- `@planner`: "or lighter context" removed — requires design package with requirements, no escape hatch. Can be spawned by @impl-orchestrator for mid-flight plan adjustment. Two new thoroughness checks: every requirement in `requirements.md` maps to a delivering subphase, every EARS statement maps to a subphase whose blueprint actually scopes the work (table assignment alone is not delivery).
- `@coder`: description reframed from file-type restriction to intent-based routing. Now full-stack: backend, frontend logic, CLI, infrastructure, data flow, build systems. "Do not use for React, TSX, CSS" restriction removed. Description adds spawn/prompt guidance (subphase, EARS statements, integration boundaries).
- `@frontend-coder`: model `claude-opus-4-6` → `gpt55` (clear specs don't need Opus aesthetic judgment — GPT executes faithfully against design targets). Fan-out updated `opus`/`opus47` → `gpt55`/`codex`. Description reframed: pick when visual quality and design fidelity are the primary concern, not just because file is frontend code. Body shifted from autonomous aesthetic judgment ("generic UI is a failure") to faithful spec execution ("match the visual target"). Adds mockup/screenshot guidance.
- `@refactor-coder`: dropped "scoped" filler from description. Added prompt guidance: state structural move and behavior-preservation constraints.
- `@browser-probe`: model `claude-opus-4-6` → `gpt55` (GPT excels at computer use). MCP Playwright plugin → `playwright-cli` skill (harness-agnostic CLI). Sandbox → `danger-full-access` (browser automation needs it). Description adds spawn/prompt guidance.
- `browser-test` skill: refactored to methodology-only — references `/playwright-cli` for browser mechanics instead of teaching Playwright usage.
- `agent-staffing/builders.md`: coder catalog entries updated — @coder is full-stack, @frontend-coder is visual design fidelity. Added @mockup-gen, @imagegen, @browser entries.
- `agent-staffing/testers.md`: @browser-probe entry updated for `playwright-cli` usage and `--annotate` for interactive browser sessions.
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
- `@dev-orchestrator`: reframed as "primary developer / translator between user and technical teams." New requirements gathering section — XY Problem awareness, JTBD-style questioning, first-principles challenge, solution-free gating before routing to design. Specialist routing table expanded: design-writer, probe for probing, investigator for diagnosis. Post-impl routing: test-orchestrator + code-documenter + tech-writer in parallel with `--from` session context. Planner terminal state handling (probe-request → probe, structural-blocking → design-orchestrator). Writing constraint: delegate via specialists, exceptions for requirements.md and prompts.
- `@design-orchestrator`: reframed as technical design owner, not problem discovery. Sonnet 1M model, autocompact 30. Explores technical options (not first-principle problems — that's dev-orchestrator). Challenges technical feasibility. Expanded refactoring awareness — "clean codebase is prerequisite, design time is cheapest fix." Spawns explorer, refactor-reviewer, reviewer. Uses probe for probes not coder.
- `@impl-orchestrator`: broke coder-centrism. New definitions section (phase, subphase, probe, diagnosis — each with right agent). Subphase loop: probe-first step, light reviewer per subphase, route issues by type (impl → coder, behavioral → probe, root-cause → investigator). Phase gate: one general reviewer (save fan-out for final gate), temp unit/integration tests deleted after. Final gate: reviewer fan-out by focus area, duplicate higher-level with opus, refactor-reviewer on full change set. Judgment/escalation discipline — recognize non-converging cycles, escalate redesign briefs.
- `@planner`: methodology moved from planning skill into agent body (inputs, thoroughness, priorities, output contract, terminal shapes). Parallelism-first. Route by work type — probe/diagnosis lanes before coding.
- `planning` skill: stripped to shared definitions only (phase, subphase, verification levels, probe/diagnosis lanes, fix-cycle routing). Both planner and impl-orchestrator load it without overlap.
- `execution-model.md`: full rewrite. Mermaid diagram matches updated impl-orchestrator — probe step, light reviewer, issue-type routing, refactor-reviewer final-gate only, temp gate tests.
- `plan-package.md`: staffing contract updated — implementer variants, probe/diagnosis steps, routing by finding type.
- `testing-principles` skill: added risk-based testing, testing trophy model (integration-heavy), test behavior not implementation, hermetic by default, DAMP over DRY, LLM-generated test caveats.
- `@tech-writer`: Diátaxis framework (tutorials, how-tos, reference, explanation). Gather context first via explorers + --from. Spawns own reviewer for accuracy. Audience-flexible — adapts to technical level.
- `@code-documenter`: agent-facing format guidance (bullet/key-value over prose, include security/performance/failure modes). Spawns own reviewer for accuracy.
- `@docs-orchestrator`: deleted. Replaced by direct spawns of code-documenter + tech-writer from dev-orchestrator.
- `@coder`: clarified that unclear runtime behavior at integration boundaries → report back to orchestrator for probe.
- 7 worker agents: added "Your final message is your report — no file needed." (reviewer, refactor-reviewer, explorer, verifier, probe, investigator, web-researcher)

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
- `shared-workspace` skill scope tightened. Removed from agents that don't mutate repo state: `@explorer`, `@reviewer`, `@refactor-reviewer`, `@architect`, `@planner`, `@frontend-designer`, `@internet-researcher`. Orientation (`meridian work` / `git status` at session start) and the safety rules (no destructive git, no `git add -A`, don't delete unfamiliar untracked files) don't apply to read-only agents or agents that only write to `$MERIDIAN_WORK_DIR/` — their caller already holds repo orientation. Retained on all four orchestrators, code-editing agents (`@coder`, `@frontend-coder`, `@verifier`, `@investigator`, `@code-documenter`, `@tech-writer`, `@`), and broad-permission testers (`@browser-probe`, `@probe`) where the safety rules are real guardrails.
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
- `@investigator`: delegation capability. Spawns `@probe`, `@explorer`, `@`, `@internet-researcher`, or narrower `@investigator` recursively. Sandbox → `danger-full-access` for `gh`/`curl`/web tools.
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
