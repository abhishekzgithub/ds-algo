select max(agg_revenue)
--,agg_table.item
from(

SELECT sum(revenue) as agg_revenue
,extract('month' from created_at) as d
,item
FROM public.amazon_transactions
group by extract('month' from created_at),item
order by sum(revenue) desc

) as agg_table
--group by item
;

create table candidates (candidate_id integer,skill varchar)

insert into candidates (candidate_id, skill)
values
(123, 'Python'),
(123, 'Tableau'),
(123, 'PostgreSQL'),
(124, 'Python'),
(124, 'Tableau'),
(124, 'PostgreSQL'),
(124, 'MSBI'),
(125, 'PostgreSQL')

update candidates set skill='Python' where candidate_id=125

delete from candidates where candidate_id=124 and skill='Python'

select candidate_id from candidates 
where skill in ('Python','Tableau','PostgreSQL')

group by candidate_id
having count(skill)=6

with cte_python as (

select * from candidates where skill='Python'
),
cte_tableau as (
select * from candidates where skill='Tableau'
),
cte_pgres as (
select * from candidates where skill='PostgreSQL'
)

select c.candidate_id from candidates c
join cte_python cp on c.candidate_id=cp.candidate_id
join cte_tableau ct on c.candidate_id=ct.candidate_id
join cte_pgres cps on c.candidate_id=cps.candidate_id

group by c.candidate_id


