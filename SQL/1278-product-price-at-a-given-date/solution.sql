with cte as(
    select distinct
        product_id,
        new_price as price,
        dense_rank() over(
            partition by product_id
            order by change_date desc
        ) as product_partition
        from products
        where change_date<='2019-08-16'
)
select
    product_id,
    price 
from cte
where product_partition=1

union

select 
    product_id,
    10 as price
from products
where product_id not in(
    select
        product_id
    from cte
)