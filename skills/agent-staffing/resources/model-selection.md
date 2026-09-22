# Model Selection

Explicit caller choices and role-specific policies take precedence over these
general preferences. Check the live model catalog and runnable routes before
selecting an alternative; a familiar alias does not prove availability.

## Implementation and Execution

Prefer **Luna → DeepSeek → Sonnet** for general implementation and execution.
Luna and DeepSeek can own substantial, coherent engineering objectives; do not
restrict them to mechanical edits or fragment the work to justify using them.

Give a detailed brief: desired outcome, relevant source or design context,
constraints, acceptance criteria, and the evidence that will demonstrate success.
Specify behavior and boundaries rather than dictating every edit.

Qwen is another option when a suitable local model is actually available. Check
the specific model's capabilities and route rather than assuming a Qwen alias
or local endpoint exists.

## When a Larger Model Earns Its Cost

| Need | Preferred model |
|---|---|
| Difficult technical analysis or technically demanding work | Sol |
| Consequential decisions and important communication | Astra |
| Consequential decisions and communication requiring particularly strong judgment and writing quality | Fable |
| Deep, sustained implementation work | Opus |

These are task-based preferences, not a universal ranking. Routine implementation
stays with the cheaper workers; choose a larger model when the particular task
needs its technical depth, judgment, or writing quality.

Writing quality is a separate capability from coding strength. For writing-heavy
work, choose a model that produces clear, coherent prose without generic filler
and preserves the source's meaning. A cheap implementation model is not
automatically a good writer. When the technical content is already grounded,
a focused writing or editing pass can avoid paying for a larger model throughout
the implementation; pass the source evidence and intended audience, not just a
rough summary. If judgment and communication cannot be separated, staff for both
from the start.

## Capability and Escalation

For screenshots and rendered interfaces, verify image input and the required
tools on the selected route. Browser operation and visual design taste are
different capabilities. Use training-eligible endpoints, including Muse
Contributor, only when the submitted context is appropriate for those terms.

Launch fallback is not performance escalation. If a worker's result misses the
goal, diagnose whether it lacked context, a required tool, or model capability.
Correct the brief or route when that is the cause; choose a stronger model when
the remaining difficulty calls for it. Pass the failed attempt and evidence so
the next worker can build on what was learned.
