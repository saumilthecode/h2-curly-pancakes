> [!summary] Quick View
> Print formatting = making output line up: separators, newlines, column width, alignment, and decimal places.

## Print Playground

<iframe class="note-widget-frame print-format" src="./pictures/print-format.html" title="Interactive print formatting playground" style="width:100%;height:600px;border:1px solid #d8d3ca;border-radius:8px;background:#fff;"></iframe>

[Open standalone print formatting playground](./pictures/print-format.html)

## `print()` Options

| Option | Controls | Example |
| ------ | -------- | ------- |
| `sep` | gap between printed values | `print(192, 168, 1, 1, sep=".")` |
| `end` | what comes after this print | `print(i, end=" ")` |
| `file` | where output goes | `print("hi", file=f)` |

```python
print("a", "b")                 # a b
print("a", "b", sep="")         # ab
print(192, 168, 178, 42, sep=".")  # 192.168.178.42
```

```python
for i in range(4):
    print(i, end=" ")

# 0 1 2 3
```

File output:

```python
with open("data.txt", "w") as file:
    print("Print output to file.", file=file)
```

## `format()` Shape

Pattern:

```text
"{0:width}{1:width}".format(value0, value1)
```

Useful forms:

| Format | Meaning |
| ------ | ------- |
| `{0:8}` | value 0 uses width 8 |
| `{0:<8}` | left align in width 8 |
| `{0:>8}` | right align in width 8 |
| `{0:^8}` | centre align in width 8 |
| `{0:6.2f}` | float, width 6, 2 decimal places |

Breakdown:

```text
{0:6.2f}
 0    value index
 6    total width
.2    decimal places
 f    float
```

## Table Pattern

Use fixed widths for columns.

```python
prices = [("shirt", 12), ("pen", 1.5), ("cake", 4.56789)]

print("{0:<8}{1:<10}{2:>8}".format("Index", "Item", "Price"))

for i, item in enumerate(prices, 1):
    name = item[0]
    price = item[1]
    print("{0:<8}{1:<10}{2:>8.2f}".format(i, name, price))
```

Output shape:

```text
Index   Item         Price
1       shirt        12.00
2       pen           1.50
3       cake          4.57
```

## CSV Table Pattern

Same idea after reading values from a file:

```python
height = float(student[2])
weight = float(student[3])
bmi = weight / (height ** 2)

print("{0:<8}{1:<12}{2:>10.2f}".format(i, name, bmi))
```

## Common Mistakes

- `end` replaces the newline.
- `sep` only works between separate print arguments.
- `{0:6.2f}` means width `6`, not `6` decimal places.
- Convert file/input strings to `float` before using `.2f`.

## Related

- [[basic python]]
- [[File Handling]]
