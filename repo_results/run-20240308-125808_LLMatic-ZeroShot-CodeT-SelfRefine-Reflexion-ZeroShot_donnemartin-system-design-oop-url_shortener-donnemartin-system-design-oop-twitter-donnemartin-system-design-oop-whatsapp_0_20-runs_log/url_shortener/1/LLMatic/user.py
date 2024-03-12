from analytics import Analytics

class User:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.urls = {}
		self.analytics = Analytics()

	def create_account(self):
		users[self.username] = self

	def add_url(self, original_url, shortened_url):
		self.urls[shortened_url] = original_url

	def edit_url(self, short_url, new_url):
		if short_url in self.urls:
			self.urls[short_url] = new_url

	def delete_url(self, short_url):
		if short_url in self.urls:
			del self.urls[short_url]

	def view_urls(self):
		return self.urls

	def view_analytics(self, short_url):
		return self.analytics.get_statistics(short_url)

users = {}
