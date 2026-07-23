WITH customer_stats AS (
    SELECT
        customer_id,
        DATEDIFF(MAX(transaction_date), MIN(transaction_date)) AS active_days,
        COUNT(*) AS total_transactions,
        SUM(CASE WHEN transaction_type = 'purchase' THEN 1 ELSE 0 END) AS purchase_transactions,
        SUM(CASE WHEN transaction_type = 'refund' THEN 1 ELSE 0 END) AS refund_transactions
    FROM customer_transactions
    GROUP BY customer_id
)
SELECT customer_id
FROM customer_stats
WHERE active_days >= 30
  AND purchase_transactions >= 3
  AND 1.0 * refund_transactions / total_transactions < 0.2
ORDER BY customer_id;