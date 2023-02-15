-- Converts the entire database hbtn_0c_0 to UTF8.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8MB4 COLLATE utf8MB4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8MB4 COLLATE utf8MB4_unicode_ci;
