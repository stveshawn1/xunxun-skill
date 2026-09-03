#!/usr/bin/env python3
"""Validate judgments and compute preregistered v2.1 pilot/full outcomes."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from grade import mapping


ROOT = Path(__file__).parent
DIMENSIONS = ("confusion_resolution", "boundary_precision", "transfer_support", "cognitive_efficiency")


def condition(label: str, a_condition: str, b_condition: str) -> str:
    return "tie" if label == "tie" else a_condition if label == "A" else b_condition


def combine(votes: list[str]) -> str:
    counts = {label: votes.count(label) for label in ("baseline", "xunxun", "tie")}
    winner = max(counts, key=counts.get)
    return winner if counts[winner] >= 2 else "tie"


def factual(value: dict, fact_count: int) -> float:
    return (sum(value["facts"]) - sum(value["forbidden"])) / fact_count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--set", choices=("pilot", "full"), default="pilot")
    args = parser.parse_args()
    suite = json.loads((ROOT / "suite.json").read_text())
    selected = set(suite["pilot_ids"]) if args.set == "pilot" else {item["id"] for item in suite["items"]}
    items = [item for item in suite["items"] if item["id"] in selected]

    overall_preferences: list[str] = []
    raw_dimension_labels: list[str] = []
    dimension_preferences = {name: [] for name in DIMENSIONS}
    factual_deltas: list[float] = []
    factual_by_domain: dict[str, list[float]] = {}
    baseline_complete: list[bool] = []
    judge_pair_agreements: list[bool] = []
    baseline_chars = xunxun_chars = 0

    for item in items:
        judgments = [
            json.loads((ROOT / "judgments" / judge / f"{item['id']}.json").read_text())
            for judge in ("sol", "terra", "gpt55")
        ]
        for replicate in range(1, 4):
            a_condition, b_condition = mapping(item["id"], replicate)
            scores = {"baseline": [], "xunxun": []}
            complete_votes = []
            overall_votes = []
            dimension_votes = {name: [] for name in DIMENSIONS}

            for judgment in judgments:
                row = next(value for value in judgment["replicates"] if value["replicate"] == replicate)
                for label, answer_condition in (("a", a_condition), ("b", b_condition)):
                    value = row[label]
                    assert len(value["facts"]) == len(item["facts"]), f"fact length: {item['id']}"
                    assert len(value["forbidden"]) == len(item["forbidden"]), f"forbidden length: {item['id']}"
                    scores[answer_condition].append(factual(value, len(item["facts"])))
                    if answer_condition == "baseline":
                        complete_votes.append(all(value["facts"]) and not any(value["forbidden"]))
                comparisons = row["comparisons"]
                overall_votes.append(condition(comparisons["overall"], a_condition, b_condition))
                for name in DIMENSIONS:
                    resolved = condition(comparisons[name], a_condition, b_condition)
                    dimension_votes[name].append(resolved)
                    raw_dimension_labels.append(resolved)

            baseline = sum(scores["baseline"]) / len(judgments)
            xunxun = sum(scores["xunxun"]) / len(judgments)
            delta = xunxun - baseline
            factual_deltas.append(delta)
            factual_by_domain.setdefault(item["domain"], []).append(delta)
            baseline_complete.append(all(complete_votes))
            judge_pair_agreements.extend(
                overall_votes[left] == overall_votes[right]
                for left, right in ((0, 1), (0, 2), (1, 2))
            )
            overall_preferences.append(combine(overall_votes))
            for name in DIMENSIONS:
                dimension_preferences[name].append(combine(dimension_votes[name]))

            baseline_chars += len((ROOT / "results" / item["id"] / "baseline" / f"r{replicate}.md").read_text())
            xunxun_chars += len((ROOT / "results" / item["id"] / "xunxun" / f"r{replicate}.md").read_text())

    run_files = [ROOT / "runs-pilot.json"] if args.set == "pilot" else [ROOT / "runs-pilot.json", ROOT / "runs-remaining.json"]
    records = [record for path in run_files for record in json.loads(path.read_text())["records"]]
    assert all(record["valid"] for record in records)
    treatment = [record for record in records if record["condition"] == "xunxun"]
    trigger_rate = sum(record["triggered"] for record in treatment) / len(treatment)
    input_tokens = {
        arm: sum(record["usage"].get("input_tokens", 0) for record in records if record["condition"] == arm)
        for arm in ("baseline", "xunxun")
    }
    non_ties = overall_preferences.count("baseline") + overall_preferences.count("xunxun")
    xunxun_preference_rate = overall_preferences.count("xunxun") / non_ties if non_ties else 0.0
    domain_fact_deltas = {domain: sum(values) / len(values) for domain, values in factual_by_domain.items()}
    dimension_net = {
        name: values.count("xunxun") - values.count("baseline")
        for name, values in dimension_preferences.items()
    }
    pilot_gate = (
        sum(baseline_complete) / len(baseline_complete) < 0.8
        and sum(value != "tie" for value in raw_dimension_labels) / len(raw_dimension_labels) >= 0.2
        and sum(judge_pair_agreements) / len(judge_pair_agreements) >= 0.6
    )
    summary = {
        "protocol": "v2.1",
        "set": args.set,
        "pairs": len(factual_deltas),
        "mean_factual_delta": sum(factual_deltas) / len(factual_deltas),
        "overall_preferences": {arm: overall_preferences.count(arm) for arm in ("xunxun", "baseline", "tie")},
        "xunxun_preference_rate_non_ties": xunxun_preference_rate,
        "dimension_net_preferences": dimension_net,
        "baseline_complete_rate": sum(baseline_complete) / len(baseline_complete),
        "non_tie_dimension_rate": sum(value != "tie" for value in raw_dimension_labels) / len(raw_dimension_labels),
        "judge_pairwise_overall_agreement": sum(judge_pair_agreements) / len(judge_pair_agreements),
        "trigger_rate": trigger_rate,
        "character_ratio": xunxun_chars / baseline_chars,
        "input_token_ratio": input_tokens["xunxun"] / input_tokens["baseline"],
        "domain_fact_deltas": domain_fact_deltas,
        "pilot_gate": pilot_gate,
    }
    if args.set == "full":
        summary["supports_general_one_turn_value"] = (
            xunxun_preference_rate >= 0.55
            and sum(factual_deltas) / len(factual_deltas) >= 0
            and min(domain_fact_deltas.values()) >= -0.05
            and sum(value > 0 for value in dimension_net.values()) >= 2
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
