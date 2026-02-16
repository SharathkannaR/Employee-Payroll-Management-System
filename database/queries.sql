-- Department Salary Cost
SELECT d.dept_name, SUM(p.net_salary) AS total_salary
FROM Payroll p
JOIN Employees e ON p.emp_id = e.emp_id
JOIN Departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

-- Top Performers
SELECT e.emp_name, pr.rating
FROM Performance_Reviews pr
JOIN Employees e ON pr.emp_id = e.emp_id
ORDER BY pr.rating DESC;

-- Attendance Percentage
SELECT emp_id,
       COUNT(CASE WHEN status='Present' THEN 1 END)*100/COUNT(*) AS attendance_percentage
FROM Attendance
GROUP BY emp_id;
