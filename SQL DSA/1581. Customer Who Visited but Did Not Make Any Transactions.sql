SELECT customer_id, COUNT(customer_id) as count_no_trans
FROM Transactions AS tra
RIGHT JOIN Visits AS vis
ON vis.visit_id = tra.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id