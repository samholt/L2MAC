class UserAccounts:
	def __init__(self):
		self.users = {}

	def create_account(self, username, password):
		if username in self.users:
			return 'Username already exists.'
		self.users[username] = {'password': password, 'urls': []}
		return 'Account created successfully.'

	def view_urls(self, username, password):
		if username not in self.users or self.users[username]['password'] != password:
			return 'Invalid credentials.'
		return self.users[username]['urls']

	def edit_url(self, username, password, old_url, new_url):
		if username not in self.users or self.users[username]['password'] != password:
			return 'Invalid credentials.'
		if old_url not in self.users[username]['urls']:
			return 'URL not found.'
		self.users[username]['urls'].remove(old_url)
		self.users[username]['urls'].append(new_url)
		return 'URL edited successfully.'

	def delete_url(self, username, password, url):
		if username not in self.users or self.users[username]['password'] != password:
			return 'Invalid credentials.'
		if url not in self.users[username]['urls']:
			return 'URL not found.'
		self.users[username]['urls'].remove(url)
		return 'URL deleted successfully.'

	def view_analytics(self, username, password):
		if username not in self.users or self.users[username]['password'] != password:
			return 'Invalid credentials.'
		return self.users[username]['urls']
