# Write your MySQL query statement below
SELECT ROUND(COUNT(m.player_id) / COUNT(DISTINCT a.player_id), 2) AS fraction
FROM activity a
LEFT JOIN (
    SELECT player_id, MIN(event_date) AS first_login
    FROM activity
    GROUP BY player_id
) AS m ON m.player_id = a.player_id AND DATE_ADD(m.first_login, INTERVAL 1 DAY) = a.event_date
