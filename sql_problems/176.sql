-- Write your PostgreSQL query statement below
SELECT (
    SELECT DISTINCT(salary) AS SecondHighestSalary
    FROM Employee
    ORDER BY salary desc
    OFFSET 1
    LIMIT 1
)

