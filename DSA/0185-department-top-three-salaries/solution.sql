SELECT t1.Department, t1.Employee, t1.Salary
FROM (SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary,
DENSE_RANK() OVER(PARTITION BY d.id ORDER BY salary DESC) AS rk
FROM Department AS d
JOIN Employee AS e ON E.departmentId = d.id) AS t1
WHERE rk<=3
