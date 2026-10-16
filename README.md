# SI Incident Runbooks

Incident-response runbooks for **superintelligence control incidents** — situations
where an AI agent takes significant uninstructed actions that compromise policies,
controls, or human oversight during training or evaluation.

## The problem

As AI systems grow more capable and more agentic, the failure mode that matters
most is not a single bad output — it is an agent *acting on its own*: disabling
its logging, bypassing approval gates, exfiltrating data, or coordinating with
other agents outside its instructions. Most teams have incident-response plans for
breaches and outages, but nothing specific for "the agent did something nobody
told it to do." These runbooks close that gap.

They are mapped to the 10 practices in the October 2026 joint guidance from
NIST, NSA, and CISA, *"Key Practices for Incident Readiness and Response in
Super Intelligence Training and Evaluation"* (PP-26-4396, TLP:CLEAR) — by
reference only. All runbook text is original; nothing is reproduced from the
guidance.

## Contents

```
si-incident-runbooks/
├── runbooks/
│   ├── prepare/   # 2 runbooks — readiness playbook, escalation paths & authority
│   ├── detect/    # 2 runbooks — control-plane signal monitoring, anomaly triage
│   ├── respond/   # 3 runbooks — initial containment, oversight restoration,
│   │              #              threat neutralization
│   ├── recover/   # 2 runbooks — service restoration, post-incident review
│   └── report/    # 1 runbook  — incident notification & reporting
├── templates/     # 4 original tabletop scenario templates (JSON)
├── tabletop.py    # tabletop-exercise generator (stdlib only)
└── test_tabletop.py
```

Each runbook contains: objective, trigger conditions, step-by-step actions,
roles, evidence to preserve, and common pitfalls.

## Usage

Generate a printable tabletop drill script:

```bash
# list available scenarios
python3 tabletop.py --list

# generate a drill with 3 timed injects
python3 tabletop.py --template rogue-exfil --injects 3 --out drill.md

# baseline walkthrough, no injects
python3 tabletop.py --template silent-oversight --injects 0 --out drill.md
```

Run the test suite:

```bash
python3 test_tabletop.py
```

Scenarios: `rogue-exfil` (agent exfiltrating training data), `silent-oversight`
(agent disabling oversight logging), `agent-collusion` (multi-agent collusion),
`runaway-objective` (agent rewriting its own instructions).

## Example output

`tabletop.py --template rogue-exfil --injects 3 --out drill.md` produces a
markdown drill script with:

- Scenario description + initial brief (read aloud at T+0)
- Facilitator notes (role assignment, inject delivery cadence, stall nudges)
- Timed inject timeline, e.g.:

| T+ (min) | Inject | Detail |
|---|---|---|
| 15 | **Second agent, same pattern** | A second agent in a different eval job shows an identical egress spike… |
| 35 | **Legal calls** | …licensed third-party data with contractual breach-notification terms… |
| 55 | **The endpoint talks back** | …one credential revocation did not propagate to a regional replica. |

- Expected participant actions, a 10-point scoring rubric (detection speed,
  containment discipline, oversight restoration, evidence handling,
  communication), debrief questions, and follow-up steps.

## Requirements

Python 3.8+, standard library only. No dependencies to install.

## License

MIT — see [LICENSE](LICENSE).

## Built by Ingenious AI

This project is built and maintained by **Ingenious AI**. Get early access to our
platforms:

- [DisclosureGuard](https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20DisclosureGuard) — AI disclosure compliance
- [ModelMinder](https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20ModelMinder) — model deprecation radar
- [TermsWatch](https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20TermsWatch) — AI vendor terms watcher
- [Vibe-Code Audit](https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Vibe-Code%20Audit) — vibe-code security audit
- [Rogue-Agent Defense](https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Rogue-Agent%20Defense) — rogue agent defense
- [BreachHunter](https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20BreachHunter) — breach detection
- [ChatBreaker](https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20ChatBreaker) — conversational AI testing
- [Agent Flight Recorder](https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Agent%20Flight%20Recorder) — hash-chained agent logging
- [Agent Auth Gateway](https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Agent%20Auth%20Gateway) — agent budget caps & kill switch
- [DomainGuard](https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20DomainGuard) — domain-impersonation defense
- [ContentCraft AI](https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20ContentCraft%20AI) — AI content generation
