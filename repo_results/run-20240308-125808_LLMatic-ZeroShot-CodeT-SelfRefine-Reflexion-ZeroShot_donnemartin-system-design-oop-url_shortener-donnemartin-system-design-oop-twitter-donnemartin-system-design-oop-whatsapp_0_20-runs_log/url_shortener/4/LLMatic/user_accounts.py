class UserAccounts:
	def __init__(self):
		self.users = {}

	def create_account(self, username):
		if username in self.users:
			return 'Username already exists.'
		self.users[username] = []
		return 'Account created successfully.'

	def get_urls(self, username):
		if username not in self.users:
			return 'Username does not exist.'
		return self.users[username]

	def add_url(self, username, url):
		if username not in self.users:
			return 'Username does not exist.'
		self.users[username].append(url)
		return 'URL added successfully.'

	def edit_url(self, username, old_url, new_url):
		if username not in self.users:
			return 'Username does not exist.'
		if old_url not in self.users[username]:
			return 'URL does not exist.'
		self.users[username].remove(old_url)
		self.users[username].append(new_url)
		return 'URL edited successfully.'

	def delete_url(self, username, url):
		if username not in self.users:
			return 'Username does not exist.'
		if url not in self.users[username]:
			return 'URL does not exist.'
		self.users[username].remove(url)
		return 'URL deleted successfully.'

	def delete_user(self, username):
		if username not in self.users:
			return 'Username does not exist.'
		del self.users[username]
		return 'User deleted successfully.'
