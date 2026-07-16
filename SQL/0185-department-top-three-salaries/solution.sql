with cte as(
    select d.name as Department,
    e.name as Employee,
    e.salary as Salary,
    dense_rank() over(
        partition by d.id
        order by e.salary desc
        ) as rank_salary
    from employee e
    join department d
        on e.departmentid=d.id
)
select
    Department,
    Employee,
    Salary
from cte
where rank_salary<=3;