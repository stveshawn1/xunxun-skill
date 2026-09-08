上次已经看过请求入口和输入校验，这次直接接着看**订单怎么保存**。

旧笔记里写的是 `storage.py` 的 `save_order`，但当前代码已移到 `repository.py`。现在 `app.py` 的调用顺序是：

```python
validate(payload)
repository.save_order(order)
format_reply(order_id)
```

重点看中间这一步：`repository.save_order(order)` 把订单存进一个字典，再返回订单的整数 ID。后面的 `format_reply(order_id)` 接收这个 ID，用它组织回复。

这里最值得记住的是：**字典只存在于内存里，程序重启后订单就没了。** 所以这里的“保存”还不是写入数据库或文件。

你已经把这条请求流程串起来了：校验输入 → 保存订单并取得 ID → 组织回复。下一步就接着看 `format_reply` 如何生成返回内容。