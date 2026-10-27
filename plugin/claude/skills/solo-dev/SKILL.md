---
name: solo-dev
description: 'Load when you implement and verify a change yourself, in one session, instead of delegating it: what you do yourself and what still goes to a spawn.'
disable-model-invocation: true
metadata:
  type: reference
---

# Solo Dev

Write the production code yourself. Briefing a worker and checking its
result costs more than a change you can hold in your head.

Spawn what needs a context of its own: the lanes `/meridian-dev-workflow:dev-workflow` staffs
(review, probe, merges, knowledge capture), an investigation, exploration
that would fill your context, and disposable alternatives built in
parallel for comparison.

Fix local problems you touch; report larger unrelated ones.
