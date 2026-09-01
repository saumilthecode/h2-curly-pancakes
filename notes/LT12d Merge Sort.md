> [!summary] Quick View
> Halve until every piece holds one element, then merge pairs back in order. `O(n log n)` in **every** case, but **not in-place**.
> Syllabus 2.2.1. Scope, Big-O and the cross-sort comparison are in [[LT12 Sorting Algorithms]].

```mermaid
flowchart TD
  A["5 2 1 8 9"] --> B["5 2"]
  A --> C["1 8 9"]
  B --> D["5"]
  B --> E["2"]
  C --> F["1"]
  C --> G["8 9"]
  G --> H["8"]
  G --> I["9"]
```

| Merge | Result |
| ----- | ------ |
| `[5]` + `[2]` | `[2, 5]` |
| `[8]` + `[9]` | `[8, 9]` |
| `[1]` + `[8, 9]` | `[1, 8, 9]` |
| `[2, 5]` + `[1, 8, 9]` | `[1, 2, 5, 8, 9]` |

```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:                    # <= keeps it stable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]           # one side is empty

def merge_sort(seq):
    if len(seq) < 2:                               # a 1-element list is sorted
        return seq
    mid = len(seq) // 2
    return merge(merge_sort(seq[:mid]), merge_sort(seq[mid:]))
```

`merge` only ever reads the **front** of each list, so merging costs `n`, not `n²`.

| Best / average / worst | `O(n log n)` — always splits and merges the same way |
| --- | --- |
| In-place | **no** — builds new lists |
| Stable | yes |

Every case is identical because *"regardless of whether the original array is sorted or not, we will have to go through the same process of splitting and merging it back"*. Halving `n` to 1 takes `log n` levels, each doing `n` work.

## Common Mistakes

- Forgetting the base case, or writing `len(seq) == 1` and looping forever on an empty list.
- Calling merge sort in-place. It is the one sort here that is not.

## Related

- [[LT12 Sorting Algorithms]]
- [[LT12e Quick Sort]]
- [[LT9a Recursion]]
