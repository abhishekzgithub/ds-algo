SELECT distinct (a.user_id)
FROM public.amazon_transactions a,public.amazon_transactions b
where a.id<>b.id
and extract( day from (b.created_at -a.created_at)) between 0 and 7
and a.user_id =b.user_id 
order by a.user_id 
;


with time_between_purchases as (
select user_id, created_at - lag(created_at) over (Partition by user_id order by created_at ASC) as time_from_last_purchase
,created_at
,lag(created_at) over (Partition by user_id order by created_at ASC)
from amazon_transactions 
order by user_id, created_at ASC
)
select distinct user_id 
from time_between_purchases
where extract(day from time_from_last_purchase) <= 7


