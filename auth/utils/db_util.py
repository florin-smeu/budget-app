import mysql.connector
import random
import socket

config = {
	'user': 'root',
	'password': 'root',
	'host': 'db',
	'port': 3306,
	'database': 'kubecaf_db',
	'autocommit': True
}

class DBUtil:
	""" Users """
	DB_SELECT_USER = "select * from users where email = '{}'"
	DB_SELECT_USER_PASSWORD = "select * from users where email = '{}' and password_hash = '{}'"
	DB_SAVE_USER = "insert into users (email, password_hash) values ('{}', '{}')"

	""" Expenses """
	DB_SELECT_EXP = "select * from expenses where email = '{}'"
	DB_SELECT_EXP_BETWEEN_DATES = "select * from expenses where email = '{}' AND exp_date between '{}' AND '{}'"

	""" Expense category """
	DB_SELECT_EXP_CAT = "select * from exp_cat where id = {}"

	""" Incomes """
	DB_SELECT_INC = "select * from incomes where email = '{}'"
	DB_SELECT_INC_BETWEEN_DATES = "select * from incomes where email = '{}' AND inc_date between '{}' AND '{}'"

	""" Income category """
	DB_SELECT_INC_CAT = "select * from inc_cat where id = {}"

	@staticmethod
	def insert_into_database(insert_command):
		"""Helper function that connects to a database and iserts an entry in
		it given the insert_command parameter.

		"""
		connection = mysql.connector.connect(**config)
		cursor = connection.cursor()

		cursor.execute(insert_command)
		cursor.close()
		connection.close()

	@staticmethod
	def query_database(command):
		"""Helper function that connects to a database and queries it given the
		command parameter.

		returns: a list of records retrieved from the database
		"""
		connection = mysql.connector.connect(**config)
		cursor = connection.cursor()

		cursor.execute(command)
		records = cursor.fetchall()
		cursor.close()
		connection.close()

		return records
