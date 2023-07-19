SELECT e.name
FROM Employee e
INNER JOIN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(DISTINCT id) >= 5
) m ON e.id = m.managerId;
