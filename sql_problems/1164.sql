SELECT
    p.product_id,
    10 AS price
FROM Products p
GROUP BY p.product_id
HAVING MIN(p.change_date) > '2019-08-16'

UNION

SELECT
    p.product_id,
    p.new_price AS price
FROM Products p
WHERE p.change_date = (
    SELECT MAX(sub.change_date)
    FROM Products sub
    WHERE sub.change_date <= '2019-08-16'
    AND sub.product_id = p.product_id
)

