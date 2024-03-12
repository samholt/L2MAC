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

	def edit_url(self, username, old_url, new_url):
		if username not in self.accounts:
			return 'Username does not exist.'
		if old_url not in self.accounts[username]['urls']:
			return 'URL does not exist.'
		self.accounts[username]['urls'].remove(old_url)
		self.accounts[username]['urls'].append(new_url)
		return 'URL edited successfully.'

	def delete_url(self, username, url):
		if username not in self.accounts:
			return 'Username does not exist.'
		if url not in self.accounts[username]['urls']:
			return 'URL does not exist.'
		self.accounts[username]['urls'].remove(url)
		return 'URL deleted successfully.'

USER_ACCOUNTS = UserAccount()

