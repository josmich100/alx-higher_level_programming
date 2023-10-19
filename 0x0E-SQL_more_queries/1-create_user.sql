-- Check if the user already exists and drop it if it does
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- Create the user with the specified username and password
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
