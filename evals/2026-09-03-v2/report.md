# Xunxun Natural-Question Evaluation v2.3 — Report

## Verdict

Xunxun passed the preregistered v2.3 aggregate gate, but the evidence supports a **modest, context-dependent one-turn benefit**, not a broad cross-domain guarantee.

Across 45 independently generated pairs, majority-blinded judgments preferred Xunxun 19 times, Baseline 12 times, and tied 14 times. Among non-ties, Xunxun's share was 61.3%. Mean required-fact coverage improved by 3.4 percentage points, the descriptive bootstrap 95% interval was approximately `+0.9pp` to `+6.1pp`, and no domain's mean fact coverage declined.

The pairwise preference sign test was not statistically significant (`p≈0.281`, ties excluded). More importantly, preferences were heterogeneous: financial statements strongly favored Xunxun, while Pi and adaptive immunity slightly favored Baseline. The correct interpretation is therefore “measurable practical signal worth further testing,” not “general effectiveness proven.”

This suite tests the neutral, pure one-turn Skill effect. It does not test personal profiles, cross-Session continuity, or the longitudinal adaptive loop.

## What changed from v1

V1 asked three polished questions at once, explicitly requested a transferable mental model and causal chain, and supplied pre-digested teaching prose. Baseline therefore received much of Xunxun's treatment directly in the user prompt and scored at the rubric ceiling.

V2 instead uses:

- 15 natural novice questions, one concept per fresh Session;
- three independent generations per condition;
- terse source snapshots in `source.md`, read by both arms;
- question-specific required facts and forbidden inferences;
- relative A/B judgments rather than generic style scores;
- three blinded judges and explicit directional-disagreement reporting;
- a pure-Skill lane that rejects other Skill reads;
- an automated runner, grader, analyzer, and private trace boundary.

Before v2, Xunxun was also simplified: the mandatory second read of `presets.md` was removed, the route summary moved into `SKILL.md`, source ontology was protected from intuitive over-simplification, and domain/source Skills were defined as complementary rather than replaceable.

## Aggregate results

| Measure | Result |
|---|---:|
| Independent items | 15 |
| Replicates per arm | 3 |
| Paired comparisons | 45 |
| Raw subject answers | 90 |
| Xunxun / Baseline / tie | 19 / 12 / 14 |
| Xunxun share among non-ties | 61.3% |
| Mean factual-coverage delta | +3.4pp |
| Descriptive bootstrap 95% interval | +0.9pp to +6.1pp |
| Pairwise-preference sign test | `p≈0.281` |
| Confusion-resolution net preference | +12 |
| Boundary-precision net preference | +16 |
| Transfer-support net preference | +18 |
| Cognitive-efficiency net preference | -3 |
| Final-character ratio X/B | 1.093 |
| Cumulative input-token ratio X/B | 1.425 |
| Cumulative output-token ratio X/B | 1.410 |
| Treatment trigger rate | 100% |
| Judge exact pairwise agreement | 53.3% |
| Judge direct-opposition rate | 5.2% |

The revised startup reduced measured input overhead from v1's `2.735×` to `1.425×`, but Xunxun still costs about 42.5% more cumulative input tokens. Its final answers were only 9.3% longer, so most remaining cost comes from the extra Skill-loading/model turn rather than user-visible prose.

## Domain distribution

| Domain | Xunxun | Baseline | Tie | Mean fact delta |
|---|---:|---:|---:|---:|
| Pi Coding Agent | 2 | 4 | 3 | 0.0pp |
| OpenAI Agents SDK | 3 | 2 | 4 | +0.9pp |
| DSH | 4 | 3 | 2 | +6.5pp |
| Adaptive immunity | 2 | 3 | 4 | +0.9pp |
| Financial statements | 8 | 0 | 1 | +8.7pp |

The aggregate advantage is concentrated in financial statements. DSH is positive overall but internally polarized. This heterogeneity is why the report does not promote the aggregate pass into a claim of universal benefit.

## Item results

| Item | X | B | Tie | Fact delta | Character ratio X/B |
|---|---:|---:|---:|---:|---:|
| `pi-session-tree` | 1 | 1 | 1 | 0.0pp | 0.965 |
| `pi-turn-step` | 0 | 1 | 2 | 0.0pp | 1.340 |
| `pi-extension-skill-template` | 1 | 2 | 0 | 0.0pp | 1.249 |
| `agents-agent-runner-session` | 2 | 1 | 0 | 0.0pp | 1.432 |
| `agents-manager-handoff` | 1 | 1 | 1 | 0.0pp | 0.934 |
| `agents-guardrail-tracing` | 0 | 0 | 3 | +2.8pp | 1.322 |
| `dsh-profile-bundle-patch` | 1 | 0 | 2 | 0.0pp | 1.053 |
| `dsh-service-lifecycle` | 3 | 0 | 0 | +19.4pp | 0.831 |
| `dsh-model-visible-log` | 0 | 3 | 0 | 0.0pp | 1.167 |
| `immune-clonal-selection` | 0 | 1 | 2 | +2.8pp | 1.275 |
| `immune-tcell-activation` | 2 | 1 | 0 | 0.0pp | 0.947 |
| `immune-memory` | 0 | 1 | 2 | 0.0pp | 1.839 |
| `accounting-debit-credit` | 2 | 0 | 1 | +6.7pp | 1.009 |
| `accounting-profit-cash` | 3 | 0 | 0 | +8.3pp | 1.163 |
| `accounting-machine-purchase` | 3 | 0 | 0 | +11.1pp | 1.183 |

