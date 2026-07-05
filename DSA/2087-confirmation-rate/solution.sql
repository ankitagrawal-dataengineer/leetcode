select s.user_id,coalesce(round(avg(c.action='confirmed'),2),0) as confirmation_rate
from signups s left join confirmations c
on s.user_id=c.user_id
group by s.user_id;
