-- list all cities of california found in the database
SELECT id, name
FROM cities WHERE state_id IN
	(SELECT id FROM states WHERE name = 'california')
ORDER BY id ASC;
