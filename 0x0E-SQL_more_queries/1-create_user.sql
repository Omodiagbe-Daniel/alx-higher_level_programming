--  creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS user_0d_1@localhost;

-- sets the password for user
SET PASSWORD FOR user_0d_1@localhost = 'user_0d_1_pwd';

-- grants all privileges to the user
GRANT ALL PRIVILEGES
	ON *.*
	TO user_0d_1@localhost;
