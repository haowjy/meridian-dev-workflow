---
name: goal-writing
description: |
  Load when turning intent into an executable goal for an agent, delegated run, work item, experiment, or handoff. Use to define outcome, evidence, constraints, anti-goals, stop conditions, and reporting shape before work begins.
metadata:
  type: reference
alwaysApply: false
---

# Goal Writing

A goal says what should become true, what evidence proves it, and what the
agent must not do on the way. Write the parts that would change what the
agent does:

- **Outcome**, observable when the work succeeds, and **why** it matters.
- **Ground truth:** the files, baselines and prior choices to treat as
  authoritative.
- **Scope and constraints:** what's in, what's out, which outcome wins when
  two conflict, and the limits on cost,
  risk and compatibility.
- **Evidence:** the command, metric, artifact or review that shows the
  outcome.
- **Anti-goals:** shortcuts that would hit the metric and miss the point.
- **When to stop or ask**, and **what to report**.

For a goal shaped like "improve X", fix the baseline and the evaluator that
may not change, say what counts as cheating or overfitting, set the budget,
and ask for every meaningful attempt, not only the best. When nobody yet
knows how to improve it, write a learning goal first: find the mechanism,
then set the performance goal. When one attempt's result should change the
next, say what changes between attempts, what is observed, and where it is
logged.

Add an independent reviewer when the goal rewards cheating, hiding failures
or redefining success, and have it review before the result is written up as
a win.

Check the goal: could two agents read it and aim at the same outcome, and
could success be verified without trusting the agent's word?
