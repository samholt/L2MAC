import hashlib
import random


class User:
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = self.hash_password(password)
		self.bank_accounts = []
		self.verification_code = None

	def hash_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def authenticate(self, password):
		return self.password == self.hash_password(password)

	def link_bank_account(self, bank_account):
		self.bank_accounts.append(bank_account)

	def create_user(self, data):
		self.name = data['name']
		self.email = data['email']
		self.password = self.hash_password(data['password'])

	def send_verification_code(self):
		self.verification_code = random.randint(100000, 999999)

	def verify(self, code):
		if self.verification_code == code:
			self.verification_code = None
			return True
		return False

	def serialize(self):
		return {
			'name': self.name,
			'email': self.email,
			'password': self.password
		}
