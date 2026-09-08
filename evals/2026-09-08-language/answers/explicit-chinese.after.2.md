`search` 通过 `services['search']` 取到之前存进字典的那个对象。连起来看：

```python
services['search'] = Search()
```

这行先用 `Search()` 创建一个对象，再把它放进 `services` 字典，对应的键是字符串 `'search'`。

接着，调用 `handle('hello')` 时执行：

```python
search = services['search']
```

右边按键 `'search'` 查出那个对象，左边让函数里的变量 `search` 指向它。**这里没有创建新对象，取到的就是之前存进去的那个。**

注意，`'search'` 是字典的键，`search` 是变量名；它们不必同名。写成下面这样也一样：

```python
obj = services['search']
return obj.query(text)
```

回到原代码，`search.query(text)` 就是在调用这个对象的 `query` 方法，把 `'hello'` 转成 `'HELLO'`，最后由 `print` 打印出来。