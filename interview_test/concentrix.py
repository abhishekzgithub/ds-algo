"""
company which revenue is increasing year by year

 industry:

year      company       revenue(mill)
2021     Company A      110
2020     Company A      130
2022     Company B       96
2019     Company A     134
2019     Company C       70
2021     Company B       50
2020     Compnay C       95
2020     Company B     110  
2021     Compnay C     120

ouput: company

select * 
,case when (revenue-prev_revenue)>0 then 1 else 0
end
as diff_revenue
from (
select *
--sum(revenue) over( partition by company,year order by revenue asc),
,lag(revenue,1) over(partition by company, year order by revenue asc) as prev_revenue
)
from industry

Answer:==
WITH cte AS(SELECT tenant, YEAR(date) AS YEAR, SUM(sales) AS SALES
            FROM tenantSales
            GROUP BY tenant, YEAR(date))
SELECT c1.*, CONVERT(varchar,
                 CONVERT(DECIMAL(10,2),
                     CONVERT(DECIMAL(10, 2), (c1.SALES - c2.SALES)) /
                     CONVERT(DECIMAL(10, 2), c2.SALES))) + '%' AS "YEARLY GROWTH"
FROM cte c1
LEFT JOIN cte c2 ON c1.tenant = c2.tenant AND c2.YEAR = c1.YEAR - 1


-------------------
1.SQL to Display all the product that got sold on both the days and number of times the prodct is sold
2.SQL to get products that was ordered on 2-May-2015 but not on 1-May-2015

 sales:

ORDER_DAY      ORDER_ID	PRODUCT_ID     QUANTITY	PRICE
2015-05-01	ODR1	     PROD1             5	     5
2015-05-01	ODR2	     PROD2             2	     10
2015-05-01	ODR3	     PROD3	            10	     25
2015-05-01	ODR4	     PROD1	                     20	     5
2015-05-02	ODR5	     PROD3	                       5	     25
2015-05-02	ODR6	     PROD4	                       6	     20
2015-05-02	ODR7	     PROD1                        2	     5
2015-05-02	ODR8	     PROD5	                       1	     50
2015-05-02	ODR9	     PROD6                        2	     50
2015-05-02	ODR10	     PROD2                        4	     10

select product_id,count(order_id) 
from sales
where 1=1
group by product_id, order_day
having count(order_day)>2

select product_id
from sales
where order_id not in (select order_id from sales where order_day='2015-05-01')

pyspark:
redshift lambda

[{name: bob,id:12},[12,4554,556],IT, {address: [{office:'addxxx'},{home:'add2...'}]}]
employee,kpis,department,listofaddress

winding ,unwindings
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
spark=SparkSession.builder.appName("test").getOrCreate()

var="[{name: bob,id:12},[12,4554,556],IT, {address: [{office:'addxxx'},{home:'add2...'}]}]"

schema="""



"""
"""
5 executor
10 cores per executor

10 executors
5 cores per executor

"""