# Evaluation prompt: OpenAI Agents SDK

你是一位技术老师。请只根据下面的资料包回答，不访问外部资料；除了读取系统决定使用的 Skill 指令外，不调用其他工具，也不要提到任何 Skill 或实验。读者会编程，但不了解 OpenAI Agents SDK。目标是让读者建立可以迁移到新例子的心智模型，而不是背诵 API。逐题回答，总长度不超过 1800 个中文字符。

## 资料包

OpenAI Agents SDK 使用少量核心抽象。`Agent` 描述一个带 instructions、model、tools、handoffs 和可选 output type 的智能体；它本身不会运行。`run()` 或可复用的 `Runner` 才负责执行：调用当前 Agent，若得到最终输出则停止；若得到 handoff 则切换当前 Agent 后继续；否则执行工具调用并把结果送回模型，直到最终输出或达到限制。`Runner` 还集中持有模型提供方、tracing、guardrails 和 session 等运行配置。

多 Agent 组合有两种常见方式。Manager（agents as tools）让中央 Agent 始终拥有对话，把专家 Agent 当工具调用，并由中央 Agent 汇总最终答案。Handoff 则把当前对话控制权交给另一个 Agent，后续循环以新 Agent 为当前执行者。前者便于集中统一策略，后者让专家直接接管。

Guardrail 是控制边界。Input guardrail 检查初始用户输入；output guardrail 检查最终输出；tool guardrail 包围每个自定义 function-tool 调用。Input guardrail 默认可以与 Agent 并行运行以降低延迟，但这意味着它触发前模型可能已经消耗 token 或执行工作；串行模式可以先阻断。Input guardrail 只作用于链中的第一个 Agent，output guardrail 只作用于产生最终输出的 Agent。

Tracing 是观测机制：它记录 run、Agent、Turn、模型生成、工具、handoff 和 guardrail 等 span，帮助调试和评估，但记录本身不会阻止执行。Session 则保存对话历史，使不同 run 可以延续上下文；它与 Runner 的执行配置、Tracing 的观测记录都不是同一个职责。

来源快照（2026-09-03）：

- <https://openai.github.io/openai-agents-js/guides/agents/>
- <https://openai.github.io/openai-agents-js/guides/running-agents/>
- <https://openai.github.io/openai-agents-js/guides/handoffs/>
- <https://openai.github.io/openai-agents-js/guides/guardrails/>
- <https://openai.github.io/openai-agents-js/guides/sessions/>
- <https://openai.github.io/openai-agents-js/guides/tracing/>

## 问题

1. Agent、Runner 和 Session 分别“定义什么、执行什么、保存什么”？为什么把它们合成一个大对象会让生命周期变模糊？
2. Manager（agents as tools）和 Handoff 都能调用专家 Agent，但控制权和最终答案归属有什么不同？分别适合什么情况？
3. Guardrail 和 Tracing 都能看到工作流事件，为什么前者是控制机制、后者只是观测机制？并行 input guardrail 带来了什么延迟与安全权衡？
