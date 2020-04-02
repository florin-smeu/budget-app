CREATE DATABASE budget_db;
use budget_db;
	
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS exp_cat;
DROP TABLE if exists inc_cat;
drop TABLE if exists expenses;
drop TABLE if exists incomes;
	
CREATE TABLE users (
	username VARCHAR(30),
	password_hash CHAR(64)
);

CREATE TABLE exp_cat (
	id INTEGER, 
	name VARCHAR(40)
);

CREATE TABLE inc_cat (
	id INTEGER, 
	name VARCHAR(40)
);

CREATE TABLE expenses (
	id INTEGER, 
	username VARCHAR(30),
	exp_date DATE,
	exp_sum FLOAT(10, 7),
	exp_cat_id INTEGER
);

CREATE TABLE incomes (
	id INTEGER,
	username VARCHAR(30),
	inc_date DATE,
	inc_sum FLOAT(10, 7),
	inc_cat_id INTEGER
);

