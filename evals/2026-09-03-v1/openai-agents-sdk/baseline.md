1. **Agent、Runner、Session**

- `Agent` 定义“谁来思考”：instructions、model、tools、handoffs，以及可选的输出类型。它是行为配置，本身不执行。
- `Runner` 定义“怎样执行”：反复调用当前 Agent；遇到工具调用就执行并回传结果，遇到 handoff 就切换 Agent，得到最终输出或达到限制后停止。它还集中管理模型提供方、guardrails、tracing 等运行配置。
- `Session` 保存“之前聊过什么”：跨多次 run 持久化对话历史，让后续执行延续上下文。

可把三者理解为：Agent 是角色与能力，Runner 是流程引擎，Session 是记忆。合成一个大对象后，静态定义、单次执行状态和跨次持久状态会混在一起：难以判断对象该复用多久、修改配置会影响哪次运行，也更难测试、并发和替换存储。

2. **Manager 与 Handoff**

Manager 模式中，中央 Agent 始终掌握对话控制权。专家 Agent 像工具一样被调用，返回局部结果；中央 Agent 决定是否继续调用其他专家，并负责整合最终答案。它适合需要统一口径、全局策略、跨专家综合判断的场景，例如旅行规划器汇总机票、酒店和天气建议。

Handoff 是控制权转移：原 Agent 把对话交给专家，之后专家成为 Runner 的当前 Agent，并直接推进流程、产生最终答案。它适合职责边界清晰、专家应直接接管的场景，例如客服入口识别为退款问题后转给退款专员。

核心区别不是“有没有调用专家”，而是调用后谁仍是主角：Manager 中专家是下属能力；Handoff 中专家成为新的负责人。

3. **Guardrail 与 Tracing**

两者都可能接触工作流事件，但作用不同：

- Guardrail 位于执行路径上，并能作出允许或阻断的控制决定。Input guardrail 检查初始输入，output guardrail 检查最终输出，tool guardrail 包围每次自定义函数工具调用。
- Tracing 只记录 run、Turn、模型生成、工具、handoff、guardrail 等 span，供调试和评估使用；记录到异常并不等于阻止异常发生。

默认并行运行 input guardrail，可以让检查与 Agent 同时开始，从而降低正常请求的等待时间；代价是 guardrail 最终阻断前，模型可能已经消耗 token，甚至完成部分工作。串行模式先检查再运行，增加检查延迟，却能更早、也更严格地阻止不应开始的执行。

还要注意作用范围：input guardrail 只检查链中的第一个 Agent，output guardrail 只检查真正产生最终输出的 Agent；它们并非自动覆盖所有中间 Agent。