with cte as
(
    select *,dense_rank() over(order by score desc) as rk
    from scores
)
select score,rk as 'rank'
from cte;
