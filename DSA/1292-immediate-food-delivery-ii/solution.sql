select round(sum(if (x.drnk=1 and x.order_date=x.customer_pref_delivery_date,1,0)*100)/count(distinct customer_id),2) as immediate_percentage 
from (
      select * ,dense_rank() over( partition by customer_id order by order_date) as drnk
      from delivery) x
           
          
