select max(salary) as secondhighestsalary from employee where salary not in (select max(Salary) from employee)
