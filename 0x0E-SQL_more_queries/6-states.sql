-- Creates a database 'hbtn_0d_usa' and a table 'states' (in DB hbtn_0d_usa) in MySQL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256)NOT NULL);
