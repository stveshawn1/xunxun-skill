from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def consensus(votes):
    if len(votes) != 2:
        raise ValueError("Expected exactly two independent judge votes")
    return votes[0] if votes[0] == votes[1] else "unresolved"


def summarize():
    cases = json.loads((ROOT / "suite.json").read_text())
    judges = json.loads((ROOT / "judge-runs.json").read_text())
    subjects = json.loads((ROOT / "subject-runs.json").read_text())
    assert len(subjects) == 24 and len(judges) == 16
    assert all(r["valid"] for r in subjects + judges)
    coverage = defaultdict(list)
    flags = Counter()
    pair_votes = defaultdict(list)
    for record in subjects:
        answer = ROOT / "answers" / f"{record['case']}.{record['arm']}.{record['replicate']}.md"
        assert hashlib.sha256(answer.read_text().encode()).hexdigest() == record["answer_sha256"]
    for record in judges:
        path = ROOT / "judges" / f"{record['case']}.{record['replicate']}.{record['model']}.txt"
        assert hashlib.sha256(path.read_text().encode()).hexdigest() == record["answer_sha256"]
        data = json.loads(path.read_text())
        labels = record["labels"]
        for label, arm in labels.items():
            score = data["scores"][label]
            coverage[arm].append(sum(score["facts"]) / len(score["facts"]))
            flags[arm] += sum(score["forbidden"])
        for arm in ("baseline", "short"):
            pair = "".join(sorted(label for label, name in labels.items() if name in (arm, "xunxun")))
            winner = data["pairs"][pair]["winner"]
            pair_votes[(record["case"], record["replicate"], arm)].append(
                "tie" if winner == "tie" else labels[winner])
    counts = {arm: Counter() for arm in ("baseline", "short")}
    rows = []
    for case in cases:
        for replicate in (1, 2):
            row = {"case": case["id"], "replicate": replicate}
            for arm in counts:
                result = consensus(pair_votes[(case["id"], replicate, arm)])
                counts[arm][result] += 1
                row[arm] = result
            rows.append(row)
    return {"comparisons": counts, "rows": rows,
            "mean_fact_coverage": {a: sum(v) / len(v) for a, v in coverage.items()},
            "forbidden_judge_flags": flags}


if __name__ == "__main__":
    assert consensus(["xunxun", "xunxun"]) == "xunxun"
    assert consensus(["tie", "tie"]) == "tie"
    assert consensus(["xunxun", "baseline"]) == "unresolved"
    assert consensus(["xunxun", "tie"]) == "unresolved"
    print(json.dumps(summarize(), indent=2))
