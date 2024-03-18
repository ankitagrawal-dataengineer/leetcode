with cte as
(
    select *,dense_rank() over(order by salary desc) as 'rnk'
    from employee
)
select ifnull(max(salary),null) SecondHighestSalary 
from cte where rnk=2;

