# Recover — Runbook 1: Service Restoration

Reference: Oct 2026 NIST / NSA / CISA joint guidance PP-26-4396, TLP:CLEAR, Recover
practice 1. Original operationalization; no reproduction of the source text.

## Objective
Bring training/evaluation activity back online in controlled stages, proving at
each stage that the neutralized threat has not returned and oversight holds.

## Trigger conditions
- Threat neutralized and declared (runbook respond/03 complete).
- Commander approves a staged resumption plan in the decision record.

## Step-by-step actions
1. **Write the stage plan.** Minimum stages:
   - Stage 0: infrastructure only — no agent activity; verify all systems healthy.
   - Stage 1: sandboxed agent with no tools, no network, human review of every
     output.
   - Stage 2: tools re-enabled one at a time, each under heightened monitoring.
   - Stage 3: normal run parameters with the new detection signals active.
   Advance only on explicit Commander sign-off per stage.
2. **Define stage exit criteria in advance.** For each stage: what must be true
   (e.g., "24h with zero P1+ alerts", "smoke test passes twice") before moving
   on. Write them before Stage 0 starts.
3. **Keep the incident channel open** through at least Stage 2. The response team
   stays on watch; this is not "back to normal" yet.
4. **Monitor for recurrence signatures.** The new detection signal from
   neutralization (respond/03) is the primary watch item. Any recurrence at any
   stage → halt, re-classify, return to Respond.
5. **Restore data and state deliberately.** Rebuild run state from pre-incident
   known-good snapshots, not from incident-window artifacts. Document what was
   restored from where.
6. **Declare full recovery.** Commander signs the decision record: all stages
   passed, exit criteria met, incident channel closed, normal operations resume.
   Notify all stakeholders named in the communications plan.

## Roles
- **Incident Commander:** owns stage gates; declares full recovery.
- **Control Engineer:** executes each stage; runs exit-criteria checks.
- **Oversight Operator:** staffs gates through the staged resumption.
- **Communications Lead:** notifies stakeholders at full recovery.

## Evidence to preserve
- The stage plan with exit criteria (dated, pre-Stage 0).
- Per-stage sign-offs and exit-criteria evidence.
- Monitoring records through all stages.
- The full-recovery declaration.

## Common pitfalls
- Skipping stages because "it looks fine." The stages are the proof.
- Restoring state from incident-window snapshots and re-importing the problem.
- Closing the incident channel at Stage 1 to "reduce noise." The watch team is
  the safety net.
- Vague exit criteria ("looks good") that let anyone declare a stage passed.
