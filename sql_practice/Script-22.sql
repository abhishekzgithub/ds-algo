--SELECT concat(user_firstname,'-',user_lastname) ,max(fr.reviewed_outcome  ) as appr
--FROM public.user_flags uf
--left join flag_review fr 
--on uf.flag_id =fr.flag_id 
--and fr.reviewed_outcome = 'APPROVED'
--group by user_firstname ,user_lastname ,fr.flag_id 
--;

SELECT concat(uf.user_firstname,'-',uf.user_lastname),uf.video_id , count(fr.flag_id )
FROM public.user_flags uf
left join flag_review fr 
on uf.flag_id =fr.flag_id 

where fr.flag_id is not null
and fr.reviewed_outcome = 'APPROVED'
group by uf.user_firstname ,uf.user_lastname,uf.video_id 
order by 1

;




SELECT username
FROM
  (SELECT concat(uf.user_firstname, ' ', uf.user_lastname) AS username,
          dense_rank() OVER (
                             ORDER BY count(DISTINCT video_id) DESC) AS rn
   FROM user_flags AS uf
   INNER JOIN flag_review AS fr ON uf.flag_id = fr.flag_id
   WHERE lower(fr.reviewed_outcome) = 'approved'
   GROUP BY username) AS inner_query
WHERE rn = 1

--CREATE TABLE wayfair_Order_Tbl(
-- ORDER_DAY date,
-- ORDER_ID varchar(10) ,
-- PRODUCT_ID varchar(10) ,
-- QUANTITY int ,
-- PRICE int
--) ;
--
--INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-01','ODR1', 'PROD1', 5, 5);
--INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-01','ODR2', 'PROD2', 2, 10);
--INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-01','ODR3', 'PROD3', 10, 25);
--INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-01','ODR4', 'PROD1', 20, 5);
--INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR5', 'PROD3', 5, 25);
--INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR6', 'PROD4', 6, 20);
--INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR7', 'PROD1', 2, 5);
--INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR8', 'PROD5', 1, 50);
--INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR9', 'PROD6', 2, 50);
--INSERT INTO wayfair_Order_Tbl  VALUES ('2015-05-02','ODR10','PROD2', 4, 10);

select * from wayfair_order_tbl ;

