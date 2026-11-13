> [!summary] Quick View
> The **Reference Guide** is the 8-page booklet you get in Paper 2, in use from 2027. It lists syntax and names with no explanations, and it leaves out a lot you still have to write.
> Official copy: [SEAB Reference Guide for H2 Computing](https://isomer-user-content.by.gov.sg/334/fbf2f4ef-108a-4331-8597-a8c71427cc8d/9569_y27_sp_2_RefG.pdf).

## What It Prints

| Area | In the guide |
| ---- | ------------ |
| Python syntax | identifier rules, comments, `import`, data types, assignment with `+=` and `del`, operators, indexing and slicing, `in`, `if` / `elif` / `else`, `while`, `for`, `def` with `return`, `class` |
| Input and files | `input()` `print()` · `open()` … `close()` **and** `with open(...) as f:` · `read()` `readline()` `readlines()` `write()` |
| Built-ins | `abs()` `bin()` `chr()` `dict()` `float()` `hex()` `int()` `len()` `list()` `max()` `min()` `ord()` `range()` `round()` `str()` |
| String methods | `encode()` `endswith()` `format()` `index()` `isalnum()` `isalpha()` `isdigit()` `islower()` `isspace()` `isupper()` `lower()` `startswith()` `upper()` |
| List methods | `append()` `extend()` `clear()` `copy()` `index()` `insert()` `pop()` `remove()` `reverse()` `sort()` |
| Dictionary | `clear()` `copy()`, and `del x[y]` |
| `csv` | `reader()` `writer()` `writerow()` |
| `random` | `random()` `randint()` `randrange()` `shuffle()` |
| `math` | `ceil()` `exp()` `floor()` `log()` `pow()` `sqrt()` `trunc()` |
| `sqlite3` | `connect()` · connection: `execute()` `commit()` `close()` `rollback()` `row_factory` · cursor: `fetchone()` `fetchall()` · `Row` |
| Other modules | `datetime`, `os.path`, `sys.exit()`, `flask`, `numpy`, `sklearn` |
| SQL | `CREATE TABLE` with `PRIMARY KEY` and `FOREIGN KEY … REFERENCES`, `SELECT … WHERE … ORDER BY`, joins three ways, `COUNT` `MAX` `MIN` `SUM`, `INSERT`, `UPDATE`, `DELETE`, `DROP TABLE` |
| SQLite | types `NULL` `REAL` `INTEGER` `TEXT` · constraints `NOT NULL` `PRIMARY KEY` `AUTOINCREMENT` `UNIQUE` · operators |
| Web | HTML elements and attributes, Jinja2 `length` and `safe`, CSS properties |

## Not Printed, So Memorise

| Area | Not in the guide | Note |
| ---- | ---------------- | ---- |
| Strings | `strip()` `split()` `replace()` `find()` `count()`, and `join()` on a string | [[BTB2 File Handling]], [[LT1 basic python]] |
| Built-ins | `sum()` `sorted()` `tuple()` `next()` `enumerate()` | [[LT7 Lists]], [[LT6 Tuple]] |
| Dictionary | `.items()` `.keys()` `.values()` | [[LT8 Dictionary]] |
| Errors | `try` / `except` | [[LT4b Types of Errors and Test Cases]] |
| `random` | `seed()` `choice()` `choices()` `sample()` | [[BTB4 Random Generator]] |
| `sqlite3` | `.cursor()` and the `?` placeholders | [[C5a Python with SQLite]] |
| SQL | `DISTINCT` `BETWEEN` `LIKE` `IN` `LIMIT` `GROUP BY` `HAVING` `AVG()` | [[C4-2 Basic SQL]] |
| Algorithms | every sort, search, tree, hash table and recursion | |

The guide is a memory aid, not a list of what you may use.

The `Specimen Insert.pdf` in your C4 folder is the old 2020 edition. The 2027 one drops `socket` and `pymongo` and adds `numpy` and `sklearn`. The SQL and `sqlite3` parts are the same.

## Related

- [[C4-2 Basic SQL]]
- [[C5a Python with SQLite]]
- [[BTB2 File Handling]]
