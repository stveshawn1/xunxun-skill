# Xunxun Paired Evaluation v1 — Report

## Verdict

This experiment does **not** establish general one-turn value from enabling neutral Xunxun.

Both blinded judges called all five pairs ties. Under the preregistered rule, Xunxun produced zero wins, one regression-sized direction did not occur because every absolute difference was at most one, and the mean paired improvement was only `+0.1/24`. The required threshold was at least three wins and a mean improvement of `+2`.

The result is best described as **high-quality parity with substantial execution overhead**, not evidence that Xunxun improves an already strong, well-scaffolded prompt.

This is a negative/ambiguous eval, so it remains under `evals/` and is not promoted to `examples/`.

## Aggregate results

Scores are the mean of two blinded judges after unblinding.

| Case | Baseline | Xunxun | Delta | Decision | Final-character ratio X/B |
|---|---:|---:|---:|---|---:|
| Pi Coding Agent | 23.0 | 24.0 | +1.0 | tie | 1.083 |
| OpenAI Agents SDK | 24.0 | 24.0 | 0.0 | tie | 1.063 |
| DSH | 24.0 | 23.0 | -1.0 | tie | 0.983 |
| Adaptive immunity | 23.5 | 24.0 | +0.5 | tie | 1.198 |
| Financial statements | 24.0 | 24.0 | 0.0 | tie | 0.935 |
| **Mean / aggregate** | **23.7** | **23.8** | **+0.1** | **0 wins** | **1.044** |

Final-answer length was controlled successfully: Xunxun was only 4.4% longer in aggregate and was shorter in two cases. The recent progressive-depth change therefore avoided a broad final-answer verbosity regression.

Runner-reported cumulative input usage was 96,470 tokens for Baseline and 263,879 for Xunxun (`2.735×`). Output usage was 4,198 versus 7,694 (`1.833×`). Much of this difference comes from the extra turns needed to read the Skill and preset, not from the final answers.

## Case review

### Pi Coding Agent: small positive, below threshold

- [Prompt](pi-coding-agent/prompt.md) · [Baseline](pi-coding-agent/baseline.md) · [Xunxun](pi-coding-agent/xunxun.md)
- Both answers clearly separated physical JSONL order from logical tree structure, traced Turn/Step, and distinguished Extension, Skill, and prompt template.
- Baseline added that a Skill instruction might be weakened or omitted by compaction; the packet did not establish that claim. Xunxun stayed within the source boundary.
- The judges awarded Xunxun `+1`, not enough for a preregistered win.

### OpenAI Agents SDK: ceiling tie

- [Prompt](openai-agents-sdk/prompt.md) · [Baseline](openai-agents-sdk/baseline.md) · [Xunxun](openai-agents-sdk/xunxun.md)
- Both answers accurately separated Agent, Runner, and Session; Manager and Handoff; Guardrail and Tracing.
- Xunxun added a compact transfer heuristic—expert as material versus expert as new owner—but Baseline already supplied an equivalent control model.
- Baseline selected the system OpenAI Docs Skill while Treatment selected Xunxun. This is an end-to-end routing effect and a confound for a pure prompt-ablation interpretation.

### DSH: small negative, below threshold

- [Prompt](dsh/prompt.md) · [Baseline](dsh/baseline.md) · [Xunxun](dsh/xunxun.md)
- Both answers built the intended composition, service-lifecycle, and event-authority models.
- Xunxun simplified Bundle to “a reusable group of patches,” omitting the more exact npm-package and manifest boundary supplied by the packet.
- It also said dependent plugins would “exit or wait” when a provider unloads, which was more specific than the packet. Both judges scored it one point below Baseline.

### Adaptive immunity: small positive, below threshold

- [Prompt](adaptive-immunity/prompt.md) · [Baseline](adaptive-immunity/baseline.md) · [Xunxun](adaptive-immunity/xunxun.md)
- Both answers were correct and causally coherent.
- Xunxun made the counterfactual and transfer rules especially explicit: diversity supplies candidates, selection chooses, expansion amplifies; recognition tests matching, costimulation permits activation.
- One judge gave Xunxun `+1`; the other scored a tie.

