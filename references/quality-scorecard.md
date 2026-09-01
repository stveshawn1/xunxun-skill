# Explanation Quality Scorecard

Use this for substantial changes to Xunxun’s presets or feedback-learning method. It evaluates observable teaching behavior, not prose style alone.

## Scenarios

Run at least these cases:

1. one standalone technical concept;
2. one supplied file or bounded reference;
3. one unfamiliar codebase or subsystem;
4. one negative-feedback recovery that requires a genuinely different explanation;
5. one transfer check where the learner applies the model to a new example.

Where independent agents are available and authorized, one agent teaches and another scores from the request, response, relevant evidence, and this rubric.

## Dimensions

| Dimension | Weight | Evidence |
|---|---:|---|
| Definition accuracy | 20 | Correct category, boundaries, and nearby distinctions |
| Preset fit | 15 | Structure matches concept/reference/codebase request |
| Mental-model coherence | 20 | Details reconnect to a reusable whole |
| Evidence and honesty | 15 | Sources, inference, analogy, and limitations are distinguished |
| Feedback adaptation | 20 | The retry changes the failed explanatory variable and resolves the issue |
| Personalization discipline | 10 | Personal preferences stay local; shared principles are not overgeneralized |

## Passing rule

A revision passes when it scores at least 80/100, has no zero in definition accuracy, evidence/honesty, or feedback adaptation, and performs no worse than the previous version on any scenario. Preserve the previous version when the candidate regresses.

Self-scoring is a development hint, not validation. Record concrete failures and change only rules supported by them.
