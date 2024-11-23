/*
 * https://datalemur.com/questions/cards-issued-difference
 * Cards Issued Difference [JPMorgan Chase SQL Interview Question]
Your team at JPMorgan Chase is preparing to launch a new credit card, 
and to gain some insights, you're analyzing how many credit cards were issued each month.

Write a query that outputs the name of each credit card 
and the difference in the number of issued cards between the month with the highest issuance cards 
and the lowest issuance. Arrange the results based on the largest disparity.
 */
--with cte as (
--select card_name
--,max(issued_amount) over(partition by card_name) as max_ranking
--,min(issued_amount) over(partition by card_name) as min_ranking
--from jpmc_monthly_card_issued 
--
--order by card_name,issue_year,issue_month
--)
--select card_name,max_ranking::int-min_ranking::int as difference from cte
--group by card_name,max_ranking,min_ranking

SELECT 
  card_name, 
  MAX(issued_amount::int) - MIN(issued_amount::int) AS difference
FROM jpmc_monthly_card_issued
GROUP BY card_name
ORDER BY difference DESC;


