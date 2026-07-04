# Source Study Method

## Cloning

```bash
mkdir -p ~/.meridian/ref
git clone <url> ~/.meridian/ref/<name>
```

Full clone by default: explorers need `git log` and `git blame` to trace how designs evolved and why boundaries were drawn.

For large repos (monorepos, multi-GB histories), clone shallow and deepen as needed:

```bash
git clone --depth 50 <url> ~/.meridian/ref/<name>    # recent history
git -C ~/.meridian/ref/<name> fetch --deepen=200      # extend window
git -C ~/.meridian/ref/<name> fetch --unshallow        # full history
```

Don't delete after investigation. `~/.meridian/ref/` accumulates over time. A repo studied once may be relevant again.

## Explorer Prompt Examples

Each spawn gets one focus area:

- "How does <project> handle auth across its API surface? Trace the middleware chain and report the pattern."
- "What are the module boundaries in <project>? Map the top-level directory structure and how they import each other."
- "How does <project> structure its error types? Find the error hierarchy and how errors propagate to callers."
- "What's the data model for <concept> in <project>? Trace the types from storage through to API response."

## Synthesis

The synthesis explorer merges individual reports into:

- Patterns that appear across projects (convergent design)
- Tradeoffs different projects made (divergent design)
- Surprises you wouldn't have thought of from docs alone
- Concrete implications for your own work
