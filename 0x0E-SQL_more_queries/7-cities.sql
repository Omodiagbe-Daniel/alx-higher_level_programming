-- create a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create the table cities in the database
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
FOREIGN KEY(state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL);
