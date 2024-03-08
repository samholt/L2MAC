class UserAccounts:
	def __init__(self):
		# Initialize user accounts
		self.accounts = {}

	def create_account(self, username):
		# Create a user account
		if username in self.accounts:
			return 'Username already exists'
		self.accounts[username] = {}
		return 'Account created successfully'

	def add_url(self, username, short_url, original_url):
		# Add a URL to a user account
		if username not in self.accounts:
			return 'Username does not exist'
		self.accounts[username][short_url] = original_url
		return 'URL added successfully'

	def view_urls(self, username):
		# View URLs of a user account
		if username not in self.accounts:
			return 'Username does not exist'
		return self.accounts[username]

	def edit_url(self, username, short_url, new_url):
		# Edit a URL of a user account
		if username not in self.accounts or short_url not in self.accounts[username]:
			return 'URL does not exist'
		self.accounts[username][short_url] = new_url
		return 'URL edited successfully'

	def delete_url(self, username, short_url):
		# Delete a URL of a user account
		if username not in self.accounts or short_url not in self.accounts[username]:
			return 'URL does not exist'
		self.accounts[username].pop(short_url)
		return 'URL deleted successfully'

	def delete_account(self, username):
		# Delete a user account
		if username in self.accounts:
			self.accounts.pop(username)
			return 'Account deleted successfully'
		return 'Username does not exist'

