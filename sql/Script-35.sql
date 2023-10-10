--https://datalemur.com/questions/odd-even-measurements
with cte as (
select 
*
, row_number() over(partition by measurement_time::date order by measurement_time asc) as measurement_num
from google_odd_even_measurements
)
select measurement_time::date
,sum(case when measurement_num%2!=0 then measurement_value end) as odd_sum
,sum(case when measurement_num%2=0 then measurement_value end) as even_sum
from cte
group by measurement_time::date

;