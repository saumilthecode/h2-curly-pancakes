# C4-4 Advanced SQL: Answers and Checks

Checked locally on 11 November 2026 using the current Coursemology slides and fresh source database downloads.

Source: https://yijc.coursemology.org/courses/3257/assessments/88878/submissions/2918269/edit

## Browser status

- Question 1: Database.db is attached but not submitted.
- Questions 2–7: answers entered and rechecked by returning to each question.
- No Check Answer, Save Draft, or Submit button was clicked. Site automatic saving was allowed by the user.
- Every question still showed Past Answers (0); none was sent for marking.

## Files

- The current C4-4 slides are in [Slides](../Slides/C4-4_Advanced_SQL.pdf). The existing file was byte-for-byte identical to the current Coursemology download.
- Database.db is the empty three-table database for Question 1. It is separate from the C4-2 walkthrough database.
- Create Tables.sql recreates its schema, with Customers and Products created before Orders.
- Question N.sql contains each query.
- Question N - Coursemology.py contains each query in the required query1 string.
- Question N - Results.csv contains the locally checked output.
- Source databases holds untouched Northwind.db and dummy.db downloaded from this C4-4 task. Pre-existing databases are retained in [Shared Resources/Databases](../../Shared%20Resources/Databases/).

## Question 1: Create database tables

- Customers, Products, Orders are present with the fields, types and NOT NULL requirements from the slides.
- Id is the primary key in each table.
- Orders.CustomerID references Customers.Id.
- Orders.ProductID references Products.Id.
- Every table contains 0 records.
- SQLite integrity check: ok. Foreign-key check: no violations.

## Expected-result checks

- Q2: (24, Maria, Larsson), (87, Pirkko, Koskitalo).
- Q3: 380.
- Q4: 50.
- Q5: 8 distinct products, matching the expected set.
- Q6: 12604.
- Q7: Geitost 189; C te de Blaye 149; Gorgonzola Telino 144; Chef Anton's Cajun Seasoning 134; R ssle Sauerkraut 124.
- Q7 supporting check: 122 USA-customer order records, covering 57 unique products, as stated in the question.

## Question 2: Customers who bought Lakkalik ri in February 2013

```sql
SELECT DISTINCT Customers.Id, FirstName, LastName
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND ProductName = 'Lakkalik ri'
AND OrderDate LIKE '%Feb%2013%';
```

Join both foreign keys and filter the product and month. DISTINCT lists each customer once. Include Customers.Id because the expected output includes it.

## Question 3: Manuel Pereira spending on 30 July 2012

```sql
SELECT SUM(UnitPrice * Quantity)
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND FirstName = 'Manuel'
AND LastName = 'Pereira'
AND OrderDate LIKE 'Jul 30 2012%';
```

Multiply each order quantity by its unit price, then SUM the amounts for that customer and date.

## Question 4: Different customers buying products from UK

```sql
SELECT COUNT(DISTINCT Customers.Id)
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND SupplierCountry = 'UK';
```

Filter SupplierCountry, not the customer country. COUNT(DISTINCT Customers.Id) counts each customer only once.

## Question 5: Products purchased by Ann Devon

```sql
SELECT DISTINCT ProductName
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND FirstName = 'Ann'
AND LastName = 'Devon';
```

Join the three tables, filter Ann Devon, and use DISTINCT to avoid repeated product names.

## Question 6: Total revenue from Ipoh Coffee

```sql
SELECT SUM(UnitPrice * Quantity)
FROM Products, Orders
WHERE Products.Id = Orders.ProductID
AND ProductName = 'Ipoh Coffee';
```

Join orders to products and SUM unit price multiplied by quantity for Ipoh Coffee.

## Question 7: Top five products by quantity sold to American customers

```sql
SELECT ProductName, SUM(Quantity)
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND Country = 'USA'
GROUP BY Products.Id, ProductName
ORDER BY SUM(Quantity) DESC
LIMIT 5;
```

Filter the customer Country to USA, group by product, SUM all quantities, sort descending, and take five rows.

## Main idea

For queries across these three tables, connect records with both conditions:

```sql
Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
```

Without the linking conditions, unrelated rows are combined and totals become wrong.
