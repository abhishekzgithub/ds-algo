/*
https://datalemur.com/questions/yoy-growth-rate

*This is the same question as problem #32 in the SQL Chapter of Ace the Data Science Interview!

Assume you're given a table containing information about Wayfair user transactions for different products. Write a query to calculate the year-on-year growth rate for the total spend of each product, grouping the results by product ID.

The output should include the year in ascending order, product ID, current year's spend, previous year's spend and year-on-year growth percentage, rounded to 2 decimal places.
**/

with cte as (select product_id
, extract(year from transaction_date::date) as year
,spend as curr_year_spend
,lag(spend,1) over(partition by product_id ) as prev_year_spend
from wayfair_user_transactions
order by product_id,year
)

select year as yr
,product_id
,curr_year_spend
,prev_year_spend
,(round(100*((curr_year_spend-prev_year_spend)/prev_year_spend)::decimal,2)) as yoy_rate
from cte


