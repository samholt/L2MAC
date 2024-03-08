import datetime
import hashlib
import random


class URL:
	def __init__(self, original_url, expiry_date=None):
		self.original_url = original_url
		self.short_url = self.generate_short_url()
		self.clicks = 0
		self.expiry_date = expiry_date if expiry_date else datetime.datetime.now() + datetime.timedelta(days=365)

	def generate_short_url(self):
		return hashlib.sha256((self.original_url + str(random.randint(1, 1000000))).encode()).hexdigest()[:6]

	def increment_clicks(self):
		self.clicks += 1

	def is_expired(self):
		return datetime.datetime.now() > self.expiry_date


class URLStore:
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
