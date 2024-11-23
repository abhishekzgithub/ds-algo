--SELECT id, first_name, last_name, age, sex, employee_title, department, salary, target, bonus, email, city, address, manager_id
--FROM public.employee;

select * from 
(
select first_name,salary,department,
dense_rank() over(partition by department order by salary desc) as salary_rank
from employee e 
--order by id asc, department
) empl
where salary_rank=3 


create table temp_table_2 (
B int
);

insert into temp_table_2(B) values (1),(1),(0),(null);




);