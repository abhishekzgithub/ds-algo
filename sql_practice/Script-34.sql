/*
 * 
 */

select age_bucket
,round(100.0 *(sending_time/(opening_time+sending_time))::decimal,2) as send_perc
,round(100.0 *(opening_time/(opening_time+sending_time))::decimal,2) as open_perc
from (
select 
age_bucket
,sum(case 
	when activity_type='open' then time_spent else 0
end
) opening_time
,
sum(case 
	when activity_type='send' then time_spent else 0
end
) sending_time

from snapchat_activites_age
group by age_bucket
--, activity_id,activity_type,time_spent
)cte
;