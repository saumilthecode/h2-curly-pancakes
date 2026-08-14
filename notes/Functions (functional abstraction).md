> [!summary] Quick View
> A function is a black box: you need to know **what** it does, not **how** it does it.

## Template

```python
def name(formal_parameters):
    # body
    return value
```

| Part | Meaning |
| ---- | ------- |
| name | what the function is called |
| formal parameters | names used in the body for the values passed in |
| body | the logic — must be indented (4 spaces) |
| `return` | sends a value back to the caller |

Type hints are optional and not enforced:

```python
def add(x: int, y: int) -> int:
    return x + y
```

## Black Box

```text
   arguments         ┌───────────────┐         returned value
   ───────────────▶  │   square(x)   │  ──────────────────▶
                     └───────────────┘
                  specification = WHAT it does   (you need this)
                  implementation = HOW it does it (hidden)
```

The same specification can have different implementations — all of these are a valid `square`:

```python
result = x * x
result = x ** 2
```

## `return` vs `print`

| | `return` | `print` |
| --- | -------- | ------- |
| Sends value back to caller | yes | no |
| Can be stored in a variable | yes | no |
| Shows on screen | no | yes |

```python
def square(x):
    print(x * x)     # displays, but returns None

square(square(2))    # TypeError — inner call gave back None
```

> [!warning]
> A function with no `return` returns `None`. `print` is for showing a human; `return` is for using the value later.

## Scope

> [!important] Local variables exist only inside the function that creates them.

1. Global scope **cannot** use local variables.
2. Local scope **can** read global variables.
3. One function's local scope cannot see another function's locals.
4. The same name can be reused in different scopes without clashing.

**Advantages of local over global variables:**

- Avoids name clashes — the same name can be reused safely elsewhere.
- Changes inside the function cannot break unrelated code.
- Makes the function self-contained, so it is easier to reuse and test.
- Memory is freed when the function ends.

## Good Abstraction

A good abstraction:

1. Makes it natural to think in tasks and subtasks
2. Makes programs easier to understand
3. Captures common patterns
4. Allows code to be reused
5. Hides implementation details
6. Separates specification from implementation
7. Makes debugging easier

Compare — the bug is far easier to find on the right:

```python
# one dense line                    # decomposed
def hypotenuse(a, b):               def square(x):
    return sqrt((a+a) * (b+b))          return x * x

                                    def sum_of_squares(x, y):
                                        return square(x) + square(y)

                                    def hypotenuse(a, b):
                                        return sqrt(sum_of_squares(a, b))
```

## Solving Problems

**Divide and conquer** — split a problem into smaller subproblems, since smaller problems are easier to solve.

**Wishful thinking (top-down)** — write the solution assuming the helper functions already exist, then go back and write them.

```python
def hypotenuse(a, b):
    return sqrt(square(a) + square(b))   # pretend both exist
```

## Avoid Magic Numbers

Hardcoded constants are hard to change and hide their meaning. Name them instead.

```python
# magic numbers                      # named constants
if distance <= 1000:                 STAGE1 = 1000
    return 3.0                       START_FARE = 3.0
elif distance <= 10000:              BLOCK = 400
    return 3.0 + 0.22 * ...
                                     if distance <= STAGE1:
                                         return START_FARE
```

## Common Mistakes

- Using `print` where `return` is needed.
- Forgetting `return`, so the function silently gives `None`.
- Trying to read a local variable from outside its function.
- Repeating a constant in several places instead of naming it once.

## Related

- [[basic python]]
- [[Conditionals]]
- [[Recursion]]
- [[Data Abstraction]]
