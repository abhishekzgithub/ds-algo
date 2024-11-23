--SELECT guest_id, nationality, gender, age
--FROM public.airbnb_guests;

--select *
--from airbnb_hosts ah, airbnb_guests ag
--where ah.nationality =ag.nationality 
--and ah.gender =ag.gender 
--;

select  distinct host_id, guest_id
from airbnb_hosts ah, airbnb_guests ag
where ah.nationality =ag.nationality 
and ah.gender =ag.gender 
--group by 1,2
order by 1,2
;

