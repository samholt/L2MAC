class UserAccounts:
	def __init__(self):
		self.users = {}

	def create_account(self, username, password):
		if username in self.users:
			return 'Username already exists.'
		self.users[username] = {'password': password, 'urls': []}
		return 'Account created successfully.'

	def add_url(self, username, password, url):
		if username not in self.users or self.users[username]['password'] != password:
			return 'Invalid credentials.'
		self.users[username]['urls'].append(url)
		return 'URL added successfully.'

	def view_urls(self, username, password):
		if username not in self.users or self.users[username]['password'] != password:
			return 'Invalid credentials.'
		return self.users[username]['urls']

	def delete_url(self, username, password, url):
		if username not in self.users or self.users[username]['password'] != password:
			return 'Invalid credentials.'
		if url in self.users[username]['urls']:
			self.users[username]['urls'].remove(url)
			return 'URL deleted successfully.'
		return 'URL not found.'

	def delete_user(self, username):
		if username in self.users:
			self.users.pop(username, None)
			return 'User account deleted successfully.'
		return 'User not found.'

	def view_analytics(self, username, password):
		if username not in self.users or self.users[username]['password'] != password:
			return 'Invalid credentials.'
		return self.users[username]['urls']

