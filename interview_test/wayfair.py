
# Question 1 

# https://www.programiz.com/sql/online-compiler/

#  * (a) Write a SQL to get all the products that got sold on both the days and the number of times the product is sold.
"""
select product_id ,count(product_id) from wayfair_order_tbl 
group by product_id
having count(order_day)>1
"""

#  * (b) Write a SQL to get products that was ordered on 02-May-2015 but not on 01-May-2015

"""
select * from wayfair_order_tbl
 where product_id not in (select product_id from wayfair_order_tbl where order_day ='2015-05-01')
"""

# CREATE TABLE wayfair_Order_Tbl(
#  ORDER_DAY date,
#  ORDER_ID varchar(10) ,
#  PRODUCT_ID varchar(10) ,
#  QUANTITY int ,
#  PRICE int
# ) ;

# INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-01','ODR1', 'PROD1', 5, 5);
# INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-01','ODR2', 'PROD2', 2, 10);
# INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-01','ODR3', 'PROD3', 10, 25);
# INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-01','ODR4', 'PROD1', 20, 5);
# INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR5', 'PROD3', 5, 25);
# INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR6', 'PROD4', 6, 20);
# INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR7', 'PROD1', 2, 5);
# INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR8', 'PROD5', 1, 50);
# INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR9', 'PROD6', 2, 50);
# INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR10','PROD2', 4, 10);

"""
Question2:
https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75
"""

##Other options
"""
# with order1 as (
# select * from Order_tbl
# where order_day='2015-05-01'
# ),
# order2 as (
# select * from Order_tbl
# where order_day='2015-05-02'
# )
# select * from order2
# where product_id not in (select product_id from order1 )

"""