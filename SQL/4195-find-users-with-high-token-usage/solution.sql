select
    user_id,
    count(prompt) as prompt_count,
    round(avg(tokens),2) as avg_tokens
from prompts
group by 
    user_id
having 
    MAX(tokens) > avg(tokens)
and count(*)>=3
order by
    avg_tokens desc,
    user_id;