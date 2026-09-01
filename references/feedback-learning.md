# Feedback Learning

Use feedback to adapt explanations without overfitting one moment or leaking personal information.

## Feedback entrance

The explicit form is:

```text
反馈：没懂的是…… / 不适合的是…… / 希望改成……
```

Equivalent feedback includes statements such as “I still don’t understand,” “too abstract,” “too many examples,” “define it first,” “this analogy is misleading,” or “I disagree with that explanation.”

## Feedback loop

Process each clear feedback item through these stages:

1. **Observation** — Preserve the user’s actual complaint without converting it immediately into a universal preference.
2. **Diagnosis** — Classify the likely mismatch: missing prerequisite, inaccurate definition, abstraction level, order, pacing, terminology, example fit, analogy fit, evidence, visual structure, or excessive detail.
3. **Trial** — Change one or a small number of variables and re-explain. A “simpler” rewrite that keeps the same structure is not a new trial.
4. **Validation** — Ask or infer from a successful follow-up whether the new form resolved the issue.
5. **Personal promotion** — Record a durable preference after explicit confirmation or repeated success for that learner.
6. **Shared promotion** — Anonymize and generalize only after the pattern succeeds across independent learners or contexts and conflicting evidence is retained.

## Explanation variables

Track preferences using concrete variables instead of personality labels:

- definition-first vs example-first;
- concrete-to-abstract vs abstract-to-concrete;
- examples per concept;
- analogy tolerance;
- formalism and notation level;
- pacing and lesson size;
- syntax detail;
- diagrams/tables/prose preference;
- counterfactual and tradeoff depth;
- historical context;
- exercises or retrieval checks;
- confidence/evidence disclosure;
- desired recap format.

## Local profile format

Use a separate section per learner-chosen identifier in `learner-profiles.local.md`:

```markdown
## learner: <identifier>

### Validated preferences
- ...

### Rejected approaches
- ...

### Pending hypotheses
- Observation: ...
  Trial: ...
  Result: pending

### Effective explanation patterns
- Context: ...
  Pattern: ...
  Evidence: ...
```

Keep concise summaries, not transcripts. Remove superseded preferences rather than preserving a changelog.

## Authorization and privacy

- `反馈：` authorizes a local update to the active learner section only.
- Natural feedback without the prefix authorizes immediate conversational adaptation, not silent persistence; offer the proposed durable update.
- Never commit or push local profiles.
- Never infer stable identity from GitHub accounts, machine usernames, paths, email, or repository metadata.
- Never upload feedback or create telemetry without explicit consent and a declared destination.
- Shared principles contain no learner identifiers or raw personal examples.

## Honest limitation

The Skill has no identity service, database, or synchronization backend. It can personalize within a writable installation and multiple explicitly selected local profiles. Cross-device learning and automatic aggregation across installations require a separately designed consent, identity, and storage system; do not imply they already exist.
