from werkzeug.security import generate_password_hash, check_password_hash

users_db = {}

class User:
	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