## Strongest positive evidence

### DSH service lifecycle

All three majority judgments preferred Xunxun, and required-fact coverage improved by 19.4pp. The better answers clearly separated:

```text
super(ctx, 'llm')  → provide an existing service instance
ctx.llm             → resolve that service through Context's Proxy
inject: ['llm']     → declare availability dependency
Fiber               → own plugin activation and cleanup
```

This is the kind of layered object distinction Xunxun was designed to protect.

### Financial statements

Eight of nine pairs favored Xunxun. The strongest answers converted abstract accounting distinctions into small transactions and cross-statement timelines. They improved transfer without dramatically increasing length.

This domain supplied more headroom because the novice questions carried plausible misconceptions—“debit means increase,” “profit means cash,” and “cash purchase means immediate expense”—that benefited from explicit boundaries and counterfactuals.

## Strongest regressions

### DSH model-visible log

Baseline won all three replicates despite equal fact coverage. Xunxun often repeated the same authority/projection distinction through several diagrams, examples, and recap lines. Judges consistently preferred Baseline's lower cognitive cost.

### Pi extension versus Skill

Baseline won two of three. Both arms reached the correct execution-boundary distinction, but Xunxun tended to add safety design advice beyond the user's immediate confusion. Extra completeness did not create extra teaching value.

### Immune memory

The item produced one Baseline preference and two ties, with a character ratio of `1.839`. Xunxun's analogies and expanded cell taxonomy occasionally helped transfer, but not enough to justify the additional reading burden.

These regressions support a narrower next rule: when the source already contains one clean decisive distinction, state it and stop; do not add an architecture tour merely because more layers are available.

## Judge behavior

| Judge | Xunxun | Baseline | Tie |
|---|---:|---:|---:|
| GPT-5.6 Sol | 16 | 8 | 21 |
| GPT-5.6 Terra | 16 | 14 | 15 |
| GPT-5.5 | 23 | 13 | 9 |

All three judges independently preferred Xunxun more often than Baseline, but their willingness to leave `tie` differed substantially. Exact agreement was only 53.3%; direct Xunxun-versus-Baseline opposition was 5.2%. The aggregate majority is directionally coherent but not highly calibrated.

## Evaluation-process findings

The pilot process itself found and corrected three harness defects before final scoring:

1. one subprocess timeout originally aborted the whole batch instead of preserving completed results;
2. path-aliasing such as `../xunxun/SKILL.md` produced a false trigger/contamination result;
3. a shell command that opened several `SKILL.md` files bypassed the original command-level contamination check.

The final harness extracts individual Skill paths, disables known competing source Skills, preserves only completed traces, and reruns an entire pair after real contamination. All final 90 subject runs are complete; all 45 Treatment runs opened Xunxun; no final run contains an unexpected Skill read.

The original v2.0 pilot was rejected for absolute-score saturation. V2.1 replaced those scores with item facts and relative teaching dimensions. V2.2 added a third judge. V2.3 separated direct directional opposition from tie-threshold disagreement. Each change was committed before the next affected judge or subject stage; the timeline is preserved in the protocol amendments.

## What the evidence supports

Supported:

- Xunxun can improve answers to natural, underspecified novice questions.
- Its clearest contributions are boundary precision and transferable rules.
- The source-ontology fix prevented the broad DSH category regression seen in v1 and produced a strong service-lifecycle result.
- The single-file route materially reduced, but did not eliminate, runtime overhead.

Not supported:

- universal gains across domains;
- statistical significance from this convenience sample;
- improved longitudinal adaptation;
- value from personal or project profiles;
- improved real-repository navigation, because subjects read fixed source snapshots rather than full checkouts.

## Next changes suggested by evidence

1. Add a stop rule for decisive distinctions: after the misconception is corrected and the boundary is usable, do not add adjacent advice unless asked.
2. Keep source-category protection; it directly addresses the v1 DSH failure.
3. Optimize Skill loading further only if the host offers a supported way to inject selected Skill instructions without an extra model/tool turn.
4. Run a separate longitudinal suite with matched scripted follow-ups before making any adaptive-learning claim.
5. Run real-checkout Pi/DSH/Agents-SDK walkthroughs separately; do not mix codebase-navigation outcomes into this one-turn concept score.

No additional Skill change is made from the final results in this report. The v2 suite should remain a regression set for future revisions.

## Evidence map

- Frozen items and checklists: [`suite.json`](suite.json)
- Subject outputs: [`results/`](results/)
- Blinded judgments: [`judgments/`](judgments/)
- Pilot and remaining run metadata: [`runs-pilot.json`](runs-pilot.json), [`runs-remaining.json`](runs-remaining.json)
- Computed aggregate: [`analysis-full.json`](analysis-full.json)
- Protocol history: [`protocol.md`](protocol.md), [`protocol-amendment-v2.1.md`](protocol-amendment-v2.1.md), [`protocol-amendment-v2.2.md`](protocol-amendment-v2.2.md), [`protocol-amendment-v2.3.md`](protocol-amendment-v2.3.md)
- Integrity and completion check: [`manifest.json`](manifest.json), [`verify.py`](verify.py)
