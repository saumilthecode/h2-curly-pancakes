#Copy your query statement into the string below.

query1='''
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice < 20
ORDER BY UnitPrice DESC
LIMIT 5;
'''
