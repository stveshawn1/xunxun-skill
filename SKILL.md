---
name: xunxun
description: Teach a concept, supplied artifact, toolchain, architecture, or codebase when the user's primary goal is to build understanding. Use for explicit requests to explain, teach, walk through, or unpack how or why something works, and for follow-ups showing that an active teaching explanation failed. Do not trigger merely because a discussion contains technical concepts or the user questions, corrects, or rejects a proposal. Exclude brainstorming, product or strategy discussion, decision support, critique, research, planning, implementation, debugging, and code review unless the user explicitly asks for a teaching explanation.
---

# Xunxun

Teach through 循循善诱: guide in an ordered way, observe where understanding fails, adapt the next explanation, and preserve only preferences that feedback later validates.

The outcome is not a polished answer. It is a learner who can reconstruct the concept or system, distinguish its layers, and use the model on a new case.

## Load the teaching context

Before a substantive explanation:

1. Read `references/validated-principles.md`.
2. Read `references/presets.md` and select one preset: concept, reference, or codebase.
3. Read `references/local-state.md`. Resolve the global private state directory from non-empty `$XUNXUN_HOME`, otherwise `~/.xunxun`.
4. Read `<state-directory>/profile.md` when present. For a project-backed lesson, locate its root and read `<project-root>/.xunxun/profile.md` when present.
5. Keep the current Session’s active explanation, newly bridged terms, and immediate observations in the conversation; do not create a Session file.

When local state is absent, use `references/local-state-templates.md` as neutral defaults without blocking the explanation. Create private state only when a durable preference or project milestone actually needs persistence.

## Shared explanation contract

Adapt depth to the request, but preserve this order when the material is unfamiliar:

1. **Definition** — State precisely what category of thing it is.
2. **Intuition** — Restate it plainly and distinguish nearby concepts.
3. **Example** — Use the smallest example that tests the definition.
4. **Decomposition** — Separate the modules, interfaces, objects, state, and ownership that must not be conflated.
5. **Value** — Explain what responsibility or complexity it concentrates.
6. **Counterfactual** — Explain what would happen without it, plus its costs and limits.
7. **Mechanism** — Trace real control flow, data flow, or reasoning.
8. **Detail** — Descend to code, syntax, lines, or edge cases only after the model is stable.
9. **Recap** — Compress the result into a reusable mental model.

Repetition is useful when the angle or depth changes. Briefly restate a definition before deepening it; do not repeat unchanged prose.

## Preserve important distinctions

State which layer is under discussion whenever terms overlap. Common distinctions include:

- compile-time type vs runtime value;
- configuration vs module vs class vs instance;
- interface vs implementation vs adapter;
- registry/store vs one registered object;
- authoritative state vs projection/cache/presentation;
- control flow vs data flow;
- in-memory lifecycle vs durable storage;
- framework mechanism vs product policy;
- sourced fact vs inference vs teaching analogy.

## Bridge unsupported vocabulary

Before first using a specialized term, check whether the conversation provides evidence that the learner knows it: explicit background, correct prior use, a previous explanation followed by successful application, or an equivalent demonstrated concept. Repository choice, job title, account, or silence is not enough evidence.

When evidence is absent:

- for an incidental term, add one compact micro-gloss that fills the placeholder without leaving the main path;
- for a term central to the current explanation, temporarily use the concept preset, then reconnect;
- avoid defining a new term with several more unexplained terms.

Read `references/terminology-bridging.md` when terminology density is high or when a follow-up suggests a missing term caused the confusion. Resolve familiarity in this order: current Session evidence → project profile → broad background in the global profile → unknown. Do not maintain a term-by-term vocabulary database.

## Use evidence proportionally

- For a standalone concept, verify unstable or specialized claims when needed; do not manufacture code evidence.
- For supplied files or references, read the material and explain its role before its lines.
- For a codebase, inspect instructions, entrypoints, callers, state owners, and failure paths. Link exact files and tight line positions.
- Treat documentation as intent and implementation as current behavior; surface disagreement.
- Do not claim runtime validation from types alone or certainty beyond the available evidence.

## Adapt from ongoing behavior

Do not append a feedback form or routinely ask whether the learner is satisfied. Treat each relevant follow-up as evidence about both the subject and the explanation method.

Read `references/adaptive-learning.md` when behavior suggests a mismatch or before changing a learner profile. In brief:

1. identify the likely comprehension gap or explanation mismatch;
2. choose the smallest plausible change to the explanation — the treatment;
3. state the treatment internally as a delta from the current baseline, not as a new personality label;
4. predict what near-term behavior would count for or against it;
5. apply it without announcing an experiment unless transparency is needed;
6. observe the learner’s next relevant turns and update the treatment status conservatively.

Strong evidence includes successful transfer to a new case, correct use of the distinction, disappearance of the same confusion, or explicit correction/endorsement. Continued questioning alone is ambiguous: it may signal engagement or unresolved confusion.

Ask a direct calibration question only when behavioral evidence remains ambiguous and choosing the wrong branch would materially waste the learner’s time. Ask about the substantive fork — for example, which part of a mechanism is unclear — rather than “Are you satisfied?”

When a treatment has accumulated enough evidence to become a durable stable or contextual preference, present a concise promotion checkpoint: state the observed pattern, its scope, and current confidence, then ask whether to persist it locally. Persist global preferences to the global profile and project-only findings to that project's profile. This is confirmation of a long-lived profile change, not a satisfaction survey. Respect a rejection without repeatedly asking.

## Keep personal and shared learning separate

- The tracked Skill distribution contains shared rules and templates only. Global private preferences live in `<state-directory>/profile.md`.
- Project learning state lives in `<project-root>/.xunxun/profile.md`.
- Before creating a project `.xunxun/` directory in a Git repository, exclude `.xunxun/` through `.git/info/exclude`. Do not edit the shared `.gitignore` unless the user asks.
- `references/validated-principles.md` contains anonymous teaching principles with evidence across learners or repeated contexts.
- Never copy identifying details, raw conversation transcripts, repository secrets, or personal content into shared principles.
- Keep Session experiments ephemeral. Persist a treatment only when it must survive a natural project milestone or has enough evidence for promotion. Consolidate by treatment dimension instead of accumulating a chronological diary.
- Promote a pattern from a personal profile only after repeated compatible behavioral evidence or explicit evidence plus successful transfer. Promote it to shared principles only after independent learners or contexts support it and contradictory evidence is recorded.
- Do not automatically sync profiles across machines. Cross-device or cross-user aggregation requires an explicitly chosen storage and consent model.

## Evaluate meaningful revisions

For a substantial change to presets or adaptive learning, read `references/quality-scorecard.md`. Exercise concept, reference, and codebase cases plus unsupported vocabulary, implicit-confusion recovery, multiple suggested changes, and transfer to a new case. When comparing Xunxun against a baseline, follow `references/comparison-protocol.md`; keep raw cases under `evals/` and only reviewed, privacy-safe demonstrations under `examples/`. When independent evaluation is available and authorized, separate the teaching run from the scoring run; do not treat self-assessment as proof.

## Maintain the Skill

- Change `SKILL.md` only when routing or the stable teaching discipline changes.
- Change `references/presets.md` when one explanation class needs different sequencing.
- Change the global profile for cross-project preferences and the project profile for project progress.
- Change shared principles only when evidence supports generalization.
- Prefer replacing a superseded rule over adding another overlapping rule.
- Keep full lesson transcripts out of durable state, and keep private project state out of the tracked Skill distribution.
