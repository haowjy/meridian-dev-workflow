# Maintainers

Agents that keep the project healthy — extracting decisions before they're lost, updating documentation to match reality, surfacing deferred issues before they compound. These don't build new features or review code; they maintain the connective tissue that lets future agents (and humans) work effectively.

## Documentation

@kb-lead — captures durable knowledge across every documentation layer. Surveys what the docs say now, mines what happened (fans out @explorer per codebase area and @session-miner per conversation as read-only investigators), reconciles against what the human decided, and writes the updates inline: `.context/` contracts, KB pages, and user `docs/`. The human's decisions in the originating session are canonical. Run after work items ship, after research produces durable findings, or when conversation context holds decisions compaction will erase. Hand it the originating session as context plus the changed files and design artifacts with `-f`; it mines the broader work history itself via `@session-miner`. For shipped implementation, also pass design artifacts so it can diff intent against outcome. Hands structure to @kb-maintainer.

@kb-maintainer — structural health of any documentation tree (KB, code-local `.context/`, user `docs/`, work-item `design/`). Treats docs like code: one concern per doc (split oversized docs, merge fragments), folder structure as domains grow, broken cross-references (`meridian kg check`), diagram validation (`meridian mermaid check`), naming that matches content. Flags contradictions and stale content for the caller, resolving what it confidently can and leaving `> [!FLAG]` inline markers for issues needing human review. Run after @kb-lead writes, at work-item boundaries, or when navigability degrades. Base agent from meridian-base; spawn `@explorer` for comparing doc claims against current code.

## Issue Mining

@investigator — surfaces problems before they compound. Two modes:

- **Proactive backlog sweeps** — mines conversations, code, and spawn reports for deferred items, latent bugs, TODO debt, and unresolved questions at phase boundaries. These items are invisible in the code and lost from conversations after compaction — if nobody extracts them at phase boundaries, they accumulate silently.
- **Reactive investigation** — digs into root cause when a test fails unexpectedly, a @reviewer flags something ambiguous, or a spawn produces surprising results. Either quick-fixes the issue, files it for tracking, or closes it as a non-issue with reasoning.
