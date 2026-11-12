# Python with SQLite — Creating Tables and Inserting Data

**Lesson:** 11 November 2026  
**Source:** [Recovered lesson transcript](Transcript.md)

The lesson moves from writing SQL directly to executing it through Python’s `sqlite3` module. Parts 1 and 2 cover creating a database, creating related tables, and inserting records. Updating and deleting records are topics for later lessons.

These notes are regenerated from the transcript. The SQL examples below use simplified field names; use the exact names, fields, and constraints from the worksheet. Technical clarifications are included where the recording is unclear or leaves a question unanswered.

## 1. Read the ER diagram before writing code

The exercise uses three tables: **products**, **customer**, and **orders**.

- A customer can have many order records; each order record refers to a customer.
- A product can appear in many order records; each order record in this exercise refers to a product.
- The `orders` table contains foreign keys that refer to primary keys in the other two tables.

A **schema** describes the structure of a table: its fields, data types, keys, and constraints. A table can have a schema while containing no records.

### Creation and insertion order

Create the referenced tables first, then the table that depends on them:

1. Create `products` and `customer`.
2. Create `orders`.
3. Insert the product and customer records.
4. Insert the order records that refer to them.

The order between `products` and `customer` is flexible here. **Do `orders` last**, because it depends on both. Creating the table structure and inserting its records are separate tasks.

