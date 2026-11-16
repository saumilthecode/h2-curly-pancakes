> [!summary] Quick View
> Reading pseudocode and turning it into Python. Paper 1 writes algorithms this way, and Paper 2 sometimes hands you pseudocode to code up.

## Pseudocode → Python

| Pseudocode | Python |
| ---------- | ------ |
| `x ← 5` or `x <- 5` or `x = 5` | `x = 5` |
| `IF m = 1` | `if m == 1:` |
| `IF x <> -1` | `if x != -1:` |
| `IF … THEN … ELSE … ENDIF` | `if …:` / `else:` |
| `ELSE IF` | `elif` |
| `WHILE Lo <= Hi AND …` … `ENDWHILE` | `while lo <= hi and …:` |
| `FOR i <- 2 TO n` … `ENDFOR` | `for i in range(2, n + 1):` |
| `FOR counter = 1 to m` … `NEXT counter` | `for counter in range(1, m + 1):` |
| `FOR element in lst:` | `for element in lst:` |
| `REPEAT` … `UNTIL cond` | `while True:` … `if cond: break` |
| `FUNCTION F(m: INTEGER) RETURNS INTEGER` … `ENDFUNCTION` | `def F(m):` |
| `PROCEDURE P(Index: INTEGER)` … `ENDPROCEDURE` | `def P(index):` (returns nothing) |
| `RETURN x` | `return x` |
| `OUTPUT x` | `print(x)` |
| `LENGTH(Seq)` | `len(seq)` |
| `APPEND element TO Left` | `left.append(element)` |
| `< Code to Swap Seq[Lo] with Seq[Hi] >` | `seq[lo], seq[hi] = seq[hi], seq[lo]` |

> [!warning] Four traps
> - `=` inside an `IF` is a **comparison**. Write `==`.
> - `//` after code can be a **comment** (`// Search upwards …`), but `LENGTH(Seq) // 2` is floor division. Read the context.
> - `FOR … TO n` **includes** `n`, so `range` needs `n + 1`.
> - LT12b and LT12c pseudocode index arrays from **1**. Python starts at `0`.

## Exam

> [!important] Specimen 2027 P1 Q1(a)(ii): rewrite a `FOR` loop as a `WHILE` loop `[4]`
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

## Related

- [[LT12b Insertion Sort]]
- [[LT12c Selection Sort]]
- [[LT11b Binary Tree]]
- [[LT5 Iteration]]
