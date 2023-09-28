--SELECT *
--from facebook_post_views fpv left join facebook_posts fp
--on fpv.post_id =fp.post_id;

select distinct post_date
,sum(case
	when post_keywords like '%spam%'
	then 1
	else 0
end  
)*100/count(*) as spam_digit

from facebook_post_views fpv left join facebook_posts fp
on fpv.post_id =fp.post_id
group by post_date
;