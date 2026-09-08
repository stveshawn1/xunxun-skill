回到 `handle` 这条线：**`search` 从字典里拿到的是之前创建并存进去的那个 `Search` 对象。**

先看存入的地方：

```python
services['search'] = Search()
```

右边的 `Search()` 创建一个对象，左边把它存到 `services` 的 `'search'` 键下。

之后执行 `handle('hello')`，来到：

```python
search = services['search']
```

这里取出那个对象，让函数里的局部变量 `search` 指向它。**没有创建新对象，也没有复制对象。** `'search'` 是字典的键，`search` 是变量名；变量换个名字也能拿到同一个对象：

```python
obj = services['search']
```

接着：

```python
return search.query(text)
```

就是调用这个对象的 `query` 方法，把 `'hello'` 转成 `'HELLO'` 返回，最后由 `print` 打印出来。