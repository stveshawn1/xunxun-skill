# Explanation Presets

Choose the narrowest preset that matches the user’s input. Transition between presets when the lesson crosses a real seam; do not force one preset over the entire conversation.

## Concept preset

Use for a term, mechanism, command, language feature, or design idea without a necessary repository.

1. Define the concept and its category.
2. Name the nearest concepts it is commonly confused with.
3. Give a minimal intuitive model.
4. Test the model with one concrete example and one boundary/non-example when useful.
5. Explain why the concept exists and what happens without it.
6. Add formal mechanics, history, syntax, or implementation only when they improve the user’s goal.
7. End with a compact reusable distinction.

Default emphasis: definition and distinctions. Increase examples, analogy, formalism, or exercises according to the learner profile.

## Reference preset

Use when the user supplies or points to code, a file, document, diagram, configuration, error, or other bounded material.

1. Identify what kind of artifact it is and its role in the surrounding system.
2. State what must be understood before reading details.
3. Identify producers, consumers, imports, exports, state, and side effects where applicable.
4. Divide the artifact into meaningful regions instead of narrating every line uniformly.
5. Trace one real path through it.
6. Read critical regions line by line; group mechanical lines.
7. Explain non-obvious syntax at the point it matters.
8. Reconnect the artifact to its system role and limits.

Default emphasis: role before contents. Do not mistake a type declaration, configuration file, or test for runtime behavior without tracing its consumer.

## Codebase preset

Use for a repository, product, subsystem, or multi-file architecture.

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
