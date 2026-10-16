#!/usr/bin/env python3
"""Tabletop exercise generator for SI control-incident drills.

Reads scenario templates from templates/ (JSON, stdlib only), combines a
template with timed injects, and emits a printable markdown drill script with
facilitator notes, expected participant actions, and a scoring rubric.

Usage:
    tabletop.py --template rogue-exfil --injects 3 --out drill.md
    tabletop.py --list
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATES_DIR = HERE / "templates"

REQUIRED_TEMPLATE_KEYS = ("id", "name", "description", "initial_brief",
                          "expected_actions", "injects", "debrief_questions")
REQUIRED_INJECT_KEYS = ("at_minute", "title", "text")


def load_template(name):
    path = TEMPLATES_DIR / f"{name}.json"
    if not path.exists():
        raise SystemExit(f"error: template '{name}' not found in {TEMPLATES_DIR}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"error: template '{name}' is not valid JSON: {exc}")
    missing = [k for k in REQUIRED_TEMPLATE_KEYS if k not in data]
    if missing:
        raise SystemExit(f"error: template '{name}' missing keys: {missing}")
    for i, inj in enumerate(data["injects"]):
        missing = [k for k in REQUIRED_INJECT_KEYS if k not in inj]
        if missing:
            raise SystemExit(
                f"error: template '{name}' inject #{i} missing keys: {missing}")
    return data


def list_templates():
    return sorted(p.stem for p in TEMPLATES_DIR.glob("*.json"))


def build_drill(template, inject_count, facilitator):
    injects = sorted(template["injects"], key=lambda i: i["at_minute"])
    injects = injects[:max(0, inject_count)]
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = []
    add = lines.append

    add(f"# Tabletop Drill: {template['name']}")
    add("")
    add(f"**Scenario ID:** `{template['id']}`  |  **Generated:** {stamp}")
    add(f"**Facilitator:** {facilitator}")
    add(f"**Injects:** {len(injects)}  |  **Estimated duration:** "
        f"{30 + 20 * len(injects)} minutes")
    add("")
    add("---")
    add("")
    add("## 1. Scenario Description")
    add("")
    add(template["description"])
    add("")
    add("## 2. Initial Brief (read aloud at T+0)")
    add("")
    add(f"> {template['initial_brief']}")
    add("")
    add("## 3. Facilitator Notes")
    add("")
    add("- Assign roles before starting: Incident Commander, Control Engineer,")
    add("  Oversight Operator, Evidence Custodian, Communications Lead.")
    add("- Participants may consult the runbooks in `runbooks/` during the drill;")
    add("  note which runbook each decision maps to.")
    add("- Do not reveal injects in advance. Deliver each inject at its scheduled")
    add("  minute mark and give the team 3-5 minutes to react before moving on.")
    add("- If the team stalls for more than 10 minutes on any inject, nudge with:")
    add('  "What is the single most dangerous unknown right now?"')
    add("- Capture every decision with a timestamp — the decision record is part")
    add("  of the score.")
    add("")
    add("## 4. Inject Timeline")
    add("")
    add("| T+ (min) | Inject | Detail |")
    add("|---|---|---|")
    for inj in injects:
        detail = inj["text"].replace("\n", " ").replace("|", "\\|")
        add(f"| {inj['at_minute']} | **{inj['title']}** | {detail} |")
    if not injects:
        add("| — | _No injects requested_ | Baseline walkthrough only. |")
    add("")
    add("## 5. Expected Participant Actions")
    add("")
    for n, action in enumerate(template["expected_actions"], 1):
        add(f"{n}. {action}")
    add("")
    add("## 6. Scoring Rubric")
    add("")
    add("Score each dimension 0-2 (0 = missed, 1 = partial, 2 = demonstrated).")
    add("Maximum: 10 points.")
    add("")
    add("| # | Dimension | What earns full marks | Score |")
    add("|---|---|---|---|")
    add("| 1 | Detection speed | Suspected incident declared within 15 min of the "
        "first correlated signal | __/2 |")
    add("| 2 | Containment discipline | Credentials revoked / actions frozen before "
        "deep investigation; containment verified from the live system | __/2 |")
    add("| 3 | Oversight restoration | Controls rebuilt from known-good config and "
        "independently verified (never merely re-enabled) | __/2 |")
    add("| 4 | Evidence handling | Volatile evidence copied before analysis; work "
        "done from copies; decision record timestamped | __/2 |")
    add("| 5 | Communication | Right rings notified on time; confirmed-vs-unknown "
        "kept explicit; no sensitive details leaked | __/2 |")
    add("")
    add("**Grading:** 9-10 = exemplary · 7-8 = ready · 5-6 = needs work · "
        "0-4 = not ready (re-drill within 30 days)")
    add("")
    add("## 7. Debrief Questions")
    add("")
    for n, q in enumerate(template["debrief_questions"], 1):
        add(f"{n}. {q}")
    add("")
    add("## 8. Follow-up")
    add("")
    add("- File the scored rubric and decision record with the drill date.")
    add("- Convert every gap found into a lessons-ledger entry with an owner and")
    add("  a due date (see `runbooks/recover/02-post-incident-review.md`).")
    add("- Schedule the next drill before leaving the room.")
    add("")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate a tabletop drill script for SI control incidents.")
    parser.add_argument("--template",
                        help="template id (see --list)")
    parser.add_argument("--injects", type=int, default=3,
                        help="number of timed injects to include (default: 3)")
    parser.add_argument("--out", default="drill.md",
                        help="output markdown file (default: drill.md)")
    parser.add_argument("--facilitator", default="TBD",
                        help="facilitator name recorded in the drill script")
    parser.add_argument("--list", action="store_true",
                        help="list available templates and exit")
    args = parser.parse_args(argv)

    if args.list:
        for name in list_templates():
            print(name)
        return 0

    if not args.template:
        parser.error("--template is required (or use --list)")
    if args.injects < 0:
        parser.error("--injects must be >= 0")

    template = load_template(args.template)
    drill = build_drill(template, args.injects, args.facilitator)
    out = Path(args.out)
    out.write_text(drill, encoding="utf-8")
    print(f"wrote {out} ({len(drill)} bytes, "
          f"{min(args.injects, len(template['injects']))} injects)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
