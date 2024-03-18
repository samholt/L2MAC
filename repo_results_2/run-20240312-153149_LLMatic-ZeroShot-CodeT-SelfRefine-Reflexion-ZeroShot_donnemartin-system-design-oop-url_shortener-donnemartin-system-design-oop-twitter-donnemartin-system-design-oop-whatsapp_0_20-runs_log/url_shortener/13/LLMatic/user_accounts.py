class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = {}

	def add_url(self, original_url, shortened_url):
		self.urls[shortened_url] = original_url

	def get_url(self, shortened_url):
		return self.urls.get(shortened_url)

	def delete_url(self, shortened_url):
		if shortened_url in self.urls:
			del self.urls[shortened_url]

	def update_url(self, shortened_url, new_url):
		if shortened_url in self.urls:
			self.urls[shortened_url] = new_url

class UserAccounts:
	def __init__(self):
		self.users = {}

	def register(self, username, password):
		if username not in self.users:
			self.users[username] = User(username, password)
			return True
		return False

	def login(self, username, password):
		user = self.users.get(username)
		if user and user.password == password:
			return True
		return False

	def get_user(self, username):
		return self.users.get(username)

	def delete_user(self, username):
		if username in self.users:
			del self.users[username]
			return True
		return False
