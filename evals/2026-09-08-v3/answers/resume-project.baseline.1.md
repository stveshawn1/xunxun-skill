上次已经看过请求路由和输入校验，这次直接接着看**订单怎么保存**。

旧笔记指向 `storage.py`，但当前版本已删除这个文件，保存逻辑在 `repository.py`。现在 `app.py` 的调用顺序是：

```python
validate(payload)
repository.save_order(order)
format_reply(order_id)
```

重点看中间的 `save_order(order)`：它把订单存进一个字典，再返回这个订单的整数 ID。随后，`format_reply(order_id)` 用这个 ID 组织响应。

这里要记住一个关键点：**字典只存在于内存中，进程重启后，保存的订单就没了。** 所以此处的“保存”还不是写入数据库或磁盘。

这就接上了之前的流程：输入通过校验 → 保存订单并拿到 ID → 用 ID 生成回复。