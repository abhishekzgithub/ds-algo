/*
 * https://datalemur.com/questions/sql-third-transaction
 */
select * from (
select * ,row_number() over (partition by user_id order by transaction_date asc)
from uber_transactions ut 
) cte
where row_number=3
