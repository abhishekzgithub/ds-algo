--SELECT source_city, destination_city, distance
--FROM public."location";

SELECT *
FROM location t1
WHERE NOT EXISTS
 (
   SELECT * FROM location t2
   WHERE t1.destination_city = t2.source_city
     AND t1.source_city = t2.destination_city
     AND t1.destination_city > t2.destination_city
 );

select least(source_city, destination_city), greatest(source_city, destination_city), max(distance)
from location
group by least(source_city, destination_city), greatest(source_city, destination_city);
