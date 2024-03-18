class UserAccounts:
	def __init__(self):
		# Class for managing user accounts
		self.users = {}
		self.sessions = {}

	def create_account(self, username, password):
		# Method to create a new user account
		if username in self.users:
			return False
		self.users[username] = {'password': password, 'urls': []}
		return True

	def login(self, username, password):
		# Method to log in a user
		if username in self.users and self.users[username]['password'] == password:
			self.sessions[username] = True
			return True
		return False

	def logout(self, username):
		# Method to log out a user
		if username in self.sessions:
			del self.sessions[username]
			return True
		return False

	def view_urls(self, username):
		# Method to view the URLs associated with a user account
		if username in self.users:
			return self.users[username]['urls']
		return None
