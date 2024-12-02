-- https://leetcode.com/problems/count-salary-categories/?envType=study-plan-v2&envId=top-sql-50

/*
'Low Salary': All the salaries strictly less than $20000.
'Average Salary': All the salaries in the inclusive range [$20000, $50000].
'High Salary': All the salaries strictly greater than $50000.
*/

select * from accounts;

select count(account_id),
CASE 
    WHEN income::INTEGER<20000 THEN 'Low Salary'
    WHEN income::INTEGER>=20000 and income::INTEGER<=50000 THEN 'Average Salary'
    WHEN income::INTEGER>50000 THEN 'High Salary'
    ELSE  '0'
END as category
from accounts
group by category;


select 'Low Salary' as category,
count(income::INTEGER) as accounts_count
from accounts
where income::INTEGER<20000
union ALL
select 'Average Salary' as category,
count(income::INTEGER) as accounts_count
from accounts
where income::INTEGER BETWEEN 20000 and 50000
UNION ALL
select 'High Salary' as category,
count(income::INTEGER) as accounts_count
from accounts
where income::INTEGER >50000
