In `handle`, this line gets the object from the dictionary:

```python
search = services['search']
```

Earlier, the program put a `Search` object there:

```python
services['search'] = Search()
```

`Search()` creates the object, and the dictionary stores it under the key `'search'`. Then `services['search']` retrieves that same object, and the local variable `search` refers to it—no new object is created.

So `search.query(text)` calls that object’s `query` method. With `'hello'`, it returns `'HELLO'`.