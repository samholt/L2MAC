class User:
	def __init__(self, username):
		self.username = username
		self.urls = {}

	def create_url(self, original_url, short_url):
		self.urls[short_url] = {'original_url': original_url, 'clicks': 0, 'clicks_data': []}

	def get_urls(self):
		return self.urls

	def edit_url(self, short_url, new_url):
		if short_url in self.urls:
			self.urls[short_url]['original_url'] = new_url

	def delete_url(self, short_url):
		if short_url in self.urls:
			del self.urls[short_url]

	def get_url_analytics(self, short_url):
		if short_url in self.urls:
			return self.urls[short_url]['clicks'], self.urls[short_url]['clicks_data']
