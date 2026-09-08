`search` gets the object by looking up the key `'search'` in the `services` dictionary.

Earlier, this line creates a `Search` object and stores it under that key:

```python
services['search'] = Search()
```

Then, inside `handle`, this line retrieves that same object and gives it the local name `search`:

```python
search = services['search']
```

It doesn’t create or copy an object. Both the dictionary entry and the local variable refer to the same object.

So `search.query(text)` calls that object’s `query` method. With `text` equal to `'hello'`, it returns `'HELLO'`, which the final line prints.