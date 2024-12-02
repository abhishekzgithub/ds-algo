/*
https://leetcode.com/problems/restaurant-growth/?envType=study-plan-v2&envId=top-sql-50
Compute the moving average of how much the customer 
paid in a seven days window (i.e., current day + 6 days before). 
average_amount should be rounded to two decimal places.
Return the result table ordered by visited_on in ascending order.
The result format is in the following example.
*/

select * from Customer;

select *, lag(amount, 6) over (
        order by visited_on
    ) as lag_6
from Customer
--partition by visited_on::DATE
--partition by visited_on::DATE

select *, sum(amount::INT) over (
        order by visited_on::DATE asc RANGE BETWEEN INTERVAL '6' DAY PRECEDING
            AND CURRENT ROW
    ), round(
        avg(amount::INT) over (
            order by visited_on::DATE asc RANGE BETWEEN INTERVAL '6' DAY PRECEDING
                AND CURRENT ROW
        ), 2
    ), ROW_NUMBER() OVER (
        order by visited_on asc
    ) as row_number
from Customer

select *
FROM (
        select *, sum(amount::INT) over (
                order by visited_on::DATE asc RANGE BETWEEN INTERVAL '6' DAY PRECEDING
                    AND CURRENT ROW
            ), round(
                avg(amount::INT) over (
                    order by visited_on::DATE asc RANGE BETWEEN INTERVAL '6' DAY PRECEDING
                        AND CURRENT ROW
                ), 2
            ), ROW_NUMBER() OVER (
                order by visited_on asc
            ) as row_number
        from (
                select sum(amount::INT) as amount, visited_on::DATE
                from Customer
                group by
                    visited_on
            )
    )
where
    row_number > 6

SELECT
    -- sum(amount::INT) 
    -- over( order by visited_on::DATE asc RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW)
    -- ,round(avg(amount::INT) 
    -- over( order by visited_on::DATE asc RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW)
    -- ,2)
    visited_on,
    sum(amount::INT) over (
        order by visited_on::DATE asc rows 6 PRECEDING
    ) as amount, round(
        avg(amount::INT) over (
            order by visited_on::DATE asc rows 6 PRECEDING
        ), 2
    ) as average_amount
from (
        select
            visited_on::DATE visited_on, sum(amount::INT) as amount
        from Customer
        group by
            visited_on
        order by visited_on asc
    )
offset 6


SELECT
    visited_on,
    sum(amount::INT) over (
        order by visited_on::DATE asc rows 6 PRECEDING
    ) as amount, round(
        avg(amount::INT) over (
            order by visited_on::DATE asc rows 6 PRECEDING
        ), 2
    ) as average_amount
from (
        select
            visited_on::DATE visited_on, sum(amount::INT) as amount
        from Customer
        group by
            visited_on
        order by visited_on asc
    )
offset 6