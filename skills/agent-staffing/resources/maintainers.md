# Maintainers

## Documentation

@kb-lead: maintain content in `.context/`, the KB, and user-facing `docs/`. For development work, `/post-dev` runs it when the change settles; spawn it directly for research or explicit knowledge maintenance. Brief it as its description asks, adding design artifacts so it can compare intent with implementation. Delegate structural changes to @kb-maintainer.

@kb-maintainer: reorganize documentation and repair links, diagrams, and naming. Use after content updates or when a documentation tree becomes hard to navigate. Pass the target tree. It flags stale or contradictory content for the content owner rather than deciding its truth. Use @explorer to compare documentation claims with code.

## Issue Mining

@investigator:

- **Proactive**: find deferred work, latent bugs, TODOs, and unresolved questions in conversations, code, and spawn reports at phase boundaries.
- **Reactive**: find the cause of unexpected test failures, ambiguous review findings, or surprising spawn results. Provide the failure evidence and relevant context, and say whether it should fix the cause or stop at the causal chain.
