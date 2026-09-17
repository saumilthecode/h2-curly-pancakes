> [!summary] Quick View
> SQL does **CRUD**: create (`CREATE TABLE`, `INSERT`), read (`SELECT`), update (`UPDATE`), delete (`DELETE`, `DROP TABLE`).
> `UPDATE` and `DELETE` without `WHERE` hit **every row**.
> Tables, records and keys are in [[C4-1 Introduction to Database]].

> [!important] What the Paper 2 Reference Guide prints
> **Given:** `CREATE TABLE` with `PRIMARY KEY (…)` and `FOREIGN KEY … REFERENCES`, `SELECT … WHERE … ORDER BY`, `COUNT` `MAX` `MIN` `SUM`, `INSERT`, `UPDATE`, `DELETE`, `DROP TABLE`, and joins (C4-4, not taught yet).
> Types `NULL` `REAL` `INTEGER` `TEXT` · constraints `NOT NULL` `PRIMARY KEY` `AUTOINCREMENT` `UNIQUE` · operators `=` `!=` `<` `<=` `>` `>=` `AND` `OR` `NOT` `IS` `IS NOT` `||`.
>
> **Not printed, so memorise:** `DISTINCT`, `BETWEEN`, `LIKE` with `%` and `_`, `IN`, `LIMIT`, `GROUP BY`, `HAVING`, `AVG()`.

| Term | Meaning |
| ---- | ------- |
| SQL | Structured Query Language — MySQL, Oracle, PostgreSQL are versions of it |
| SQL Server | client–server DBMS: a database server, plus client apps that connect to it |
| SQLite | **serverless** DBMS, embedded directly in an application |

The lab tool is **DB Browser for SQLite**; statements go in the *Execute SQL* tab.

## C4-2a Create a Table

```sql
CREATE TABLE Customers (
    Id          INTEGER NOT NULL,
    FirstName   TEXT NOT NULL,
    LastName    TEXT NOT NULL,
    City        TEXT,
    Country     TEXT NOT NULL,
    Phone       TEXT NOT NULL,
    PRIMARY KEY(Id)
);
```

`NOT NULL` makes a field compulsory; `City` can be empty. `;` ends each statement.

Foreign keys each get their own clause:

```sql
CREATE TABLE Orders (
    Id          INTEGER NOT NULL,
    OrderDate   TEXT NOT NULL,
    CustomerID  INTEGER NOT NULL,
    ProductID   INTEGER NOT NULL,
    Quantity    INTEGER NOT NULL,
    PRIMARY KEY(Id),
    FOREIGN KEY(CustomerID) REFERENCES Customers(Id),
    FOREIGN KEY(ProductID) REFERENCES Products(Id)
);
```

A composite key is **one** clause listing every field: `PRIMARY KEY(CustomerID, Colour, Date)`. Two `PRIMARY KEY` clauses raise *table has more than one primary key*.

### Data Types

| Type | Holds |
| ---- | ----- |
| `INTEGER` | whole numbers; Booleans as `0` / `1` |
| `REAL` | decimals |
| `TEXT` | strings; dates as `'YYYY-MM-DD'` |
| `BLOB` | binary data such as an image — avoid, it bloats the file |
| `NUMERIC` | anything else, e.g. Boolean or DateTime |

`CHAR(30)` is fixed length; `VARCHAR(30)` is variable, so `'John'` uses 4. SQLite stores both as `TEXT` and ignores the `(30)`.

## C4-2b Insert

```sql
INSERT INTO Products (ProductName, UnitPrice, Package, SupplierName, SupplierCountry)
VALUES ('Chai', 18, '10 boxes x 20 bags', 'Exotic Liquids', 'UK');

INSERT INTO Products (ProductName, UnitPrice, Package, SupplierName, SupplierCountry)
VALUES ('Chang', 19, '24 - 12 oz bottles', 'Exotic Liquids', 'UK'),
       ("Chef Anton's Gumbo Mix", 21.35, '36 boxes', 'New Orleans Cajun Delights', 'USA');
```

- Values match the column list **in order**.
- `Id` is left out — the integer primary key **auto-increments**.
- Omitted field → `NULL`; if `NOT NULL`, the insert fails.
- Several rows share one `VALUES`, separated by commas.
- Text containing `'` goes in **double quotes**.
- Strings are quoted, numbers are not. Line breaks don't matter.

## C4-2c Query

```text
SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT …;
```

