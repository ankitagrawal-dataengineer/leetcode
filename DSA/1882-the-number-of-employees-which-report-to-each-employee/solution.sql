
select a1.employee_id,a1.name,count(a2.reports_to) as reports_count,
round(avg(a2.age),0) as average_age from employees a1 join employees a2 
on a1.employee_id = a2.reports_to group by a2.reports_to 
order by a1.employee_id

