select t1.Department,t1.Employee,t1.Salary from
(select d.name as Department,e.name as Employee,e.salary as Salary,
dense_rank() over(partition by d.id order by salary desc) as rk
from Employee e join department d on e.departmentId = d.id) as t1
where rk=1





