`search` gets the object through the dictionary lookup you just learned:

```python
search = services['search']
```

Earlier, this line created a `Search` object and stored it under the key `'search'`:

```python
services['search'] = Search()
```

So inside `handle`, `services['search']` retrieves that same object, and the local variable `search` refers to it. It doesn’t create a new object.

Then `search.query(text)` calls that object’s `query` method. With `'hello'`, it returns `'HELLO'`.