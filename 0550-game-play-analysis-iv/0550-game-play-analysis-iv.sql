# Write your MySQL query statement below
# SELECT ROUND(COUNT(m.player_id) / COUNT(DISTINCT a.player_id), 2) AS fraction
# FROM activity a
# LEFT JOIN (
#     SELECT player_id, MIN(event_date) AS first_login
#     FROM activity
#     GROUP BY player_id
# ) AS m ON m.player_id = a.player_id AND DATE_ADD(m.first_login, INTERVAL 1 DAY) = a.event_date

# Common Table Expression
WITH first_logins AS (
    SELECT a.player_id, MIN(a.event_date) as first_login
    FROM activity as a
    GROUP BY a.player_id
), consec_logins AS (
    SELECT COUNT(A.player_id) AS num_logins
    FROM first_logins as F INNER JOIN
        activity as A ON F.player_id = A.player_id 
        AND F.first_login = DATE_SUB(A.event_date, INTERVAL 1 DAY)
)

SELECT ROUND((SELECT C.num_logins FROM consec_logins C) / 
             (SELECT COUNT(F.player_id) FROM first_logins F), 2) AS fraction;