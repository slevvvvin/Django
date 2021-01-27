CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON test_my_db.* TO 'django_user'@'%';
