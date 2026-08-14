> [!summary] Quick View
> Types, operators, booleans, strings and slicing — the building blocks everything else sits on.

## Types

| Type | Meaning | Example |
| ---- | ------- | ------- |
| `int` | whole number | `-3`, `45` |
| `float` | real number | `3.14` |
| `bool` | `True` / `False` | `True` |
| `str` | text, immutable | `"yijc"` |
| `None` | absence of a value | `None` |

`type(x)` returns the type of `x`.

## Type Conversion

| Call | Result |
| ---- | ------ |
| `str(123)` | `"123"` |
| `float("45.2")` | `45.2` |
| `int(23.8)` | `23` — truncates, does not round |
| `int("42")` | `42` |
| `int("42.5")` | **error** — string must look like an `int` |
| `int("yijc")` | **error** |

> [!warning]
> `int()` truncates towards zero: `int(1.99)` is `1`, not `2`. Use `round()` to round.

## Arithmetic Operators

| Operator | Meaning | Example |
| -------- | ------- | ------- |
| `+` `-` | add, subtract | |
| `*` `/` | multiply, divide (`/` always gives a float) | `11 / 3` → `3.666...` |
| `//` | floor divide | `11 // 3` → `3` |
| `%` | remainder / modulo | `11 % 3` → `2` |
| `**` | to the power of | `2 ** 3` → `8` |

## Comparison Operators

`==`  `!=`  `>`  `<`  `>=`  `<=` — all return a `bool`.

> [!important] `==` vs `=`
> `==` asks whether two values are the same. `=` assigns the value on the right to the name on the left.

```python
42 == 42      # True
42 == 42.0    # True  — same numeric value
42 == "42"    # False — number vs string
```

Strings compare by character code, so comparisons are alphabetical-ish, not by length:

```python
"Ten" > "One"    # True  — 'T' (84) > 'O' (79)
"FIVE" == 5      # False — str vs int
```

## Logical and Membership Operators

| Operator | `True` when |
| -------- | ----------- |
| `and` | both sides are `True` |
| `or` | either side is `True` |
| `not` | flips the value |
| `in` | value exists inside a sequence |
| `not in` | value does not exist inside it |

> [!example]- Truth tables
> | `a` | `b` | `a and b` | `a or b` |
> | --- | --- | --------- | -------- |
> | `True` | `True` | `True` | `True` |
> | `True` | `False` | `False` | `True` |
> | `False` | `True` | `False` | `True` |
> | `False` | `False` | `False` | `False` |
>
> `not True` → `False`, `not False` → `True`.

## Booleans and Truthiness

- `True` equals `1`, `False` equals `0`.
- Anything **not `0` and not empty** counts as `True` in a condition.
- So `while lst:` means "while `lst` is not empty".

> [!warning]
> Write `True` and `False` — not `true`, `false`, `"True"` or `"False"`.

## Strings

Single or double quotes both work. Pick the one that avoids clashing with the text:

```python
spam = "That is Alice's cat."   # fine
spam = 'That is Alice\'s cat.'  # also fine, escaped
```

### Escape Characters

| Escape | Prints as |
| ------ | --------- |
| `\'` | single quote |
| `\"` | double quote |
| `\t` | tab |
| `\n` | newline |
| `\\` | backslash |

### String Operations

```python
"Hello " + "World"   # 'Hello World'  — concatenation
"HELLO " * 3         # 'HELLO HELLO HELLO ' — repetition
"Hello" in "Hello World"   # True (case sensitive)
len("Hello World")   # 11
```

### Useful Methods

| Method | Does |
| ------ | ---- |
| `s.upper()` / `s.lower()` | change case |
| `s.index(value)` | position of `value`, error if absent |
| `s.isdigit()` / `s.isalpha()` | check contents |
| `ord(c)` / `chr(n)` | character ↔ code number |

## Slicing

```python
text = "abcdefgh"
text[start:stop:step]
```

- `start` is included, `stop` is **not**, `step` is the interval.
- Slicing always returns a **new** string.

Think of the index as a cursor sitting to the *left* of each character:

```text
 a  b  c  d  e  f  g  h
 |  |  |  |  |  |  |  |  |
 0  1  2  3  4  5  6  7  8
-8 -7 -6 -5 -4 -3 -2 -1

text[1:6]  -> "bcdef"     cut at 1, cut at 6
text[:2]   -> "ab"        start defaults to 0
text[::2]  -> "aceg"      every 2nd character
text[::-1] -> "hgfedcba"  negative step reverses
```

Negative indices count from the back: `text[-1]` is the last character.

## Comments

```python
# a single-line comment

"""
a documentation string
over multiple lines
"""
```

In Jupyter, `Ctrl` + `/` toggles comments on the selected lines.

## Common Mistakes

- Using `=` where `==` is meant.
- Forgetting `stop` is excluded from a slice.
- Expecting `int("3.5")` to work — it raises an error.
- Comparing a number to its string form: `42 == "42"` is `False`.

## Related

- [[Conditionals]]
- [[Functions (functional abstraction)]]
- [[Print Formatting]]
