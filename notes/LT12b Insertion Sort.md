> [!summary] Quick View
> Keep a sorted run at the front; take the next element and swap it leftwards into place. `O(n²)`, `O(n)` on nearly sorted data.
> Syllabus 2.2.1. Scope, Big-O and the cross-sort comparison are in [[LT12 Sorting Algorithms]].

Cards: the left hand is sorted, take one from the table and slide it in.

```text
sorted            unsorted
[ 8  23  45  78 | 32   56 ]
                  ^ insert this one
```

One pass moves one more element into the sorted prefix, so the sorted region grows from the **left**.

## Two Core Skills

1. Swap two elements into order.
2. Given a sorted run with one loose element at the end, swap it leftwards until it lands.

Skill 1 sorts the first two, skill 2 absorbs the rest.

```python
def insert(seq, i):                     # skill 2 - seq[:i] already sorted
    while i > 0 and seq[i - 1] > seq[i]:
        seq[i - 1], seq[i] = seq[i], seq[i - 1]
        i -= 1

def insertion_sort(seq):
    for i in range(1, len(seq)):
        insert(seq, i)
    return seq
```

> [!important]
> Stop at the **first** element that isn't bigger. `i > 0` must come first, or `seq[-1]` wraps to the end of the list.

| Best | `O(n)` — sorted already, no swaps |
| --- | --- |
| Average / worst | `O(n²)` |
| In-place | yes |
| Stable | yes |

## Exam

> [!important] Specimen 2027 P1 Q5(c) — complete the pass table `[4]`
> `swift kite plover avocet swallow` ascending.
>
> | Pass | List |
> | ---- | ---- |
> | 1 | `swift` `kite` `plover` `avocet` `swallow` *(given)* |
> | 2 | **`kite`** `swift` `plover` `avocet` `swallow` |
> | 3 | `kite` **`plover`** `swift` `avocet` `swallow` |
> | 4 | **`avocet`** `kite` `plover` `swift` `swallow` |
> | 5 | `avocet` `kite` `plover` **`swallow`** `swift` |
>
> One row per element absorbed. `swallow` < `swift` on the third letter.

> [!important] Specimen 2027 P1 Q5(d) — two factors affecting performance `[2]`
> The size of the data set, and how nearly sorted it already is.

## Related

- [[LT12 Sorting Algorithms]]
- [[LT12a Bubble Sort]]
- [[LT12e Quick Sort]]
