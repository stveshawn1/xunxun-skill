回到这一行：

```python
search = services['search']
```

它用键 `'search'` 从字典 `services` 中取出对象，再让局部变量 `search` 指向它。

这个对象是在前面放进去的：

```python
services['search'] = Search()
```

这里 `Search()` 创建一个 `Search` 对象，字典把它保存在键 `'search'` 对应的位置。之后 `handle()` 查这个键，拿到的就是**同一个对象**，不会重新创建。

所以接下来：

```python
return search.query(text)
```

就是调用那个对象的 `query` 方法。传入 `'hello'`，得到 `'HELLO'`。

注意：`'search'` 是字典的字符串键，`search` 是变量名；变量即使改叫 `s`，只要仍然查 `services['search']`，拿到的对象也一样。