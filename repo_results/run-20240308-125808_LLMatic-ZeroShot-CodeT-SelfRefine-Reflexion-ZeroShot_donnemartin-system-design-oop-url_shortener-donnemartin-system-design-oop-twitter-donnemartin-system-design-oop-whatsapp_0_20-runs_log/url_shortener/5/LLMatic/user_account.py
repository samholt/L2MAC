class UserAccount:
	def __init__(self):
		self.accounts = {}

	def create_account(self, username, password):
		if username in self.accounts:
			return 'Username already exists'
		self.accounts[username] = {'password': password, 'urls': [], 'analytics': {}}
		return 'Account created successfully'

	def view_urls(self, username):
		if username not in self.accounts:
			return 'Username does not exist'
		return self.accounts[username]['urls']

	def edit_url(self, username, old_url, new_url):
		if username not in self.accounts:
			return 'Username does not exist'
		if old_url not in self.accounts[username]['urls']:
			return 'URL does not exist'
		self.accounts[username]['urls'].remove(old_url)
		self.accounts[username]['urls'].append(new_url)
		return 'URL edited successfully'

	def delete_url(self, username, url):
		if username not in self.accounts:
			return 'Username does not exist'
		if url not in self.accounts[username]['urls']:
			return 'URL does not exist'
		self.accounts[username]['urls'].remove(url)
		return 'URL deleted successfully'

	def view_analytics(self, username):
		if username not in self.accounts:
			return 'Username does not exist'
		return self.accounts[username]['analytics']

	def delete_user(self, username):
		if username not in self.accounts:
			return 'Username does not exist'
		del self.accounts[username]
		return 'User deleted successfully'

	def get_all_users(self):
		return self.accounts
