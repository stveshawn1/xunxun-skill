In `handle`, this line gets the object from the dictionary:

```python
search = services['search']
```

Earlier, this line created a `Search` object and stored it under the key `'search'`:

```python
services['search'] = Search()
```

So `services['search']` looks up that same object, and the local variable `search` now refers to it. No new object is created by the lookup.

Then `search.query(text)` calls that object’s `query` method. With `'hello'`, it returns `'HELLO'`.