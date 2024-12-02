/*

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
---------------------------

Write a solution to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.

Movies table:
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+
Users table:
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+
MovieRating table:
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  | 
| 2           | 2            | 2            | 2020-02-01  | 
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  | 
| 3           | 2            | 4            | 2020-02-25  | 
+-------------+--------------+--------------+-------------+
Output: 
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+
*/

select 
u.user_id, count(mr.movie_id) as count_movie_id
--u.name, m.title
from Movies m, Users u, MovieRating mr
where mr.movie_id=m.movie_id and mr.user_id=u.user_id
group by u.user_id--, mr.movie_id, mr.rating
--having count_movie_id=max(mr.rating)


/*
Find the movie name with the highest average rating in February 2020. 
In case of a tie, return the lexicographically smaller movie name.
*/

select movie_id
from MovieRating mr
where created_at like '%2020-02%'
group by movie_id
order by avg(rating::int) desc
limit 1


select * from MovieRating;

select mr.user_id as user_id,
count(mr.movie_id) over (partition by mr.user_id) as count_movie
from MovieRating mr

select mr.user_id, count(mr.movie_id)
from MovieRating mr
group by mr.user_id
order by count(movie_id) desc
limit 1

select mr.user_id
from MovieRating mr
group by mr.user_id
order by count(*) desc, mr.user_id