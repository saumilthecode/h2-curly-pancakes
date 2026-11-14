# C4-2 Basic SQL: Answers and Checks

Checked locally on 11 November 2026 using fresh database downloads from the Coursemology task.

## Files

- Slides are in [Slides](../Slides/): the four individual C4-2 PDFs and C4-2 Basic SQL.pdf (26 pages). The [Specimen Insert](../../Shared%20Resources/Specimen%20Insert.pdf) is in Shared Resources.
- Question 1.sql to Question 7.sql contain the SQL answers.
- Question N - Coursemology.py contains the same SQL inside the required query1 triple-quoted string. Paste the whole file into the corresponding code editor.
- Question N - Results.csv contains locally checked output.
- Source databases contains untouched fresh Northwind.db and dummy.db downloads. Pre-existing databases are retained in [Shared Resources/Databases](../../Shared%20Resources/Databases/).
- dummy_Q7_completed.db is a separate copy with the Question 7 update applied once.
- Create Tables.sql, Insert Data.sql, and Database.db reproduce the C4-2a/b table-and-insert examples in the slides. These working files are separate from the shared databases.

## Browser status

All seven answers are entered and were rechecked by returning to every question. The user approved the site's automatic saving after it was discovered. No Check Answer, Submit, or Save Draft button was clicked. Every question still showed Past Answers (0), so no answer was sent for marking.

## Local checks

- Q1: 7 UK customers, matching the displayed expected set.
- Q2: 11 German customers in ascending city order, matching the displayed expected list.
- Q3: 29 distinct supplier-country pairs, ordered by country.
- Q4: Ravioli Angelo 19.50; Gula Malacca 19.45; Chang 19; Inlagd Sill 19; Boston Crab Meat 18.40, matching the displayed expected list.
- Q5: USA 12; Germany 9; Australia 8, matching the displayed expected list.
- Q6: 26, matching the displayed expected result.
- Q7: 40 products originally below $20 increased by $1; all other prices unchanged; 0 incorrect prices.

### Q7 sample-output discrepancy

The website's displayed expected list includes Maxilaku at 20 after the update, suggesting an original price of 19. However, the freshly downloaded dummy.db has Maxilaku priced at 20 already. The wording says under $20, so the correct SQL leaves it unchanged. The SQL below follows the question, rather than altering the condition to force the sample output.

## Question 1: Find all customers from UK.

```sql
SELECT FirstName, LastName, Country
FROM Customers
WHERE Country = 'UK';
```

WHERE selects only UK customers. The three selected fields match the expected output.

## Question 2: Find all customers from Germany sorted by city.

```sql
SELECT FirstName, LastName, Country, City
FROM Customers
WHERE Country = 'Germany'
ORDER BY City;
```

WHERE selects German customers, and ORDER BY City sorts them in ascending order.

## Question 3: Find all suppliers sorted by country.

```sql
SELECT DISTINCT SupplierName, SupplierCountry
FROM Products
ORDER BY SupplierCountry;
```

DISTINCT removes repeated supplier-country pairs because a supplier can provide several products.

## Question 4: Find the products with the top five highest unit prices below $20.

```sql
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice < 20
ORDER BY UnitPrice DESC
LIMIT 5;
```

Filter below $20 first, sort prices from highest to lowest, then take five rows.

## Question 5: List the top three countries with the most products available.

```sql
SELECT SupplierCountry, COUNT(ProductName)
FROM Products
GROUP BY SupplierCountry
ORDER BY COUNT(ProductName) DESC
LIMIT 3;
```

GROUP BY gathers each country's products; COUNT counts them; descending order and LIMIT give the top three.

## Question 6: Count products priced between $20 and $40, both inclusive.

```sql
SELECT COUNT(Id)
FROM Products
WHERE UnitPrice BETWEEN 20 AND 40;
```

BETWEEN includes both $20 and $40. The result is 26.

## Question 7: Increase the unit prices of all products under $20 by $1.

```sql
UPDATE Products
SET UnitPrice = UnitPrice + 1
WHERE UnitPrice < 20;
```

The WHERE condition applies to each original price, so only prices originally below $20 increase by $1. Run this update only once on a fresh database copy.

## Key reminders

- WHERE filters individual records before grouping.
- GROUP BY creates groups for aggregate functions such as COUNT.
- ORDER BY sorts ascending by default; DESC sorts descending.
- LIMIT restricts the number of output rows.
- Always use a WHERE condition with UPDATE or DELETE when only some records should change.