Clauses must come in this order — `ORDER BY` before `WHERE` is a syntax error.

```sql
SELECT * FROM Products;                              -- every field
SELECT Id, ProductName, UnitPrice FROM Products;     -- chosen fields
SELECT DISTINCT SupplierName FROM Products;          -- each value once
```

### `WHERE`

| Operator | Means |
| -------- | ----- |
| `=` | equal |
| `<>` or `!=` | not equal |
| `>` `<` `>=` `<=` | comparisons |
| `BETWEEN 10 AND 20` | range, **both ends included** |
| `LIKE '%ja%'` | pattern — `%` is any number of characters, `_` exactly one |
| `IN ('Germany', 'France', 'UK')` | any of the listed values |

```sql
SELECT * FROM Customers WHERE Country = 'Mexico';
SELECT * FROM Customers WHERE Country IN ('Germany', 'France', 'UK');
SELECT * FROM Customers WHERE Country = 'USA' AND (City = 'Seattle' OR City = 'Portland');
```

`AND` is applied before `OR`, as in [[LT1 basic python|Python]], so bracket the `OR`. `'%ja%'` matches *Janine* and *Alejandra*; `'U_'` matches `UK` but not `USA`.

### Sorting and Limiting

```sql
SELECT ProductName, UnitPrice FROM Products ORDER BY UnitPrice DESC LIMIT 10;   -- top 10
SELECT FirstName, Country FROM Customers ORDER BY Country ASC, FirstName DESC;
```

`ORDER BY` is ascending by default. A second field only breaks ties in the first.

### Aggregates and Groups

```sql
SELECT COUNT(Id) FROM Products;
SELECT AVG(UnitPrice) FROM Products;       -- also SUM, MAX, MIN

SELECT COUNT(ProductName), SupplierCountry FROM Products
GROUP BY SupplierCountry
ORDER BY COUNT(ProductName) DESC;
```

`GROUP BY` returns **one row per group**. Without an aggregate beside it, the result shows one arbitrary product per country.

```sql
SELECT COUNT(Id), Country FROM Customers
GROUP BY Country
HAVING COUNT(Id) > 5
ORDER BY COUNT(Id) DESC;
```

| `COUNT(Id)` | `Country` |
| ----------- | --------- |
| 13 | USA |
| 11 | France |
| 11 | Germany |
| 9 | Brazil |
| 7 | UK |

> [!warning] `WHERE` cannot use an aggregate
> `WHERE` filters **rows** before grouping; `HAVING` filters **groups** after. `WHERE COUNT(Id) > 5` fails with *misuse of aggregate*.

## C4-2d Update

```sql
UPDATE Customers SET Country = 'Singapore'
WHERE FirstName = 'Thomas' AND LastName = 'Hardy';     -- 1 row

UPDATE Orders SET Quantity = Quantity + 5 WHERE Id = 7;  -- 35 becomes 40

UPDATE Customers SET Country = 'Singapore';             -- all 91 rows
```

## C4-2e Delete and Drop

```sql
DELETE FROM Customers WHERE FirstName = 'Victoria';    -- 1 record
DELETE FROM Customers;                                 -- every record, table stays
DROP TABLE Customers;                                  -- the table itself is gone
```

| Statement | Records | Table |
| --------- | ------- | ----- |
| `DELETE FROM … WHERE` | the matching ones go | stays |
| `DELETE FROM …` | all go | stays, empty |
| `DROP TABLE …` | all go | **gone** |

`Northwind.db`: `Orders` references Victoria's `Id`, so the **foreign key** blocks deleting her or dropping `Customers`. `dummy.db` removes this constraint. SQLite has no `DROP DATABASE`.

> [!warning] Foreign keys are off by default outside DB Browser
> DB Browser enforces foreign keys; the `sqlite3` CLI and Python module require `PRAGMA foreign_keys = ON`.

> [!important] Before any `UPDATE` or `DELETE`
> Preview affected rows with `SELECT` using the **same `WHERE`**.

## Exam

