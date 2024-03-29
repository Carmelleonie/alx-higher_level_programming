-- A script that creates the database hbtn_0d_usa and the table cities

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
state_id INT NOT NULL FOREIGN KEY REFERENCES states(id), 
name VARCHAR(256) NOT NULL);
