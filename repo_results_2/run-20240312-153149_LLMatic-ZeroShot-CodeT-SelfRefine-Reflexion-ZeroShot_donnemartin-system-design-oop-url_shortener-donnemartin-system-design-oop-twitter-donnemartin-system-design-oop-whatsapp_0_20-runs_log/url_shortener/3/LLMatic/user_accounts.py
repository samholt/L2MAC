class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = {}

	@staticmethod
	def register(username, password):
		if username not in users:
			users[username] = User(username, password)
			return True
		return False

	@staticmethod
	def login(username, password):
		if username in users and users[username].password == password:
			return True
		return False

	@staticmethod
	def add_url(username, short_url, long_url):
		if username in users:
			users[username].urls[short_url] = long_url
			return True
		return False

	@staticmethod
	def view_urls(username):
		if username in users:
			return users[username].urls
		return None

	@staticmethod
	def edit_url(username, short_url, new_long_url):
		if username in users and short_url in users[username].urls:
			users[username].urls[short_url] = new_long_url
			return True
		return False

	@staticmethod
	def delete_url(username, short_url):
		if username in users and short_url in users[username].urls:
			del users[username].urls[short_url]
			return True
		return False

	# Admin functions
	@staticmethod
	def view_all_urls():
		all_urls = {}
		for username, user in users.items():
			all_urls[username] = user.urls
		return all_urls

	@staticmethod
	def delete_user(username):
		if username in users:
			del users[username]
			return True
		return False

users = {}

# Initialize a test user
User.register('test', 'password')
User.add_url('test', 'short', 'long')