> [!important] 2025 Promo P2 Task 9 — `bakery.db`, table `products (Name, Description, UnitPrice, Quantity)` `[8]`
> ```sql
> SELECT Name, Description FROM products;                      -- 9.1
>
> SELECT Name, UnitPrice FROM products WHERE UnitPrice >= 5.00; -- 9.2
>
> SELECT SUM(UnitPrice * Quantity) FROM products;              -- 9.3
>
> INSERT INTO products (Name, Description, UnitPrice, Quantity) -- 9.4
> VALUES ('Sourdough Loaf',
>         'A rustic, tangy bread with a chewy inside and a thick, crunchy crust.',
>         7.00, 30);
> ```
>
> | Task | 1m | 1m |
> | ---- | -- | -- |
> | 9.1 | `SELECT … FROM …` | both fields |
> | 9.2 | `UnitPrice >= 5.00` | `SELECT … FROM … WHERE …` |
> | 9.3 | `UnitPrice * Quantity` | `SUM()` |
> | 9.4 | `INSERT INTO … VALUES …` | 4 fields and 4 values |
>
> 9.3 is revenue **if everything sells** — multiply inside `SUM`, per row.

> [!important] 2024 Promo P2 Task 8 — table `books (Id, Title, Author, Publisher, Year, UnitPrice, Quantity)` `[10]`
> ```sql
> SELECT Title, Publisher FROM books;                        -- 8.1
> SELECT Title, Year FROM books WHERE Year > 2000;           -- 8.2
> SELECT DISTINCT Publisher FROM books ORDER BY Publisher;   -- 8.3
> SELECT SUM(UnitPrice * Quantity) FROM books;               -- 8.4
> INSERT INTO books (Title, Author, Publisher, Year, UnitPrice, Quantity)
> VALUES ('The Hidden Language of Computer Hardware and Software',
>         'Charles Petzold', 'Microsoft Press', 2000, 34.99, 2);   -- 8.5
> ```
>
> Same marks as 2025, plus **8.3**: 1m `ORDER BY`, 1m `DISTINCT` — each publisher once. `DISTINCT` isn't in the Reference Guide.

> [!example]- 2024 A-Level P1 Q4(a)(iii) — create the property table `[4]`
> Each property has a reference code, address, price in dollars and number of bedrooms.
>
> ```sql
> CREATE TABLE Property (
>     PropertyRef  TEXT NOT NULL,
>     Address      TEXT NOT NULL,
>     Price        INTEGER NOT NULL,
>     Bedrooms     INTEGER NOT NULL,
>     PRIMARY KEY(PropertyRef)
> );
> ```
>
> The reference *code* is `TEXT`. Field names match your own table description from (a)(ii).

> [!example]- SLS D1–D6 — `Northwind.db`
> ```sql
> -- D1 customers from the UK (7 rows)
> SELECT FirstName, LastName, Country FROM Customers WHERE Country = 'UK';
>
> -- D2 German customers by city (11 rows)
> SELECT FirstName, LastName, Country, City FROM Customers
> WHERE Country = 'Germany' ORDER BY City;
>
> -- D3 all suppliers by country (29 rows; without DISTINCT, 78)
> SELECT DISTINCT SupplierName, SupplierCountry FROM Products ORDER BY SupplierCountry;
>
> -- D4 five highest unit prices below $20
> SELECT ProductName, UnitPrice FROM Products
> WHERE UnitPrice < 20 ORDER BY UnitPrice DESC LIMIT 5;
>
> -- D5 three countries with the most products: USA 12, Germany 9, Australia 8
> SELECT SupplierCountry, COUNT(ProductName) FROM Products
> GROUP BY SupplierCountry ORDER BY COUNT(ProductName) DESC LIMIT 3;
>
> -- D6 products from $20 to $40 inclusive (26)
> SELECT COUNT(ProductName) FROM Products WHERE UnitPrice BETWEEN 20 AND 40;
> ```

> [!example]- SLS E1 — raise every price under $20 by $1 (`dummy.db`)
> ```sql
> SELECT Id, UnitPrice FROM Products WHERE UnitPrice < 20;       -- 40 rows
> UPDATE Products SET UnitPrice = UnitPrice + 1 WHERE UnitPrice < 20;
> ```
>
> To check, compare the **same `Id`s** before and after. Rerunning `WHERE UnitPrice < 20` returns 36 rows: the four products priced from `19` to `19.5` are no longer under `20`.

## Common Mistakes

- `UPDATE` or `DELETE` with no `WHERE`.
- `WHERE COUNT(…)` instead of `HAVING`.
- Mixing up `DELETE FROM` (records) with `DROP TABLE` (the table).
- Clauses out of order, e.g. `LIMIT` before `ORDER BY`.
- A single-quoted string that contains `'`.

## Related

- [[C4-1 Introduction to Database]]
- [[BTB2 File Handling]]
- [[LT1 basic python]]
