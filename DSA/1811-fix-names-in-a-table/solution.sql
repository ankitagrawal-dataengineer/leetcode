select user_id,concat(upper(left(name,1)),
'',lower(right(name,length(name)-1))) name 
from users order by user_id
