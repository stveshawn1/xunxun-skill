回到 `handle` 里的这一行：

```python
search = services['search']
```

你已经理解了键值查找：这里用键 `'search'` 从字典 `services` 里取出对象，再让局部变量 `search` 指向它。

那个对象是前面这一行放进去的：

```python
services['search'] = Search()
```

可以分成两步理解：

1. `Search()` 创建一个 `Search` 对象。
2. `services['search'] = ...` 把这个对象存到字典的 `'search'` 键下。

所以，**`handle` 中的 `search` 拿到的是之前创建的同一个对象**，这里没有再创建一个。

接下来：

```python
return search.query(text)
```

就调用这个对象的 `query` 方法。传入 `'hello'`，得到 `'HELLO'`，最后由 `print` 打印出来。

注意：`'search'` 是字典的键，`search` 是变量名。变量换成 `obj` 也一样：

```python
obj = services['search']
return obj.query(text)
```