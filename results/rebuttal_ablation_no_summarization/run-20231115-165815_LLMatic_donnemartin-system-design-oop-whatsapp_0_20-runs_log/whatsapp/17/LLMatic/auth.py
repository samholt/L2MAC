class Auth:
	def __init__(self):
		self.users = {}

	def signup(self, username, password):
		if username in self.users:
			return False
		self.users[username] = password
		return True

	def validate_user(self, username, password):
		if username in self.users and self.users[username] == password:
			return True
		return False
