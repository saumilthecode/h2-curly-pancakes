> [!summary] Quick View
> Dictionary = mutable key-value lookup table.

## Basics

```python
{key1: value1, key2: value2, ...}
```

- Keys are unique and hashable.
- Values can be any type.
- Access is by key, not index.

## Creating

```python
{}
dict()
dict([("boys", 11), ("girls", 13)])
```

`dict()` can convert an iterable of key-value pairs:

- tuple of tuples
- list of tuples
- tuple of lists
- list of lists

## Access / Check / Update

```python
d[key]          # get value; KeyError if key missing
key in d        # checks keys only
d[key] = value  # add or update
del d[key]      # delete one entry
d.clear()       # delete all entries
```

## Iteration

```python
for key in d:
    print(d[key])

for key, value in d.items():
    print(key, value)
```

## Related

- [[Lists]]
- [[Tuple]]
- [[Iteration]]
