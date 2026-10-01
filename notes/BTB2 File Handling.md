> [!summary] Quick View
> Read/write text and CSV files using `open()` … `close()` or `with open(...)`. Follow the question's required form.

## Opening

```python
f = open("textfile.txt", "r")
data = f.read()
f.close()
```

> [!important] Make sure the file is closed
> If you use an explicit `open()`, include the matching `close()`. Your schemes give a mark for it:
>
> | Source | Wording |
> | ------ | ------- |
> | LS2 | `1m: both open and close` |
> | 2023 Promo P2 | `[1]open,read,close file` |
> | 2024 Promo P2 | `1m open and close` |
> | 2025 Promo P2 | `1m open and close` |
> | 2026 Mastery P2 | `1m open and close` |
>
> The y27 Reference Guide prints **both** styles, so either is fine. `with` closes the file for you, even if something goes wrong inside. The Mock Promo's own answer uses `with`.

| Mode | Does |
| ---- | ---- |
| `"r"` | read (the default), errors if the file is missing |
| `"w"` | write: creates the file, **overwrites** if it exists |
| `"a"` | append: creates the file if needed, otherwise adds to its end |

With `with`, do not call `close()` yourself:

```python
with open("output.txt", "w") as f:
    f.write("Output Line\n")
```

## Handling a Missing File

```python
try:
    with open("textfile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("The file does not exist.")
```

Catch **specific** exceptions; `except Exception` can hide bugs.

## Reading

| Method | Returns |
| ------ | ------- |
| `f.read()` | the whole file as one string |
| `f.read(n)` | the next `n` characters |
| `f.readline()` | one line, as a string |
| `f.readlines()` | every line, as a **list** |

```python
f = open("welcome.txt")
for line in f:                  # loop the file directly
    print(line.rstrip("\n"))
f.close()
```

> [!warning]
> Strip trailing `\n` with `.strip()` or `.rstrip("\n")` to prevent `print` adding blank lines.

## Writing and Appending

```python
f = open("writefile.txt", "w")
for i in range(10):
    f.write("This is line " + str(i) + "\n")
f.close()
```

`write()` takes a **string**. Convert numbers with `str()`, and add `\n` yourself.

Change `"w"` to `"a"` to append instead of overwrite.

## CSV Files

Comma-separated values: plain text, one row per line, fields separated by commas. Used by spreadsheets and databases. A `.txt` file may use another separator, such as a tab.

### With the `csv` Module

```python
from csv import reader

f = open("datafile.csv", "r")
content = reader(f)
next(content)                         # skip the header row

for name, gender, ht, wt in content:
    print(name, gender, ht, wt)
f.close()
```

Rows are **lists**. No header: omit `next(content)`. Without unpacking: use `for row in content:`.

```python
from csv import writer

fields = ["Name", "Class", "Level", "Score"]
data = [["Nick", "S15", "15", "5460"],
        ["Mary", "S16", "12", "6105"]]

f = open("records.csv", "w", newline="")
content = writer(f)
content.writerow(fields)          # one row
content.writerows(data)           # many rows
f.close()
```

> [!important]
> Use `newline=""` when writing, or on Windows the file gets a blank line between every row.

### Reading Manually

```python
def read_csv(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()

    data = ()
    for line in lines[1:]:            # [1:] skips the header
        row = line.strip().split(",")
        data += (tuple(row),)
    return data
```

- `.strip()` removes the newline
- `.split(",")` breaks the line into fields. Use `.split("\t")` for tab-separated files
- convert numbers as you go: `float(row[2])`
- this builds a **tuple** of tuples. For the exam's **list** of tuples, start with `data = []` and use `data.append(tuple(row))`

```text
one line, step by step

  "Ali,M,1.72,60\n"
        |  .strip()          drop the newline
        v
  "Ali,M,1.72,60"
        |  .split(",")       cut on the commas
        v
  ['Ali', 'M', '1.72', '60']        every field is still a string
        |  tuple()
        v
  ('Ali', 'M', '1.72', '60')
        |  records.append(...)   the exam wants a list of tuples
        v
  records = [('Ali', 'M', '1.72', '60'), ('Bea', 'F', '1.60', '52'), ...]
```

### Writing Manually

```python
def export(records, filename):
    f = open(filename, "w")
    f.write("Name,Gender,Height,Weight\n")
    for r in records:
        f.write(",".join(str(field) for field in r) + "\n")
    f.close()
```

> [!important] Promo P2: read a file into a list, every year
> | Paper | Task | Builds | Marks |
> | ----- | ---- | ------ | ----- |
> | 2023 | 3.1 | a list of **lists** (open and close were given) | `[5]` |
> | 2024 | 2.1 | a list of tuples | `[6]` |
> | 2025 | 2.1 | a list of tuples | `[6]` |
> | 2026 Mock | 2.1 | a list of tuples, `Area` left out, readings as `float` | `[4]` |
>
> What the schemes tick:
>
> | Step | Code |
> | ---- | ---- |
> | open **and close** (2024, 2025) | `f = open(filename)` … `f.close()` |
> | skip the header | `next(f)` or `lines[1:]` |
> | strip and split (2m in 2024) | `line.strip().split(',')` |
> | make a tuple | `tuple(line)` |
> | start a list and append | `result = []` … `result.append(tup)` |
>
> 2023 gave its mark for iterating instead of the tuple. The 2024 scheme's code builds `(line[0], line[1], line[3])`, which drops two scores the question asked for. Keep every field the question lists.
>
> Values come back as **strings**. The Mock gave 1m for converting the readings to numbers, and later tasks give a mark for `int()` or `float()`.

## Common Mistakes

- Opening with `"w"` when you meant `"a"`: it wipes the file.
- Forgetting `\n`, so everything lands on one line.
- Writing a number without `str()`.
- Forgetting the values read from a file are **strings**. Convert before doing arithmetic.
- Forgetting to skip the header row.

## Related

- [[LT7 Lists]]
- [[LT6 Tuple]]
- [[LT10a Data Abstraction]]
- [[BTB3 Print Formatting]]
