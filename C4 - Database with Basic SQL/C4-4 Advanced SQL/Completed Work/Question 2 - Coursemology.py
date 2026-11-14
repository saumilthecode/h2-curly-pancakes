#Copy your query statement into the string below.

query1='''
SELECT DISTINCT Customers.Id, FirstName, LastName
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND ProductName = 'Lakkalik ri'
AND OrderDate LIKE '%Feb%2013%';
'''