**SQLite clarification:** foreign-key checks must be enabled for each connection with `PRAGMA foreign_keys = ON`, outside an active transaction. With ordinary immediate foreign-key checks, an order’s referenced product and customer must exist when the order is inserted. See [SQLite’s foreign-key documentation](https://www.sqlite.org/foreignkeys.html).

## 2. Query related tables using linking conditions

The teacher uses equality conditions in `WHERE`, combined with `AND`, to link tables. For example, assuming the indicated key names:

```sql
SELECT *
FROM customer AS c, products AS p, orders AS o
WHERE c.id = o.customer_id
  AND p.id = o.product_id;
```

- `c.id = o.customer_id` links an order to its customer.
- `p.id = o.product_id` links an order to its product.
- Both conditions are needed for this three-table relationship. Missing a linking condition can produce unrelated combinations of records.

This performs an inner join using comma-separated tables and `WHERE` conditions. **`JOIN` is valid SQL**; the teacher is choosing to teach the linking-condition approach for this course. `AND` combines conditions and is not a separate “N method.”

Use the approach taught in class consistently and understand which primary-key/foreign-key pair each condition connects.

## 3. Connect → execute → commit → close

| Step | Purpose |
| --- | --- |
| `import sqlite3` | Make Python’s SQLite module available. |
| `sqlite3.connect("database.db")` | Open a connection to the database file. Create the file if it does not exist. |
| `db.cursor()` | Create a cursor used to execute SQL and work with query results. |
| `c.execute(sql)` | Execute an SQL statement. |
| `db.commit()` | Commit pending changes in the transaction. |
| `db.close()` | Close the connection when finished. |

A simplified first-run table-creation example:

```python
import sqlite3

db = sqlite3.connect("database.db")
try:
    c = db.cursor()
    c.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL
        )
    """)
    db.commit()
finally:
    db.close()
```

Triple quotes create a Python string that can span several lines. The SQL inside that string is executed by SQLite. Multiline SQL is valid; pay attention to matching quotation marks, brackets, and commas.

**Connecting to an existing database does not erase it.** It reconnects to the existing file and its contents. Closing a connection is also not a substitute for committing pending inserts. See the [Python `sqlite3` reference](https://docs.python.org/3/library/sqlite3.html).

### Understand what happens when a cell runs again

- Rerunning `connect()` reconnects to the same file.
- Rerunning the example’s `CREATE TABLE products` raises an error if `products` already exists.
- `CREATE TABLE IF NOT EXISTS` avoids that existing-table error, but does **not** change an existing table’s schema.
- Rerunning an `INSERT` can insert another record or fail because of a constraint.
- The video’s separate file-reset step clears existing database contents. Use it only when intentionally rebuilding the database, not whenever adding data.

If a table was created with an incorrect field definition, editing the Python text alone does not modify the table already stored in the database. Decide how to correct or rebuild it before continuing. See [SQLite’s `CREATE TABLE` documentation](https://www.sqlite.org/lang_createtable.html).

## 4. Insert data using parameterized queries

With an open connection `db` and cursor `c`, assuming the simplified table above already exists:

```python
sql = "INSERT INTO products (name, price) VALUES (?, ?)"
values = ("Keyboard", 29.90)

c.execute(sql, values)
db.commit()
```

The two `?` placeholders correspond to the two values, in order. When an ID is generated automatically, omit that ID from the inserted column list; the number of supplied values can therefore be smaller than the total number of fields in the table.

For a single bound value, a one-item tuple needs a trailing comma:

```python
c.execute("SELECT * FROM products WHERE id = ?", (product_id,))
```

### Why parameterize?

**SQL injection** occurs when input is incorporated into an SQL statement in a way that lets it change the command’s meaning. Parameter binding keeps supplied values separate from the SQL command, so those values are treated as data.

- Pass values as the second argument to `execute()`.
- Do not build SQL containing user-supplied values using string concatenation or f-strings.
- Match the number and order of values to the placeholders and listed columns.
- Placeholders bind values; they do not substitute table or column names.

A fixed SQL statement with literal values can work, but the class’s consistent approach for supplying values is the `?` parameter style. Python also supports named parameters; the teacher is focusing on question-mark placeholders. See [Python’s placeholder guidance](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries).

## 5. Debug the SQL and the Python separately

| Problem | What to check |
| --- | --- |
| `table ... already exists` | Was the table-creation cell run before? Reconnecting does not reset the database. |
| `no such table` or `no such column` | Check spelling, the stored schema, and which database file Python opened. |
| Incorrect number of bindings | Count the `?` placeholders and supplied values. Check for a missing comma in a one-item tuple. |
| Syntax error | Check quotation marks, commas, parentheses, and the SQL statement itself. |
| Foreign-key error | Check that the referenced customer/product records exist and that the IDs are correct. |
| Database locked | Check for another connection or DB Browser transaction holding a lock. Finish the transaction and close resources when done. |
| Data appears missing | Check the database path, whether changes were committed, and whether a reset step was rerun. |

The teacher’s suggested process:

1. Inspect the SQL statement and its punctuation.
2. Simplify its formatting temporarily if line breaks make the problem hard to see.
3. Test a fixed example of the SQL in DB Browser to see whether the SQL itself works.
4. If it works there, inspect Python’s connection, parameters, and execution code.
5. Inspect the resulting tables and records, then close DB Browser when finished with it.

The suggestion to put a troublesome statement on one line is a debugging technique. It is not a general rule against multiline Python, SQL, or properly written comments.

## 6. Automatic IDs and deletion

The teacher points out that an automatically generated ID need not be supplied in an ordinary insert. The class also raises this question: **if ID 5 is deleted, will the next record receive 5 or 6?** The detailed answer was deferred to a concept-clarification lesson.

**Verified SQLite clarification:** the exact table definition matters.

| Definition | What happens after deleting the highest ID, 5, from IDs 1–5? |
| --- | --- |
| `INTEGER PRIMARY KEY` | The next automatically generated ID can be 5 again. |
| `INTEGER PRIMARY KEY AUTOINCREMENT` | After those inserts were committed, the next automatically generated ID is 6; deleted committed IDs are not automatically reused. |

`AUTOINCREMENT` does not guarantee an unbroken sequence with no gaps. Do not use an ID as a count of the current records. See [SQLite’s explanation of automatic IDs](https://www.sqlite.org/autoinc.html).

## 7. File handling and naming reminders

- With `with open(...) as f:`, Python closes the file when the block ends. An additional `f.close()` is unnecessary.
- With a plain `f = open(...)`, arrange to close the file when finished.
- Keep indentation correct when combining a `with` block and loops.
- A SQLite connection’s `with` block handles transactions; it does **not** automatically close the connection. Keep file handling and database connection handling distinct.
- Use `orders` for the exercise’s table name. `ORDER` is an SQL keyword, as in `ORDER BY`; avoid using it as an unquoted table name.

References: [Python file handling](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files), [SQLite connection context managers](https://docs.python.org/3/library/sqlite3.html#how-to-use-the-connection-context-manager).

## 8. Class workflow and revision advice

**Practical work**

- Watch video parts 1 and 2, pause, and type the code yourself.
- The teacher directs this cohort to use Jupyter Notebook. Organize work with Markdown headings and separate code cells for the numbered tasks; the older video refers to separate `.py` files.
- Complete the customer and orders tables and their data, not just the products example shown in the video.
- Finish the creation and insertion tasks, and be ready to show the database and its records next lesson. Without tables and data, later queries cannot be completed.

**Resources and notes**

- Coding exercises and associated videos remain in Cosmology; theory and concept-clarification activities use SLS.
- OneNote is planned as the central location for announcements, PDFs, and summary material.
- Keep downloaded resources in the subject folders. Record links or document/page references so revision does not require searching every platform again.
- Consolidate what you learned after each lesson in your own words. Start with explanations that help you understand, then condense them into revision sheets nearer the exam.

**Answering theory questions**

Knowing the topic is not enough: an answer must state the relevant point clearly and completely. Use the sample answers to identify what is missing and how to improve the wording. If a question asks for two advantages, choose two distinct advantages that apply to the stated context and explain them to the required depth.

## Quick self-check

- Can I explain why `orders` comes after `products` and `customer`?
- Can I write both linking conditions for the three-table query?
- Can I distinguish opening a database, creating a table, and resetting a file?
- Can I explain what `execute()`, `commit()`, and `close()` each do?
- Can I insert values with `?` placeholders and explain how this prevents SQL injection through those values?
- Can I diagnose an existing-table error without accidentally erasing my data?
- Can I check that the actual database contains all three tables and their records?
