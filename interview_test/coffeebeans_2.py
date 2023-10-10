"""
covid:
 country, city, person, age, gender, status(positive,recovered,dead),  date, 


	- daily positive cases trend country wise
	- avg recovery rate in days
	- all countries that have a descending curve

    1.
    select country,extract('day' from date),count(status) as positive_cases_trend
    from covid
    where status='positive'
    group by country,extract('day' from date)

    2. how long someone takes to recover from the disease
    with recovered_cte as (select * 
    from covid
    where status='recovered')
    , positive_cte as (
        select * from covid where status='positive'
    )

    select avg(max_recovery_time) from (
    select p.person,extract(day from (min(p.date)-max(r.date))) as max_recovery_time
    from recovered_cte r join positive_cte p on r.person=p.person
    group by p.person, extract(day from min(p.date)-max(r.date))
    ) as cte
    --group by person

    3.


"""