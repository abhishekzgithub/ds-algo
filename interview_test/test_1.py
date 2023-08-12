# select
# (select count(distinct id) from hr.emp group by id) as total_count
# ,(select count(distinct id) from hr.emp where gender='M' group by id) as male_count
# ,(select count(distinct id) from hr.emp where gender='F' group by id) as female_count
# from hr.emp

# with gender as (
# select sum(
# case when gender='M' then 1 else 0 end
# ) gender_count
# from hr.emp
# group by 
# )

# select sum(
# case when gender='M' then 1 else 0 end
# ) male_gender_count
# ,sum(
# case when gender='F' then 1 else 0 end
# ) female_gender_count
# ,(select count(distinct id) from hr.emp )
# from hr.emp
# group by gender


# select department_name, count(distinct emp.id) as employee_count
# from hr.employees emp left join hr.departments dept
# on emp.department_id=dept.department_id
# group by emp.department_id
