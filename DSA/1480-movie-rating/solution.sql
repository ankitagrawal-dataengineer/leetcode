with cte1 as
(
    select u.name,dense_rank()
    over(order by count(m.user_id) desc,u.name asc) rnk1
    from users u join movierating m
    using(user_id)
    group by m.user_id 
),

cte2 as
(
    select m1.title,dense_rank()
    over(order by avg(m2.rating) desc,m1.title asc) rnk2
    from movies m1 join movierating m2
    using(movie_id)
    where m2.created_at between '2020-02-01' and '2020-02-29'
    group by m2.movie_id
)

select name as results from cte1 where rnk1=1
union all
select title as results from cte2 where rnk2=1



