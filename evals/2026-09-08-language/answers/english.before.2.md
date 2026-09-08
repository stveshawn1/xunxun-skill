回到这一行：

```python
search = services['search']
```

`services['search']` 用键 `'search'` 从字典里取出对象，再让变量 `search` 指向它。这个对象是前面放进去的：

```python
services['search'] = Search()
```

这里 `Search()` 创建一个 `Search` 实例，也就是一个可以调用 `query` 方法的具体对象；赋值把它存到字典的 `'search'` 键下。

所以，`handle` 里的 `search` 拿到的是**之前创建的同一个对象**，没有再创建一个。接着：

```python
return search.query(text)
```

就调用这个对象的方法，把 `'hello'` 转成 `'HELLO'`。