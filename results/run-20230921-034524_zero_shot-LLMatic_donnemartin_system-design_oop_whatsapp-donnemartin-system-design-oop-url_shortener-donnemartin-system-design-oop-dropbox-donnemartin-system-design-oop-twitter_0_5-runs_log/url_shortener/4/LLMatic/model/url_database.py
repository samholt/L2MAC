class URLDatabase:
	def __init__(self):
		self.urls = {}

	def add_url(self, url):
		self.urls[url.short_url] = url

	def get_url(self, short_url):
		return self.urls.get(short_url)

	def delete_expired_urls(self):
		expired_urls = [short_url for short_url, url in self.urls.items() if url.is_expired()]
		for short_url in expired_urls:
			self.urls.pop(short_url)
