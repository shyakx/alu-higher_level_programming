-- the script that creates a new table
-- if the table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS (
	id INT  DEFAULT 1,
	name VARCHAR(256)
	);
