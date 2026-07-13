WITH partition_product_id AS (
    SELECT *,
           DENSE_RANK() OVER (
               PARTITION BY product_id
               ORDER BY change_date DESC
           ) AS rk
    FROM Products
    WHERE change_date <= '2019-08-16'
)

SELECT product_id, new_price AS price
FROM partition_product_id
where rk=1

UNION

Select product_id,10 as price
from products 
where product_id not in (
    select product_id from partition_product_id
);