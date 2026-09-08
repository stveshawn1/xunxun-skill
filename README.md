<p align="center">
  <img src="docs/banner.svg" alt="循循 Xunxun：AI 讲了很多，你还是没懂？从卡住的地方开始，沿着主线讲明白。" width="100%">
</p>

<p align="center">
  一个帮 AI 带你学概念、读文件、看懂代码库的 Skill。<br>
  先讲清主线，遇到不懂的地方换个角度，再接着往下走。
</p>

<p align="center">
  <a href="#开始用">开始用</a> ·
  <a href="#先看一个真实例子">真实例子</a> ·
  <a href="#试着这样问">试用指令</a> ·
  <a href="#测试结果">测试与不足</a>
</p>

## 你可能也遇到过

本来想看懂一个代码库，AI 开口就是 runtime、context、dependency injection。每解释一个词，又冒出三个词。问了半天，最初那条主线已经找不回来了。

循循把这类反馈整理成一套可安装的讲解规则。名字取自“循循善诱”，叫它 **Xunxun / 循循** 都可以。

| 你卡住的地方 | 循循的讲解方式 |
|---|---|
| “每个字都认识，连起来不知道在说什么。” | 先说明它是什么、解决什么问题，再展开必要细节。 |
| “这个新名词又是什么意思？” | 补一句直观解释；如果是关键前提，先讲懂它。 |
| “我只想看代码怎么跑起来。” | 从真实入口走到结果，把后续细节接回同一条主线。 |
| “你刚才讲得太抽象了。” | 先检查有没有讲错或漏答，再换例子、拆层次或缩小问题。 |
| “下次别再让我重复说讲解习惯了。” | 你明确要求记住的偏好保存在本地；项目进度可选择保存。 |

Skill 是供 AI 读取的一套工作指引。循循需要搭配支持 Skills、能读取本地文件的 AI 工具使用；它没有独立聊天窗口，也不提供模型服务。

## 先看一个真实例子

**同一个问题：买机器当场花了一大笔钱，为什么利润表不把它全部算成当期费用？**

下面是旧版对照评测中的原文节选。两边都解释了资产和折旧，也都给了数字例子。

**未启用循循：**

> 机器能在未来多个期间持续创造收益，所以按权责发生制，购买成本应在受益期间内逐步确认为折旧费用，避免当期利润被一次性压低、以后期间利润又被高估。

**启用循循：**

> 机器在哪些期间提供经济利益，其成本就分摊到哪些期间。这叫折旧；它是对机器成本的会计分摊，不代表每年又付了一次钱。

这个片段值得看的是最后半句：它补上了初学者可能仍没弄清的“折旧和付款是什么关系”。该次配对中，三位模型裁判都偏好循循的回答；这不等于实际用户学习效果已被验证。

[查看未启用全文](evals/2026-09-03-v2/results/accounting-machine-purchase/baseline/r3.md) · [查看启用全文](evals/2026-09-03-v2/results/accounting-machine-purchase/xunxun/r3.md) · [更多对比与反例](examples/reviewed-evidence-v2.md)

## 开始用

### 1. 安装

**不熟悉终端？** 在你正在用、支持安装 Skills 的 AI 工具里发送：

```text
帮我安装这个 Skill：
https://github.com/stveshawn1/xunxun-skill
```

**使用终端：** 需要已安装 Node.js，且能运行 `npx`。执行后选择你的 AI 工具：

```bash
npx skills add stveshawn1/xunxun-skill --skill xunxun -g
```

`-g` 表示安装到个人目录，方便在不同项目使用。只想装在当前项目，去掉它。

<details>
<summary>指定 Codex / Claude Code 安装，以及检查和更新</summary>

安装到 Codex：

```bash
npx skills add stveshawn1/xunxun-skill --skill xunxun -g -a codex
```

安装到 Claude Code：

```bash
npx skills add stveshawn1/xunxun-skill --skill xunxun -g -a claude-code
```

检查已安装的 Skills：

```bash
npx skills list -g
```

更新：

```bash
npx skills update xunxun -g
```

