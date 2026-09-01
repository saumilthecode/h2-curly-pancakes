> [!summary] Quick View
> Find the **smallest** in the unsorted part, swap it to the front, move the boundary. Always `O(n²)`.
> Scope and the cross-sort comparison are in [[LT12 Sorting Algorithms]].

> [!warning] Not in outcome 2.2.1
> 2.2.1 names only insertion, bubble, quicksort and merge; the assessment is marked *[OPTIONAL]*. Its own preamble warns it *"may be tested during the A Level exam if the pseudocode/algorithm is given in a question"*, so learn to read the pseudocode below.
> Learn it for the contrast: the only `O(n²)` sort here that is **unstable**, and the only one with **no best case**.

```text
[ 1  2 | 6  4  7  3 ]      smallest of 6 4 7 3 is 3, swap with 6
[ 1  2  3 | 4  7  6 ]      boundary moves right
```

## Four Core Skills

Each question builds on the last.

1. `smallest(seq)` — return the smallest **value**, no `min()`.
2. `smallest(seq)` — return its **index** instead. The index is what a swap needs.
3. `swap_smallest(seq)` — swap that element with `seq[0]`.
4. `selection_sort(seq)` — repeat skill 3 on the shrinking unsorted tail.

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

Track the **index**, not the value — you cannot swap with a value you didn't locate.

## Pseudocode

```text
Count <- 1
WHILE Count < NumberOfItems
    Index <- Count
    Lowest <- MyList[Index]
    Pointer <- Count + 1
    REPEAT
        IF Lowest > MyList[Pointer]
            Lowest <- MyList[Pointer]
            Index <- Pointer
        ENDIF
        Pointer <- Pointer + 1
    UNTIL Pointer > NumberOfItems
    MyList[Count], MyList[Index] <- MyList[Index], MyList[Count]
    Count <- Count + 1
ENDWHILE
```

> [!important] WHILE vs REPEAT-UNTIL
> `WHILE` tests at the **start**, so the body may never run — you pass the condition to *enter*. `REPEAT-UNTIL` tests at the **end**, so the body always runs at least once — you pass the condition to *exit*. Python has no `REPEAT`; write `while True:` with `if <condition>: break` at the bottom.

> [!example]- Trace `MyList = [53, 21, 60, 18, 42, 19]`
> | `Count` | `Lowest` | `MyList` after the swap |
> | ------- | -------- | ----------------------- |
> | 1 | 18 | `18 21 60 53 42 19` |
> | 2 | 19 | `18 19 60 53 42 21` |
> | 3 | 21 | `18 19 21 53 42 60` |
> | 4 | 42 | `18 19 21 42 53 60` |
> | 5 | 53 | `18 19 21 42 53 60` |
>
> Pass 5 swaps an element with itself. The scan still ran — that is why there is no best case.

| Best / average / worst | `O(n²)` — the scan always runs to the end |
| --- | --- |
| In-place | yes |
| Stable | **no** |

Every case runs `n - 1` passes and `n(n-1)/2` comparisons — *"regardless of whether the list is sorted, you will still do the check"*.

> [!example]- Why it is unstable
> `5, 3, 6, 5, 9, 2, 7` — the smallest is `2`, so it swaps with the **first** `5`, which lands at index 5, behind the second `5`.
>
> ```text
> 5a  3  6  5b  9  2  7   ->   2  3  6  5b  9  5a  7
> ```
>
> Long-range swaps break stability; [[LT12a Bubble Sort|bubble]] and [[LT12b Insertion Sort|insertion]] only swap neighbours.

## Exam

> [!important] Describe selection sort
> Required keywords: **unsorted**, **repeat**, **swap**, **smallest**.
> Find the **smallest** value in the **unsorted** part of the list, **swap** it with the first unsorted element, then **repeat** on the rest until one element remains.

> [!example]- Sorting tuples, and counting comparisons
> People are `(gender, age)`; sort oldest first. Only the comparison flips — `>` instead of `<` on `item[1]`.
>
> ```python
> for j in range(i + 1, n):
>     comparisons += 1
>     if lst[j][1] > lst[biggest][1]:
>         biggest = j
> ```
>
> `n = 3` gives 3 comparisons, `n = 4` gives 6 — `n(n-1)/2`, independent of the data.

## Related

- [[LT12 Sorting Algorithms]]
- [[LT12a Bubble Sort]]
- [[LT12b Insertion Sort]]
