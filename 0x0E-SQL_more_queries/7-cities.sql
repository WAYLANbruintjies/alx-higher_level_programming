-- Creates the database hbtn_0d_usa and the table cities in DB 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL FOREIGN KEY, name VARCHAR(256) NOT NULL,
REFERENCES states(id));
