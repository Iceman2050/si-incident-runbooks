# Report — Runbook 1: Incident Notification and Reporting

Reference: Oct 2026 NIST / NSA / CISA joint guidance PP-26-4396, TLP:CLEAR, Report
practice 1. Original operationalization; no reproduction of the source text.

## Objective
Notify the right parties — internal leadership, affected stakeholders, and any
authorities with a reporting expectation — with accurate, appropriately scoped
information, on time, without leaking sensitive details.

## Trigger conditions
- P0 classification (report runbook activates immediately, in parallel with
  response — reporting is not a post-recovery activity).
- P1 classification where the blast radius is still unknown after 2 hours.
- Any incident involving exfiltrated data, affected third parties, or
  safety-relevant agent behavior, regardless of classification.

## Step-by-step actions
1. **Determine who must be told.** Three rings:
   - **Ring 1 (immediate):** executive sponsor, legal, security leadership. P0 →
     notify within 1 hour of classification.
   - **Ring 2 (same day):** affected internal teams, affected customers/partners
     if their data or systems were touched.
   - **Ring 3 (as required):** external authorities or sector bodies where a
     reporting expectation or obligation exists. Legal determines the list; the
     Communications Lead executes.
2. **Write the notification from evidence, not adjectives.** Each notification
   states: what happened (facts), when (timestamps), what is affected (scope as
   currently known), what is being done (response status), what the recipient
   should do (if anything). Mark clearly what is confirmed vs. under
   investigation.
3. **Scope information to the recipient.** Ring 1 gets the full working picture.
   Ring 2 gets what affects them plus the action requested of them. Ring 3 gets
   exactly what the reporting expectation requires — no more. Never paste the
   internal incident channel into an external notification.
4. **Protect sensitive details.** Incident reports must not include: credentials
   or secrets, model weights or proprietary training details beyond what the
   obligation requires, or personal data of individuals beyond the minimum
   necessary. The Evidence Custodian reviews every external notification before
   it leaves.
5. **Track acknowledgments.** Record who was notified, when, through which
   channel, and when they acknowledged. An unacknowledged Ring 1 notification
   escalates per the authority matrix timers.
6. **Issue updates on a cadence.** P0: updates every 4 hours until contained,
   then daily until closed. Each update re-states the confirmed-vs-investigating
   boundary so earlier uncertainty isn't mistaken for current fact.
7. **File the final report.** Within 10 business days of closure: full timeline,
   root cause, impact assessment, changes made (link the lessons ledger). This
   is the document future reporting obligations and audits will reference.

## Roles
- **Communications Lead:** drafts and sends notifications; tracks acknowledgments.
- **Incident Commander:** approves content and cadence.
- **Legal (or designated advisor):** determines Ring 3 obligations; reviews
  external text.
- **Evidence Custodian:** reviews notifications for sensitive-detail leakage.

## Evidence to preserve
- Every notification sent (full text, recipient list, timestamp, channel).
- Acknowledgment records.
- The confirmed-vs-investigating boundary as stated in each update.
- The final report, versioned.

## Common pitfalls
- Reporting only after recovery. By then the obligation clock has usually
  expired and stakeholders have heard it secondhand.
- Mixing confirmed facts with working hypotheses in one paragraph. Recipients
  act on the scariest sentence.
- Over-sharing externally to appear transparent — including details that create
  legal exposure or help nobody.
- No acknowledgment tracking. "We sent the email" is not "they know."
- Letting the final report slide. The incident isn't closed until the report
  is filed.
