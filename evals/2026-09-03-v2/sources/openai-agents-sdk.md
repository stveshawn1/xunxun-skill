# OpenAI Agents SDK source snapshot

Snapshot date: 2026-09-03.

`Agent` instances carry instructions, a model, tools, handoffs, and optional output typing. An Agent does not execute itself.

`run()` or a reusable `Runner` owns execution. Its loop invokes the current Agent; final output stops the loop; a handoff changes the current Agent; otherwise tool calls are executed and their results return to the next model turn. Runner configuration includes model provider, guardrails, tracing, and session behavior.

A Session stores conversation history across runs. A RunResult contains the final output, current/last Agent, history, and run state; it is not the same thing as durable Session history.

Two composition patterns:

- Manager / agents-as-tools: the manager remains responsible for the conversation and synthesizes the final answer from specialist results.
- Handoff: control moves to the specialist, which becomes the current Agent in the continuing loop.

Guardrail families:

- Input guardrails inspect initial input and apply only to the first Agent in the chain.
- Output guardrails inspect the final output-producing Agent.
- Tool guardrails wrap custom function-tool calls.
- Parallel input guardrails reduce latency but the Agent may already spend tokens or perform work before a tripwire arrives. Serial checks block first.

Tracing records run, Agent, Turn, generation, tool, handoff, and guardrail spans. Recording an event does not itself block it.

Sources:

- <https://openai.github.io/openai-agents-js/guides/agents/>
- <https://openai.github.io/openai-agents-js/guides/running-agents/>
- <https://openai.github.io/openai-agents-js/guides/handoffs/>
- <https://openai.github.io/openai-agents-js/guides/guardrails/>
- <https://openai.github.io/openai-agents-js/guides/sessions/>
- <https://openai.github.io/openai-agents-js/guides/tracing/>

