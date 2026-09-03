#!/usr/bin/env python3
"""Verify v2.3 evidence integrity, isolation, counts, and final decision."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).parent
REPO = ROOT.parents[1]


def artifact_files() -> list[Path]:
    files = [
        REPO / "SKILL.md",
        ROOT / "suite.json",
        ROOT / "judge-schema.json",
        ROOT / "run.py",
        ROOT / "grade.py",
        ROOT / "analyze.py",
        ROOT / "report.md",
        ROOT / "runs-pilot.json",
        ROOT / "runs-remaining.json",
        ROOT / "judge-runs-pilot.json",
        ROOT / "judge-runs-remaining.json",
        ROOT / "analysis-pilot.json",
        ROOT / "analysis-full.json",
        *ROOT.glob("protocol*.md"),
        *ROOT.glob("sources/*.md"),
        *ROOT.glob("results/*/*/r*.md"),
        *ROOT.glob("judgments/*/*.json"),
    ]
    return sorted(set(files), key=lambda path: str(path))


def artifact_root() -> str:
    digest = hashlib.sha256()
    for path in artifact_files():
        relative = path.relative_to(REPO)
        digest.update(str(relative).encode())
        digest.update(b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).hexdigest().encode())
        digest.update(b"\n")
    return digest.hexdigest()


def main() -> None:
    manifest = json.loads((ROOT / "manifest.json").read_text())
    assert artifact_root() == manifest["artifact_root_sha256"], "artifact root mismatch"
    suite = json.loads((ROOT / "suite.json").read_text())
    assert len(suite["items"]) == 15 and len(suite["pilot_ids"]) == 5
    assert len(list(ROOT.glob("results/*/*/r*.md"))) == 90
    assert len(list(ROOT.glob("judgments/*/*.json"))) == 45

    records = []
    for name, expected in (("pilot", 30), ("remaining", 60)):
        run = json.loads((ROOT / f"runs-{name}.json").read_text())
        assert len(run["records"]) == expected and not run["invalid_pairs"]
        records.extend(run["records"])
    assert all(row["valid"] and not row["unexpected_skill_reads"] for row in records)
    treatment = [row for row in records if row["condition"] == "xunxun"]
    baseline = [row for row in records if row["condition"] == "baseline"]
    assert len(treatment) == len(baseline) == 45
    assert all(row["triggered"] for row in treatment)
    assert not any(row["triggered"] for row in baseline)

    analysis = json.loads((ROOT / "analysis-full.json").read_text())
    for key, expected in manifest["expected_analysis"].items():
        actual = analysis[key]
        if isinstance(expected, float):
            assert abs(actual - expected) < 1e-12, f"analysis mismatch: {key}"
        else:
            assert actual == expected, f"analysis mismatch: {key}"

    forbidden = ("/Users/", "shaolingyun", "01a0", "BEGIN PRIVATE KEY", "sk-")
    for path in artifact_files():
        if path.suffix not in {".md", ".json", ".py"}:
            continue
        text = path.read_text(errors="replace")
        assert not any(value in text for value in forbidden), f"private marker: {path}"

    print(json.dumps({
        "artifact_root_sha256": manifest["artifact_root_sha256"],
        "items": 15,
        "answers": 90,
        "judgments": 45,
        "isolated_pairs": 45,
        "analysis": analysis,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
