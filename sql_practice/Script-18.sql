--SELECT id, "location", age, gender, is_senior
--FROM public.facebook_employees;

select location, avg(popularity) 
from facebook_hack_survey fhs   join facebook_employees fe 
on fhs.employee_id =fe.id 
group by location
;