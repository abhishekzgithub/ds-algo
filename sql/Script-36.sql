---https://datalemur.com/questions/sql-highest-grossing
--select category,product, max(spend) over(order by product rows between 2 preceding and current row)
--from amazon_product_spend
--
--where extract(year from transaction_date)=2022
----group by category,product,spend
----order by max(spend) desc
----limit 2
--;
--select * from (
--select category,product, spend as total_spend
--,dense_rank() over(partition by category ,product order by max(spend) desc) spend_rank
----max(spend) over(partition by product )
----order by product rows between 2 preceding and current row)
--from amazon_product_spend
--
--where extract(year from transaction_date)=2022
--group by category,product,spend
----order by max(spend) desc
----limit 2
--) cte
--where spend_rank<3
--
--;
--
--select * from (
--select category,product, spend as total_spend
--,dense_rank() over(partition by category ,product order by max(spend) desc) spend_rank
----max(spend) over(partition by product )
----order by product rows between 2 preceding and current row)
--from amazon_product_spend
--
--where extract(year from transaction_date)=2022
--group by category,product,spend
----order by max(spend) desc
----limit 2
--) cte
--where spend_rank<3
--
--;

select category,product, total_spend
from (
select category,product, sum(spend) as total_spend
,dense_rank() over(partition by category order by sum(spend) desc) spend_rank
from amazon_product_spend

where extract(year from transaction_date)=2022
group by category,product
order by category,sum(spend) desc
)cte where spend_rank<3

;


 