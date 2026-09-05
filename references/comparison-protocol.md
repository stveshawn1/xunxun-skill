# Baseline vs Xunxun Comparison Protocol

Compare the same explanation task with and without Xunxun while keeping other conditions as similar as practical. The goal is transparent human review, not a claim of causal proof from one pair.

Choose one estimand before writing prompts:

- **Pure Skill effect** — disable unrelated optional Skills in both arms; only Xunxun availability differs.
- **Ecosystem effect** — preserve the normal Skill set and treat routing or composition changes as part of the outcome.
- **Longitudinal effect** — give both arms the same scripted follow-ups; state accumulation inside one sequence is intentional, while sequences start fresh.

Do not average these lanes into one result.

## Conditions

- **Baseline** — the agent receives the task and source material but cannot read Xunxun, its references, or global/project `.xunxun/profile.md` files.
- **Treatment** — the agent receives the same task and source material with Xunxun enabled. State whether it uses neutral defaults, a global profile, a project profile, or both.

Keep fixed where possible:

- model and reasoning effort;
- system/developer instructions unrelated to Xunxun;
- tools and permissions;
- repository commit and working-tree state;
- prompt wording and attachments;
- fresh-session context window;
- run date range.

Use one natural user question per independent item. Do not bundle several concepts into one answer unless the bundled experience itself is under test. Use raw or realistically supplied context; do not encode Xunxun's desired definitions, distinctions, causal chain, examples, or transfer language into the Baseline prompt.

Model sampling is nondeterministic. Repeat important items enough to observe direction and variance; use a small pilot first to verify that prompts and grading leave headroom before scaling the run.

Use separate fresh sessions so one run cannot learn from the other. If model or environment drift cannot be controlled, disclose it.

## Case lifecycle

```text
draft → baseline run → treatment run → human review → accepted/rejected → optional public demo
```

Store each new experiment in a separate directory under `evals/`; do not reuse old outputs after changing the model, prompts, sources, or Skill. Do not edit weak outputs to make either side look better.

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

Report required-fact coverage and unsupported inferences separately. If using a combined score, disclose its formula and label it as combined, not as coverage. Score each independent question against a question-specific factual checklist before applying general teaching-quality dimensions. Include a transfer or misconception check when the claimed outcome is learner understanding, not merely polished prose. Treat saturated scores as a failed measurement design, not proof that both conditions are perfect.

## Public demo promotion

Promote a reviewed case into `examples/` only when:

- the prompt and outputs can be published safely;
- private learner-profile contents are absent;
- model/config differences are disclosed;
- the human review explains both improvements and regressions;
- the case is representative rather than cherry-picked solely for a large win.

Keep rejected or ambiguous cases in `evals/`; they are evidence for improving the Skill even when they are not showcase material.
