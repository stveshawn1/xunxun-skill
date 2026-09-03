#!/usr/bin/env python3
"""Run isolated, replicated Baseline/Xunxun pairs for the v2 suite."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).parent
REPO = ROOT.parents[1]
SKILL = REPO / "SKILL.md"
OPENAI_DOCS = SKILL.parent.parent / ".system" / "openai-docs" / "SKILL.md"


def config(disabled: list[Path]) -> str:
    rows = ",".join(f'{{path={json.dumps(str(path))},enabled=false}}' for path in disabled if path.exists())
    return f"skills.config=[{rows}]"


def parse_trace(text: str) -> tuple[dict, list[str]]:
    usage: dict = {}
    skill_reads: list[str] = []
    for line in text.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "turn.completed":
            usage = event.get("usage", {})
        item = event.get("item", {})
        if item.get("type") == "command_execution" and "SKILL.md" in item.get("command", ""):
            skill_reads.append(item["command"])
    return usage, skill_reads


def sanitize(command: str) -> str:
    return command.replace(str(SKILL), "<xunxun-skill>/SKILL.md").replace(
        str(OPENAI_DOCS), "<openai-docs-skill>/SKILL.md"
    )


def run_one(item: dict, condition: str, replicate: int, workdir: Path, neutral: Path, model: str, effort: str) -> dict:
    output_dir = ROOT / "results" / item["id"] / condition
    output_dir.mkdir(parents=True, exist_ok=True)
    answer = output_dir / f"r{replicate}.md"
    trace = ROOT / ".traces" / item["id"] / condition / f"r{replicate}.jsonl"
    trace.parent.mkdir(parents=True, exist_ok=True)

    disabled = [OPENAI_DOCS]
    if condition == "baseline":
        disabled.append(SKILL)

    command = [
        "codex", "exec", "--ephemeral", "--ignore-user-config", "--ignore-rules",
        "--skip-git-repo-check", "-s", "read-only", "-m", model,
        "-c", f'model_reasoning_effort="{effort}"', "-c", config(disabled),
        "--color", "never", "--json", "-o", str(answer), "-",
    ]
    environment = dict(os.environ)
    environment["XUNXUN_HOME"] = str(neutral)
    completed = subprocess.run(
        command,
        cwd=workdir,
        env=environment,
        input=item["prompt"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=420,
        check=False,
    )
    trace.write_text(completed.stdout)
    usage, skill_reads = parse_trace(completed.stdout)
    allowed = [] if condition == "baseline" else [str(SKILL)]
    unexpected = [read for read in skill_reads if not any(path in read for path in allowed)]
    valid = completed.returncode == 0 and answer.is_file() and answer.stat().st_size > 0 and not unexpected
    return {
        "item": item["id"],
        "condition": condition,
        "replicate": replicate,
        "returncode": completed.returncode,
        "valid": valid,
        "usage": usage,
        "triggered": any(str(SKILL) in read for read in skill_reads),
        "skill_reads": [sanitize(read) for read in skill_reads],
        "unexpected_skill_reads": [sanitize(read) for read in unexpected],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--set", choices=("pilot", "remaining", "full"), default="pilot")
    parser.add_argument("--replicates", type=int, default=3)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument("--effort", default="medium")
    args = parser.parse_args()
    if args.replicates < 1 or args.workers < 2:
        parser.error("replicates must be positive and workers must be at least 2")

    suite = json.loads((ROOT / "suite.json").read_text())
    pilot = set(suite["pilot_ids"])
    selected = pilot if args.set == "pilot" else (
        {item["id"] for item in suite["items"]} - pilot if args.set == "remaining"
        else {item["id"] for item in suite["items"]}
    )
    items = [item for item in suite["items"] if item["id"] in selected]

    with tempfile.TemporaryDirectory(prefix="xunxun-v2-") as temporary:
        temp = Path(temporary)
        neutral = temp / "neutral-state"
        neutral.mkdir()
        (neutral / "profile.md").write_text("")
        workdirs: dict[str, Path] = {}
        for item in items:
            workdir = temp / "work" / item["id"]
            workdir.mkdir(parents=True)
            shutil.copyfile(ROOT / "sources" / item["source"], workdir / "source.md")
            workdirs[item["id"]] = workdir

        tasks = []
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            for item in items:
                for replicate in range(1, args.replicates + 1):
                    for condition in ("baseline", "xunxun"):
                        tasks.append(executor.submit(
                            run_one, item, condition, replicate, workdirs[item["id"]], neutral, args.model, args.effort,
                        ))
            records = [future.result() for future in as_completed(tasks)]

    records.sort(key=lambda row: (row["item"], row["replicate"], row["condition"]))
    invalid_pairs = sorted({
        (record["item"], record["replicate"])
        for record in records if not record["valid"]
    })
    metadata = {
        "set": args.set,
        "model": args.model,
        "effort": args.effort,
        "replicates": args.replicates,
        "workers": args.workers,
        "invalid_pairs": [{"item": item, "replicate": replicate} for item, replicate in invalid_pairs],
        "records": records,
    }
    (ROOT / f"runs-{args.set}.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
    invalid = [record for record in records if not record["valid"]]
    print(json.dumps({"runs": len(records), "invalid": len(invalid), "invalid_pairs": len(invalid_pairs)}, indent=2))
    raise SystemExit(1 if invalid else 0)


if __name__ == "__main__":
    main()
