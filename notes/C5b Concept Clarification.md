> [!summary] Quick View
> Five things that confuse people in [[C5a Python with SQLite|C5a]]: a **primary key must never be empty**, `AUTOINCREMENT` **never reuses** a deleted `Id`, a **foreign key blocks** deleting a record something still points to, **quotes** depend on what's inside the string, and **`?`** lets the user supply the value.
> SQLite is more relaxed than other DBMSs. Learn the rule, not what SQLite lets you get away with.

## A. Can a Primary Key Be NULL?

**No.** A primary key exists to identify each record, so every record needs a value in it.

```sql
CREATE TABLE OnlyText (
    Name TEXT PRIMARY KEY,
    Class TEXT
);

INSERT INTO OnlyText (Name) VALUES ('Name5'), ('Name6');     -- Class is NULL: fine
INSERT INTO OnlyText (Class) VALUES ('Class5'), ('Class6');  -- Name is NULL: wrong
```

| Name | Class |
| ---- | ----- |
| Name5 | NULL |
| Name6 | NULL |
| NULL | Class5 |
| NULL | Class6 |

SQLite accepts the last insert, twice, because it doesn't strictly enforce `NOT NULL` on a text primary key. Other DBMSs reject it. Add `NOT NULL` and SQLite rejects it too: *NOT NULL constraint failed: OnlyText.Name*.

Leaving out a **non-key** field is fine when it has no `NOT NULL`: it's stored as `NULL`.

> [!important] Class, 13 Nov: say "record"
> A primary key is a field, or combination of fields, that **uniquely identifies each record**. Not "specific data", not "a row".
> A single field works when it's unique on its own, like an NRIC number. If one person makes many bank withdrawals, you need NRIC **and** date: a **composite** key.

## B. Auto-Increment

Leave out an `Id` and SQLite fills it in. Whether a deleted `Id` comes back depends on how the table was made.

```sql
CREATE TABLE NoAuto (
    Id INTEGER PRIMARY KEY,
    Name TEXT
);

CREATE TABLE WithAuto (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT
);
```

| Step | `NoAuto` | `WithAuto` |
| ---- | -------- | ---------- |
| insert without an `Id` | next number after the largest | next number after the largest ever used |
| insert `Id` 5 yourself after 1, 2 | allowed | allowed, and the next one is **6**, not 3 |
| delete the **last** record, then insert | its `Id` is **reused** | its `Id` is **never** reused |

The run from the slides:

```text
NoAuto     Ids 1–6     delete 6     insert Name7, Name8, Name9   ->  6, 7, 8
WithAuto   Ids 1, 2, 5–8 delete 8   insert Name9, Name10         ->  9, 10
```

> [!warning] Why reuse is bad
> Delete customer 6, then a new customer also gets 6. A message saying "update customer 6's phone number" could now mean either person. Once an `Id` is used it should stay retired, and `AUTOINCREMENT` makes sure of that.

Auto-increment only makes sense for an `INTEGER` key. A text key like an NRIC has no "next" value.

`NoAuto` filling in an `Id` at all is an SQLite convenience. Other DBMSs may not do it, so don't rely on it.

## C. Deletion Denied

Customer (<u>Id</u>, Name)
Purchase (Product, <u class="fk">Cid</u>)

```sql
CREATE TABLE Customer (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT
);

CREATE TABLE Purchase (
    Product TEXT,
    Cid INTEGER REFERENCES Customer(Id)
);

INSERT INTO Customer (Name) VALUES ('Adam'), ('Bob');
INSERT INTO Purchase (Product, Cid) VALUES ('Cake', 2);
```

```mermaid
erDiagram
  direction LR
  Customer ||--o{ Purchase : ""
```

| Statement | Result |
| --------- | ------ |
| `DELETE FROM Customer WHERE Id=1;` | allowed: no purchase points to Adam |
| `DELETE FROM Customer WHERE Id=2;` | *FOREIGN KEY constraint failed*: Bob's purchase points to him |
| `DROP TABLE Customer;` | *FOREIGN KEY constraint failed* |
| a purchase with `Cid` 9 | *FOREIGN KEY constraint failed*: there's no customer 9 |

**Referential integrity**: every record in the **child** table (`Purchase`) must match a real record in the **parent** table (`Customer`). The foreign key keeps it that way by refusing deletes and inserts that would break the link.

So:

- **Create and fill the parent first**, then the child. Delete the other way round.
- **Create the tables exactly as the table description says.** Leave out the `REFERENCES` and nothing protects the data.

> [!warning] On in DB Browser, off in Python
> DB Browser checks foreign keys. Python's `sqlite3` doesn't until you run `c.execute("PRAGMA foreign_keys = ON")` straight after `connect()`. Without it, all three statements above go through.

## D. Single or Double Quotes?

Use the quote that **isn't** inside the string.

| String contains | Enclose it in | Example |
| --------------- | ------------- | ------- |
| `'` | `"…"` | `"This is Mr Lim's bag."` |
| `"` | `'…'` | `'He says: "Hello World."'` |
| both | `'''…'''` or `"""…"""` | `'''Mr Lim's name is "John".'''` |

Same rule in SQL: `("Chef Anton's Gumbo Mix", 21.35, …)`.

Through `?` you don't have to think about it: the value goes in as data and its quotes don't matter.

## E. Why Parameterise?

This works, but the country is fixed in the code:

```python
c.execute('''UPDATE Customers SET Country='Singapore'
          WHERE FirstName="Thomas" AND LastName="Hardy";''')
```

With `?`, the value can come from the user:

```python
new_country = input("Enter a new country: ")

c.execute('''UPDATE Customers SET Country=?
          WHERE FirstName="Thomas" AND LastName="Hardy";''', (new_country,))
```

The shape is always `c.execute(sql_string, data_tuple)`. Each `?` takes the next value from the tuple. It also stops SQL injection ([[C5a Python with SQLite#Exam|C5a]]).

## Exam

> [!important] Explain why an `Id` should not be reused
> The same `Id` would then identify two different records over time, so anything that still refers to the old `Id` would wrongly point to the new record. `AUTOINCREMENT` prevents this by never reusing a value.

> [!important] Explain how a foreign key keeps data consistent
> A foreign key value must match the primary key of an existing record in the parent table. The DBMS refuses to delete a parent record that child records still refer to, and refuses a child record that refers to a parent that doesn't exist, so no record is left pointing at nothing.

> [!tip] Class, 13 Nov: field names
> One word. `myName` or `my_name` are fine, `my-name` and `my name` are not. Spaces in field names lose marks in the theory paper ([[C4-1 Introduction to Database#Table Description|C4-1]]).

## Common Mistakes

- A primary key with no value, because SQLite let it through.
- Expecting a deleted `Id` to come back, or not to, without checking whether the table uses `AUTOINCREMENT`.
- Deleting a parent record before the child records that point to it.
- Leaving out the `REFERENCES` clause, so nothing stops a broken link.
- `'Mr Lim's bag'`: the `'` inside ends the string early.
- Hard-coding a value that should come from `input()`.

## Related

- [[C5a Python with SQLite]]
- [[C4-1 Introduction to Database]]
- [[C4-2 Basic SQL]]
- [[C4-3a Introduction to Relational Database]]
