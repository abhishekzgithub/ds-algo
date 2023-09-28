/*
 * Write a query to identify the top 2 Power Users who sent the highest number 
 * of messages on Microsoft Teams in August 2022. 
 * Display the IDs of these 2 users along with the total number of messages they sent. 
 * Output the results in descending order based on the count of the messages.

Assumption:

No two users have sent the same number of messages in August 2022.
 */

select sender_id,count(message_id)  as message_count
from microsoft_messages
where extract(month from sent_date)=8
and extract(year from sent_date)=2022
group by sender_id
order by count(message_id) desc
limit 2