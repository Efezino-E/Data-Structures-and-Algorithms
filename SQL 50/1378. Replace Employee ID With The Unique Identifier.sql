SELECT unique_id, name
FROM Employees AS Emp
LEFT JOIN EmployeeUNI AS EmpUNI
ON Emp.id = EmpUNI.id