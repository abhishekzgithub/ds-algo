with cte as (
SELECT "date", consumption, 'eu' as region
FROM public.fb_eu_energy
union
SELECT "date", consumption, 'asia' as region
FROM public.fb_asia_energy
union
SELECT "date", consumption, 'na' as region
FROM public.fb_na_energy
),
cte2 as (
select "date",sum(consumption) as total_consumption, dense_rank() over(order by sum(consumption) desc) as col_rank  from cte
group by "date"
order by 1 desc,2 desc
)
select "date", total_consumption
from cte2
where col_rank=1

;

