class User:
	users = {}

	def __init__(self, user_id, username, password):
		self.user_id = user_id
		self.username = username
		self.password = password
		User.users[username] = self

	def login(self, username, password):
		# Implement login logic here
		if username in User.users and User.users[username].password == password:
			return True
		return False

	def logout(self):
		# Implement logout logic here
		# Since we don't maintain a session, there's nothing to do here
		pass

	def register(self, username, password):
		# Implement registration logic here
		if username not in User.users:
			User.users[username] = User(len(User.users) + 1, username, password)
			return True
		return False
