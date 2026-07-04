---
name: agent-browser
type: reference
description: |
  Drive a real browser from the CLI with agent-browser: navigate, snapshot the
  accessibility tree with compact @eN refs, click/fill/extract, screenshot, read
  console and runtime errors, inspect network and React, and watch a session live
  in the dashboard. Use when a task needs a live browser: scraping, data or
  design-token extraction, form filling, verifying frontend rendering and flows,
  capturing screenshots, or reproducing a UI bug. Body covers the stable core loop
  and the commands you reach for most; load specialized skills (dogfood, electron,
  slack, cloud sandboxes) on demand via `agent-browser skills get`.
model-invocable: true
---

# agent-browser

Fast browser automation CLI. Chrome/Chromium over CDP, accessibility-tree
snapshots with compact `@eN` refs: interact with a page in a few hundred
tokens instead of parsing HTML.

Install once if the command is missing:

```bash
npm i -g agent-browser && agent-browser install   # add --with-deps on Linux
```

## Core loop

```bash
agent-browser open https://example.com
agent-browser snapshot -i        # interactive elements only, with @eN refs
agent-browser click @e3          # act on a ref from the snapshot
agent-browser snapshot -i        # re-snapshot after any page change
agent-browser close
```

Refs (`@e1`, `@e2`, …) are reassigned on every snapshot and go **stale the
moment the page changes**: after navigation, submits, dynamic re-renders.
Always re-snapshot before the next ref interaction.

## Commands you reach for

```bash
# interact
agent-browser fill @e1 "user@example.com"
agent-browser type "query"; agent-browser press Enter
agent-browser select @e9 "value"; agent-browser check @e12; agent-browser hover @e4

# read
agent-browser get text @e5          # also: html | value | attr <name> | url | title
agent-browser snapshot              # full tree (omit -i)
agent-browser eval "document.title"

# capture
agent-browser screenshot out.png    # --full for full-page
agent-browser pdf out.pdf

# diagnose
agent-browser console               # console messages
agent-browser errors                # runtime/page errors   (--json on either)
agent-browser network requests      # also: network har
agent-browser react tree|inspect|renders   # React component detail
agent-browser vitals                # performance

# wait / sessions
agent-browser wait --load networkidle
agent-browser close --all
```

Add `--json` for structured output to pipe elsewhere.

## Watch a session live

The dashboard is bundled into the binary (no install) and shows a live
viewport plus a command/console activity feed:

```bash
agent-browser dashboard start       # serves on :4848
agent-browser open https://example.com
```

Open `http://localhost:4848` (or a proxied URL like
`https://dashboard.agent-browser.localhost`). To watch from another device,
expose the port over tailscale when it's available:

```bash
tailscale serve 4848
```

## Going deeper

The binary serves docs matched to its installed version: load them when the
core surface isn't enough or a command behaves unexpectedly:

```bash
agent-browser skills get core --full    # full command reference + templates
agent-browser skills get dogfood        # exploratory testing / QA / bug hunts
agent-browser skills get electron       # desktop apps (VS Code, Slack, ...)
agent-browser skills get slack          # Slack workspace automation
agent-browser skills list               # everything on the installed version
```
