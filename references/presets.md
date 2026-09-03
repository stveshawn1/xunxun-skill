# Explanation Presets

Choose the narrowest preset that matches the user’s input. Each preset describes available depth, not sections that must all appear in one answer. Start with the smallest complete orientation, deepen only as the request or later behavior requires, and transition when the lesson crosses a real seam.

## Concept preset

Use for a term, mechanism, command, language feature, or design idea without a necessary repository.

Start with its definition/category, a plain-language intuition, and the nearest useful distinction. That is often enough for a small question.

Add a concrete example or non-example when it tests the model. Add value, counterfactual, formal mechanics, history, syntax, or implementation only when they resolve the learner's actual question. After a long explanation, end with a compact reusable distinction.

Default emphasis: definition and distinctions, with progressive depth rather than a fixed lesson shape. Increase examples, analogy, formalism, or exercises according to the learner profile.

## Reference preset

Use when the user supplies or points to code, a file, document, diagram, configuration, error, or other bounded material.

First identify what kind of artifact it is and its role in the surrounding system. Give that orientation before deciding how far to continue.

When deeper reading is useful:

1. State what must be understood before reading details.
2. Identify producers, consumers, imports, exports, state, and side effects where applicable.
3. Divide the artifact into meaningful regions instead of narrating every line uniformly.
4. Trace one real path through it.
5. Read critical regions line by line; group mechanical lines.
6. Explain non-obvious syntax at the point it matters.
7. Reconnect the artifact to its system role and limits.

Default emphasis: role before contents. Do not mistake a type declaration, configuration file, or test for runtime behavior without tracing its consumer.

## Codebase preset

Use for a repository, product, subsystem, or multi-file architecture.

Begin with a compact system map and proposed learning route; do not dump the entire repository map into the first answer.

Across subsequent turns as needed:

1. Read repository instructions and identify executable/product surfaces.
2. Build a route from real entrypoints and authoritative state, not directory order.
3. Map major subsystems and their interfaces before deep reading.
4. Follow one main execution path end to end, recording created objects, state ownership, lifecycle, errors, and persistence.
5. Preserve a visible progress map so prerequisite detours return to the correct point.
6. Zoom from system → subsystem → module → interface → runtime objects → call/data/lifecycle path → function → branch → line/token.
7. Explain architecture through both benefits and counterfactual costs.
8. Reconcile documentation, types, implementation, tests, and runtime evidence.

Default emphasis: an executable mental model. Do not mechanically inventory folders or jump to line-by-line explanation before the owning path is clear.

## Mixed requests

- A language question blocking code reading temporarily uses the concept preset, then returns to the saved codebase position.
- A file inside a codebase uses the reference preset nested under the codebase map.
- A concept discovered in a file is defined with the concept preset, then reattached to the file’s role.

The preset selects the baseline structure, not a permanent tone or learner type. The active learner profile supplies supported defaults; adaptive treatments are explicit deltas from that baseline and may be topic-specific.
