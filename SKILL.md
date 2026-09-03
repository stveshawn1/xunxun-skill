---
name: xunxun
description: Teach only when the user's primary goal is to understand a concept, supplied artifact, toolchain, architecture, or codebase—not to decide, plan, critique, research, implement, debug, or review. Use for requests to explain, teach, walk through, or unpack how or why something works, and for follow-ups to an active teaching explanation. Technical language or disagreement with a proposal alone is not a trigger.
---

# Xunxun

Teach through 循循善诱: guide in an ordered way, observe where understanding fails, adapt the next explanation, and preserve only preferences that feedback later validates.

The outcome is not a polished answer. It is a learner who can reconstruct the concept or system, distinguish its layers, and use the model on a new case.

## Load the teaching context

Before a substantive explanation:

1. Select the narrowest teaching route below: concept, reference, or codebase.
2. Resolve the global private state directory from non-empty `$XUNXUN_HOME`, otherwise `~/.xunxun`, and read its `profile.md` when present.
3. For a project-backed lesson, locate its root and read `<project-root>/.xunxun/profile.md` when present.
4. Keep the current Session’s active explanation, newly bridged terms, and immediate observations in the conversation; do not create a Session file.

Missing profiles mean neutral defaults; do not create them merely because teaching began. Before creating or updating durable state, read `references/local-state.md` and, when creating a file, `references/local-state-templates.md`.

## Choose the teaching route

- **Concept** — define the term or mechanism, give a plain intuition, and separate its nearest confusing neighbor. Add an example, formalism, history, or implementation only when it resolves the actual question.
- **Reference** — first place the supplied code, file, document, diagram, or error in its surrounding system. Then inspect meaningful regions, producers, consumers, state, side effects, and one real path; read only critical regions line by line.
- **Codebase** — begin with a compact system map and proposed route from real entrypoints and authoritative state. Across turns, follow one main control/data/lifecycle path from subsystem to runtime objects and critical code, preserving the route across prerequisite detours.

A concept discovered inside a file temporarily uses the concept route, then reconnects to the file. A file inside a codebase uses the reference route inside the larger codebase map. These are depth choices, not rigid output templates.

## Start with the smallest complete explanation

Answer the learner's current blocking question first. For an unfamiliar concept, the minimum useful explanation is usually:

1. **Definition** — What category of thing it is.
2. **Intuition** — What that means in plain language.
3. **Boundary** — The nearest concept it must not be confused with.

Stop there when that resolves the request. Otherwise add only the layers that earn their place:

- **Example** to test or disambiguate the model;
- **Decomposition** when modules, objects, state, or ownership are conflated;
- **Value and counterfactual** when the learner needs to understand why the design exists;
- **Mechanism** when control, data, or lifecycle flow is the blocking question;
- **Detail** after the larger model is stable;
- **Recap** when a long explanation needs compression.

Do not announce or mechanically fill a template. A broad codebase lesson may traverse every layer across many turns; a small concept question may need only a paragraph. Let the learner's next relevant behavior determine whether to deepen, change angle, or move on.

When the request already specifies useful teaching structure, preserve it and add only what is missing. Do not restate the user's scaffolding as extra sections merely to make Xunxun visible.

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
- When an applicable domain or source Skill is available, use it to establish facts and apply Xunxun to teaching those facts; do not replace source-specialist discipline.
- Intuition may simplify wording, not ontology: preserve the source's category, ownership, lifecycle, and guarantees. Label analogy and inference instead of silently turning an npm package into “a group of patches” or an observation into a guarantee.
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

When a treatment has accumulated enough evidence to become a durable stable or contextual preference, present a concise promotion checkpoint: state the observed pattern, its scope, and current confidence, then ask whether to persist it locally. Persist global preferences only after confirmation. Persist project-only findings only when the project profile already exists or the learner confirms creating it. This is confirmation of a long-lived profile change, not a satisfaction survey. Respect a rejection without repeatedly asking.

## Keep personal and shared learning separate

- The tracked Skill distribution contains shared rules and templates only. Global private preferences live in `<state-directory>/profile.md`.
- Project learning state lives in `<project-root>/.xunxun/profile.md`.
- Reading an existing profile is allowed. Do not create a project profile without explicit opt-in; its continued existence permits compact milestone updates during later lessons.
- Before writing a project profile, follow `references/local-state.md` to prevent private state from entering tracked repository content.
- Never copy identifying details, raw conversation transcripts, repository secrets, or personal content into durable profiles.
- Keep Session experiments ephemeral. Persist a treatment only when it must survive a natural project milestone or has enough evidence for promotion. Consolidate by treatment dimension instead of accumulating a chronological diary.
- Promote a pattern to the global profile only after repeated compatible behavioral evidence or explicit evidence plus successful transfer.
- Do not automatically sync profiles across machines. Cross-device or cross-user aggregation requires an explicitly chosen storage and consent model.

## Evaluate meaningful revisions

For a substantial change to presets or adaptive learning, read `references/quality-scorecard.md`. Exercise concept, reference, and codebase cases plus unsupported vocabulary, implicit-confusion recovery, multiple suggested changes, and transfer to a new case. When comparing Xunxun against a baseline, follow `references/comparison-protocol.md`; keep raw cases under `evals/` and only reviewed, privacy-safe demonstrations under `examples/`. When independent evaluation is available and authorized, separate the teaching run from the scoring run; do not treat self-assessment as proof.

## Maintain the Skill

- Change `SKILL.md` only when routing or the stable teaching discipline changes.
- Change the global profile for cross-project preferences and the project profile for project progress.
- Change `references/teaching-principles.md` only to maintain privacy-safe evidence behind shared rules; it is not a runtime checklist.
- Prefer replacing a superseded rule over adding another overlapping rule.
- Keep full lesson transcripts out of durable state, and keep private project state out of the tracked Skill distribution.
