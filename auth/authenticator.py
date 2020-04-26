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


""" ############################ UAuth API ############################# """
@app.route('/signin', methods=['POST'])
def sign_in():
	"""Function that queries the database to see if the sign in data a user
	provided is valid.

	:returns a token if the provided params are correct
	"""
	email = request.args.get('email')
	password_hash = request.args.get('password_hash')

	# Check if a username exists in the database for the given password hash
	command = DBUtil.DB_SELECT_USER_PASSWORD.format(email, password_hash)
	records = DBUtil.query_database(command)

	if len(records) == 0:
		return {'token': TokenUtil.INVALID_TOKEN}, HTTPStatus.BAD_REQUEST
	else:
		token_info = {'email': email, 'timestamp': time.time()}
		auth_token = TokenUtil.create_token(token_info)
		return {'token': auth_token}, HTTPStatus.OK


@app.route('/signup', methods=['POST'])
def sign_up():
	"""Method that allows a user to sign up.

	:returns a token if the provided params are correct"""
	email = request.args.get('email')
	password_hash = request.args.get('password_hash')

	# Check if a username is already in the database
	command = DBUtil.DB_SELECT_USER.format(email)
	records = DBUtil.query_database(command)

	if len(records) != 0:
		return {'token': 'INVALID_TOKEN'}, HTTPStatus.BAD_REQUEST
	else:
		insert_command = DBUtil.DB_SAVE_USER.format(email, password_hash)
		DBUtil.insert_into_database(insert_command)
		token_info = {'email': email, 'timestamp': time.time()}
		auth_token = TokenUtil.create_token(token_info)
		return {'token': auth_token}, HTTPStatus.OK

@app.route('/')
def root():
	return {'message': 'Authentication server works!'}, HTTPStatus.OK


if __name__ == "__main__":
	app.run(host="0.0.0.0")
