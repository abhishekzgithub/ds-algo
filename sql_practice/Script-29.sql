/*https://datalemur.com/questions/sql-avg-review-ratings
 * Average Review Ratings [Amazon SQL Interview Question]
Given the reviews table, write a query to retrieve the 
average star rating for each product, grouped by month. 
The output should display the month as a numerical value, 
product ID, and average star rating rounded to two decimal places. 
Sort the output first by month and then by product ID.
 */

/*pandas
 * df_amazon_reviews_agg=df_amazon_reviews.groupby(["product_id",df_amazon_reviews.index.month]).mean("stars").sort_values(by=["submit_date","product_id"],ascending=False)

df_amazon_reviews_agg=df_amazon_reviews.groupby(["product_id",df_amazon_reviews.submit_date.dt.month]).mean("stars").sort_values(by=["submit_date","product_id"],ascending=False)


 */

select extract(month from submit_date) as mth
,product_id as product
,avg(stars)::float as avg_stars
from amazon_reviews

group by product_id ,extract(month from submit_date)
order by extract(month from submit_date) desc, product_id desc
;
