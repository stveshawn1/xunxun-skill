#!/usr/bin/env python3
"""Verify immutable inputs and recompute the preregistered v1 decision."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).parent
DIMENSIONS = (
    "accuracy",
    "definition_boundaries",
    "mental_model_mechanism",
    "terminology_scaffolding",
    "relevance_cognitive_load",
    "transfer_readiness",
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def main() -> None:
    manifest = load_json(ROOT / "manifest.json")
    for relative, expected in manifest["sha256"].items():
        actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        assert actual == expected, f"hash mismatch: {relative}"

    judges = [load_json(ROOT / "judges" / f"{name}.json") for name in ("sol", "terra")]
    case_rows = []
    accuracy_losses = []
    baseline_chars = 0
    xunxun_chars = 0

    for case_id, mapping in manifest["cases"].items():
        deltas = []
        accuracy_deltas = []
        for judge in judges:
            case = next(item for item in judge["cases"] if item["id"] == case_id)
            for label in ("a", "b"):
                score = case[label]
                assert score["total"] == sum(score[key] for key in DIMENSIONS), (
                    f"invalid total: {case_id}/{label}"
                )
            baseline_label = "a" if mapping["a"] == "baseline" else "b"
            xunxun_label = "a" if mapping["a"] == "xunxun" else "b"
            baseline = case[baseline_label]
            xunxun = case[xunxun_label]
            deltas.append(xunxun["total"] - baseline["total"])
            accuracy_deltas.append(xunxun["accuracy"] - baseline["accuracy"])

        mean_delta = sum(deltas) / len(deltas)
        mean_accuracy_delta = sum(accuracy_deltas) / len(accuracy_deltas)
        decision = "win" if mean_delta >= 2 else "regression" if mean_delta <= -2 else "tie"
        case_rows.append({"id": case_id, "delta": mean_delta, "decision": decision})
        accuracy_losses.append(-mean_accuracy_delta)
        baseline_chars += len((ROOT / case_id / "baseline.md").read_text())
        xunxun_chars += len((ROOT / case_id / "xunxun.md").read_text())

    wins = sum(row["decision"] == "win" for row in case_rows)
    mean_delta = sum(row["delta"] for row in case_rows) / len(case_rows)
    character_ratio = xunxun_chars / baseline_chars
    thresholds = manifest["thresholds"]
    supported = (
        wins >= thresholds["minimum_wins"]
        and mean_delta >= thresholds["minimum_mean_delta"]
        and max(accuracy_losses) <= thresholds["maximum_accuracy_loss"]
        and character_ratio <= thresholds["maximum_character_ratio"]
    )

    print(json.dumps({
        "cases": case_rows,
        "wins": wins,
        "mean_delta": mean_delta,
        "character_ratio": round(character_ratio, 3),
        "supports_one_turn_value": supported,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
