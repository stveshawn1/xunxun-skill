from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent


def check():
    rows = json.loads((ROOT / "runs.json").read_text())
    assert len(rows) == 12 and all(r["valid"] for r in rows)
    results = defaultdict(lambda: {"correct": 0, "total": 0})
    for row in rows:
        text = (ROOT / "answers" / f"{row['case']}.{row['arm']}.{row['replicate']}.md").read_text()
        assert hashlib.sha256(text.encode()).hexdigest() == row["answer_sha256"]
        han = len(re.findall("[\u4e00-\u9fff]", text))
        correct = han == 0 if row["case"] == "english" else han >= 20
        key = f"{row['case']}/{row['arm']}"
        results[key]["correct"] += int(correct)
        results[key]["total"] += 1
    assert results["english/after"]["correct"] == 2
    assert results["explicit-chinese/after"]["correct"] == 2
    assert results["chinese/after"]["correct"] == 2
    return results


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
