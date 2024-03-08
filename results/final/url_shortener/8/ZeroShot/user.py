class User:
	def __init__(self, user_id):
		self.user_id = user_id
		self.urls = []

	def add_url(self, short_url):
		self.urls.append(short_url)

	def get_urls(self):
		return self.urls
