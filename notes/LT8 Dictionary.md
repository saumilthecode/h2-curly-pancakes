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
d[key]           # get value - KeyError if the key is missing
key in d         # checks KEYS only, never values
d[key] = value   # add if new, update if it exists
del d[key]       # delete one entry
d.clear()        # delete all entries
```

> [!warning]
> `in` searches keys. For `{'mains': 'chicken'}`, `'mains' in d` is `True` but `'chicken' in d` is `False`.

A value can itself be a dictionary — chain the keys to reach inside:

```python
cat = {'name': 'kitty', 'age': 4, 'stats': {'ht': 12.5, 'wt': 3.7}}
cat['stats']['ht']        # 12.5
cat['ht']                 # KeyError - 'ht' is not a top-level key
```

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

| Loop | Each item is |
| ---- | ------------ |
| `for k in d:` | a **key** — use `d[k]` for the value |
| `for v in d.values():` | a value |
| `for pair in d.items():` | a **tuple** `('apple', 4)` |
| `for k, v in d.items():` | the tuple, unpacked |

## Patterns

```python
def total(d):
    t = 0
    for value in d.values():
        t += value
    return t

def increase(d):
    for key in d:
        d[key] += 1        # mutates the dictionary passed in
    return d
```

**Counting** — the most examined dictionary use. Build the dictionary as you go: the first sighting creates the key, later ones add to it.

```python
def count(seq):
    result = {}
    for item in seq:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
```

```text
count([1,2,3,1,1,2,3,1,1,3,2])  ->  {1: 5, 2: 3, 3: 3}
count('mississippi')            ->  {'m': 1, 'i': 4, 's': 4, 'p': 2}
```

`result[item] += 1` on its own raises `KeyError` the first time, hence the `if`/`else`. The same shape counts words after `paragraph.split()`, or vowels only by wrapping the body in `if ch in 'aeiou':`.

Combining two dictionaries with the same keys:

```python
def average(result1, result2):
    result = {}
    for subject in result1:
        result[subject] = (result1[subject] + result2[subject]) / 2
    return result
```

## Common Mistakes

- Using an index: `d[0]` looks for the *key* `0`, not the first entry.
- Expecting `in` to find a value.
- Using a list as a key — it's mutable, so it isn't allowed.
- Accessing a missing key directly instead of checking with `in` first.
- `d[item] += 1` without creating the key first — `KeyError` on the first occurrence.
- Rebuilding a dictionary when the question says *return the mutated dictionary*, or mutating when it wants a new one. Read which is asked for.

## Related

- [[LT7 Lists]]
- [[LT6 Tuple]]
- [[LT10d Hashing]]
- [[LT10a Data Abstraction]]
