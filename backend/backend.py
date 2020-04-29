from flask import Flask, request
from flask_cors import CORS
import mysql.connector
from utils.db_util import *
from utils.aes_util import *
from utils.token_util import *
from utils.http_status import *
import time
import json
import random
import socket


app = Flask(__name__)
CORS(app)

def compute_average(records):
	computed_sum = 0
	for i in range(len(records)):
		computed_sum += records[i][3]
	return computed_sum / len(records)


""" ########################### Expenses API ###########################  """

@app.route('/avg_daily_exp', methods=['GET'])
def average_daily_expenses():
	"""Method that returns the average income sum for a user per day.
	"""
	token_info = request.args.get('token')
	auth_token = TokenUtil.read_token(token_info)
	if not TokenUtil.validate_token(auth_token):
		return {"error": "unauthorized"}, HTTPStatus.UNAUTHORIZED
	email = auth_token['email']

	command = DBUtil.DB_SELECT_EXP.format(email)
	records = DBUtil.query_database(command)

	if len(records) != 0:
		average = compute_average(records)
		return {'email': email, 'average': average}, HTTPStatus.OK
	else:
		return {'email': email, 'average': 'no data'}, HTTPStatus.OK


@app.route('/avg_weekly_exp', methods=['GET'])
def average_weekly_expenses():
	return {'data': 'No data'}, HTTPStatus.OK


@app.route('/avg_monthly_exp', methods=['GET'])
def average_monthly_expenses():
	return {'data': 'No data'}, HTTPStatus.OK


@app.route('/daily_detailed_exp', methods=['GET'])
def daily_detailed_expenses():
	"""Method that returns the expenses detailed per day for a user.
	"""
	token_info = request.args.get('token')
	auth_token = TokenUtil.read_token(token_info)
	if not TokenUtil.validate_token(auth_token):
		return {"error": "unauthorized"}, HTTPStatus.UNAUTHORIZED
	email = auth_token['email']

	command = DBUtil.DB_SELECT_EXP.format(email)
	records = DBUtil.query_database(command)

	if len(records) != 0:
		answer = {}
		for record in records:
			command = DBUtil.DB_SELECT_EXP_CAT.format(record[4])
			exp_cat_records = DBUtil.query_database(command)
			answer[record[0]] = {'date': record[2],
								 'exp_sum': record[3],
								 'exp_cat': exp_cat_records[0][1]}

		return {'email': email, 'records': answer}, HTTPStatus.OK
	else:
		return {'email': email, 'records': 'No data'}, HTTPStatus.OK


@app.route('/exp_between_dates', methods=['GET'])
def expenses_between_dates():
	"""Method that returns the expenses that happened between two dates.
	"""
	token_info = request.args.get('token')
	auth_token = TokenUtil.read_token(token_info)
	if not TokenUtil.validate_token(auth_token):
		return {"error": "unauthorized"}, HTTPStatus.UNAUTHORIZED
	email = auth_token['email']
	date1 = request.args.get('date1')
	date2 = request.args.get('date2')

	command = DBUtil.DB_SELECT_EXP_BETWEEN_DATES.format(email, date1, date2)
	records = DBUtil.query_database(command)

	if len(records) != 0:
		answer = {}
		for record in records:
			command = DBUtil.DB_SELECT_EXP_CAT.format(record[4])
			exp_cat_records = DBUtil.query_database(command)
			answer[record[0]] = {'date': record[2],
								 'exp_sum': record[3],
								 'exp_cat': exp_cat_records[0][1]}

		return {'email': email, 'records': answer}, HTTPStatus.OK
	else:
		return {'email': email, 'records': 'No data'}, HTTPStatus.OK

""" ########################## Incomes API #############################@  """

@app.route('/avg_daily_inc', methods=['GET'])
def average_daily_incomes():
	"""Method that returns the average income sum for a user per day.
	"""
	token_info = request.args.get('token')
	auth_token = TokenUtil.read_token(token_info)
	if not TokenUtil.validate_token(auth_token):
		return {"error": "unauthorized"}, HTTPStatus.UNAUTHORIZED
	email = auth_token['email']

	command = DBUtil.DB_SELECT_INC.format(email)
	records = DBUtil.query_database(command)

	if len(records) != 0:
		average = compute_average(records)
		return {'email': email, 'average': average}, HTTPStatus.OK
	else:
		return {'email': email, 'average': 'no data'}, HTTPStatus.OK



@app.route('/avg_weekly_inc', methods=['GET'])
def average_weekly_incomes():
	return {'data': 'No data'}, HTTPStatus.OK


@app.route('/avg_monthly_inc', methods=['GET'])
def average_monthly_incomes():
	return {'data': 'No data'}, HTTPStatus.OK


@app.route('/daily_detailed_inc', methods=['GET'])
def daily_detailed_incomes():
	"""Method that returns the incomes detailed per day for a user.
	"""
	token_info = request.args.get('token')
	auth_token = TokenUtil.read_token(token_info)
	if not TokenUtil.validate_token(auth_token):
		return {"error": "unauthorized"}, HTTPStatus.UNAUTHORIZED
	email = auth_token['email']

	command = DBUtil.DB_SELECT_INC.format(email)
	records = DBUtil.query_database(command)

	if len(records) != 0:
			answer = {}
			for record in records:
				command = DBUtil.DB_SELECT_INC_CAT.format(record[4])
				inc_cat_records = DBUtil.query_database(command)

				answer[record[0]] = {'date': record[2],
									 'inc_sum': record[3],
									 'inc_cat': inc_cat_records[0][1]}

			return {'email': email, 'records': answer}, HTTPStatus.OK
	else:
		return {'email': email, 'records': 'No data'}, HTTPStatus.OK


@app.route('/inc_between_dates', methods=['GET'])
def incomes_between_dates():
	"""Method that returns the incomes that happened between two dates.
	"""
	token_info = request.args.get('token')
	auth_token = TokenUtil.read_token(token_info)
	if not TokenUtil.validate_token(auth_token):
		return {"error": "unauthorized"}, HTTPStatus.UNAUTHORIZED
	email = auth_token['email']
	date1 = request.args.get('date1')
	date2 = request.args.get('date2')

	command = DBUtil.DB_SELECT_INC_BETWEEN_DATES.format(email, date1, date2)
	records = DBUtil.query_database(command)

	if len(records) != 0:
		answer = {}
		for record in records:
			command = DBUtil.DB_SELECT_INC_CAT.format(record[4])
			inc_cat_records = DBUtil.query_database(command)

			answer[record[0]] = {'date': record[2],
								 'inc_sum': record[3],
								 'inc_cat': inc_cat_records[0][1]}


		return {'email': email, 'records': answer}, HTTPStatus.OK
	else:
		return {'email': email, 'records': 'No data'}, HTTPStatus.OK


@app.route('/')
def root():
	"""Root of the server
	"""
	return {'message': 'Budget app server works!'}, HTTPStatus.OK

if __name__ == "__main__":
	app.run(host="0.0.0.0")
