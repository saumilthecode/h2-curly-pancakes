> [!summary] Quick View
> `for` repeats a **known** number of times. `while` repeats **until a condition fails**.

## `for` vs `while`

| | `for` | `while` |
| --- | ----- | ------- |
| Use when | you know how many repeats | you don't know how many repeats |
| Driven by | a sequence | a condition |
| Counter | handled for you | you must update it yourself |
| Typical risk | off-by-one bounds | infinite loop |

> [!important] `if` vs `while`
> `if` runs its body **at most once**. `while` runs its body **repeatedly** while the condition stays `True`.

## `for` Loop

```python
for var_name in sequence:
    # body
```

| Form | Produces |
| ---- | -------- |
| `range(9)` | `0` to `8` |
| `range(3, 9)` | `3` to `8` |
| `range(3, 9, 2)` | `3, 5, 7` |
| `for ch in "Singapore"` | each character |
| `for i in range(len(s))` | each index, when you need the position |

`start` is included, `stop` is excluded, `step` is the interval.

## `while` Loop

```python
while condition:
    # body
```

```python
total = 0
while total < 5:
    total = total + 1
```

## Loop Control

- `break`: exit the loop immediately.
- `continue`: skip the rest of this iteration, go to the next one.

```python
for i in range(9):
    if i % 2 == 0:
        continue      # skip evens
    print(i)          # 1 3 5 7
```

```text
        for i in range(9):
              |
   +--------> i = next value from range          range exhausted
   |          |                                        |
   |          v                                        v
   |   if i % 2 == 0:  -- true --> continue --+     loop ends
   |          |                               |
   |          | false                         |
   |          v                               |
   |       print(i)                           |
   |          |                               |
   +----------+<------------------------------+

   break, anywhere in the body, jumps straight to "loop ends"
```

## Accumulator Pattern

Set up a variable before the loop, update it inside, return it after.

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
```

> [!example]- Trace table for `factorial(6)`
> | `i` | `result` after the step |
> | --- | ---------------------- |
> | - | `1` |
> | `1` | `1` |
> | `2` | `2` |
> | `3` | `6` |
> | `4` | `24` |
> | `5` | `120` |
> | `6` | `720` |
>
> Returns `720`.

Same thing with `while`:

```python
def factorial(n):
    result = 1
    counter = 1
    while counter <= n:
        result = result * counter
        counter = counter + 1
    return result
```

## Infinite Loops

The condition must eventually become `False` (or the body must `break`).

```python
value = 9
while value != 0:     # 9, 7, 5, 3, 1, -1, -3 ... never exactly 0
    value = value - 2
```

Use `while value > 0:`. An infinite loop hangs the cell: interrupt the kernel (■), restart it if that fails, then `print()` inside the loop to trace the variable.

> [!important] Promo P2 Task 1: input validation in 2024, 2025 and the Mock
> **2024 T1.1** `[2]`: re-prompt until `10 <= x <= 100`. 1m `while x < 10 or x > 100:` · 1m input again inside the loop.
>
> **2025 T1.1** `[4]`: collect 9 valid scores. A `for` loop with no validation capped at **2m**. A `while` loop without validation, **3m**.
>
> **2026 Mock T1** `[4+2]`: 1m re-prompt until the name is non-empty with no digit · 1m re-prompt until the item count is 1 to 6 · 1m keep going until that many readings are stored · 1m check each reading is 0 to 100 before appending. Then 1m average rounded to 1 d.p. · 1m count readings `>= 70` and display everything. The scheme's name check:
>
> ```python
> while inspector == "" or any(character.isdigit() for character in inspector):
>     inspector = input("Invalid name. Inspector name: ")
> ```
>
> Readings `42, 75, 68, 91, 54` give average `66.0` and `2` items needing attention.

## Common Mistakes

- Hardcoding a value where the parameter should be used (`range(10)` instead of `range(n)`).
- Off-by-one: forgetting `stop` is excluded, so `range(1, n)` misses `n`.
- Putting `return` **inside** the loop body, so it exits on the first iteration.
- Forgetting to update the counter in a `while` loop.
- Starting a **product** at `0`, which makes everything zero. Sums start at `0`, products at `1`.

## Related

- [[LT2 Conditionals]]
- [[LT9a Recursion]]
- [[LT7 Lists]]
- [[LT4b Types of Errors and Test Cases]]
