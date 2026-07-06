select left(trans_date,7) as month,country,count(id) as trans_count, sum(if(state='approved',1,0)) as approved_count,sum(amount) trans_total_amount,
sum(if(state='approved',amount,0)) approved_total_amount from transactions
group by country,left(trans_date,7);


