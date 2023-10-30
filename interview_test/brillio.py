"""

t1 t2
1	1
1	1
1	2
2	2
3	4
3	null
3

full outer join
t1  t2
1   1
1   1
1   1
1   1
1   1
1   1
1   1
1   1
1   1
1   1
1   1
2   2
2   2


right join
t1  t2
1   1
1   1
1   1
1   1
1   1
1   1
2   2
2   2
null 4
null   null

Inner join
t1 t2
1   1
1   1
1   1
1   1
1   1
1   1
2   2
2   2

Left join
t1 t2
1   1
1   1
1   1
1   1
1   1
1   1
2   2
2   2
3   null
3   null
3   null


employee:

id name salary deptid 

select * from(
select * , dense_rank() over(partition by id,deptid order by salary desc) as salary_rank
from employee
) cte_employee
where salary_rank in (1,2,3)


"""


# def find_min_max(arr):
#     minn=arr[0]
#     maxx=arr[0]
#     for ele in arr:
#         if ele >maxx:
#             maxx=ele
#         elif ele<minn:
#             minn=ele
#     print("Minimum is ",minn)
#     print("Maximum is ",maxx)

# arr=[234,45,-23,45,-56,567]
# find_min_max(arr)

"""
sales:
orderid custid order_date total_amount


1. total revenue

2.lazy evaluation

"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark=SparkSession.builder.appName("test").getOrCreate()

dataframe=spark.createDataFrame()

dataframe.withColumn("total_revenue",sum(F.col("total_amount")))
