# Write your MySQL query statement below
SELECT a.machine_id, ROUND(AVG(b.timestamp - a.timestamp), 3) as processing_time
FROM Activity AS a
LEFT JOIN Activity as b
ON  a.machine_id = b.machine_id 
    AND a.process_id = b.process_id 
    AND a.activity_type = 'start'
    AND b.activity_type = 'end'
WHERE b.timestamp - a.timestamp IS NOT NULL
GROUP BY machine_id