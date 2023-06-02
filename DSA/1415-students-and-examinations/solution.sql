

Select 
  s.student_id, 
  s.student_name,
  s1.subject_name,
  count(e.subject_name) as attended_exams
from Students s
join Subjects s1
left join Examinations e
on s.student_id = e.student_id 
  and s1.subject_name = e.subject_name
group by s.student_id, s1.subject_name
order by s.student_id, s1.subject_name;

