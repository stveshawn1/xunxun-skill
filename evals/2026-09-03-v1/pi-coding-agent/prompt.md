# Evaluation prompt: Pi Coding Agent

你是一位技术老师。请只根据下面的资料包回答，不访问外部资料、不调用工具，也不要提到任何 Skill 或实验。读者会编程，但不了解 Pi。目标是让读者建立可以迁移到新例子的心智模型，而不是背诵定义。逐题回答，总长度不超过 1800 个中文字符。

## 资料包

Pi Coding Agent 的 Session 默认保存为 JSONL：每行是一个带 `type` 的 JSON 对象。首行是 Session header；后续 entry 带 `id`、`parentId` 和时间戳。当前格式通过父指针形成树，因此一次 Session 可以在同一个文件里保存多个分支。加载给模型的对话不是简单读取全部行，而是沿当前叶子回溯活动分支，再根据 compaction 等 entry 构造当前上下文。

Compaction 不删除原始历史，而是在文件末尾追加一个摘要 entry，并记录从哪里保留近期消息。之后给模型的是“摘要 + 保留的近期消息”；JSONL 仍保存完整事件，所以持久历史与当前模型上下文不是同一个东西。Compaction 是有损投影：摘要可能遗漏细节，但原日志仍可用于回看或切换分支。

Pi 中一个 Turn 是“从一条用户输入开始，到模型给出不再要求调用工具的最终回复”为止。一个 Turn 可以包含多个 Step。每个 Step 是一次“向模型发请求 → 收到回复 → 如果有工具调用则执行工具并把结果送回模型”的循环；同一步里可以有多个并行工具调用。

Extension 是运行中的 TypeScript 模块，可以订阅生命周期事件、拦截或修改工具调用、注册模型可调用工具和命令、操作 UI，并通过追加 Session entry 保存扩展状态。Extension 以宿主进程权限执行，应只安装可信代码。Skill 则主要是给模型读取的 Markdown 工作指引；prompt template 是用户主动展开的提示词模板。三者都能扩展 Pi，但执行权限、触发方式和作用层不同。

来源快照（2026-09-03）：

- <https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/session.md>
- <https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/compaction.md>
- <https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md>

## 问题

1. 为什么说 Pi 的 JSONL 同时是“追加式历史”和“可分支的树”？如果用户回到旧节点继续对话，文件和模型上下文分别发生什么？
2. Turn 和 Step 的边界分别在哪里？请用一次“模型先读文件、再改文件、最后回答”的任务走一遍循环。
3. Extension、Skill、prompt template 各是什么层的扩展？为什么把一个危险命令拦截器做成 Skill 并不能提供与 Extension 相同的保证？

