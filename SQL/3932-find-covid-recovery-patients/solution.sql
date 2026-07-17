WITH first_positive AS (
    SELECT
        patient_id,
        MIN(test_date) AS positive_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
)
SELECT
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(MIN(c.test_date), fp.positive_date) AS recovery_time
FROM first_positive fp
JOIN covid_tests c
    ON c.patient_id = fp.patient_id
   AND c.result = 'Negative'
   AND c.test_date > fp.positive_date
JOIN patients p
    ON p.patient_id = fp.patient_id
GROUP BY
    p.patient_id
ORDER BY
    recovery_time,
    p.patient_name;