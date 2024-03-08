from werkzeug.security import generate_password_hash, check_password_hash


class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password_hash = generate_password_hash(password)
		self.email = email

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
