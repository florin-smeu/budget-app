from flask import Flask, render_template, request
import mysql.connector
import random
import socket

app = Flask(__name__)


config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': 3306,
    'database': 'budget_db',
    'autocommit': True
}

def insert_into_database(insert_command):
	"""Helper function that connects to a database and iserts an entry in 
	it given the insert_command parameter.

	"""
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	cursor.execute(insert_command)
	cursor.close()
	connection.close()


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


""" ############################ UAuth API #############################@  """
@app.route('/sign_in')
def sign_in():
	"""Function that queries the database to see if the sign in data a user 
	provided is valid.

	:returns a relevant string regarding the outcome of the sign in process
	"""
	username = request.args.get('username')
	password_hash = request.args.get('password_hash')
	
	# Check if a username exists in the database for the given password hash
	command = "select * from users where username = '{}' " \
		  "and password_hash = '{}'".format(username, password_hash)
	records = query_database(command)
	
	if len(records) == 0:
		return 'Invalid username or password'
	else:
		return 'Welcome, {}!'.format(username)


@app.route('/sign_up')
def sign_up():
	"""Method that allows a user to sign up.
	
	returns: a relevant string regarding the outcome of the sign up process"""
	username = request.args.get('username')
	password_hash = request.args.get('password_hash')
	
	# Check if a username is already in the database
	command = "select * from users where username = '{}'".format(username)
	records = query_database(command)

	if len(records) != 0:
		return 'Username already in use!'
	else:
		insert_command = "insert into users (username, password_hash)" \
				 "values ('{}', '{}')".format(username, password_hash)
		insert_into_database(insert_command)
		return 'Sign up successful, {}'.format(username)


""" ########################### Expenses API ###########################@  """

def compute_average(records):
	computed_sum = 0
	for i in range(len(records)):
		computed_sum += records[i][3]
	return computed_sum / len(records)


@app.route('/average_daily_expenses')
def average_daily_expenses():
	"""Method that returns the average income sum for a user per day.
	"""
	username = request.args.get('username')

	command = "select * from expenses where username = '{}'".format(username)
	records = query_database(command)
	
	if len(records) != 0:
		average = compute_average(records)
		return "User {} spends daily on average {}".format(username, average) 
	else:
		return 'No data'


@app.route('/average_weekly_expenses')
def average_weekly_expenses():
	return 'No data'

	
@app.route('/average_monthly_expenses')
def average_monthly_expenses():
	return 'No data'


@app.route('/daily_detailed_expenses')
def daily_detailed_expenses():
	"""Method that returns the expenses detailed per day for a user.
	"""
	username = request.args.get('username')
	
	command = "select * from expenses where username = '{}'".format(username)
	
	records = query_database(command)
	
	if len(records) != 0:
		return str(records)
	else:
		return 'No data'


@app.route('/expenses_between_dates')
def expenses_between_dates():
	"""Method that returns the expenses that happened between two dates.
	"""
	date1 = request.args.get('date1')
	date2 = request.args.get('date2')
	username = request.args.get('username')
	
	command = "select * from expenses where username = '{}' AND " \
		  "exp_date between '{}' AND '{}'".format(username, date1, date2)
	records = query_database(command)
	
	if len(records) != 0:
		return str(records)
	else:
		return 'No data'

""" ########################## Incomes API #############################@  """

@app.route('/average_daily_incomes')
def average_daily_incomes():
	"""Method that returns the average income sum for a user per day.
	"""
	username = request.args.get('username')

	command = "select * from incomes where username = '{}'".format(username)
	records = query_database(command)
	
	if len(records) != 0:
		average = compute_average(records)
		return "User {} earns daily on average {}".format(username, average) 
	else:
		return 'No data'


@app.route('/average_weekly_incomes')
def average_weekly_incomes():
	return 'No data'

	
@app.route('/average_monthly_incomes')
def average_monthly_incomes():
	return 'No data'


@app.route('/daily_detailed_incomes')
def daily_detailed_incomes():
	"""Method that returns the incomes detailed per day for a user.
	"""
	username = request.args.get('username')
	
	command = "select * from incomes where username = '{}'".format(username)
	
	records = query_database(command)
	
	if len(records) != 0:
		return str(records)
	else:
		return 'No data'


@app.route('/incomes_between_dates')
def incomes_between_dates():
	"""Method that returns the incomes that happened between two dates.
	"""
	date1 = request.args.get('date1')
	date2 = request.args.get('date2')
	username = request.args.get('username')

	command = "select * from incomes where username = '{}' AND " \
		  "inc_date between '{}' AND '{}'".format(username, date1, date2)
	
	records = query_database(command)
	
	if len(records) != 0:
		return str(records)
	else:
		return 'No data'


@app.route('/')
def root():
	"""Root of the server
	"""
	return 'Budget app server works!'

if __name__ == "__main__":
	app.run(host="0.0.0.0")
