# C4-4 Coursemology Questions

Source: https://yijc.coursemology.org/courses/3257/assessments/88878

Audited: 12 November 2026. Complete prompt-only archive: 7 questions. Personal answers, feedback, grades, submission state and comments are excluded. Original source wording is retained, including unusual database spellings.

## Question 1: Create database tables

Follow the slides from 1 to 8 closely to create the 3 tables in Database.db: 

Customers

Products

Orders (create this table last)

Submit this empty database here.

Upload constraint: EXACTLY 1 file.

## Question 2

Download the Northwind.db database and use it for all the query questions.

Write a SQL query statement to find the Customers, i.e. FirstName and LastName, who purchased the product "Lakkalik ri" in Feb 2013

Output from DB Browser should be as follows:

![Question 2 source image 1](Coursemology%20source%20resources/C4-4/Question%20assets/Q2-1.png)

### Provided template

```python
#Copy your query statement into the string below.

query1='''
SELECT which attribute(s) FROM which table(s) and necessary condition(s)
'''
```

### Displayed public expected output

```text
ans1
Expected: {(24, 'Maria', 'Larsson'), (87, 'Pirkko', 'Koskitalo')}
```

## Question 3

Write a SQL query statement to find how much Manuel Pereira spent on Jul 30 2012.

Output from DB Browser should be as follows:

![Question 3 source image 1](Coursemology%20source%20resources/C4-4/Question%20assets/Q3-1.png)

### Provided template

```python
#Copy your query statement into the string below.

query1='''
SELECT which attribute(s) FROM which table(s) and necessary condition(s)
'''
```

### Displayed public expected output

```text
ans1
Expected: {(380,)}
```

## Question 4

Write a SQL query statement to count the number of different customers buying products from UK.

Output from DB Browser should be as follows:

![Question 4 source image 1](Coursemology%20source%20resources/C4-4/Question%20assets/Q4-1.png)

### Provided template

```python
#Copy your query statement into the string below.

query1='''
SELECT which attribute(s) FROM which table(s) and necessary condition(s)
'''
```

### Displayed public expected output

```text
ans1
Expected: {(50,)}
```

## Question 5

Write a SQL query statement to list all the products purchased by Ann Devon.

Output from DB Browser should be as follows:

![Question 5 source image 1](Coursemology%20source%20resources/C4-4/Question%20assets/Q5-1.png)

### Provided template

```python
#Copy your query statement into the string below.

query1='''
SELECT which attribute(s) FROM which table(s) and necessary condition(s)
'''
```

### Displayed public expected output

```text
ans1
Expected: {('Spegesild',), ('Konbu',), ('Inlagd Sill',), ('Guaran\xa0 Fant\xa0stica',), ('Gula Malacca',), ('Gnocchi di nonna Alice',), ('Sirop d rable',), ('Flotemysost',)}
```

## Question 6

Write a SQL query statement to find the total revenue received from all the orders for 'Ipoh Coffee'.

Output From DB Browser should be as follows:
![Question 6 source image 1](Coursemology%20source%20resources/C4-4/Question%20assets/Q6-1.png)

### Provided template

```python
#Copy your query statement into the string below.

query1='''
SELECT which attribute(s) FROM which table(s) and necessary condition(s)
'''
```

### Displayed public expected output

```text
ans1
Expected: [(12604,)]
```

## Question 7

Write a SQL query statement to list the top 5 products that has the highest quantities sold to American customers.

Output from DB Browser should be as follows:

![Question 7 source image 1](Coursemology%20source%20resources/C4-4/Question%20assets/Q7-1.png)

You may want to note that there are 122 records of orders made by American customers,

each of these orders has the quantity ordered by the customer.

In these 122 orders, there are only 57 unique products.

To look for Top5 products ordered, you may consider adding up all the quantities of a particular product.

### Provided template

```python
#Copy your query statement into the string below.

query1='''
SELECT which attribute(s) FROM which table(s) and necessary condition(s)
'''
```

### Displayed public expected output

```text
ans1
Expected: {('Geitost', 189), ('Gorgonzola Telino', 144), ('R ssle Sauerkraut', 124), ('C te de Blaye', 149), ("Chef Anton's Cajun Seasoning", 134)}
```

## Source and resource notes

See [Resource audit](Coursemology%20source%20resources/C4-4/Resource%20audit.md) for original download links, file comparisons and image provenance. Templates were recovered from the existing source-capture JSON, not from personal answer code; whitespace display markers were normalised. All descriptions and displayed expected outputs were checked against the live assessment.
