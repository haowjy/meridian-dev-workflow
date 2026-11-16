# Testers

## Briefing a Prober

Lead with the user: who they are, what they are trying to get done, and what
changed for them. Then name the risky areas: where the change could show the
wrong thing, lose work, or leave the user stuck. Ask the prober to use the
system as that user would and report anything odd, not only what the brief
predicts. A script of steps with expected results turns it into a checklist
runner that checks the rows and stops noticing. Write exact steps only for
conditions a user can't create by hand, such as a held or refused request,
going offline, or a second session acting at the same time, and give the
mechanism for each.

One brief covers both the existing flows near the change that must still
work and the new behavior, on every viewport the change reaches. Checks
that would share state run one after another in that one run.

## When to Probe

Probe once, on the final code, after review has converged; `reviewers.md`
After the Review says what happens to what it finds.
