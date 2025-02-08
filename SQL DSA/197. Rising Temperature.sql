SELECT a.id AS id
FROM Weather AS a
LEFT JOIN Weather AS b
ON a.recordDate = b.recordDate + INTERVAL 1 DAY
WHERE a.temperature > b.temperature