class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
		self.user_data = {}

	def create_user(self, username, password, email):
		self.user_data[username] = {'password': password, 'email': email}
		return self.user_data[username]

	def update_user(self, username, password=None, email=None):
		if username in self.user_data:
			if password:
				self.user_data[username]['password'] = password
			if email:
				self.user_data[username]['email'] = email
			return self.user_data[username]
		return None

	def delete_user(self, username):
		if username in self.user_data:
			del self.user_data[username]
			return True
		return False
