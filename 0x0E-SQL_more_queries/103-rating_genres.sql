-- This script  lists all genres in the database hbtn_0d_tvshows_rate by their rating.
USE hbtn_0d_tvshows;

SELECT tv_genres.name, SUM(rating) as rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows_rate ON tv_show_genres.show_id = tv_shows_rate.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
