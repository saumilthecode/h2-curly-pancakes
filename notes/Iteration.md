> [!summary] Quick View
> Use loops to repeat code. Python mainly uses `for` loops and `while` loops.

## `for` Loop

```python
for var_name in sequence:
    # code in the body of the loop
```

- A `for` loop goes through each item in a sequence.
- Common sequences include strings, lists, tuples, and `range(...)`.

## `range()`

```python
range(9)          # 0 to 8
range(start, stop, step)
```

- `start` is included.
- `stop` is not included.
- `step` is the interval.

## Loop Control

- `break` stops the loop immediately.
- `continue` skips the current iteration and moves to the next one.

## `while` Loop

```python
while expression:
    # body
```

- A `while` loop keeps running while the condition is `True`.

## Related

- [[Conditionals]]
- [[Lists]]
- [[Tuple]]
