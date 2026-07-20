SELECT s1.id, s1.visit_date, s1.people
FROM stadium s1
JOIN stadium s2 ON s1.id = s2.id + 1
JOIN stadium s3 ON s2.id = s3.id + 1
WHERE s1.people >= 100
  AND s2.people >= 100
  AND s3.people >= 100

UNION

SELECT s2.id, s2.visit_date, s2.people
FROM stadium s1
JOIN stadium s2 ON s1.id = s2.id + 1
JOIN stadium s3 ON s2.id = s3.id + 1
WHERE s1.people >= 100
  AND s2.people >= 100
  AND s3.people >= 100

UNION

SELECT s3.id, s3.visit_date, s3.people
FROM stadium s1
JOIN stadium s2 ON s1.id = s2.id + 1
JOIN stadium s3 ON s2.id = s3.id + 1
WHERE s1.people >= 100
  AND s2.people >= 100
  AND s3.people >= 100

ORDER BY visit_date;