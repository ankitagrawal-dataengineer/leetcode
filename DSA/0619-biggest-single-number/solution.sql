with cte as (select max(num) num from mynumbers group by num having count(num)=1 )
select max(num) num from cte;


