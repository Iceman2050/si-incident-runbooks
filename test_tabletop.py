#!/usr/bin/env python3
"""Tests for si-incident-runbooks. Stdlib only (unittest). Run: python3 test_tabletop.py"""

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

EXPECTED_RUNBOOKS = [
    "runbooks/prepare/01-incident-readiness-playbook.md",
    "runbooks/prepare/02-escalation-paths-and-authority.md",
    "runbooks/detect/01-control-plane-signal-monitoring.md",
    "runbooks/detect/02-anomaly-classification-and-triage.md",
    "runbooks/respond/01-initial-containment.md",
    "runbooks/respond/02-oversight-restoration.md",
    "runbooks/respond/03-threat-neutralization.md",
    "runbooks/recover/01-service-restoration.md",
    "runbooks/recover/02-post-incident-review.md",
    "runbooks/report/01-incident-notification-and-reporting.md",
]

# Required sections per runbook (case-insensitive heading match).
REQUIRED_SECTIONS = ["objective", "trigger", "step", "roles"]


class TestRunbooks(unittest.TestCase):
    def test_all_runbooks_exist(self):
        missing = [r for r in EXPECTED_RUNBOOKS if not (HERE / r).exists()]
        self.assertEqual(missing, [], f"missing runbooks: {missing}")
        self.assertEqual(len(EXPECTED_RUNBOOKS), 10)

    def test_runbooks_have_required_sections(self):
        for rel in EXPECTED_RUNBOOKS:
            text = (HERE / rel).read_text(encoding="utf-8").lower()
            for section in REQUIRED_SECTIONS:
                self.assertIn(section, text,
                              f"{rel} missing section containing '{section}'")

    def test_runbooks_have_evidence_and_pitfalls(self):
        for rel in EXPECTED_RUNBOOKS:
            text = (HERE / rel).read_text(encoding="utf-8").lower()
            self.assertIn("evidence", text, f"{rel} missing evidence section")
            self.assertIn("pitfall", text, f"{rel} missing pitfalls section")

    def test_runbooks_are_original_length(self):
        for rel in EXPECTED_RUNBOOKS:
            size = (HERE / rel).stat().st_size
            self.assertGreater(size, 1500, f"{rel} suspiciously short")


def run_generator(template, injects, out):
    return subprocess.run(
        [sys.executable, str(HERE / "tabletop.py"),
         "--template", template, "--injects", str(injects),
         "--out", str(out), "--facilitator", "Test Facilitator"],
        capture_output=True, text=True)


class TestGenerator(unittest.TestCase):
    def templates(self):
        return sorted(p.stem for p in (HERE / "templates").glob("*.json"))

    def test_four_templates_present(self):
        self.assertEqual(len(self.templates()), 4)

    def test_templates_are_valid_json_with_required_keys(self):
        for name in self.templates():
            data = json.loads((HERE / "templates" / f"{name}.json").read_text())
            for key in ("id", "name", "description", "initial_brief",
                        "expected_actions", "injects", "debrief_questions"):
                self.assertIn(key, data, f"{name} missing key {key}")
            self.assertGreaterEqual(len(data["injects"]), 1)

    def test_generator_produces_markdown_for_every_template(self):
        for name in self.templates():
            with tempfile.TemporaryDirectory() as td:
                out = Path(td) / "drill.md"
                proc = run_generator(name, 3, out)
                self.assertEqual(proc.returncode, 0,
                                 f"{name}: {proc.stderr}")
                text = out.read_text(encoding="utf-8")
                self.assertTrue(text.startswith("# Tabletop Drill:"),
                                f"{name}: missing title heading")
                self.assertIn("## 6. Scoring Rubric", text,
                              f"{name}: missing rubric")

    def test_inject_count_respected(self):
        name = self.templates()[0]
        total = len(json.loads(
            (HERE / "templates" / f"{name}.json").read_text())["injects"])
        for requested in (0, 2, 99):
            with tempfile.TemporaryDirectory() as td:
                out = Path(td) / "drill.md"
                proc = run_generator(name, requested, out)
                self.assertEqual(proc.returncode, 0)
                text = out.read_text(encoding="utf-8")
                section = text.split("## 4. Inject Timeline")[1].split("## 5.")[0]
                rows = re.findall(r"^\| \d+ \|", section, re.M)
                self.assertEqual(len(rows), min(requested, total),
                                 f"requested={requested}, got {len(rows)}")

    def test_rubric_and_actions_present(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "drill.md"
            proc = run_generator("rogue-exfil", 3, out)
            self.assertEqual(proc.returncode, 0)
            text = out.read_text(encoding="utf-8")
            self.assertIn("Scoring Rubric", text)
            self.assertIn("Maximum: 10 points", text)
            self.assertIn("Expected Participant Actions", text)
            self.assertIn("Debrief Questions", text)
            self.assertIn("Test Facilitator", text)

    def test_unknown_template_fails(self):
        with tempfile.TemporaryDirectory() as td:
            proc = run_generator("no-such-template", 3, Path(td) / "d.md")
            self.assertNotEqual(proc.returncode, 0)

    def test_list_flag(self):
        proc = subprocess.run(
            [sys.executable, str(HERE / "tabletop.py"), "--list"],
            capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0)
        self.assertEqual(len(proc.stdout.strip().splitlines()), 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
