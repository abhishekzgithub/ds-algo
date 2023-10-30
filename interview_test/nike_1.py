"""
marketing analytics
pyspark,aws,databricks,airflow,tableau,snowflake
lead data engineer;work through stake holders,product mananger, requirements
----
Imagine an e-commerce firm doing business across the globe. There are 500M transactions happening on a day on average and at the end of the day the data is landing on S3 location as a single delimited file. 
The schema of the transaction data file is:

Transaction_id, customer_id, transaction_amt, country_code.

Today, most of the transactions volume come from the US, you can imagine the distribution is 80% from the US and remaining 20% spread across other countries

Design a batch pipeline that can read this data and create a report with total transaction amount at each country level. Ensure the design is scalable for any transactions growth in the future and also factor in distribution changes, for example 6 months later the distribution could be 60% US, 30% China and 10% remaining countries.

source: s3

destination:redshift


5,000,000

10000

500


USA 400
country_code
customer_id

salting

China 100

->any preprocessing
doing transformation
applying the actions
saving the into database using indexes


"""

"""
Write a query to retrieve data for customers who registered in the past ten days and spent over $100. 
The first table is a customer purchase table with five columns: 

customer id, purchase date, product id, unit price, and units purchased. 

The second table is a customer details table with two columns:
 customer id and registration date.

with cte as (
select cp.cutomer_id,cp.purchase_date,cp.product_id,cp.unit_price,cp.units_purchased,cd.registration_date, (cp.unit_price*cp.units_purchased) as total_spent
from customer_purchase as cp join customer_details as cd on cp.customer_id=cd.customer_id
)

select customer_id
from cte
where registration_date between (date.now()-10, date.now())
group by customer_id
having sum(total_spent)>100

"""

