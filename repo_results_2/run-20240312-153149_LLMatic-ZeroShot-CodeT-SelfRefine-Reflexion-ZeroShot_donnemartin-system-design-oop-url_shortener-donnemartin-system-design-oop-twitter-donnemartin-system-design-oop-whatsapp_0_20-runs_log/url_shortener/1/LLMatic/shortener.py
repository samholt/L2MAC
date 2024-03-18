import string
import random
from urllib.parse import urlparse
from datetime import datetime


class Shortener:
	def __init__(self):
		self.url_map = {}
		self.analytics_map = {}

	def validate_url(self, url):
		try:
			result = urlparse(url)
			return all([result.scheme, result.netloc])
		except ValueError:
			return False

	def generate_short_url(self, url, custom_alias=None, expiration_date=None):
		if not self.validate_url(url) or (custom_alias and custom_alias in self.url_map):
			return None
		if custom_alias:
			self.url_map[custom_alias] = {'url': url, 'expiration_date': expiration_date}
			self.analytics_map[custom_alias] = {'clicks': 0, 'click_data': []}
			return custom_alias
		else:
			short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
			while short_url in self.url_map:
				short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
			self.url_map[short_url] = {'url': url, 'expiration_date': expiration_date}
			self.analytics_map[short_url] = {'clicks': 0, 'click_data': []}
			return short_url

	def get_original_url(self, short_url, ip_address=None):
		url_data = self.url_map.get(short_url, None)
		if url_data is not None:
			if url_data['expiration_date'] is not None and datetime.now() > url_data['expiration_date']:
				return None
			if ip_address is not None:
				self.analytics_map[short_url]['clicks'] += 1
				self.analytics_map[short_url]['click_data'].append({'timestamp': datetime.now().isoformat(), 'ip_address': ip_address})
			return url_data['url']
		return None

	def get_analytics(self, short_url):
		return self.analytics_map.get(short_url, None)
