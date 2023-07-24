WITH child_nodes AS (
    SELECT DISTINCT p_id
    FROM Tree
    WHERE p_id IS NOT NULL
)

SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT * FROM child_nodes) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;
