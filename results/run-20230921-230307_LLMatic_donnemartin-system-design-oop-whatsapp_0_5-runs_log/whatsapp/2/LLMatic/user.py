from getpass import getpass


class User:
	def __init__(self, email, password):
		self.email = email
		self.password = password

	def sign_up(self):
		self.email = input('Enter your email: ')
		self.password = getpass('Enter your password: ')
		return self

	def log_in(self, email, password):
		if self.email == email and self.password == password:
			return True
		return False

	def recover_password(self):
		self.password = getpass('Enter your new password: ')
		return self
