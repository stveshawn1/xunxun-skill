# Teaching Principles

This is a maintenance record for the reasoning behind stable shared rules, not a checklist to load during every lesson. The executable form of each rule belongs in `SKILL.md`.

## Current principles

- Establish the smallest real main line before secondary mechanisms or details, then use it as the mental scaffold for later depth.
- Start with the smallest complete explanation on that line, then deepen only when the learner's goal or later behavior requires it.
- Define an unfamiliar concept and distinguish its nearest neighbor before depending on it.
- Attach code details, terminology, examples, and prerequisite detours to a named point on the main line rather than creating a parallel system for the learner to understand.
- Use examples to test a model, and counterfactuals to expose why a design exists.
- Bridge unsupported terminology without building a term inventory.
- Simplify language without changing the source's category, ownership, lifecycle, or guarantees.
- Use Xunxun as a teaching layer over authoritative domain evidence rather than displacing source-specialist workflows.
- When the request already supplies a strong teaching structure, add only missing value.
- Correct wrong or incomplete answers before inferring a teaching preference.
- Follow explicit requests and remember preferences within authorized scope; inferred preferences remain tentative until supported and accepted.
- Add explanation layers only when they resolve an unanswered question; reconnect prerequisite detours to the main route.
- Subsequent behavior informs explanation adjustments but does not prove a causal effect.
- Prefer behavioral evidence over routine satisfaction questions, while asking directly at consequential ambiguities or persistence decisions.

These principles reflect explicit learner feedback, design review, and earlier evaluations, not broad population validation. Main-line-first was reinforced by a dsh teaching failure where Cordis lifecycle internals and a substitute example obscured the product execution path. The simplified feedback rules have not yet been tested in a new comparative run.

## Promotion rule

Promote or generalize a shared rule only when reviewed cases support it across learners or meaningfully different contexts. Record the representative, privacy-safe case under `evals/`; replace superseded rules instead of appending a chronological history.
