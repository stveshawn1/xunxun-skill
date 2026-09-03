# Xunxun Paired Evaluation v1 — Preregistered Protocol

This protocol and the five prompts are frozen before any scored answer is generated.

## Question

Does the neutral, publicly distributed Xunxun Skill improve one-turn explanations across unfamiliar systematic domains, compared with the same Codex model without Xunxun?

This experiment tests explanation structure, boundaries, terminology bridging, mechanism, and cognitive load. It does **not** test longitudinal adaptation, profile promotion, or cross-Session continuity.

## Cases

| ID | Domain | Reader background | Questions |
|---|---|---|---:|
| `pi-coding-agent` | coding-agent architecture | programmer, new to Pi | 3 |
| `openai-agents-sdk` | agent application framework | programmer, new to the SDK | 3 |
| `dsh` | modular agent harness | programmer, new to DSH internals | 3 |
| `adaptive-immunity` | biology | no specialist background | 3 |
| `financial-statements` | accounting | no specialist background | 3 |

Each prompt contains a bounded source packet. Answers must use only that packet, answer in Chinese, avoid tools and external research, and stay under 1,800 Chinese characters.

## Conditions

- **Baseline:** Xunxun is disabled through Codex `skills.config`; all other settings are unchanged.
- **Treatment:** Xunxun is available for implicit invocation. `$XUNXUN_HOME` points to an empty directory, and no project profile exists.
- Model: `gpt-5.6-sol`.
- Reasoning effort: `high`.
- Runner: `codex exec --ephemeral --ignore-user-config --ignore-rules --skip-git-repo-check -s read-only`.
- The paired runs for a case start together from fresh sessions.
- The exact same prompt bytes are passed to both conditions.
- Output order is blinded as A/B before grading.
- Network retries and usage metadata are retained as run metadata but are not teaching-quality evidence.

The only intended treatment difference is whether Xunxun is visible. A diagnostic run must first confirm that the Baseline skill list excludes `xunxun` and the Treatment list includes it.

## Rubric

Score every dimension from 0 to 4, using the source packet as the authority.

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| Accuracy | materially wrong | mostly correct with omissions | correct and source-faithful |
| Definition and boundaries | absent/confused | usable but incomplete | precise category and nearby distinctions |
| Mental model and mechanism | list of facts | partial causal flow | coherent, reconstructable system model |
| Terminology scaffolding | jargon blocks understanding | uneven bridging | unfamiliar terms bridged proportionally |
| Relevance and cognitive load | meandering/overloaded | acceptable | compact, prioritized, no template dumping |
| Transfer readiness | cannot apply model | some reusable distinctions | supports prediction on a new example |

Maximum: 24 points per output.

## Predeclared interpretation

- Per-case Xunxun win: treatment exceeds baseline by at least 2 points.
- Per-case tie: absolute difference is at most 1 point.
- Per-case regression: baseline exceeds treatment by at least 2 points.
- Evidence supports one-turn value only if Xunxun wins at least 3 of 5 cases, mean improvement is at least 2 points, no case loses more than 1 Accuracy point, and mean character-count ratio is at most 1.6.
- If quality improves but the length threshold fails, conclude a verbosity tradeoff rather than unqualified effectiveness.
- If gains concentrate in only one domain family, conclude contextual rather than general value.

These thresholds are practical decision rules, not a claim of statistical significance.

## Review

Two fresh model judges should score blinded A/B outputs using this rubric, with Xunxun disabled. The final report must retain both judges' scores, objective character counts, disagreements, unblinded mapping, and a separate evidence-based maintainer review. Self-assessment alone is not proof.

