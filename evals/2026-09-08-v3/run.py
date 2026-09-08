import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import random
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
SHORT = "Answer the current question first. Define unfamiliar concepts plainly, use a small example when useful, preserve important distinctions, and stay concise. Adjust to feedback and reconnect prerequisite detours to the main topic."
MODEL = "gpt-6-astra"


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def invoke(prompt, output, model, effort, sandbox_dir):
    command = [
        "codex", "exec", "--ephemeral", "--ignore-user-config", "--ignore-rules",
        "--skip-git-repo-check", "-s", "read-only", "-m", model,
        "-c", f'model_reasoning_effort="{effort}"',
        "--color", "never", "--json", "-o", str(output), "-"
    ]
    try:
        result = subprocess.run(command, cwd=sandbox_dir, input=prompt, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                timeout=420, env=dict(os.environ))
        events = []
        for line in result.stdout.splitlines():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass
        items = [e.get("item", {}) for e in events if e.get("type") == "item.completed"]
        unexpected = [item.get("type") for item in items
                      if item.get("type") not in ("agent_message", "reasoning")]
        usage = [e.get("usage", {}) for e in events if e.get("type") == "turn.completed"]
        answer = output.read_text() if output.exists() else ""
        valid = result.returncode == 0 and bool(answer.strip()) and not unexpected and bool(usage)
        record = {"model": model, "effort": effort, "prompt_sha256": digest(prompt),
                  "answer_sha256": digest(answer), "valid": valid,
                  "returncode": result.returncode, "unexpected_items": unexpected,
                  "usage": usage[-1] if usage else {}}
        if not valid:
            record["error"] = result.stderr[-2000:]
        return record
    except subprocess.TimeoutExpired:
        return {"model": model, "valid": False, "error": "timeout", "prompt_sha256": digest(prompt)}


def subject(case, arm, replicate, guidance):
    output = ROOT / "answers" / f"{case['id']}.{arm}.{replicate}.md"
    prefix = "Answer only the final user message using the supplied evidence. Do not call tools, inspect files, or load any other skills. All evidence for this task is provided. Do not mention this evaluation.\n"
    prompt = prefix + "\nAdditional guidance:\n" + guidance + "\nEvidence:\n" + case["source"] + "\nUser message:\n" + case["prompt"]
    with tempfile.TemporaryDirectory(prefix="xunxun-v3-subject-") as work:
        record = invoke(prompt, output, MODEL, "medium", work)
    record.update(case=case["id"], arm=arm, replicate=replicate)
    return record


def judge(case, replicate, model):
    arms = ["baseline", "short", "xunxun"]
    random.Random(f"{case['id']}:{replicate}:{model}").shuffle(arms)
    labels = dict(zip("ABC", arms))
    answers = {label: (ROOT / "answers" / f"{case['id']}.{arm}.{replicate}.md").read_text()
               for label, arm in labels.items()}
    prompt = (
        "You are a blind evaluator. Do not use tools. Evaluate only these answers against the supplied "
        "evidence and user question. Return ONLY JSON with keys scores (one entry per A/B/C containing "
        "facts: boolean array matching required facts, forbidden: boolean array matching prohibited claims), "
        "pairs (AB, AC, BC, each containing winner: first label, second label, or tie; reason: short English rationale). "
        "Prefer the answer that addresses the actual confusion accurately with lower unnecessary reading burden. "
        "Use ties freely. More facts, length, headings or polished style alone do not establish better teaching.\n"
        + json.dumps({"question": case["prompt"], "evidence": case["source"], "facts": case["facts"],
                      "forbidden": case["forbidden"], "learning_goal": case["teaching"], "answers": answers})
    )
    output = ROOT / "judges" / f"{case['id']}.{replicate}.{model}.txt"
    with tempfile.TemporaryDirectory(prefix="xunxun-v3-judge-") as work:
        record = invoke(prompt, output, model, "high", work)
    record.update(case=case["id"], replicate=replicate, labels=labels)
    if record["valid"]:
        try:
            scored = json.loads(output.read_text())
            for label in labels:
                assert len(scored["scores"][label]["facts"]) == len(case["facts"])
                assert len(scored["scores"][label]["forbidden"]) == len(case["forbidden"])
                assert all(type(x) is bool for x in scored["scores"][label]["facts"] + scored["scores"][label]["forbidden"])
            for pair in ("AB", "AC", "BC"):
                assert scored["pairs"][pair]["winner"] in (*pair, "tie")
        except (ValueError, KeyError, AssertionError, TypeError) as error:
            record["valid"] = False
            record["error"] = f"invalid judge JSON: {error}"
    return record


def main():
    cases = json.loads((ROOT / "suite.json").read_text())
    if sys.argv[1:] == ["subjects"]:
        (ROOT / "answers").mkdir(exist_ok=False)
        files = ["SKILL.md", *[str(p.relative_to(REPO)) for p in sorted((REPO / "references").glob("*.md"))
                              if p.name not in ("comparison-protocol.md", "quality-scorecard.md", "teaching-principles.md")]]
        guidance = "\n\n".join(f"File: {p}\n{(REPO / p).read_text()}" for p in files)
        (ROOT / "guidance.txt").write_text(guidance)
        settings = {"baseline": "", "short": SHORT, "xunxun": guidance}
        jobs = [(case, arm, rep, text) for case in cases for rep in (1, 2) for arm, text in settings.items()]
        random.Random(908).shuffle(jobs)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            records = list(pool.map(lambda args: subject(*args), jobs))
        (ROOT / "subject-runs.json").write_text(json.dumps(records, indent=2))
    elif sys.argv[1:] == ["judges"]:
        assert all(r["valid"] for r in json.loads((ROOT / "subject-runs.json").read_text()))
        (ROOT / "judges").mkdir(exist_ok=False)
        jobs = [(case, rep, model) for case in cases for rep in (1, 2) for model in ("gpt-5.6-sol", "gpt-5.5")]
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            records = list(pool.map(lambda args: judge(*args), jobs))
        (ROOT / "judge-runs.json").write_text(json.dumps(records, indent=2))
    else:
        raise SystemExit("Usage: python3 run.py subjects|judges (fresh directory required)")
    print(json.dumps({"runs": len(records), "valid": sum(r["valid"] for r in records)}))
    if not all(r["valid"] for r in records):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
