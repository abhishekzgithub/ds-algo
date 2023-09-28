select max(agg_revenue),agg_table.item
from(

SELECT sum(revenue) as agg_revenue
,extract('month' from created_at) as d
,item
FROM public.amazon_transactions
group by extract('month' from created_at),item

) as agg_table
group by item
;
