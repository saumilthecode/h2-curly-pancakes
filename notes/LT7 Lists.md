> [!summary] Quick View
> A list is an **ordered, mutable** collection that allows duplicates.

## Collection Types

| Type | Ordered | Mutable | Duplicates |
| ---- | ------- | ------- | ---------- |
| Tuple `()` | yes | no | allowed |
| List `[]` | yes | yes | allowed |
| Dictionary `{k: v}` | by insertion | yes | keys must be unique |
| Set `set()` | no | yes | not allowed |

> [!warning]
> `{}` creates an empty **dictionary**. The empty set is `set()`.

## Creating

```python
numbers = [1, 2, 3]
empty = []

list((1, 2, 3))   # [1, 2, 3]   from a tuple
list("abc")       # ['a', 'b', 'c']
list(range(5))    # [0, 1, 2, 3, 4]
```

## Access and Update

```python
lst = list(range(5))    # [0, 1, 2, 3, 4]
lst[4]                  # 4
lst[2:]                 # [2, 3, 4]
lst[1:4:2]              # [1, 3]
lst[4] = 5              # lists are mutable
```

## Common Operations

| Operation | Result |
| --------- | ------ |
| `len(lst)` | number of elements |
| `sum(lst)` | total — numbers only |
| `max(lst)` / `min(lst)` | largest / smallest |
| `x in lst` | membership |
| `lst1 + lst2` | concatenation, new list |
| `lst * 3` | repetition |

> [!note]
> `max()` and `min()` need comparable elements. `sum(['a','b'])` and a mixed list of numbers and strings both raise errors.

## Methods

```python
lst = [3, 1, 4, 7, 3]
```

| Method | Does | Returns the item? |
| ------ | ---- | ----------------- |
| `lst.index(3)` | first position of `3` → `0`; error if absent | — |
| `lst.count(3)` | how many times `3` appears → `2` | — |
| `lst.append(x)` | add **one** item to the end | no |
| `lst.extend(seq)` | add **each** item of `seq` to the end | no |
| `lst.insert(i, x)` | insert `x` at index `i` | no |
| `lst.remove(x)` | remove the first `x`; error if absent | **no** |
| `lst.pop()` | remove and return the last item | **yes** |
| `lst.pop(i)` | remove and return item at index `i` | **yes** |
| `lst.reverse()` | reverse in place | no |
| `lst.copy()` | a new list with the same items | — |

### `append` vs `extend`

```python
a = [1, 2]
a.append("hi")         # a is now [1, 2, 'hi']; append returns None

b = [1, 2]
b.extend("hi")         # b is now [1, 2, 'h', 'i']; extend returns None

c = [1, 2]
c.append([3, 4])       # c is now [1, 2, [3, 4]]

d = [1, 2]
d.extend([3, 4])       # d is now [1, 2, 3, 4]
```

### `remove` vs `pop`

`remove` takes the **value**, `pop` takes the **index** — and only `pop` gives the item back.

## Deleting

```python
del lst[1:9:2]   # delete a slice
del lst[-1]      # delete one item
del lst[:]       # clear - same as lst.clear()
del lst          # delete the variable itself
```

## Sorting

- `sorted(lst)` returns a **new** sorted list, leaving `lst` alone.
- `lst.sort()` sorts **in place** and returns `None`.

## Copying vs Assigning

```python
lst2 = lst          # same list, two names - changing one changes both
lst2 = lst.copy()   # a genuinely separate list
```

## Iteration

```python
for ele in lst:            # when you only need the values
    print(ele)

for i in range(len(lst)):  # when you need the index
    print(lst[i])

while lst:                 # while lst is not empty
    lst.pop()
```

`while lst:` and `while len(lst) > 0:` mean the same thing.

## Common Mistakes

- Using `lst.remove(2)` when you meant index `2` — it removes the *value* `2`.
- Expecting `lst.sort()` to return the sorted list; it returns `None`.
- Assigning instead of copying, then wondering why both lists changed.
- Calling `.index()` or `.remove()` on a value that isn't there — both raise errors.

## Related

- [[LT6 Tuple]]
- [[LT8 Dictionary]]
- [[LT5 Iteration]]
- [[BTB2 File Handling]]
