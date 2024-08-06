SELECT name
FROM salesperson where name not in
(SELECT s.name
FROM salesperson s 
join Orders o 
on s.sales_id = o.sales_id
join company c 
on c.com_id = o.com_id 
where c.name='RED')
