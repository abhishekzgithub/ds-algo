--select * 
--,date_part('month',min_date::date)-date_part('month',max_date::date)
----,max_date::date)
----,to_date(min_date,'YYYY-MM-DD HH:MM:SS')
--from(
--select user_id
--,min(post_date) as min_date
--,max(post_date) as max_date
----,datediff(to_date(max(post_date)::text)),to_datetime(min(post_date::timestamp)))
--,extract(YEAR from post_date::timestamp) as year
--from fb_posts
--where extract(YEAR from post_date::timestamp)=2021
--group by user_id,post_date
--) as cte
----,extract(YEAR from post_date::timestamp)
----group by extract(MONTH from post_date::timestamp)
--

select user_id,min(post_date),max(post_date)
,cast(max(post_date::date)-min(post_date::date) as int)*(60*60) as difference
,extract('hour' from max(post_date)-min(post_date)) as time_difference

from fb_posts
where extract(YEAR from post_date)=2021
group by user_id
having count(post_id)>1
order by user_id
;