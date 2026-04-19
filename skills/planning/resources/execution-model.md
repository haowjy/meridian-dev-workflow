# Execution Model

The plan is executed by @impl-orchestrator as a nested loop: phases outside, subphases inside, with verification at both levels.

```mermaid
flowchart TB
    START([Read Plan]) --> PHASE

    subgraph PHASE["FOR EACH PHASE"]
        direction TB

        subgraph SUBPHASE["FOR EACH SUBPHASE"]
            C["@coder / @refactor-coder / @frontend-coder"]
            C --> LV["Light @verifier<br/>(build + existing tests)"]
            LV --> LR{"Issues?"}
            LR -->|yes| C
            LR -->|no| NEXT_SUB([Next Subphase])
        end

        NEXT_SUB --> GATE

        subgraph GATE["PHASE EXIT GATE"]
            direction LR
            V["@verifier<br/>(full)"]
            ST["@smoke-tester<br/>(verify mode)"]
            UT["@unit-tester /<br/>@integration-tester"]
            RV["@reviewer<br/>(fan-out)"]
            RFR["@refactor-reviewer"]
        end

        GATE --> PASS{"Gate passes?"}
        PASS -->|no, findings| C
        PASS -->|yes| COMMIT([Commit phase])
        COMMIT --> NEXT_PHASE([Next Phase])
    end

    NEXT_PHASE --> FINAL

    subgraph FINAL["FINAL GATE"]
        FRV["@reviewer fan-out<br/>(full change set)"]
        FST["@smoke-tester"]
        CHECK["Verify plan coverage<br/>Verify design alignment"]
    end

    FINAL --> GAPS{"Gaps found?"}
    GAPS -->|yes, add phases| PHASE
    GAPS -->|no| DONE([Ship])
```

## Why Two Levels

- **Light verification between subphases** catches drift early, inside the phase, while context is fresh and the fix is cheap. Full fan-out between subphases would be over-processing.
- **Full gate at phase boundaries** enforces the real quality bar before the phase commits. Subphases can break things temporarily; the gate catches what slipped.
- **Final gate after all phases** proves the whole change set hangs together and matches the design. Discovered gaps feed back as new phases.

## Fix-Cycle Routing

- Light-verification issues within a subphase → back to the same coder spawn (context is still fresh).
- Phase-gate issues → back into the phase, usually as a scoped coder fix followed by re-running the affected lanes, not the full gate.
- Final-gate gaps → new phase appended to the plan, following the normal phase loop.

## When Subphases Are Omitted

If the phase is small enough that a single coder session can finish it before intermediate verification would help, the phase can be flat — no subphases, just the phase exit gate. The plan should mark these explicitly rather than leaving the reader to infer.
