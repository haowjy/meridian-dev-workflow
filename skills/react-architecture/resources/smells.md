# React Architecture Smells

Detailed hunt lists for each structural dimension. Use alongside the body heuristics.

## Token Smells

- Raw hex/rgb colors instead of semantic token references
- Hardcoded spacing values (px, rem) instead of spacing scale tokens
- One-off font sizes, weights, or line heights outside the type scale
- Inline border-radius, shadow, or z-index values that should be tokens
- Component-level color/spacing overrides that fight the theme

Good: semantic CSS variables (`--background`, `--foreground`, `--primary`), one source of truth for spacing/type/radius/shadow/color/breakpoints, runtime theming through variable swaps.

## State Smells

- Server/remote data copied into Zustand or global stores, duplicating cache/invalidation/sync logic that TanStack Query already handles
- Context used as a global store for interactive state
- State lifted higher than necessary, creating invisible dependencies
- Duplicated or contradictory state (two sources of truth)
- Missing URL state for filters, tabs, pagination, selected entities

Good: local component state for transient UI, context for stable app-wide metadata, TanStack Query for remote/server state, Zustand for client-global interactive state, URL state for navigation-meaningful selections.

## Composition Smells

- Prop drilling through 3+ levels where composition (children/slots) or context would be cleaner
- Components with 10+ props
- Nested component definitions inside render (creates new identities, destroys state, breaks memoization)
- Premature extraction with one caller
- Monolith components mixing orchestration, rendering, and data fetching

Good: compound component pattern (`Tabs`/`TabsList`/`TabsTrigger`/`TabsContent`), children and slots over deep prop threading.

## Import Smells

- Cross-feature imports (`features/billing/` importing `features/auth/` internals)
- Barrel file sprawl creating circular dependencies and slow dev startup
- No boundary between shared primitives and feature-specific code
- Import chains forcing 4+ files to understand one component

Good: feature internals (hooks, stores, components, styles) colocated with the feature they serve.

## API Consistency Smells

- Inconsistent variant prop naming (`size="sm"` vs `size="small"` vs `isSmall={true}`)
- Mixed composition patterns (children vs render props vs slot props for the same kind of content)
- Inconsistent naming conventions (`UserCard` vs `cardUser` vs `user-card`)
- Missing or inconsistent TypeScript prop types
