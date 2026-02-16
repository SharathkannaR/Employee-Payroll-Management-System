from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database connection configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Sharath@05",
    "database": "payroll_system"
}

# Helper function to get a fresh database connection
def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

# Employess Data API
@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Employees LIMIT 50")
        employees = cursor.fetchall()
        return jsonify(employees)
    except mysql.connector.Error as err:
        print(f"Query error: {err}")
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Departments Data API
@app.route('/employee-departments', methods=['GET'])
def employee_departments():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT e.emp_name, d.dept_name, e.base_salary
        FROM Employees e
        JOIN Departments d ON e.dept_id = d.dept_id
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        print(f"Query error: {err}")
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Top 5 Salaries API
@app.route('/top-salaries', methods=['GET'])
def top_salaries():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT emp_name, base_salary
        FROM Employees
        ORDER BY base_salary DESC
        LIMIT 5
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        print(f"Query error: {err}")
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Attendance Summary API
@app.route('/attendance-summary', methods=['GET'])
def attendance_summary():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT emp_id, COUNT(*) AS present_days
        FROM Attendance
        WHERE status = 'Present'
        GROUP BY emp_id
        ORDER BY present_days DESC
        LIMIT 10
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        print(f"Query error: {err}")
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

@app.route("/api/salary-by-dept")
def salary_by_department():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT d.dept_name AS department,
                   SUM(e.base_salary) AS total_salary
            FROM Employees e
            JOIN Departments d ON e.dept_id = d.dept_id
            GROUP BY d.dept_name
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        print(f"Query error: {err}")
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Department Salary API (for dashboard)
@app.route("/api/department-salary", methods=['GET'])
def department_salary():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT d.dept_name, SUM(e.base_salary) AS total_salary
            FROM Employees e
            JOIN Departments d ON e.dept_id = d.dept_id
            GROUP BY d.dept_name
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        print(f"Query error: {err}")
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Attendance Trend API (for dashboard)
@app.route("/api/attendance-trend", methods=['GET'])
def attendance_trend():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT DATE(attendance_date) AS attendance_date, COUNT(*) AS present
            FROM Attendance
            WHERE status = 'Present'
            GROUP BY DATE(attendance_date)
            ORDER BY attendance_date DESC
            LIMIT 30
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        print(f"Query error: {err}")
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Top Performers API (for dashboard)
@app.route("/api/top-performers", methods=['GET'])
def top_performers():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT e.emp_name, ROUND(AVG(pr.rating)) AS rating
            FROM Employees e
            JOIN Performance_Reviews pr ON e.emp_id = pr.emp_id
            GROUP BY e.emp_id, e.emp_name
            ORDER BY rating DESC
            LIMIT 10
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        print(f"Query error: {err}")
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

# Hiring Growth API (for dashboard)
@app.route("/api/hiring-growth", methods=['GET'])
def hiring_growth():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    try:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT DATE_FORMAT(hire_date, '%Y-%m') AS month, COUNT(*) AS hires
            FROM Employees
            WHERE hire_date IS NOT NULL
            GROUP BY DATE_FORMAT(hire_date, '%Y-%m')
            ORDER BY month DESC
            LIMIT 12
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        print(f"Query error: {err}")
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)

