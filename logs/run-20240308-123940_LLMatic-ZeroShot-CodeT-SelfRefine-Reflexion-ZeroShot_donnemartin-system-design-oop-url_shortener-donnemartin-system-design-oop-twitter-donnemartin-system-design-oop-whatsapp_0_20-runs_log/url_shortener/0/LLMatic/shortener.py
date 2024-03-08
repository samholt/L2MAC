import string
import random
from urllib.parse import urlparse
import time
import threading


class Shortener:
	def __init__(self):
		self.url_map = {}
		self.expiry_map = {}

	def validate_url(self, url):
		parsed = urlparse(url)
		return all([parsed.scheme, parsed.netloc])

	def generate_short_url(self, url, custom_alias=None, expiry_time=None):
		if custom_alias:
			short_url = custom_alias
		else:
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
		if short_url in self.url_map:
			return self.generate_short_url(url)
		self.url_map[short_url] = url
		if expiry_time:
			self.expiry_map[short_url] = expiry_time
			threading.Timer(expiry_time - time.time(), self.delete_url, args=[short_url]).start()
		return short_url

	def get_original_url(self, short_url):
		return self.url_map.get(short_url, None)

	def delete_url(self, short_url):
		if short_url in self.url_map:
			del self.url_map[short_url]
		if short_url in self.expiry_map:
			del self.expiry_map[short_url]
