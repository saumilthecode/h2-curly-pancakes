#Copy your query statement into the string below.

query1='''
SELECT DISTINCT ProductName
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND FirstName = 'Ann'
AND LastName = 'Devon';
'''
