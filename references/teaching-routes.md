# Practical teaching routes

These are examples of how the three routes adapt to a learning goal, not additional modes or mandatory output sections. Choose only the relevant treatment. Use the supplied material when present; ask for a missing artifact only when it prevents a grounded explanation.

## Concept: distinguish or calculate

**Confused neighbors.** Define each category, then apply both concepts to the same small example. Identify the condition under which their behavior differs. Avoid listing unrelated properties. If the learner needs to choose a solution rather than understand a distinction, respect the teaching trigger boundary.

Example request: `Explain concurrency versus parallelism.`

Useful result: the learner can distinguish overlapping task progress from simultaneous execution. A scheduler architecture tour is unnecessary unless requested.

**Formula or algorithm.** Explain the question it answers, what its inputs and output mean, and the units or assumptions. Introduce symbols as needed, then work one small example when useful. Distinguish exact relationships from approximations; do not replace the mechanism with an analogy. Derive the formula only when the derivation is the question or resolves a gap.

Example request: `Explain this weighted-average formula.`

Useful result: the learner can trace how a changed weight affects the result. Do not add a quiz unless requested or needed to clarify a consequential ambiguity.

## Reference: follow what the artifact actually does

**Paper or article.** Identify the central question and argument. Connect the proposed method or reasoning to the evidence and conclusion. Explain relevant figures or equations in place. Distinguish the author's claims, measured results, assumptions, and your inference. State when only an abstract or excerpt is available; do not imply a full-paper review.

Example request: `Walk me through this paper's central argument.`

Useful result: the learner can say what evidence supports the central claim and where it stops. Do not summarize every section equally.

**Configuration.** Find who loads it, how explicit values combine with defaults or overrides, and which runtime behavior changes. Trace one meaningful setting to its consumer. If the loader is unavailable, distinguish documented behavior from verified implementation. Never imply that parsing YAML alone creates a running object.

Example request: `What does this plugin configuration start?`

Useful result: the learner can connect a setting to its runtime effect. Avoid an inventory of every option.

**Function or module.** Locate its caller, inputs, outputs, and meaningful side effects. Trace one concrete input through the relevant branches; explain critical lines after establishing the role. Show a failure path only when it changes the learner's understanding of the contract. Mark illustrative execution separately from actually executed checks.

Example request: `Trace one request through this handler.`

Useful result: the learner can follow where the input goes and what observable result is produced.

## Codebase: execution and ownership

**Main execution path.** Choose one real user operation and follow its entry, core processing, authoritative state, and visible result. Keep the initial map compact; introduce supporting modules where the path reaches them. Defer unrelated entrypoints and internal alternatives. Preserve the current location and next step across prerequisite detours.

Example request: `Guide me through this repository from its main entry point.`

**Object lifecycle.** When the confusion concerns runtime objects, follow who creates the instance, who retains or resolves it, when it is used, and who disposes of it. Separate class definitions, instances, registries, and durable records. Explain only lifecycle guarantees supported by the source. This focus can also apply to a single supplied file without expanding to the whole repository.

Example request: `Who creates and disposes of this service?`

Useful result: the learner can locate the object within the execution path and identify its owner. Do not promise cleanup or restart behavior merely because a dependency is declared.

## Finish or reconnect

End when the current question is answered with usable distinctions. A small question may need one paragraph; a repository walkthrough may continue over many turns. If a prerequisite required a detour, reconnect it to the exact point it explains. Do not require every lesson to include examples, diagrams, counterfactuals, or a comprehension test.
