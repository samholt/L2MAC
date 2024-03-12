class User:
	def __init__(self, username):
		self.username = username
		self.urls = {}

	def create_account(self):
		return {'username': self.username, 'urls': self.urls}

	def add_url(self, short_url, original_url):
		self.urls[short_url] = original_url
		return self.urls

	def view_urls(self):
		return self.urls

	def edit_url(self, short_url, new_url):
		if short_url in self.urls:
			self.urls[short_url] = new_url
		return self.urls

	def delete_url(self, short_url):
		if short_url in self.urls:
			del self.urls[short_url]
		return self.urls

	def view_analytics(self, analytics):
		user_analytics = {}
		for url in self.urls:
			user_analytics[url] = analytics.retrieve(url)
		return user_analytics
