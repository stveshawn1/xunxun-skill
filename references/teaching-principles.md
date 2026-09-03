# Teaching Principles

This is a maintenance record for the reasoning behind stable shared rules, not a checklist to load during every lesson. The executable form of each rule belongs in `SKILL.md`.

## Current principles

- Start with the smallest complete explanation, then deepen only when the learner's goal or later behavior requires it.
- Define an unfamiliar concept and distinguish its nearest neighbor before depending on it.
- Move from system role and real execution paths toward code details rather than narrating directories or lines uniformly.
- Use examples to test a model, and counterfactuals to expose why a design exists.
- Bridge unsupported terminology without building a term inventory.
- Simplify language without changing the source's category, ownership, lifecycle, or guarantees.
- Use Xunxun as a teaching layer over authoritative domain evidence rather than displacing source-specialist workflows.
- When the request already supplies a strong teaching structure, add only missing value.
- Treat explanation changes as scoped hypotheses; subsequent behavior informs them but does not prove a causal effect.
- Prefer behavioral evidence over routine satisfaction questions, while asking directly at consequential ambiguities or persistence decisions.

These principles currently reflect explicit learner feedback, design review, and the negative/ambiguous v1 evaluation, not broad population validation.

## Promotion rule

Promote or generalize a shared rule only when reviewed cases support it across learners or meaningfully different contexts. Record the representative, privacy-safe case under `evals/`; replace superseded rules instead of appending a chronological history.
