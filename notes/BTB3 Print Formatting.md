> [!summary] Quick View
> Making output line up: separators, line endings, column width, alignment and decimal places.

## `print()` Options

| Option | Controls | Example |
| ------ | -------- | ------- |
| `sep` | what goes **between** the values | `print(192, 168, 1, 1, sep=".")` |
| `end` | what goes **after** the line | `print(i, end=" ")` |
| `file` | where the output goes | `print("hi", file=f)` |

```python
print("a", "b")                     # a b     - space is the default sep
print("a", "b", sep="")             # ab
print(192, 168, 178, 42, sep=".")   # 192.168.178.42

for i in range(4):
    print(i, end=" ")               # 0 1 2 3   - no line breaks
```

Sending output to a file:

```python
f = open("data.txt", "w")
print("Print output to file.", file=f)
f.close()
```

## `format()`

```text
"{0:<8}".format(value)
   | |+- width 8
   | +-- align left
   +---- which value (index 0)
```

| Format | Meaning |
| ------ | ------- |
| `{0:8}` | width 8, default alignment |
| `{0:<8}` | left aligned in width 8 |
| `{0:>8}` | right aligned in width 8 |
| `{0:^8}` | centred in width 8 |
| `{0:6.2f}` | float, width 6, **2 decimal places** |

By default strings align left and numbers align right.

```text
{0:6.2f}
 |  | |+- f = float
 |  | +-- 2 decimal places
 |  +---- total width 6
 +------- value index 0
```

## Table Pattern

Fixed widths make the columns line up.

```python
prices = [("shirt", 12), ("pen", 1.5), ("cake", 4.56789)]

print("{0:<8}{1:<10}{2:>8}".format("Index", "Item", "Price"))

for i, item in enumerate(prices, 1):
    print("{0:<8}{1:<10}{2:>8.2f}".format(i, item[0], item[1]))
```

```text
Index   Item         Price
1       shirt        12.00
2       pen           1.50
3       cake          4.57
```

> [!example]- How the widths line up
> ```text
> print("{0:<8}{1:<10}{2:>8.2f}".format(1, "cake", 4.56789))
>
> 1       cake          4.57
> +--8---++---10---++--8---+
> ```
>
> | Part | Meaning |
> | ---- | ------- |
> | `{0:<8}` | value 0, left aligned, width 8 |
> | `{1:<10}` | value 1, left aligned, width 10 |
> | `{2:>8.2f}` | value 2, right aligned, width 8, 2 decimals |
>
> The value overflows its column rather than being cut off if it is too wide.

Convert values read from a file before formatting them:

```python
height = float(student[2])
weight = float(student[3])
bmi = weight / (height ** 2)

print("{0:<8}{1:<12}{2:>10.2f}".format(i, name, bmi))
```

## Common Mistakes

- `{0:6.2f}` means width `6`, **not** 6 decimal places.
- Using `.2f` on a string read from a file or `input()` — convert with `float()` first.
- Expecting `sep` to work inside a single string; it only goes between separate arguments.
- Forgetting `end` **replaces** the newline, so the next print continues on the same line.

## Related

- [[LT1 basic python]]
- [[BTB2 File Handling]]
