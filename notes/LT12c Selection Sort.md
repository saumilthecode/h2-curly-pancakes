> [!summary] Quick View
> Find the **smallest** in the unsorted part, swap it to the front, move the boundary. Always `O(n²)`.
> Scope and the cross-sort comparison are in [[LT12 Sorting Algorithms]].

> [!warning] Not in outcome 2.2.1
> 2.2.1 names only insertion, bubble, quicksort and merge; the video list marks LT12c *[OPTIONAL]*. Learn it for the contrast — it is the only `O(n²)` sort here that is **unstable**, and the only one with **no best case**.

```text
[ 1  3 | 4  6  5  2 ]      smallest of 4 6 5 2 is 2, swap with 4
[ 1  3  2 | 6  5  4 ]      boundary moves right
```

```python
def selection_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if seq[j] < seq[smallest]:
                smallest = j
        seq[i], seq[smallest] = seq[smallest], seq[i]
    return seq
```

| Best / average / worst | `O(n²)` — the scan always runs to the end |
| --- | --- |
| In-place | yes |
| Stable | **no** |

Every case is the same because *"regardless of whether the list is sorted, you will still do the check"*.

> [!example]- Why it is unstable
> `[4a, 5, 3, 2, 4b, 1]` — the smallest is `1`, so it swaps with `4a`, throwing it behind `4b`. Long-range swaps break stability; [[LT12a Bubble Sort|bubble]] and [[LT12b Insertion Sort|insertion]] only swap neighbours.

## Related

- [[LT12 Sorting Algorithms]]
- [[LT12a Bubble Sort]]
- [[LT12b Insertion Sort]]
