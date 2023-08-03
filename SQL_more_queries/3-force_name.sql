-- the script that create a table
-- if the table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
	);
