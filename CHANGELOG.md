# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

Versions prior to 0.0.14 are tracked only in git history.

## [Unreleased]

## [0.0.15] - 2026-04-10

### Added

- `caveman` skill (external dependency on
  [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)) loaded
  into the three intermediary orchestrators — `@design-orchestrator`,
  `@impl-orchestrator`, and `@docs-orchestrator` — to compress their
  coordination chatter (delegation prompts, decision log entries, phase
  status updates) without affecting human-facing artifacts. Each
  orchestrator runs `caveman full` mode with an agent-specific extension
  to caveman's "keep substance" rule: decision logs, phase status updates,
  and scenarios/ seeds still record the *why* in caveman style so resumed
  work can rehydrate reasoning. Sub-agent profiles (`@architect`, `@coder`,
  `@code-documenter`, `@tech-writer`, etc.) stay non-caveman, so design
  docs, code, fs/ mirrors, and user-facing docs are unaffected.
- `caveman` dependency declared in `mars.toml` — downstream projects that
  pin to `v0.0.15` pick it up transitively; pinning to `v0.0.14` skips the
  caveman layer entirely.

## [0.0.14] - 2026-04-10

### Added

- `@investigator` gained delegation capability — can now spawn
  `@smoke-tester`, `@explorer`, `@unit-tester`, `@internet-researcher`, or
  narrower `@investigator` instances (recursively) to get to ground truth
  on flagged issues. Sandbox bumped to `danger-full-access` so `gh`,
  `curl`, and web research tooling work reliably alongside file edits.
- `@impl-orchestrator` gained an "External knowledge gaps" escalation
  paragraph — when a `@coder` is stuck on how a library or API actually
  behaves, spawn an `@internet-researcher` instead of burning more
  `@coder` cycles guessing from training-data assumptions.
- `CHANGELOG.md` introduced, following the Keep a Changelog format.

### Changed

- Renamed `@researcher` → `@internet-researcher`. The new name advertises
  the distinguishing value (external/upstream knowledge) and pairs
  naturally with `@explorer` (the internal-codebase counterpart). The
  agent body was refreshed to make the "internet vs. codebase" split
  explicit and discourage overlap with `@explorer`.
- `@investigator` refocused around "diagnose → triage" with three outcomes
  (scoped fix, filed GitHub issue, documented non-issue). Dropped the
  dual-primary reactive/backlog-sweep split in favor of a single coherent
  role. Filing GitHub issues promoted to a first-class outcome — no
  longer a fallback.
- `@architect` "External research" section rewritten to frame external
  research as grounding design decisions in ecosystem knowledge rather
  than guessing from training data. Explicitly calls out the
  `@internet-researcher` vs `@explorer` distinction.
- `@design-orchestrator` "Research what you don't know" guidance now
  explicitly names `@internet-researcher` as "the single most-forgotten
  delegation in the design loop" and urges heavy use.
- `agent-staffing` skill's `builders.md` now headlines
  `@internet-researcher` with the same framing and reframes `@explorer`
  as "the internal counterpart to `@internet-researcher`."
- README prose and agent table updated for the rename.

### Removed

- `@researcher` profile (replaced by `@internet-researcher`).
