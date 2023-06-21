select p.product_id,round(sum(p.price*u.units)/sum(u.units),2) average_price from prices p join unitssold u on p.product_id=u.product_id and u.purchase_date between p.start_date and p.end_date group by u.product_id 


