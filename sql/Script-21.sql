SELECT passengerid, survived, pclass, "name", sex, age, sibsp, parch, ticket, fare, cabin, embarked
FROM public.titanic
where age =26
;

select percentile_cont(0.75) within group (order by age asc)
from titanic t 

select survived
,sum(case when pclass=1 then 1 else 0 end) as first_class
,sum(case when pclass=2 then 1 else 0 end ) as second_class
,sum(case when pclass=3 then 1 else 0 end ) as second_class

from titanic t 
group by survived

select survived
,(case when pclass=1 then 1 else 0 end) as first_class
,(case when pclass=2 then 1 else 0 end ) as second_class
,(case when pclass=3 then 1 else 0 end ) as second_class

from titanic t 
--group by survived

