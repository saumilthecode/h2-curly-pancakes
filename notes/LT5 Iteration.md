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

- `break` — exit the loop immediately.
- `continue` — skip the rest of this iteration, go to the next one.

```python
for i in range(9):
    if i % 2 == 0:
        continue      # skip evens
    print(i)          # 1 3 5 7
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
> | — | `1` |
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

The condition must eventually become `False`.

```python
value = 9
while value != 0:     # 9, 7, 5, 3, 1, -1, -3 ... never exactly 0
    value = value - 2
```

Use `while value > 0:` instead. In Jupyter an infinite loop kills the kernel — restart it, then add a `print()` inside the loop to see what the variable is doing.

## Common Mistakes

- Hardcoding a value where the parameter should be used (`range(10)` instead of `range(n)`).
- Off-by-one: forgetting `stop` is excluded, so `range(1, n)` misses `n`.
- Putting `return` **inside** the loop body, so it exits on the first iteration.
- Forgetting to update the counter in a `while` loop.

## Related

- [[LT2 Conditionals]]
- [[LT9a Recursion]]
- [[LT7 Lists]]
- [[LT4b Types of Errors and Test Cases]]
