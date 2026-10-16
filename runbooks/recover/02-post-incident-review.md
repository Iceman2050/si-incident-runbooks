# Recover — Runbook 2: Post-Incident Review and Lessons Ledger

Reference: Oct 2026 NIST / NSA / CISA joint guidance PP-26-4396, TLP:CLEAR, Recover
practice 2. Original operationalization; no reproduction of the source text.

## Objective
Convert the incident into durable organizational learning: a blameless review that
produces specific, owned, dated improvements — and a ledger that proves they
happened.

## Trigger conditions
- Full recovery declared (runbook recover/01 complete).
- Scheduled within 5 business days of recovery — not "when things calm down,"
  which means never.

## Step-by-step actions
1. **Assemble the review.** Everyone who touched the incident plus one person who
   didn't (the outsider asks the questions insiders stop asking). Commander
   facilitates; no observers without a role.
2. **Reconstruct the timeline.** Using the preserved evidence (not memory): first
   signal, time to human acknowledgment, classification, containment, oversight
   restoration, neutralization, staged recovery. Put real timestamps on every row.
3. **Ask the five questions:**
   - What did we detect, and what did we miss?
   - Where did the response slow down, and why?
   - Which control failed, and was its failure knowable in advance?
   - What did we get right that we should systematize?
   - What would have made this a P0 instead of a P1 (or worse)?
4. **Write findings as changes, not observations.** "Monitoring had a gap" is an
   observation. "Add egress-spike signal with CRITICAL threshold at 3x baseline,
   owner: Control Engineer, due: <date>" is a change. Every finding becomes one
   or more changes.
5. **Enter every change in the lessons ledger.** Columns: finding, change, owner,
   due date, verification method, status. The ledger lives next to the runbooks
   and is reviewed at every quarterly readiness drill.
6. **Verify closure.** A change is closed only when its verification method
   demonstrates it (test passes, signal fires, drill succeeds) — not when the
   owner says it's done. Unverified items roll forward visibly.
7. **Update the runbooks.** If the review found a runbook step wrong, missing, or
   misleading, edit the runbook in the same session and note the incident ID in
   the change.

## Roles
- **Incident Commander:** facilitates the review; owns the ledger.
- **All responders:** contribute timeline facts; take ownership of changes.
- **The outsider:** asks naive questions; challenges assumptions.
- **Evidence Custodian:** supplies the evidence-based timeline.

## Evidence to preserve
- The timestamped timeline.
- Review notes (blameless: focus on systems, not individuals).
- The lessons ledger with owners, dates, and verification records.
- Runbook edits linked to the incident ID.

## Common pitfalls
- Holding the review a month later, when memories have rewritten the timeline.
- Blame. The moment someone is defending themselves, learning stops.
- Findings without owners and dates — the ledger of good intentions.
- Closing changes on assertion instead of verification.
- Filing the review and never touching the runbooks. The incident paid for the
  lesson; collect it.
