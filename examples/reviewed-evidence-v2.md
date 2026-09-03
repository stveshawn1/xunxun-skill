# What Xunxun Changes: Reviewed Examples

This page shows representative differences from the preregistered v2.3 evaluation. It is supporting evidence for understanding Xunxun, not part of the Skill's runtime instructions.

## How to read this page

Each pair used the same natural novice question, source snapshot, model settings, and fresh-session conditions. The only intended difference was whether Xunxun was loaded. Each condition was generated three times, and every pair was compared blindly by three judges.

The four positive examples below were selected after aggregate analysis for clarity and domain variety; the selection itself is not the basis of the aggregate result. The counterexample is included because the same treatment can also add unnecessary explanation. Excerpts are faithful English translations with surrounding text omitted; follow the links for the complete, unedited Chinese outputs and judgments.

## Overall signal

| Measure | v2.3 result |
|---|---:|
| Independent questions | 15 |
| Paired comparisons | 45 |
| Xunxun / Baseline / tie | 19 / 12 / 14 |
| Xunxun share among non-ties | 61.3% |
| Mean required-fact coverage delta | +3.4 percentage points |
| Final-answer character ratio | 1.093× |
| Cumulative input-token ratio | 1.425× |

This is a modest, context-dependent signal. The pairwise sign test was not statistically significant (`p≈0.281`), and much of the aggregate advantage came from the financial-statements questions.

## Positive example 1: separating DSH service mechanisms

**Question:** Why does `super(ctx, 'llm')` make `ctx.llm` available, and what does `inject: ['llm']` do?

The Baseline answer explained the core mechanism, but also made a lifecycle guarantee not established by the supplied source:

> If the plugin providing `llm` is unloaded or hot-replaced, plugins depending on it will also be temporarily unloaded ... When the new `llm` service reappears, consumers restart.

Xunxun kept the three mechanisms separate and stopped at the supported boundary:

> `super(ctx, 'llm')`: register and provide the `llm` service  
> `ctx.llm`: query and obtain the registered service instance  
> `inject: ['llm']`: declare that the current plugin depends on `llm`

All three judges preferred Xunxun in this replicate. Across the three replicates, Xunxun won all three majority decisions; item-level fact coverage improved by 19.4 percentage points while the answers were shorter overall.

[Baseline output](../evals/2026-09-03-v2/results/dsh-service-lifecycle/baseline/r1.md) · [Xunxun output](../evals/2026-09-03-v2/results/dsh-service-lifecycle/xunxun/r1.md) · Judgments: [Sol](../evals/2026-09-03-v2/judgments/sol/dsh-service-lifecycle.json), [Terra](../evals/2026-09-03-v2/judgments/terra/dsh-service-lifecycle.json), [GPT-5.5](../evals/2026-09-03-v2/judgments/gpt55/dsh-service-lifecycle.json)

**Observed contribution:** boundary precision. Xunxun did not merely add detail; it reduced an unsupported inference.

## Positive example 2: Agent, Runner, and Session

**Question:** Aren't Agent and Runner both running the model? Why separate them, and where does Session belong?

The Baseline answer gave the correct definitions:

> Agent defines “who does it and how”; Runner is responsible for “running it”; Session is responsible for “remembering what happened” across multiple runs.

Xunxun made the design reason and lifecycle boundary more explicit:

> Agent defines how to run: model, instructions, tools, handoff, output type. It is like a role-and-capability configuration and does not start execution itself.  
> Runner actually runs it ... During a handoff, the Runner does not change; the current Agent does.  
> Session is not the next layer under Agent or an internal step of Runner; it is a state-storage layer that collaborates with both.

Two judges preferred Xunxun and one tied in this replicate. At item level, Xunxun won two replicates, Baseline won one, and factual coverage was equal.

[Baseline output](../evals/2026-09-03-v2/results/agents-agent-runner-session/baseline/r1.md) · [Xunxun output](../evals/2026-09-03-v2/results/agents-agent-runner-session/xunxun/r1.md) · Judgments: [Sol](../evals/2026-09-03-v2/judgments/sol/agents-agent-runner-session.json), [Terra](../evals/2026-09-03-v2/judgments/terra/agents-agent-runner-session.json), [GPT-5.5](../evals/2026-09-03-v2/judgments/gpt55/agents-agent-runner-session.json)

**Observed contribution:** transfer support. The answer moved from labels to a rule that still works during handoff and across multiple runs.

## Positive example 3: profit without payroll cash

**Question:** If a company has profit, how can it still lack enough cash to pay wages?

The Baseline answer listed several common causes and supplied a short example. Xunxun instead used one continuous transaction story:

