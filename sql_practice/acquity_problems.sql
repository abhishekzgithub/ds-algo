Write SQL query to retrieve departments with an average project duration greater than 6 months.

-- ouput: department

select * from acquity_employee;

select d.department_name

from  acquity_employee e
, acquity_department as d
, acquity_assignments as a
, acquity_projects as p
where e.department_id=d.department_id
and e.employee_id=a.assignment_id
and a.project_id=p.project_id
--and  extract('MONTH' from p.end_date::timestamp) - extract('MONTH' from p.start_date::date)>=6
group by d.department_name
having avg(extract('MONTH' from p.end_date::timestamp) - extract('MONTH' from p.start_date::date))>=6


select extract(month from p.end_date::timestamp),extract(month from  p.start_date::timestamp)
,(p.end_date-p.start_date)
from acquity_projects p