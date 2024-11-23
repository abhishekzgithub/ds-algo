with apple_users as (
SELECT  user_id ,device
FROM public.playbook_events pe
where 
1=1
and (device like '%iphone 5s%'
or device like '%macbook pro%'
or device like '%ipad air%')
)
select 
pu."language"
,count(distinct(au.user_id)) as n_apple_users
,count(distinct(pu.user_id))

from playbook_users pu 
join playbook_events pe on pu.user_id =pe.user_id 
left join apple_users au on pu.user_id =au.user_id
group by pu."language" 
order by 2 desc,3 desc
