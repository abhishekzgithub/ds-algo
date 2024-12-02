--SELECT employee_id, department_id, primary_flag
--FROM public."Employee";
--with employee_single_n as (
--select employee_id, department_id
--from "Employee" e 
--where employee_id in (
--select e.employee_id
--from public."Employee" e 
--group by employee_id
--having count(department_id)=1
--)
--order by employee_id
--),
--
--employee_multiple_y as (
--select employee_id,department_id
--from public."Employee" e 
--
--where primary_flag='Y'
--)
--
--select * from employee_multiple_y union select * from employee_single_n ;
--
--with employee_count_cte as (
--select *,
--count(employee_id) over (partition by department_id) as employee_count
--from "Employee" e 
--order by employee_id
--)
--select * from employee_count_cte where employee_count=1 or primary_flag='Y'
--

select * from (
select *,
count(employee_id) over (partition by employee_id) as employee_count
from "Employee" e 
order by employee_id
) 
where primary_flag='Y' or employee_count=1

SELECT 
  employee_id, 
  department_id 
FROM 
  (
    SELECT 
      *, 
      COUNT(employee_id) OVER(PARTITION BY employee_id) AS EmployeeCount
    FROM 
      "Employee"
  ) EmployeePartition 
WHERE 
  EmployeeCount = 1 
  OR primary_flag = 'Y';

