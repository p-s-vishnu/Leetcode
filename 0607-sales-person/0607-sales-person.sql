# 1 Salesperson can work for multiple companies
WITH red_sales AS (
    SELECT DISTINCT sales_id as id
    FROM ORDERS
    WHERE com_id = (SELECT DISTINCT com_id FROM Company WHERE name = 'RED')
)

SELECT DISTINCT s.name
FROM SalesPerson s
WHERE s.sales_id NOT IN (SELECT id from red_sales);