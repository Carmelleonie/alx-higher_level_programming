-- A script that creates the database hbtn_0d_usa and the table cities

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
state_id INT FOREIGN KEY REFERENCES states(id) NOT NULL, 
name VARCHAR(256) NOT NULL);
