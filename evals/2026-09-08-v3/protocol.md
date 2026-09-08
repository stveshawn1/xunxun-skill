# Current-guidance comparison: v3

Frozen before generation on 2026-09-08. This is a small diagnostic comparison of supplied instructions, not a study of real learner outcomes.

- Four self-contained cases; two independent generations per condition (24 answers).
- Conditions: baseline, a short teaching prompt, and the current complete runtime guidance.
- Model: gpt-6-astra, medium reasoning. Identical source, question, tool prohibition and empty temporary working directory; only supplied guidance differs.
- References are supplied inline to control access and avoid confusing loading cost with answer quality. This does not test automatic Skill discovery, selective reference loading, actual profile persistence, or full repository navigation.
- Two cases use English and two use Chinese. Two provide fixed prior-learning context; these are continuation snapshots, not independently observed multi-turn learning.
- Two independent model judges (gpt-5.6-sol and gpt-5.5, high reasoning) see shuffled anonymous answers for only one case and replicate per call. They receive facts, prohibited claims and the learning goal, never treatment labels.
- Judge facts and unsupported claims separately. Each judge reports whether the baseline/full and short/full pairs are preferable or tied, plus justification. Agreement requires both judges; disagreement is reported as unresolved, not converted into a victory.
- Report every generated answer and judge result, including failures. No retry for quality. Transport failures may be retried with the failed attempt disclosed.
- A result is a diagnostic signal only. Do not declare effectiveness from a small convenience sample or improve promotional numbers by excluding losing cases.
- Revise the Skill only for a concrete recurring failure, then test the change in a new directory. Do not change grading criteria after seeing results.
- Existing v1/v2 evidence stays archived. The README may describe intended behavior and link research records without using a leaderboard as marketing.
