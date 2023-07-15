# Write your MySQL query statement below
with CTE1 as
(
select u.name,  dense_rank() over(order by count(m.rating) desc, u.name asc) as rnk1
from MovieRating as m
join Users as u 
using (user_id)
group by user_id
),

CTE2 as
(
select m2.title, dense_rank() over(order by avg(rating) desc, m2.title asc) as rnk2 
from MovieRating as m1
join Movies as m2
using (movie_id)
where m1.created_at between '2020-02-01' and '2020-02-29'
group by movie_id

)

select name as results 
from CTE1
where rnk1 = 1

union all

select title as results
from CTE2
where rnk2 = 1
;
