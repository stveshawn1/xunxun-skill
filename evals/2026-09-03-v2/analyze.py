#!/usr/bin/env python3
"""Validate judgments and compute preregistered pilot/full v2 outcomes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from grade import mapping


ROOT = Path(__file__).parent
DIMENSIONS = ("intuition", "boundary", "mechanism", "novice_relevance")


def score(value: dict, fact_count: int) -> float:
    raw = 2 * sum(value["facts"]) - 2 * sum(value["forbidden"]) + sum(value[key] for key in DIMENSIONS)
    return raw / (2 * fact_count + 8)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--set", choices=("pilot", "full"), default="pilot")
    args = parser.parse_args()
    suite = json.loads((ROOT / "suite.json").read_text())
    selected = set(suite["pilot_ids"]) if args.set == "pilot" else {item["id"] for item in suite["items"]}
    items = [item for item in suite["items"] if item["id"] in selected]
    deltas: list[float] = []
    preferences: list[str] = []
    baseline_scores: list[float] = []
    vectors: list[tuple] = []
    baseline_chars = xunxun_chars = 0
    factual_by_domain: dict[str, list[float]] = {}

    for item in items:
        judgments = [json.loads((ROOT / "judgments" / judge / f"{item['id']}.json").read_text()) for judge in ("sol", "terra")]
        for replicate in range(1, 4):
            condition_scores = {"baseline": [], "xunxun": []}
            condition_facts = {"baseline": [], "xunxun": []}
            preferred_conditions = []
            a_condition, b_condition = mapping(item["id"], replicate)
            for judgment in judgments:
                row = next(value for value in judgment["replicates"] if value["replicate"] == replicate)
                for label, condition in (("a", a_condition), ("b", b_condition)):
                    value = row[label]
                    assert len(value["facts"]) == len(item["facts"]), f"fact length: {item['id']}"
                    assert len(value["forbidden"]) == len(item["forbidden"]), f"forbidden length: {item['id']}"
                    condition_scores[condition].append(score(value, len(item["facts"])))
                    condition_facts[condition].append(sum(value["facts"]) / len(item["facts"]))
                    vectors.append(tuple(value[key] for key in DIMENSIONS))
                if row["preferred"] == "tie":
                    preferred_conditions.append("tie")
                else:
                    preferred_conditions.append(a_condition if row["preferred"] == "A" else b_condition)

            baseline = sum(condition_scores["baseline"]) / 2
            xunxun = sum(condition_scores["xunxun"]) / 2
            baseline_scores.append(baseline)
            deltas.append(xunxun - baseline)
            if preferred_conditions[0] == preferred_conditions[1]:
                preferences.append(preferred_conditions[0])
            elif "tie" in preferred_conditions:
                preferences.append(next(value for value in preferred_conditions if value != "tie"))
            else:
                preferences.append("tie")
            factual_by_domain.setdefault(item["domain"], []).append(
                sum(condition_facts["xunxun"]) / 2 - sum(condition_facts["baseline"]) / 2
            )
            baseline_chars += len((ROOT / "results" / item["id"] / "baseline" / f"r{replicate}.md").read_text())
            xunxun_chars += len((ROOT / "results" / item["id"] / "xunxun" / f"r{replicate}.md").read_text())

    run_files = [ROOT / "runs-pilot.json"] if args.set == "pilot" else [ROOT / "runs-pilot.json", ROOT / "runs-remaining.json"]
    records = [record for path in run_files for record in json.loads(path.read_text())["records"]]
    assert all(record["valid"] for record in records)
    treatment = [record for record in records if record["condition"] == "xunxun"]
    trigger_rate = sum(record["triggered"] for record in treatment) / len(treatment)
    input_tokens = {
        condition: sum(record["usage"].get("input_tokens", 0) for record in records if record["condition"] == condition)
        for condition in ("baseline", "xunxun")
    }
    non_ties = preferences.count("baseline") + preferences.count("xunxun")
    xunxun_preference_rate = preferences.count("xunxun") / non_ties if non_ties else 0.0
    max_vector = (2, 2, 2, 2)
    pilot_gate = (
        sum(value >= 0.9 for value in baseline_scores) / len(baseline_scores) < 0.8
        and len(set(vectors)) > 1
        and vectors.count(max_vector) / len(vectors) < 0.8
    )
    domain_fact_deltas = {domain: sum(values) / len(values) for domain, values in factual_by_domain.items()}
    summary = {
        "set": args.set,
        "pairs": len(deltas),
        "mean_normalized_delta": sum(deltas) / len(deltas),
        "preferences": {condition: preferences.count(condition) for condition in ("xunxun", "baseline", "tie")},
        "xunxun_preference_rate_non_ties": xunxun_preference_rate,
        "trigger_rate": trigger_rate,
        "character_ratio": xunxun_chars / baseline_chars,
        "input_token_ratio": input_tokens["xunxun"] / input_tokens["baseline"],
        "domain_fact_deltas": domain_fact_deltas,
        "pilot_gate": pilot_gate,
    }
    if args.set == "full":
        summary["supports_general_one_turn_value"] = (
            summary["mean_normalized_delta"] >= 0.03
            and summary["xunxun_preference_rate_non_ties"] >= 0.55
            and min(domain_fact_deltas.values()) >= -0.05
            and summary["character_ratio"] <= 1.5
            and trigger_rate >= 0.8
        )
    output = ROOT / f"analysis-{args.set}.json"
    output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(output.read_text(), end="")
    if args.set == "pilot" and not pilot_gate:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
