-- Write your PostgreSQL query statement below
DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(id) FROM Person
    GROUP BY email
)
AND email IN (
    SELECT email FROM Person
    GROUP BY email
    HAVING COUNT(id) > 1
);

