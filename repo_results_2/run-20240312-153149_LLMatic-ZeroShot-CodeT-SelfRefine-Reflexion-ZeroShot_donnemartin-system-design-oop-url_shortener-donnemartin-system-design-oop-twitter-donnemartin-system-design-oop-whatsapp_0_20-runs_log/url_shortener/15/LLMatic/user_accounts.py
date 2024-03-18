class UserAccounts:
	def __init__(self):
		self.users = {}

	def create_account(self, username):
		if username in self.users:
			return 'Username already exists.'
		self.users[username] = {}
		return 'Account created successfully.'

	def view_urls(self, username):
		if username not in self.users:
			return 'Username does not exist.'
		return self.users[username]

	def edit_url(self, username, old_url, new_url):
		if username not in self.users or old_url not in self.users[username].keys():
			return 'Invalid username or URL.'
		self.users[username][new_url] = self.users[username].pop(old_url)
		return 'URL edited successfully.'

	def delete_url(self, username, url):
		if username not in self.users or url not in self.users[username].keys():
			return 'Invalid username or URL.'
		del self.users[username][url]
		return 'URL deleted successfully.'

	def view_analytics(self, username):
		if username not in self.users:
			return 'Username does not exist.'
		return {url: data['clicks'] for url, data in self.users[username].items()}
