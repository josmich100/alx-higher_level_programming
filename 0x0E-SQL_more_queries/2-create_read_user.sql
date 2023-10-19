-- Check if the database already exists and create it if it doesn't
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user already exists and create it if it doesn't
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the database hbtn_0d_2 to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
