# Current-guidance diagnostic evaluation

## Finding

This small test did **not** demonstrate an advantage for the full Xunxun guidance over either the default model or a short teaching prompt. Do not use it as a positive marketing claim.

The full guidance covered more checklist facts, but the judges often preferred shorter answers. Both full-guidance responses to the English return-to-code case were in Chinese, despite an English user message.

The evaluation prompted GPT-6 Astra at medium reasoning with four cases and two repeats per condition: 24 fresh subject calls. Two judges independently reviewed each anonymous triplet: 16 fresh judge calls. All completed successfully and the runner reported no unexpected completed tool items.

The Skill source was `b90172e` and the evaluation protocol was committed as `57de32b` before generation. The installed harness reported `codex-cli 0.153.4`. Cases use supplied concept facts and synthetic code fixtures, not live upstream repositories.

## Results

Agreement means both judges chose the same result. A disagreement, including preference versus tie, is unresolved.

| Comparator | Both prefer Xunxun | Both prefer comparator | Both tie | Unresolved |
|---|---:|---:|---:|---:|
| Default model | 1 | 5 | 0 | 2 |
| Short teaching prompt | 1 | 4 | 0 | 3 |

| Condition | Mean fact coverage | Prohibited-claim flags |
|---|---:|---:|
| Default model | 91.7% | 0 |
| Short teaching prompt | 97.9% | 0 |
| Full Xunxun guidance | 100% | 0 |

Coverage is averaged over 8 answers and 2 judges per condition. Flags count judge observations, not independent mistakes. Coverage and unsupported claims are separate; neither is a measure of human learning.

The short prompt was:

> Answer the current question first. Define unfamiliar concepts plainly, use a small example when useful, preserve important distinctions, and stay concise. Adjust to feedback and reconnect prerequisite detours to the main topic.

## Interpretation and limits

- There is a ceiling on these narrow fact checks: a strong base model already answers most of them correctly.
- Extra completeness did not reliably justify extra explanation. A configuration answer could cover more constructor detail while being less useful for the immediate retry-count question.
- The language mismatch is a concrete failure, not merely a judge's style preference.
- All runtime guidance and references were supplied inline. This deliberately tests the full supplied instruction set; it is heavier than Xunxun's intended selective loading. The result cannot establish the effectiveness or cost of a normal installed-Skill workflow.
- The fixed continuation snapshots give each condition the same history, but do not measure how a real conversation evolves or whether a learner understood it.
- Project progress is supplied to every condition. Actual file discovery, state writes, permission handling, and automatic triggering are not tested.
- Two repeats and four convenience cases are not enough for a general claim. This is not a population learning study or an independent human review.

## Concrete change and follow-up

Added an explicit response-language rule to the Skill: honor the learner's requested language; otherwise use the latest substantive user message's language. Skill examples and reference language cannot override it.

A separate [language check](../2026-09-08-language/report.md) compares frozen pre-change guidance with revised guidance. It does not overwrite the failing v3 answers and does not convert a language fix into a claim of improved overall teaching quality.

No additional teaching rules were added simply to chase judge preferences. The README now uses a clearly labeled illustrative walkthrough and links this record without promoting a win rate.

## Reproduce and inspect

- [Frozen questions and evidence](suite.json)
- [Protocol committed before generation](protocol.md)
- [Exact supplied guidance](guidance.txt)
- [Raw answers](answers/)
- [Raw anonymous judgments](judges/)
- [Subject metadata](subject-runs.json) and [judge metadata with label mapping](judge-runs.json)
- [Runner](run.py) and [summary/hash check](summarize.py)

Run `python3 evals/2026-09-08-v3/summarize.py` to verify saved output hashes and recompute the table. The runner refuses to reuse an existing output directory. New model experiments should use a new directory.

The common prompt prohibits tool use, which is checked against completed items reported by the CLI; it is not a server-enforced tool disable. Private local profiles are not supplied. Ambient host instructions are not fully captured, which limits reproduction on a different installation.
