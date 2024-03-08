class UserAccount:
	def __init__(self):
		self.accounts = {}

	def create_account(self, username):
		if username in self.accounts:
			return 'Username already exists.'
		else:
			self.accounts[username] = {}
			return 'Account created successfully.'

	def view_urls(self, username):
		if username not in self.accounts:
			return 'Username does not exist.'
		else:
			return self.accounts[username]

	def edit_url(self, username, old_url, new_url):
		if username not in self.accounts:
			return 'Username does not exist.'
		elif old_url not in self.accounts[username]:
			return 'URL does not exist.'
		else:
			self.accounts[username][new_url] = self.accounts[username].pop(old_url)
			return 'URL edited successfully.'

	def delete_url(self, username, url):
		if username not in self.accounts:
			return 'Username does not exist.'
		elif url not in self.accounts[username]:
			return 'URL does not exist.'
		else:
			del self.accounts[username][url]
			return 'URL deleted successfully.'

	def delete_user(self, username):
		if username in self.accounts:
			del self.accounts[username]
			return 'User deleted successfully.'
		else:
			return 'Username does not exist.'
