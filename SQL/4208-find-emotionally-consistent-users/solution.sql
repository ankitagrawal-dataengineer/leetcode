with reaction_cte as(
    select
        user_id,
        reaction,
        count(*) as reaction_count,
        dense_rank() over(partition by user_id order by count(*) desc) as rn
        from reactions
        group by 
            user_id,
            reaction
)
select
    r.user_id,
    rc.reaction as dominant_reaction,
    round(rc.reaction_count*1.0/count(*),2) as reaction_ratio
from reactions r
join reaction_cte rc
on r.user_id=rc.user_id
where rc.rn=1
group by
    r.user_id,
    rc.reaction,
    rc.reaction_count
having 
    count(*)>=5
AND rc.reaction_count * 1.0 / COUNT(*) >= 0.60
order by
    reaction_ratio desc,
    r.user_id
