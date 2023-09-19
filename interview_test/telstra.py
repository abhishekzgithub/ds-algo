import sys
abc=[3,4,7,1,2,9]
maxx=abc[0]
minn=abc[0]
for ele in abc:
    if ele>maxx:
        maxx=ele
    if ele<minn:
        minn=ele

print(maxx,minn)
median=(minn+maxx)/2
print(int(median))

query="""
select emp_id
from 
(select emp_id,dense_rank() over( order by salary desc) as salary_rank from employee_details)
employee
where 
salary_rank=3
group by emp_id

)
"""



"""
select * from(
select *,avg(salary) over(partition by dept order by salary desc) avg_salary
from employee_details
)employee
where salary>avg_salary


"""

import pyspark
from pyspark.sql import SparkSession,col,dense_rank
from pyspark.sql.window import Window

spark=SparkSession.builder.appName("spark").getOrCreate()
df=None
w=Window().orderBy("salary").desc().partitionBy("department")
df=df.withColumn("salary_rank",dense_rank().over(w))
df.filter(col("salary_rank")==3)