### Financial statements: ceiling tie

- [Prompt](financial-statements/prompt.md) · [Baseline](financial-statements/baseline.md) · [Xunxun](financial-statements/xunxun.md)
- Both answers correctly separated debit/credit sides from increase/decrease, traced the two-period credit sale, and connected equipment purchase and depreciation across statements.
- Xunxun added journal-entry notation and was shorter, but the rubric found no material quality difference.

## Why the experiment found little incremental value

### 1. The prompts already contained much of the treatment

Every prompt explicitly asked for a transferable mental model, boundaries, or a causal chain. The source packets were deliberately concise and already organized around the distinctions being tested. This made the test fair and source-bounded, but it also gave Baseline the same high-level scaffolding that Xunxun normally contributes.

The 23–24/24 scores across both conditions show a ceiling effect. This experiment answers a narrow question well: **Xunxun adds little when a strong model receives an unusually well-designed teaching prompt and pre-digested source packet.** It does not answer whether Xunxun helps with natural, underspecified questions or raw code/doc context.

### 2. The underlying model is already a strong explainer

Baseline independently used definitions, distinctions, examples, causal chains, and transferable summaries. Xunxun cannot claim value merely because these features appear in Treatment; the paired outputs show they often appear without it.

### 3. The Skill adds execution cost before it adds content

Treatment normally made one model turn to select/read `SKILL.md`, another to read `presets.md`, and a final turn to answer. Baseline usually answered in one turn. The extra context produced no preregistered wins here.

### 4. One turn cannot exercise Xunxun's main differentiator

The adaptive loop depends on later behavior: repeated confusion, transfer, correction, or progression. A one-turn three-question answer can test static teaching discipline but not treatment selection, promotion, or project continuity.

## Implications for Xunxun

The evidence does not support deleting Xunxun, but it does reject a broad claim that the current neutral Skill automatically improves any one-turn explanation.

The strongest supported interpretation is narrower:

- Xunxun preserves parity across five diverse domains without a large final-answer length penalty.
- It sometimes improves explicit boundaries or transfer heuristics.
- It sometimes over-simplifies a source boundary.
- Its current loading path is expensive relative to those small gains.

## Proposed improvements

1. **Reduce the two-read startup path.** Put the minimum preset router directly in `SKILL.md`, or otherwise avoid a second model/tool turn just to read `presets.md`. Re-test token usage before adding more teaching rules.
2. **Add a source-boundary check.** When a packet defines an implementation category—such as “Bundle is an npm package whose manifest points to a patch”—do not compress it into a looser category merely for intuition. Mark inferences instead of silently extending lifecycle behavior.
3. **Skip redundant teaching treatment.** If the user prompt already specifies the desired mental model, distinctions, examples, and causal chain, answer directly; Xunxun should contribute only missing structure.
4. **Compose with authoritative domain Skills.** The Agents SDK case suggests Xunxun can compete with a source-specialist Skill. Teaching method should wrap verified domain evidence rather than displace its source discipline.
5. **Run a second, higher-headroom eval.** Use natural short questions plus raw excerpts instead of pre-digested teaching packets, while preserving matched context and source truth.
6. **Test the actual adaptive claim separately.** Use multi-turn cases with a planted misunderstanding, a changed explanation treatment, and a transfer question. Do not infer longitudinal value from this one-turn suite.

No Skill changes are made from this result alone. The next revision should target one observed failure at a time and rerun the same frozen v1 cases as regression controls.

## Evidence limits

- Five cases and two model judges do not establish statistical significance.
- Judges used the same model family as the subject runs, though one used Sol and one Terra.
- The maintainer authored the source packets and performs the final review.
- The rubric saturated, limiting discrimination.
- Natural user behavior, multi-turn adaptation, personal profiles, and cross-Session state were not tested.
- Transport repeatedly fell back from WebSocket to HTTPS; both conditions were affected similarly.

Raw blinded judgments are preserved in [`judges/sol.json`](judges/sol.json) and [`judges/terra.json`](judges/terra.json). Reproduction and integrity details are in [`run-metadata.md`](run-metadata.md).
