/*
 * https://datalemur.com/questions/completed-trades
 * Assume you're given the tables containing completed trade orders and user details in a Robinhood trading system.

Write a query to retrieve the top three cities that have the highest number of completed trade 
orders listed in descending order. 
Output the city name and the corresponding number of completed trade orders.
 */
/*
Pandas
df=df_robinhood_trades.merge(df_robinhood_cities,how="left",on=["user_id"])
df_result=df[df.status=="Completed"].groupby("city").count()
df_result.index
*/

--select * from robinhood_trades
select rc.city
--,rc.user_id
,count(*) 
from robinhood_trades rt left join robinhood_cities rc on rt.user_id=rc.user_id
where 1=1
and status='Completed'
group by rc.city
order by  count(*) desc
limit 3


