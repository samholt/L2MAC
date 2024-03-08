import hashlib

class User:
	def __init__(self, name, email, password, bank_accounts=[]):
		self.name = name
		self.email = email
		self.password = hashlib.sha256(password.encode()).hexdigest()
		self.bank_accounts = bank_accounts

	@classmethod
	def create(cls, name, email, password, bank_accounts=[]):
		return cls(name, email, password, bank_accounts)

	def authenticate(self, password):
		return self.password == hashlib.sha256(password.encode()).hexdigest()
