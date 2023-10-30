#print([i*i for i in range(10) if i%2==0])
"""
source1:
id

source2:
id

import pandas as pd
df1=pd.read_csv(0)

df2[df2.id not in [<list>]]

df2.merge(df1, on="id", how="left")

employee:

id salary managerid

-find all employees whose salary is greater than manager

select e1.id as emp_id,m1.id as manager_id, m1.salary as manager_salary, e1.salary as emp_salary
from employee e1 join employee m1 on m1.managerid=e1.id and e1.salary>m1.salary


-find out third highest salary

select *
from (
select *, dense_rank() over(order by salary desc) as salary_rank
) cte
where salary_rank=3

"""
