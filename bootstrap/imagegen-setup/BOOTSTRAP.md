# Image Generation Setup (Optional)

The `imagegen` agent generates images via Codex. This capability is not
available in all environments and is not required for most workflows.

**Before configuring:** Ask the user whether they want image generation
enabled. Skip this setup if they don't need it.

## Requirements

- Codex harness must be available
- Image generation must be supported by the Codex backend in use

## Configuration

If the user wants image generation, add to `.codex/config.toml`:

```toml
[features]
image_generation = true
```

Without this flag, image generation calls will fail silently or return
errors.

## When to skip

Skip this setup if:

- The project does not use visual assets (mockups, diagrams, icons)
- The Codex backend in use does not support image generation
- The user prefers external tools for image work
