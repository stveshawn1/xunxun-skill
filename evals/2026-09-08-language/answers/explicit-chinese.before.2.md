`search` 通过 `services['search']`，取到了之前放进字典的那个对象。把存和取连起来看：

```python
services['search'] = Search()
```

这里先执行 `Search()`，创建一个 `Search` 对象，再把它放进 `services` 字典，键是字符串 `'search'`。

接着，`handle` 运行到：

```python
search = services['search']
```

右边按键 `'search'` 查出那个对象，左边让函数里的变量 `search` 指向它。**这里没有创建新对象，也没有复制对象。**

注意：`'search'` 是字典的键，`search` 是变量名；它们同名只是为了方便阅读。改成这样也一样：

```python
obj = services['search']
return obj.query(text)
```

所以后面的 `search.query(text)`，就是调用先前创建的那个对象的方法。传入 `'hello'`，返回 `'HELLO'`，最后由 `print` 打印出来。