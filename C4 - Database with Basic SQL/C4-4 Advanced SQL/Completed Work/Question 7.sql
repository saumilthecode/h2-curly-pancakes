SELECT ProductName, SUM(Quantity)
FROM Customers, Orders, Products
WHERE Customers.Id = Orders.CustomerID
AND Orders.ProductID = Products.Id
AND Country = 'USA'
GROUP BY Products.Id, ProductName
ORDER BY SUM(Quantity) DESC
LIMIT 5;
