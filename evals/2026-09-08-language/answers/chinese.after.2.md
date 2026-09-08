回到 `handle` 里的这一行：

```python
search = services['search']
```

它从字典里取出先前存好的 `Search` 对象，再让局部变量 `search` 指向它。沿着代码看，分两步：

1. **创建并存入对象**
   ```python
   services['search'] = Search()
   ```
   `Search` 是类，`Search()` 创建一个实例；字典的 `'search'` 键保存对这个实例的引用。

2. **取出同一个对象**
   ```python
   search = services['search']
   ```
   `handle` 调用时，通过键找到那个实例，赋给局部变量 `search`。这里没有创建或复制对象。

接着：

```python
return search.query(text)
```

就调用这个实例的 `query` 方法。因此 `handle('hello')` 返回 `'HELLO'`，最后由 `print` 打印出来。

注意：`'search'` 是字典的键，`search` 是局部变量名，两者同名只是写法上的选择。改成 `obj = services['search']`，仍然能拿到同一个对象。