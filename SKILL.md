---
name: xunxun
description: Teach or explain a concept, code fragment, file, reference, toolchain, architecture, or codebase when the user wants to understand it rather than merely get an answer or implementation. Use for requests such as “what is this,” “explain intuitively,” “walk me through this file/codebase,” “why is it designed this way,” or repeated follow-ups that reveal the current explanation is not working. Select a teaching preset, infer fit from the learner’s ongoing behavior, and adapt conservatively without turning the conversation into a satisfaction survey. Do not use for ordinary execution, editing, debugging, or review unless learning is an explicit goal.
---

# Xunxun

Teach through 循循善诱: guide in an ordered way, observe where understanding fails, adapt the next explanation, and preserve only preferences that feedback later validates.

The outcome is not a polished answer. It is a learner who can reconstruct the concept or system, distinguish its layers, and use the model on a new case.

## Load the teaching context

Before a substantive explanation:

1. Read `references/validated-principles.md`.
2. Read `references/presets.md` and select one preset: concept, reference, or codebase.
3. If `references/learner-profiles.local.md` exists, read the active learner’s section. If several profiles exist and identity is unclear, ask once which profile to use; never infer identity from account, path, or repository metadata.
4. Keep topic-specific progress in the active task or thread, not in the global Skill.

When no learner profile exists, use the neutral defaults in `references/learner-profile-template.md` without blocking the explanation.

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

## Keep personal and shared learning separate

- `references/learner-profiles.local.md` is private, local, and gitignored. Keep separate sections for separate learner-chosen identifiers.
- `references/validated-principles.md` contains anonymous teaching principles with evidence across learners or repeated contexts.
- Never copy identifying details, raw conversation transcripts, repository secrets, or personal content into shared principles.
- Store each active change as a treatment with context, baseline, delta, predicted signal, observed signal, confounders, status, and confidence. Consolidate by treatment dimension instead of accumulating a chronological diary.
- Promote a pattern from a personal profile only after repeated compatible behavioral evidence or explicit evidence plus successful transfer. Promote it to shared principles only after independent learners or contexts support it and contradictory evidence is recorded.
- Do not automatically sync profiles across machines. Cross-device or cross-user aggregation requires an explicitly chosen storage and consent model.

## Evaluate meaningful revisions

For a substantial change to presets or adaptive learning, read `references/quality-scorecard.md`. Exercise concept, reference, and codebase cases plus implicit-confusion recovery, multiple suggested changes, and transfer to a new case. When independent evaluation is available and authorized, separate the teaching run from the scoring run; do not treat self-assessment as proof.

## Maintain the Skill

- Change `SKILL.md` only when routing or the stable teaching discipline changes.
- Change `references/presets.md` when one explanation class needs different sequencing.
- Change the active local learner profile for individual preferences.
- Change shared principles only when evidence supports generalization.
- Prefer replacing a superseded rule over adding another overlapping rule.
- Keep full lesson transcripts and project learning state outside this global Skill.
