WITH all_products AS (
    SELECT COUNT(DISTINCT product_key) as key_count
    FROM Product
)

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING count(DISTINCT product_key) = (SELECT key_count FROM all_products);