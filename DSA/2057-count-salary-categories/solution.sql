select category, accounts_count from (
    select (
        case when income < 20000 then 'Low Salary'
        when income > 50000 then 'High Salary'
        else 'Average Salary' end
    ) as category, count(*) as accounts_count
    from accounts
    group by category
    union (select 'Low Salary', 0)
    union (select 'Average Salary', 0)
    union (select 'High Salary', 0)
) t
group by category
