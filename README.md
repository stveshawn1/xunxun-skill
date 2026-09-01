# Xunxun · 循循

> Definition, intuition, evidence, feedback, then a better explanation.

Xunxun is an Agent Skill for teaching concepts, supplied files, and codebases through explicit explanation presets. It keeps each learner’s validated preferences local, adapts when an explanation fails, and promotes only anonymous, repeatedly validated patterns into shared teaching principles.

## What it does

- **Concept preset** — definitions, distinctions, minimal examples, value, and limits.
- **Reference preset** — place a file or artifact in its system before reading critical regions.
- **Codebase preset** — follow entrypoints, natural seams, execution paths, state, and lifecycle before line-level code.
- **Feedback learning** — accept `反馈：...`, retry with a different explanatory variable, validate, and update a private learner profile.
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
反馈：这个解释太抽象，我需要先看一个具体例子。
```

## Repository structure

```text
xunxun-skill/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── presets.md
    ├── feedback-learning.md
    ├── validated-principles.md
    ├── learner-profile.template.md
    └── quality-scorecard.md
```

The real learner profile lives in the gitignored `references/learner-profiles.local.md`. It is never committed or pushed by the Skill.

## Design boundary

Xunxun has no account system or synchronization backend. It can maintain explicitly selected local learner profiles. Cross-device or cross-installation learning requires a separate consent, identity, and storage design.
