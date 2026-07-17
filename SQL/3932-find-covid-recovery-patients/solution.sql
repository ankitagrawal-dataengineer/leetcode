with first_positive as(
    select 
        patient_id,
        min(test_date) as test_date
    from covid_tests
    where result='Positive'
    group by patient_id
)

select
    p.patient_id as patient_id,
    p.patient_name as patient_name,
    p.age as age,
    datediff(min(ct.test_date),fp.test_date) as recovery_time
from first_positive fp
join covid_tests ct
on
    fp.patient_id=ct.patient_id
and ct.result='Negative'
and ct.test_date>fp.test_date
join patients p
on
    p.patient_id=ct.patient_id
group by
    p.patient_id
order by
    recovery_time,
    p.patient_name