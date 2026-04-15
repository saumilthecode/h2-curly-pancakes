> [!info] Main Idea
> Break a big problem into smaller reusable functions.

## Function Template

```python
def name(formal_parameters):
    # body / logic
    return value
```

## Parts of a Function

- `name` is the name of the function.
- `formal_parameters` are the inputs listed in the function definition.
- The body is the actual logic.

## Return and Type Hints

```python
def add(x: int, y: int) -> int:
    return x + y
```

- `return` sends a value back to the code that called the function. It is not the same as `print`.
- Type hints such as `x: int` and `-> int` help readability, but Python does not enforce them by default.

## Scope

> [!note] Scope Rule
> Local variables only exist inside the function where they are created.

- Global scope cannot use local variables from inside a function.
- Local scope can access global variables, unless it is trying to reassign them.
- One local scope cannot access another function's local variables.
- You can use the same variable name in different scopes.

## Built-in Immutable Values

Built-in data types include `int`, `float`, `bool`, and `str`.
Values like numbers and strings are immutable. Variables are names that can be reassigned to different values.

## Related

- [[basic python]]
- [[Conditionals]]
