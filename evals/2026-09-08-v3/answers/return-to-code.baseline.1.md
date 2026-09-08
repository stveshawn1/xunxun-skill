In `handle`, this line gets the object:

```python
search = services['search']
```

Earlier, the program put a `Search` object into the dictionary:

```python
services['search'] = Search()
```

`Search()` creates the object, and the dictionary stores it under the key `'search'`. Inside `handle`, `services['search']` looks up that same object and assigns it to the local variable `search`. It doesn’t create a new object.

Then `search.query(text)` calls that object’s `query` method, which turns `'hello'` into `'HELLO'`.