class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = {}

	def create_account(self, users_db):
		if not self.username or not self.password:
			return {'error': 'Invalid username or password'}
		if self.username in users_db:
			return {'error': 'Username already exists'}
		else:
			users_db[self.username] = self
			return 'Account created successfully'

	def view_urls(self):
		return self.urls

	def edit_url(self, old_url, new_url):
		if old_url in self.urls:
			self.urls[new_url] = self.urls.pop(old_url)
			return 'URL edited successfully'
		else:
			return {'error': 'URL not found'}

	def delete_url(self, url):
		if url in self.urls:
			del self.urls[url]
			return 'URL deleted successfully'
		else:
			return {'error': 'URL not found'}

	def view_analytics(self):
		analytics = {}
		for url in self.urls:
			analytics[url] = self.urls[url].get_analytics(url)
		return analytics
