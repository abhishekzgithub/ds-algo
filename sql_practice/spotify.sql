/*
 * https://datalemur.com/questions/top-fans-rank
 */
--select *
--from spotify_artists_songs_global_song_rank 
--where rank<=10
--;

select artist_id,artist_name
from (
select artist_id,artist_name
,dense_rank() over(order by count("song_id.1") desc) as artist_rank
from spotify_artists_songs_global_song_rank 
where rank<=10
group by artist_id,artist_name
) cte
where artist_rank<=5

;




