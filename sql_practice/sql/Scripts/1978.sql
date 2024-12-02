--https://leetcode.com/problems/employees-whose-manager-left-the-company/?envType=study-plan-v2&envId=top-sql-50

/*

Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.
*/

select * from Employees1978;

select * from Employees1978
where salary::integer <30000
and manager_id not in (select DISTINCT(employee_id) from Employees1978)

/*
https://leetcode.com/problems/exchange-seats/?envType=study-plan-v2&envId=top-sql-50
Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.
*/
select student,
case 
when id::INTEGER%2=0 then lag
--when id::INTEGER%2!=0 then lead
else COALESCE(lead,id)
end as newid
from (
select 
*,
lag(id,1) over(order by id)
,lead(id,1) over(order by id)
from seat
) as lag_lead_seat
order by newid


select * from seat