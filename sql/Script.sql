--SELECT user_id,item,created_at
----, extract(day from max(created_at)-min(created_at)),max(created_at),min(created_at) as extract_diff
----DENSE_RANK() OVER( partition by user_id,item
----order by user_id asc) as buy_rank,
----dense_rank() OVER( order by item asc) as buy_rank_1
--,lead(created_at, 1) over(partition by user_id order by created_at asc )
--,lag(created_at, 1) over(partition by user_id order by created_at asc )
--FROM public.sales
--
--group by user_id,item,created_at
----having extract(day from max(created_at)-min(created_at)) between 1 and 7
--;


--
--select 
----a.* 
--DISTINCT(a.user_id) 
--FROM amazon_transactions a
--JOIN amazon_transactions b
--    ON a.user_id = b.user_id
--WHERE extract(day from (a.created_at - b.created_at)) between 1 and 7
--    AND a.id != b.id
--order by a.user_id asc


--select * from orders o 
--order by order_date asc;
-- Need to find out total cost order for 1st three
with cte as (
select * from orders o
order by cust_id asc,order_date asc
)
--select *,
--lag(order_date) over(partition by cust_id 
--order by order_date asc range between INTERVAL '1'  preceding  and INTERVAL '1' following) as next_day
--from cte o 
----order by order_date asc;
select *,
sum(total_order_cost) over(partition by cust_id order by order_date asc) as summ
,avg(total_order_cost) over(partition by cust_id order by order_date asc) as avgg
,count(total_order_cost) over(partition by cust_id order by order_date asc) as countt
,min(total_order_cost) over(partition by cust_id order by cust_id  asc) as minn
,max(total_order_cost) over(partition by order_date order by cust_id  asc ) as maxx
,order_date - interval  '1 day' as DAY_1_LAG,
extract(month  from order_date)
from cte
--order by cust_id asc
--alter table orders 
--drop column id;

--do $$ 
--<<first_block>>
--declare
--  film_count integer := 0;
--begin
--   -- get the number of films
--   select count(*) 
--   into film_count
--   from orders o ;
--   -- display a message
--   raise notice 'The number of films is %', film_count;
--end first_block $$;
--
--
--
--
