#Copy your query statement into the string below.

query1='''
SELECT SUM(UnitPrice * Quantity)
FROM Products, Orders
WHERE Products.Id = Orders.ProductID
AND ProductName = 'Ipoh Coffee';
'''
