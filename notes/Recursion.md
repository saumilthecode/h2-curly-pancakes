> [!summary] Quick View
> Recursion = solve a problem by solving a smaller version of the same problem.

## Must Have

- base case
- recursive call
- movement toward the base case
- remember to `return`

## Factorial Shape

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

## Tracing

- frame expansion
- trace tree diagram
- arrows down go first
- arrows up are returns

![[recursion.png]]

## Debugging

If it never reaches the base case, it keeps recursing until maximum recursion depth.

Add `print(n)` at the start to see whether the input is moving toward the base case.

## Related

- [[Functions (functional abstraction)]]
- [[Iteration]]
