回到这一行：

```python
search = services['search']
```

它从字典 `services` 中，用键 `'search'` 取出之前存进去的对象，再让变量 `search` 指向它。

那个对象是在这里创建并存入字典的：

```python
services['search'] = Search()
```

右边的 `Search()` 创建一个 `Search` 对象；左边把它存到 `'search'` 这个键下面。因此，`handle` 中的查找**不会创建新对象**，拿到的就是先前存入的那个对象。

接着：

```python
return search.query(text)
```

调用这个对象的 `query` 方法。这里传入的是 `'hello'`，所以最终打印 `HELLO`。