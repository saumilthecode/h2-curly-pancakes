SELECT SupplierCountry, COUNT(ProductName)
FROM Products
GROUP BY SupplierCountry
ORDER BY COUNT(ProductName) DESC
LIMIT 3;
