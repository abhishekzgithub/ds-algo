--
--create table location ( source_city varchar(255), Destination_city varchar(255), Distance int);
--
--insert into location values
--('Hyderabad', 'Chennai',   700),
--('Chennai',   'Hyderabad', 700),
--('Hyderabad', 'Bangalore', 650),
--('Cochin', 'Bangalore', 650),
--('Hyderabad', 'England', 650),
--('England', 'Hyderabad', 650)

select * from (
select l.source_city
       ,l.destination_city
       ,case when l.source_city < l.destination_city then l.source_city else l.destination_city end as source_col
       ,case when l.source_city > l.destination_city then l.source_city else l.destination_city end as destination_col
       ,row_number() over(partition by case when l.source_city < l.destination_city then l.source_city else l.destination_city end
                                       ,case when l.source_city > l.destination_city then l.source_city else l.destination_city end
                           order by l.source_city) as rnk
from location l
)x
where x.rnk=1


select l.*
from location l
where l.source_city < l.destination_city;

select * from location;
SELECT DISTINCT Distance,
       FIRST_VALUE(source_city) OVER (PARTITION BY Distance) AS source,
       FIRST_VALUE(destination_city) OVER (PARTITION BY Distance) AS destination
FROM location;
