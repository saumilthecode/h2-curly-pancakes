> [!summary] Quick View
> The five sorts, and how to choose between them. One note each:
> [[LT12a Bubble Sort]] · [[LT12b Insertion Sort]] · [[LT12c Selection Sort]] · [[LT12d Merge Sort]] · [[LT12e Quick Sort]]

> [!important] Syllabus scope
> | Ref | Outcome |
> | --- | ------- |
> | 2.2.1 | implement **insertion, bubble, quicksort, merge** sorts |
> | 2.2.3 | compare efficiencies using Big-O, **worst case** — *Exclude: space complexity* |
>
> **Selection sort is not in 2.2.1**; the video list marks LT12c *[OPTIONAL]*.
> Asked in 2020 Q2, 2022 Q4(e), 2023 Q6, specimen 2027 P1 Q5.

## Big-O

How the work grows with `n`. Constants and smaller terms are dropped, so `n(n-1)/2` is `O(n²)`. A log's base is only a constant factor, so `O(log n)` needs no base.

```mermaid
%%{init: {"themeVariables": {"xyChart": {"plotColorPalette": "#e74c3c, #2980b9, #16a085"}}}}%%
xychart-beta
    title "red n^2 --- blue n log n --- teal n"
    x-axis "n" [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    y-axis "operations" 0 --> 400
    line "n^2" [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
    line "n log n" [2, 8, 15.5, 24, 33.2, 43, 53.3, 64, 75.1, 86.4]
    line "n" [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

| `n` | `n` | `n log n` | `n²` |
| --- | --- | --------- | ---- |
| 10 | 10 | 33 | 100 |
| 100 | 100 | 664 | 10,000 |
| 1000 | 1000 | 9,966 | **1,000,000** |

No sort here is `O(log n)`. That last cell is the bubble sort warning: *"n = 1000 elements... 1 million comparisons"*.

> [!important] Growth is not speed
> Big-O ignores constant overhead, so `O(n log n)` can lose on small inputs. Lecture timings, 1000 random lists each:
>
> | `n` | Bubble | Improved | Merge |
> | --- | ------ | -------- | ----- |
> | 10 | 391 ns | 322 ns | **770 ns** |
> | 100 | 28 µs | 19 µs | **8 µs** |
> | 1000 | 3 ms | 2 ms | **0.1 ms** |
> | 5000 | 77 ms | 51 ms | **0.65 ms** |

2.2.3 also covers [[LT11a Search|search]] — linear `O(n)`, binary `O(log n)`.

## In-Place and Stable

| | Meaning |
| --- | ------- |
| **In-place** | sorted items use the **same storage** — no second list built |
| **Stable** | equal elements keep their **relative order** |

> [!warning] Stability is a property of the code, not the algorithm
> *"Did the code swap even when two elements are equal?"* `>` is stable, `>=` is not.

One pass of each `O(n²)` sort:

| Sort | One pass | Sorted end |
| ---- | -------- | ---------- |
| [[LT12a Bubble Sort\|Bubble]] | largest remaining **bubbles to the end** | right |
| [[LT12b Insertion Sort\|Insertion]] | one element **joins the sorted prefix** | left |
| [[LT12c Selection Sort\|Selection]] | smallest remaining is **swapped to the front** | left |

## Comparison

| | Best | Average | **Worst** | In-place | Stable |
| --- | ---- | ------- | --------- | -------- | ------ |
| [[LT12a Bubble Sort\|Bubble]] (optimised) | `O(n)` | `O(n²)` | `O(n²)` | yes | yes |
| [[LT12b Insertion Sort\|Insertion]] | `O(n)` | `O(n²)` | `O(n²)` | yes | yes |
| [[LT12c Selection Sort\|Selection]] | `O(n²)` | `O(n²)` | `O(n²)` | yes | no |
| [[LT12d Merge Sort\|Merge]] | `O(n log n)` | `O(n log n)` | `O(n log n)` | **no** | yes |
| [[LT12e Quick Sort\|Quicksort]] | `O(n log n)` | `O(n log n)` | **`O(n²)`** | yes | no |

Nearly sorted → insertion or optimised bubble. Guaranteed performance → merge, the only `O(n log n)` worst case. Tight memory → anything but merge. Order of equal items matters → not selection, not quicksort.

> [!example]- 1280 books, one second per comparison
> Bubble 818,560 comparisons — **nine days**. Insertion about half — **five days**. Quicksort **under 3½ hours**.

## Exam Answers

The comparative questions. Single-algorithm ones sit in each sort's own note.

> [!important] 2020 Q2(c) — largely sorted data: insertion over quicksort `[4]`
> Insertion runs `O(n)` on nearly sorted data — each element is near its place, so the inner loop exits after a comparison or two. Quicksort with a first/last pivot hits its **worst case** `O(n²)` on that same input. Insertion also has no recursion overhead and is stable.

> [!important] 2022 Q4(e) — merge over quicksort in a fixed-capacity array `[2]`
> Merge is `O(n log n)` in every case; quicksort degrades to `O(n²)` on bad splits. A fixed array of **ordered** data is exactly quicksort's worst case.

## Common Mistakes

- Judging stability from the algorithm's name instead of the code.
- Giving a best case without saying which **version** of bubble sort.
- Quoting quicksort's average `O(n log n)` when 2.2.3 asks for the **worst** case.

## Related

- [[LT11a Search]]
- [[LT9a Recursion]]
- [[LT11b Binary Tree]]
- [[LT7 Lists]]
