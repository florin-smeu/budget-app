CREATE DATABASE budget_db;
use budget_db;

CREATE TABLE users (
	username VARCHAR(30)
	password_hash CHAR(64)
);

CREATE TABLE expenses_categories (
	id INTEGER, 
	name VARCHAR(40),
);

CREATE TABLE incomes_categories (
	id INTEGER, 
	name VARCHAR(40),
);

CREATE TABLE user_expenses_categories (
	username VARCHAR(30)
	id INTEGER, 
);

CREATE TABLE user_incomes_categories (
	username VARCHAR(30)
	id INTEGER, 
);

CREATE TABLE expenses (
	id INTEGER, 
	expense_date DATE,
	expense_sum FLOAT(10, 7),
	expense_category_id INTEGER,
);

CREATE TABLE incomes (
	id INTEGER, 
	income_date DATE,
	income_sum FLOAT(10, 7),
	income_category_id INTEGER,
);

INSERT INTO users
	(username, password_hash)
VALUES
  ('fsmeu', '41e2cbe589cb11ecdc9c82feb0710ff119fe36c018ab2bd0e93a7009f478a99c'),
  ('user', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8');



