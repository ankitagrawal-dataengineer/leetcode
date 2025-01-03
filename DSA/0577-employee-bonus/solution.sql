select e.name,b.bonus from employee e left join bonus b
on e.empId = b.empId where b.empId is null or b.bonus<1000;

