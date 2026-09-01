> [!summary] Quick View
> Find the version of the problem **one size smaller**, assume it is already solved, then write the single step that assembles the answer.

Theory — base case, recursion tree, call stack — is in [[LT9a Recursion|LT9a]].

## The Method

1. **Spot the smaller problem.** What does size `n` have in common with size `n - 1`? Sometimes it isn't obvious.
2. **Write the relationship.** `f(n) = <something> combined with f(n-1)`.
3. **Wishful thinking.** Assume `f(n-1)` already returns the right answer. Only write the combining step.
4. **Find the base case.** The smallest input whose answer you can state outright.

> [!important]
> Step 1 is the hardest; steps 2–4 are mechanical.

## Shrinking Patterns

| The smaller problem | Shrinks by | Typical shape |
| ------------------- | ---------- | ------------- |
| The rest of the string / list | drop `s[0]` or `s[-1]` | `s[0] + f(s[1:])` |
| A smaller number | `n - 1` | `n * f(n - 1)` |
| Two smaller numbers | `n-1` and `n-2` | `f(n-1) + f(n-2)` |
| A counter running down | `n - 1`, data changed each call | `f(transform(s), n - 1)` |
| One row up a triangle | `n-1` on both `n` and `r` | `f(n-1, r-1) + f(n-1, r)` |

## Pattern: Head + Rest of String

Handle the first character; recurse on everything after it.

```python
def remove_adj_dup(string):
    if len(string) <= 1:              # base case: 0 or 1 char, nothing adjacent
        return string
    if string[0] == string[1]:
        return remove_adj_dup(string[1:])          # drop the duplicate
    return string[0] + remove_adj_dup(string[1:])  # keep it, recurse on the rest
```

```text
remove_adj_dup('abbccdd')  ->  'abcd'
remove_adj_dup('100002')   ->  '102'
```

Base case is `<= 1`, not `== 0` — with one character left, `string[1]` does not exist.

## Pattern: Counter as a Second Parameter

The data changes each call and a counter says when to stop. **Two base cases**: the counter running out, and the data running out.

```python
def shift_left(string, n):
    if string == "" or n == 0:
        return string
    return shift_left(string[1:] + string[0], n - 1)   # move head to the tail

def shift_right(string, n):
    if string == "" or n == 0:
        return string
    return shift_right(string[-1] + string[:-1], n - 1)  # move tail to the head
```

```text
shift_left("12345", 2)   ->  "34512"
shift_right("12345", 2)  ->  "45123"
```

> [!note]
> The recursive call is the **whole** return value — nothing is left pending, so the stack does no work on the way back up. Contrast `factorial`, where a multiplication waits in every frame.

## Pattern: Two Recursive Calls

```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:            # two base cases - the recurrence reaches back two steps
        return 1
    return fib(n - 1) + fib(n - 2)
```

> [!warning] Why `fib` is slow
> Each call spawns two more, so the tree grows exponentially and the same values are recomputed many times. `fib(5)` alone calls `fib(2)` three times.
>
> ```mermaid
> flowchart TD
>   f5["fib(5)"] --> f4["fib(4)"]
>   f5 --> f3b["fib(3)"]
>   f4 --> f3a["fib(3)"]
>   f4 --> f2c["fib(2)"]:::dup
>   f3a --> f2a["fib(2)"]:::dup
>   f3a --> f1a["fib(1)"]
>   f3b --> f2b["fib(2)"]:::dup
>   f3b --> f1b["fib(1)"]
>   classDef dup stroke-width:2px,stroke-dasharray:4 3
> ```
>
> The dashed nodes are the same call recomputed — `fib(2)` three times.
>
> The iterative version is `O(n)`.

**General rule:** the recurrence reaches back `k` steps, so you need `k` base cases.

```python
def f(n):
    if n < 3:                                        # covers n = 0, 1, 2 in one line
        return n
    return f(n - 1) + 2 * f(n - 2) + 3 * f(n - 3)
```

`n < 3` covers all three base values in one test, and handles negatives — `f(-1)` returns `-1`.

## Pattern: Building a List

Wrap the current item in a list and concatenate the recursive result.

```python
def collatz(n):
    if n == 1:
        return [1]                      # base case: sequence ends
    if n % 2 == 0:
        return [n] + collatz(n // 2)
    return [n] + collatz(3 * n + 1)
```

```text
collatz(3)  ->  [3, 10, 5, 16, 8, 4, 2, 1]
```

> [!important]
> Use `//`, not `/`.
>
> | | Result |
> | --- | ------ |
> | `n // 2` | `[3, 10, 5, 16, ...]` |
> | `n / 2` | `[3.0, 10.0, 5.0, ...]` — floats |
>
> Tests still pass (`3.0 == 3`), so this one slips through silently.

Same shape for a tuple: `return (n,) + collatz(...)`.

## Pattern: Two Shrinking Parameters

Pascal's triangle — each entry is the sum of the two above it.

```python
def choose(n, r):
    if r == 0 or n == r:        # the 1s down both edges
        return 1
    return choose(n - 1, r - 1) + choose(n - 1, r)
```

```text
                1                 row 0
              1   1               row 1
            1   2   1             row 2
          1   3   3   1           row 3
        1   4   6   4   1         row 4

4C2 = 3C1 + 3C2 = 3 + 3 = 6
```

The base case is the **edge** of the triangle, not a single value — both `r == 0` and `n == r` must be caught, or the recursion walks off the side.

> [!example]- More from the training set
> Alternating recurrence — different rules for odd and even:
>
> ```python
> def recursive_sum(x):
>     if x < 3:
>         return 1
>     elif x % 2 == 0:
>         return recursive_sum(x-1) + recursive_sum(x-2) + recursive_sum(x-3)
>     return recursive_sum(x-1) + recursive_sum(x-2)
> ```
>
> ```text
> recursive_sum(3) = rs(2) + rs(1)         = 1 + 1  = 2
> recursive_sum(4) = rs(3) + rs(2) + rs(1) = 2 + 1 + 1 = 4
> recursive_sum(6) = rs(5) + rs(4) + rs(3) = 6 + 4 + 2 = 12
> ```

## Choosing the Base Case

| Recursion shrinks by | Base case is |
| -------------------- | ------------ |
| slicing a string / list | empty, or short enough that the comparison still works |
| counting `n` down | `n == 0` |
| reaching back `k` terms | `k` separate values, or one `n < k` test |
| two parameters | the **edges** of the grid |

> [!warning]
> Test the base case against the *smallest legal input*, not a convenient one. `len(string) == 0` looks right until the recursive step reads `string[1]`.

## Common Mistakes

- Missing a base case when the recurrence reaches back more than one step.
- `/` instead of `//`, quietly turning integers into floats.
- Returning `[n] + f(...)` from one branch but `n + f(...)` from another — the types must match.
- Leaving a debugging `print()` in the submitted function.

## Related

- [[LT9a Recursion]]
- [[LT5 Iteration]]
- [[LT10b Stack]]
- [[LT11a Search]]
