# Xunxun · 循循

> Explain, observe, adapt — without turning learning into a survey.

Xunxun is an Agent Skill for teaching concepts, supplied files, and codebases through explicit explanation presets. It observes whether later behavior progresses, repeats, transfers, or rejects the model; then applies a small explanation treatment and updates only local, evidence-supported preferences.

## What it does

- **Concept preset** — definitions, distinctions, minimal examples, value, and limits.
- **Reference preset** — place a file or artifact in its system before reading critical regions.
- **Codebase preset** — follow entrypoints, natural seams, execution paths, state, and lifecycle before line-level code.
- **Progressive depth** — start with the smallest complete explanation and add layers only when the learner's goal or later behavior requires them.
- **Terminology bridging** — add a minimal intuitive gloss when the learner has not demonstrated a required specialized term.
- **Adaptive learning** — use a contextual-bandit-inspired loop to select scoped treatment deltas, infer fit from ongoing behavior, and update compact private state.
- **Promotion checkpoints** — when a durable preference is supported, explain the proposed local update and ask whether to retain it.
- **Honest personalization** — no identity inference, telemetry, automatic upload, or claim of cross-device learning.

## Install

```sh
npx skills add stveshawn1/xunxun-skill
```

Or ask a Skill-compatible agent to install:

```text
帮我安装这个 Skill：https://github.com/stveshawn1/xunxun-skill
```

## Use

```text
用循循解释一下 TypeScript 的类型擦除。
用循循带我读这个文件，先说它在系统中的角色。
用循循带我走完整个代码库的主链路。
这个解释还是太抽象，我其实卡在“运行时为什么不认类型”。
```

## Repository structure

```text
xunxun-skill/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── adaptive-learning.md
│   ├── terminology-bridging.md
│   ├── comparison-protocol.md
│   ├── local-state.md
│   ├── local-state-templates.md
│   ├── teaching-principles.md
│   └── quality-scorecard.md
├── evals/
│   └── case-template.md
└── examples/
    └── comparison-template.md
```

The repository contains shared rules and templates. Cross-project preferences live in `$XUNXUN_HOME/profile.md`, or `~/.xunxun/profile.md` by default. Project learning state is opt-in and lives in `<project-root>/.xunxun/profile.md`; Git repositories keep it private through local exclusion. Current Session state remains ephemeral.

## Compare with and without Xunxun

Use `evals/case-template.md` to run the same prompt in fresh, matched sessions without and with Xunxun. Record unedited outputs and human review before drawing a conclusion. Promote only privacy-safe, representative reviewed cases into `examples/` using `examples/comparison-template.md`.

The first preregistered five-domain paired evaluation found no material one-turn improvement under highly structured prompts: both blinded judges rated all five pairs as ties, with a mean Xunxun delta of `+0.1/24` and `2.735×` cumulative input-token usage. This negative result, raw outputs, judgments, integrity manifest, and proposed next tests are preserved in [`evals/2026-09-03-v1/report.md`](evals/2026-09-03-v1/report.md).

The corrected v2.3 evaluation used 15 independent natural novice questions, three generations per arm, item-specific fact checks, and three blinded judges. Xunxun was preferred in 19 of 31 non-tied pairs (61.3%), improved mean fact coverage by 3.4 percentage points, and used `1.425×` cumulative input tokens. Gains were strongly context-dependent—especially concentrated in financial statements—so the result supports modest practical value, not universal effectiveness. Full raw evidence and process amendments are in [`evals/2026-09-03-v2/report.md`](evals/2026-09-03-v2/report.md).

## Design boundary

Xunxun deliberately has no term-by-term vocabulary database, account system, automatic Session-end hook, locking, or synchronization backend. It may repeat a small terminology bridge when evidence is unclear; that cost is preferable to maintaining stale vocabulary state. Cross-device or concurrent-writer support requires a separate consent, identity, and storage design.
