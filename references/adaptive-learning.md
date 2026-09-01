# Adaptive Explanation Learning

Adapt explanations from longitudinal behavioral evidence without pretending that an ordinary conversation identifies causal effects.

## Causal frame

At a relevant decision point `t`:

- **context** `x_t` — topic, difficulty, learner history, current confusion, and active preset;
- **treatment** `a_t` — one deliberate change to the explanation method;
- **observed outcome** `y_t` — the learner’s subsequent relevant behavior;
- **counterfactual** — what would have happened under another explanation, which is normally unobserved.

This is inspired by single-case repeated-measure designs and contextual bandits, not a randomized experiment. Topic difficulty, prior knowledge, fatigue, model quality, and concurrent treatment changes can confound observations. Record causal hypotheses and directional evidence; do not claim proof or fabricate numerical effect sizes.

Useful theoretical lenses:

- Single-case designs: repeated observations of one learner across baseline and treatment phases — <https://pmc.ncbi.nlm.nih.gov/articles/PMC10601531/>.
- Micro-randomized trials: repeated decision points, proximal outcomes, and time-varying moderation — <https://www.ambujtewari.com/research/klasnja15microrandomized.pdf>. Xunxun does not randomize explanations by default.
- Contextual bandits: choose an action from context, observe only the selected action’s reward, and update the policy — <https://arxiv.org/abs/1003.0146>.

## Detect a likely mismatch

Infer explanation fit from the sequence, not one phrase in isolation.

### Evidence for understanding

- The learner correctly applies the distinction to a new example.
- The learner predicts the next step or explains the mechanism back in their own words.
- Follow-ups move deeper without returning to the same unresolved premise.
- The learner corrects an earlier misconception using the new model.
- An explicit endorsement is followed by behavior consistent with understanding.

### Evidence against the current explanation

- The learner repeats essentially the same question or returns to the same premise.
- The next question reveals misuse of the central distinction.
- The learner explicitly rejects the analogy, order, detail level, or evidence.
- Follow-ups become more syntactic while the system role remains confused.
- The learner abandons the path immediately after an unexplained jargon chain.

### Ambiguous signals

- “OK,” silence, or topic change.
- Continued questions without evidence of whether they are deeper or repetitive.
- Faster or shorter replies without a reliable latency baseline.
- Agreement that merely mirrors the explanation.

Do not equate continued engagement with satisfaction or topic change with failure.

## Propose a treatment

Diagnose the smallest plausible mismatch, then choose a low-cost delta from the active baseline.

| Suspected mismatch | Candidate treatment |
|---|---|
| Missing prerequisite | Define or teach the prerequisite, then reconnect |
| Abstraction too high | Concrete failure/example before formal model |
| Example obscures rule | Definition, boundary, and non-example before examples |
| Layers conflated | Explicit side-by-side distinction or object map |
| Mechanism unclear | Trace control/data/state flow step by step |
| Role unclear | Re-anchor the item in the whole system |
| Detail overload | Smaller lesson unit and one coherent concept cluster |
| Evidence skepticism | Separate source, inference, analogy, and uncertainty |
| Representation mismatch | Switch prose ↔ table ↔ diagram ↔ executable example |

Prefer one changed dimension at a time where it does not degrade teaching. If the learner proposes several changes:

1. split them into separate treatments;
2. order them by which addresses the earliest blocking gap;
3. apply sequentially and observe after each;
4. if they must be bundled, mark a compound treatment and do not attribute the outcome to one component.

Do not randomly serve an inferior explanation merely to explore. Conservative exploration is acceptable only among plausible, low-cost alternatives when evidence is weak.

## Predict proximal signals

Before or immediately after applying a treatment, record what should change in the next one to three relevant turns.

Examples:

- concrete-first treatment → learner uses the example to state the formal distinction;
- layer map treatment → learner stops conflating class, instance, and registry;
- smaller lesson treatment → follow-up targets the next concept rather than reopening several earlier ones;
- evidence treatment → disagreement shifts from source uncertainty to the actual design tradeoff.

Predictions make later interpretation less vulnerable to hindsight.

## Update treatment state

Use qualitative confidence; the data rarely justify numeric probabilities.

```text
candidate → active → supported
                   → contextual
                   → contradicted
                   → superseded
```

- **candidate** — plausible but untried.
- **active** — currently applied; proximal signals pending.
- **supported** — repeated compatible behavior, or explicit evidence plus successful transfer.
- **contextual** — useful only for a topic, difficulty level, or preset.
- **contradicted** — behavior repeatedly moves opposite the prediction.
- **superseded** — a later, more precise treatment explains the evidence better.

One positive turn raises confidence but rarely establishes a general preference. One negative turn weakens a treatment but may reflect a harder topic. Prefer patterns across comparable contexts.

## Local treatment ledger

Maintain one compact ledger per learner in `learner-profiles.local.md`:

```markdown
### Stable preferences
- Treatment: definition before analogy
  Scope: unfamiliar framework concepts
  Confidence: high
  Evidence: repeated successful transfer across two topics

### Contextual preferences
- Treatment: concrete failure before formal model
  Scope: runtime/trust-boundary topics
  Confidence: medium

### Active treatments
- ID: T-004
  Context: explaining runtime type erasure
  Baseline: definition → intuition → example
  Delta: move executable failure example before mechanism
  Prediction: learner distinguishes static typing from runtime validation in next relevant turn
  Observations: pending
  Confounders: new topic also introduced JSON parsing
  Status: active

### Contradicted or superseded
- Treatment: always start with examples
  Result: contradicted; examples obscured definitions in architecture topics
```

After evidence accumulates, fold completed treatments into stable/contextual preferences and retain only a concise evidence summary. Do not keep an append-only diary of every message.

## Observe without interrogating

Usually continue the substantive lesson and infer fit from behavior. Do not routinely ask “Did that help?” or require the learner to manage the experiment.

Ask directly only when:

- two plausible diagnoses imply materially different, costly paths;
- the next behavior remains ambiguous after a low-cost trial;
- the user requests explicit control over the teaching method;
- a persistent profile change would be consequential and evidence is conflicting.

Ask about the actual uncertainty, for example “Are you stuck on why the object exists, or on how the Proxy returns it?” This produces more useful evidence than a satisfaction rating.

## Privacy and authorization

- Personal treatment ledgers remain in the gitignored local profile.
- Never commit, push, upload, or create telemetry from the ledger.
- Never infer stable identity from account or machine metadata.
- Shared principles contain no learner identifiers or raw personal examples.
- The Skill has no cross-device identity or synchronization backend; do not imply otherwise.
