-- Write your PostgreSQL query statement below
SELECT e.name AS Employee
FROM Employee as e
WHERE e.managerId IS NOT NULL
AND e.salary > (
    SELECT sub.salary
    FROM Employee AS sub
    WHERE sub.id = e.managerId
)

