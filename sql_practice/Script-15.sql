SELECT distinct fr.post_id,
fp.poster ,fp.post_text ,fp.post_keywords ,fp.post_date 
FROM public.facebook_reactions fr join facebook_posts fp 
on fr.post_id =fp.post_id 
where reaction ='heart'
;
