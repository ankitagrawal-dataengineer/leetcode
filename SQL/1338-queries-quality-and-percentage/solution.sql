select query_name,round(sum(rating/position)/count(*),2) as quality,
ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
from queries group by query_name;
