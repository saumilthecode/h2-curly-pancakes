> [!summary] Quick View
> A dictionary is a mutable **key → value** lookup table. Access is by key, never by index.

## Basics

```python
{'Name': 'James', 'Age': 18, 'Gender': 'M'}
```

| | Rule |
| --- | ---- |
| Keys | unique and **immutable** (`str`, `int`, `tuple`) |
| Values | any type, including lists, tuples and other dictionaries |
| Lookup | by key |

Also called an *associative array*. Python implements it with a [[LT10d Hashing|hash table]], which is why keys must be hashable and lookup is fast.

## Creating

```python
{}                                    # empty
dict()                                # empty
dict([('boys', 11), ('girls', 13)])   # from key-value pairs
```

`dict()` accepts any sequence of key-value pairs — list of tuples, tuple of tuples, list of lists.

## Access, Check, Update

```python
d[key]           # get value — KeyError if the key is missing
key in d         # checks KEYS only, never values
d[key] = value   # add if new, update if it exists
del d[key]       # delete one entry
d.clear()        # delete all entries
```

> [!warning]
> `in` searches keys. For `{'mains': 'chicken'}`, `'mains' in d` is `True` but `'chicken' in d` is `False`.

## Keys and Values

```python
list(d.keys())     # ['mains', 'dessert', 'sides']
list(d.values())   # the values
d.items()          # (key, value) pairs
```

## Iteration

```python
for key in d:                  # iterates over KEYS
    print(key, d[key])

for key, value in d.items():   # both at once
    print(key, value)
```

## Common Mistakes

- Using an index: `d[0]` looks for the *key* `0`, not the first entry.
- Expecting `in` to find a value.
- Using a list as a key — it's mutable, so it isn't allowed.
- Accessing a missing key directly instead of checking with `in` first.

## Related

- [[LT7 Lists]]
- [[LT6 Tuple]]
- [[LT10d Hashing]]
- [[LT10a Data Abstraction]]
