import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# CONNECT TO DATABASE
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sharath@05",   # your mysql password
    database="payroll_system"
)

# DEPARTMENT-WISE SALARY COST
query1 = """
SELECT d.dept_name, SUM(e.base_salary) AS total_salary
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
"""

df1 = pd.read_sql(query1, conn)

plt.figure(figsize=(8,5))
plt.bar(df1['dept_name'], df1['total_salary'])
plt.title("Department-wise Salary Cost")
plt.xlabel("Department")
plt.ylabel("Total Salary")
plt.show()

# Attendance Trend
query2 = """
SELECT attendance_date, COUNT(*) AS present_count
FROM Attendance
WHERE status = 'Present'
GROUP BY attendance_date
ORDER BY attendance_date
"""

df2 = pd.read_sql(query2, conn)

plt.figure(figsize=(8,5))
plt.plot(df2['attendance_date'], df2['present_count'])
plt.title("Daily Attendance Trend")
plt.xlabel("Date")
plt.ylabel("Employees Present")
plt.xticks(rotation=45)
plt.show()

# Top Performers
query3 = """
SELECT e.emp_name, AVG(p.rating) AS avg_rating
FROM Performance_Reviews p
JOIN Employees e ON p.emp_id = e.emp_id
GROUP BY e.emp_name
ORDER BY avg_rating DESC
LIMIT 10
"""

df3 = pd.read_sql(query3, conn)

plt.figure(figsize=(8,5))
plt.barh(df3['emp_name'], df3['avg_rating'])
plt.title("Top 10 Performers")
plt.xlabel("Average Rating")
plt.ylabel("Employee")
plt.show()

# Hiring Growth
query4 = """
SELECT DATE_FORMAT(hire_date, '%Y-%m') AS month, COUNT(*) AS hires
FROM Employees
GROUP BY month
ORDER BY month
"""

df4 = pd.read_sql(query4, conn)

plt.figure(figsize=(8,5))
plt.plot(df4['month'], df4['hires'], marker='o')
plt.title("Hiring Growth Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Hires")
plt.xticks(rotation=45)
plt.show()
