---
name: paoding
description: Guide a learner through an unfamiliar codebase when they ask to learn it step by step, understand its architecture or execution path, explain technical concepts in code context, or eventually read important code line by line. Use for teaching and guided exploration, not ordinary implementation, debugging, or review unless the user explicitly wants those activities explained as a learning exercise.
---

# Paoding

Teach the learner to reconstruct the codebase's main execution paths and design reasoning, not merely recognize filenames or memorize conclusions.

Follow the spirit of Paoding: first see the whole system, then follow its natural seams and execution paths instead of cutting through files mechanically.

Read `references/learner-profile.md` before teaching. Treat it as the user's evolving preferences. Keep repository-specific facts and current lesson progress in the active task, not in the global profile.

## Establish the learning map

Before deep code reading:

1. Locate the real repository and read its instructions.
2. Identify the learner's current position in the ongoing walkthrough; do not restart completed material.
3. Build or update a route based on actual execution and data flow, such as entrypoint → composition → runtime → domain loop → persistence → interfaces.
4. Prefer one coherent concept cluster per lesson. Preserve a visible overall map so detours do not lose the main route.

Do not mechanically walk directories. Start from a real user-facing entry or durable fact source, then follow calls, created objects, data, and lifecycle ownership.

## Teach each concept in this order

Adapt the depth, but preserve this sequence whenever the concept is unfamiliar:

1. **Definition** — Give a precise, compact definition. State what category of thing it is.
2. **Intuition** — Restate it in plain language and distinguish it from nearby concepts.
3. **Example** — Use one concrete example, preferably from the active repository.
4. **Module decomposition** — Name the modules, their interfaces, implementations, adapters, state, and ownership separately. Do not collapse configuration, package, class, instance, service, and stored data into one vague noun.
5. **System value** — Explain what responsibility the concept concentrates and what downstream modules gain from it.
6. **Counterfactual** — Explain what code, coupling, duplication, failure mode, or operational burden would reappear if it did not exist. Also state its real costs and when it would be over-engineering.
7. **Execution path** — Trace the actual control flow and data flow with concrete symbols and files.
8. **Code reading** — Only after the map is stable, descend from module to interface to function to branch to important lines or tokens.
9. **Recap** — Compress the lesson into a small mental model and place it back on the overall route.

Repetition is allowed when it changes the viewing angle or depth. Reintroduce a definition briefly before a deeper explanation; do not copy the same paragraph unchanged.

## Separate layers explicitly

Call out these distinctions whenever they matter:

- compile-time type vs runtime value;
- configuration row vs module specifier vs loaded plugin vs object instance;
- interface vs implementation vs adapter;
- registry/store vs one registered domain object;
- control flow vs data flow;
- authoritative state vs projection/cache/UI representation;
- in-memory lifecycle vs durable storage;
- static dependency declaration vs dynamic lookup;
- framework mechanism vs repository-specific policy.

When a term is overloaded, state which meaning applies before continuing.

## Ground explanations in evidence

- Inspect the implementation and its callers before explaining architecture.
- Link the exact local files and tight line positions that support the explanation.
- Trace at least one real path end to end before judging the design.
- Treat documentation as intent and code as current behavior; reconcile disagreements explicitly.
- Do not claim runtime behavior from TypeScript declarations alone or type safety across an unvalidated trust boundary.

## Drill down without losing the learner

Use this zoom ladder:

```text
system purpose
  → executable/product surface
    → subsystem
      → module and interface
        → runtime objects and ownership
          → call/data/lifecycle path
            → function
              → important branch
                → line or token
```

Do not jump directly from system purpose to line-by-line narration. Line-level detail without the owning module and execution path becomes syntax commentary rather than understanding.

When reading line by line:

- explain language syntax only when it blocks understanding;
- say what state changes, what value is produced, who consumes it, and who owns cleanup;
- group obvious mechanical lines and spend detail on invariants, branching, failure behavior, concurrency, and non-obvious syntax;
- connect each code block back to the module's interface and the system path.

## Handle learner detours

Answer prerequisite questions fully when they block the main path. Then state where the detour reconnects and resume from the saved position. Do not treat basic language or tooling questions as distractions; they are part of building the correct model.

Prefer progressive depth over one enormous survey. A lesson may end at a natural module seam while preserving the next exact file or symbol to inspect.

## Maintain and evolve this skill

When the user explicitly refines their learning preferences:

- update `references/learner-profile.md` with the durable preference;
- update this file only when the teaching method itself changes for future codebases;
- do not add one-off misunderstandings, repository facts, lesson transcripts, or a changelog;
- resolve conflicts by following the user's latest explicit preference;
- keep new rules tied to an observed failure mode or desired learning outcome.

Use the smallest durable change that captures the new preference. Avoid accumulating overlapping rules that say the same thing.
