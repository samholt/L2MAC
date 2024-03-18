class UserAccounts:
	def __init__(self):
		self.users = {}

	def register(self, username, password):
		if username in self.users:
			return 'Username already exists'
		self.users[username] = {'password': password, 'urls': []}
		return 'User registered successfully'

	def login(self, username, password):
		if username not in self.users or self.users[username]['password'] != password:
			return 'Invalid username or password'
		return 'Logged in successfully'

	def add_url(self, username, url):
		if username not in self.users:
			return 'User not found'
		self.users[username]['urls'].append(url)
		return 'URL added successfully'

	def view_urls(self, username):
		if username not in self.users:
			return 'User not found'
		return self.users[username]['urls']

	def edit_url(self, username, old_url, new_url):
		if username not in self.users:
			return 'User not found'
		if old_url not in self.users[username]['urls']:
			return 'URL not found'
		self.users[username]['urls'].remove(old_url)
		self.users[username]['urls'].append(new_url)
		return 'URL edited successfully'

	def delete_url(self, username, url):
		if username not in self.users:
			return 'User not found'
		if url not in self.users[username]['urls']:
			return 'URL not found'
		self.users[username]['urls'].remove(url)
		return 'URL deleted successfully'

	def delete_user(self, username):
		if username in self.users:
			del self.users[username]
			return 'User deleted successfully'
		return 'User not found'
