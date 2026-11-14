SELECT SUM(UnitPrice * Quantity)
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND FirstName = 'Manuel'
AND LastName = 'Pereira'
AND OrderDate LIKE 'Jul 30 2012%';
