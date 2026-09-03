# Evaluation prompt: Financial Statements

你是一位面向非专业读者的会计老师。请只根据下面的资料包回答，不访问外部资料；除了读取系统决定使用的 Skill 指令外，不调用其他工具，也不要提到任何 Skill 或实验。目标是让读者建立可以迁移到新交易的系统模型，而不是背诵口诀。这是一般教育，不是投资建议。逐题回答，总长度不超过 1800 个中文字符。

## 资料包

资产负债表描述某一时点的资源和索取权，基本关系是“资产 = 负债 + 所有者权益”。利润表描述一段期间内收入和费用如何形成利润。现金流量表描述同一期间现金如何因经营、投资和融资活动而增减。三张表相关但不等价：净利润不是现金净增加额，资产负债表的现金期末变化要由现金流量表解释。

复式记账要求每笔交易至少影响两个账户，借方合计等于贷方合计，从而保持会计等式。借方只是账户左侧，贷方只是右侧，并不分别等于增加和减少：资产、费用通常借方增加；负债、权益、收入通常贷方增加。

权责发生制按经济活动发生时间确认收入和费用，而不是等现金收付才确认。例如本期赊销服务会同时增加收入和应收账款，但当时没有现金流入；以后客户付款时，应收账款转为现金，不再产生第二次收入。赊购本期使用的服务会形成费用和应付账款；以后付款时减少现金和应付账款，不再产生第二次费用。

用现金购买一台将使用多期的机器时，现金资产减少、固定资产增加；购买现金列为投资活动流出。机器的成本不是在购买期一次性变成全部费用，而是在其受益期间通过折旧逐步进入利润表。折旧会降低利润但本身不是当期现金流出，因此经营现金流从净利润出发时通常要把非现金折旧调整回来。

来源快照（2026-09-03）：

- <https://www.sec.gov/about/reports-publications/beginners-guide-financial-statements>
- <https://openstax.org/books/principles-finance-2e/pages/4-2-economic-basis-for-accrual-accounting>
- <https://openstax.org/books/principles-finance-2e/pages/5-3-the-relationship-between-the-balance-sheet-and-the-income-statement>
- <https://openstax.org/books/principles-financial-accounting/pages/2-1-describe-the-income-statement-statement-of-owners-equity-balance-sheet-and-statement-of-cash-flows-and-how-they-interrelate>

## 问题

1. 为什么“借方 = 增加、贷方 = 减少”是错误心智模型？复式记账真正保持的约束是什么？
2. 一家公司为什么可能利润为正却现金紧张？请用“本期赊销 100 元、下期收款”的两步过程说明收入、应收账款和现金分别何时变化。
3. 对“现金购买一台长期使用的机器”这笔交易，三张表分别看到什么？为什么它不会在购买当期把全部现金支出直接等同为利润表费用？
