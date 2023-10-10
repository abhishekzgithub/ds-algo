--https://datalemur.com/questions/histogram-users-purchases


select transaction_date,user_id,count(spend) as purchase_count 
from (
SELECT transaction_date,user_id,spend
, dense_rank() over(partition by user_id order by transaction_date desc) spend_rank
FROM walmart_df_user_transactions
) as cte
where spend_rank=1
group by transaction_date,user_id
--order by transaction_date desc,user_id
;