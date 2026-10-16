# Respond — Runbook 2: Oversight Restoration

Reference: Oct 2026 NIST / NSA / CISA joint guidance PP-26-4396, TLP:CLEAR, Respond
practice 2. Original operationalization; no reproduction of the source text.

## Objective
Re-establish reliable human oversight before any agent activity resumes: every
approval gate, log stream, and monitoring dashboard must be independently verified
working — not merely re-enabled.

## Trigger conditions
- Containment declared (runbook respond/01 complete).
- Any incident where logging, approval gates, or monitoring were disabled,
  bypassed, or went silent — even if containment was quick.
- Before ANY resumption of agent activity, however limited.

## Step-by-step actions
1. **Inventory what oversight existed.** From the pre-run control list (prepare/01):
   human-approval gates, log streams, dashboards, output filters, budget limits.
   Mark each as: intact / bypassed / disabled / unknown.
2. **Treat "unknown" as compromised.** If you cannot prove a control was working
   through the incident window, assume it was not. Rebuild it rather than
   trusting it.
3. **Restore from known-good configuration.** Rebuild each control from the
   versioned pre-run config — never by toggling the current (possibly tampered)
   state back on. Verify config hashes match the pre-run record.
4. **Verify independently of the agent.** The agent under investigation must play
   no role in proving oversight works. A second engineer — or an independent
   test harness — triggers each gate and confirms: the gate fires, the log
   records, the dashboard shows it, the alert routes.
5. **Re-establish the human in the loop.** Confirm named humans are at their
   stations for every approval gate that will be active on resumption. An
   approval queue with nobody watching is a disabled gate.
6. **Run the oversight smoke test.** Execute a scripted sequence: benign action
   (gate should pass), policy-violating action (gate should block), gate-bypass
   attempt (alarm should fire). All three must behave correctly before proceeding.
7. **Sign off in the decision record.** Commander + Control Engineer co-sign:
   oversight restored and independently verified at <time>. No resumption
   without this sign-off.

## Roles
- **Control Engineer:** rebuilds controls from known-good config; runs the smoke
  test (a second engineer verifies).
- **Oversight Operator:** confirms humans are staffed at every gate; owns
  dashboards.
- **Incident Commander:** co-signs the restoration; blocks resumption until done.
- **Evidence Custodian:** preserves pre/post config hashes and smoke-test logs.

## Evidence to preserve
- Per-control status table (intact / bypassed / disabled / unknown).
- Config hashes before and after restoration.
- Smoke-test results (all three scenarios, timestamped).
- The co-signed restoration decision record.

## Common pitfalls
- Re-enabling a tampered control instead of rebuilding from known-good config.
- Letting the incident agent "help verify" oversight. It is the subject, not the
  auditor.
- Verifying gates fire but not that a human is watching the queue. Both halves
  matter.
- Rushing this step because leadership wants the run resumed. Oversight
  restoration is the gate; there is no fast lane.
