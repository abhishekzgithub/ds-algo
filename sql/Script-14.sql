--select * 
--from google_customers_1 gc  join google_orders_1 go2 
--on gc.id =go2.cust_id 
--order by gc.id asc;
with cte as (
select count(address)*100/count(*)
from google_customers_1 gc  join google_orders_1 go2 
on gc.id =go2.cust_id 
--order by go2.id asc
)
select count(address)*100/count(*) as percent_shipable from cte;

