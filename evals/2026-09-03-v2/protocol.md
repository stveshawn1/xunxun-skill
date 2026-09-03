# Xunxun Evaluation v2 — Preregistered Protocol

## Purpose

Measure whether Xunxun improves explanations for natural novice questions. V1 remains a high-scaffolding ceiling/regression suite; v2 removes its treatment-shaped prompts and evaluates each concept independently.

## Lanes

This report covers the **pure one-turn Skill effect**. Other optional source Skills are disabled in both arms, profiles are neutral, and only Xunxun availability differs. Ecosystem routing and longitudinal adaptation are separate future lanes and must not be averaged into this result.

## Items

- Five domains: Pi Coding Agent, OpenAI Agents SDK, DSH, adaptive immunity, and financial statements.
- Three independently run novice questions per domain: 15 items total.
- Each item starts from a fresh ephemeral Session and is generated three times per condition.
- Total subject outputs after the full run: `15 × 2 × 3 = 90`.
- Every item receives the same domain source snapshot through `source.md`, but only a short natural user question. The prompt does not request definitions, distinctions, causal chains, examples, transfer, or a teaching template.

The machine-readable item list, prompts, fact checklists, forbidden inferences, and pilot selection are frozen in [`suite.json`](suite.json).

## Conditions

- Baseline: Xunxun disabled.
- Treatment: neutral Xunxun available for implicit invocation.
- OpenAI Docs is disabled in both arms to prevent the v1 Agents-SDK routing confound.
- Model: `gpt-5.6-sol`.
- Reasoning effort: `medium`, matching the local configured default rather than v1's forced `high`.
- Same source, prompt bytes, working directory, tool permissions, and concurrent time block within each pair.
- `$XUNXUN_HOME` contains an explicit empty `profile.md`; no project profile exists.
- The runner records whether Treatment actually opened Xunxun. Failure to trigger is an outcome, not grounds for rewriting the prompt.
- Reading any other Skill invalidates that run. A failed run invalidates its pair.

## Pilot gate

Run the five `pilot_ids`, three replicates per arm (`30` outputs), then grade them before launching the remaining items.

Proceed only if:

1. every scored pair is isolated and complete;
2. fewer than 80% of Baseline outputs reach at least 90% of the checklist-based maximum;
3. at least one scored dimension varies across outputs;
4. blinded judges do not assign the same maximum vector to at least 80% of outputs.

If the gate fails, revise measurement—not Xunxun—and preregister a new protocol before rerunning.

## Blinding

For each item and replicate, A/B mapping is derived from the parity of the first hexadecimal character of:

```text
SHA-256(<skill-commit>:<item-id>:<replicate>)
```

Odd means A=Xunxun; even means A=Baseline. Judges receive the source, natural prompt, item-specific checklist, and A/B outputs, but not the mapping.

## Grading

Two fresh judges (`gpt-5.6-sol` and `gpt-5.6-terra`, high reasoning) independently return:

- one boolean per required fact;
- one boolean per forbidden inference;
- 0–2 scores for intuition, boundary clarity, mechanism, and novice relevance;
- A/B/tie preference with rationale.

Deterministic normalized score:

```text
raw = 2 × covered facts - 2 × forbidden inferences
      + intuition + boundary + mechanism + novice relevance
maximum = 2 × required fact count + 8
normalized = raw / maximum
```

Scores are averaged across the two judges before condition comparison. Item-level results aggregate three independent replicates; suite-level results aggregate all 45 pairs.

## Interpretation

Report mean paired normalized-score delta, pairwise win/tie/loss rate, trigger rate, final-character ratio, cumulative token ratio, and judge disagreement.

Evidence supports general one-turn value only when all hold:

- mean paired normalized-score delta is at least `+0.03`;
- at least 55% of non-tied pairs favor Xunxun;
- no domain's mean factual coverage drops by more than `0.05`;
- mean final-character ratio is at most `1.5`;
- Treatment trigger rate is at least 80%.

Bootstrap confidence intervals may be reported as descriptive uncertainty, but this convenience sample does not justify population-level causal claims.

## Execution environment

[`run.py`](run.py) creates one isolated temporary source workspace, starts paired conditions concurrently, saves raw answers, retains private traces outside tracked results, records usage and Skill reads, and exits nonzero on contamination or incomplete runs.

The current Codex CLI attempts WebSocket delivery before falling back to HTTPS, and the built-in provider preference cannot be overridden through supported config. This affects both arms symmetrically and is treated as latency noise, not an outcome.

