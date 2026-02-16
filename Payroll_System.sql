/*Payroll_system*/
use payroll_system

-- Creating a Table for Seq_numbers 
CREATE TABLE seq_numbers (
    n INT PRIMARY KEY
);
-- Inserting numbers into Seq_numbers Table
INSERT INTO seq_numbers (n)
VALUES
(1),(2),(3),(4),(5),(6),(7),(8),(9),(10),
(11),(12),(13),(14),(15),(16),(17),(18),(19),(20),
(21),(22),(23),(24),(25),(26),(27),(28),(29),(30),
(31),(32),(33),(34),(35),(36),(37),(38),(39),(40),
(41),(42),(43),(44),(45),(46),(47),(48),(49),(50),
(51),(52),(53),(54),(55),(56),(57),(58),(59),(60),
(61),(62),(63),(64),(65),(66),(67),(68),(69),(70),
(71),(72),(73),(74),(75),(76),(77),(78),(79),(80),
(81),(82),(83),(84),(85),(86),(87),(88),(89),(90),
(91),(92),(93),(94),(95),(96),(97),(98),(99),(100),
(101),(102),(103),(104),(105),(106),(107),(108),(109),(110),
(111),(112),(113),(114),(115),(116),(117),(118),(119),(120),
(121),(122),(123),(124),(125),(126),(127),(128),(129),(130),
(131),(132),(133),(134),(135),(136),(137),(138),(139),(140),
(141),(142),(143),(144),(145),(146),(147),(148),(149),(150);

/*Creating a Departments table*/
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL UNIQUE
);

/*Creating a Employees Table*/
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    hire_date DATE,
    dept_id INT,
    base_salary DECIMAL(10,2),
    status ENUM('Active', 'Inactive') DEFAULT 'Active',
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

/*Creating a Attendance Table*/
CREATE TABLE Attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    attendance_date DATE,
    status ENUM('Present', 'Absent'),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

/*Creating a Leave Table*/
CREATE TABLE Leaves (
    leave_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    leave_start DATE,
    leave_end DATE,
    reason VARCHAR(255),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

/*Creating a Performance_Reviews Table*/
CREATE TABLE Performance_Reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    review_date DATE,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

/*Creating a Salary Table*/
CREATE TABLE Salary (
    salary_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    month VARCHAR(20),
    year INT,
    bonus DECIMAL(10,2) DEFAULT 0,
    deductions DECIMAL(10,2) DEFAULT 0,
    final_salary DECIMAL(10,2),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

/*Inserting the Data into Departments*/
INSERT INTO Departments (dept_name)
VALUES ('HR'), ('IT'), ('Finance'), ('Marketing'), ('Operations');

/*Inserting Employees Data into the Employees Table*/
INSERT INTO Employees (emp_name, email, phone, hire_date, dept_id, base_salary, status)
SELECT
    CONCAT('Employee_', n),
    CONCAT('employee', n, '@company.com'),
    CONCAT('9', LPAD(FLOOR(RAND()*1000000000),9,'0')),
    DATE_SUB(CURDATE(), INTERVAL FLOOR(RAND()*1500) DAY),
    FLOOR(1 + RAND()*5),
    FLOOR(25000 + RAND()*75000),
    IF(RAND() > 0.1, 'Active', 'Inactive')
FROM seq_numbers;

-- inserting Attendance
INSERT INTO Attendance (emp_id, attendance_date, status)
SELECT
    e.emp_id,
    DATE_SUB(CURDATE(), INTERVAL FLOOR(RAND()*60) DAY),
    IF(RAND() > 0.15, 'Present', 'Absent')
FROM Employees e
JOIN seq_numbers s ON s.n <= 2;

-- Inserting values into Leaves
INSERT INTO Leaves (emp_id, leave_start, leave_end, reason)
SELECT
    FLOOR(1 + RAND()*150),
    DATE_SUB(CURDATE(), INTERVAL FLOOR(RAND()*200) DAY),
    DATE_ADD(CURDATE(), INTERVAL FLOOR(RAND()*5) DAY),
    ELT(FLOOR(1 + RAND()*4),'Medical','Vacation','Personal','Emergency')
FROM seq_numbers
LIMIT 120;

-- Performance Previews
INSERT INTO Performance_Reviews (emp_id, review_date, rating, comments)
SELECT 
    e.emp_id,
    DATE_SUB(CURDATE(), INTERVAL FLOOR(RAND()*365) DAY),
    FLOOR(1 + RAND()*5),
    ELT(FLOOR(1 + RAND()*4),
        'Excellent',
        'Good',
        'Average',
        'Needs Improvement')seq_numbersperformance_reviewsperformance_reviews
FROM Employees e
ORDER BY RAND()
LIMIT 180;

-- Inserting a Values into Salary Table
INSERT INTO Salary (emp_id, month, year, bonus, deductions, final_salary)
SELECT
    e.emp_id,
    ELT(FLOOR(1 + RAND()*6),'Jan','Feb','Mar','Apr','May','Jun'),
    2025,
    FLOOR(RAND()*10000),
    FLOOR(RAND()*4000),
    e.base_salary + FLOOR(RAND()*5000)
FROM Employees e
JOIN seq_numbers s ON s.n <= 1;

------------------------------------------------------------------------------------------------------------
select count(*) from Employees
select count(*) from Departments
SELECT COUNT(*) FROM Leaves;
SELECT COUNT(*) FROM Performance_Reviews;
SELECT COUNT(*) FROM Salary;


-- attendance of employee in asc
select * from Attendance
order by emp_id asc;

-- Latest Employees hired First 10
SELECT emp_id, emp_name, hire_date
FROM Employees
ORDER BY hire_date DESC
LIMIT 10;

-- highest salary first 10
SELECT emp_id, emp_name, base_salary
FROM Employees
ORDER BY base_salary DESC
LIMIT 10;





