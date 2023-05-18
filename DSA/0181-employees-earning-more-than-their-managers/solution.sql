select m.name as Employee from employee e inner join employee m where e.id=m.managerid and e.salary<m.salary;
