-- Create Database --
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create DB user --
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- GRANT the created user all access --
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- GRANT SELECT ACCESS--
GRANT SELECT ON performance_schema TO 'hbnb_dev'@'localhost';