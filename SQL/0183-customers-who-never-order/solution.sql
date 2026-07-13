SELECT c.name AS Customers
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customerid = c.id
);