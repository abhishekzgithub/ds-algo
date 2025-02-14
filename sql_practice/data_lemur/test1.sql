/*****************************************************************************
https://platform.stratascratch.com/coding/2156-unique-employee-logins?code_type=1
Unique Employee Logins
You have been tasked with finding the worker IDs of individuals who logged in between the 13th to the 19th inclusive of December 2021.
In your output, provide the unique worker IDs for the dates requested.
*/

select * from worker_logins
order by worker_id, login_timestamp;


select worker_id from worker_logins
where login_timestamp between '2021-12-13' and '2021-12-19'
group by worker_id
 