-- Create Database --
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create DB user --
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- GRANT the created user all access --
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- GRANT SELECT ACCESS--
GRANT SELECT ON performance_schema TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;