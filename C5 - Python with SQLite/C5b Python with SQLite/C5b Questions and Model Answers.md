# C5b Concept Clarification

[Existing slides](2024_C5b_Python_with_SQLite_-_Concepts_Clarification.pdf) · [Teacher summary guide](SQL_Concepts_Study_Guide.pdf) · [All seven video transcripts](C5b%20Video%20Transcripts.txt)

Source: [SLS C5b](https://vle.learning.moe.edu.sg/class-group/assignment/attempt/348e5ef9-5364-46e8-8762-3c67d5b97437). Questions retain their SLS numbers. Answers below are checked model answers, not personal submissions or AI feedback.

## A. Can a primary key be NULL?

Video: [C5b Python with SQL Part 1b - A - voiceover](https://www.youtube.com/watch?v=Kous3DUa-7s)

### Q1

```sql
CREATE TABLE OnlyText (Name TEXT PRIMARY KEY, Class TEXT);
INSERT INTO OnlyText (Class) VALUES ('C1');
```

What happens when SQLite runs the INSERT statement?

Options:

- A. `Error: the NOT NULL constraint fails on the Name field.`
- B. `Error: the PRIMARY KEY value is missing.`
- C. `The row is inserted, and Name is stored as ''.`
- D. `The row is inserted, and Name is stored as NULL.`

**Model answer:**

The row is inserted, and `Name` is stored as `NULL`.

### Q2

```sql
CREATE TABLE OnlyText (Name TEXT PRIMARY KEY, Class TEXT);
INSERT INTO OnlyText (Class) VALUES ('C1');
```

SQLite inserts this row. Explain why SQLite accepts it, and why a NULL primary key is a problem.

**Model answer:**

In this ordinary SQLite rowid table, `TEXT PRIMARY KEY` does not automatically enforce `NOT NULL` because SQLite retains this historical behaviour. Multiple rows can therefore have a NULL key, which cannot act as a unique, usable record identifier and violates entity integrity. An explicit `NOT NULL` constraint prevents this; `INTEGER PRIMARY KEY`, STRICT tables and WITHOUT ROWID tables have different NULL handling.


## B. Automatic IDs and AUTOINCREMENT

`INTEGER PRIMARY KEY` already generates IDs automatically. `AUTOINCREMENT` changes reuse behaviour; it is not required merely to generate an ID.

Video: [C5b Python with SQL Part 1b - B - voiceover](https://www.youtube.com/watch?v=dFe3Bo4JX2Y)

### Q3

```sql
CREATE TABLE NoAuto (Id INTEGER PRIMARY KEY, Name TEXT);
```

The table holds records with Id 1 to 6.

```sql
DELETE FROM NoAuto WHERE Id = 6;
INSERT INTO NoAuto (Name) VALUES ('New');
```

What Id does SQLite give the new record?

Options:

- A. `5`
- B. `6`
- C. `7`
- D. `NULL`

**Model answer:**

**6.** After Id 6 is deleted, the largest remaining Id is 5. Ordinary `INTEGER PRIMARY KEY` automatically allocates an unused Id, normally the current maximum plus one, so it reuses 6 here.

### Q4

```sql
CREATE TABLE WithAuto (Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT);
```

The table holds records with Id 1 to 6.

```sql
DELETE FROM WithAuto WHERE Id = 6;
INSERT INTO WithAuto (Name) VALUES ('New');
```

What Id does SQLite give the new record?

Options:

- A. `1`
- B. `6`
- C. `7`
- D. `NULL`

**Model answer:**

**7.** `AUTOINCREMENT` remembers the highest committed Id previously allocated in this table, so automatic allocation does not reuse the deleted Id 6.

### Q5

In the NoAuto table (Id INTEGER PRIMARY KEY), the record with Id 6 was deleted, and the next new record was given Id 6.

Explain why this is a problem, and how AUTOINCREMENT prevents it.

**Model answer:**

An old external or historical reference to Id 6 could now identify a different person. `AUTOINCREMENT` prevents this automatic reuse by choosing an Id greater than any previously committed Id in that table. The deleted record is not overwritten; it was already removed. This rule concerns automatically generated IDs, not someone explicitly supplying an old unused ID.


## C. Deletion and referential integrity

Foreign keys are enforced in these questions. In SQLite this requires enabling them for the connection, for example with `PRAGMA foreign_keys = ON;`. No cascading delete is specified.

Video: [C5b Python with SQL Part 1b - C - voiceover](https://www.youtube.com/watch?v=PPfdB3BQlUg)

### Q6

Customer (Id_, Name) holds (1, 'Adam') and (2, 'Bob').

Purchase (Product_, Cid*) holds ('Cake', 2). Cid references Customer(Id).

Foreign keys are enforced.

Which statement fails?

Options:

- A. `DELETE FROM Customer WHERE Id = 1;`
- B. `DELETE FROM Customer WHERE Id = 2;`
- C. `DELETE FROM Purchase WHERE Cid = 2;`
- D. `INSERT INTO Customer (Name) VALUES ('Cara');`

**Model answer:**

`DELETE FROM Customer WHERE Id = 2;` fails. Purchase `('Cake', 2)` still refers to Bob's Customer record. With foreign-key enforcement and the stated/default non-cascading behaviour, SQLite prevents deletion of that referenced parent.

### Q7

Customer (Id_, Name) holds (1, 'Adam') and (2, 'Bob').

Purchase (Product_, Cid*) holds ('Cake', 2). Cid references Customer(Id).

```sql
DELETE FROM Customer WHERE Id = 2;
```

This statement fails with 'FOREIGN KEY constraint failed'.

Explain why the DBMS does not allow this deletion.

**Model answer:**

The Purchase record `('Cake', 2)` has foreign key `Cid = 2`, referring to Bob's `Customer.Id = 2`. Deleting Bob would leave that purchase pointing to a customer that does not exist, so the DBMS rejects the deletion to preserve referential integrity.


## D. Single, double and triple quotes

Video: [C5b Python with SQL Part 1b - D - voiceover](https://www.youtube.com/watch?v=HIV0QaSkKvA)

### Q8

Which Python string literal stores exactly this text?

Mr Lim's "Robot" kit

Options:

- A. `"Mr Lim's "Robot" kit"`
- B. `'''Mr Lim's "Robot" kit'''`
- C. `'Mr Lim"s "Robot" kit'`
- D. `'Mr Lim's "Robot" kit'`

**Model answer:**

Of the listed options:

```python
'''Mr Lim's "Robot" kit'''
```

Triple single quotes allow both the apostrophe and double quotation marks inside the string without ending it. Appropriately escaped ordinary string literals would also work, but the other listed options do not store the exact requested text. This question concerns Python string delimiters.


## E. Parameterised SQL

Video: [C5b Python with SQL Part 1b - E - voiceover](https://www.youtube.com/watch?v=ujll_gUA_Fc)

### Q9

```python
new_country = input('Enter a new country: ')
c.execute('UPDATE Customers SET Country = ? WHERE Id = 4', (new_country,))
```

Explain why the program uses ? and the tuple (new_country,) instead of writing Country = 'Singapore' inside the SQL string.

**Model answer:**

`new_country` is supplied by the user at run time, so hardcoding `'Singapore'` would ignore any other choice. The `?` is a placeholder, and `execute()` binds the value from the one-item tuple `(new_country,)` to that placeholder. The SQL structure stays separate from the data. Binding is not automatic validation of whether the country value is sensible.

### Q10

```python
new_country = 'Singapore'
```

Which statement updates the Country of the customer with Id 4 to the value in new_country?

Options:

- A. `c.execute('UPDATE Customers SET Country = ? WHERE Id = 4', (new_country))`
- B. `c.execute('UPDATE Customers SET Country = ? WHERE Id = 4', (new_country,))`
- C. `c.execute('UPDATE Customers SET Country = ? WHERE Id = 4', new_country)`
- D. `c.execute('UPDATE Customers SET Country = new_country WHERE Id = 4')`

**Model answer:**

```python
c.execute('UPDATE Customers SET Country = ? WHERE Id = 4', (new_country,))
```

The comma makes a one-item tuple. `(new_country)` alone is just the original string, not a tuple. Python's sqlite3 also accepts suitable parameter sequences such as lists; the tuple is the form used in this lesson.


## F. SQL injection and race conditions

Video: [Demo SQL Injection v2](https://www.youtube.com/watch?v=b78_jhA0Ta0)

Video: [Race Condition v2](https://www.youtube.com/watch?v=4FfZUuVWuiE)

### Q11

A login page runs this code:

```python
name = input('Username: ')
pw = input('Password: ')
sql = "SELECT * FROM details WHERE name = '" + name + "' AND (password = '" + pw + "')"
c.execute(sql)
```

A user types Alice as the username and 1' OR '1'='1 as the password. The page shows Alice's details.

Explain why this input works without Alice's password, and how using ? placeholders (as in the Parameterise SQL questions) prevents this attack.

**Model answer:**

Concatenation puts the entered text into the SQL command. Its password condition becomes:

```sql
password = '1' OR '1'='1'
```

Since `'1'='1'` is true, that parenthesised password condition is true without the password. The separate `name = 'Alice'` condition still limits the result to Alice; it does not select every username.

Bind both inputs as values instead:

```python
sql = 'SELECT * FROM details WHERE name = ? AND password = ?'
c.execute(sql, (name, pw))
```

The entire attack text is then compared as password data, not parsed as SQL operators, so it cannot turn the password check into an always-true condition.

### Race condition: key point

A race condition occurs when the result depends on how concurrent operations interleave. In the video, both ATMs read the same $100 balance before either withdrawal completes, so both approve $100 and the second subtraction leaves -$100. Protect the balance check and update together using a transaction with appropriate isolation/locking, or a suitable atomic conditional update; calling `commit()` after separate unsafe steps is not enough.


## G. Real-life security reflection

[CSA SingCERT advisory: SQL Injection Attacks Affecting Singapore Websites](https://www.csa.gov.sg/alerts-advisories/Advisories/2023/ad-2023-021), 25 October 2023. It describes unauthorised access, defacement and data compromise, and recommends input validation, least privilege, patched software and other defences.

**Prompt:** The advisory lists "validate user input" as one defence. Which parts of a Python program that uses SQLite read input from a user? Write 2 to 3 sentences on how a program could handle that input safely.

**Model answer (3 sentences):** The username, password and country read through `input()` or a web form are untrusted input. Check each value has the expected type, length and permitted content, then supply it to `execute()` through `?` placeholders and a parameter tuple rather than string concatenation. Validation checks whether data is acceptable; parameter binding stops that data being interpreted as SQL code.

## Precision when using the clips

- Some captions use old C5a/C5b labels; follow the current SLS section names above.
- The SQL-injection clip demonstrates multiple commands in DB Browser. Python `sqlite3.execute()` accepts one SQL statement, but single-statement SQL injection can still bypass an unsafe password condition.
- The question answers above state the precise SQLite rules; automatic captions may mishear SQL terms.

References: [SQLite primary-key quirks](https://www.sqlite.org/quirks.html#primary_keys_can_sometimes_contain_nulls), [automatic IDs](https://sqlite.org/autoinc.html), [foreign keys](https://sqlite.org/foreignkeys.html), [bound parameters](https://www.sqlite.org/lang_expr.html#parameters).
