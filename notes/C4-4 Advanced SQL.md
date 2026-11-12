> [!summary] Quick View
> "Advanced" means **more than one table**. List every table in `FROM`, then tie them together in `WHERE` with one **linking condition** per relationship: `Customers.Id = Orders.CustomerID`.
> Create the tables a foreign key points to **first**, and the linked entity `Orders` **last**.
> Syllabus 3.3.8. Single-table SQL is in [[C4-2 Basic SQL]].

> [!important] What the Paper 2 Reference Guide prints
> Three ways to read from two tables:
>
> ```text
> SELECT … FROM table1, table2 WHERE …;                   <- the one this course uses
> SELECT … FROM table1 INNER JOIN table2 ON …;
> SELECT … FROM table1 LEFT OUTER JOIN table2 ON …;
> ```
>
> Your course teaches only the first, with `AND` between the conditions. See [[#JOIN]].

## C4-4a Create Multiple Tables

```text
┌───────────┐        ┌────────┐        ┌──────────┐
│ Customers │───────<│ Orders │>───────│ Products │
└───────────┘        └────────┘        └──────────┘
                     linked entity
```

```text
Customers (Id, FirstName, LastName, City, Country, Phone)
           ──
Products (Id, ProductName, UnitPrice, Package, SupplierName, SupplierCountry)
          ──
Orders (Id, OrderDate, CustomerID*, ProductID*, Quantity)
        ──
```

A customer buys many products and a product is bought by many customers. `Orders` is the **linked entity** between them ([[C4-3c ER Diagram]]), so it holds both foreign keys.

```sql
CREATE TABLE Orders (
    Id          INTEGER NOT NULL,
    OrderDate   TEXT NOT NULL,
    CustomerID  INTEGER NOT NULL,
    ProductID   INTEGER NOT NULL,
    Quantity    INTEGER NOT NULL,
    FOREIGN KEY(ProductID) REFERENCES Products(Id),
    FOREIGN KEY(CustomerID) REFERENCES Customers(Id),
    PRIMARY KEY(Id)
);
```

`FOREIGN KEY(field in this table) REFERENCES OtherTable(its primary key)`, one clause per foreign key. The `Customers` and `Products` statements are in [[C4-2 Basic SQL#C4-2a Create a Table|C4-2a]].

> [!important] Order of creation
> `Customers` and `Products` first, in either order. **`Orders` last**, because its foreign keys refer to the other two. Coursemology Q1 says it too: *"Orders (create this table last)"*.

Save all three statements in a text file, `Create Tables.sql`. Paste it into the *Execute SQL* tab and run it to build every table at once.

> [!example]- What SQLite really does if `Orders` is created first (checked)
> The lecture says the creation fails. SQLite actually lets the `CREATE` through and complains later, when you insert with foreign keys switched on: *no such table: main.Customers*. Other database systems reject the `CREATE` itself. The rule is the same either way.

## C4-4b Query Multiple Tables

Uses `Northwind.db`: 91 customers, 78 products, 830 orders. Download it again if you have changed it.

### The Problem

*Find the customers, FirstName and LastName, who bought "Lakkalik ri" in Feb 2013.* `Orders` only holds IDs, so one table at a time takes three queries, carrying numbers across by hand:

```sql
SELECT Id FROM Products WHERE ProductName = 'Lakkalik ri';          -- 76

SELECT CustomerID, ProductID, OrderDate FROM Orders
WHERE OrderDate LIKE '%Feb%2013%' AND ProductID = 76;               -- 24 and 87

SELECT FirstName, LastName FROM Customers WHERE Id = 24 OR Id = 87; -- Maria, Pirkko
```

### Two Tables, Then Three

```sql
SELECT Customers.Id, FirstName, LastName
FROM Orders, Customers
WHERE OrderDate LIKE '%Feb%2013%'
AND ProductID = 76
AND Customers.Id = Orders.CustomerID;        -- the link
```

```sql
SELECT Customers.Id, FirstName, LastName
FROM Orders, Customers, Products
WHERE OrderDate LIKE '%Feb%2013%'
AND ProductName = 'Lakkalik ri'
AND Customers.Id = Orders.CustomerID         -- link 1
AND Orders.ProductID = Products.Id;          -- link 2
```

| Id | FirstName | LastName |
| -- | --------- | -------- |
| 24 | Maria | Larsson |
| 87 | Pirkko | Koskitalo |

```text
 Customers ──────────────── Orders ──────────────── Products
     Customers.Id = Orders.CustomerID
                               Orders.ProductID = Products.Id
```

Each link is **primary key = foreign key**.

### What the Link Does

`FROM Customers, Orders` with no link pairs **every** customer with **every** order. The linking condition keeps only the pairs that belong together.

| Query on `Northwind.db` | Rows |
| ----------------------- | ---- |
| `FROM Customers, Orders`, no link | 91 × 830 = 75 530 |
| add `Customers.Id = Orders.CustomerID` | 830, one per order |
| the three-table query above with link 1 left out | 182 instead of 2 |

**Tables − 1 links:** two tables need one, three tables need two.

### Which Table's Field

- `Id` is in all three tables, so write `Customers.Id` or `Products.Id`. A bare `Id` gives *ambiguous column name: Id*.
- A field that is in only one table needs no table name: `FirstName`, `Quantity`, `UnitPrice`, `ProductID`, `CustomerID`. Writing it anyway is not wrong.

### Dates Are Text

`OrderDate` holds text such as `Jul 30 2012 12:00:00:000AM`, and single-digit days have two spaces: `Feb  3 2013 …`. Match with `LIKE`: `'%Feb%2013%'` for a month, `'Jul 30 2012%'` for a day. `=` would need the whole string.

### Calculating Across Tables

*How much did Manuel Pereira spend on Jul 30 2012?* The name is in `Customers`, the quantity in `Orders`, the price in `Products`.

```sql
SELECT Quantity * UnitPrice
FROM Customers, Products, Orders
WHERE FirstName = 'Manuel' AND LastName = 'Pereira'
AND OrderDate LIKE 'Jul 30 2012%'
AND Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id;          -- 380
```

He is customer 33 and ordered 20 of product 2, Chang, at 19: 20 × 19 = 380. Wrap it in `SUM( )` when several rows could match, to get one total.

Once linked, the rows behave like one wide table, so everything from [[C4-2 Basic SQL#C4-2c Query|C4-2c]] still works:

| Want | Use |
| ---- | --- |
| each customer or product once | `SELECT DISTINCT …` |
| how many different customers | `COUNT(DISTINCT Customers.Id)` |
| one total over the matching rows | `SUM(UnitPrice * Quantity)` |
| a total for each product | `GROUP BY ProductName` with `SUM(Quantity)` |

## JOIN

From class, 11 Nov 2026: join is **not taught**, because there are many kinds of it (left, right and more). The two `AND` conditions do the same job, and the course uses them consistently. The Reference Guide still prints joins, so recognise them:

```sql
SELECT Customers.Id, FirstName, LastName
FROM Orders
INNER JOIN Customers ON Customers.Id = Orders.CustomerID
INNER JOIN Products ON Orders.ProductID = Products.Id
WHERE OrderDate LIKE '%Feb%2013%' AND ProductName = 'Lakkalik ri';
```

Same two rows. The link moves from `WHERE` to `ON`.

> [!example]- Extension: `LEFT OUTER JOIN` keeps rows that have no match
> ```sql
> SELECT Customers.Id, FirstName, LastName
> FROM Customers LEFT OUTER JOIN Orders ON Customers.Id = Orders.CustomerID
> WHERE Orders.Id IS NULL;
> ```
>
> Returns the two customers who never ordered: 22 Diego Roel and 57 Marie Bertrand. The linking-condition method cannot show them, because they have no order to pair with.

## Exam

> [!important] Writing any multi-table query
> 1. Which tables hold the fields you **show** and the fields you **filter** on? Put them all in `FROM`. Include `Orders` even if you show nothing from it: it is the only path between `Customers` and `Products`.
> 2. Write the **links**, one per relationship.
> 3. Add the **filters** with `AND`.
> 4. Decide the output: plain fields, `DISTINCT`, `COUNT`, `SUM`, `GROUP BY`.
>
> From class: in J2 the web app work uses two or three linked tables, not a single table.

> [!example]- Coursemology C4-4 Q2–Q7: `Northwind.db` (each returns the expected output)
> ```sql
> -- Q2 bought Lakkalik ri in Feb 2013: (24, Maria, Larsson), (87, Pirkko, Koskitalo)
> SELECT DISTINCT Customers.Id, FirstName, LastName
> FROM Customers, Orders, Products
> WHERE Customers.Id = Orders.CustomerID AND Orders.ProductID = Products.Id
> AND ProductName = 'Lakkalik ri' AND OrderDate LIKE '%Feb%2013%';
>
> -- Q3 Manuel Pereira's spending on Jul 30 2012: 380
> SELECT SUM(UnitPrice * Quantity)
> FROM Customers, Orders, Products
> WHERE Customers.Id = Orders.CustomerID AND Orders.ProductID = Products.Id
> AND FirstName = 'Manuel' AND LastName = 'Pereira' AND OrderDate LIKE 'Jul 30 2012%';
>
> -- Q4 number of different customers buying products from UK: 50
> SELECT COUNT(DISTINCT Customers.Id)
> FROM Customers, Orders, Products
> WHERE Customers.Id = Orders.CustomerID AND Orders.ProductID = Products.Id
> AND SupplierCountry = 'UK';
>
> -- Q5 products purchased by Ann Devon: 8 products
> SELECT DISTINCT ProductName
> FROM Customers, Orders, Products
> WHERE Customers.Id = Orders.CustomerID AND Orders.ProductID = Products.Id
> AND FirstName = 'Ann' AND LastName = 'Devon';
>
> -- Q6 total revenue from Ipoh Coffee: 12604 (two tables, one link)
> SELECT SUM(UnitPrice * Quantity)
> FROM Products, Orders
> WHERE Products.Id = Orders.ProductID AND ProductName = 'Ipoh Coffee';
>
> -- Q7 top 5 products by quantity sold to American customers: Geitost 189 first
> SELECT ProductName, SUM(Quantity)
> FROM Customers, Orders, Products
> WHERE Customers.Id = Orders.CustomerID AND Orders.ProductID = Products.Id
> AND Country = 'USA'
> GROUP BY ProductName
> ORDER BY SUM(Quantity) DESC LIMIT 5;
> ```
>
> Q4 without `DISTINCT` gives 83: it counts order rows, not customers. Q4 filters `SupplierCountry` (the product's), Q7 filters `Country` (the customer's).

## Common Mistakes

- Leaving out a link: thousands of rows, or a total many times too big.
- A bare `Id` when more than one table has it.
- `COUNT(Customers.Id)` to count customers. It counts order rows. Use `COUNT(DISTINCT …)`.
- Filtering the wrong country: `Country` is the customer's, `SupplierCountry` is the product's.
- `OrderDate = 'Jul 30 2012'`. The field also holds the time, so nothing matches.
- Leaving `Orders` out of `FROM` because nothing from it is displayed.
- Creating `Orders` before the two tables it refers to.

## Related

- [[C4-2 Basic SQL]]
- [[C4-3c ER Diagram]]
- [[C4-3b Normalisation]]
- [[C4-1 Introduction to Database]]
