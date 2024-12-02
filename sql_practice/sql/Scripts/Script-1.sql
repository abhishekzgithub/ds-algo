-- #7fd2c637bef349a587ed0b6456d04f14
-- Find all numbers that appear at least three 
-- times consecutively.

-- Return the result table in any order.

-- The result format is in the following example.

-- SELECT id, num
-- FROM public."Logs";

select num as ConsecutiveNums
from (
select id,num,
lead(num,1) over( order by id ASC) as rank1,
lead(num,2) over( order by id ASC) as rank2
from public."Logs" l
)
where  rank1=rank2 and rank2=num
group by num

-- select id
-- from public."Logs" l
-- group by id
-- having count(num)=3