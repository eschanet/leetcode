# Write your MySQL query statement below
select
    a.Name as employee
from Employee as a join Employee as b
    on a.ManagerId = b.Id
where a.Salary > b.Salary


    
    