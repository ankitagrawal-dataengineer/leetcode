# Write your MySQL query statement below
with highest_salary as(
    select d.name as department,e.name as employee,e.salary,dense_rank() over(partition by e.departmentId order by e.salary desc) as rk
    from employee e join department d
    on e.departmentId=d.id
)

select department,employee,salary
from highest_salary
where rk=1;