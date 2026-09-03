### 1. Profile、Bundle、Patch 与启动合成

- **Patch** 是最小的配置变换：可插入插件 entry、按稳定 id 修改配置，或禁用已有 entry。
- **Bundle** 是一个可复用的 npm 包，通过 manifest 指向自己的 `cordis.patch.yml`，代表一组可组合的能力。
- **Profile** 是用户可直接启动的组合：它在 `dsh.profile.bundles` 中选择 Bundle，并明确规定应用顺序，还可附带 Profile 自己的 patch。

例如“基础能力 + headless 能力 + 用户覆盖”的合成过程是：

```text
空 entry 列表
→ 基础 Bundle patch
→ headless Bundle patch
→ Profile patch
→ 全局用户 patch
→ 命令行 --patch
→ 启动器派生覆盖层
```

越后的层优先级越高。因此，headless 可以建立在基础能力之上，用户又可以修改或关闭前面引入的插件，命令行还能针对本次运行临时覆盖。

这个顺序是产品语义，因为它决定了“谁有最终决定权”、能力能否被替换，以及同一个 Profile 实际启动什么系统。交换两层可能改变插件配置、启停状态乃至运行行为，并非单纯改变配置文件的组织方式。

### 2. 服务、注入与 Fiber 的生命周期

`super(ctx, 'llm')` 表示服务实例向**当前作用域**提供名为 `llm` 的服务。内部通过 `ctx.reflect.provide(...)` 注册实例，同时把撤销注册的动作绑定到拥有该实例的 Fiber。

`ctx.llm` 不是普通字段读取。`Context` 是 Proxy，这次访问会进入服务解析器，从当前作用域关系中查找 `llm` 实例。

`inject: ['llm']` 声明的是插件的启动条件：“作用域中能解析到 `llm` 后，我才能运行。”它不会把字符串直接转换成对象；真正的对象仍由服务注册和上下文解析提供。

完整链条是：

```text
服务 Fiber 执行并 provide('llm')
→ 等待 llm 的插件 Fiber 依赖满足
→ Fiber 从 PENDING 转为装载，插件可通过 ctx.llm 使用服务
→ 插件或服务卸载
→ Fiber 执行其清理函数、释放生命周期资源并撤销服务
```

所以 Fiber 是把依赖等待、插件实例、状态和清理动作连成一体的运行时边界。

### 3. “Model-visible means logged”与 Headless 输出

它约束的是：**任何具有语义、将进入模型输入的内容，都必须先成为 Session 中的日志事实。**不能让模型看到只存在于临时内存缓冲、却无法恢复或审计的内容。

这只是单向蕴含：模型可见的一定已记录；已记录的不一定模型可见，因为日志还可以包含诊断事件。

Session 是带连续 `seq` 的内存权威 append-only 事件序列；模型对话只是由这些事件折叠出的投影。一次模型函数返回的字符串只是执行过程中的瞬时结果，可能尚未成为最终消息，也不能代表持久化的结束原因。

因此 Headless 在追加 follow-up 前记录起始 `seq`，等待 Agent idle 并 flush 后，只扫描本次区间内的 `assistant/message` 与 `turn/end`：输出最后一条已记录的 assistant 文本，并按已记录的结束原因确定退出码。这样终端结果与恢复、重放和审计所依据的 Session 事实一致。