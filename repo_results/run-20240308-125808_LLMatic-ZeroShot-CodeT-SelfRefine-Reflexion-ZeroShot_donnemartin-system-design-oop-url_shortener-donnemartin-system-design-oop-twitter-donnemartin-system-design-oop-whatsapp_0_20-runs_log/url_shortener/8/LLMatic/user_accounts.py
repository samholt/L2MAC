class UserAccount:
	def __init__(self, username):
		self.username = username
		self.urls = {}

	def create_url(self, original_url, shortened_url):
		self.urls[shortened_url] = original_url

	def view_urls(self):
		return self.urls

	def edit_url(self, shortened_url, new_url):
		if shortened_url in self.urls:
			self.urls[shortened_url] = new_url

	def delete_url(self, shortened_url):
		if shortened_url in self.urls:
			del self.urls[shortened_url]

	def view_analytics(self, analytics):
		user_analytics = {}
		for url in self.urls:
			if url in analytics:
				user_analytics[url] = analytics[url]
		return user_analytics
