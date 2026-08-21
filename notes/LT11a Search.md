> [!summary] Quick View
> **Linear search** checks every element — `O(n)`, works on any sequence.
> **Binary search** halves the range each step — `O(log n)`, **needs sorted data**.

## Python's Built-in Searches

| Method | Returns |
| ------ | ------- |
| `seq.count(x)` | how many times `x` occurs |
| `seq.index(x)` | index of the **first** occurrence only |
| `x in seq` | `True` / `False` |

> [!note]
> `index()` stops at the first match — `'mississippi'.index('i')` is `1`, not the later ones. It also **raises an error** if the item is absent; our own version returns `None` instead.

## Linear Search

Sequential: go through every element in turn. Works on unsorted data.

| Case | Comparisons |
| ---- | ----------- |
| Best | 1 — first element |
| Worst | `n` — last element, or not present at all |
| Order of growth | `O(n)` |

```python
def find(seq, item):            # exists?
    for element in seq:
        if element == item:
            return True
    return False

def index(seq, item):           # where?
    for i in range(len(seq)):
        if seq[i] == item:
            return i
    return None

def count(seq, item):           # how many?
    c = 0
    for element in seq:
        if element == item:
            c += 1
    return c
```

> [!important]
> `find` and `index` `return` **inside** the loop — as soon as there's a match, stop. `count` can only return **after** the loop, because it must see every element.

### Recursive Versions

Take the head, recurse on the tail.

```python
def find(seq, item):
    if len(seq) == 0:
        return False
    elif seq[0] == item:
        return True
    return find(seq[1:], item)

def count(seq, item):
    if len(seq) == 0:
        return 0
    elif seq[0] == item:
        return 1 + count(seq[1:], item)
    return count(seq[1:], item)

def index(seq, item):
    if len(seq) == 0:
        print("Item not found.")
        return 0
    elif seq[0] == item:
        return 0
    return 1 + index(seq[1:], item)
```

`count` and `index` both build their answer **on the way back up** — each level adds `1` to whatever the level below returned.

> [!warning]
> Recursive `index` can't return `None` when the item is missing: the caller would try `1 + None`. Returning `0` instead is ambiguous — it also means "found at position 0" — hence the `print`. The iterative version has no such problem.

## Binary Search

> [!warning] Precondition
> The sequence **must be sorted**. State this in any "describe the algorithm" answer — it's a mark.

Divide and conquer: compare the middle element to the **key**, then throw away the half it cannot be in. Repeat until found, or until the range is empty.

```text
seq   5   9  12  18  25  34  85 100 123 345
idx   0   1   2   3   4   5   6   7   8   9
      ^               ^                   ^
     lo              mid                 hi
```

### The Algorithm

1. `lo = 0`, `hi = len(seq) - 1`.
2. While `lo <= hi`:
3. `mid = (lo + hi) // 2` — **integer division**, an index can't be `4.5`.
4. If `seq[mid] == key` → found, return `True`.
5. If `key < seq[mid]` → search left: `hi = mid - 1`.
6. Else → search right: `lo = mid + 1`.
7. If `lo > hi` the range is empty — the key does not exist, return `False`.

| Order of growth | `O(log n)` |
| --------------- | ---------- |
| Why | each step halves the remaining elements |

### Trace Table

This is the examined format. Columns: `Low`, `High`, `Low <= High`, `Mid`, `Seq[Mid]`, `Key == Seq[Mid]`, `Key < Seq[Mid]`.

Searching `[5, 9, 12, 18, 25, 34, 85, 100, 123, 345]` for **key = 85**:

| Low | High | Low <= High | Mid | Seq[Mid] | Key == Seq[Mid] | Key < Seq[Mid] |
| --- | ---- | ----------- | --- | -------- | --------------- | -------------- |
| 0 | 9 | True | 4 | 25 | False | False |
| 5 | 9 | True | 7 | 100 | False | True |
| 5 | 6 | True | 5 | 34 | False | False |
| 6 | 6 | True | 6 | 85 | **True** | — |

> [!example]- Same list, key = 86 (not present)
> | Low | High | Low <= High | Mid | Seq[Mid] | Key == Seq[Mid] | Key < Seq[Mid] |
> | --- | ---- | ----------- | --- | -------- | --------------- | -------------- |
> | 0 | 9 | True | 4 | 25 | False | False |
> | 5 | 9 | True | 7 | 100 | False | True |
> | 5 | 6 | True | 5 | 34 | False | False |
> | 6 | 6 | True | 6 | 85 | False | False |
> | 7 | 6 | **False** | — | — | — | — |
>
> The search stops the moment `Low > High`. Only then can you say the key is **not** in the sequence. Note the last row still has to be written out — `Low > High` is the finding.

### Iterative Code

```python
def BinarySearch(seq, item):
    lo = 0
    hi = len(seq) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if seq[mid] == item:
            return True
        elif item < seq[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return False
```

### Recursive Code

A **helper function** carries `lo` and `hi`; the outer function just sets them up.

```python
def Search(seq, lo, hi, item):
    if lo > hi:                             # base case: empty range
        return False
    mid = (lo + hi) // 2
    if seq[mid] == item:                    # base case: found
        return True
    elif item < seq[mid]:
        return Search(seq, lo, mid - 1, item)
    else:
        return Search(seq, mid + 1, hi, item)

def BinarySearch(seq, item):
    return Search(seq, 0, len(seq) - 1, item)
```

> [!tip]
> Slicing (`seq[:mid]`) also works but loses the original indices, so you can't report *where* the item was. Passing `lo`/`hi` keeps them.

## Searching Records, Not Numbers

Real data is a sequence of records. You search on **one field** and return **another**.

```python
def binary_search(tup, student):
    low = 0
    high = len(tup) - 1
    while low <= high:
        mid = (low + high) // 2
        name = tup[mid][1]              # compare on the name field only
        if name == student:
            return tup[mid][0]          # return the class, not True
        elif name > student:
            high = mid - 1
        else:
            low = mid + 1
    return None
```

Three things change from the plain version:

- the comparison reads **one field** of the record, `tup[mid][1]`
- the data must be sorted **by that same field**
- it returns the useful value (or `None`), not `True`/`False`

`<` and `>` compare strings alphabetically, so the algorithm is unchanged — but the sort must be alphabetical too, or binary search will miss.

## Comparison

| | Linear | Binary |
| --- | ------ | ------ |
| Data must be sorted | no | **yes** |
| Order of growth | `O(n)` | `O(log n)` |
| Worst case on 1000 items | 1000 checks | 10 checks |
| Good for | small or unsorted data | large sorted data |

Compare with [[LT10d Hashing|Hashing]], which reaches an item in `O(1)` — but only if you have the key, and it cannot answer range questions. A [[LT11b Binary Tree|binary search tree]] gets the same `O(log n)` without needing the data sorted into an array first.

## Common Mistakes

- Using `/` instead of `//` for `mid` — gives a float, and `seq[4.5]` is a `TypeError`.
- `hi = mid` or `lo = mid` instead of `mid - 1` / `mid + 1` — the range stops shrinking and the loop never ends.
- Setting `hi = len(seq)` instead of `len(seq) - 1`.
- Forgetting `return` on the recursive call.
- Applying binary search to unsorted data — it will "work" and silently give wrong answers.
- Saying "not found" before `lo > hi`.

## Related

- [[LT9a Recursion]]
- [[LT5 Iteration]]
- [[LT7 Lists]]
- [[LT10d Hashing]]
- [[LT11b Binary Tree]]
