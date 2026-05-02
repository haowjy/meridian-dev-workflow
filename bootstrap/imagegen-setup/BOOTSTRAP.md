# Image Generation Setup

The `imagegen` agent requires Codex image generation to be enabled.

Add the following to your project-level `.codex/config.toml`:

```toml
[features]
image_generation = true
```

Without this flag, image generation calls will fail silently or return errors.
