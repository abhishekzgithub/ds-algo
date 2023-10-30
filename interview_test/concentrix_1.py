"""
sql: order
order_type	order_no	amount
1	1001	100
2	2002	null
2	1003	-5
2	2004	700
1	1005	900
1	1006	500
…	…	…
1	1005	900

order_type null_count negative_count total_count

with cte as (
select order_type,
case when order_no<0 then 1 else null end as negative_count_item
,case when order_no=null then 1 else null end as null_count_item

from  order
)

select order_type, count(null_count_item) as null_count, count(negative_count_item) as negative_count, count(order_no) as total_count
from cte
group by order_type

UNION

select 'total' as order_type, 'null' as null_count, 'null' as negative_count, 'null as total_count
from cte

UNION


select count(distinct order_type) as order_type
, sum(null_count_item) as null_count, sum(negative_count_item) as negative_count, sum(count(order_no)) as total_count
from cte

---
tree:
parent_id	id
        A	A1
        A	A2
        A1	A12
        A2	A21
        A2	A23
        B	B1
        B	B2
        B2	B21

LEV1 LEV2 LEV3 M2

with cte as parent_cte
select *
from tree t1 left join tree t2 on t2.id=t1.parent_id 
join tree t3 on t3.id=t2.parent_id 

Output is:
with cte as (
select 
*
from tree t1
where not exists (
select * from tree t2 where t1.parent_id=t2.id
)
)
select * from cte 
join tree on cte.id=tree.parent_id 

"""
"""
org:
department	user	t_start_date	t_end_date
sales	    tom	    1/1/2022	    10/1/2022
hr	        jack	3/1/2022	    9/1/2022
hr	        linda	3/1/2022	    10/1/2099
sales	    jack	9/1/2022	    10/1/2099
hr	        tom	    10/1/2022	    10/1/2099

[3:20 PM] Zhang, Will

who are in the HR department on 2022/06/01

select user from
org 
where department='hr'
and  t_start_date<='2022/06/01'
and  t_end_date>='2022/06/01'

lag
lead
sum
first
last
row_num
rank
dense_rank

---
table
col1 col2
a  100

a  399

a  101

b   1

b   2

-----
result
col1 col2 rolling_sum
a  100  100

a  100  499

a  111  600

b  1     1

b  2     3

select *, sum(col2) over(partition by col1) as rolling_sum
from table

---
word
python
output={'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
string =  "hello world"

def func(string):
    dict_ele={}
    for ele in string:
        if dict_ele.get(ele,None):
            dict_ele[ele]+=1
        else:
            dict_ele[ele]=1
    return dict_ele
--
check_obj = {'customer_cart_di':['cust_name','mcust_no'],'customer_click_sku_log_di':['cust_name','cust_no','mcust_no']}
    
    """
import pyspark.sql.functions as F
from pyspark.sql import SparkSession

import findspark
findspark.init()
check_obj = {'customer_cart_di':['cust_name','mcust_no'],'customer_click_sku_log_di':['cust_name','cust_no','mcust_no']}

spark=SparkSession.builder.appName("test").getOrCreate()


dataframe=spark.createDataFrame(check_obj,column=list(check_obj.keys()))

dataframe=(dataframe.withColumn("customer_cart_di",F.explode(F.col("customer_cart_di")))
           .withColumn("customer_click_sku_log_di",F.explode(F.col("customer_click_sku_log_di"))))
dataframe.show()


####
#len(dataframe[dataframe["name"].isna()])
#count of null
dataframe.withColumn("count_of_null",sum(df[col].isNull().cast()))
