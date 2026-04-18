> [!summary] Quick View
> A list is an ordered, mutable collection that allows duplicate values.

## Basics

- Lists use square brackets: `[]`
- Lists are mutable, so you can change their contents.
- Lists allow duplicate values.
- Empty lists are allowed: `[]`

## Creating Lists

```python
numbers = [1, 2, 3]
empty = []
```

```python
list(tup)      # converts a tuple to a list
list("abc")    # ['a', 'b', 'c']
list(range(5)) # [0, 1, 2, 3, 4]
```

## Access and Update

```python
lst = list(range(5))
lst[4] = 5
```

This changes the item at index `4` to `5`.

## Common Operations

- `in` checks whether an item is in the list.
- `not in` checks whether an item is not in the list.
- `len(lst)` gives the number of elements.
- `sum(lst)` adds the numerical elements in the list.
- `max(lst)` gives the largest element.
- `min(lst)` gives the smallest element.

> [!note]
> `max()` and `min()` work when the elements can be compared with each other. A mixed list of numbers and strings will cause an error.

## Useful Methods

```python
lst = [3, 1, 4, 7, 3]
```

- `lst.index(3)` gives the first position of `3`, which is `0`.
- `lst.index(5)` gives an error because `5` is not in the list.
- `lst.count(3)` gives the number of times `3` appears, which is `2`.
- `lst.reverse()` reverses the list in place.
- `lst.copy()` makes a copy of the list.

## Copying Lists

```python
copied = lst.copy()
```

Use `.copy()` when you want a new list instead of another variable pointing to the same list.

## Iteration

```python
for i in range(len(lst)):
    print(lst[i])
```

```python
for ele in lst:
    print(ele)
```

```python
while lst:
    lst.pop()
```

- `while lst:` runs while the list is not empty.
- This can be used as a self-destructing loop if you keep removing items.

## Adding Items

- `lst.append(value)` adds one item to the end and mutates the list.
- `lst.extend(values)` adds each item from another iterable to the end.
- `lst = lst + [value]` also adds an item, but creates a new list.

```python
lst.append("hi")     # adds "hi" as one item
lst.extend("hi")     # adds "h", "i"
```

- `.append()` adds the whole thing as one item.
- `.extend()` goes through the item in its brackets.

## Removing Items

- `lst.pop()` removes and returns the last item by default.
- `lst.pop(index)` removes and returns the item at that index.

```python
del lst[start:stop:step]
```

- `del lst[:]` clears the whole list.
- `lst.clear()` also clears the whole list.
- `del lst` deletes the variable itself.

## Sorting

- `sorted(lst)` returns a new sorted list.
- `lst.sort()` sorts the same list in place.

## Related

- [[Tuple]]
- [[Iteration]]
