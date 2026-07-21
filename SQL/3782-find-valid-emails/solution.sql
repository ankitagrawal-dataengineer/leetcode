select
    user_id,
    email
from users
WHERE 
    email REGEXP '^[A-Za-z0-9_]+@[A-Za-z]+\\.com$'
order by 
    user_id;