`search` 通过 `services['search']` 这个键值查找，拿到了之前放进字典的 `Search` 实例。连起来看就是：

```python
services['search'] = Search()
```

这里先执行 `Search()`，创建一个对象，再把它作为值存进 `services`，对应的键是字符串 `'search'`。

接着，`handle` 运行到：

```python
search = services['search']
```

它用同一个键 `'search'` 取出那个对象，让局部变量 `search` 指向它。**这里没有新建或复制对象，拿到的还是之前存进去的那个。**

注意这两个名字的角色：`'search'` 是字典的键，`search` 是函数里的变量名。变量换个名字也一样：

```python
obj = services['search']
return obj.query(text)
```

回到原代码，`search.query(text)` 就是在调用那个对象的 `query` 方法。传入 `'hello'` 后返回 `'HELLO'`，最后由 `print` 打印出来。