# meridian-dev-workflow

Agent profiles and skills for the dev orchestration workflow.

## Plugin

A release rebuilds the committed `plugin/` tree and its marketplace catalogs
(`.claude-plugin/`, `.cursor-plugin/`, `package.json`) at the new version. Never
edit them by hand; run `meridian mars build plugin` after changing a source file
if you want the tree current before a release.

## Depends on meridian-base

This package depends on meridian-base (`[dependencies.meridian-base]` in
`mars.toml`). Its agents (`@explorer`, `@kb-lead`, `@kb-maintainer`,
`@cold-reader`, `@session-miner`) and skills (`/llm-writing`,
`/knowledge-layers`, `/md-validation`, ...) are installed wherever this package
is, so references to them here resolve: Mars installs meridian-base alongside
it, and the `plugin/` build bundles it. Codex and OpenCode plugins carry skills
only, so no `@agent` resolves there.

The plugin bundles the meridian-base version recorded in
`plugin/.mars-plugin.json`; after a meridian-base release that changes its
agents or skills, release this package so plugin users get it.

## Watching

Behavior a released change expects but no real run has shown yet. Check it on
the next runs that exercise it, then delete the entry, fixing the prompt first
if the runs show otherwise.

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
  having explorers find what's related first; without `@architect` it still builds or
  compares real alternatives instead of settling on the first structure it
  finds; when it goes past the design into planning or code, the problem
  needed it.
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
