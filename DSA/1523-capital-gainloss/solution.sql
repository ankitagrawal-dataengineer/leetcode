with cte as
(
    select stock_name, 
    sum(case when operation='Sell' then price
    end) as sell,
    sum(case when operation='Buy' then price
    end) as buy
    from stocks group by stock_name
)
select stock_name,sell-buy as capital_gain_loss 
from cte;

