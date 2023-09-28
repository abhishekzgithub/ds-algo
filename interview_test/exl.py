"""
SalesTransaction
TxnDate	SKU ID	Price	QtySold
1/1/2023	S1	$2	25
1/1/2023	S3	$10	10
1/3/2023	S5	$5	15
1/4/2023	S7	$24	3
11/10/2022	S9	$11	10
12/5/2022	S4	$4	18
8/4/2022	S5	$5	8

ProductMapping
SKU	SKU Name	Category	Sub-Category
S1	Coke	        C3	SC1
S2	Pepsi	        C4	SC4
S3	Butter	        C5	SC5
S4	Kellogs	        C8	SC1
S5	Mint	        C9	SC6
S6	Apple	        C1	SC7
S7	Ecig	        C2	SC9

1. find the topmost category sold highest daily
2. average product sold
,max product sold

with cte as (
select *, 
date_format('Y',st.TxnDate) as year,
date_format('m',st.TxnDate) as month,
date_format('d',st.TxnDate) as day,
sum(cast(replace(Price, '$',''),'integer')*QtySold) over(partition by month, day) as total_sales

from SalesTransaction st join ProductMapping pm
on st.sku=pm.sku

)
select month,day,category, max(total_sales)
from cte
group by year,month,day,category

2. what was the 
temp date
31 1/4/2023
30 1/5/2023

select *
from 

left
ID
1
1
2
4
4
NULL

right
ID
1
1
3
4

left join 
1 1
1 1
1 1
1 1
2 null
4 4
4 4
null null


"""
columns=["student","marks"]
60
70

#students having more marks than the average
"""
select *
from student
group by student
having marks>avg(marks)

"""