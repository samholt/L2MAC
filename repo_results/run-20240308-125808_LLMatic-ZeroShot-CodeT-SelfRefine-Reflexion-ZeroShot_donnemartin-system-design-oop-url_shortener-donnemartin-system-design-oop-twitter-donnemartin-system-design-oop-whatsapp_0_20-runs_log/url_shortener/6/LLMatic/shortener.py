import string
import random
from urllib.parse import urlparse
from datetime import datetime


class Shortener:
	def __init__(self):
		self.url_mapping = {}
		self.clicks = {}
		self.click_details = {}
		self.expirations = {}

	def generate_short_url(self, original_url):
		short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
		self.url_mapping[short_url] = original_url
		self.clicks[short_url] = 0
		self.click_details[short_url] = []
		return short_url

	def validate_url(self, url):
		parsed = urlparse(url)
		return all([parsed.scheme, parsed.netloc])

	def get_original_url(self, short_url):
		return self.url_mapping.get(short_url, None)

	def record_click(self, short_url, location):
		if short_url in self.clicks:
			self.clicks[short_url] += 1
			self.click_details[short_url].append({'time': datetime.now().isoformat(), 'location': location})
		else:
			return 'URL not found', 404

	def get_clicks(self, short_url):
		return self.clicks.get(short_url, 0)

	def get_click_details(self, short_url):
		return self.click_details.get(short_url, [])

	def set_expiration(self, short_url, expiration_datetime):
		if short_url in self.url_mapping:
			self.expirations[short_url] = expiration_datetime
		else:
			return 'URL not found', 404

	def get_expiration(self, short_url):
		return self.expirations.get(short_url, None)
