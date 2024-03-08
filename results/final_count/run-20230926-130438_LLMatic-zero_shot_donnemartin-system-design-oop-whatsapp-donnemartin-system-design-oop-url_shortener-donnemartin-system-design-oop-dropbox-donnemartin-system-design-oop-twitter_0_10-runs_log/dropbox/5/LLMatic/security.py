from cryptography.fernet import Fernet
from datetime import datetime


def generate_key():
	key = Fernet.generate_key()
	return key


def encrypt_file_content(key, content):
	cipher_suite = Fernet(key)
	cipher_text = cipher_suite.encrypt(content)
	return cipher_text


def decrypt_file_content(key, cipher_text):
	cipher_suite = Fernet(key)
	plain_text = cipher_suite.decrypt(cipher_text)
	return plain_text


class Log:
	def __init__(self, user, action):
		self.user = user
		self.action = action
		self.timestamp = datetime.now()


# Mock database
log_db = {}


def add_log_entry(user, action):
	log_entry = Log(user, action)
	if user not in log_db:
		log_db[user] = []
	log_db[user].append(log_entry)
	return log_entry
