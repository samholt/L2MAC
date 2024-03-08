import random
from werkzeug.security import generate_password_hash, check_password_hash

class User:
	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password_hash = self.set_password(password)
		self.bank_account = None
		self.verification_code = None

	def set_password(self, password):
		return generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def link_bank_account(self, bank_account):
		self.bank_account = bank_account
		return self.bank_account

	def generate_verification_code(self):
		self.verification_code = ''.join(random.choices('0123456789', k=6))
		return self.verification_code

	def send_verification_code(self):
		print('Verification code:', self.verification_code)

	def verify(self, code):
		return self.verification_code == code
