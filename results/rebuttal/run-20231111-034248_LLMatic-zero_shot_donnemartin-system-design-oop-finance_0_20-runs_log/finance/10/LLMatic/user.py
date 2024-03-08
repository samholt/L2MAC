import hashlib


class User:
	def __init__(self):
		self.users = {}

	def create_user(self, username, password):
		if username in self.users:
			return 'Username already exists'
		else:
			self.users[username] = hashlib.sha256(password.encode()).hexdigest()
			return 'User created successfully'

	def login(self, username, password):
		if username not in self.users:
			return 'Username does not exist'
		elif self.users[username] != hashlib.sha256(password.encode()).hexdigest():
			return 'Incorrect password'
		else:
			return 'Login successful'

	def password_recovery(self, username):
		if username not in self.users:
			return 'Username does not exist'
		else:
			return 'Password recovery email sent'
