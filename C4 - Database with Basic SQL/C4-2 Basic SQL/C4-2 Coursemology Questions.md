# C4-2 Coursemology Questions

Source: https://yijc.coursemology.org/courses/3257/assessments/88874

Audited: 12 November 2026. Complete prompt-only archive: 7 questions. Personal answers, feedback, grades, submission state and comments are excluded. Original source wording is retained, including unusual database spellings.

## Question 1

Write the query statement to find all the customers from UK (in the Northwind.db database).

Output from DB Browser should be as follows:

![Question 1 source image 1](Source%20Resources/Question%20assets/Q1-1.png)

To help you with the first question, paste your SQL Query statement into line 4 in the template:

![Question 1 source image 2](Source%20Resources/Question%20assets/Q1-2.png)

### Provided template

```python
#Copy your query statement into the string below.

query1='''
SELECT which attribute(s) FROM which table(s)
'''
```

### Displayed public expected output

```text
ans1
Expected: {('Thomas', 'Hardy', 'UK'), ('Simon', 'Crowther', 'UK'), ('Elizabeth', 'Brown', 'UK'), ('Ann', 'Devon', 'UK'), ('Hari', 'Kumar', 'UK'), ('Helen', 'Bennett', 'UK'), ('Victoria', 'Ashworth', 'UK')}
```

## Question 2

Write the query statement to find all the customers from Germany sorted by the city.

Output from DB Browser should be as follows:

![Question 2 source image 1](Source%20Resources/Question%20assets/Q2-1.png)

### Provided template

```python
#Copy your query statement into the string below.

query1='''
SELECT which attribute(s) FROM which table(s) and other necessary condition(s)
'''
```

### Displayed public expected output

```text
ans1
Expected: [('Sven', 'Ottlieb', 'Germany', 'Aachen'), ('Maria', 'Anders', 'Germany', 'Berlin'), ('Philip', 'Cramer', 'Germany', 'Brandenburg'), ('Horst', 'Kloss', 'Germany', 'Cunewalde'), ('Renate', 'Messner', 'Germany', 'Frankfurt a.M.'), ('Henriette', 'Pfalzheim', 'Germany', 'K ln'), ('Alexander', 'Feuer', 'Germany', 'Leipzig'), ('Hanna', 'Moos', 'Germany', 'Mannheim'), ('Peter', 'Franken', 'Germany', 'Mnchen'), ('Karin', 'Josephs', 'Germany', 'Mnster'), ('Rita', 'Mller', 'Germany', 'Stuttgart')]
```

## Question 3

Write the query statement to find all the supplier sorted by the country.

Output from DB Browser should be as follows:

![Question 3 source image 1](Source%20Resources/Question%20assets/Q3-1.png)![Question 3 source image 2](Source%20Resources/Question%20assets/Q3-2.png)

### Provided template

```python
#Copy your query statement into the string below.

query1='''
SELECT which attribute(s) FROM which table(s) and the necessary condition(s)
'''
```

### Displayed public expected output

```text
ans1 in correct_answers
Expected: True
```

## Question 4

Write the query statement to find the products with top 5 highest unit prices below $20.

Output from DB Browser should be as follows:

 ![Question 4 source image 1](Source%20Resources/Question%20assets/Q4-1.png)

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
Expected: [('Ravioli Angelo', 19.5), ('Gula Malacca', 19.45), ('Chang', 19), ('Inlagd Sill', 19), ('Boston Crab Meat', 18.4)]
```

## Question 5

Write the query statement to list the top 3 countries with the most products available.

Output From DB Browser should be as follows:

USA : 12

Germany : 9

Australia : 8

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
Expected: [('USA', 12), ('Germany', 9), ('Australia', 8)]
```

## Question 6

Write the query statement to find the number of products with unit price between $20 and $40, both inclusive.

Output From DB Browser should be as follows:
![Question 6 source image 1](Source%20Resources/Question%20assets/Q6-1.png)

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
Expected: [(26,)]
```

## Question 7

Write the SQL command to increase the unit prices of all the products under $20 by $1.

### Provided template

```python
#Copy your query statement into the string below.

query1='''
write the SQL command to update the unit price of which table with the necessary condition(s)
'''
```

### Displayed public expected output

```text
new_prices
Expected: [('Aniseed Syrup', 11), ('Boston Crab Meat', 19.4), ('Chai', 19), ('Chang', 20), ('Chartreuse verte', 19), ('Chocolade', 13.75), ('Escargots de Bourgogne', 14.25), ('Filo Mix', 8), ('Geitost', 3.5), ('Genen Shouyu', 16.5), ('Gorgonzola Telino', 13.5), ('Guaran\xa0 Fant\xa0stica', 5.5), ('Gula Malacca', 20.45), ('Inlagd Sill', 20), ("Jack's New England Clam Chowder", 10.65), ('Konbu', 7), ('Lakkalik ri', 19), ('Laughing Lumberjack Lager', 15), ('Longlife Tofu', 11), ('Louisiana Hot Spiced Okra', 18), ('Maxilaku', 20), ('NuNuCa Nua-Nougat-Creme', 15), ('Original Frankfurter grne Soae', 14), ('Outback Lager', 16), ('Pavlova', 18.45), ('R d Kaviar', 16), ('Ravioli Angelo', 20.5), ('Rh nbr u Klosterbier', 8.75), ('Rogede sild', 10.5), ('Sasquatch Ale', 15), ('Scottish Longbreads', 13.5), ('Singaporean Hokkien Fried Mee', 15), ("Sir Rodney's Scones", 11), ('Spegesild', 13), ('Steeleye Stout', 19), ('Stroopwafels', 10.75), ('Teatime Chocolate Biscuits', 10.2), ('TourtiSre', 8.45), ('Tunnbr d', 10), ('Valkoinen suklaa', 17.25), ('Zaanse koeken', 10.5)]
```

## Source and resource notes

See [Resource audit](Source%20Resources/Resource%20audit.md) for original download links, file comparisons and image provenance. Templates were recovered from the existing source-capture JSON, not from personal answer code; whitespace display markers were normalised. All descriptions and displayed expected outputs were checked against the live assessment.
