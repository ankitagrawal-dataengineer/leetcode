with cte as
(
    select e.id,e.name employee,
    e.salary salary,
    d.name department,dense_rank() 
    over(partition by d.id 
    order by e.salary desc) 'rnk'
    from employee e join
    department d on e.departmentid=
    d.id
)

select department,employee,salary
from cte where rnk=1;
