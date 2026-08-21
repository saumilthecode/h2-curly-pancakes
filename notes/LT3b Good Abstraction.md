> [!summary] Quick View
> Breaking a problem into small, well-named functions. Manage complexity by dividing and conquering.

The mechanics of writing a function — parameters, `return`, scope — are in [[LT3a Functional Abstraction|LT3a]].

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

The same bug, written two ways:

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

You check three short functions instead of re-reading one long expression.

## Why It Allows Reuse

`square()` is written once and used by anything that needs it.

```python
PI = 3.14159

def area_of_circle(r):
    return PI * square(r)      # no need to rewrite r * r
```

## Solving Problems

**Divide and conquer** — split a problem into smaller subproblems, since smaller problems are easier to solve.

**Wishful thinking (top-down)** — write the solution assuming the helper functions already exist, then go back and write them.

```python
def hypotenuse(a, b):
    return sqrt(square(a) + square(b))   # pretend both exist
```

Same technique drives [[LT9b Recursion (Application)|recursive]] solutions.

## Avoid Magic Numbers

Hardcoded constants are hard to change and hide their meaning. Name them instead.

```python
# magic numbers - what is 1000? what is 0.22?
def fare(distance):
    if distance <= 1000:
        return 3.0
    return 3.0 + 0.22 * ((distance - 1000) // 400)


# named constants - the rule reads itself, and a fare rise is one edit
STAGE1_METRES = 1000
START_FARE    = 3.0
BLOCK_METRES  = 400
BLOCK_FARE    = 0.22

def fare(distance):
    if distance <= STAGE1_METRES:
        return START_FARE
    return START_FARE + BLOCK_FARE * ((distance - STAGE1_METRES) // BLOCK_METRES)
```

## Common Mistakes

- Repeating a constant in several places instead of naming it once.
- One long function that does everything, so a bug could be on any line.
- Helper functions named `f`, `g`, `temp` — the decomposition stops helping if the names say nothing.

## Related

- [[LT3a Functional Abstraction]]
- [[LT10a Data Abstraction]]
- [[LT9b Recursion (Application)]]
- [[LT1 basic python]]
