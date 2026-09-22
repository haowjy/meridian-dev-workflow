# Maintainers

## Documentation

@kb-lead: maintain content in `.context/`, the KB, and user-facing `docs/` after shipped work, research, or before conversation decisions are lost. Pass the originating session, changed files, and design artifacts. Human decisions are authoritative; design artifacts let it compare intent with implementation. Delegate structural changes to @kb-maintainer.

@kb-maintainer: reorganize documentation and repair links, diagrams, and naming. Use after content updates or when a documentation tree becomes hard to navigate. Pass the target tree. It flags stale or contradictory content for the content owner rather than deciding its truth. Use @explorer to compare documentation claims with code.

## Issue Mining

@investigator:

- **Proactive**: find deferred work, latent bugs, TODOs, and unresolved questions in conversations, code, and spawn reports at phase boundaries.
- **Reactive**: find the cause of unexpected test failures, ambiguous review findings, or surprising spawn results. Provide the failure evidence and relevant context; require a fix, a tracked issue, or evidence that no issue exists.
