import mysql.connector
import random
import socket

config = {
	'user': 'root',
	'password': 'root',
	'host': 'db',
	'port': 3306,
	'database': 'budget_db',
	'autocommit': True
}

class DBUtil:
	DB_SELECT_USER = "select * from users where email = '{}'"
	DB_SELECT_USER_PASSWORD = "select * from users where email = '{}' and password_hash = '{}'"
	DB_SAVE_USER = "insert into users (email, password_hash) values ('{}', '{}')"

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
