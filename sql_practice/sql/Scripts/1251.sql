-- Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places. If a product does not have any sold units, its average selling price is assumed to be 0.

select * from Prices;

select * from UnitsSold;


-- with cte as (
SELECT usold.*
,p.*
, usold.units::INTEGER * p.price::INTEGER as total_price
, case 
when
usold.purchase_date BETWEEN p.start_date and p.end_date
then 'Y'
else 'N'
end as flag
, sum((p.price::INTEGER * usold.units::INTEGER)/sum(usold.units::INTEGER))
from UnitsSold usold right join prices p
on p.product_id=usold.product_id
and usold.purchase_date BETWEEN p.start_date and p.end_date
GROUP BY usold.units,p.price

--)
select product_id, (total_price) as average_price
from (

group by product_id
;


select 