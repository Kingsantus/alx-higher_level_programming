-- This script converts hbtn_0c_0 database to UTF8
-- first line of code Select database
-- second line of code Convert database to utf8mb4 character set
-- third line of code Convert each table in database to utf
-- fourth line of code Convert field in first_table table to UTF

USE hbtn_0c_0;

ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
