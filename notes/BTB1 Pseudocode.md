> [!summary] Quick View
> Reading pseudocode and turning it into Python. Every construct here comes from your papers and lectures: the 2023 and 2025 promos, the 2027 specimen, the 2020 A-Level, and LT12b/12c.

## Pseudocode → Python

| Pseudocode | Python | Seen in |
| ---------- | ------ | ------- |
| `x ← 5` or `x <- 5` or `x = 5` | `x = 5` | 2025 promo, LT12b, specimen |
| `IF m = 1` | `if m == 1:` | specimen |
| `IF x <> -1` | `if x != -1:` | 2020 A-Level |
| `IF … THEN … ELSE … ENDIF` | `if …:` / `else:` | 2025 promo |
| `ELSE IF` | `elif` | 2023 promo |
| `WHILE Lo <= Hi AND …` … `ENDWHILE` | `while lo <= hi and …:` | 2025 promo |
| `FOR i <- 2 TO n` … `ENDFOR` | `for i in range(2, n + 1):` | LT12b |
| `FOR counter = 1 to m` … `NEXT counter` | `for counter in range(1, m + 1):` | specimen |
| `FOR element in lst:` | `for element in lst:` | 2023 promo |
| `REPEAT` … `UNTIL cond` | `while True:` … `if cond: break` | LT12c |
| `FUNCTION F(m: INTEGER) RETURNS INTEGER` … `ENDFUNCTION` | `def F(m):` | specimen |
| `PROCEDURE P(Index: INTEGER)` … `ENDPROCEDURE` | `def P(index):` — returns nothing | 2020 A-Level |
| `RETURN x` | `return x` | all |
| `OUTPUT x` | `print(x)` | 2020 A-Level |
| `LENGTH(Seq)` | `len(seq)` | 2025 promo |
| `APPEND element TO Left` | `left.append(element)` | 2023 promo |
| `< Code to Swap Seq[Lo] with Seq[Hi] >` | `seq[lo], seq[hi] = seq[hi], seq[lo]` | 2025 promo |

> [!warning] Four traps
> - `=` inside an `IF` is a **comparison** — write `==`.
> - `//` after code is a **comment** in the 2025 pseudocode (`// Search upwards …`), but `length(seq) // 2` in the 2023 one is floor division. Read the context.
> - `FOR … TO n` **includes** `n`, so `range` needs `n + 1`.
> - LT12b and LT12c pseudocode index arrays from **1**. Python starts at `0`.

## Exam

> [!important] Specimen 2027 P1 Q1(a)(ii) — rewrite a `FOR` loop as a `WHILE` loop `[4]`
> ```text
> 01 FUNCTION IterSum(m: INTEGER, n: INTEGER) RETURNS INTEGER
> 02   total = 0
> 03   FOR counter = 1 to m
> 04      total = total + (n * counter)
> 05   NEXT counter
> 06   RETURN total
> 07 ENDFUNCTION
> ```
>
> The `WHILE` version must set up and move the counter itself:
>
> ```text
> total = 0
> counter = 1
> WHILE counter <= m
>     total = total + (n * counter)
>     counter = counter + 1
> ENDWHILE
> RETURN total
> ```

> [!important] Promo P2 — fill the blanks, then code it
> **2025 Task 5** — partition with the first element as pivot: A `Hi ← Hi - 1`, B swap `Seq[Lo]` and `Seq[Hi]`, C swap `Seq[Start]` and `Seq[Hi]`. Then `QuickSortHelper` A/B are the two recursive calls on `Start … Mid - 1` and `Mid + 1 … End`. See [[LT12e Quick Sort]].
>
> **2023 Task 5** — merge sort blanks A–H. See [[LT12d Merge Sort#Exam|LT12d]].
>
> **2023 P1 Q2(d)** — non-in-place quicksort blanks A–D. See [[LT12e Quick Sort#Exam|LT12e]].

## Related

- [[LT12b Insertion Sort]]
- [[LT12c Selection Sort]]
- [[LT11b Binary Tree]]
- [[LT5 Iteration]]
