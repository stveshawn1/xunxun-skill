1. **Agent、Runner、Session**

- `Agent` 定义“谁来思考”：instructions、model、tools、handoffs，以及可选的输出类型。它是能力与行为的声明，本身不执行。
- `Runner` 执行“接下来做什么”：调用当前 Agent；遇到最终输出就结束，遇到 handoff 就切换 Agent，遇到工具调用就执行并把结果送回模型。它还集中管理模型提供方、tracing、guardrails 等运行配置。
- `Session` 保存“此前聊过什么”：把对话历史延续到下一次 `run`。它不负责推进执行，也不是 tracing 日志。

可以把它们理解为：Agent 是角色说明书，Runner 是舞台调度，Session 是连续剧的前情记录。

若合成一个大对象，三种不同生命周期会混在一起：Agent 定义通常可长期复用；一次 run 有明确起止；Session 则跨多次 run 持续存在。混合后很难判断某项状态应当重置、复用还是持久化，并发执行、测试隔离和恢复对话也更容易发生状态串扰。

2. **Manager 与 Handoff**

关键区别不是“有没有专家”，而是“当前控制者是谁”。

Manager 模式中，中央 Agent 始终掌握对话。专家 Agent 像工具一样被调用，只返回局部结果；中央 Agent 决定调用谁、如何组合，并产出最终答案。它适合需要统一语气、统一策略、跨多个专家综合判断的场景。

Handoff 则会改变 Runner 的“当前 Agent”：原 Agent 把控制权交给专家，后续循环由专家继续处理，专家可以直接产出最终答案。它适合任务已经明确进入某个专业领域，希望专家直接接管后续对话的场景。

一个迁移判断法是：若专家只是提供材料，选 Manager；若专家应成为新的负责人，选 Handoff。

3. **Guardrail 与 Tracing**

两者都能接触工作流事件，但权限不同：

- Guardrail 是决策边界：检查内容或调用，并能阻断执行。Input guardrail 检查初始输入，tool guardrail 包围每次自定义 function-tool 调用，output guardrail 检查最终输出。
- Tracing 是运行记录：把 run、模型生成、工具、handoff、guardrail 等记成 span，供调试和评估；记录到异常行为并不等于阻止它。

还要注意作用范围：input guardrail 只保护链中的第一个 Agent；output guardrail 只检查实际产生最终输出的 Agent。

并行 input guardrail 与 Agent 同时开始，可以减少等待时间；代价是“先执行、后判定”的投机窗口：在 guardrail 触发前，模型可能已经消耗 token 或完成部分工作。串行模式先检查再运行，延迟更高，但能更早阻断。安全边界越严格，越应倾向串行；更看重响应速度且可接受少量无效工作时，并行更合适。