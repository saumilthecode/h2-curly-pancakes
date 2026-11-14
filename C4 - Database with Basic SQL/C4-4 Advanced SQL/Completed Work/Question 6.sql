SELECT SUM(UnitPrice * Quantity)
FROM Products, Orders
WHERE Products.Id = Orders.ProductID
AND ProductName = 'Ipoh Coffee';
