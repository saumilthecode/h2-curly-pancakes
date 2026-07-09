> [!summary] Quick View
> File handling lets Python read from and write to external text and CSV files.

## Opening Files

```python
f = open("textfile.txt")      # read mode by default
f = open("textfile.txt", "r") # read mode explicitly
f.close()
```

Prefer `with open(...)` because it closes the file automatically.

```python
with open("textfile.txt", "r") as f:
    data = f.read()
```

## Exception Handling

```python
try:
    with open("textfile.txt", "r") as f:
        data = f.read()
        print(data)
except Exception as e:
    print(e)
```

If the file does not exist, Python raises a file-not-found error.

## Reading Text Files

| Method | Result |
| ------ | ------ |
| `read(size)` | reads into one string; `size` is optional |
| `readline()` | reads one line |
| `readlines()` | reads all lines into a list |

```python
with open("textfile.txt", "r") as f:
    content = f.read()
```

`content` is a string.

```python
with open("textfile.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip("\n"))
```

`lines` is a list. Each line may still contain the newline character `\n`.

You can also loop over the file object directly:

```python
with open("welcome.txt") as f:
    for line in f:
        print(line)
```

## Writing Text Files

```python
with open("writefile.txt", "w") as f:
    for i in range(10):
        f.write("This is line " + str(i) + "\n")
```

Mode `"w"`:

- creates the file if it does not exist
- overwrites the file if it already exists

## Appending Text Files

```python
with open("writefile.txt", "a") as f:
    for i in range(10):
        f.write("This is line " + str(i + 10) + "\n")
```

Mode `"a"` adds new content to the end of the existing file.

## CSV Files

CSV means comma-separated values.

- It is a plain text format.
- It is commonly used by spreadsheets and databases.
- Each row is stored as a line.
- Fields in a row are separated by commas.

TXT files may also store tabulated data using another separator, such as tabs.

```python
def openfile(filename):
    f = open(filename)
    result = ()

    for line in f:
        data = line.strip().split("\t")
        name = data[0]
        gender = data[1]
        height = float(data[2])
        weight = float(data[3])
        result += ((name, gender, height, weight),)

    f.close()
    return result
```

This creates a tuple of records from a tab-separated text file.

## Reading CSV Files

```python
from csv import reader

with open("datafile.csv", "r") as f:
    content = reader(f)
    for row in content:
        print(row)
```

Each `row` is a list.

To skip the header:

```python
from csv import reader

with open("datafile.csv", "r") as f:
    content = reader(f)
    next(content)

    for row in content:
        print(row)
```

To unpack fields:

```python
from csv import reader

with open("datafile.csv", "r") as f:
    content = reader(f)
    next(content)

    for name, gender, ht, wt in content:
        print(name, gender, ht, wt)
```

Manual CSV reading pattern:

```python
def read_csv(filename):
    file = open(filename)
    lines = file.readlines()
    data = ()

    for line in lines[1:]:
        line = line.strip()
        row = line.split(",")
        data = data + (tuple(row),)

    file.close()
    return data
```

- `lines[1:]` skips the header.
- `tuple(row)` stores each row as an immutable record.

## Writing CSV Files

```python
from csv import writer

fields = ["Name", "Class", "Level", "Score"]
data = [
    ["Nick", "S15", "15", "5460"],
    ["Mary", "S16", "12", "6105"],
    ["Peter", "S15", "10", "3700"],
]

with open("records.csv", "w", newline="") as f:
    content = writer(f)
    content.writerow(fields)
    content.writerows(data)
```

Use `newline=""` to avoid extra blank lines in the CSV file.

Manual CSV export pattern:

```python
def export(tup):
    f = open("data.csv", "w")
    f.write("Name,Gender,Height,Weight\n")

    for student in tup:
        f.write(str(student[0]) + "," + str(student[1]) + "," +
                str(student[2]) + "," + str(student[3]) + "\n")

    f.close()
```

## Related

- [[Lists]]
- [[Data Abstraction]]
- [[basic python]]
