回到 `handle` 这条线：**`search` 通过字典里保存的引用，拿到之前创建的那个 `Search` 对象。**

先看对象放进去的地方：

```python
services['search'] = Search()
```

`Search()` 创建一个对象，随后字典把指向它的引用保存在键 `'search'` 下。“引用”表示通过它可以访问那个对象，对象本身不会被复制一份。

执行 `handle('hello')` 时：

```python
search = services['search']
```

右边取出这个引用，赋给函数里的局部变量 `search`。因此，**`search` 和 `services['search']` 指向同一个对象**；这里没有再次执行 `Search()`，也没有创建新对象。

接着：

```python
return search.query(text)
```

就调用这个对象的 `query` 方法，把 `'hello'` 转成 `'HELLO'` 并返回，最后由 `print` 输出。

这里 `'search'` 是字典的键，`search` 是局部变量名。它们恰好同名；局部变量改成 `s`，只要后面也用 `s.query(text)`，仍然拿到并使用同一个对象。