select e1.name from employee e1,employee e2 where e1.id=e2.managerid group by e1.name having count(*)>=5

