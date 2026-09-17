# C4 Database and Basic SQL: Complete SLS Questions and Resources

- **Source:** Singapore Student Learning Space, assignment “C4 Database and Basic SQL”
- **Extracted:** 1 September 2026
- **Sections covered:** C4-1 and C4-2a to C4-2e
- **Question count:** 14

This is a prompt-only archive. It excludes the student’s answers, submission status, marks and correctness feedback.

## Resource index

### A. C4-1 Introduction to Database

- Slides: [C4-1_Introduction_to_Database.pdf](C4-1_Introduction_to_Database.pdf)
- Video: [C4-1 Introduction to Database v2](https://www.youtube.com/watch?v=LiT_ktHG1-E) (10:24)
- Transcript: `113 - C4-1 Introduction to Database v2 [LiT_ktHG1-E].txt` in `notes/transcripts`

### B. C4-2a Basic SQL: Create Database and Tables

- Slides: [C4-2a_Basic_SQL_-_create_database_and_tables.pdf](C4-2a_Basic_SQL_-_create_database_and_tables.pdf)
- Video: [C4-2a Basic SQL - create database and tables v2](https://www.youtube.com/watch?v=-OexChjx7kg) (5:06)
- Transcript: `114 - C4-2a Basic SQL - create database and tables v2 [-OexChjx7kg].txt` in `notes/transcripts`
- No SLS questions in this section.

### C. C4-2b Basic SQL: Insert Data into Tables

- Slides: [C4-2b_Basic_SQL_-_insert_data_into_tables.pdf](C4-2b_Basic_SQL_-_insert_data_into_tables.pdf)
- Video: [C4-2b Basic SQL - insert data into tables v2](https://www.youtube.com/watch?v=Qk8n6iOcb0Y) (3:10)
- Transcript: `115 - C4-2b Basic SQL - insert data into tables v2 [Qk8n6iOcb0Y].txt` in `notes/transcripts`
- No SLS questions in this section.

### D. C4-2c Basic SQL: Basic Query

- Slides: [C4-2c_Basic_SQL_-_basic_query.pdf](C4-2c_Basic_SQL_-_basic_query.pdf)
- Practice database: [Northwind.db](Northwind.db)
- Original package: [Northwind.zip](Northwind.zip)
- SLS explicitly states that no walkthrough video is provided.

### E. C4-2d and C4-2e Basic SQL: Update and Delete Records

- Slides: [C4-2d_e_Basic_SQL_-_update_and_delete_records.pdf](C4-2d_e_Basic_SQL_-_update_and_delete_records.pdf)
- Practice database: [dummy.db](dummy.db)
- Original package: [dummy.zip](dummy.zip)
- Video: [C4-2d_2e Basic SQL - Update and Delete Records and Tables v2](https://www.youtube.com/watch?v=-mC5SGlLOUU) (4:28)
- Transcript: `116 - C4-2d_2e Basic SQL - Update and Delete Records and Tables v2 [-mC5SGlLOUU].txt` in `notes/transcripts`

# A. C4-1 Introduction to Database

## Question A1: Limitations of flat files

What are some limitations of using flat files to store data?

Select one or more:

- May contain duplicate copies of the same data.
- May contain data inconsistency.
- Difficult to update or change any data.
- Difficult to search or query for information.

## Question A2: Tables in a database

Which statements are true about tables in a database?

Select one or more:

- Each record is unique.
- Each record contains data for the various fields.
- A Primary Key (PK) is the data that helps to identify a particular record.
- The order of the fields in a table is important.
- The order of the records in a table is important.

## Question A3: Number of records

The following table shows the balloon information in a gift-shop database. How many records are there in the table?

![BALLOONS table for Question A3](C4%20SLS%20question%20assets/C4-A-Q3.png)

Choices:

- 3
- 4
- 5
- 6

## Question A4: Number of fields

How many fields are there in the BALLOONS table?

![BALLOONS table for Question A4](C4%20SLS%20question%20assets/C4-A-Q4.png)

Choices:

- 3
- 4
- 5
- 6

## Question A5: Table description

![BALLOONS table for Question A5](C4%20SLS%20question%20assets/C4-A-Q5.png)

Write the table description for the table named `BALLOONS` using this format:

```text
TABLENAME (attribute1_, attribute2, ...)
```

Place an underscore after the field name to denote the Primary Key. Follow the field names exactly.

## Question A6: Primary key

The following image shows the `CUSTOMERS` table.

![CUSTOMERS table](C4%20SLS%20question%20assets/C4-A-Q6.png)

Select the primary key:

- `CustomerID`
- `Name`
- `Email`
- `Postal Code`

## Question A7: Composite primary key

The following table shows sales records for balloons. Assume a customer is not allowed to buy balloons of the same colour on the same day.

![Balloon sales table](C4%20SLS%20question%20assets/C4-A-Q7.png)

Select the fields that form the composite primary key:

- `CustomerID`
- `Colour`
- `Quantity`
- `Date`

# D. C4-2c Basic SQL: Basic Query

Use the provided `Northwind.db` database.

## Question D1: Customers from the United Kingdom

Write an SQL query to find all customers from the United Kingdom. The SLS prompt provides a partial starting hint beginning with `SELECT FirstName, LastName, ...`.

![Expected DB Browser output for Question D1](C4%20SLS%20question%20assets/C4-D-Q1.png)

## Question D2: German customers sorted by city

Write an SQL query to find all customers from Germany, sorted by city.

![Expected DB Browser output for Question D2](C4%20SLS%20question%20assets/C4-D-Q2.png)

## Question D3: Suppliers sorted by country

Write an SQL query to find all suppliers, sorted by country.

![Expected DB Browser output for Question D3](C4%20SLS%20question%20assets/C4-D-Q3.png)

## Question D4: Five highest unit prices below $20

Write an SQL query to find the products with the five highest unit prices below `$20`.

![Expected DB Browser output for Question D4](C4%20SLS%20question%20assets/C4-D-Q4.png)

## Question D5: Countries with the most products

Write an SQL query to list the three countries with the most products available.

Expected output:

- USA: 12
- Germany: 9
- Australia: 8

## Question D6: Products priced from $20 to $40

Write an SQL query to find the number of products with a unit price between `$20` and `$40`, both inclusive.

![Expected DB Browser output for Question D6](C4%20SLS%20question%20assets/C4-D-Q6.png)

# E. C4-2d and C4-2e: Update and Delete Records

Use the provided `dummy.db` database.

## Question E1: Updating product prices

1. Write an SQL command to list the unit prices of all products under `$20`.
2. Write an SQL command to increase the unit prices of all products under `$20` by `$1`.
3. Check that the command successfully increased every unit price that was originally below `$20`.
