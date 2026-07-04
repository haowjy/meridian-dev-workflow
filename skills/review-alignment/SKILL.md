---
name: review-alignment
type: reference
description: "Alignment verification: does one artifact faithfully represent another? Coverage, drift, gap classification. Load when verifying plan vs design, code vs spec, output vs intent."
model-invocable: false
---

# Review Alignment

Verify that one artifact faithfully represents another. `/review` judges quality within an artifact: correctness, structural health, security. You judge fidelity between artifacts: does the checked artifact deliver what the source-of-truth artifact promised?

## Procedure

Read the source-of-truth artifacts first. Build a mental checklist of what they promise. Then read the artifact being checked and verify each promise has coverage. When conversation history is available (via `--from` or `$MERIDIAN_CHAT_ID`), mine it for user intent and decisions that may not have made it into formal artifacts.

## What You Check

**Requirement coverage.** Every outcome or goal in the source of truth maps to concrete work in the checked artifact.

**Requirements traceability.** Every stated requirement maps to delivered code that actually satisfies it. A requirement listed but not implemented is a gap.

**Structural intent.** Does the checked artifact match the architectural intent of the source of truth? Layer boundaries, seam placement, ownership splits. Implementation that works but violates the design's structural model is drift.

**Conversational intent.** When conversation history is available, check whether the user's stated priorities and decisions survived into the formal artifacts and downstream work.

## Report Format

For each source-of-truth item checked:

- **Covered**: the checked artifact delivers this. One sentence of evidence.
- **Gap**: the checked artifact does not deliver this. State what's missing and where coverage was expected.
- **Partial**: partially delivered. State what's covered and what's missing.
- **Drift**: the checked artifact delivers something, but it doesn't match the intent. State the divergence. If the item is both incomplete and divergent, classify as Drift and note the remaining gap.

End with a summary: total items checked, covered count, gap count, partial count, drift count.

## Scope

You verify alignment: state gaps and let the orchestrator route fixes. Code quality and structural health belong to `/review`, tests to tester agents.
