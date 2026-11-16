> [!summary] Quick View
> Breaking a problem into small, well-named functions. Manage complexity by dividing and conquering.

The mechanics of writing a function (parameters, `return`, scope) are in [[LT3a Functional Abstraction|LT3a]].

## What Makes an Abstraction Good

A good abstraction:

1. Makes it natural to think in tasks and subtasks
2. Makes programs easier to understand
3. Captures common patterns
4. Allows code to be reused
5. Hides implementation details
6. Separates specification from implementation
7. Makes debugging easier

> [!tip]
> A "state three advantages of using functions" question is answered from this list.

## Why It Makes Debugging Easier

```python
# dense - buried in one expression
def hypotenuse(a, b):
    return sqrt((a + a) + (b + b))


# decomposed - the bug is visibly in square()
def square(x):
    return x + x                      # should be x * x

def sum_of_squares(x, y):
    return square(x) + square(y)

def hypotenuse(a, b):
    return sqrt(sum_of_squares(a, b))
```

## Why It Allows Reuse

`square()` is written once and used by anything that needs it.

```python
PI = 3.14159

def area_of_circle(r):
    return PI * square(r)      # no need to rewrite r * r
```

### Building on Helpers

The lesson's exercises stack one function on another, each trusting the one below:

```python
from math import pi

def circle_area(circum):
    if circum < 0:
        return None
    radius = circum / (2 * pi)
    return round(pi * square(radius), 3)        # circle_area(34) is 91.992

def bigger_sum2(x, y, z):                       # squares of the two larger numbers
    if x <= y and x <= z:                       # x is the smallest, so leave it out
        return sum_of_squares(y, z)
    elif y <= x and y <= z:
        return sum_of_squares(x, z)
    else:
        return sum_of_squares(x, y)             # bigger_sum2(6, -3, 8) is 100
```

`//` and `%` pull digits out of a number without turning it into a string. Digit 1 is the rightmost:

```python
def get_nth_digit(k, n):
    return (k // 10 ** (n - 1)) % 10            # get_nth_digit(123456, 2) is 5
```

`// 10 ** (n - 1)` drops the digits to the right. `% 10` keeps the last one left.

## Solving Problems

**Divide and conquer**: split a problem into smaller, easier subproblems.

**Wishful thinking (top-down)**: write the solution assuming the helper functions already exist, then go back and write them.

```python
def hypotenuse(a, b):
    return sqrt(square(a) + square(b))   # pretend both exist
```

```mermaid
flowchart TD
  h["hypotenuse(a, b)"] --> s["sum_of_squares(a, b)"]
  h --> r["sqrt"]
  s --> q1["square(a)"]
  s --> q2["square(b)"]
```

Write the top box first and assume the ones below it work. Then write those.

Same technique drives [[LT9b Recursion (Application)|recursive]] solutions.

## Avoid Magic Numbers

The lecture's taxi fare: **$3.00** for the first 1 km, **$0.22** per 400 m block or part of one up to 10 km, **$0.25** per block after that.

```text
 metres   0        1000                        10000  ->
          |---------|---------------------------|----------->
            $3.00     $0.22 per 400 m block       $0.25 per 400 m block
            flat      or part of one              or part of one

 3300 m    3.00 + 0.22 * ceil(2300/400) = 3.00 + 0.22 * 6  = 4.32
 10000 m   3.00 + 0.22 * ceil(9000/400) = 3.00 + 0.22 * 23 = 8.06
 14500 m   8.06 + 0.25 * ceil(4500/400) = 8.06 + 0.25 * 12 = 11.06
```

```python
from math import ceil

def taxi_fare(distance):                                  # metres
    if distance <= 1000:
        return 3.0
    elif distance <= 10000:
        return 3.0 + 0.22 * ceil((distance - 1000) / 400)
    else:
        return 8.06 + 0.25 * ceil((distance - 10000) / 400)
```

`ceil` because *"or less"* means a part block is charged in full. `taxi_fare(3300)` gives `4.32`, `taxi_fare(14500)` gives `11.06`.

Every literal there is a **magic number**. When fares change each one must be found and edited. Miss one and the code quietly returns the wrong fare.

`8.06` is the fare at 10 km, so compute it: call the function itself.

```python
def taxi_fare(distance):
    stage1     = 1000
    stage2     = 10000
    start_fare = 3.0
    increment1 = 0.22
    increment2 = 0.25
    block      = 400

    if distance <= stage1:
        return start_fare
    elif distance <= stage2:
        return start_fare + increment1 * ceil((distance - stage1) / block)
    else:
        return taxi_fare(stage2) + increment2 * ceil((distance - stage2) / block)
```

Raising the start fare to `$3.20`, or shrinking the block to 300 m, is now one edit.

> [!tip] The lecture's own caveat
> Naming every constant is *"yes and no"*: worth it for code that will be maintained, overkill for a function run once.

## Exam

> [!important] "State three advantages of using functions"
> Pick three from the list at the top, each with its reason:
> - **Reuse**: written once, called wherever it's needed, so there's less repeated code.
> - **Easier debugging**: each function can be tested on its own, so a bug is found in a small piece of code.
> - **Hides the details**: the caller only needs to know what the function does, not how.
> - **Easier to understand**: the problem is split into named tasks and subtasks.

## Common Mistakes

- Repeating a constant in several places instead of naming it once.
- One long function that does everything, so a bug could be on any line.
- Helper functions with meaningless names like `f`, `g`, `temp`.

## Related

- [[LT3a Functional Abstraction]]
- [[LT10a Data Abstraction]]
- [[LT9b Recursion (Application)]]
- [[LT1 basic python]]
