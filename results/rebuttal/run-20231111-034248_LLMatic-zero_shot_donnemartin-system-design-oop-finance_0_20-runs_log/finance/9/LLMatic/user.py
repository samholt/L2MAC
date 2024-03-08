class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email

	def get_username(self):
		return self.username

	def get_email(self):
		return self.email

	def check_password(self, password):
		return self.password == password

class UserManager:
	def __init__(self):
		self.users = {}

	def create_user(self, username, password, email):
		if username not in self.users:
			self.users[username] = User(username, password, email)
			return self.users.get(username)
		return None

	def get_user(self, username):
		return self.users.get(username)
