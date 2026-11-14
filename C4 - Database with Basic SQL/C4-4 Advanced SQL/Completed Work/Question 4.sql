SELECT COUNT(DISTINCT Customers.Id)
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND SupplierCountry = 'UK';
