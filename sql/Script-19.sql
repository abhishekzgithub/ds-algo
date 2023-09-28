--SELECT id, cust_id, order_date, order_details, total_order_cost
--FROM public.orders;

--select first_name, sum(total_order_cost) as total_order_cost, o.order_date
--from orders o left join customers c
--on o.cust_id=c.id 
--where o.order_date between '2019-02-01' and '2019-05-01'
--group by first_name,o.order_date 
--order by sum(total_order_cost) desc
--limit 1
--;

select first_name,order_date ,order_details,total_order_cost 
from orders o left join customers c
on o.cust_id=c.id 
where first_name in ('Jill','Eva')
order by cust_id asc
;


