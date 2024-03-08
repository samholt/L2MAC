class UserAccount:
	def __init__(self):
		self.accounts = {}

	def create_account(self, username, password):
		if username in self.accounts:
			return 'Username already exists.'
		self.accounts[username] = {'password': password, 'urls': []}
		return 'Account created successfully.'

	def view_urls(self, username):
		if username not in self.accounts:
			return 'Username does not exist.'
		return self.accounts[username]['urls']

	def add_url(self, username, url):
		if username not in self.accounts:
			return 'Username does not exist.'
		self.accounts[username]['urls'].append(url)
		return 'URL added successfully.'

	def delete_url(self, username, url):
		if username not in self.accounts:
			return 'Username does not exist.'
		if url not in self.accounts[username]['urls']:
			return 'URL does not exist.'
		self.accounts[username]['urls'].remove(url)
		return 'URL removed successfully.'

	def delete_account(self, username):
		if username in self.accounts:
			del self.accounts[username]
			return 'Account deleted successfully.'
		else:
			return 'Username does not exist.'

	def get_all_users(self):
		return list(self.accounts.keys())
