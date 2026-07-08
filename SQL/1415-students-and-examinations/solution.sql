select s1.student_id,s1.student_name,s2.subject_name,count(e.subject_name) as attended_exams
from students s1 cross join subjects s2 left join examinations e
on s1.student_id=e.student_id and e.subject_name=s2.subject_name
group by s1.student_id,s2.subject_name
order by s1.student_id,s2.subject_name;
