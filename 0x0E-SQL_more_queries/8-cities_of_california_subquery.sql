-- script that lists all the cities of California that can be found
-- in the database hbtn_0d_usa.
SELECT id, name FROM cities WHERE states.id IN (
	SELECT id FROM states WHERE name=California
) ORDER BY id;
