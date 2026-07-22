with heavy_weeks as(
    select
        employee_id,
        YEARWEEK(meeting_date,1) AS week_no,
        SUM(duration_hours) AS total_hours
    FROM meetings
    GROUP BY
        employee_id,
        YEARWEEK(meeting_date,1)
    HAVING SUM(duration_hours) > 20
)

select
    e.employee_id,
    e.employee_name,
    e.department,
    count(*) as meeting_heavy_weeks
from employees e
join heavy_weeks hw
on
    e.employee_id=hw.employee_id
group by  
    e.employee_id,
    e.employee_name,
    e.department
having
    COUNT(*)>=2
order by
    meeting_heavy_weeks desc,
    e.employee_name;