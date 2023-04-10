-- A script that lists all the cities of California that can be found in the database hbtn_0d_usa.

SELECT id state_id name
FROM cities
where states.name = California
ORDER BY state_id ASC;
