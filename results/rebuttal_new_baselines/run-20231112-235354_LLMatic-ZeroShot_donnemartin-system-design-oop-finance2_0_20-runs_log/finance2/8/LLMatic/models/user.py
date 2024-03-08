import hashlib

# Mock database
users_db = {}

class User:
	def __init__(self, name=None, email=None, password=None):
		self.name = name
		self.email = email
		self.password = hashlib.sha256(password.encode()).hexdigest() if password else None
		self.bank_accounts = []

	@classmethod
	def create_user(cls, name, email, password):
		user = cls(name, email, password)
		users_db[email] = user
		return user

	@classmethod
	def find_by_email(cls, email):
		return users_db.get(email)

	def authenticate(self, email, password):
		return self.email == email and self.password == hashlib.sha256(password.encode()).hexdigest()

	def link_bank_account(self, bank_account):
		self.bank_accounts.append(bank_account)
		return self.bank_accounts
