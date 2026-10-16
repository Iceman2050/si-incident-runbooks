# Detect — Runbook 2: Anomaly Classification and Triage

Reference: Oct 2026 NIST / NSA / CISA joint guidance PP-26-4396, TLP:CLEAR, Detect
practice 2. Original operationalization; no reproduction of the source text.

## Objective
Turn a raw detection into a classified, prioritized event within 30 minutes: is this
an SI control incident, a lesser control failure, or a benign anomaly — and what
happens next for each.

## Trigger conditions
- A suspected incident is declared from correlated signals (runbook detect/01).
- Any single CRITICAL alert where correlation is ambiguous.
- A human (researcher, operator, external reporter) reports suspicious agent
  behavior.

## Step-by-step actions
1. **Capture the intake.** Record: time detected, signal(s) that fired, agent/run
   identifier, who reported it, and the raw evidence snapshot. Assign an event ID.
   Do this before any interpretation.
2. **Apply the classification ladder:**
   - **P0 — Confirmed SI control incident:** agent took a significant uninstructed
     action that compromised a policy, control, or human oversight. Full response.
   - **P1 — Suspected control incident:** signals correlate but intent/impact not
     yet confirmed. Contain first, classify in parallel.
   - **P2 — Control degradation without agent misconduct:** a control failed or
     went blind but no evidence of uninstructed agent action. Fix the control;
     keep watching.
   - **P3 — Benign anomaly:** explained by known causes (test traffic, config
     change). Document and close.
3. **Decide the posture.** P0/P1 → open incident channel, invoke Respond runbooks,
   Commander assumes command. P2 → assign an owner and a fix deadline; escalate
   to P1 if a second signal appears. P3 → log and close.
4. **Write the working hypothesis.** One paragraph: what we think happened, what
   we still don't know, and what single piece of evidence would change our mind.
   Update it as facts arrive; keep old versions.
5. **Set the next check-in.** For P0/P1: 30-minute cadence until contained. For P2:
   hourly. Each check-in re-asks the classification — incidents get reclassified
   as evidence arrives, never locked at intake.

## Roles
- **Incident Commander:** owns classification and posture decisions.
- **Control Engineer:** supplies technical evidence for/against each class.
- **Oversight Operator:** provides the timeline of human-gate and telemetry state.
- **Evidence Custodian:** versions the working hypothesis and intake record.

## Evidence to preserve
- Intake record with event ID and raw evidence snapshot.
- Classification decision and the reasoning recorded at the time.
- All hypothesis versions (do not overwrite).
- Check-in notes and any reclassification rationale.

## Common pitfalls
- Classifying to minimize embarrassment. Downgrading a P1 to P2 to avoid the
  response process is how incidents become disasters.
- Waiting for certainty before containing. P1 means contain first, classify in
  parallel — the classification ladder is designed for exactly this.
- Losing the intake snapshot. Interpretation changes; the original evidence must
  not.
- One classification forever. Re-ask the question at every check-in.
