# Write your MySQL query statement below
select w2.id as Id
from weather w1 join weather w2
ON w2.recordDate = DATE_ADD(w1.recordDate, INTERVAL 1 DAY)
where w2.temperature>w1.temperature; 

