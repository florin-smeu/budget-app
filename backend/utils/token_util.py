from utils.db_util import *
from utils.aes_util import *
import json
import time

TIME_VALID = 300
PASSWORD = 'fancypass'
ENCODING = 'utf-8'

class TokenUtil:


	@staticmethod
	def create_token(token_info):
		encoded_token_info = json.dumps(token_info)
		encrypted_token_info = AESUtil.encrypt(encoded_token_info, PASSWORD)
		hex_token_info = encrypted_token_info.hex()
		return hex_token_info

	@staticmethod
	def read_token(token_info):
		bytes_token_info = bytes.fromhex(token_info)
		decrypted_token_info = AESUtil.decrypt(bytes_token_info, PASSWORD)
		decrypted_token_info = bytes.decode(decrypted_token_info)
		decrypted_token_dict = json.loads(decrypted_token_info)
		return decrypted_token_dict

	@staticmethod
	def validate_token(token):
		if not isinstance(token, dict):
			print("[ERROR] Not a dictionary")
			return False
		if 'email' not in token or 'timestamp' not in token:
			print("[ERROR] Malformed token")
			return False
		if time.time() - token['timestamp'] > TIME_VALID:
			print("[ERROR] Token expired")
			return False

		command = DBUtil.DB_SELECT_USER.format(token['email'])
		records = DBUtil.query_database(command)
		if len(records) == 0:
			return False

		return True
