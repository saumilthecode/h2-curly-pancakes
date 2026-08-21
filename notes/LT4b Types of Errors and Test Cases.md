> [!summary] Quick View
> Three error categories: **syntax**, **runtime**, **logic**. Test data covers **normal**, **boundary** and **erroneous** values.

## Error Categories

| Category | When it shows up | Symptom |
| -------- | ---------------- | ------- |
| Syntax | before the code runs | Python refuses to run the file |
| Runtime | during execution | program crashes part-way |
| Logic | never — it runs fine | output is simply wrong |

### Syntax Errors

Invalid Python grammar.

```python
def double(x):
    return 2x        # invalid
```

Also: missing colon, unmatched bracket, wrong indentation.

### Runtime Errors

Valid code that fails while running.

| Cause | Example |
| ----- | ------- |
| Division by zero | `x / 0` |
| Undeclared variable | `x + k` where `k` was never assigned |
| Incompatible types | `"Answer: " + square(5)` |
| Wrong number of arguments | `square(3, 5)` for `def square(x)` |
| Runaway recursion | `factorial(-1)` never reaches the base case |

### Logic Errors

The program runs and produces an answer — the wrong one.

```python
def check(x):
    if x > 100:
        return 'Big'
    elif x > 2000:      # unreachable: anything > 2000 is already > 100
        return 'Very Big!'
```

Also: a missing `return` (function silently gives `None`), off-by-one loop bounds, and floating-point imprecision:

```python
((10) ** (1/2)) ** 2      # 10.000000000000002
```

## Debugging

- Read the error message — it names the line and the type.
- Check variable values; add `print()` at the top of a loop or function to trace them.
- Re-run with smaller or different inputs. Does the same error appear?
- Narrow it down systematically — eliminate what cannot be the cause.

> [!note]
> Debugging removes the bugs you found. It does not prove the program is error-free — the remaining bugs are just harder to find.

## Exception Handling

Catch errors instead of letting the program crash.

```python
try:
    f = open("data.txt")
    print(f.read())
    f.close()
except Exception as e:
    print("Could not read file:", e)
```

## Test Case Categories

| Category | Purpose |
| -------- | ------- |
| Normal | typical valid input, should be accepted |
| Boundary / extreme | valid values at the exact limits |
| Erroneous / abnormal | invalid input, should be rejected |
| Volume | large data, tests efficiency and response time |

```text
        erroneous  |  normal range  |  erroneous
       <-----------+----------------+----------->
                   0               100
                   ^                ^
                boundary        boundary
```

> [!warning] Why boundary tests exist
> The sample data given in a question often **misses the boundary**. If the rule is "60 and above" and no one in the data is exactly 60, then `age > 60` passes every provided test and is still wrong. Test the limit itself, not just values near it.

### Worked Example

For `percentage(score, total)`:

| Type | Test | Expected |
| ---- | ---- | -------- |
| Normal | `percentage(20, 80)` | `25.0` |
| Boundary | `percentage(0, 80)` | `0.0` |
| Boundary | `percentage(60, 60)` | `100.0` |
| Erroneous | `percentage(-10, 80)` | rejected |
| Erroneous | `percentage(120, 60)` | rejected |

```python
def percentage(score, total):
    if score < 0 or score > total:
        return 'Error'
    return (score / total) * 100
```

> [!tip] Write tests that answer themselves
> Print the **comparison**, not the result — then every passing test reads `True` and you never have to recompute the expected answer by hand.
>
> ```python
> print(percentage(20, 80) == 25.0)     # True
> print(percentage(60, 60) == 100.0)    # True
> ```
>
> Provided test cases are a floor, not a ceiling. Failing one usually means several others would fail too — write your own.

## Related

- [[LT4a Data validation and verification]]
- [[LT5 Iteration]]
- [[LT9a Recursion]]
