class UserAccounts:
	def __init__(self):
		self.users = {}

	def register(self, username, password):
		if username in self.users:
			return False
		self.users[username] = {'password': password, 'urls': []}
		return True

	def login(self, username, password):
		if username in self.users and self.users[username]['password'] == password:
			return True
		return False

	def add_url(self, username, url):
		if username in self.users:
			self.users[username]['urls'].append(url)
			return True
		return False

	def get_urls(self, username):
		if username in self.users:
			return self.users[username]['urls']
		return None

	def delete_url(self, username, url):
		if username in self.users and url in self.users[username]['urls']:
			self.users[username]['urls'].remove(url)
			return True
		return False

	def delete_user(self, username):
		if username in self.users:
			del self.users[username]
			return True
		return False
