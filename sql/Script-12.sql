--SELECT "year", category, nominee, movie, winner, id
--FROM public.oscar_nominees


select count(*)
from oscar_nominees on2 
where
nominee like 'Abigail Breslin'
order by 1;