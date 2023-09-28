SELECT *
FROM 
--public.playbook_events pe join
playbook_users pu 

--on pe.user_id =pu.user_id 
;

--SELECT pu."language" ,pe.device,count(distinct (pe.user_id))
--FROM public.playbook_events pe join playbook_users pu 
--on pe.user_id =pu.user_id 
--where 
--1=1
--and (device like '%iphone%'
--or device like '%macbook%'
--or device like '%ipad%')
--group by pu."language" ,device
--order by 3 desc
--;


WITH apples AS
    (SELECT 
        u.user_id
        , u.language
        , e.device
    FROM playbook_users u
    JOIN playbook_events e
    ON u.user_id = e.user_id
    WHERE device ILIKE '%MacBook_Pro%'
        OR device ILIKE '%iPhone_5s%' 
        OR device ILIKE '%iPad_air%'
    )
SELECT
    u.language
    , COUNT(DISTINCT a.user_id) AS n_apple_users
    , COUNT(DISTINCT u.user_id) AS n_all_users
FROM playbook_users u
JOIN playbook_events e
ON u.user_id = e.user_id
LEFT JOIN apples a
ON u.user_id = a.user_id
GROUP BY 1
ORDER BY 3 DESC;