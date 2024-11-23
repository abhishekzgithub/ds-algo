SELECT user_id_sender, user_id_receiver, "date", "action"
FROM public.fb_friend_requests

;

with temptable as (
SELECT f1.user_id_sender ,f2.user_id_receiver ,f1."date" as accepted_date, f1."action",f2."action" 
FROM fb_friend_requests f1 left join fb_friend_requests f2
on f1.user_id_sender =f2.user_id_sender 
and f1.user_id_receiver =f2.user_id_receiver 
and f2."action" ='accepted' 
where f1."action" ='sent'
--group by 1,2,3,4,5
order by f1.user_id_sender 

where f1."action" <>f2."action" 
and f1.user_id_sender =f2.user_id_sender 
and f1.user_id_receiver =f2.user_id_receiver 
and (f1."action" ='sent'
and f2."action" ='accepted')
--group by f1."date" 
order by f1."date" asc
)
select accepted_date,(count(user_id_receiver)/count(*)::float/1) from temptable
group by accepted_date;

SELECT 
     Q1.date,
     COUNT(Q2.user_id_receiver)
     ,COUNT(Q1."date")
    ,(COUNT(Q2.user_id_receiver) / COUNT(Q1.*)::float/1) as percentage_acceptance 
FROM fb_friend_requests Q1
LEFT JOIN fb_friend_requests Q2 
    ON Q1.user_id_sender = Q2.user_id_sender 
    AND Q1.user_id_receiver = Q2.user_id_receiver 
    AND Q2.action = 'accepted' 
WHERE  Q1.action='sent'
GROUP BY Q1.date
ORDER BY Q1.date

