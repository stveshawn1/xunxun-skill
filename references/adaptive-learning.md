# Adapt Explanations from Feedback

Help the learner continue the lesson. Keep only enough context to understand why the explanation changed and whether later behavior supports using it again.

## Correct before adapting

When a learner objects or remains confused, check accuracy, source support, whether the question was answered, and missing prerequisites first. Repair the answer before inferring a teaching preference. Correcting an unsupported claim is not evidence of a special preference for accuracy.

## Explicit requests and inferred preferences

- Follow an explicit request immediately. The current request overrides stored preferences.
- If the learner explicitly asks to remember it, persist within that scope using `local-state.md`; do not ask for the same authorization again.
- Otherwise keep a suspected preference in the Session. Try a useful adjustment and observe relevant follow-ups.
- A repeated pattern may justify proposing a concise local preference. Explain its scope and evidence, then ask whether to retain it if persistence has not already been authorized.
- Replace or remove a preference the learner rejects. Do not retain conflicting rules.

Explicit choice is sufficient to honor a preference, but does not prove that it improves learning.

## Choose a useful adjustment

| Current obstacle | Possible adjustment |
|---|---|
| Missing prerequisite | Explain it briefly, then reconnect to the main path |
| Too abstract | Use one concrete example |
| Example hides the rule | State the definition and a distinguishing boundary |
| Objects or layers conflated | Compare their roles side by side |
| Mechanism unclear | Trace one real execution or state-change sequence |
| Detail overload | Address one coherent question, then stop |
| Representation unhelpful | Switch to a table, diagram, prose, or executable example |

Use the smallest change that addresses the obstacle. Several changes can be applied together when needed; do not make the learner wait through separate experiments.

## Read feedback conservatively

Correct application to a new example or correct use of a previously confused distinction supports understanding. Repeating the same mistaken premise or explicitly rejecting an analogy suggests the explanation needs repair.

“OK,” silence, a topic change, and continued questioning alone are ambiguous. Deeper questions may show progress. Do not infer satisfaction or failure from these signals alone.

Keep a brief Session note only when useful: what changed, why, and what later behavior suggested. There is no required status vocabulary, numerical confidence, or fixed observation window.

Ask about the actual obstacle when ambiguity would materially change the next explanation, rather than routinely asking “Are you satisfied?”

## Keep durable state small

Follow `local-state.md`. Global state holds preferences the learner has asked or agreed to retain. Project state holds where the lesson stopped, remaining gaps, and the next step; include established understanding or a scoped adaptation only when useful for continuity. Temporary guesses stay in the Session. Never upload private state.

For example, after supporting feedback and permission to retain it:

> For runtime mechanisms, start with one concrete failure example. The learner requested this and later correctly distinguished static checking from runtime validation.

The observation supports reuse in that context; it does not establish a universal learning style.

## Theoretical boundary

Contextual bandits and single-case designs motivate choosing an adjustment from context and learning from subsequent observations. Xunxun does not implement a bandit algorithm or run randomized trials. The alternative explanation's outcome is unobserved; topic difficulty, prior knowledge, and other changes may explain apparent improvement. Use these ideas to avoid overclaiming, not to impose experiment bookkeeping on an ordinary lesson.

Background: [contextual bandits](https://arxiv.org/abs/1003.0146), [single-case designs](https://pmc.ncbi.nlm.nih.gov/articles/PMC10601531/).
