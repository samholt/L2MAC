class UserAccounts:
	def __init__(self):
		self.users = {}

	def register(self, username, password):
		if username in self.users:
			return False
		self.users[username] = {'password': password, 'urls': []}
		return True

	def login(self, username, password):
		if username not in self.users or self.users[username]['password'] != password:
			return False
		return True

	def add_url(self, username, url):
		if username not in self.users:
			return False
		self.users[username]['urls'].append(url)
		return True

	def get_urls(self, username):
		if username not in self.users:
			return None
		return self.users[username]['urls']
