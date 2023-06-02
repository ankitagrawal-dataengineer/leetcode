select p.product_id, ROUND(SUM(p.price * u.units) / SUM(units), 2) as average_price
from Prices p join UnitsSold u
on p.product_id = u.product_id
and u.purchase_date between p.start_date and p.end_date
group by u.product_id
