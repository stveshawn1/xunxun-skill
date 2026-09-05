# Explanation Quality Scorecard

Use this for substantial changes to Xunxun’s presets or adaptive-learning method. It evaluates observable teaching behavior and causal discipline, not prose style alone.

## Scenarios

Run at least these cases:

1. one standalone technical concept;
2. one supplied file or bounded reference;
3. one unfamiliar codebase or subsystem;
4. one implicit-confusion sequence where the learner repeats or misapplies a premise without explicitly rating the explanation;
5. one case where continued questioning is deeper engagement rather than dissatisfaction;
6. one case with several requested improvements applied together without forcing separate experiments or claiming which component caused success;
7. one transfer check where the learner applies the model to a new example.
8. one promotion checkpoint where a supported treatment is proposed for local persistence without asking for a generic satisfaction rating.
9. one explanation containing a necessary specialized term the learner has not demonstrated, testing whether a micro-gloss bridges it without derailing the lesson.
10. one explanation where current Session, project profile, or broad background already establishes a term, testing that Xunxun does not over-explain it again.
11. one cross-Session continuation that restores a compact project profile without replaying transient Session notes.
12. one overloaded term used in two projects or domains, testing that one project's profile does not leak into another.
13. one negative-routing case where the learner questions or rejects a product, strategy, or implementation proposal without asking to learn; Xunxun must not activate.
14. one natural underspecified novice question that does not request a mental model, causal chain, distinctions, or examples by name.
15. one independent concept item per fresh Session, plus a separate scripted multi-turn case where accumulation is intentional and matched across conditions.
16. an explicit request to remember a preference, followed by a conflicting current request; honor both scopes without redundant confirmation.
17. an objection to an incorrect answer; correct it without inventing a learner preference.

Where independent agents are available and authorized, one agent teaches and another scores from the request, response, relevant evidence, and this rubric.

## Dimensions

| Dimension | Weight | Evidence |
|---|---:|---|
| Definition accuracy | 15 | Correct category, boundaries, and nearby distinctions |
| Preset fit | 5 | Structure matches concept/reference/codebase request |
| Mental-model coherence | 10 | Details reconnect to a reusable whole |
| Vocabulary scaffolding | 10 | Unsupported terms receive proportional bridges; demonstrated terms are not re-taught |
| Evidence and honesty | 15 | Sources, inference, analogy, and limitations are distinguished |
| Behavioral inference | 15 | Repetition, progression, transfer, rejection, and ambiguity are distinguished |
| Treatment discipline | 15 | Correct content errors first; make a useful adjustment and interpret subsequent behavior conservatively |
| Personalization discipline | 5 | Session, project profile, and global profile stay scoped correctly; private project state is locally excluded; explicit requests to remember are honored; inferred global preferences require confirmation |
| Causal humility | 10 | No counterfactual or causal effect is claimed without identification |

## Passing rule

A revision passes when it scores at least 80/100, has no zero in definition accuracy, vocabulary scaffolding, evidence/honesty, behavioral inference, or causal humility, and performs no worse than the previous version on any scenario. Preserve the previous version when the candidate regresses.

Self-scoring is a development hint, not validation. Record concrete failures and change only rules supported by them.

Before a large run, pilot the rubric. If most untreated outputs already score near the maximum, revise the cases or item-specific checks before spending the full evaluation budget.
