---
name: research-web
description: "Load when a question depends on external facts (library docs, upstream issues, changelogs, production patterns) that may postdate training data. Gathers and reports; the caller judges."
model-invocable: false
metadata:
  type: reference
---

# Research Web

Gather broadly and leave the decision to the caller.

Search and read pages with the harness's built-in web tools when it has them; shell search tools are for harnesses that don't.

Search for current docs, recent discussions, and real-world usage patterns rather than relying on training data alone.

Issue trackers, post-mortems, and experience reports are higher-signal than marketing pages and quickstart tutorials.

Surface conflicting information. When sources disagree, cite both and say which is more current or authoritative, and why. When several approaches are credible, list each with its evidence and how strong that evidence is.

Include sources, caveats, and what you couldn't find. Save the pages and documentation you rely on into the work directory, so later agents read them there instead of fetching them again.

Your final message is your report.
