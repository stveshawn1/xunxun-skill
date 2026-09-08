上次看完了请求路由和输入校验，这次接着看**订单怎么保存**。

旧笔记写的是 `storage.py`，但当前代码已移除这个文件，保存逻辑在 `repository.py`。现在的调用顺序是：

```python
validate(payload)
repository.save_order(order)
format_reply(order_id)
```

重点看中间一步：`save_order(order)` 把订单存进一个字典，再返回整数类型的订单 ID。可以理解为给订单编个号，之后通过这个编号找到它。

比如，保存一笔订单后返回 `3`，字典中就用 `3` 对应这笔订单；接着 `format_reply(order_id)` 用这个编号生成回复。

这里要记住一个区别：**存进字典不等于永久保存**。这个字典只存在于内存中，程序重启后，之前保存的订单就没了。

这次先把流程连起来：校验输入 → 保存订单并取得 ID → 用 ID 生成回复。下一步就看 `format_reply` 如何组织返回内容。