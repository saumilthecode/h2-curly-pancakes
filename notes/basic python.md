> [!summary] Quick View
> Core ideas for types, operators, comparisons, booleans, and slicing.

## Types

| Type  | Meaning                  |
| ----- | ------------------------ |
| int   | whole number             |
| float | decimal number           |
| bool  | `True` / `False`         |
| str   | string / text            |
| None  | no value / null-like     |

##  Functions and Methods

| Function / method | What it does                                      |
| ----------------- | ------------------------------------------------- |
| `type(x)`         | finds the type of `x`                             |
| `s.upper()`       | makes a string uppercase                          |
| `s.lower()`       | makes a string lowercase                          |
| `s.index(value)`  | finds the index of `value` inside a string        |
| `ord(char)`       | gives the Unicode number of a character           |
| `s.isdigit()`     | checks if a string contains only digits           |

## Type Conversion

| Function   | What it does                                  |
| ---------- | --------------------------------------------- |
| `str(x)`   | turns `x` into a string                       |
| `float(x)` | turns `x` into a float                        |
| `int(x)`   | turns `x` into an integer, removing decimals  |

## Assignment

```python
a = 10
```

The value `10` is assigned to the variable `a`.

## Arithmetic Operators

`*` on a string repeats it a number of times.

| Operator | Meaning                                 |
| -------- | --------------------------------------- |
| `+`      | plus                                    |
| `-`      | minus                                   |
| `*`      | multiply                                |
| `**`     | to the power of                         |
| `/`      | divide and return a float               |
| `//`     | floor divide / round down               |
| `%`      | remainder only                          |

## Comparison Operators

| Operator | Meaning                         |
| -------- | ------------------------------- |
| `>`      | left is greater than right      |
| `<`      | left is less than right         |
| `==`     | equal to                        |
| `!=`     | not equal to                    |
| `>=`     | greater than or equal to        |
| `<=`     | less than or equal to           |

Examples:

```python
42 == 42      # True
42 == 42.0    # True, same numeric value
42 == "42"    # False, number vs string
```

## Logical and Membership Operators

| Operator | Meaning                                      |
| -------- | -------------------------------------------- |
| `and`    | `True` if both sides are `True`              |
| `or`     | `True` if either side is `True`              |
| `not`    | flips `True` to `False`, or `False` to `True` |
| `in`     | checks if a value exists inside something    |
| `not in` | checks if a value does not exist inside it   |

## Booleans

| Boolean | Numeric value |
| ------- | ------------- |
| `True`  | `1`           |
| `False` | `0`           |

## Slicing

```python
text = "HelloWorld"

text[start:end:step]
text[2:5:1]  # "llo"
```

- `start` is where the slice begins.
- `end` is where the slice stops, but it is not included.
- `step` is the interval between characters.

Negative indexing counts from the back of the string.

## Related

- [[Conditionals]]
- [[Functions (functional abstraction)]]
