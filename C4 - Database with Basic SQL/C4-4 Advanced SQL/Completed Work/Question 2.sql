SELECT DISTINCT Customers.Id, FirstName, LastName
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND ProductName = 'Lakkalik ri'
AND OrderDate LIKE '%Feb%2013%';
