with cte as
(
    select requester_id as id from RequestAccepted
    union all
    select accepter_id from RequestAccepted
)

select id,count(*) as num
from cte
group by id
order by num desc 
limit 1
