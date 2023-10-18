-- This script  lists all shows from hbtn_0d_tvshows_rate by their rating.
USE hbtn_0d_tvshows;

SELECT tv_shows.title, SUM(rating) as rating_sum
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows_rate ON tv_shows.id = tv_shows_rate.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
