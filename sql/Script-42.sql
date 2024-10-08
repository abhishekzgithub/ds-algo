/*
 * https://datalemur.com/questions/median-search-freq
 * Google's marketing team is making a Superbowl commercial and needs a simple statistic to put on their TV ad: the median number of searches a person made last year.

However, at Google scale, querying the 2 trillion searches is too costly. Luckily, you have access to the summary table which tells you the number of searches made last year and how many Google users fall into that bucket.

Write a query to report the median of searches made by a user. Round the median to one decimal point.
 * */

--select * 
--from google_search_frequency
--
--;

--select searches 
--from google_search_frequency
--
--group by searches,
--generate_series(0,num_users)
--order by searches


WITH searches_expanded AS (
  SELECT searches
  FROM google_search_frequency
  GROUP BY 
    searches, 
    GENERATE_SERIES(1, num_users))

SELECT 
  ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (
    ORDER BY searches)::DECIMAL, 1) AS  median
FROM searches_expanded;
