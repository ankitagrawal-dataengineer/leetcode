SELECT ROUND(SUM(tiv_2016),2) as tiv_2016
FROM insurance i1
WHERE tiv_2015 IN (SELECT tiv_2015 FROM insurance i2
                   WHERE i1.pid != i2.pid)
AND (lat, lon) NOT IN (SELECT lat, lon FROM insurance i3
                       WHERE i3.pid != i1.pid)

