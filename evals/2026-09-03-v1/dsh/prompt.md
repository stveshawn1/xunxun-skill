# Evaluation prompt: DeepSeek Harness

你是一位技术老师。请只根据下面的资料包回答，不访问外部资料、不调用工具，也不要提到任何 Skill 或实验。读者会编程，但不了解 DSH 内部实现。目标是让读者建立可以迁移到新例子的心智模型，而不是背诵类名。逐题回答，总长度不超过 1800 个中文字符。

## 资料包

DSH 的 Profile 是 `$DSH_HOME/profiles/<name>` 下的一套可启动组合。它的 `package.json` 用 `dsh.profile.bundles` 保存有序 Bundle 名单；每个 Bundle 是一个 npm 包，并通过 manifest 指向自己的 `cordis.patch.yml`。启动时，以空的 entry 列表为根，依次应用 Bundle patches、Profile 自己的 patch、全局用户 patch、命令行 `--patch` overlay，最后再加启动器派生的覆盖层。后面的层优先级更高。Patch 可以插入插件 entry、按 id 改配置或禁用 entry；Bundle 是可复用的一组 patch，Profile 是选择并排序这些组的用户组合。

Cordis `Context` 是带作用域的依赖容器和运行时门面。它返回一个 Proxy，普通 `ctx.foo` 读取会进入服务解析器。`Service` 子类调用 `super(ctx, name)` 时，会执行 `ctx.reflect.provide(name, this, check)`，把实例放进当前作用域，并把移除动作绑定到拥有它的 Fiber。Fiber 是一次插件装载的运行时实例，跟踪依赖、配置、状态和清理函数；依赖尚未满足时处于 PENDING，满足后装载，卸载时按生命周期释放。插件声明 `inject` 是在说“这些服务可用时我才能启动”，不是把字符串直接变成对象。

Session 是内存中的权威 append-only event sequence。事件具有连续 `seq`，涵盖 `turn/start`、`step/start`、user/assistant message、tool call/result 和结束事件。模型看到的对话 surface 是从已记录事件折叠出来的投影；设计约束“model-visible means logged”表示任何会进入模型输入的语义内容必须先有对应日志事实，不能只存在于某个临时内存缓冲。日志可包含不进入模型的诊断事件，因此反方向不成立。

Headless runner 等待应用插件树装载完成，创建 Agent，等待 idle，记录起始 seq，追加用户 follow-up，再等待 idle 并 flush Session。它不直接信任某个模型调用函数返回的临时字符串，而是在这次 seq 区间里扫描 `assistant/message` 和 `turn/end`，输出最后一条 assistant 文本并根据持久化的结束原因决定退出码。这样终端输出与可恢复、可审计的 Session 事实保持一致。

代码快照：`deepseek-ai/deepseek-harness@b150a551b8`。

- `packages/boot/app-boot/src/profile.ts`
- `apps/cli/src/profile-boot.ts`
- `vendor/cordis/src/context.ts`
- `vendor/cordis/src/service.ts`
- `vendor/cordis/src/fiber.ts`
- `packages/core/session/src/index.ts`
- `packages/core/session/src/surface.ts`
- `packages/bundle/headless/src/index.ts`

## 问题

1. Profile、Bundle、Patch 分别是什么？请用“基础能力 + headless 能力 + 用户覆盖”说明启动时如何合成，为什么层顺序是产品语义而不只是配置细节？
2. `super(ctx, 'llm')`、`ctx.llm`、`inject: ['llm']` 和 Fiber 之间是什么关系？请沿“提供服务 → 依赖满足 → 插件启动 → 卸载清理”串起来。
3. “Model-visible means logged”准确约束了什么？为什么 Headless 从 Session Event Log 提取最终回答，而不是直接使用最近一次模型函数的返回值？

