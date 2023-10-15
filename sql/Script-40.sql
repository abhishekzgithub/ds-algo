/*
 * https://datalemur.com/questions/user-retention
 * Assume you're given a table containing information on Facebook user actions. 
 * Write a query to obtain number of monthly active users (MAUs) in July 2022, including the month in numerical format "1, 2, 3".

Hint:

An active user is defined as a user who has performed actions such as 'sign-in', 
'like', or 'comment' in both the current month and the previous month.
 */

--select *,extract(month from event_date) as  month from facebook_user_actions order by user_id;

--select user_id,extract(month from event_date)
--from facebook_user_actions 
--where event_type in ('sign-in','like','comment')
--group by user_id,extract(month from event_date)
----having count(extract(month from event_date))>1

--select * ,extract(month from f1.event_date) as current_month ,extract(month from f2.event_date) as prev_month
--from facebook_user_actions f1,facebook_user_actions f2
--where f1.user_id=f2.user_id
--and extract(month from f1.event_date)=extract(month from f2.event_date)-1

--with cte as (
--select f1.user_id, f1.event_id,f1.event_type
--
--,extract(month from f1.event_date) as current_month 
--,extract(month from f2.event_date) as prev_month
--from facebook_user_actions f1,facebook_user_actions f2
--where f1.user_id=f2.user_id
--and extract(month from f1.event_date)=extract(month from f2.event_date)-1
--and f1.event_type in ('sign-in','like','comment')
--)
--
--select prev_month as month,count(distinct user_id) as monthly_active_users
--from cte
--where prev_month=7
--group by prev_month

SELECT 
  EXTRACT(MONTH FROM curr_month.event_date) AS mth, 
  COUNT(DISTINCT curr_month.user_id) AS monthly_active_users 
FROM facebook_user_actions AS curr_month
WHERE  EXISTS (
  SELECT last_month.user_id 
  FROM facebook_user_actions AS last_month
  WHERE last_month.user_id = curr_month.user_id
    AND EXTRACT(MONTH FROM last_month.event_date) =
    EXTRACT(MONTH FROM curr_month.event_date - interval '1 month')
)
  AND EXTRACT(MONTH FROM curr_month.event_date) = 7
  AND EXTRACT(YEAR FROM curr_month.event_date) = 2022
GROUP BY EXTRACT(MONTH FROM curr_month.event_date);