安装方式依据 [Vercel Skills CLI 文档](https://github.com/vercel-labs/skills)。CLI 支持多种工具，但本仓库的既有对照评测使用 Codex；不表示已逐一验证所有工具的表现。这里直接从 GitHub 安装，不依赖 skills.sh 搜索收录。

</details>

### 2. 开始第一轮讲解

安装完成后，在能加载已安装 Skills 的新会话里发：

```text
用 xunxun 解释一下 TypeScript 的类型擦除。
我只写过一点 Python。
```

想读代码，就先打开项目再发：

```text
用 xunxun 带我读这个代码库。
先从一次真实用户请求的入口，讲到最终结果。
```

### 3. 直接说你卡在哪里

不需要学一套反馈口令。正常追问即可：

```text
我还是不懂，类型删掉之后，谁来检查输入？
```

循循的规则要求它沿着这个疑问继续解释，而不是把之前的全文再说一遍。效果会受模型、资料质量和问题本身影响。

## 试着这样问

以下是用法示例，不是测试结果。

| 想做什么 | 复制这句话，再补上你的材料 |
|---|---|
| 学一个概念 | 用 xunxun 解释这个概念。我目前知道…… |
| 读一个文件 | 用 xunxun 带我读这个文件，先讲它在整个系统里负责什么。 |
| 学习项目主线 | 用 xunxun 带我从入口走一遍主链路，关键代码再逐行看。 |
| 换一种讲法 | 这个例子我跟不上，先用真实代码里最短的一条路径讲。 |
| 保存讲解偏好 | 记住：讲陌生概念时，先给定义，再给一个简单例子。 |
| 下次接着学 | 把这次学到哪里、还卡在哪里和下一步，保存在这个项目的本地学习记录里。 |

正常讨论方案、评审代码、要求修改程序时，循循不应自动介入教学。

## 偏好和进度保存在哪里？

默认不创建画像。你要求记住偏好或保存项目进度后，Agent 才按规则写入：

| 位置 | 保存内容 |
|---|---|
| `~/.xunxun/profile.md` | 你要求或同意保留的跨项目讲解偏好 |
| `<项目>/.xunxun/profile.md` | 本项目的学习位置、未解决问题、下一步 |
| 当前对话 | 临时疑问、尝试的讲法和即时反馈 |

这些是本地 Markdown 文件。循循要求 Agent 防止项目私有记录被 Git 提交，不自动上传或跨设备同步。普通会话仍由你使用的 AI 工具处理；本地记录也需要被该工具读取，不能理解成模型调用完全离线。

## 测试结果

**当前为 public beta。** 仓库保留完整正反案例，方便你自己判断是否值得用。

旧版评测覆盖 Pi Coding Agent、OpenAI Agents SDK、DSH、适应性免疫和财务报表：15 个问题，每种条件生成 3 次，共 45 组配对，交给 3 位模型裁判盲评。

| 配对结果 | 组数 |
|---|---:|
| 偏好循循 | 19 |
| 偏好默认回答 | 12 |
| 平局 | 14 |

收益主要集中在财务题。也有明确反例：DSH 的事件日志问题，默认回答在三次配对中都获胜，因为循循的展开增加了重复。初版在高度结构化提示下则没有测出明显优势。

**这些测试评估旧版单轮回答，不证明当前版本、长期个性化或跨会话带读更有效。** 累计输入 token 用量约为默认条件的 1.425 倍。主观偏好结果未达到统计显著性。

[精选案例](examples/reviewed-evidence-v2.md) · [v2 完整报告](evals/2026-09-03-v2/report.md) · [v1 结果](evals/2026-09-03-v1/report.md)

<details>
<summary>指标修正与复核方式</summary>

历史报告中的“事实覆盖率”实际计算为：

```text
（覆盖的必需事实数 − 越界推断数）÷ 必需事实总数
```

因此 `+0.034` 是综合分数变化，不能解释成事实覆盖率提高 3.4%。原始回答和报告保持冻结，精选案例已说明这一修正。

评测对应早期 Skill `d49f0e9`。若复核原始完整性清单，在独立 checkout 中检出 `7a2f074`，再运行 `python3 evals/2026-09-03-v2/verify.py`；清单包含当时的 `SKILL.md`。

</details>

## 一起把它讲得更好

欢迎在 [Issues](https://github.com/stveshawn1/xunxun-skill/issues) 留下：你问了什么、回答哪里没讲明白、你希望怎样讲。附一小段去除隐私后的内容就够了，不必上传完整对话。

你也可以 Star 仓库，方便回来查看新的案例和改动。

作者也在[小红书](https://www.xiaohongshu.com/user/profile/684f805c000000001d035fa4)分享 AI 学习与循循的使用过程。

<details>
<summary>想看实现？从这些文件开始</summary>

- [SKILL.md](SKILL.md)：触发范围和讲解规则。
- [适应反馈](references/adaptive-learning.md)：怎样判断和调整讲法。
- [本地状态](references/local-state.md)：偏好与项目进度的读写。
- [评估说明](references/comparison-protocol.md)：怎样做对照。
- [examples/](examples/)：经过整理的演示。
- [evals/](evals/)：原始实验材料。

</details>
