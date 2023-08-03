-- the script to create a database AND new user
--the user should have only SELECT privilege in this database
-- and also the user will be set to the specific password
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY user_0d_2_pwd;
GRANT SELECT ON hbtn_0d_2 TO user_0d_2@localhost;
