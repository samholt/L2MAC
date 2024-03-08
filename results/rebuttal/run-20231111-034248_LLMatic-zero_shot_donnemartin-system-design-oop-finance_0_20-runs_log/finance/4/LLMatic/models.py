class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.data = {}

	def create_user(self, username, password, email):
		self.data[username] = {'password': password, 'email': email}
		return self.data[username]

	def update_user(self, username, password=None, email=None):
		if username in self.data:
			if password:
				self.data[username]['password'] = password
			if email:
				self.data[username]['email'] = email
			return self.data[username]
		return None

	def delete_user(self, username):
		if username in self.data:
			del self.data[username]
			return True
		return False
