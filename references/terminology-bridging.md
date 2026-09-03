# Terminology Bridging

Keep specialized vocabulary from becoming invisible prerequisites.

## Familiarity evidence

Treat a term as known only when there is relevant evidence:

- the learner explicitly states the background;
- they use the term correctly in a way that depends on its meaning;
- they previously explained or applied the concept successfully;
- they demonstrate an equivalent concept under another name.

Do not infer familiarity from profession, repository choice, account metadata, a single copied phrase, or lack of questions.

## Bridge depth

### Incidental term

Give one inline clause, usually 5–20 words:

```text
Contextual Bandit（根据当前情境选择一个动作，再用反馈改进后续选择）
```

Then continue the main explanation.

### Important supporting term

Give a compact definition plus one distinction or micro-example:

```text
Counterfactual 指“同一时刻如果采用另一种讲法会怎样”；
现实中只能看到实际采用的那一种结果。
```

### Central term

Temporarily enter the concept preset: definition → intuition → minimal example → boundary, then return to the saved path.

## Avoid glossary cascades

Do not write:

```text
Policy 是根据 posterior reward 优化 action utility 的决策函数。
```

when posterior, reward, action, and utility are also unsupported. Prefer familiar words first, then attach the canonical term:

```text
Policy 是“在当前情境下选择哪种讲法”的规则。
```

## Familiarity without a vocabulary database

Resolve familiarity from the smallest available evidence surface:

1. correct use or application in the current Session;
2. a concept listed under `Established concepts` in the project profile;
3. broad background recorded in the global learner profile;
4. otherwise, treat the term as unknown and add a proportional bridge.

Do not persist every term or assign statuses such as introduced, working, or demonstrated. At a natural project milestone, update the compact `Established concepts` section only when it helps resume the learning route. For genuinely cross-project background, update the global profile only through the normal promotion rule.

If evidence is unclear, repeat a short bridge. A few repeated words cost less than a stale vocabulary subsystem.
