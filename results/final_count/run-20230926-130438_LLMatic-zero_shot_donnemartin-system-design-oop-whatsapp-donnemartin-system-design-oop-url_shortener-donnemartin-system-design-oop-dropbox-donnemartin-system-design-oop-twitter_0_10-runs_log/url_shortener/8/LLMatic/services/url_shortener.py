import string
import random
from datetime import datetime


class UrlShortener:
	def __init__(self):
		self.url_dict = {}
		self.analytics_dict = {}

	def validate_url(self, url):
		if url.startswith('http://') or url.startswith('https://'):
			return True
		return False

	def generate_short_url(self, url, expiration_date=None, custom_short_url=None):
		if custom_short_url and custom_short_url in self.url_dict:
			return 'Error: This custom short URL is not available'
		short_url = custom_short_url or ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
		while short_url in self.url_dict:
			short_url = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
		self.url_dict[short_url] = {'url': url, 'expiration_date': expiration_date}
		self.analytics_dict[short_url] = {'clicks': 0, 'click_details': []}
		return short_url

	def get_original_url(self, short_url):
		url_data = self.url_dict.get(short_url, None)
		if url_data and url_data['expiration_date'] and datetime.now() > url_data['expiration_date']:
			return 'Error: This URL has expired'
		return url_data['url'] if url_data else None

	def record_click(self, short_url, location):
		if short_url in self.analytics_dict:
			self.analytics_dict[short_url]['clicks'] += 1
			self.analytics_dict[short_url]['click_details'].append({'timestamp': datetime.now().isoformat(), 'location': location})

	def get_analytics(self, short_url):
		return self.analytics_dict.get(short_url, None)
