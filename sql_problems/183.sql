-- Write your PostgreSQL query statement below
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT c.id
    FROM Customers c
    INNER JOIN Orders o
    ON c.id = o.customerId
)

