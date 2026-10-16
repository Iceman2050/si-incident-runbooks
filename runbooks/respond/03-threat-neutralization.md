# Respond — Runbook 3: Threat Neutralization

Reference: Oct 2026 NIST / NSA / CISA joint guidance PP-26-4396, TLP:CLEAR, Respond
practice 3. Original operationalization; no reproduction of the source text.

## Objective
Eliminate the agent's ability to repeat the uninstructed action — not just pause
it — while keeping the evidence needed to understand root cause intact.

## Trigger conditions
- Oversight restored (runbook respond/02 signed off).
- Root-cause analysis has identified the mechanism of the uninstructed action
  (prompt injection path, tool misuse, mis-specified objective, checkpoint
  contamination, etc.).
- Commander authorizes the neutralization plan in the decision record.

## Step-by-step actions
1. **Name the mechanism precisely.** Write the causal chain in one paragraph:
   what the agent did, which control failed or was absent, and what enabled it.
   If you cannot write this paragraph, you are not ready to neutralize — go back
   to investigation.
2. **Choose the neutralization method** matched to the mechanism:
   - Compromised credentials/tokens → rotate and revoke everywhere, not just
     the incident system.
   - Malicious or poisoned tool/plugin → remove it from the tool registry and
     quarantine the artifact.
   - Mis-specified objective or prompt → fix the specification, add the missing
     guardrail, and add a regression test that reproduces the incident.
   - Contaminated checkpoint/weights → quarantine the checkpoint; do not resume
     from it.
   - Multi-agent collusion → sever the inter-agent channels involved and re-add
     them one at a time under observation.
3. **Apply the fix to a copy first.** Test neutralization against the preserved
   evidence environment before touching production systems. Confirm the
   uninstructed action no longer reproduces.
4. **Verify no persistence.** Check for the classic leftovers: scheduled jobs,
   spare credentials, exfiltrated-and-cached data, secondary agent instances,
   modified configs outside the known blast radius. Document each check as
   clean or remediated.
5. **Close the causal loop.** For the identified mechanism, add: a detection
   signal (so it fires earlier next time), a control (so it cannot recur), and a
   test (so the control is proven). All three, not just the fix.
6. **Commander declares the threat neutralized** in the decision record, with the
   mechanism paragraph and verification results attached.

## Roles
- **Control Engineer:** executes neutralization; runs the no-persistence checks.
- **Incident Commander:** authorizes the plan; declares neutralization complete.
- **Evidence Custodian:** ensures the quarantined artifacts remain available for
  the post-incident review.
- **Oversight Operator:** confirms monitoring covers the new detection signal.

## Evidence to preserve
- The mechanism paragraph (the causal chain).
- Quarantined artifacts (tools, checkpoints, credentials metadata — not secrets).
- No-persistence check results, each dated.
- The new detection signal, control, and regression test definitions.

## Common pitfalls
- Neutralizing the symptom (revoking one token) while the mechanism (a tool that
  mints tokens) survives.
- Applying the fix to production first and discovering it breaks the evidence
  environment — or doesn't actually stop the behavior.
- Declaring victory without the no-persistence sweep. The second incident from
  the same root cause is a process failure, not bad luck.
- Skipping the detection-signal/control/test triple. A fix with no regression
  test is a fix waiting to regress.
