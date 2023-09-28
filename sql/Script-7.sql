SELECT 
--ah.*,au.*
count(distinct (au.unit_id))
FROM public.airbnb_units au join airbnb_hosts ah 
on au.host_id =ah.host_id 
where ah.age<30
and au.unit_type ='Apartment'
group by ah.nationality ,au.host_id
;
