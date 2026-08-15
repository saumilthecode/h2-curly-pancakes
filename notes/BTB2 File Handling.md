> [!summary] Quick View
> Read from and write to external text and CSV files. Prefer `with open(...)` — it closes the file for you.

## Opening

```python
with open("textfile.txt", "r") as f:
    data = f.read()
```

| Mode | Does |
| ---- | ---- |
| `"r"` | read — the default; errors if the file is missing |
| `"w"` | write — creates the file, **overwrites** if it exists |
| `"a"` | append — adds to the end of an existing file |

Without `with`, you must close it yourself:

```python
f = open("textfile.txt")
...
f.close()
```

## Handling a Missing File

```python
try:
    with open("textfile.txt", "r") as f:
        print(f.read())
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
with open("welcome.txt") as f:
    for line in f:              # loop the file directly
        print(line.rstrip("\n"))
```

> [!warning]
> Lines keep their trailing `\n`. Strip it with `.strip()` or `.rstrip("\n")`, or `print` adds a blank line between rows.

## Writing and Appending

```python
with open("writefile.txt", "w") as f:
    for i in range(10):
        f.write("This is line " + str(i) + "\n")
```

`write()` takes a **string** — convert numbers with `str()`, and add `\n` yourself.

Change `"w"` to `"a"` to append instead of overwrite.

## CSV Files

Comma-separated values — plain text, one row per line, fields separated by commas. Used by spreadsheets and databases. A `.txt` file may use another separator, such as a tab.

### With the `csv` Module

```python
from csv import reader

with open("datafile.csv", "r") as f:
    content = reader(f)
    next(content)                     # skip the header row

    for name, gender, ht, wt in content:
        print(name, gender, ht, wt)
```

Each row comes back as a **list**. Drop the `next(content)` line if there is no header, and use `for row in content:` if you don't want to unpack.

```python
from csv import writer

fields = ["Name", "Class", "Level", "Score"]
data = [["Nick", "S15", "15", "5460"],
        ["Mary", "S16", "12", "6105"]]

with open("records.csv", "w", newline="") as f:
    content = writer(f)
    content.writerow(fields)      # one row
    content.writerows(data)       # many rows
```

> [!important]
> Use `newline=""` when writing, or the file gets a blank line between every row.

### Reading Manually

Same job without the module — split each line yourself.

```python
def read_csv(filename):
    with open(filename) as f:
        lines = f.readlines()

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
    with open(filename, "w") as f:
        f.write("Name,Gender,Height,Weight\n")
        for r in records:
            f.write(",".join(str(field) for field in r) + "\n")
```

## Common Mistakes

- Opening with `"w"` when you meant `"a"` — it wipes the file.
- Forgetting `\n`, so everything lands on one line.
- Writing a number without `str()`.
- Forgetting the values read from a file are **strings** — convert before doing arithmetic.
- Forgetting to skip the header row.

## Related

- [[LT7 Lists|Lists]]
- [[LT6 Tuple|Tuple]]
- [[LT10a Data Abstraction|Data Abstraction]]
- [[BTB3 Print Formatting|Print Formatting]]
