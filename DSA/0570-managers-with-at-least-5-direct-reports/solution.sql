select e2.name
from employee e1 join employee e2
on e1.managerid=e2.id
group by e1.managerid 
having count(*)>=5;
