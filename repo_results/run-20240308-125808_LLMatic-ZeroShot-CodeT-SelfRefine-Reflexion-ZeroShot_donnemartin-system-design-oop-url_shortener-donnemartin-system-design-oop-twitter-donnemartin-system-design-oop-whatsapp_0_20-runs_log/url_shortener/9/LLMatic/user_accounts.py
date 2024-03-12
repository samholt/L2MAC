class UserAccounts:
	def __init__(self):
		self.users = {}

	def create_account(self, username):
		if username in self.users:
			return 'Username already exists.'
		self.users[username] = []
		return 'Account created successfully.'

	def view_urls(self, username):
		if username not in self.users:
			return 'Username does not exist.'
		return self.users[username]

	def add_url(self, username, url):
		if username not in self.users:
			return 'Username does not exist.'
		self.users[username].append(url)
		return 'URL added successfully.'

	def delete_url(self, username, url):
		if username not in self.users:
			return 'Username does not exist.'
		if url not in self.users[username]:
			return 'URL does not exist.'
		self.users[username].remove(url)
		return 'URL removed successfully.'
