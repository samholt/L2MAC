class User:
	def __init__(self):
		self.users = {}

	def register(self, username, password):
		if username in self.users:
			return False
		self.users[username] = {'password': password, 'urls': {}}
		return True

	def authenticate(self, username, password):
		if username in self.users and self.users[username]['password'] == password:
			return True
		return False

	def add_url(self, username, short_url, original_url):
		if username in self.users:
			self.users[username]['urls'][short_url] = original_url
			return True
		return False

	def get_urls(self, username):
		if username in self.users:
			return self.users[username]['urls']
		return {}

	def edit_url(self, username, short_url, new_url):
		if username in self.users and short_url in self.users[username]['urls']:
			self.users[username]['urls'][short_url] = new_url
			return True
		return False

	def delete_url(self, username, short_url):
		if username in self.users and short_url in self.users[username]['urls']:
			del self.users[username]['urls'][short_url]
			return True
		return False
