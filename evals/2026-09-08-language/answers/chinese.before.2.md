回到 `handle` 里的这一行：

```python
search = services['search']
```

它用键 `'search'` 从字典里取出之前存进去的对象，再让局部变量 `search` 指向它。对象来自前面这一行：

```python
services['search'] = Search()
```

把这两处连起来看：

1. `Search()` 创建一个 `Search` 实例，也就是一个能调用 `query` 的具体对象。
2. `services['search'] = ...` 把这个对象存到字典的 `'search'` 键下。
3. 执行 `handle('hello')` 时，`search = services['search']` 取到的就是**同一个对象，没有重新创建或复制**。
4. `search.query(text)` 调用这个对象的方法，把 `'hello'` 转成 `'HELLO'`，最后由 `print` 打印出来。

这里 `'search'` 是字典的键，`search` 是函数里的变量名；两者不必同名。写成 `s = services['search']`，再调用 `s.query(text)`，也会拿到并使用同一个对象。