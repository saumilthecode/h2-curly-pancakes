> [!summary] Quick View
> Print formatting = controlling separators, newlines, alignment, width, and decimal places so output is readable.

## Print Playground

<iframe class="note-widget-frame print-format" src="./pictures/print-format.html" title="Interactive print formatting playground" style="width:100%;height:600px;border:1px solid #d8d3ca;border-radius:8px;background:#fff;"></iframe>

[Open standalone print formatting playground](./pictures/print-format.html)

## `print()` Basics

`print()` can output several values.

```python
value = 3.564
print("a = ", value)
print("b = ", value + 10)
```

By default:

- values are separated by a space
- each `print()` ends with a newline
- output goes to the screen

## `sep`

`sep` controls what goes between values.

```python
print("a", "b")                 # a b
print("a", "b", sep="")         # ab
print(192, 168, 178, 42, sep=".")  # 192.168.178.42
print("a", "b", sep=":-)")      # a:-)b
```

Use `sep` when the values are already separate arguments.

## `end`

`end` controls what comes after a `print()`.

```python
for i in range(4):
    print(i)
```

Output:

```text
0
1
2
3
```

Same loop, one line:

```python
for i in range(4):
    print(i, end=" ")
```

Output:

```text
0 1 2 3
```

With arrows:

```python
for i in range(4):
    print(i, end=" -> ")
```

Output:

```text
0 -> 1 -> 2 -> 3 ->
```

## `file`

`file` sends printed output somewhere else, like a text file.

```python
f = open("data.txt", "w")
print("Print output to file.", file=f)
f.close()
```

Safer pattern:

```python
with open("data.txt", "w") as file:
    print("Print output to file.", file=file)
```

## `format()` Placeholders

`format()` puts values into `{}` placeholders.

```python
name = "Bob"
score = 17

print("{} scored {}".format(name, score))
```

Numbered placeholders:

```python
print("{0} scored {1}".format(name, score))
```

## Width

Width reserves a fixed number of spaces.

```python
print("{0:8}{1:15}".format("Index", "Name"))
```

Meaning:

- `{0:8}` means first value uses width `8`
- `{1:15}` means second value uses width `15`
- fixed width helps columns line up

Example:

```python
names = ["Albert", "Bob", "Chloe", "Desmond", "Eve"]

print("{0:8}{1:15}".format("Index", "Name"))
i = 1

for name in names:
    print("{0:8}{1:15}".format(str(i), name))
    i += 1
```

## Alignment

Alignment goes before the width.

| Format | Meaning |
| ------ | ------- |
| `{0:<8}` | left align in width 8 |
| `{0:>8}` | right align in width 8 |
| `{0:^8}` | centre align in width 8 |

Strings are usually left aligned by default. Numbers are usually right aligned by default.

## Decimal Places

Use `.2f` for two decimal places.

```python
price = 4.56789
print("{0:6.2f}".format(price))  #  4.57
```

Breakdown:

```text
{0:6.2f}
  0   value index
  6   total width
 .2   two decimal places
  f   float
```

## Table Pattern

```python
prices = [("shirt", 12), ("pen", 1.5), ("cake", 4.56789)]

print("{0:8}{1:10}{2:>6}".format("Index", "Item", "Price"))
i = 1

for item, price in prices:
    print("{0:8}{1:10}{2:6.2f}".format(str(i), item, price))
    i += 1
```

## CSV Table Pattern

```python
import csv

print("{0:<8}{1:<12}{2:<10}{3:>10}{4:>10}{5:>10}".format(
    "Index", "Name", "Gender", "Height", "Weight", "BMI"
))

with open("data.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    i = 1

    for student in reader:
        name = student[0]
        gender = student[1]
        height = float(student[2])
        weight = float(student[3])
        bmi = weight / (height ** 2)

        print("{0:<8}{1:<12}{2:<10}{3:>10.2f}{4:>10.2f}{5:>10.2f}".format(
            i, name, gender, height, weight, bmi
        ))

        i += 1
```

## Common Mistakes

- Forgetting that `end` replaces the newline.
- Using `sep` after joining everything into one string.
- Forgetting the colon in `{0:8}`.
- Mixing up width and decimal places in `{0:6.2f}`.
- Not converting input/file values to `float` before numeric formatting.

## Related

- [[basic python]]
- [[File Handling]]
