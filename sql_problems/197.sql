-- Write your PostgreSQL query statement below
SELECT id
FROM Weather as main
WHERE temperature > (
    SELECT sub.temperature
    FROM Weather as sub
    WHERE sub.recordDate = main.recordDate - 1
)

