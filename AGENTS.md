# meridian-dev-workflow

A development team for Meridian projects: leads the user works with in a session, the
specialists they delegate to (coders, reviewers, probers, researchers), and the skills
that carry a change from first edit to merged PR. It ships through `mars add` and as a
plugin for Claude Code, Codex, Cursor and OpenCode.

## Rules

- **meridian-base is always installed beside this package.** Name its agents
  (`@explorer`, `@kb-lead`, `@kb-maintainer`, `@cold-reader`, `@session-miner`) and
  skills (`/llm-writing`, `/knowledge-layers`, `/md-validation`, ...) freely: Mars
  installs it alongside, and the plugin bundles it.
- **Codex and OpenCode plugins carry skills only,** so no `@agent` a skill names
  resolves for those users.
- **`plugin/` and its catalogs are Mars output.** `plugin/`, `.claude-plugin/`,
  `.cursor-plugin/` and `package.json` are rebuilt at each release; never edit them by
  hand. `meridian mars build plugin` brings them current before one.
- **The plugin bundles the meridian-base version recorded in
  `plugin/.mars-plugin.json`.** After a meridian-base release that changes its agents
  or skills, release this package too, or plugin users keep the old ones.

## Watching

- **Structure before style (`/information-architecture`, `/uxdev`
  `resources/direction.md`).** On the next UI run where the structure is
  open: the agent loads `/information-architecture` without being told,
  writes down the things, their nesting and the frame, draws grey-box
  wireframes from the kit, runs `scripts/validate.py` and screenshots each
  screen, and shows them before any styled mockup; a mockup-dev spawn stops
  at the wireframes. Watch for the overcorrection, wireframes for a visual
  tweak on a settled layout, for screens that copy `assets/example.html`'s
  layout instead of the product's structure, and for parallel mockup-dev
  spawns writing their structure into the project's design docs before the
  human has chosen one.
- **Issues show the problem (`/issues`).** On the next issues agents file:
  the open issues were searched first; the body follows the repo's issue
  template, else the PR template's before-fix sections, else
  `resources/issue-template.md`; a bug has repro steps with expected and
  actual and the commit; anything visible has a screenshot linked at a
  commit; slowness has numbers with what they ran on; no spawn IDs or local
  paths. In meridian-flow, the fixing PR's Why and Examples start from the
  issue's.
- **Calls under an unclear brief are reported, not asked (`/dev-workflow`
  Keep Going).** On the next autonomous lead runs: the calls made go in the
  work directory with their reasons, and the final report lists them apart
  from the questions still open.
- **design-lead reviews at the draft.** On the next interactive design-lead
  runs: the reviewer starts in the turn the draft is written, its brief
  carries what the human said and decided, and once the review is back the
  human sees the design with only the questions it leaves open, not a
  request to approve the whole. Work a handoff brief lists as unreviewed is
  under review in the new lead's first turn.
- **product-lead as the user's point of contact.** On the next long
  product-lead runs in meridian-flow: it keeps what it knows about each lead
  outside its context and picks it up after compaction; it tracks leads the
  user launched, not only its handoffs; its handoff briefs say it coordinates
  the lead, and the lead keeps it informed. If leads don't report back, the
  brief line needs to say what to report.
- **Reviewers hand wide reading to one `@explorer` (`/review` Read It
  Whole).** On the next reviews of a change that deletes or replaces code
  or repeats a pattern: the reviewer still reads the change itself, spawns
  one explorer for the sweep instead of grepping it all, and spawns none
  for a small local change.
- **One reviewer, one round, one probe per feature.** On the next lead run
  that builds a feature in phases or part PRs: one code review of the whole
  feature, not one per part; the reviewer loads `/thermo-nuclear-review` or
  `/architecture` on its own when structure looks wrong, and still reports
  structure findings; blocking structure findings and shared causes go to
  `@design-lead` instead of a second round; the re-review stays on the
  fixes; the prober runs once on final code, from a brief that leads with
  the user's goal, and its report has a "What felt off" part. Watch for the
  structure lens going soft without the thermo lane, and for regressions
  that the narrow re-review or the single probe missed.
- **design-lead designs alone, after zooming out.** On the next
  design-lead runs: it zooms out to the system around the problem before
  proposing a structure, reading the docs itself and, in a large area,
  having explorers find what's related first; it builds or
  compares real alternatives instead of settling on the first structure it
  finds; when it goes past the design into planning or code, the problem
  needed it. Since `/architecture` asks for it: the design compares real
  alternatives even when the first looked right, and for each reference
  the human named it says what it read of how that system works (source,
  docs, its builders' write-ups), not what it recalled.
- **product-lead hands off leads the user steers.** On the next run where
  the user is about to leave or asks about spawning: it writes handoffs
  and gives the launch commands, and spawns a lead only when told to.
- **Implementers own the codebase (`/code`).** On the next `coder`,
  `frontend-coder`, `solo-dev` and `ux-lead` runs: they merge repeated code
  and fix the bugs they find instead of adding beside them or reporting
  them, and a spawned coder names each fix beyond its task in its report.
  Watch for fixes that spread a change past what its review can cover.
- **Whoever writes the code verifies it (`/dev-workflow` Verify,
  `/testing`).** On the next lead runs that delegate code: the coder
  exercises each failure on the real system and the lead reads its report
  instead of probing again; the full suite runs on the commit sent to
  review and the commit shipped, and a review fix reruns only its tests;
  `/post-dev` catches user docs the change made stale.
