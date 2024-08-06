
select w2.id Id from weather w1 
join weather w2
where
w2.temperature > w1.temperature and
datediff(w2.recordDate,w1.recordDate)=1;
