# Prepare — Runbook 1: Incident Readiness Playbook

Reference: Oct 2026 NIST / NSA / CISA joint guidance "Key Practices for Incident
Readiness and Response in Super Intelligence Training and Evaluation" (PP-26-4396,
TLP:CLEAR), Prepare practice 1. This runbook restates nothing from that text; it is an
original operationalization for training and evaluation teams.

## Objective
Make sure that before any SI training or evaluation run, the organization can stand
up a control-incident response within one hour: people know their jobs, channels are
open, access exists, and the definition of an "SI control incident" is unambiguous.

## Trigger conditions (when this runbook is exercised)
- A new training run, fine-tune, or eval campaign is scheduled (run it at T-7 days).
- Quarterly, as a readiness audit (run it even if nothing is scheduled).
- After any real control incident is closed (run it as the readiness re-certification
  step before resuming training).

## Step-by-step actions
1. **Define the incident scope.** Write the one-paragraph definition of an SI control
   incident your team uses: any agent taking a significant uninstructed action that
   compromises a policy, a control, or human oversight. Post it where everyone can see
   it. If you cannot agree on the sentence, you are not ready.
2. **Stand up the incident roster.** Confirm named individuals (not job titles) for:
   Incident Commander, Control Engineer, Oversight Operator, Evidence Custodian,
   Communications Lead. Record deputies for each.
3. **Provision a dedicated incident channel.** Create it now, not during the incident.
   Verify all roster members can post, pin, and read. Pin the roster and this runbook.
4. **Grant pre-authorized access.** The Control Engineer must be able to halt a
   training run, revoke agent credentials, and freeze weights/storage without
   waiting for a ticket. Test each action against a non-production sandbox.
5. **Inventory your controls.** List every control that must stay intact during the
   run: human-approval gates, logging/telemetry, output filters, sandbox boundaries,
   budget/quota limits. Record each control's owner and health signal.
6. **Establish the evidence repository.** A write-once store (append-only directory,
   immutable bucket, or signed log) the Evidence Custodian controls from minute one.
7. **Run a cold-start drill.** Page the roster with no warning and measure
   time-to-acknowledge for each member. Target: all five acknowledged within 15 min.
   Log the result; anything slower is a finding, not a shrug.
8. **Sign off.** Incident Commander records readiness state (READY / READY WITH
   FINDINGS / NOT READY). A training run does not start in NOT READY state.

## Roles
- **Incident Commander:** decides readiness state, runs the drill, owns the roster.
- **Control Engineer:** proves halt/revoke/freeze actions work; owns the control list.
- **Oversight Operator:** verifies human gates and monitoring dashboards are live.
- **Evidence Custodian:** stands up the repository; defines chain-of-custody rules.
- **Communications Lead:** confirms notification paths (internal + any mandatory
  external reporting) function end-to-end.

## Evidence to preserve
- The dated readiness sign-off and drill timing log.
- Screenshots/records of pre-authorized access tests.
- The agreed incident definition and control inventory (versioned).
- Any findings and their remediation owners.

## Common pitfalls
- Treating a quarterly slide deck as readiness. Readiness is demonstrated access
  and demonstrated speed, not a document.
- Rostering job titles instead of names. "On-call engineer" cannot be paged.
- Granting halt access in theory only — never tested against the real run
  infrastructure.
- Defining the incident scope during the incident. That argument costs hours.
