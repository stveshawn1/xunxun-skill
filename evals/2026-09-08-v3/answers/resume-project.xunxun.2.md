上次我们看完了请求入口和输入校验，下一步是看订单怎样保存。旧笔记里的 `storage.py` 已被删除；当前这一步在 `repository.py` 的 `save_order` 中。

沿着 `app.py`，接下来的调用是：

```python
validate(payload)
repository.save_order(order)
format_reply(order_id)
```

校验之后，`repository.save_order(order)` 把订单存进一个字典，并返回整数类型的订单 ID。随后，`format_reply(order_id)` 用这个 ID 组织回复。这里要分清：**订单保存在字典里，返回给下一步的是订单 ID。**

这个字典只存在于程序内存中，所以“保存成功”不代表已经写入磁盘；程序退出后，不能靠这个字典恢复订单。

这次先接到这里：**校验 → 存入内存字典 → 返回 ID → 组织回复**。下次就从 `format_reply` 看这个 ID 怎样变成最终回复。