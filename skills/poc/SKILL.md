---
name: poc
description: "Load when a feasibility question needs an answer from running code: throwaway code that answers it, then is deleted."
model-invocable: true
user-invocable: true
metadata:
  type: mode-shift
harness-overrides:
  claude:
    argument-hint: What question should the POC answer?
---

# POC

State the question, build what answers it, report what you learned.
