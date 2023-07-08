CREATE DATABASE nifty_db;

CREATE USER nifty_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE nifty_db TO nifty_admin;