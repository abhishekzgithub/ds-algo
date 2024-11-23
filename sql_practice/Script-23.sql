--Write a SQL to get all the products that got sold on both the days and the number of times the product is sold.

--select * from wayfair_order_tbl order by product_id;


--select product_id from wayfair_order_tbl w1 where order_day='2015-05-02'
--except
--select product_id from wayfair_order_tbl w1 where order_day='2015-05-01'


-- prod1,prod2,prod3

select * from 
(select product_id from wayfair_order_tbl where order_day ='2015-05-01')
as wh,(select product_id from wayfair_order_tbl where order_day ='2015-05-02')
as wh1
where wh.product_id


wayfair_order_tbl 
where order_day in ('2015-05-01','2015-05-02')
order by order_day,product_id

 
