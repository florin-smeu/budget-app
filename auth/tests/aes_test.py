from utils.aes_util import *
import json
import time

password = 'fancypass'

def create_token(token_info):
	encoded_token_info = json.dumps(token_info)
	print("encoded_token_info", encoded_token_info)

	encrypted_token_info = AESUtil.encrypt(encoded_token_info, password)
	print("encrypted_token_info", encrypted_token_info)

	hex_token_info = encrypted_token_info.hex()
	print("hex_create", hex_token_info)

	return hex_token_info


def read_token(token_info):
	#encoded_token_info = token_info.encode('ascii')
	encoded_token_info = bytes.fromhex(token_info)

	decrypted_token_info = AESUtil.decrypt(encoded_token_info, password)
	decrypted_token_info = bytes.decode(decrypted_token_info)
	decrypted_token_dict = json.loads(decrypted_token_info)
	return decrypted_token_dict

def main():

	token_info = {'email': 'fsmeu@gmail.com', 'timestamp': time.time()}
	created_token = create_token(token_info)
	print({'token': created_token})

	deciphered_token = read_token(created_token)
	print(deciphered_token)


if __name__ == "__main__":
	main()
