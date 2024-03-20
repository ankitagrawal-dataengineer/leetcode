with cte as
(
    select account_id, case
    when income<20000 then 'Low Salary' 
    when income>50000 then 'High Salary'
    else 'Average Salary'
    end as 'category'
    from accounts
),
cte_1 as
(
    select 'Low Salary' category 
    union
    select 'Average Salary' category
    union
    select 'High Salary' category
)
select c2.category,count(account_id) accounts_count
from cte c1 right join cte_1 c2 on c1.category=c2.category
group by c1.category;
