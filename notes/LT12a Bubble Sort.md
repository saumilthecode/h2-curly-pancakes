> [!summary] Quick View
> Compare **adjacent** pairs, swap any out of order, repeat. `O(n²)`, or `O(n)` best case if **optimised**.
> Syllabus 2.2.1. Scope, Big-O and the cross-sort comparison are in [[LT12 Sorting Algorithms]].

## One Pass

`[24, 5, 36, 18, 12]`:

| `i` | Compare | | After |
| --- | ------- | - | ----- |
| 0 | `24`, `5` | swap | `5, 24, 36, 18, 12` |
| 1 | `24`, `36` | — | `5, 24, 36, 18, 12` |
| 2 | `36`, `18` | swap | `5, 24, 18, 36, 12` |
| 3 | `36`, `12` | swap | `5, 24, 18, 12, 36` |

The loop ends at `len(seq) - 2`, or `seq[i + 1]` runs off the end.

## All Passes

`[8, 3, 6, 9, 5]`, sorted part **bold**:

| Pass | Array |
| ---- | ----- |
| 1 | `3, 6, 8, 5,` **`9`** |
| 2 | `3, 6, 5,` **`8, 9`** |
| 3 | `3, 5,` **`6, 8, 9`** |
| 4 | **`3, 5, 6, 8, 9`** |

`n` items need **`n - 1`** passes. One pass places the largest remaining element at the end, so the sorted region grows from the **right**.

## Three Versions

| Version | Inner loop | Outer loop |
| ------- | ---------- | ---------- |
| Simple | all `n - 1` pairs every pass | fixed count |
| Improved | **one fewer pair** each pass | `n - 1` passes |
| Optimised | one fewer pair each pass | **stops** on a swap-free pass |

```python
def simple_bubblesort(seq):
    for ijk in range(len(seq)):
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq

def improved_bubblesort(seq):
    n = len(seq)
    for pass_num in range(n - 1):
        for i in range(n - 1 - pass_num):          # tail already sorted
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq

def optimised_bubblesort(seq):
    n = len(seq)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        if not swapped:
            break
    return seq
```

## Comparisons Counted

Q11 on the notebook's own lists, `n = 6`:

| List | Simple | Improved | Optimised |
| ---- | ------ | -------- | --------- |
| `[5,4,3,2,1,0]` reversed | 30 | 15 | 15 |
| `[5,4,0,1,2,3]` | 30 | 15 | **12** |
| `[3,0,2,4,1,5]` | 30 | 15 | **14** |
| `[0,1,2,3,4,5]` sorted | 30 | 15 | **5** |

Simple always makes `n(n-1)` comparisons; improved makes `n(n-1)/2` — the sum `(n-1) + (n-2) + ... + 1`. Only **optimised** responds to the data, and its `swapped` flag is what gives the `O(n)` best case.

| Best | `O(n)` **optimised only** |
| --- | --- |
| Average / worst | `O(n²)`, worst is a reversed list |
| In-place | yes |
| Stable | yes |

## Exam

> [!important] Describe bubble sort
> Required keywords: **pass**, **compare**, **repeat**, **adjacent**, **swap** — and describe the first three passes.
> **Compare** each **adjacent** pair along the list, **swapping** them if they are out of order. That is one **pass**, and it leaves the largest value at the end. **Repeat** on the remaining unsorted part, one fewer element each time, until a pass makes no swaps.

## Common Mistakes

- Inner loop to `len(seq)` not `len(seq) - 1` — `seq[i + 1]` goes out of range.
- Claiming an `O(n)` best case without saying **optimised**; simple and improved cannot stop early.
- Counting `n` passes instead of `n - 1`.

## Related

- [[LT12 Sorting Algorithms]]
- [[LT12b Insertion Sort]]
- [[LT5 Iteration]]
