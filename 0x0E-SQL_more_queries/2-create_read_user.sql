-- create a new user user_0d_2
CREATE USER IF NOT EXISTS user_0d_2@localhost;

-- set password for user
SET PASSWORD FOR user_0d_2@localhost = 'user_0d_2_pwd';

-- create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- grant select permission to user
GRANT SELECT
	ON hbtn_0d_2.*
	TO user_0d_2@localhost;
