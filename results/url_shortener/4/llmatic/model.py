import datetime
from typing import Dict


class URL:
	def __init__(self, long_url: str, short_url: str, custom_url: str = None):
		self.long_url = long_url
		self.short_url = short_url
		self.custom_url = custom_url
		self.click_count = 0
		self.expiration_date = datetime.datetime.now() + datetime.timedelta(days=30)

	def increment_click_count(self):
		self.click_count += 1


class URLDatabase:
	def __init__(self):
		self.urls: Dict[str, URL] = {}

	def add_url(self, url: URL):
		self.urls[url.short_url] = url

	def get_url(self, short_url: str) -> URL:
		return self.urls.get(short_url)

	def update_click_count(self, short_url: str):
		url = self.get_url(short_url)
		if url:
			url.increment_click_count()

	def delete_expired_urls(self):
		current_time = datetime.datetime.now()
		self.urls = {short_url: url for short_url, url in self.urls.items() if url.expiration_date > current_time}
