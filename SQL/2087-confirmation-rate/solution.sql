select s.user_id,round(sum(coalesce(c.action='confirmed',0))/count(*),2) as confirmation_rate
from signups s left join confirmations c
on s.user_id=c.user_id 
group by s.user_id;