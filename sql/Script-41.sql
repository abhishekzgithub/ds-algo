/*
 * https://datalemur.com/questions/prime-warehouse-storage
 * Amazon wants to maximize the number of items it can stock in a 500,000 square feet warehouse. 
 * It wants to stock as many prime items as possible, and afterwards use the 
 * remaining square footage to stock the most number of non-prime items.

Write a query to find the number of prime and non-prime items that can be stored in the 500,000 square feet warehouse. 
Output the item type with prime_eligible followed by not_prime and the maximum number of items that can be stocked.

Effective April 3rd 2023, we added some new assumptions to the question to provide additional clarity.

Assumptions:

Prime and non-prime items have to be stored in equal amounts, regardless of their size or square footage. 
This implies that prime items will be stored separately from non-prime items in their respective containers, 
but within each container, all items must be in the same amount.
Non-prime items must always be available in stock to meet customer demand, so the non-prime item count should never be zero.
Item count should be whole numbers (integers).
 * 
 * */

--select * from amazon_inventory at2 
--where not exists (
--select * from amazon_inventory at1 where at1.item_id=at2.item_id and item_type='prime_eligible'
--)
--;

--select  item_type
----,count(*) as item_count
--,sum(square_footage) over(partition by item_type) as total_sqft
--from amazon_inventory 
--group by item_type,square_footage


select 
50000/sum(square_footage)
--,100*(square_footage/500000) as item_count
from amazon_inventory 
where item_type='prime_eligible'

