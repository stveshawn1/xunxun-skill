`search` gets the object through the dictionary lookup you just learned:

```python
search = services['search']
```

The object was created and stored earlier:

```python
services['search'] = Search()
```

That earlier line creates a `Search` object and stores it under the key `'search'` in `services`. Inside `handle`, `services['search']` retrieves **that same object**, and the local variable `search` refers to it. No new object is created by the lookup.

Then:

```python
return search.query(text)
```

calls that object’s `query` method. With `'hello'` as the input, it returns `'HELLO'`.

Here, `'search'` in quotes is the dictionary key; `search` without quotes is the local variable holding the retrieved object.