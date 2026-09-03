#!/usr/bin/env python3
"""Blind and grade v2 paired outputs with two independent model runs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).parent
REPO = ROOT.parents[1]
SKILL = REPO / "SKILL.md"
OPENAI_DOCS = SKILL.parent.parent / ".system" / "openai-docs" / "SKILL.md"
SKILL_COMMIT = "d49f0e9"


def mapping(item_id: str, replicate: int) -> tuple[str, str]:
    first = hashlib.sha256(f"{SKILL_COMMIT}:{item_id}:{replicate}".encode()).hexdigest()[0]
    return ("xunxun", "baseline") if int(first, 16) % 2 else ("baseline", "xunxun")


def prompt_for(item: dict) -> str:
    sections = [
        "You are a blinded evaluator. Use only the supplied source and checklist. Do not use tools or guess which condition produced an answer.",
        "For each A/B answer, return one boolean per required fact and forbidden inference. Then compare A/B directly on whether it resolves the expressed confusion, preserves the conceptual boundary, supports transfer to a new example, and does so with lower cognitive cost. Give an overall A/B/tie choice. Use tie freely; fluency or extra length alone is not an advantage. Return only schema-valid JSON.",
        f"ITEM: {item['id']}",
        f"NATURAL USER QUESTION:\n{item['prompt']}",
        f"SOURCE:\n{(ROOT / 'sources' / item['source']).read_text()}",
        "REQUIRED FACTS:\n" + "\n".join(f"{index + 1}. {fact}" for index, fact in enumerate(item["facts"])),
        "FORBIDDEN INFERENCES:\n" + "\n".join(f"{index + 1}. {fact}" for index, fact in enumerate(item["forbidden"])),
    ]
    for replicate in range(1, 4):
        a, b = mapping(item["id"], replicate)
        sections.extend([
            f"REPLICATE {replicate} — ANSWER A:\n{(ROOT / 'results' / item['id'] / a / f'r{replicate}.md').read_text()}",
            f"REPLICATE {replicate} — ANSWER B:\n{(ROOT / 'results' / item['id'] / b / f'r{replicate}.md').read_text()}",
        ])
    return "\n\n=====\n\n".join(sections)


def run_judge(item: dict, judge: str, model: str) -> dict:
    output = ROOT / "judgments" / judge / f"{item['id']}.json"
    trace = ROOT / ".traces" / "judges" / judge / f"{item['id']}.jsonl"
    output.parent.mkdir(parents=True, exist_ok=True)
    trace.parent.mkdir(parents=True, exist_ok=True)
    if output.is_file():
        try:
            existing = json.loads(output.read_text())
            if len(existing["replicates"]) == 3:
                return {"item": item["id"], "judge": judge, "model": model, "returncode": 0, "valid": True, "reused": True}
        except (json.JSONDecodeError, KeyError, TypeError):
            pass
    disabled = f'skills.config=[{{path={json.dumps(str(SKILL))},enabled=false}},{{path={json.dumps(str(OPENAI_DOCS))},enabled=false}}]'
    command = [
        "codex", "exec", "--ephemeral", "--ignore-user-config", "--ignore-rules",
        "--skip-git-repo-check", "-s", "read-only", "-m", model,
        "-c", 'model_reasoning_effort="high"', "-c", disabled,
        "--color", "never", "--json", "--output-schema", str(ROOT / "judge-schema.json"),
        "-o", str(output), "-",
    ]
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=os.environ,
        input=prompt_for(item),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=420,
        check=False,
    )
    trace.write_text(completed.stdout)
    valid = completed.returncode == 0 and output.is_file()
    if valid:
        try:
            result = json.loads(output.read_text())
            valid = len(result["replicates"]) == 3
        except (json.JSONDecodeError, KeyError, TypeError):
            valid = False
    return {"item": item["id"], "judge": judge, "model": model, "returncode": completed.returncode, "valid": valid, "reused": False}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--set", choices=("pilot", "remaining", "full"), default="pilot")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    suite = json.loads((ROOT / "suite.json").read_text())
    pilot = set(suite["pilot_ids"])
    selected = pilot if args.set == "pilot" else (
        {item["id"] for item in suite["items"]} - pilot if args.set == "remaining"
        else {item["id"] for item in suite["items"]}
    )
    items = [item for item in suite["items"] if item["id"] in selected]
    judges = {"sol": "gpt-5.6-sol", "terra": "gpt-5.6-terra", "gpt55": "gpt-5.5"}
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(run_judge, item, name, model) for item in items for name, model in judges.items()]
        records = [future.result() for future in as_completed(futures)]
    records.sort(key=lambda row: (row["item"], row["judge"]))
    (ROOT / f"judge-runs-{args.set}.json").write_text(json.dumps(records, indent=2) + "\n")
    invalid = [record for record in records if not record["valid"]]
    print(json.dumps({"runs": len(records), "invalid": len(invalid)}, indent=2))
    raise SystemExit(1 if invalid else 0)


if __name__ == "__main__":
    main()
