-- Creates a MySQL server user caled 'user_0d_1' on localhost
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY user_0d_1_pwd;
GRANT ALL PRIVILEGES
ON *.*
TO user_0d_1@localhosit
IDENTIFIED BY user_0d_1_pwd;
