# Prepare — Runbook 2: Escalation Paths and Authority Matrix

Reference: Oct 2026 NIST / NSA / CISA joint guidance PP-26-4396, TLP:CLEAR, Prepare
practice 2. Original operationalization; no reproduction of the source text.

## Objective
Define in advance who can authorize what during an SI control incident — including
the authority to kill a run worth millions of dollars — so decisions take minutes,
not a meeting.

## Trigger conditions
- Reviewed at T-7 days before any training/eval run (with runbook 01).
- Reviewed quarterly, and immediately after any leadership or roster change.
- Activated during any suspected SI control incident (this runbook becomes the
  authority reference the moment the incident channel opens).

## Step-by-step actions
1. **Write the authority tiers.** Minimum set:
   - Tier 0 (any roster member): freeze agent actions, open the incident channel.
   - Tier 1 (Incident Commander): halt the training run, revoke credentials,
     engage external support.
   - Tier 2 (executive sponsor + Commander): disclose to external authorities,
     authorize data-destructive containment, pause the whole training program.
2. **Name the people per tier, with deputies.** A tier without a reachable human is
   a broken tier. Record phone numbers, not just handles.
3. **Define the decision record.** Every Tier 1+ decision is logged with: time,
   decider, options considered, action taken, rationale in one sentence. No
   decision happens off-record.
4. **Pre-authorize the expensive actions.** The halt of a large training run is the
   classic failure point — engineers wait for budget approval while the incident
   burns. Get written pre-authorization from finance/leadership that halting a run
   for a suspected control incident will not be second-guessed.
5. **Set escalation timers.** If the Commander has not acknowledged within 10 min,
   the deputy assumes command automatically and the timer is logged. If a Tier 2
   authority is unreachable within 30 min, Tier 1 may act and document the gap.
6. **Publish the "who wakes whom" tree.** A one-page diagram pinned in the incident
   channel: detector → Commander → deputies → executive sponsor → external.
7. **Rehearse a disagreement.** In the quarterly drill, inject a scenario where two
   tiers disagree (e.g., engineer wants to halt, executive hesitates on cost).
   Practice the conflict path, not just the happy path.

## Roles
- **Incident Commander:** holds Tier 1 authority; enforces the timer rules.
- **Executive sponsor:** holds Tier 2 authority; must be reachable, not just named.
- **Control Engineer:** may invoke Tier 0 actions unilaterally; documents them.
- **Communications Lead:** owns external escalation once Tier 2 authorizes it.

## Evidence to preserve
- The signed authority matrix (who, which tier, deputies, dates).
- The pre-authorization memo for expensive halt actions.
- All Tier 1+ decision records from real incidents and drills.

## Common pitfalls
- Authority that exists on paper but was never socialized with the person holding
  it. Call them and confirm.
- Timers with no automatic failover — "we'll figure it out" is not an escalation.
- Logging decisions in chat threads that scroll away. Use the decision record.
- Assuming the executive sponsor will be available. Deputies and unreachable
  clauses exist for a reason.
