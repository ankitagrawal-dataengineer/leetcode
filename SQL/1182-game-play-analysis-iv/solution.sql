with first_login as(
    select
        player_id,
        min(event_date) as first_login_date
        from activity
        group by player_id
)

select 
    round(sum(datediff(
        a.event_date,f.first_login_date)=1)
        /count(distinct a.player_id),2) as fraction
from activity a
left join first_login f
on 
    a.player_id=f.player_id;