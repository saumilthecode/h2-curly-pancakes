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

## Related

- [[Tuple]]
- [[Iteration]]
