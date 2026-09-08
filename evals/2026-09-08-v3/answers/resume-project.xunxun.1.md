上次看到了请求流程和输入校验，这次接着看**订单如何保存**。旧笔记指向 `storage.py`，但当前版本已删除这个文件，保存入口改为 `repository.py` 中的 `save_order`。

接着校验后的这条路径看：

```python
validate(payload)
repository.save_order(order)
format_reply(order_id)
```

这里有三个关键点：

- `validate(payload)` 负责输入校验；接下来 `repository.save_order(order)` 才负责保存订单。
- `save_order` 把订单放进一个字典，并返回整数类型的订单 ID。
- `format_reply(order_id)` 使用这个 ID 组织回复。

这一步最重要的区别是：**当前“保存”只是在进程内存中保留订单**，没有写入磁盘或数据库。进程结束后，这份字典中的订单就不会保留；拿到订单 ID，并不代表订单已经长期存储。

我们现在走到了“保存订单 → 返回 ID”，下一步就是看 `format_reply` 怎样把 ID 变成用户收到的回复。