上次已经看过请求路由和输入校验，这次接着看**订单怎么保存**。

旧笔记指向 `storage.py`，但当前版本已删除它，保存逻辑移到了 `repository.py`。现在 `app.py` 的调用顺序是：

```python
validate(payload)
repository.save_order(order)
format_reply(order_id)
```

重点看中间的 `save_order(order)`：它把订单放进一个**内存字典**，然后返回这个订单的整数 ID。可以把字典理解成一张临时登记表：例如用 `1` 对应一份订单，保存后返回 `1`，后面的 `format_reply(order_id)` 再用这个编号组织回复。

这里要分清：**目前“保存”只是放进内存，没有写入磁盘或数据库，程序重启后订单就没了。**

这样，上次的输入校验就接上了后续流程：校验通过 → 保存订单并取得编号 → 根据编号生成回复。