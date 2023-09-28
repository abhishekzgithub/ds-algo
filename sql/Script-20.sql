--SELECT id, first_name, last_name, age, sex, employee_title, department, salary, target, bonus, email, city, address, manager_id
--FROM public.employee;

--with cte as (
--select *, dense_rank() over(order by salary desc) as salary_rank from employee
--)
--select * from cte where salary_rank=2
--with cte as (
--select * from employee order by salary desc limit 2
--)
--select * from cte
--order by salary asc limit 1

--select * FROM Employee Emp1 WHERE 1 = ( 
--SELECT COUNT(DISTINCT(Emp2.Salary)) FROM Employee Emp2
--  WHERE Emp2.Salary > Emp1.Salary
--  )
--  
  
select (
SELECT Emp2.salary ,Emp1.salary  FROM Employee Emp2, Employee Emp1
  WHERE Emp2.Salary > Emp1.Salary
  
  
  )
  FROM Employee Emp1 
  
  WHERE 1 = ( 
SELECT * FROM Employee Emp2
  WHERE Emp2.Salary > Emp1.Salary
  )
    
