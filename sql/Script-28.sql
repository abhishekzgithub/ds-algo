/*
 * https://datalemur.com/questions/duplicate-job-listings
 * 
 * This is the same question as problem #8 in the SQL Chapter of Ace the Data Science Interview!

Assume you're given a table containing job postings from various companies on the LinkedIn platform. 
Write a query to retrieve the count of companies that have posted duplicate job listings.

Definition:

Duplicate job listings are defined as two job listings within the same company that share identical titles 
and descriptions.
 */

SELECT count(*) as duplicate_companies FROM (

select company_id,title,job_id ,row_number() over(partition by company_id ,title) job_row
from linkedin_joblistings
) as cte
where job_row=2 
;