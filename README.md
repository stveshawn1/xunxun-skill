# Xunxun · 循循

> Explain, observe, adapt — without turning learning into a survey.

Xunxun is an Agent Skill for teaching concepts, supplied files, and codebases through explicit explanation presets. It observes whether later behavior progresses, repeats, transfers, or rejects the model; then applies a small explanation treatment and updates only local, evidence-supported preferences.

## What it does

- **Concept preset** — definitions, distinctions, minimal examples, value, and limits.
- **Reference preset** — place a file or artifact in its system before reading critical regions.
- **Codebase preset** — follow entrypoints, natural seams, execution paths, state, and lifecycle before line-level code.
- **Terminology bridging** — add a minimal intuitive gloss when the learner has not demonstrated a required specialized term.
- **Adaptive learning** — use a contextual-bandit-inspired loop to select scoped treatment deltas, infer fit from ongoing behavior, and update a compact private evidence ledger.
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
│   ├── presets.md
│   ├── adaptive-learning.md
│   ├── terminology-bridging.md
│   ├── comparison-protocol.md
│   ├── local-state.md
│   ├── validated-principles.md
│   ├── local-state-templates.md
│   └── quality-scorecard.md
├── evals/
│   └── case-template.md
└── examples/
    └── comparison-template.md
```

The repository contains rules and templates only. Private state lives under non-empty `$XUNXUN_HOME`, otherwise `~/.xunxun`, separated into global learner profile/vocabulary and per-project ledgers. Current Session state remains ephemeral.

## Compare with and without Xunxun

Use `evals/case-template.md` to run the same prompt in fresh, matched sessions without and with Xunxun. Record unedited outputs and human review before drawing a conclusion. Promote only privacy-safe, representative reviewed cases into `examples/` using `examples/comparison-template.md`.

## Design boundary

Xunxun has no account system, automatic Session-end hook, locking, or synchronization backend. It can maintain explicitly selected local learner and project state. Cross-device or concurrent-writer support requires a separate consent, identity, and storage design.
