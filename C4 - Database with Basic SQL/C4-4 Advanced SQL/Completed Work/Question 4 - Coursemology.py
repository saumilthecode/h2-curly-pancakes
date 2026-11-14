#Copy your query statement into the string below.

query1='''
SELECT COUNT(DISTINCT Customers.Id)
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND SupplierCountry = 'UK';
'''
