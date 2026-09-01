# Xunxun · 循循

> Explain, observe, adapt — without turning learning into a survey.

Xunxun is an Agent Skill for teaching concepts, supplied files, and codebases through explicit explanation presets. It observes whether later behavior progresses, repeats, transfers, or rejects the model; then applies a small explanation treatment and updates only local, evidence-supported preferences.

## What it does

- **Concept preset** — definitions, distinctions, minimal examples, value, and limits.
- **Reference preset** — place a file or artifact in its system before reading critical regions.
- **Codebase preset** — follow entrypoints, natural seams, execution paths, state, and lifecycle before line-level code.
- **Adaptive learning** — infer fit from ongoing behavior, apply a scoped treatment delta, and update a compact private evidence ledger.
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
└── references/
    ├── presets.md
    ├── adaptive-learning.md
    ├── validated-principles.md
    ├── learner-profile-template.md
    └── quality-scorecard.md
```

The real learner profile lives in the gitignored `references/learner-profiles.local.md`. It is never committed or pushed by the Skill.

## Design boundary

Xunxun has no account system or synchronization backend. It can maintain explicitly selected local learner profiles. Cross-device or cross-installation learning requires a separate consent, identity, and storage design.
