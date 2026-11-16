> [!summary] Quick View
> Keep a sorted run at the front. Take the next element and swap it leftwards into place. `O(n²)`, `O(n)` on nearly sorted data.
> Syllabus 2.2.1. Scope, Big-O and the cross-sort comparison are in [[LT12 Sorting Algorithms]].

| `8` | `23` | `45` | `78` | ==`32`== | `56` |
| --- | ---- | ---- | ---- | -------- | ---- |
| sorted | sorted | sorted | sorted | **insert next** | unsorted |

Each pass adds one element to the sorted prefix on the **left**.

## Two Core Skills

1. Swap two elements into order.
2. Given a sorted run with one loose element at the end, swap it leftwards until it lands.

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

## Pseudocode

Exam pseudocode **shifts** elements right. The Python above swaps them. Indexing starts at **1**.

```text
FOR Pointer <- 2 TO NumberOfItems
    ItemToBeInserted <- MyList[Pointer]
    CurrentItem <- Pointer - 1
    WHILE (MyList[CurrentItem] > ItemToBeInserted) AND (CurrentItem > 0)
        MyList[CurrentItem + 1] <- MyList[CurrentItem]
        CurrentItem <- CurrentItem - 1
    ENDWHILE
    MyList[CurrentItem + 1] <- ItemToBeInserted
ENDFOR
```

This is the lesson's pseudocode word for word. Once `CurrentItem` reaches `0` it still reads `MyList[0]`, which doesn't exist when indexing starts at 1. In Python put the index test first: `while i > 0 and seq[i - 1] > seq[i]`.

> [!example]- Trace `MyList = [53, 21, 60, 18, 42, 19]`
> | `Pointer` | `ItemToBeInserted` | `MyList` after |
> | --------- | ------------------ | -------------- |
> | 2 | 21 | `21 53 60 18 42 19` |
> | 3 | 60 | `21 53 60 18 42 19` |
> | 4 | 18 | `18 21 53 60 42 19` |
> | 5 | 42 | `18 21 42 53 60 19` |
> | 6 | 19 | `18 19 21 42 53 60` |
>
> `Pointer` 3 changes nothing; `60` is already past everything.
>
> Shifting puts `32` into a sorted run without losing it:
>
> | Step | `[0]` | `[1]` | `[2]` | `[3]` | `[4]` | `[5]` | `hold` |
> | ---- | ----- | ----- | ----- | ----- | ----- | ----- | ------ |
> | start | 8 | 23 | 45 | 78 | 32 | 56 | 32 |
> | `78 > 32`: copy right | 8 | 23 | 45 | 78 | ==78== | 56 | 32 |
> | `45 > 32`: copy right | 8 | 23 | 45 | ==45== | 78 | 56 | 32 |
> | `23 <= 32`: drop `32` in | 8 | 23 | ==32== | 45 | 78 | 56 | |
>
> The duplicate is normal. That slot is overwritten when `hold` goes back in.

## Comparisons Counted

`insertion_sort_comparison(seq)` counts every `seq[j-1] > seq[j]` test, including the failed one that ends the shift.

| List | Comparisons |
| ---- | ----------- |
| `[8,7,5,4,3,1]` reversed | 15 |
| `[7,1,3,5,8,4]` | 10 |
| `[1,3,5,4,8,7]` nearly sorted | 7 |

Reversed is the worst case, `n(n-1)/2 = 15` for `n = 6`. Sorted is `n - 1 = 5`: one failed test per element, which is the `O(n)` best case.

| Best | `O(n)` (sorted already, no swaps) |
| --- | --- |
| Average / worst | `O(n²)` |
| In-place | yes |
| Stable | yes |

## Exam

> [!important] Specimen 2027 P1 Q5(c): complete the pass table `[4]`
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

> [!important] Specimen 2027 P1 Q5(d): two factors affecting performance `[2]`
> The size of the data set, and how nearly sorted it already is.

## Related

- [[LT12 Sorting Algorithms]]
- [[LT12a Bubble Sort]]
- [[LT12e Quick Sort]]
