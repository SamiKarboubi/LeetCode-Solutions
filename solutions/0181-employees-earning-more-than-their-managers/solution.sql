/* Write your PL/SQL query statement below */
SELECT e.name Employee FROM Employee e,Employee m WHERE m.id=e.managerId AND e.salary>m.salary;
