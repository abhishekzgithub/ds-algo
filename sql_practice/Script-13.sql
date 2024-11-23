--SELECT id, cust_id, order_date, order_details, total_order_cost
--FROM public.google_orders_1;
--
--select * 
--from google_customers_1 gc left join google_orders_1 go2 
--on gc.id=go2.cust_id 
--;

select count(address) 
from google_customers_1 gc left join google_orders_1 go2 
on gc.id=go2.cust_id 
;