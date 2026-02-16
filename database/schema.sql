CREATE DATABASE IF NOT EXISTS payroll_system;
USE payroll_system;

CREATE TABLE Departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL
);

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    hire_date DATE,
    dept_id INT,
    base_salary DECIMAL(10,2),
    status VARCHAR(20),
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    attendance_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

CREATE TABLE Payroll (
    payroll_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    salary_month DATE,
    gross_salary DECIMAL(10,2),
    deductions DECIMAL(10,2),
    net_salary DECIMAL(10,2),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

CREATE TABLE Leaves (
    leave_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    leave_date DATE,
    reason VARCHAR(255),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

CREATE TABLE Performance_Reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    review_date DATE,
    rating INT,
    comments VARCHAR(255),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);
