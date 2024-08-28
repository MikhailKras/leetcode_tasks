-- Write your PostgreSQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e
JOIN Department d
ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT e_sub.departmentId, MAX(e_sub.salary)
    FROM Employee e_sub
    GROUP BY e_sub.departmentId
)

