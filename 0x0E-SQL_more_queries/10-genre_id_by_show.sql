-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT s.title, sg.genre_id FROM tv_show_genres sg
INNER JOIN tv_shows s
ON s.id = sg.show_id
ORDER BY s.title, sg.genre_id;
