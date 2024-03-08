import hashlib

# Mock database
users_db = {}

class User:
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = hashlib.sha256(password.encode()).hexdigest()
		self.bank_accounts = []

	@classmethod
	def create_user(cls, name, email, password):
		user = cls(name, email, password)
		users_db[email] = user
		return user

	@classmethod
	def authenticate(cls, email, password):
		user = cls.get_user_by_email(email)
		if user and user.password == hashlib.sha256(password.encode()).hexdigest():
			return user
		return None

	def link_bank_account(self, bank_account):
		self.bank_accounts.append(bank_account)
		return self.bank_accounts

	@classmethod
	def get_user_by_email(cls, email):
		return users_db.get(email, None)

	def to_dict(self):
		return {
			'name': self.name,
			'email': self.email,
			'password': self.password,
			'bank_accounts': [bank_account.to_dict() for bank_account in self.bank_accounts]
		}
