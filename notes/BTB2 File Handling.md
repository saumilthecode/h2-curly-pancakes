> [!summary] Quick View
> Read from and write to external text and CSV files. In assessments, write the **explicit `open()` … `close()`** pair — that's how the mark is worded.

## Opening

```python
f = open("textfile.txt", "r")
data = f.read()
f.close()
```

> [!important] Always write the `close()`
> Closing is a **separately itemised mark point**, not a formality:
>
> | Source | Wording |
> | ------ | ------- |
> | Your LS2 mark scheme | `1m: both open and close` |
> | Cambridge 9618/42 Nov 2022 | *"closing the text file (in appropriate place)"* |
> | Cambridge 9618/42 Nov 2023 | *"Opening text file to read and closing the file in an appropriate place"* |
> | Cambridge 9618/43 Jun 2023 | *"Opening StackData.txt to read and closing file"* |
>
> Across seven published Cambridge Paper 4 mark schemes (2022–2024), **`with open(...)` does not appear once** — every Python model answer uses `X = open(...)` … `X.close()`.
>
> `with` is valid Python and the syllabus reference guide does show it. But the mark is written around an examiner seeing an open **and** a close, so write the explicit pair whenever it is being marked.

| Mode | Does |
| ---- | ---- |
| `"r"` | read — the default; errors if the file is missing |
| `"w"` | write — creates the file, **overwrites** if it exists |
| `"a"` | append — adds to the end of an existing file |

The `with` form, for reference — no `close()` is needed or expected inside it:

```python
with open("output.txt", "w") as f:
    f.write("Output Line\n")
```

## Handling a Missing File

```python
try:
    f = open("textfile.txt", "r")
    print(f.read())
    f.close()
except Exception as e:
    print(e)
```

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
> Lines keep their trailing `\n`. Strip it with `.strip()` or `.rstrip("\n")`, or `print` adds a blank line between rows.

## Writing and Appending

```python
f = open("writefile.txt", "w")
for i in range(10):
    f.write("This is line " + str(i) + "\n")
f.close()
```

`write()` takes a **string** — convert numbers with `str()`, and add `\n` yourself.

Change `"w"` to `"a"` to append instead of overwrite.

## CSV Files

Comma-separated values — plain text, one row per line, fields separated by commas. Used by spreadsheets and databases. A `.txt` file may use another separator, such as a tab.

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

Each row comes back as a **list**. Drop the `next(content)` line if there is no header, and use `for row in content:` if you don't want to unpack.

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
> Use `newline=""` when writing, or the file gets a blank line between every row.

### Reading Manually

Same job without the module — split each line yourself.

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
- `.split(",")` breaks the line into fields — use `.split("\t")` for tab-separated files
- convert numbers as you go: `float(row[2])`

### Writing Manually

```python
def export(records, filename):
    f = open(filename, "w")
    f.write("Name,Gender,Height,Weight\n")
    for r in records:
        f.write(",".join(str(field) for field in r) + "\n")
    f.close()
```

## Common Mistakes

- Opening with `"w"` when you meant `"a"` — it wipes the file.
- Forgetting `\n`, so everything lands on one line.
- Writing a number without `str()`.
- Forgetting the values read from a file are **strings** — convert before doing arithmetic.
- Forgetting to skip the header row.

## Related

- [[LT7 Lists]]
- [[LT6 Tuple]]
- [[LT10a Data Abstraction]]
- [[BTB3 Print Formatting]]
