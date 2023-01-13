-- SQL Script that creates a table
-- Called Users with a lot of requirements
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	country ENUM("US", "CO", "TN") NOT NULL DEFAULT "US",
	PRIMARY KEY (id)
)
