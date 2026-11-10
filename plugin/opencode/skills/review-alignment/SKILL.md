---
name: review-alignment
description: Load when one artifact must faithfully match another (plan vs design, code vs spec, output vs intent) and the check needs to be systematic, not a skim.
metadata:
  type: reference
---

# Review Alignment

Check, promise by promise, that one artifact delivers what another
promised. `/meridian-dev-workflow:review` owns the verdict; load this when the check must be
systematic.

Read the source of truth first, including `DIVERGENCE/` in the work
directory, since a logged divergence is plan, not drift. List what it
promises: outcomes, structural intent (layer boundaries, seams, ownership),
and, when you have the conversation, the human's stated priorities. Then
mark each promise against the checked artifact:

- **Covered**, with one sentence of evidence.
- **Gap:** missing, and where coverage was expected.
- **Partial:** what's covered and what's missing.
- **Drift:** delivered, but not as intended; say how it diverges.

Report gaps and drift first, and leave routing the fixes to your caller.
