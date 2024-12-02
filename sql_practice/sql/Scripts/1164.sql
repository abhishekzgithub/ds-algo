-- 1164. Product Price at a Given Date
-- Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

select * from product;

SELECT * from product
where change_date<='2019-08-16'

select product_id, max(cast(new_price as INTEGER))
 from product
where change_date<='2019-08-16'
group by product_id
union ALL
select product_id, min(cast(new_price as INTEGER))
 from product
where change_date>'2019-08-16'
group by product_id
;

