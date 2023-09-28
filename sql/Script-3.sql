SELECT id, "date", user1, user2, msg_count
FROM public.fb_messages
order by user1 
;

select user1,count(*)
from fb_messages fm 
group by user1 
order by user1 asc
;

with message_sent as
(

)