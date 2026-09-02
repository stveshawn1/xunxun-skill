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

## Vocabulary evidence by scope

Record only recurring or structurally important terms, not every introduced noun:

```markdown
## Project vocabulary
- Term: contextual-bandit@adaptive-explanation
  Status: introduced | working | demonstrated
  Evidence: learner correctly mapped context/action/reward to a new case
```

- **introduced** — a bridge was provided; no application evidence yet.
- **working** — follow-ups use the term plausibly but transfer is untested.
- **demonstrated** — correct explanation or application provides evidence.

Resolve evidence through `references/local-state.md`: Session first, then exact project/domain evidence, then exact demonstrated global/domain evidence. Newly introduced terms stay in the Session unless they recur; project-specific meanings stay in the project ledger; only demonstrated cross-project meanings enter global vocabulary.

If later behavior contradicts familiarity, lower the status without treating it as failure by the learner; the earlier evidence was incomplete.
