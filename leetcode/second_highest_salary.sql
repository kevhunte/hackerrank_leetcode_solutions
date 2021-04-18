# Write your MySQL query statement below
Select Max(Salary) as SecondHighestSalary
From Employee
Where Salary < (Select Max(Salary) from Employee)