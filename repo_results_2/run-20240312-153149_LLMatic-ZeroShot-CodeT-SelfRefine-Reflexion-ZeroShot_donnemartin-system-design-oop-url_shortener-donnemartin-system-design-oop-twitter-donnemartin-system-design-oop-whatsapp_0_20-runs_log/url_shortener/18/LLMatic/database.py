class Database:
	def __init__(self):
		self.users = {}
		self.urls = {}

	def add_user(self, user):
		self.users[user.username] = user

	def get_user(self, username):
		return self.users.get(username, None)

	def delete_user(self, username):
		if username in self.users:
			del self.users[username]
			return True
		return False

	def add_url(self, url):
		self.urls[url.short_url] = url

	def get_url(self, short_url):
		return self.urls.get(short_url, None)

	def delete_url(self, short_url):
		if short_url in self.urls:
			del self.urls[short_url]
			return True
		return False

	def get_original_url(self, short_url):
		url = self.get_url(short_url)
		if url:
			return url.redirect()
		return None
