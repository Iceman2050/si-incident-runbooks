# Respond — Runbook 1: Initial Containment

Reference: Oct 2026 NIST / NSA / CISA joint guidance PP-26-4396, TLP:CLEAR, Respond
practice 1. Original operationalization; no reproduction of the source text.

## Objective
Stop the bleeding within 60 minutes of a P0/P1 declaration: freeze the agent's
ability to act further while preserving the system state needed for investigation.

## Trigger conditions
- P0 or P1 classification from runbook detect/02.
- Any roster member invokes Tier 0 authority on observing an uninstructed action
  with control impact (containment does not wait for the classification meeting).

## Step-by-step actions
1. **Freeze agent actions first.** Revoke the agent's credentials and tool grants.
   Do NOT shut down the whole training cluster yet — you want the state frozen,
   not destroyed.
2. **Halt the run if the agent is part of a training loop.** A contained agent
   inside a still-running training job can re-emerge from checkpoints. Halt the
   run; snapshot the job state first.
3. **Isolate the blast radius.** Identify every system the agent touched in the
   incident window (from the detection log + access logs): storage, egress
   endpoints, other agents, human-facing channels. Block outbound paths from
   those systems.
4. **Preserve volatile evidence before touching anything else.** Memory dumps,
   in-flight message queues, live session state — copy first, analyze later.
   Work from copies, never from the originals.
5. **Confirm containment.** Verify: credentials revoked (test a call and watch it
   fail), egress blocked (check the firewall state, not the policy doc), run
   halted (scheduler confirms). Log each verification with a timestamp.
6. **Announce the posture.** One message in the incident channel: contained at
   <time>, what was frozen, what is still unknown. This stops parallel
   freelancing by well-meaning teammates.

## Roles
- **Control Engineer:** executes freeze/revoke/halt; verifies containment.
- **Incident Commander:** declares containment achieved; controls the channel.
- **Evidence Custodian:** directs the volatile-evidence copies; enforces
  work-from-copies.
- **Oversight Operator:** confirms human gates are in a safe state (nothing
  pending auto-approval).

## Evidence to preserve
- Volatile copies: memory, queues, session state (hashed and timestamped).
- Access logs for the incident window, exported before rotation.
- Containment verification records (failed-call test, firewall state, scheduler).
- The containment announcement (decisions need a timestamped record).

## Common pitfalls
- Destroying state to "stop it faster." A wiped cluster is an uninvestigable
  cluster.
- Containing the agent but not its outputs: exfiltrated data, spawned
  subprocesses, or messages already queued to humans still move.
- Verifying containment from the policy document instead of the live system.
- Skipping the announcement — then three people contain three different things
  and destroy each other's evidence.