> The company completes a project and recognizes 1 million in revenue, but the customer pays next month—profit increases by 1 million, cash does not increase, and accounts receivable increases by 1 million.  
> ...  
> Monthly profit = 100 − 30 − 20 − 2 = 480,000  
> Ending cash = 40 − 20 − 15 = 50,000

It then named the reusable mechanism:

> There are three key timing mismatches: revenue versus collection, expenditure versus expense, and profit versus ability to pay.

All three judges preferred Xunxun in this replicate. Xunxun won all three item-level majority decisions, with fact coverage improving by 8.3 percentage points.

[Baseline output](../evals/2026-09-03-v2/results/accounting-profit-cash/baseline/r1.md) · [Xunxun output](../evals/2026-09-03-v2/results/accounting-profit-cash/xunxun/r1.md) · Judgments: [Sol](../evals/2026-09-03-v2/judgments/sol/accounting-profit-cash.json), [Terra](../evals/2026-09-03-v2/judgments/terra/accounting-profit-cash.json), [GPT-5.5](../evals/2026-09-03-v2/judgments/gpt55/accounting-profit-cash.json)

**Observed contribution:** a single causal example connected three abstract statements without requiring accounting vocabulary first.

## Positive example 4: buying a machine versus recognizing an expense

**Question:** A machine costs a large amount immediately. Why is the entire amount not an expense on that period's income statement?

Both answers were accurate. Xunxun added one small sentence that closed a common novice misunderstanding:

> Depreciation is the accounting allocation of the machine's cost; it does not mean the company pays again every year.

It also organized the distinction by the question each statement answers:

| Statement | Question | Effect of buying the machine |
|---|---|---|
| Cash-flow statement | When did money move? | Full outflow now |
| Balance sheet | What does the company still own? | A machine asset appears |
| Income statement | How much resource was consumed this period? | Only this period's depreciation |

All three judges preferred Xunxun in this replicate. Xunxun won all three item-level majority decisions, with fact coverage improving by 11.1 percentage points.

[Baseline output](../evals/2026-09-03-v2/results/accounting-machine-purchase/baseline/r3.md) · [Xunxun output](../evals/2026-09-03-v2/results/accounting-machine-purchase/xunxun/r3.md) · Judgments: [Sol](../evals/2026-09-03-v2/judgments/sol/accounting-machine-purchase.json), [Terra](../evals/2026-09-03-v2/judgments/terra/accounting-machine-purchase.json), [GPT-5.5](../evals/2026-09-03-v2/judgments/gpt55/accounting-machine-purchase.json)

**Observed contribution:** misconception repair. The extra sentence explains why depreciation and cash payment can occur in different periods.

## Counterexample: when the source already has one decisive distinction

**Question:** What does `model-visible means logged` mean, and why can't Headless print the string just returned by the model call?

Both answers correctly established that Session is the authority, that model-visible content is projected from recorded events, and that Headless reads the committed turn interval. Xunxun then repeated the same boundary through a diagram, a list of possible intermediate states, a two-source-of-truth example, a seven-step sequence, and a recap.

The Baseline answer covered the same facts more economically, including the decisive example:

> The model's first response may be a tool call; the natural-language answer that should actually be printed comes after the tool executes and the model is called a second time.

All three judges preferred Baseline in this replicate, and Baseline won all three item-level majority decisions despite equal fact coverage.

[Baseline output](../evals/2026-09-03-v2/results/dsh-model-visible-log/baseline/r2.md) · [Xunxun output](../evals/2026-09-03-v2/results/dsh-model-visible-log/xunxun/r2.md) · Judgments: [Sol](../evals/2026-09-03-v2/judgments/sol/dsh-model-visible-log.json), [Terra](../evals/2026-09-03-v2/judgments/terra/dsh-model-visible-log.json), [GPT-5.5](../evals/2026-09-03-v2/judgments/gpt55/dsh-model-visible-log.json)

**Observed limitation:** once a compact distinction fully resolves the confusion, additional teaching structure can become repetition rather than value.

## What this evidence supports

The examples support a narrow claim: Xunxun can improve an underspecified novice explanation when the main difficulty is a hidden boundary, a causal chain, or a misleading everyday intuition. They also show that Xunxun can lose when the source and Baseline already offer one clean decisive explanation.

They do not establish universal benefit, statistical significance, longitudinal personalization, or real-codebase navigation quality. Those require separate evidence.

For the frozen questions, all 90 outputs, all 45 judgment files, protocol amendments, aggregate analysis, and integrity checks, see the [complete v2.3 report](../evals/2026-09-03-v2/report.md).
