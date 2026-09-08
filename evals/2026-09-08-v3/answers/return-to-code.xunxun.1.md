回到这行代码：

```python
search = services['search']
```

它用键 `'search'` 从字典 `services` 中取出之前存进去的对象，再让局部变量 `search` 指向它。

这个对象是在前面这行创建并存入字典的：

```python
services['search'] = Search()
```

这里 `Search()` 创建一个对象，`services['search'] = ...` 把它存到键 `'search'` 对应的位置。所以函数里取到的是**之前创建的同一个对象**，没有重新创建。

接下来：

```python
return search.query(text)
```

就是调用这个对象的 `query` 方法。传入 `'hello'`，得到 `'HELLO'`，最后由 `print` 打印出来。