-- a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement


SELECT s.title, sg.genre_id
FROM tv_shows s LEFT OUTER JOIN tv_show_genres sg
ON s.id = sg.show_id
WHERE sg.genre_id IS NULL;
ORDER BY s.title, sg.genre_id;
