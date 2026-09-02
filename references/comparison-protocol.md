# Baseline vs Xunxun Comparison Protocol

Compare the same explanation task with and without Xunxun while keeping other conditions as similar as practical. The goal is transparent human review, not a claim of causal proof from one pair.

## Conditions

- **Baseline** — the agent receives the task and source material but cannot read Xunxun, its references, or a learner profile.
- **Treatment** — the agent receives the same task and source material with Xunxun enabled. State whether it uses the neutral template or a named local profile.

Keep fixed where possible:

- model and reasoning effort;
- system/developer instructions unrelated to Xunxun;
- tools and permissions;
- repository commit and working-tree state;
- prompt wording and attachments;
- fresh-session context window;
- run date range.

Use separate fresh sessions so one run cannot learn from the other. If model or environment drift cannot be controlled, disclose it.

## Case lifecycle

```text
draft → baseline run → treatment run → human review → accepted/rejected → optional public demo
```

Store the raw comparison in `evals/`. Do not edit weak outputs to make either side look better.

## Human review

Define the learning objective and rubric before revealing which output used Xunxun where practical. Review at least:

- correctness and definition boundaries;
- unsupported terminology handling;
- mental-model coherence;
- example usefulness;
- system value and counterfactual explanation;
- evidence and uncertainty;
- cognitive load and unnecessary detours;
- ability to support the likely next question.

Record concrete evidence, not only “A feels better.” One pair is illustrative. Repeat important cases or vary the topic before generalizing.

## Public demo promotion

Promote a reviewed case into `examples/` only when:

- the prompt and outputs can be published safely;
- private learner-profile contents are absent;
- model/config differences are disclosed;
- the human review explains both improvements and regressions;
- the case is representative rather than cherry-picked solely for a large win.

Keep rejected or ambiguous cases in `evals/`; they are evidence for improving the Skill even when they are not showcase material.
