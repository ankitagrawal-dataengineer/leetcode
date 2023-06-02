select v.customer_id,count(v.customer_id) as count_no_trans from visits v left join transactions t on v.visit_id=t.visit_id WHERE t.transaction_id IS NULL  group by v.customer_id;


